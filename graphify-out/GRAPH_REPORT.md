# Graph Report - wiki  (2026-08-05)

## Corpus Check
- 4 files · ~1,546,550 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 33 nodes · 42 edges · 6 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]

## God Nodes (most connected - your core abstractions)
1. `make_fill()` - 5 edges
2. `thin_border()` - 5 edges
3. `value_cell()` - 4 edges
4. `input_label_value()` - 4 edges
5. `header_row()` - 3 edges
6. `data_row()` - 3 edges
7. `label_cell()` - 3 edges
8. `calculate_rlv()` - 3 edges
9. `sensitivity_table()` - 3 edges
10. `section_header()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `label_cell()` --calls--> `thin_border()`  [EXTRACTED]
  drafts/build_rlv_model.py → drafts/build_rlv_model.py  _Bridges community 2 → community 3_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.2
Nodes (1): Residual Land Value Excel Model Garrett Health District Residences - New Westmin

### Community 1 - "Community 1"
Cohesion: 0.36
Nodes (5): api_calculate(), api_sensitivity(), calculate_rlv(), Garrett Health District — Web App Flask app serving the DOM + interactive RLV ca, sensitivity_table()

### Community 2 - "Community 2"
Cohesion: 0.47
Nodes (6): data_row(), header_row(), make_fill(), section_header(), thin_border(), value_cell()

### Community 3 - "Community 3"
Cohesion: 0.67
Nodes (3): input_label_value(), label_cell(), Write a label + yellow input cell pair

### Community 4 - "Community 4"
Cohesion: 1.0
Nodes (2): Calculate residual land value for given cap rate and construction cost, sensitivity_land_value()

### Community 5 - "Community 5"
Cohesion: 1.0
Nodes (2): calc_model(), Calculate residual land value.     height_premium: multiplier on construction co

## Knowledge Gaps
- **5 isolated node(s):** `Residual Land Value Excel Model Garrett Health District Residences - New Westmin`, `Write a label + yellow input cell pair`, `Calculate residual land value.     height_premium: multiplier on construction co`, `Calculate residual land value for given cap rate and construction cost`, `Garrett Health District — Web App Flask app serving the DOM + interactive RLV ca`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 0`** (10 nodes): `bold_font()`, `bottom_border()`, `net_after_tax()`, `normal_font()`, `Residual Land Value Excel Model Garrett Health District Residences - New Westmin`, `set_currency()`, `set_decimal()`, `set_number()`, `set_pct()`, `build_rlv_model.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 4`** (2 nodes): `Calculate residual land value for given cap rate and construction cost`, `sensitivity_land_value()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 5`** (2 nodes): `calc_model()`, `Calculate residual land value.     height_premium: multiplier on construction co`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `input_label_value()` connect `Community 3` to `Community 0`, `Community 2`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Why does `calc_model()` connect `Community 5` to `Community 0`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Why does `sensitivity_land_value()` connect `Community 4` to `Community 0`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **What connects `Residual Land Value Excel Model Garrett Health District Residences - New Westmin`, `Write a label + yellow input cell pair`, `Calculate residual land value.     height_premium: multiplier on construction co` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._