# vault-analytics

A Python CLI, run against my Obsidian vault, with three commands:
`stats` (notes per unit, line counts, tag distribution), `check`
(dead wikilinks, orphan notes, unused attachments), and `flashcards`
(extract FAQ/SUCCESS callout pairs into a CSV importable by Anki).
Single user: me. Runs locally.

**Out of v0.1:** GUI, watch mode, spaced-repetition scheduling,
editing notes in place, config files, packaging to PyPI.

## Usage

    python vault.py stats --vault /path/to/vault

## Status

- [x] Milestone 1 — walking skeleton (`stats` counts real notes)
- [ ] Milestone 2 — parser core (frontmatter/wikilinks/callouts + pytest)
- [ ] Milestone 3 — `check` command
- [ ] Milestone 4 — `flashcards` command
- [ ] Milestone 5 — ship v0.1

---
**Next session:** extract parsing into `parser.py`, add pytest with 3 fixture notes.