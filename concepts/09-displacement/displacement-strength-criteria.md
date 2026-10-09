# Displacement Strength Criteria

**Category:** 09-displacement
**Aliases:** displacement quality, energetic vs. anemic/lethargic displacement
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-EP05, ICT-2022-MENTORSHIP-EP06, ICT-2022-MENTORSHIP-EP24, ICT-2022-MENTORSHIP-EP40
**Tags:** displacement, quality

## Definition

ICT grades displacement **qualitatively and binary** — energetic/animated versus weak/anemic/lethargic — not with a numeric score. He does not teach a "weak / moderate / strong" three-tier framework or any multi-factor scoring: searched both corpora (153 2016-17/2020 packets, 40 captioned 2022 episodes) for `weak displacement`, `moderate displacement`, `strong displacement`, `displacement is (weak|strong)`: 0 hits in either. His own contrast pairs are: "energetic" vs. "a little lethargic little move" (`ICT-2022-MENTORSHIP-EP06` [19:05]); "energetic break" vs. "a very weak anemic move" (`ICT-2022-MENTORSHIP-EP05` [20:40]); "toe in the water" vs. "meaningful displacement" (`ICT-2022-MENTORSHIP-EP40` [08:56]); "melted ... no displacement, no energetic move" (`ICT-2022-MENTORSHIP-EP24` [23:30]). (A prior version of this page presented an unsourced 5-factor numeric scoring system; this version replaces it with ICT's own binary test, cited below.)

## Formal Criteria

ICT's actual test is pass/fail on each of the following qualitative reads, not a weighted score:

- Does the move look energetic/animated, or lethargic/weak/anemic? (EP05 [20:40], EP06 [19:05])
- Did it "fall in" with conviction, or was it only a "toe in the water"? (EP40 [08:56])
- Did price actually move/close through the level, or did it "melt" without displacing? (EP24 [23:30])

ICT states no numeric sub-criteria (body/range ratio, opposing-wick percentage, body-vs-average multiple, or a "follow-through candle count") for any of these reads.

## Formula / Math

```
# ICT gives no number for this.
# No 5-factor score, no 0.50/0.70/0.85 body-ratio bands, no 1.0/1.5/2.0x
# body-vs-average bands, no 5-15 point scale, and no "follow-through:
# 3+ candles" criterion appear in either corpus (searched `follow.?through`:
# 4 raw hits, all about session/contract follow-through, unrelated to
# displacement; 0 hits in the 2022 episodes).
#
# ICT's test is binary: energetic/animated vs. lethargic/anemic/weak.
```

## Machine-Readable

```json
{
  "id": "displacement-strength-criteria",
  "category": "09-displacement",
  "aliases": ["displacement-quality"],
  "criteria": [
    {"id": "c1", "expr": "binary: energetic/animated vs. lethargic/anemic/weak"},
    {"id": "c2", "expr": "five_factor_numeric_score: not given by ICT (0 hits, both corpora)"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2022",
  "related": ["displacement-definition","bullish-displacement","bearish-displacement","displacement-and-fvg"],
  "sources": ["ICT-2022-MENTORSHIP-EP05","ICT-2022-MENTORSHIP-EP06","ICT-2022-MENTORSHIP-EP24","ICT-2022-MENTORSHIP-EP40"]
}
```

## Visual Pattern

```
   "toe in the water" (not enough):          "fell in" / energetic (meaningful):

        ╱╲   small, hesitant dip                  ▲
       ╱  ╲                                       ██
      ╱    ╲                                      ██   wide, fast, commits
                                                   ██   through the level
```

ICT's own imagery — "toe in the water" vs. a candle that "falls in" — is the closest thing to a visual test; there is no bar-geometry formula behind it.

## Timeframes

M1–D, matching the timeframes displacement itself is taught on.

## Examples

**Example 1 — ICT's own pass/fail reasoning, not a score:**
- Sell-side stops are run below a low: "they go down, run out the sell stops, traders are caught in; then what — what's the next logic? we got to look for displacement, it's got to trade back above this old low, it's got to have displacement above that; did it happen here? no" (`ICT-2022-MENTORSHIP-EP24` [22:52]).
- Price returns to the old low but "melted, didn't do anything above that oh[ld] low — there was no displacement, no energetic move" (EP24 [23:30]).
- → fails ICT's qualitative test (no displacement above the old low), so there is no long idea. There is no partial-credit scoring step.

## Common Mistakes

- **Attributing a 5-factor table, numeric bands (0.50/0.70/0.85, 1.0/1.5/2.0×), or a 5–15 point score to ICT.** None of this is in either corpus; it is a prior library invention that was mislabeled as ICT's.
- **Citing "Year Refined 2024."** Neither corpus reaches 2024; this library has no source for that date, and it has been removed.
- **Treating "follow-through candle count" as an ICT displacement criterion.** The only `follow-through` hits in either corpus are about session/contract follow-through, unrelated to displacement quality.
- **Single-factor numeric scoring of any kind.** Use ICT's own binary, verbal judgment instead (energetic/animated vs. lethargic/anemic/weak).

## ICT vs Community

A prior version of this page attributed an invented 5-factor numeric score to ICT; searched both corpora for `weak displacement`, `moderate displacement`, `strong displacement`, `displacement is (weak|strong)`, and `follow.?through` near displacement context: 0 supporting hits in either. ICT's own test is a binary, qualitative read — energetic/animated vs. lethargic/anemic/weak/"toe in the water" — documented under Formal Criteria above.

## Related Concepts

- [displacement-definition](displacement-definition.md) — the qualitative test this page restates in detail.
- [bullish-displacement](bullish-displacement.md), [bearish-displacement](bearish-displacement.md), [displacement-and-fvg](displacement-and-fvg.md).

## Citations

- `ICT-2022-MENTORSHIP-EP05` [20:40] — "energetic break" vs. "very weak anemic move."
- `ICT-2022-MENTORSHIP-EP06` [19:05] — "energetic" vs. "a little lethargic little move."
- `ICT-2022-MENTORSHIP-EP24` [22:52]–[23:30] — sell-stop run below a low; "melted ... no displacement, no energetic move" above the old low.
- `ICT-2022-MENTORSHIP-EP40` [08:56] — "toe in the water" vs. meaningful displacement.
