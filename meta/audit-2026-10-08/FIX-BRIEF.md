# Fix brief — apply the 2026-10-08 audit to your cluster's pages

Repo: `C:/Users/User/ict-knowledge-library`. Your audit report: `meta/audit-2026-10-08/<cluster>.md` (named in your prompt).
Read `AGENTS.md` (conventions), `TEMPLATE.md`, and your report in full before editing.

## What to do
Apply EVERY finding in your report to the pages it covers (WRONG, MINOR-FIXES, and the small notes on SOUND pages):
- **CONTRADICTED** → rewrite the claim to what ICT says, with the quote.
- **EMBELLISHED** (invented numbers/thresholds/rules) → remove. If a formula block depended on it, replace with
  `# ICT gives no number for this` or the number ICT does give. Do not keep invented numbers as "heuristics".
- **ERA-SPLIT** → state both, each with its quote and era (2016-17 vs 2022). Do not collapse.
- **NOT IN CORPUS / UNVERIFIABLE** → keep the content only if it is clearly labelled as unverified, set
  `ICT Confidence: medium` (or `disputed` if the corpus contradicts it), and record on-page the searched population
  ("searched 153 2016-17/2020 packets + 41 2022 Mentorship episodes for '<terms>': 0 hits").
- **SMC terms** (CHoCH, BOS, "fresh", close-back-inside, etc.): never present them as ICT's. Keep as `Aliases`
  tagged `(SMC)` and say on-page "not ICT's term — 0 hits in either corpus". Do not delete or rename pages.
- **Year Introduced / Year Refined** → correct where the report shows a different year (header AND JSON).
- **Citations**: replace stub Source IDs with the real ones the evidence comes from. Real IDs:
  - 2016-17/2020/2021 packets: `C:/Users/User/AppData/Local/Temp/claude/C--Users-User/013404bc-24f8-4bbb-8821-2ef6d66f5d15/scratchpad/packet_map.tsv`
    (folder → youtube id → Source ID).
  - 2022 Mentorship: `ICT-2022-MENTORSHIP-EP01` … `EP41` (now in SOURCES.md; captions in `meta/audit-2026-10-08/m22-captions/`).
  You MAY keep a stub ID if it still supports something on the page, but every definitional claim must rest on a real one.
- **Confidence**: `high` only if the page's definitional claims are all quote-backed after your edit.

## Quotes
Every quote you add must be verbatim from `raw/*/report.md` or `m22-captions/ep*.txt`, short, with `[mm:ss]`, and
findable by grep. Copy from the audit report only after grepping it yourself. Auto-captions have spelling errors —
quote as-is, clarify in [brackets].

## Format invariants (lint enforces)
10 sections, 7 top-matter fields, valid JSON with `id` = filename; header `**Source IDs:**` == JSON `sources[]`;
every Source ID appears in `## Citations`; JSON `year_introduced` == header; links resolve.
Run `python tools/lint.py` at the end — it must report `problems: 0`.

## Scope (hard)
- Edit ONLY the pages listed in your prompt. Do NOT edit SOURCES.md, INDEX.md, TIMELINE.md, GLOSSARY.md, log.md,
  README, any other page, or tools/. Do NOT run git. Do NOT reference the owner's trading engines or projects
  (library scope rule). No web. Do NOT run any trading/MT5/alert script or kill processes.
- If a fix needs a change outside your pages (another page contradicts yours, INDEX one-liner now wrong,
  TIMELINE placement), list it in your hand-back instead.

## Hand-back (final message)
1. Pages edited, and per page 1–3 lines on what changed.
2. Year Introduced changes: `page: old → new` (the lead moves TIMELINE entries).
3. INDEX.md / GLOSSARY one-liners that are now wrong (quote the line, give the replacement).
4. Cross-page conflicts left for other owners.
5. Lint output tail. Anything from the report you did NOT apply, and why.
