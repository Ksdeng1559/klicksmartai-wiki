# Obsidian — Self-Organizing Vault

**Source:** [XDA Developers — "I set up my Obsidian vault to organize itself"](https://www.xda-developers.com/set-up-obsidian-vault-to-organize-itself-havent-touched-folder-structure-in-weeks/)  
**Author:** Nolen Jonker · Published Apr 18, 2026

---

## Core Problem

Manual folder organization breaks down when notes accumulate faster than you can sort them. The friction of filing notes kills actual use. The solution is to eliminate manual routing entirely — set up the rules once, let plugins handle the rest.

---

## Three-Layer System

### Layer 1 — QuickAdd (Community Plugin)

**Use:** Create new notes with intentional structure from the start.

- Install QuickAdd community plugin
- Create a **Template choice** command
- Point it at a pre-made template file
- Assign it to a specific destination folder
- Name the command (e.g., "New Article Draft")
- Command appears in command palette
- Every use: prompts for title → creates note from template → drops directly in the right folder

**Key insight:** The note isn't just in the right place, it's already set up for something. This kills the "ghost note" problem — half-formed ideas that never get finished. When creating a new note requires a tiny bit of intentionality, you stop spinning up blank notes you'll abandon.

---

### Layer 2 — Auto Note Mover (Community Plugin)

**Use:** Sort existing notes and notes created outside QuickAdd.

- Install Auto Note Mover community plugin
- Add a rule: pick destination folder + set a trigger tag
- Example: tag `#design` → note moves to `/notes/design/`
- Set trigger to **Automatic** — plugin watches in the background
- The moment you tag a note, it moves itself

**⚠️ Caveat:** Tags are **case-sensitive**. `#design` and `#Design` are different rules. Use this to your advantage:
- `#design` → Auto Note Mover trigger (moves the file)
- `#Design` → Obsidian tag for filtering/browsing

---

### Layer 3 — Claude via Filesystem Connector (AI Delegation)

**Use:** Deep clean of an already-messy vault.

- Connect Claude directly to the Obsidian vault via filesystem access
- Delegate: renaming notes, moving files, creating folders, sorting through the existing mess
- More powerful than the plugins but not automatic — like handing off a deep clean to something that can handle the scale

**Author's setup:** QuickAdd + Auto Note Mover handle ongoing organization. Claude handles periodic deep cleans. Result: "vault feels like something I actually want to use every day."

---

## The Ghost Note Problem

Obsidian lets you start a note for anything — a half-formed idea, a title you don't want to forget, an outline that never became an outline. The problem: vault fills with untitled notes and single-sentence drafts you'll never finish.

**QuickAdd's fix:** Templates baked into the creation process. Every new note starts with structure, so it has a purpose from birth.

---

## Author's Result

> "The setup took maybe half an hour total, most of which was just deciding on folder structure and tag naming. Two plugins, configured once."

---

## Key Plugins

| Plugin | Purpose |
|--------|---------|
| **QuickAdd** | Structured note creation → places note in correct folder with template |
| **Auto Note Mover** | Watches for tags → auto-moves notes to destination folders |

---

## Related

- [[obsidian]] — Vault location and configuration
- [[about-this-wiki]] — How Dennis's wiki is structured
