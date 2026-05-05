# Internal Structure

**Category:** 01-market-structure
**Aliases:** minor structure, internal range structure, intra-range pivots
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** structure, fractal, internal, dealing-range

## Definition

Internal structure is the set of swing highs and swing lows that occur **inside** the current dealing range — i.e., between the most recent long-term high (LTH) and long-term low (LTL) that bound the range. Internal swings are short-term and intermediate-term pivots; they generate the trade-management decisions inside the range, but breaking one of them does NOT change the larger directional bias.

## Formal Criteria

- A swing point `s` is internal iff its price level is strictly between the prices of the bounding LTH and LTL of the current dealing range.
- Internal swings drive lower-timeframe BOS / CHoCH events that are valid for entries but not for HTF bias change.
- A break of internal structure (an "iBOS" or internal CHoCH) is sometimes called a **shift in internal order flow** but does NOT invalidate the larger external trend.

## Formula / Math

```
LTH_range = price of bounding long-term high
LTL_range = price of bounding long-term low

is_internal(swing_s) := LTL_range < price(s) < LTH_range
```

External structure breaks bound the range. Internal breaks happen within it.

## Machine-Readable

```json
{
  "id": "internal-structure",
  "category": "01-market-structure",
  "aliases": ["minor-structure", "internal-range-structure"],
  "criteria": [
    {"id": "c1", "expr": "LTL_range < price(swing) < LTH_range"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["external-structure","swing-high","swing-low","bos-bullish","choch-bullish","internal-range-liquidity"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   LTH ──────────────────────────  external
        \   /\          /\
         \ /  \   /\   /  \
          v    \ /  \ /
   STL    ITL   v    v       internal swings
   ──────────────────────────
   LTL ──────────────────────────  external
```

Pivots between LTH and LTL = internal. The range top and bottom themselves = external.

## Timeframes

Internal-vs-external is **relative to the timeframe being analyzed**. A swing high that is internal on the daily chart can be (and usually is) an external long-term high on an M5 chart. Always state the reference timeframe when discussing internal structure.

## Examples

**Example 1 — H4 dealing range:**
- H4 LTH at 1.1000, H4 LTL at 1.0800.
- Any M15 / H1 swing between 1.0800 and 1.1000 is internal to the H4 range.
- An M15 close below an M15 STL at 1.0850 = internal BOS — useful for an entry, irrelevant for the H4 bias.

## Common Mistakes

- **Treating internal BOS as bias change.** Internal breaks scaffold lower-timeframe entries but do not flip HTF bias.
- **Forgetting the reference TF.** "Internal" is meaningless without saying "internal to the H4 range" (or whichever TF defines the dealing range).
- **Mixing fractal layers.** STH/ITH on an M15 chart is not the same fractal layer as STH/ITH on the daily.

## Related Concepts

- [external-structure](external-structure.md) — the bounding LTH/LTL pair.
- [swing-high](swing-high.md) / [swing-low](swing-low.md) — building blocks.
- [bos-bullish](bos-bullish.md) / [bos-bearish](bos-bearish.md) — internal vs external BOS.
- [internal-range-liquidity](../02-liquidity/internal-range-liquidity.md) — liquidity inside the range.
- [dealing-range](../05-pd-arrays/dealing-range.md) — the range whose bounds define internal vs external.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — internal vs external pivot framing.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operationalized for entries inside HTF dealing ranges.
