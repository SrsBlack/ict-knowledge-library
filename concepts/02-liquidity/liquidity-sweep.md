# Liquidity Sweep

**Category:** 02-liquidity
**Aliases:** sweep, raid, liquidity raid, stop hunt, wick-sweep
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, sweep, raid, foundational

## Definition

A liquidity sweep is the act of price trading through a [liquidity-pool](liquidity-pool.md) — taking out the resting orders — and then **failing to follow through**, typically reversing back across the swept level on the same or following candle. The sweep is the algorithm's mechanism for filling institutional positions: by trapping retail breakout traders and stopping out resting positions, it gathers the counter-flow needed to fill in size. A sweep is distinguished from a [break-of-structure](../01-market-structure/bos-bullish.md) by the lack of close beyond the swept level — sweep wicks; BOS closes.

## Formal Criteria

For a bullish-side (BSL) sweep:

- Price trades above a known BSL pool (swing high, EQH, trendline).
- The candle that takes the level closes back below it (or close to it without sustaining the break).
- Often a long upper wick is the tell.
- Optional confirmation: a [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) forms in the opposite (bearish) direction shortly after the wick.

For a sell-side (SSL) sweep: symmetric — wick below SSL pool, close back above.

## Formula / Math

```
BSL_sweep(level, n) := high_n > level
                       AND close_n < level
                       AND (high_n - close_n) > 0.6 * range_n   [long upper wick]

SSL_sweep(level, n) := low_n < level
                       AND close_n > level
                       AND (close_n - low_n) > 0.6 * range_n    [long lower wick]
```

The 60% wick rule is a common quantification; ICT teaches it visually.

## Machine-Readable

```json
{
  "id": "liquidity-sweep",
  "category": "02-liquidity",
  "aliases": ["sweep", "raid", "liquidity-raid", "stop-hunt", "wick-sweep"],
  "criteria": [
    {"id": "c1", "expr": "high_or_low_breaches_pool == true"},
    {"id": "c2", "expr": "close_returns_inside_pool == true"},
    {"id": "c3", "expr": "wick_length_pct >= 0.6"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["liquidity-pool","liquidity-run","buy-side-liquidity","sell-side-liquidity","stop-run-definition","turtle-soup","judas-swing"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish-side (BSL) sweep                sell-side (SSL) sweep

                █  ← long upper wick          ▲   ← close back above
   ─────────────█────  BSL                    █
                █                             █
                ─ close back below           ─█──── SSL
                                              █  ← long lower wick
                                              █
```

The decisive feature is the close direction: opposite of the wick.

## Timeframes

Every TF. HTF sweeps (D, H4) are major reversal triggers; LTF sweeps are entry signals inside HTF setups.

## Examples

**Example 1 — Asian range BSL sweep:**
- Asian session high 1.0875 (BSL).
- London opens; M5 wicks to 1.0879, closes at 1.0871.
- Wick length ≈ 8 pips; close below the pool.
- → BSL sweep. Often the start of a Judas-swing-down setup.

## Common Mistakes

- **Mistaking sweep for BOS.** A wick-only break is a sweep, not a structural break. Use candle close.
- **Insisting on perfect reversal.** Some sweeps are followed by reversal; others are continuation steps where the algorithm gathered fuel and continues. Read the displacement direction afterward.
- **Single-bar fixation.** Sweeps can take 2–3 bars to play out (push above, hover, then close back). The defining feature is "broke the level, did not sustain the break."

## Related Concepts

- [liquidity-pool](liquidity-pool.md) — what gets swept.
- [liquidity-run](liquidity-run.md) — broader concept that includes the displacement that follows.
- [buy-side-liquidity](buy-side-liquidity.md) / [sell-side-liquidity](sell-side-liquidity.md) — types of pool.
- [stop-run-definition](../29-stop-runs/stop-run-definition.md) — same phenomenon in different naming.
- [turtle-soup](../20-turtle-soup/turtle-soup.md) — false-breakout pattern built on sweeps.
- [judas-swing](../13-judas-swing/judas-swing.md) — session-specific sweep pattern.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — sweep terminology refined.
- `ICT-2022-MENTORSHIP-OVERVIEW` — sweep operational use for entries.
