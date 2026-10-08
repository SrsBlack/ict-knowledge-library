# Review brief — check the rewritten pages (READ-ONLY)

You are the review gate for pages a writer just rewrote from an audit report. You did not write them. Be adversarial.
Repo: `C:/Users/User/ict-knowledge-library`. See each page's change with `git diff -- <page>` (read-only git is fine).
Inputs: the audit report `meta/audit-2026-10-08/<cluster>.md`, the fix brief `meta/audit-2026-10-08/FIX-BRIEF.md`,
the corpora `raw/*/report.md` (2016-17/2020/2021 Whisper transcripts) and `meta/audit-2026-10-08/m22-captions/ep*.txt`
(2022 Mentorship auto-captions). Source-ID → packet map: `C:/Users/User/AppData/Local/Temp/claude/C--Users-User/013404bc-24f8-4bbb-8821-2ef6d66f5d15/scratchpad/packet_map.tsv`.
A mechanical checker found these cited quotes NOT verbatim in either corpus (decide for each: ASR/punctuation-trivial,
paraphrase passed off as a quote, or fabricated):
`C:/Users/User/AppData/Local/Temp/claude/C--Users-User/013404bc-24f8-4bbb-8821-2ef6d66f5d15/scratchpad/quote_misses.txt`.

## Check, per page
1. Every audit finding for the page was applied, and applied correctly (not over-corrected the other way).
2. Every definitional claim on the page is now backed by a real quote (grep it yourself) or explicitly labelled
   unverified/ICT-gives-no-number. Flag ANY new specific claim (number, time, rule, "ICT says") the writer added that is
   not in the audit report and not quote-backed — writers can invent while fixing.
3. Quotes: verbatim, timestamp roughly right (±1 min), cited Source ID actually is the packet/episode the quote is in.
4. Era-splits stated faithfully (2016-17 vs 2022), not collapsed, not one era silently picked.
5. Year Introduced / Year Refined consistent with the evidence; header == JSON.
6. SMC terms presented as SMC, not ICT. No references to the owner's trading engine/projects (library scope rule).
7. Internal consistency: Definition, Formal Criteria, Formula, Examples, Common Mistakes agree with each other.

## Output
Write `meta/audit-2026-10-08/review-<cluster>.md`:
```
| page | PASS / FIX | issue count |
## <page>
- [FIX|NOTE] <issue> — evidence: "<quote>" (<packet|epNN> [mm:ss]) — required change: <exact instruction>
```
Only FIX items that are errors (wrong, unsupported, mis-cited). Style nits → NOTE, at most 3 per page.
Hard rules: edit nothing except your review file; no git writes; no web; no trading/MT5/alert scripts; no process kills.
Final message: path + counts (PASS/FIX pages, FIX items) + the single most serious remaining error.
