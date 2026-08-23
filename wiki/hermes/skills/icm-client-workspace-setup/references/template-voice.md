# Voice — <client_name>

## Audience

<List the principal audience for this client's deliverables: developer, investor, county official, internal team, etc.>

## Tone
- **Direct and structured.** Lead with the answer, then evidence.
- **Data-cited, evidence-led.** Every claim carries a URL or source reference. Reproducible.
- **Professional, [industry]-appropriate register.** No hype, no buzzwords, no inflated claims.
- **Conservative on numbers.** Never invent market size, yields, or demographics. If a figure isn't in a source, say "unknown — needs verification" rather than guessing.

## Do
- Use tables for multi-item data (deliverables, contact lists, county stats).
- Inline-cite external claims: `[source](url)` or `(source: url)`.
- Mark any relationship assumption with `[VALIDATE: <contact>]` so the HITL gate catches it.
- Keep sentences short. Use section headers.

## Don't
- Don't write marketing fluff or superlatives ("best-in-class", "revolutionary").
- Don't assert a person's role, intent, or commitment without a source or a `[VALIDATE]` marker.
- Don't touch securities language without reading `_config/compliance.md` first (if present).

## Examples

**Good:**
```
The development at <address> includes <components>.
[source: owner-provided site plan render, <date>]
```

**Bad:**
```
This is the best opportunity in <region> — guaranteed returns.
```
(No source. Potentially securities-touching. Unverifiable.)
