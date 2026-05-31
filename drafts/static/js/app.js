/* Garrett Health District — RLV Calculator JS */

function fmt(n) {
  if (n === null || n === undefined || isNaN(n)) return '—';
  const abs = Math.abs(n);
  if (abs >= 1_000_000) return '$' + (n / 1_000_000).toFixed(2) + 'M';
  if (abs >= 1_000) return '$' + (n / 1_000).toFixed(0) + 'K';
  return '$' + n.toFixed(0);
}

function fmtUnits(n) {
  if (!n && n !== 0) return '—';
  return n.toLocaleString() + ' units';
}

function fmtCap(n) {
  if (!n && n !== 0) return '—';
  return n.toFixed(2) + '%';
}

function rlvClass(val) {
  if (!val && val !== 0) return 'neutral';
  if (val > 0) return 'positive';
  if (val < -2_000_000) return 'negative';
  if (val < 0) return 'negative';
  return 'positive';
}

function rlvColor(val) {
  if (!val && val !== 0) return 'neutral';
  return val > 0 ? 'positive' : 'negative';
}

// ── Calculate ──────────────────────────────────────────────────────────────────

document.getElementById('btn-calculate').addEventListener('click', runCalculate);

async function runCalculate() {
  const btn = document.getElementById('btn-calculate');
  btn.textContent = 'Calculating…';
  btn.disabled = true;

  const payload = {
    lot_sqft:          parseFloat(document.getElementById('i_lot_sqft').value) || 15000,
    fsr:               parseFloat(document.getElementById('i_fsr').value) || 3.0,
    storeys:           parseInt(document.getElementById('i_storeys').value) || 6,
    construction_cost: parseFloat(document.getElementById('i_construction_cost').value) || 430,
    avg_rent:          parseFloat(document.getElementById('i_avg_rent').value) || 2100,
    cap_rate:          parseFloat(document.getElementById('i_cap_rate').value) || 5.75,
    dcl_per_sqft:      parseFloat(document.getElementById('i_dcl').value) || 5.0,
  };

  try {
    const [calcRes, sensRes] = await Promise.all([
      fetch('/api/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      }).then(r => r.json()),
      fetch('/api/sensitivity', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      }).then(r => r.json()),
    ]);

    renderResults(calcRes);
    renderSensitivity(sensRes, payload.cap_rate, payload.construction_cost);

    document.getElementById('result-placeholder').style.display = 'none';
    document.getElementById('result-output').style.display = 'block';
    document.getElementById('sensitivity-output').style.display = 'block';
  } catch (err) {
    console.error('Calculation error:', err);
    alert('Error running calculation. Check console.');
  } finally {
    btn.textContent = 'Calculate';
    btn.disabled = false;
  }
}

function renderResults(r) {
  // Programme
  document.getElementById('r_gross_area').textContent = r.gross_area.toLocaleString() + ' sqft';
  document.getElementById('r_unit_count').textContent = fmtUnits(r.unit_count);
  document.getElementById('r_parking').textContent = r.parking_spaces + ' spaces';

  // Revenue
  document.getElementById('r_gdv').textContent = fmt(r.gdv);
  document.getElementById('r_noi').textContent = fmt(r.noi);

  // Costs
  document.getElementById('r_construction').textContent = fmt(r.construction_cost);
  document.getElementById('r_parking_cost').textContent = fmt(r.parking_total);
  document.getElementById('r_hard_costs').textContent = fmt(r.hard_costs);
  document.getElementById('r_ae').textContent = fmt(r.ae);
  document.getElementById('r_pm').textContent = fmt(r.pm);
  document.getElementById('r_marketing').textContent = fmt(r.marketing);
  document.getElementById('r_dcl').textContent = fmt(r.dcl);
  document.getElementById('r_permits').textContent = fmt(r.permits);
  document.getElementById('r_legal').textContent = fmt(r.legal);
  document.getElementById('r_soft_costs').textContent = fmt(r.soft_costs);
  document.getElementById('r_interest').textContent = fmt(r.interest_reserve);
  document.getElementById('r_fin_fee').textContent = fmt(r.fin_fee);
  document.getElementById('r_financing').textContent = fmt(r.financing);
  document.getElementById('r_dev_profit').textContent = fmt(r.dev_profit);
  document.getElementById('r_total_cost').textContent = fmt(r.total_cost);

  // RLV
  const rlvVal = r.rlv;
  const rlvEl = document.getElementById('r_rlv');
  const rlvBox = document.getElementById('rlv-box');
  const cls = rlvClass(rlvVal);
  rlvEl.textContent = fmt(rlvVal);
  rlvBox.className = 'rlv-box ' + cls;
  document.getElementById('r_rlv_per_unit').textContent =
    '($' + (rlvVal / r.unit_count).toFixed(0) + ' per unit land budget)';

  // KPIs
  document.getElementById('r_profit_unit').textContent = fmt(r.profit_per_unit);
  document.getElementById('r_dev_yield').textContent = r.dev_yield + '%';
  document.getElementById('r_breakeven').textContent = r.breakeven_cap + '%';
}

function renderSensitivity(data, baseCap, baseConstr) {
  const { rows, cap_rates } = data;
  const capRates = cap_rates || [5.0, 5.25, 5.5, 5.75, 6.0, 6.5];

  let html = `<table class="sens-table"><thead><tr><th>Const. $/sqft</th>`;
  capRates.forEach(cap => {
    const highlight = Math.abs(cap - baseCap) < 0.01 ? '★ ' : '';
    html += `<th>${highlight}${cap.toFixed(2)}%</th>`;
  });
  html += `</tr></thead><tbody>`;

  rows.forEach(row => {
    const constr = row.construction_cost;
    const baseRow = Math.abs(constr - baseConstr) < 1;
    html += `<tr><td>$${constr}/sqft</td>`;
    capRates.forEach(cap => {
      const key = `cap_${cap}`;
      const val = row[key];
      const cls = rlvColor(val);
      const base = Math.abs(cap - baseCap) < 0.01 && baseRow ? ' base-case' : '';
      const sign = val > 0 ? '+' : '';
      html += `<td class="${cls}${base}">${sign}${(val / 1_000_000).toFixed(2)}M</td>`;
    });
    html += `</tr>`;
  });

  html += `</tbody></table>`;
  document.getElementById('sensitivity-table').innerHTML = html;
}

// Run on load with defaults
window.addEventListener('load', () => {
  // Auto-calculate on first load
  setTimeout(runCalculate, 300);
});

// Scroll spy for nav
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => {
    const rect = s.getBoundingClientRect();
    if (rect.top <= 80) current = s.getAttribute('id');
  });
  document.querySelectorAll('.nav-links a').forEach(a => {
    a.style.opacity = a.getAttribute('href') === `#${current}` ? '1' : '0.7';
  });
});
