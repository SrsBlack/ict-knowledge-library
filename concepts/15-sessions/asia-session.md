# Asia Session

**Category:** 15-sessions
**Aliases:** Asian session, Tokyo session, Asia trading hours
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** sessions, asia, accumulation, foundational

## Definition

The Asia session covers the overnight trading window from 18:00 NY (prev day) to 03:00 NY (or 19:00 → 04:00 during non-DST). It is characterized by **low volatility, range-building, and accumulation** — institutions are typically not delivering large directional moves during Asia. The Asian range that forms here (Asian high and Asian low) becomes a primary set of liquidity pools for the London open, which routinely sweeps one side as part of its [judas-swing](../13-judas-swing/judas-swing.md).

## Formal Criteria

- Time window: 18:00 NY (prev day) → 03:00 NY (DST) / 19:00 → 04:00 (non-DST).
- Volatility: typically the lowest of any session (ATR ~30–50% of London/NY ATR).
- Behavior: range-bound, overlapping candles, often produces equal highs and equal lows along the bounds.
- Output: an Asian range high (BSL pool) and Asian range low (SSL pool) that London targets.

## Formula / Math

```
asia_window = [18:00 NY prev day, 03:00 NY]    # DST, simplified

asian_high = max(high(t)) for t in asia_window
asian_low  = min(low(t))  for t in asia_window
asian_range = asian_high - asian_low
```

## Machine-Readable

```json
{
  "id": "asia-session",
  "category": "15-sessions",
  "aliases": ["asian-session", "tokyo-session"],
  "criteria": [
    {"id": "c1", "expr": "time_in [18:00_prev, 03:00] NY"},
    {"id": "c2", "expr": "volatility low relative to London/NY"},
    {"id": "c3", "expr": "produces asian_high and asian_low"}
  ],
  "timeframes": ["M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["asian-range","asian-range-high","asian-range-low","london-session","judas-swing","range-contraction","accumulation-phase"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   18:00 (prev) ────────────────── 03:00 (NY time)

   Asian high ────────────────────── ← BSL pool
                /\  /\
               /  \/  \   ← tight, overlapping
              /        \      candles
             /          \
   Asian low ───────────────────── ← SSL pool
```

## Timeframes

Most analysis uses M15 / H1 to identify the Asian range; M5 for the actual range bounds and equal-high / equal-low formation; H4 for context.

## Examples

**Example 1 — typical Asia → London setup:**
- Asia produces a 30-pip range on EURUSD: high 1.0875, low 1.0845.
- London opens at 03:00 NY; M5 wicks the Asian high (1.0879) and closes at 1.0871.
- → Asian BSL swept; Judas swing complete; long-bias setups now look for Asian-low SSL test or direct rally.

## Common Mistakes

- **Treating Asia as random noise.** The Asian range is *deliberately* engineered liquidity by accumulation-phase delivery; ignoring it loses one of the most reliable session-based reads.
- **Using server-time bounds.** If your charts are on GMT or broker time, the "Asia session" displayed will be offset; always anchor to NY time.
- **Trading Asia mean-reversion blindly.** Asian breakouts late in the session (last hour) sometimes signal continuation, not noise.

## Related Concepts

- [asian-range](../14-asian-range/asian-range.md) — the price range Asia produces.
- [asian-range-high](../14-asian-range/asian-range-high.md) / [asian-range-low](../14-asian-range/asian-range-low.md) — the bounds.
- [london-session](london-session.md) — the session that follows and exploits Asia.
- [judas-swing](../13-judas-swing/judas-swing.md) — typical post-Asia pattern.
- [range-contraction](../01-market-structure/range-contraction.md) — Asia is the canonical contraction phase.
- [accumulation-phase](../12-power-of-three/accumulation-phase.md) — AMD-cycle equivalent.

## Citations

- `ICT-2016-KILLZONES` — Asia kill zone (subset of session) defined.
- `ICT-2022-MENTORSHIP-OVERVIEW` — Asia as the accumulation window in daily AMD.
