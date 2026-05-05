# Accumulation Phase

**Category:** 12-power-of-three
**Aliases:** A-phase, accumulation, build-up phase
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-PO3, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** po3, amd, accumulation

## Definition

The **accumulation phase** is the first phase of the PO3 / AMD cycle: a quiet, range-bound, low-volatility window during which institutional positions are built without revealing directional intent. Characterized by tight ranges, overlapping candles, and engineered liquidity (equal highs/lows along the bounds) that becomes the next phase's manipulation target. The Asia session is the canonical daily-scale accumulation window.

## Formal Criteria

- Tight price range bounded by recent LTH and LTL.
- Low ATR relative to recent expansion.
- Overlapping candles, no decisive directional close.
- Often equal highs and equal lows form along the bounds (engineered liquidity).
- Time-of-day correspondence: Asia session (intraday), session Q1 (90-min cycle), week's Q1 = Monday.

## Formula / Math

```
accumulation_phase := no_external_bos
                      AND ATR_recent <= 0.7 * ATR_prior_expansion
                      AND candle_overlap_pct >= 0.7
                      AND range bounded by recent LTH and LTL
```

Equivalent to [range-contraction](../01-market-structure/range-contraction.md) at the price-action level.

## Machine-Readable

```json
{
  "id": "accumulation-phase",
  "category": "12-power-of-three",
  "aliases": ["A-phase", "accumulation", "build-up-phase"],
  "criteria": [
    {"id": "c1", "expr": "low_volatility_range == true"},
    {"id": "c2", "expr": "overlapping_candles == true"},
    {"id": "c3", "expr": "engineered_liquidity_at_bounds == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["power-of-three","manipulation-phase","distribution-phase","intraday-amd","range-contraction","asia-session","asian-range","equal-highs","equal-lows"],
  "sources": ["ICT-2016-PO3","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   accumulation phase (intraday Asia example):

   range_high ────────────  ← BSL pool (engineered)
        /\  /\  /\
       /  \/  \/  \   ← tight, overlapping candles
      /            \
   range_low  ────────────  ← SSL pool (engineered)
```

## Timeframes

All TFs. Daily accumulation = Asia; weekly accumulation = Monday; monthly accumulation = early-month consolidation.

## Examples

**Example 1 — daily accumulation:**
- 18:00–03:00 NY: EURUSD prints 30-pip range, ATR ≈ 4 pips, overlapping candles.
- Two equal lows at 1.0848.
- → Asia accumulation phase. Manipulation (London open) likely sweeps 1.0848 next.

## Common Mistakes

- **Trading mean-reversion blindly.** Accumulation chop offers no edge without PD-array + bias confluence.
- **Confusing late-distribution with accumulation.** A late-cycle range that looks like accumulation may be distribution-exhaustion before reversal — check HTF context.

## Related Concepts

- [power-of-three](power-of-three.md), [manipulation-phase](manipulation-phase.md), [distribution-phase](distribution-phase.md), [intraday-amd](intraday-amd.md), [range-contraction](../01-market-structure/range-contraction.md), [asia-session](../15-sessions/asia-session.md), [asian-range](../14-asian-range/asian-range.md), [equal-highs](../02-liquidity/equal-highs.md), [equal-lows](../02-liquidity/equal-lows.md).

## Citations

- `ICT-2016-PO3`, `ICT-2022-MENTORSHIP-OVERVIEW`.
