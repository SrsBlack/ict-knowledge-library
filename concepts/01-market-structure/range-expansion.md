# Range Expansion

**Category:** 01-market-structure
**Aliases:** expansion, expansion phase, breakout
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** structure, expansion, breakout, momentum, dealing-range

## Definition

Range expansion is the phase in which price breaks out of a prior contraction or consolidation and travels with momentum, typically widening the average true range and producing displacement candles. ICT pairs expansion with [range-contraction](range-contraction.md) as the two complementary phases of price delivery: contraction builds energy via consolidation; expansion releases it via directional movement.

## Formal Criteria

- The most recent dealing range (consolidation between an LTH and an LTL) has just been broken via an external BOS.
- Subsequent candles show an ATR (or candle-body length) materially larger than the contraction-phase average.
- Price travels in a single direction with shallow pullbacks until it reaches its next external structure target (HTF liquidity pool, HTF PD array, etc.).
- Expansion ends when displacement subsides and price begins to consolidate again.

## Formula / Math

```
ATR_contraction = mean(true_range, last_N_contraction_bars)
ATR_expansion   = mean(true_range, last_N_post_break_bars)

range_expanding := ATR_expansion >= K * ATR_contraction      [K typically 1.5..3]
                    AND directional_close_count >= 0.7 * N    [70% closes in same direction]
```

ICT teaches expansion qualitatively rather than with a fixed numerical filter; the formula above is a common quantification used in research.

## Machine-Readable

```json
{
  "id": "range-expansion",
  "category": "01-market-structure",
  "aliases": ["expansion-phase", "breakout"],
  "criteria": [
    {"id": "c1", "expr": "external_bos_just_occurred == true"},
    {"id": "c2", "expr": "ATR_recent >= 1.5 * ATR_contraction"},
    {"id": "c3", "expr": "directional_close_majority == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2022",
  "related": ["range-contraction","bos-bullish","bos-bearish","displacement-definition","external-structure"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   contraction               expansion
   ───────────────────       ───────────────
       /\  /\  /\                 ▲
      /  \/  \/  \               █▲
     /            \             █ █
    /              \           █  █
                              █   █
                     ─→ break ─→ wide directional candles
```

Tight, overlapping candles → external BOS → wide, mostly-one-color candles.

## Timeframes

Every TF M5 → W. Higher-TF expansion is rarer but produces the largest moves and the cleanest [displacement](../09-displacement/displacement-definition.md) signatures.

## Examples

**Example 1 — H1 expansion after contraction:**
- H1 prints 30 bars in a 35-pip range; ATR ≈ 8 pips.
- An H1 candle breaks the range high and prints a 28-pip body. Subsequent 5 bars all close green, average body 18 pips.
- → range expansion. Bias: continuation toward next HTF liquidity target.

## Common Mistakes

- **Confusing every breakout with expansion.** A break that immediately stalls is not expansion; it's a failed break or a sweep.
- **Ignoring direction quality.** Expansion is mostly one-color candles. Mixed-color, overlapping bodies = still ranging.
- **Trading against expansion.** ICT teaches that fading expansion is low-probability; counter-trend setups belong to the contraction phase or to specific HTF reversal setups (CHoCH/MSS).

## Related Concepts

- [range-contraction](range-contraction.md) — the prior phase.
- [bos-bullish](bos-bullish.md) / [bos-bearish](bos-bearish.md) — usually triggers the expansion.
- [displacement-definition](../09-displacement/displacement-definition.md) — what an expansion candle looks like.
- [external-structure](external-structure.md) — what is being broken.

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW` — expansion / contraction framing for live trading.
