# Asian Range Sweep

**Category:** 14-asian-range
**Aliases:** Asia sweep, AR sweep, Asian liquidity raid
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** asian-range, sweep, raid, judas

## Definition

An Asian range sweep is the [liquidity-sweep](../02-liquidity/liquidity-sweep.md) of either the Asian range high or low at the start of the London session — typically inside the London Open killzone (02:00–05:00 NY) and frequently inside the 02:50–03:10 macro window. It is the canonical [judas-swing](../13-judas-swing/judas-swing.md) of the trading day. The sweep itself is a single-candle (or short-burst) wick through the bound, with the close back inside the range.

## Formal Criteria

For a high-side sweep:

- Price wicks above asian_range_high.
- The candle (or one of the next 1–2 candles) closes back below asian_range_high.
- Long upper wick relative to candle range.

For a low-side sweep: symmetric.

The sweep is the manipulation phase ([manipulation-phase](../12-power-of-three/manipulation-phase.md)) in a daily AMD cycle. Post-sweep, expect displacement in the opposite direction (the true delivery).

## Formula / Math

```
high_side_sweep := high(n) > asian_range_high
                    AND close(n) < asian_range_high
                    AND wick_top_pct(n) >= 0.6

low_side_sweep := low(n) < asian_range_low
                   AND close(n) > asian_range_low
                   AND wick_bottom_pct(n) >= 0.6
```

## Machine-Readable

```json
{
  "id": "asian-range-sweep",
  "category": "14-asian-range",
  "aliases": ["asia-sweep", "asian-liquidity-raid"],
  "criteria": [
    {"id": "c1", "expr": "wick_breaches_asian_range_bound == true"},
    {"id": "c2", "expr": "close_returns_inside_range == true"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["asian-range","asian-range-high","asian-range-low","liquidity-sweep","judas-swing","london-open-killzone","macro-time-0250-0310","manipulation-phase"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   high-side sweep                    low-side sweep
   asian_high ──┬────                       /  ← close back inside
                █  long wick                █
                █                           ─── asian_low
   ─ close back inside                      █
                                            █  long wick
```

## Timeframes

M1 / M5 / M15.

## Examples

**Example 1 — high-side sweep, bullish bias-aligned reversal:**
- Asian range 1.0848–1.0876.
- HTF bias bullish.
- 02:55 NY (LO-KZ + macro): M5 wicks 1.0879, closes 1.0871.
- Wait — bullish bias should make this a **continuation** sweep (i.e., the algorithm took fuel but is going up). Sweep direction up matches HTF bias = run-and-continue scenario.
- Confirmation needed: post-sweep, did the next 1–3 M5 candles displace up through 1.0879 with close + FVG? If yes, continuation; if displacement is down, the sweep WAS the Judas in a different setup (counter-bias, take only with reduced conviction).

**Example 2 — low-side sweep, bullish bias = textbook Judas:**
- Same range; HTF bullish.
- 02:55 NY: M5 wicks 1.0846 (Asian SSL), closes 1.0853.
- Bullish bias + low-side sweep = textbook Judas swing. Expect bullish displacement next.
- 03:05: M5 prints 18-pip green displacement, FVG at 1.0858. Entry zone confirmed.

## Common Mistakes

- **Sweep without bias context.** Any sweep is interpretable both ways (continuation vs reversal); HTF bias decides which.
- **Single-candle fixation.** Sweep can take 2–3 M5 candles to play out (push, hover, return). Defining feature is "broke the level, did not sustain it."
- **Trading the sweep instead of the post-sweep displacement.** Entry on the sweep wick gets stopped if it extends. Wait for the displacement direction confirmation.

## Related Concepts

- [asian-range](asian-range.md), [asian-range-high](asian-range-high.md), [asian-range-low](asian-range-low.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [judas-swing](../13-judas-swing/judas-swing.md), [london-open-killzone](../10-killzones/london-open-killzone.md), [macro-time-0250-0310](../04-time-cycles/macro-time-0250-0310.md), [manipulation-phase](../12-power-of-three/manipulation-phase.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
