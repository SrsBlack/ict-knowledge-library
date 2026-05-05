# Range Contraction

**Category:** 01-market-structure
**Aliases:** contraction, contraction phase, consolidation, accumulation range
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW, ICT-2016-PO3
**Tags:** structure, contraction, consolidation, accumulation, dealing-range

## Definition

Range contraction is the phase in which price oscillates inside a tightening dealing range with overlapping candles, narrow ATR, and no decisive directional close. ICT treats contraction as the **accumulation / engineered-liquidity phase** where institutional positioning happens before the next [range-expansion](range-expansion.md). It is the time-domain side of the AMD cycle's accumulation phase.

## Formal Criteria

- Price is bounded between a recent LTH and LTL with neither bound being broken on a candle close.
- ATR (or candle-body average) is materially lower than the recent expansion-phase average.
- A high proportion of candles overlap with their predecessors (no gap, no displacement).
- Equal highs and equal lows tend to form along the range boundaries — these are the engineered liquidity pools that the next expansion will sweep.

## Formula / Math

```
contraction := no_external_bos
                AND ATR_recent <= 0.7 * ATR_prior_expansion
                AND overlap_pct >= 0.7
```

`overlap_pct` = fraction of candles whose body overlaps the prior candle's range.

## Machine-Readable

```json
{
  "id": "range-contraction",
  "category": "01-market-structure",
  "aliases": ["contraction-phase", "consolidation", "accumulation-range"],
  "criteria": [
    {"id": "c1", "expr": "no_external_bos_during_window == true"},
    {"id": "c2", "expr": "ATR_recent <= 0.7 * ATR_prior_expansion"},
    {"id": "c3", "expr": "candle_overlap_pct >= 0.7"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2022",
  "related": ["range-expansion","accumulation-phase","equal-highs","equal-lows","liquidity-pool","dealing-range"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW","ICT-2016-PO3"]
}
```

## Visual Pattern

```
   prior expansion              contraction              next expansion
   ────────────                 ─────────────────        ────────────
   ▲                             /\  /\  /\
   █▲                           /  \/  \/  \                 ▲
   █ █                         /            \               █▲
   █  █                       (tight, overlap-               █ █
                                heavy candles)               █  █
```

Visually distinct from expansion: many small bodies, lots of wicks, no decisive direction.

## Timeframes

All M5 → D. HTF contractions (D / H4) often last days and produce the largest subsequent expansion moves. LTF contractions are the staging area for session-based setups (Asian range, NY AM open range, etc.).

## Examples

**Example 1 — Asian session contraction:**
- During Asian hours, EURUSD oscillates in a 25-pip range on M5 with ATR ≈ 4 pips.
- → range contraction. Equal highs and equal lows form at the range bounds.
- London open often sweeps one bound and then expands toward the other (Judas swing → expansion).

## Common Mistakes

- **Calling every chop "consolidation".** Contraction has a specific structural definition: bounded by an LTH and LTL with no external BOS. Random chop without clear bounds is not the same.
- **Trading mean-reversion blindly inside contraction.** Tradeable mean-reversion setups inside a contraction need confluence with PD arrays, sessions, or HTF bias — not just "the range is tight."
- **Missing the engineered-liquidity bait.** Equal highs / equal lows that form during contraction are bait for the next sweep; assume they will be taken.

## Related Concepts

- [range-expansion](range-expansion.md) — what follows a contraction.
- [accumulation-phase](../12-power-of-three/accumulation-phase.md) — the AMD-cycle equivalent.
- [equal-highs](../02-liquidity/equal-highs.md) / [equal-lows](../02-liquidity/equal-lows.md) — what forms at the bounds.
- [liquidity-pool](../02-liquidity/liquidity-pool.md) — what the bounds become.
- [dealing-range](../05-pd-arrays/dealing-range.md) — the price range a contraction operates inside.

## Citations

- `ICT-2016-PO3` — accumulation phase concept (foundational PO3 lecture).
- `ICT-2022-MENTORSHIP-OVERVIEW` — expansion/contraction terminology for chart reading.
