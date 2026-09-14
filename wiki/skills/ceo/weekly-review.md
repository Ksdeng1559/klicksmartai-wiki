# Weekly Review Agent

This agent facilitates a structured 15-minute CEO check-in designed to replace unfocused anxiety with operational clarity.

## Key Functions

**Business Context Integration:** The agent first checks for a `BUSINESS_CONTEXT.md` file to ground discussions in actual quarterly priorities and metrics. If missing, it guides setup before proceeding.

**Six-Section Framework:**
1. **Scorecard** — Track 3-5 essential metrics with trend analysis
2. **Wins** — Deliberately surface successes to counter problem-bias
3. **Losses & Lessons** — Extract actionable insights from setbacks
4. **Priority Check** — Measure progress against quarterly goals
5. **Next Week's Focus** — Distill to exactly three priorities with clear "done" definitions
6. **Energy Check** — Monitor founder wellbeing as a leading indicator

## Design Philosophy

The approach emphasizes conversational flow over questionnaires and enforces constraints that fight common founder behaviors: "Three priorities, not thirteen" and mandatory win-naming prevent both overwhelm and burnout patterns.

Continuity tracking through previous review files identifies recurring issues as systemic signals rather than isolated incidents. As the prompt notes, "one bad week is noise. Three bad weeks is a signal."

## Output

Reviews generate a clean markdown document saved to `reviews/weekly-review-[YYYY-MM-DD].md`, creating an auditable operating rhythm that compounds through consistency rather than intensity.
