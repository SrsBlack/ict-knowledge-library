# verify-index — review of the lead's INDEX.md / GLOSSARY.md / TIMELINE.md edits (2026-10-08)

Scope: every hunk in `git diff -- INDEX.md GLOSSARY.md TIMELINE.md` checked against the concept
page it summarises (Definition + Formal Criteria + header fields), plus a pass over the
UNCHANGED INDEX/GLOSSARY lines for definitions the rewritten pages now contradict.

Method: read-only. Pages read in full for the 43 INDEX hunks, 17 GLOSSARY hunks and the 32
TIMELINE re-dates; `**Year Introduced**` of every TIMELINE-touched stem (incl. the links left in
place) listed and compared.

## Verdict

- **Changed lines:** 42 of 43 INDEX one-liners and 17 of 17 GLOSSARY one-liners agree with their
  page. **1 definite error** (INDEX:96 dealing-range) and **2 minor imprecisions** (INDEX:154,
  INDEX:32). The breaker colour fix the lead already made is correct on both sides.
- **TIMELINE:** all 32 re-dated entries match each page's `Year Introduced` (28 → 2016, 2 → 2017,
  1 → 2022, 1 → 2023). Every link removed from a 2017/2022 group reappears in a re-dated list;
  no link lost. The links left in the 2017 groups (fib-705, fib-79, ote-failure, ict-fib-overview,
  standard-deviation-projections, fib-vs-ote, partial-takes, correlation-risk, bullish/bearish-
  displacement, displacement-and-fvg) all still read 2017 on their pages. The "(Dec 2016)" added to
  the OB entry is confirmed by SOURCES.md:160. Three lines of stale bold prose remain (section C).
- **Unchanged lines contradicted by the rewritten pages:** 13 (section B). These are not the
  lead's one-liner errors but the lead asked for them; several summarise pages that were NOT
  rewritten and still carry the old claim themselves (noted per item).

---

## A. Errors in the CHANGED lines

### A1. INDEX.md:96 — dealing-range — "wick-anchored" is not on the page and contradicts the fib pages  **(ERROR)**

Current:
`- [dealing-range](concepts/05-pd-arrays/dealing-range.md) — most recent energetic swing low→high ("current trading range" in 2016); wick-anchored for premium/discount.`

Page says: the range is anchored on "the most recent energetic 3-candle swing low → swing high";
Formula: `dealing_range = [swing_low, swing_high]`; "no LTH/LTL (depth-3) bounding rule". The
word "wick" appears nowhere in `dealing-range.md`. Meanwhile `ote-overview.md` Formal Criteria:
"The fib is anchored to candle bodies, not wicks … Wick-anchoring shifts leg_size and therefore
every level below"; and INDEX.md:300 itself reads "fib-anchoring — where the fib attaches: candle
bodies, not wicks". The one-liner adds a claim the page does not make and sets INDEX:96 against
INDEX:300.

Replacement:
`- [dealing-range](concepts/05-pd-arrays/dealing-range.md) — most recent energetic swing low→high ("current trading range" in 2016; term itself 2017+); no LTH/LTL depth rule; EQ = its midpoint.`

### A2. INDEX.md:154 — killzone-times-table — era/market split misstated  **(minor)**

Current:
`… — quick-reference card: 2017 forex vs 2022 index windows (NY AM 07-10 FX, 08:30-11 indices).`

Page says: the two sets are the **April-2017 mentorship set** and the **2022 YouTube set**; the
2022 set contains BOTH an FX New York window (07:00–10:00, ep17) and the index AM/PM windows
(08:30–11:00, 13:30–16:00, ep41). 07–10 FX is in both eras; the split is by era, not forex-vs-index.
Also the page's headline point — "the term 'kill zone' exists in 2016; the clock does not" — is
what justified the 2016→2017 re-date and is absent.

Replacement:
`… — quick-reference card: April-2017 mentorship set vs 2022 YouTube set (NY 07-10 FX in both; 08:30-11 / 13:30-16 indices are 2022 only); no clocked killzone before Apr 2017.`

### A3. INDEX.md:32 — mss-vs-choch — "shift (intraday)" over-fixes the rank  **(minor)**

Current:
`… — disambiguation: CHoCH is SMC (0 corpus hits); ICT's only split is shift (intraday) vs break (more significant).`

Page says: EP03 does call "shift" the lesser/intraday word and "break" the more significant one,
but the page then adds: "'shift' also names the largest turn ICT teaches — the three-to-four-month
quarterly shift … So 'shift' is not reserved for small/intraday events either; scale depends on
context, not a fixed rank." The bracket "(intraday)" states the fixed rank the page warns against.

Replacement:
`… — disambiguation: CHoCH is SMC (0 corpus hits); ICT's only split is shift (lesser) vs break (more significant) — by significance, not mechanism, and not a fixed rank.`

### Verified correct (no action)

INDEX 27, 28, 31, 33, 41, 42, 46, 47 (10–20 pip / 15–30 min figure is on the page, Formula +
Citations, `ICT-2016-LIQUIDITY-POOLS`), 48, 49, 50 (Dec 2016 confirmed by SOURCES.md:149), 53,
105, 106, 107, 108, 110, 116, 120, 121, 133, 134, 135, 136, 137, 141, 144, 162, 167, 173, 182,
191, 193, 197, 231, 296, 323, 342, 343, 358.
GLOSSARY 17, 18, 19, 20, 25, 26, 36, 39, 54, 56, 67, 71, 73, 78, 86, 96, 137.

---

## B. UNCHANGED INDEX/GLOSSARY lines now contradicted by the rewritten pages

Ordered by how directly the rewritten page contradicts them.

### B1. INDEX.md:29–30 — choch-bullish / choch-bearish presented as ICT definitions

Current:
`- [choch-bullish](…) — first close above swing high after bearish leg (reversal).`
`- [choch-bearish](…) — first close below swing low after bullish leg.`

Rewritten `mss-vs-choch.md`: "'CHoCH' (change of character) is not an ICT term … 0 hits in both
corpora … SMC community vocabulary". `mss.md`: "no FVG or close required" — the close rule is SMC
too. (The two choch pages were not rewritten and still state the SMC rule as if ICT's.)

Replacement:
`- [choch-bullish](…) — SMC label (0 corpus hits): first close above a swing high after a bearish leg; ICT's own term is "break/shift in market structure" — see mss-vs-choch.`
`- [choch-bearish](…) — SMC label (0 corpus hits): mirror of choch-bullish; see mss-vs-choch.`

### B2. INDEX.md:219 — ote-79 "invalidation reference" — the page itself was corrected the other way

Current:
`- [ote-79](…) — deep OTE entry / invalidation reference.`

Rewritten `ote-79.md`: "⚠ 0.79 is an ENTRY bound, not the stop … This file previously described
0.79 as 'the OTE invalidation reference' … The dedicated OTE material places the stop at the
leg-origin extreme (fib 1.0), exactly." `stop-placement-by-pd-array.md`: "No source anywhere in
the OTE corpus references the stop to 0.79."

Replacement:
`- [ote-79](…) — deepest OTE entry bound (not the stop; SL sits at the leg-origin extreme).`

Same claim at **INDEX.md:303** `fib-79 — deep OTE / invalidation reference.` — `fib-79.md` was NOT
rewritten and still says "canonical invalidation reference … SLs typically sit just beyond 0.79";
it now contradicts ote-79 / ote-overview / stop-placement. Flag the page, and change the line to:
`- [fib-79](…) — lower OTE bound; ⚠ page still calls it the invalidation reference, contradicted by ote-79 / stop-placement-by-pd-array.`

### B3. INDEX.md:226 — mitigation-of-fvg "CE-threshold … (2025 default)"

Current:
`- [mitigation-of-fvg](…) — CE-threshold FVG mitigation (2025 default).`

Rewritten `fvg-mitigation.md`: "Completion, as the corpus states it, is a full close-in … No 'CE
mitigation' rule exists in the corpus." Rewritten `consequent-encroachment.md`: "CE is not stated
as the primary or required entry … the separate, unverified 2025 claim." (`mitigation-of-fvg.md`
not rewritten; still carries the CE rule.)

Replacement:
`- [mitigation-of-fvg](…) — FVG tested/filled; ⚠ the CE-threshold "2025 default" is unverified — corpus completion is a full close-in (see fvg-mitigation).`

### B4. INDEX.md:109 — ce-as-primary-entry stated as fact

Current:
`- [ce-as-primary-entry](…) — 2025: CE elevated to default entry.`

Rewritten `consequent-encroachment.md` calls this "the separate, unverified 2025 claim";
rewritten `ict-2022-model.md`: "No source for 'CE' or a 2025 default exists in this corpus —
`consequent` has zero hits across the 41 episodes."

Replacement:
`- [ce-as-primary-entry](…) — claimed 2025 shift to CE as default entry — UNVERIFIED, no corpus source; 2022 ICT enters at the near edge.`

### B5. INDEX.md:124 — unmitigated-order-block "fresh OB, highest conviction"

Current:
`- [unmitigated-order-block](…) — fresh OB, highest conviction.`

Rewritten `bullish-order-block.md` Formal Criteria: "**Not fresh-only.** Both eras permit repeated
return visits … 'supply and demand requires fresh zones, okay? That's nonsense. I have no affinity
for anything like that.' (EP18 [40:41–41:12]); 'we have [an] order block — it trades into that
multiple times' (EP30)." (`unmitigated-order-block.md` not rewritten; still says "highest-conviction".)

Replacement:
`- [unmitigated-order-block](…) — OB not yet revisited; ⚠ "fresh = highest conviction" is an SMC rule ICT rejects (EP18 40:41) — see bullish-order-block.`

### B6. INDEX.md:192 — asia-session "18:00 prev → 03:00 NY"

Current:
`- [asia-session](…) — 18:00 prev → 03:00 NY; accumulation / range-building.`

Rewritten `asian-range.md` Formal Criteria: "20:00 → 00:00 NY — this is the only clocked Asian
window in either corpus; no 'full session' alternative (18:00–03:00 or similar) appears anywhere."

Replacement:
`- [asia-session](…) — accumulation / range-building; ⚠ no 18:00–03:00 window in corpus — ICT's only clocked Asian window is the 20:00–00:00 NY Asian range.`

### B7. INDEX.md:152 — london-close-killzone "10:00–12:00 NY; overlaps NY AM"

Current:
`- [london-close-killzone](…) — 10:00–12:00 NY; overlaps NY AM.`

Rewritten `london-close.md`: era-split "10:00 → 12:00 NY (2017) or 10:00 → 11:00 NY (2022)";
"**Abuts, does not overlap, the forex NY killzone** … There is no shared minute in either era for
forex. **Overlaps only the 2022 index AM window.**"

Replacement:
`- [london-close-killzone](…) — 10:00–12:00 NY (2017) / 10:00–11:00 (2022); abuts the forex NY KZ, overlaps only the 2022 index AM window.`

### B8. INDEX.md:151 — ny-am-killzone "08:00–11:00 NY"

Current:
`- [ny-am-killzone](…) — 08:00–11:00 NY; highest-volume KZ.`

Rewritten `killzone-times-table.md`: New York "no longer matches either the 2017 set or the
widely-circulated '08:00–11:00' figure" — ICT's clocks are 07:00–10:00 (FX, 2017 and 2022) and
08:30–11:00 (indices AM, 2022). INDEX.md:90 (ipda-true-day) already says the 07–10 clock
"contradicts the public killzone table".

Replacement:
`- [ny-am-killzone](…) — 07:00–10:00 NY (FX, 2017 + 2022) / 08:30–11:00 (indices, 2022); the "08:00–11:00" figure is not ICT's.`

### B9. INDEX.md:26 — external-structure "LTH/LTL pair that bounds the range"

Current:
`- [external-structure](…) — LTH/LTL pair that bounds the range.`

Rewritten `dealing-range.md`: "No LTH/LTL (depth-3) bounding rule, and no 'external BOS ends the
range' rule, appear in either corpus"; rewritten `external-range-liquidity.md`: "not a fixed
LTH/LTL swing depth". (`external-structure.md` not rewritten.)

Replacement:
`- [external-structure](…) — the swings bounding the current range; ⚠ the LTH/LTL (depth-3) bounding rule is a library convention, not ICT's (see dealing-range).`

### B10. GLOSSARY.md:65–66 — MMBM / MMSM defined as AMD variants and linked to power-of-three

Current:
`- **MMBM** — Market Maker Buy Model. AMD running to upside distribution. → [power-of-three](…)`
`- **MMSM** — Market Maker Sell Model. AMD running to downside distribution. → [power-of-three](…)`

Rewritten `power-of-three.md`: "'MMBM/MMSM as PO3 aliases' … are not ICT's vocabulary for this
concept"; Common Mistakes: "The market maker buy/sell model is a **separate curve construct** …
No sentence in either corpus equates it with PO3"; "this library has no dedicated page for it yet,
so it is not cross-linked here as a PO3 alias."

Replacement:
`- **MMBM** — Market Maker Buy Model. A multi-leg price-curve construct (consolidation → sell-side run → smart-money reversal → re-accumulation); NOT a PO3/AMD alias. → no dedicated page yet; see power-of-three Common Mistakes.`
`- **MMSM** — Market Maker Sell Model. Mirror of MMBM; NOT a PO3/AMD alias. → see power-of-three Common Mistakes.`

### B11. INDEX.md:61, 128, 129 — CHoCH / BOS used as ICT pivot labels

Current:
`- [order-flow-shift](…) — bias-flip via CHoCH/MSS.`
`- [reversal-order-block](…) — OB at CHoCH/MSS pivot.`
`- [continuation-order-block](…) — OB at BOS pivot in trend.`

Rewritten `bos-bullish.md` / `mss-vs-choch.md`: CHoCH and BOS are SMC labels (0 hits); ICT's one
term covers continuation and reversal, so "BOS pivot in trend" encodes the continuation-only
reading the pages reject.

Replacement:
`- [order-flow-shift](…) — bias-flip via a market structure shift/break.`
`- [reversal-order-block](…) — OB at the reversal structure-shift pivot.`
`- [continuation-order-block](…) — OB at a with-trend structure break (the "BOS" label is SMC).`

### B12. GLOSSARY.md:135 — SMC cross-reference row maps "BOS" to an ICT equivalent called "BOS"

Current:
`| Internal BOS / external BOS | Internal vs external structure + BOS | [bos-bullish]… |`

GLOSSARY:19 (lead's own edit) now says BOS is "SMC label, not ICT's"; rewritten
`external-range-liquidity.md`: "'Taking ERL = external BOS = bias change' is not in either corpus —
searched 'external bos', 'external break of structure', 'external structure' (0/0 each)."

Replacement:
`| Internal BOS / external BOS | Break in market structure, read against the current trading range (IRL/ERL) — "BOS" and "external structure" are SMC terms, 0 corpus hits | [bos-bullish]…, [internal-range-liquidity]…, [external-range-liquidity]… |`

### B13. INDEX.md:194 — ny-am-session "08:00 → 12:00 NY"  (low)

Rewritten `london-close.md`: "not the '08:00–12:00' figure, which belongs to bond-market NY AM
hours" (cf. INDEX:199 bond-split-session-rules AM 08:00–12:00). Replacement:
`- [ny-am-session](…) — NY morning: FX KZ 07:00–10:00, indices 08:30–11:00; 08:00–12:00 is the bond AM window.`

### Low-priority, noted only
- INDEX.md:158–161 — silver-bullet-overview/-london/-ny-am/-ny-pm state the three SB windows as
  fact; rewritten `silver-bullet-rules.md` (INDEX:162 now flagged) says no Silver Bullet teaching
  exists in either corpus. The sibling lines carry no flag. Suggest appending "(unverified in
  corpus — see silver-bullet-rules)" to INDEX:158.
- INDEX.md:228 — partial-vs-full-mitigation "fresh/partial/mitigated/fully-consumed lifecycle";
  rewritten `fvg-mitigation.md`: "A rebalanced FVG is not described as 'consumed'." Page not
  rewritten; wording only.
- INDEX.md:138 — failed-breaker "breaker that fails on retest"; TIMELINE already records "'Failed
  breaker' is not a label ICT uses anywhere in the corpus". No flag on the INDEX line.

---

## C. TIMELINE — stale prose after the link moves (no dating errors)

- TIMELINE 2022 section, line now reading `**range-expansion** / **range-contraction** — phase
  terminology operationalized. → [range-contraction]` — bold text still names range-expansion
  (re-dated to 2016 and its link removed). Drop "**range-expansion** /".
- TIMELINE 2017 section, `**OTE methodology + ICT fib levels** introduced (0.62 / 0.705 / 0.79
  retracement; …)` — the five OTE pages and fib-62 moved to 2016, so the sentence "introduced"
  with the three levels now sits over links that are only ote-failure / ict-fib-overview /
  fib-705 / fib-79 / SD projections / fib-vs-ote. Also note the page-level inconsistency this
  exposes: fib-62 reads 2016 while fib-705 / fib-79 still read 2017 for the same Sep-2016 lecture
  (`ICT-2016-EQUILIBRIUM-DISCOUNT` 29:35 names all three).
- TIMELINE 2017 section, `**Risk management** discipline (R-multiple, position sizing, structural
  SL, partial takes, correlation risk)` — the bracket still lists the three items moved to 2016;
  only partial-takes / correlation-risk remain linked.
- TIMELINE 2017 section, `**choch-bullish** / **choch-bearish** — CHoCH reversal terminology.` —
  still presents CHoCH as 2017 ICT terminology; rewritten `mss-vs-choch.md` says 0 corpus hits.
- TIMELINE 2016 "All 5 killzones + supporting files" keeps the six killzone pages at 2016 while the
  rewritten `killzone-times-table.md` says no clocked killzone exists before April 2017 — the
  pages themselves read 2016, so this is a page-dating question for the audit, not a lead error.
