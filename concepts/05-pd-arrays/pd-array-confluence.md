# PD Array Confluence

**Category:** 05-pd-arrays
**Aliases:** PDA confluence, multi-array alignment, confluence stacking
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2025
**Source IDs:** ICT-2017-INDEX-TRADE-SETUPS, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2025-ADV-LIQUIDITY
**Tags:** pd-array, confluence, alignment

## Definition

PD array confluence is the **alignment of multiple independent factors** at a single price level — distinct from but related to nesting. Where [pd-array-nesting](pd-array-nesting.md) requires same-direction PD arrays overlapping spatially, confluence is broader: it includes time-of-day (killzone, macro), HTF bias, structural context (CHoCH/MSS just delivered), and adjacent liquidity pools (sweep target nearby) — all firing at the same level. ICT's discipline: **the more independent factors that align, the higher the conviction.**

## Formal Criteria

Independent confluence factors that ICT teaches:

1. **Spatial PD-array nesting** — bullish OB containing bullish FVG (counts as 1 nest, often 2 arrays).
2. **HTF alignment** — entry-TF array sits inside an HTF array.
3. **Bias agreement** — HTF bias direction matches setup direction.
4. **Time-of-day** — setup forms inside a killzone or macro window.
5. **Structural context** — recent MSS / CHoCH supports the direction.
6. **Adjacent liquidity** — clear DOL above (longs) / below (shorts) within reach.
7. **Fresh, unmitigated arrays** — preferred over already-tested ones.

A medium-confluence setup has 3–4 factors firing; high-confluence has 5+; low-confluence has 1–2.

## Formula / Math

```
confluence_score(setup) = sum(1 for factor in factors if active(factor, setup))

# Working scale:
# 1-2 factors:  low confluence (skip or tiny size)
# 3-4 factors:  medium confluence (standard size)
# 5-6 factors:  high confluence (full size, increased conviction)
# 7+:           rare; reserved for "A+" setups
```

## Machine-Readable

```json
{
  "id": "pd-array-confluence",
  "category": "05-pd-arrays",
  "aliases": ["PDA-confluence", "multi-array-alignment"],
  "criteria": [
    {"id": "c1", "expr": "count_aligned_independent_factors >= 3 for actionable setup"},
    {"id": "c2", "expr": "factors include any of: nesting, HTF_align, bias, time_of_day, structure, adjacent_liquidity, freshness"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2025",
  "related": ["pd-array-definition","pd-array-hierarchy","pd-array-nesting","htf-pd-array-hierarchy","htf-bias-framework","killzone-overview","macro-times-overview","draw-on-liquidity"],
  "sources": ["ICT-2017-INDEX-TRADE-SETUPS","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2025-ADV-LIQUIDITY"]
}
```

## Visual Pattern

```
Confluence at a single setup zone (bullish discount example):

   ░░░░░ ←  H4 bullish OB (factor 1: HTF array)
   ░▓▓░░    │
   ░▓░▓░ ←  H1 bullish FVG nested inside (factor 2: nesting)
   ░░░░░    │
            ↑
     deep discount of D range (factor 3: depth)
     HTF bias bullish        (factor 4: bias)
     formed in NY AM KZ      (factor 5: time-of-day)
     macro 09:50-10:10       (factor 6: precision time)
     fresh, unmitigated      (factor 7: freshness)
     PWL SSL just swept      (factor 8: adjacent liquidity from below)
     PDH BSL above as DOL    (factor 9: clear target)

   → 9-factor confluence = "A+" setup
```

## Timeframes

Most actionable on entry TFs (M5 / M15) where multiple factors can align. HTF-only setups still count factors but typically with broader, more diffuse alignment.

## Examples

**Example 1 — counting factors:**
- HTF bias bullish.
- Setup: bullish OB at H4, M15 FVG nested inside it.
- Time: NY AM KZ + 09:50 macro starting.
- Recent: M5 just printed bullish CHoCH 10 min ago.
- DOL: PDH BSL 60 pips above.
- Freshness: both arrays unmitigated.
- → factors: nesting, HTF align, bias, time-of-day (KZ), time-of-day (macro), structure (CHoCH), adjacent liquidity (DOL), freshness = 8 factors → "A+" setup.

## Common Mistakes

- **Counting dependent factors as independent.** "Bullish OB" and "discount-side array" are not independent — the OB being on the bull side already implies it's at discount if we're long-biased. Count once.
- **Confluence theatre.** Adding spurious "factors" (e.g., RSI, MA crossings) inflates the score without adding ICT-relevant signal. Stick to ICT factors.
- **Single-factor trades.** Acting on a single factor (e.g., "fresh OB" with nothing else) leads to many low-quality entries; require 3+ for standard setups.

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [pd-array-hierarchy](pd-array-hierarchy.md), [pd-array-nesting](pd-array-nesting.md), [htf-pd-array-hierarchy](htf-pd-array-hierarchy.md).
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [killzone-overview](../10-killzones/killzone-overview.md), [macro-times-overview](../04-time-cycles/macro-times-overview.md), [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md).

## Citations

- `ICT-2017-INDEX-TRADE-SETUPS` (10:55–11:08) "a overlap or a nested premium array… the higher time frame confluence with nested ideas of premium array"; (13:05) a nested HTF discount array "further bolsters the idea".

- `ICT-2022-MENTORSHIP-OVERVIEW` — confluence discipline taught for entry selection.
- `ICT-2025-ADV-LIQUIDITY` — strengthening principle and multi-factor framing refined in 2025.
