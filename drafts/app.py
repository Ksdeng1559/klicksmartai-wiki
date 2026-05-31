"""
Garrett Health District — Web App
Flask app serving the DOM + interactive RLV calculator
"""

import os
import math
from flask import Flask, render_template, request, jsonify, send_file
from openpyxl import load_workbook
from io import BytesIO

app = Flask(__name__)
APP_DIR = os.path.dirname(os.path.abspath(__file__))
XLSX_PATH = os.path.join(APP_DIR, "garrett-health-district-residences-rlv.xlsx")

# ── RLV Calculator Core ─────────────────────────────────────────────────────

def calculate_rlv(
    lot_sqft=15000,
    fsr=3.0,
    storeys=6,
    construction_cost=430,
    avg_rent=2100,
    cap_rate=5.75,
    dcl_per_sqft=5.00,     # after partial waiver
    op_cost_per_sqft=9.50,
    vacancy_rate=0.02,
    gross_up=1.18,
    unit_size=700,
    parking_per_unit=0.4,
    parking_cost=35000,
    ae_pct=0.08,
    pm_pct=0.03,
    marketing_pct=0.02,
    legal=150000,
    permit_fees=12,
    interest_rate=0.065,
    interest_months=18,
    dev_profit_pct=0.15,
    financing_fee_pct=0.01,
):
    # Gross floor area
    net_area = lot_sqft * fsr
    gross_area = net_area * gross_up

    # Units
    unit_count = max(1, int(gross_area / unit_size))

    # Revenue
    gross_rent = unit_count * avg_rent * 12
    vacancy_loss = gross_rent * vacancy_rate
    effective_rent = gross_rent - vacancy_loss
    operating_costs = net_area * op_cost_per_sqft
    noi = effective_rent - operating_costs

    # Cap rate valuation (GDV)
    gdv = noi / (cap_rate / 100) if cap_rate > 0 else 0

    # Construction
    construction_cost_total = gross_area * construction_cost
    parking_spaces = max(0, int(unit_count * parking_per_unit))
    parking_total = parking_spaces * parking_cost
    hard_costs = construction_cost_total + parking_total

    # Soft costs
    ae = hard_costs * ae_pct
    pm = hard_costs * pm_pct
    marketing = gdv * marketing_pct
    dcl = net_area * dcl_per_sqft
    permits = net_area * permit_fees
    soft_costs = ae + pm + marketing + legal + dcl + permits

    # Financing
    interest_reserve = (hard_costs + soft_costs) * interest_rate * (interest_months / 12)
    fin_fee = gdv * financing_fee_pct
    financing = interest_reserve + fin_fee

    # Developer profit
    dev_profit = gdv * dev_profit_pct

    # Total cost
    total_cost = hard_costs + soft_costs + financing + dev_profit

    # Residual land value
    rlv = gdv - total_cost

    # Profitability
    profit_per_unit = dev_profit / unit_count if unit_count > 0 else 0
    dev_yield = dev_profit / total_cost if total_cost > 0 else 0
    breakeven_cap = (noi / (gdv + dev_profit)) * 100 if (gdv + dev_profit) > 0 else 0

    return {
        "unit_count": unit_count,
        "net_area": round(net_area),
        "gross_area": round(gross_area),
        "parking_spaces": parking_spaces,
        "gross_rent_yr": round(gross_rent),
        "noi": round(noi),
        "gdv": round(gdv),
        "hard_costs": round(hard_costs),
        "construction_cost": round(construction_cost_total),
        "parking_total": round(parking_total),
        "soft_costs": round(soft_costs),
        "ae": round(ae),
        "pm": round(pm),
        "marketing": round(marketing),
        "dcl": round(dcl),
        "permits": round(permits),
        "legal": legal,
        "financing": round(financing),
        "interest_reserve": round(interest_reserve),
        "fin_fee": round(fin_fee),
        "dev_profit": round(dev_profit),
        "total_cost": round(total_cost),
        "rlv": round(rlv),
        "profit_per_unit": round(profit_per_unit),
        "dev_yield": round(dev_yield * 100, 1),
        "breakeven_cap": round(breakeven_cap, 2),
    }


def sensitivity_table(
    lot_sqft=15000, fsr=3.0, storeys=6, construction_cost=430,
    avg_rent=2100, dcl_per_sqft=5.0, cap_rates=None, constr_costs=None
):
    if cap_rates is None:
        cap_rates = [5.0, 5.25, 5.5, 5.75, 6.0, 6.5]
    if constr_costs is None:
        constr_costs = [400, 415, 430, 445, 460, 475]

    rows = []
    for cr in constr_costs:
        row = {"construction_cost": cr}
        for cap in cap_rates:
            r = calculate_rlv(
                lot_sqft=lot_sqft, fsr=fsr, storeys=storeys,
                construction_cost=cr, avg_rent=avg_rent, cap_rate=cap,
                dcl_per_sqft=dcl_per_sqft
            )
            row[f"cap_{cap}"] = r["rlv"]
        rows.append(row)
    return rows, cap_rates


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/calculate", methods=["POST"])
def api_calculate():
    data = request.get_json() or {}
    result = calculate_rlv(
        lot_sqft=float(data.get("lot_sqft", 15000)),
        fsr=float(data.get("fsr", 3.0)),
        storeys=int(data.get("storeys", 6)),
        construction_cost=float(data.get("construction_cost", 430)),
        avg_rent=float(data.get("avg_rent", 2100)),
        cap_rate=float(data.get("cap_rate", 5.75)),
        dcl_per_sqft=float(data.get("dcl_per_sqft", 5.0)),
    )
    return jsonify(result)

@app.route("/api/sensitivity", methods=["POST"])
def api_sensitivity():
    data = request.get_json() or {}
    rows, cap_rates = sensitivity_table(
        lot_sqft=float(data.get("lot_sqft", 15000)),
        fsr=float(data.get("fsr", 3.0)),
        storeys=int(data.get("storeys", 6)),
        construction_cost=float(data.get("construction_cost", 430)),
        avg_rent=float(data.get("avg_rent", 2100)),
        dcl_per_sqft=float(data.get("dcl_per_sqft", 5.0)),
    )
    return jsonify({"rows": rows, "cap_rates": cap_rates})

@app.route("/download/xlsx")
def download_xlsx():
    if not os.path.exists(XLSX_PATH):
        return "File not found", 404
    return send_file(
        XLSX_PATH,
        as_attachment=True,
        download_name="garrett-health-district-residences-rlv.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
