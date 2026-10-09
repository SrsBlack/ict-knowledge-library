# Balanced Price Range (BPR)

**Category:** 06-fair-value-gaps
**Aliases:** BPR, balanced range, mirror FVG zone, opposing FVG overlap
**ICT Confidence:** medium
**Year Introduced:** 2023
**Year Refined:** 2023
**Source IDs:** ICT-2017-STT-INTRAWEEK-REVERSALS
**Tags:** fvg, bpr, balance, unverified, placeholder-date

⚠ **WRONG dating/attribution — corrected 2026-10-08 per audit; year is a PLACEHOLDER, not a
finding.** This page previously stated "Year Introduced: 2017" sourced to the stub
`ICT-2017-CHARTER-OVERVIEW`. `balanced price range|bpr` has **zero hits** as the two-opposing-FVGs
pattern in either corpus (153 2016-17/2020-21 packets, 40 captioned 2022 Mentorship episodes), and **no
dated source for that pattern exists anywhere in `SOURCES.md`** — the only 2023 registry entry,
`ICT-2023-NDOG-NWOG`, is for a different concept (NDOG/NWOG) and is not cited here. "2023" above
is a four-digit **placeholder** required by this vault's lint format (which requires a bare year),
not an evidenced date; treat it as "unknown," not as a finding. `ICT-2017-CHARTER-OVERVIEW` has
been dropped from Source IDs — it supported nothing on this page and, as a 2017 stub, contradicted
the 2023 placeholder it was previously cited to justify. The one near-match actually in the
2016-17 corpus, "price balanced range" (`ICT-2017-STT-INTRAWEEK-REVERSALS`, Mar 2017), is a
**different concept** — a plain consolidation range inside a market-maker buy/sell weekly profile
— not an overlap of opposing FVGs, and is not the basis for any date on sense 1. The
two-opposing-FVGs definition below is **not corpus-sourced** at any date; it is kept as the
community/later usage this library's readers will encounter, clearly separated from the 2017
quote. Do not cite the 2017 source, and do not read "2023" as a finding, for the FVG-overlap
definition.

## Definition

**Two distinct things share this name.**

1. **The two-opposing-FVGs pattern** (the sense this page's Formal Criteria / JSON describe): a
   price zone where a bullish FVG and a bearish FVG overlap, typically from a recent two-sided
   push through the same area. **This exact pattern has no located ICT source in this library's
   corpus.** It is presented here only as the commonly circulated BPR definition, pending a
   located primary source — treat as unverified, not ICT-confirmed.
2. **"Price balanced range" (2017, corpus-confirmed, a different concept):** a consolidation zone
   inside a weekly market-maker profile that price returns to or exceeds before reversing — "[w]e
   have the consolidation known as in this example as the price balanced range. In other words,
   price is in a small little range and then it leaves it on Tuesday. Aggressively sells off."
   (`ICT-2017-STT-INTRAWEEK-REVERSALS` [18:33]–[18:42]); "intra-week reversals will many times
   look to return to the previous balance the price range or exceed it" (`ICT-2017-STT-INTRAWEEK-REVERSALS`
   [18:06]–[18:12]). This has nothing to do with opposing FVGs and should not be merged with
   sense 1 above.

## Formal Criteria

For the two-opposing-FVGs sense (unverified — see Definition):

- A bullish FVG zone `[fvg_bull_low, fvg_bull_high]` and a bearish FVG zone `[fvg_bear_low, fvg_bear_high]` overlap.
- Overlap region = intersection of the two ranges.

No corpus statement requires both FVGs to be "unmitigated," restricts BPR to a particular market
phase ("contraction"), or declares a mitigation event ends the BPR's relevance — all three were
removed as invented.

## Formula / Math

```
overlap = max(fvg_bull_low, fvg_bear_low), min(fvg_bull_high, fvg_bear_high)
is_bpr = overlap[0] < overlap[1]      # non-empty intersection

# UNVERIFIED pattern overall — see Definition sense 1.
```

## Machine-Readable

```json
{
  "id": "balanced-price-range",
  "category": "06-fair-value-gaps",
  "aliases": ["BPR", "balanced-range", "mirror-FVG-zone"],
  "criteria": [
    {"id": "c1", "expr": "UNVERIFIED: bullish_FVG and bearish_FVG share overlapping price region"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2023",
  "year_refined": "2023",
  "dating": "placeholder, not evidenced — no dated source for the two-opposing-FVGs pattern exists in SOURCES.md; treat year_introduced/year_refined as unknown, not as findings",
  "related": ["fair-value-gap","bullish-fvg","bearish-fvg","range-contraction","htf-bias-framework","pd-array-confluence"],
  "sources": ["ICT-2017-STT-INTRAWEEK-REVERSALS"]
}
```

## Visual Pattern

```
   ▒▒▒▒  ← bearish FVG zone
   ▒▓▒▒
   ▓▓▓▓  ← overlap (unverified BPR reading)
   ░▓░░
   ░░░░  ← bullish FVG zone
```

## Timeframes

Not stated in the corpus for sense 1. `ICT-2017-STT-INTRAWEEK-REVERSALS`'s "price balanced range"
(sense 2) is discussed inside a weekly market-maker profile; no chart timeframe is stated for it.

## Examples

No corpus-sourced example exists for the two-opposing-FVGs sense. The following is illustrative
of the commonly circulated reading only, not an ICT-cited case:

**Example 1 — H1 overlap (illustrative, not corpus-sourced):**
- H1 bearish FVG forms at 1.0945–1.0955.
- Hours later, an H1 bullish FVG forms at 1.0942–1.0952.
- Overlap: [1.0945, 1.0952].

## Common Mistakes

- **Citing the 2017 "price balanced range" lecture for the two-opposing-FVGs pattern.** They are
  different concepts (see Definition sense 2 vs. sense 1); the 2017 lecture never mentions FVGs
  in this context.
- **Claiming "ICT teaches BPR as a decision zone reacting in either direction."** No such
  statement exists in either corpus.
- **Requiring both FVGs "unmitigated," restricting BPR to "contraction," or filtering by
  timeframe ("M5 too noisy").** None of these are corpus-sourced; all were invented.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [bullish-fvg](bullish-fvg.md), [bearish-fvg](bearish-fvg.md).
- [range-contraction](../01-market-structure/range-contraction.md) — unrelated claim removed; no
  corpus link between BPR and contraction phases.
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [pd-array-confluence](../05-pd-arrays/pd-array-confluence.md).

## Citations

- `ICT-2017-STT-INTRAWEEK-REVERSALS` — "Month 07 — Intraweek Market Reversals & Overlapping
  Models" (Mar 2017). Corpus-confirmed "price balanced range" (sense 2, a consolidation, not an
  FVG overlap) [18:06]–[18:12], [18:33]–[18:42]. This is the library's only citation on this page;
  **sense 1 (the two-opposing-FVGs pattern) has no dated source anywhere in `SOURCES.md`** — the
  "2023" header/JSON year is a placeholder required by this vault's lint format, not a finding.
  The previously cited `ICT-2017-CHARTER-OVERVIEW` has been removed: it is a 2017 registry stub
  that supported nothing on this page and contradicted the 2023 placeholder it was cited to
  justify.
