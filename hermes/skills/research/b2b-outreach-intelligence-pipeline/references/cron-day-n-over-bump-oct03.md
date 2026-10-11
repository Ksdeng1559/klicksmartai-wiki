# Day-N over-bump reference (Oct 3 2026 third instance, fire-3 correction surface)

## Pattern

The Aug 21 2026 07:02Z and Sep 24 2026 19:03Z entries in the
`b2b-outreach-intelligence-pipeline` SKILL.md document the **same-day Day-N
over-bump bug** — afternoon crons copy morning's Day-N value verbatim
instead of re-deriving live, then add an unprincipled +1, producing a stale
queue that drifts +1 per occurrence. Both entries document the
**morning-of-new-UTC-day** catch mechanism (a two-comparison rule).

This reference documents the **fire-3-of-same-UTC-day** catch mechanism, a
different and more frequent correction surface.

## Verified case: Oct 3 2026 13:05Z (fire 3, late-afternoon canonical)

The Oct 3 cron ran three fires in a single UTC day:
- Fire 1 (morning, 01:29Z) — wrote `outreach-briefing.2026-10-03.md` with R25 = Day 164 (anchor 2026-04-23, recomputed live).
- Fire 2 (afternoon, 07:04Z) — wrote `outreach-briefing.2026-10-03-afternoon.md` with R25 = Day 165 (anchor `2026-05-22` in the table — internally inconsistent: (Oct 3 - May 22).days + 1 = 135, not 165).
- Fire 3 (late-afternoon, 13:05Z) — wrote `outreach-briefing.2026-10-03-late-afternoon.md` with R25 = Day 164 (anchor 2026-04-23, live recompute against canonical anchor).

The afternoon file's R25 = 165 = morning's 164 + 1 (the over-bump). The
afternoon's anchor `2026-05-22` was a non-canonical placeholder that does
not back-compute to 165 either — the bug is at TWO levels: (a) wrong
anchor, (b) over-bump +1. Fire 3 caught both via live re-derive.

## The dual-correction-surface insight

The same-day over-bump safety net has TWO correction surfaces, both required:

1. **Morning-of-new-UTC-day cron** (Aug 21 + Sep 24 entries) — runs the
   `(a) (Sep N morning) vs (Sep N-1 morning) should be +1, AND
   (b) (Sep N morning) vs (Sep N-1 afternoon) should also be +1`
   comparison. If (a) is +1 but (b) is 0, the prior afternoon over-bumped.
   New morning is correct; over-bumped afternoon file is preserved as audit
   evidence. The Aug 21 entry is the canonical reference for this surface.

2. **Fire-3-of-same-UTC-day cron** (this entry, Oct 3 verified) — runs
   `day_n_live.py` against canonical anchor in Notes, cross-checks against
   fire-2 afternoon value. If fire-3 live matches morning but differs from
   afternoon, afternoon over-bumped, fire-3's live value is canonical for
   the rest of the UTC day. The morning file's value is the original
   truth. The afternoon file is preserved as audit evidence (no
   retroactive write per Aug 21 rule).

Future cron agents reading only the Aug 21 / Sep 24 entries will know to
check the morning of new UTC day, but will not know to also check fire 3
of the SAME UTC day when the cron runs ≥3 fires. Fire-3 catch is the
missing surface.

## When each surface applies

| Cron cadence on a UTC day | Catch surface |
|---|---|
| 1 fire | None — over-bump is impossible (no same-day reference to over-bump from). |
| 2 fires (morning + afternoon) | Morning-of-next-UTC-day (a)+(b) two-comparison rule. |
| ≥3 fires (morning + afternoon + late-afternoon, etc.) | Fire-3 live re-derive within the same UTC day, AND morning-of-next-UTC-day (a)+(b) two-comparison rule. |

When ≥3 fires occur, BOTH surfaces are active. Fire-3 catches the bug
within the same UTC day; morning-of-next-UTC-day verifies the carry
forward was clean.

## Failure mode avoided

Without the fire-3 surface, the over-bump persists into next-UTC-day
morning as a Day-N drift of +1. The morning-of-new-UTC-day cron MAY catch
it (Sep 24 silent persistence case) or may not catch it (if fire-3 of the
prior day had corrected it forward and the carry-in matches the new
morning's recompute). When the morning catches it, the owner sees a
spurious "over-bump detected" message in the next-UTC-day briefing with
no apparent cause. When the morning does not catch it, the cron corpus
accumulates a permanent +1 offset that compounds over time — every
afternoon cron introduces a new +1, the next-morning cron verifies, and
the corpus drifts.

The fire-3 surface is the EARLIEST catch — within the same UTC day, before
the bug propagates to next-UTC-day morning. This keeps the corpus clean
and prevents compounding.

## Implementation pattern (verified working, Oct 3 13:05Z)

```python
# /tmp/cron_{date}/day_n_live_v3.py
import json
from datetime import datetime, timezone, timedelta

# Load sheet data
rows = ...  # from scan_sheet.py
NOTES_COL = ...  # index from header

# For each stale-queue row, extract canonical anchor from Notes
# (look for "HITL Presented: YES | Refresh proposed {date}" pattern)
import re
ANCHOR_RE = re.compile(r'Refresh proposed (\d{4}-\d{2}-\d{2})')

# Compute Day-N live
today = datetime.now(timezone.utc).date()
live_day_n = {}
for i, row in enumerate(rows[1:], start=2):
    if len(row) > NOTES_COL:
        m = ANCHOR_RE.search(row[NOTES_COL])
        if m:
            anchor = datetime.fromisoformat(m.group(1)).date()
            delta = (today - anchor).days
            live_day_n[f'R{i}'] = 1 + delta

# Cross-check against afternoon file
afternoon_day_n = load_afternoon_file()  # from prior fire
over_bumps = []
for rid, live in live_day_n.items():
    afternoon = afternoon_day_n.get(rid)
    if afternoon is not None and live != afternoon:
        over_bumps.append((rid, afternoon, live, 'same-day over-bump'))

# If over-bumps detected, fire-3 value is canonical
if over_bumps:
    print(f'Detected {len(over_bumps)} same-day over-bumps in afternoon file:')
    for rid, afternoon, live, reason in over_bumps:
        print(f'  {rid}: afternoon={afternoon} -> fire-3-live={live} ({reason})')
    print('Fire-3 values are canonical for the rest of this UTC day.')
```

The script outputs the cross-check table directly into the briefing's
stale-queue section. The morning file's value is the original truth; the
afternoon file is audit evidence; the fire-3 file is the corrected
canonical. The Oct 3 13:05Z briefing carried this exact format in
section 1 ("Day-N over-bump correction (R25)").

## Oct 4 morning carry-forward check (predicted)

The Oct 4 morning cron should see R25 = 164 in fire-3 of Oct 3 (canonical)
and recompute R25 = 165 against canonical anchor 2026-04-23 (1 day later
than Oct 3). The +1 increment is correct, the +1 matches what afternoon
wrongly reported on Oct 3 (165). The two errors (afternoon's over-bump +
fire-3's correct value carrying into Oct 4 morning) happen to converge at
the same number on Oct 4, masking the bug. The Oct 4 morning will NOT see
a "carry-forward drift" warning because its recompute matches the
over-bumped afternoon's value by coincidence. This is why the fire-3
catch is the only reliable safety net for the over-bump class.

## Documented instances (3 total as of 2026-10-03)

1. **Aug 21 2026 07:02Z afternoon cron** — Veritas R88-90 Day 11, R31 Day 78, R32/33 Day 111 (verified working: 13:00Z late-afternoon fire caught it via live recompute).
2. **Sep 24 2026 19:03Z afternoon cron** — R6 R11 R25 R31 R32 R33 (verified persistent: no fire-3 catch surface, drift persisted into Sep 25 morning).
3. **Oct 3 2026 13:05Z late-afternoon cron** — R25 only (this reference; verified working: fire-3 caught it via live recompute against canonical anchor).

The 3/3 instances are afternoon fires. The 2/3 instances with fire-3 catch
succeeded. The 1/3 instance without fire-3 catch (Sep 24) persisted into
next-UTC-day. The pattern: **afternoon fires are the over-bump source,
fire-3 is the catch, morning-of-next-UTC-day is the verification.** When
the cron runs ≥3 fires in a UTC day, fire-3 catches it; when it runs
≤2 fires, only morning-of-next-UTC-day can catch it, and the bug may
persist if the morning's recompute happens to match the over-bumped
value (Sep 24 case).

## Skill-library hygiene

This reference file was created in lieu of patching
`b2b-outreach-intelligence-pipeline/SKILL.md` directly because the SKILL.md
is over the 100K character limit (158,278 chars as of 2026-10-03). Future
maintenance: keep the SKILL.md entry at a 2-3 sentence summary pointing
to this reference file, not the full case writeup. Detailed case writeups
belong in this reference (or in dated `references/cron-day-n-over-bump-{date}.md`
files following the Sep 24 naming convention).
