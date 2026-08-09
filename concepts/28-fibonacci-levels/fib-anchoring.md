# Fib Anchoring — Bodies, Not Wicks

**Category:** 28-fibonacci-levels
**Aliases:** body anchoring, candle-body fib, where to drop the fib, fib attachment points
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2020
**Source IDs:** ICT-2017-OTE, ICT-2017-OTE-AUSSIE-NYO, ICT-2017-OTE-FIBER-NYO, ICT-2017-OTE-DRILL-FIBER, ICT-2020-OTE-EURUSD-EXAMPLE, ICT-2020-OTE-VOL01
**Tags:** fibonacci, fib, ote, anchoring, candle-body, measurement

## Definition

When ICT drops a fib on a measured swing leg, the two attachment points are **candle-body extremes, not wick extremes**. The stated reason is data quality rather than theory: wicks are the part of a candle that differs most between brokers, so a wick-anchored measurement is not reproducible across feeds. Because every retracement and projection level is computed from `leg_size`, the anchoring choice propagates into the entire level set — the OTE band, the stop at fib 1.0, and every target. Two traders drawing "the same" fib on the same leg will disagree on every level if one anchors to wicks.

This rule governs the **fib tool only**. PD arrays keep their own anchoring conventions — an order block "is starting at the wick" (`ICT-2020-OTE-VOL01`).

## Formal Criteria

- The leg-end anchor is the **highest body** (bullish leg) or **lowest body** (bearish leg) of the terminal swing — not the extreme of its wick.
- The leg-origin anchor is likewise the body extreme of the origin swing.
- For a candle whose body extreme is the anchor, the price used is that candle's **open or close**, whichever is the relevant extreme. In the Primer's worked example the highest body belongs to a down-close candle, so the anchor price is its **open**.
- Wick extremes are used for **structure and PD-array identification** (swing pivots, order-block boundaries) but not as fib attachment points.

## Formula / Math

```
body_high(n) := max(open_n, close_n)
body_low(n)  := min(open_n, close_n)

# bullish leg (origin swing O, terminal swing T):
leg_start := min( body_low(n)  for n in O )
leg_end   := max( body_high(n) for n in T )

# bearish leg:
leg_start := max( body_high(n) for n in O )
leg_end   := min( body_low(n)  for n in T )

leg_size  := leg_end - leg_start        # signed by direction

# NOT used as anchors:
#   high_n, low_n   (wick extremes)

# Primer worked example, EURUSD M15 (ICT-2017-OTE, ~36:28):
#   highest body of the terminal swing is a down-close candle
#   leg_end = open of that candle = 1.1799
#   the wick above 1.1799 is deliberately excluded
```

## Machine-Readable

```json
{
  "id": "fib-anchoring",
  "category": "28-fibonacci-levels",
  "aliases": ["body-anchoring", "candle-body-fib"],
  "criteria": [
    {"id": "c1", "expr": "leg_end == max(body_high) over terminal swing (bullish)"},
    {"id": "c2", "expr": "leg_start == min(body_low) over origin swing (bullish)"},
    {"id": "c3", "expr": "wick_extremes_used_as_fib_anchor == false"},
    {"id": "c4", "expr": "order_block_boundary_anchor == wick", "strength": "contrast"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2020",
  "related": ["ict-fib-overview","fib-62","fib-705","fib-79","fib-vs-ote","symmetrical-price-projections","ote-overview","ote-rules","bullish-order-block"],
  "sources": ["ICT-2017-OTE","ICT-2017-OTE-AUSSIE-NYO","ICT-2017-OTE-FIBER-NYO","ICT-2017-OTE-DRILL-FIBER","ICT-2020-OTE-EURUSD-EXAMPLE","ICT-2020-OTE-VOL01"]
}
```

## Visual Pattern

```
   terminal swing of a bullish leg:

          │        ← wick high        NOT the anchor
        ┌─┴─┐
        │   │  ← open of a down-close candle = highest body
        │   │     ══════════════════  fib 0.0 DROPPED HERE
        └─┬─┘
          │

   origin swing:

          │
        ┌─┴─┐
        │   │
        └─┬─┘  ← lowest body           fib 1.0 DROPPED HERE
          │       ══════════════════
          │    ← wick low             NOT the anchor

   The excluded wick span is exactly the part of the candle
   that varies between brokers.
```

## Timeframes

All TFs. The absolute error from wick-anchoring scales with candle range, so the distortion is largest on HTF legs and on high-volatility sessions.

## Examples

**Example 1 — EURUSD M15, Primer worked example (`ICT-2017-OTE`, 35:36–39:12):**
- Impulse leg breaks an intermediate-term high; the fib is drawn on that leg.
- ICT identifies "the highest body right there, this candle right there… we're going to look at that as the open, so the open is 1.1799" and drops fib 0.0 at **1.1799**.
- The candle's wick trades above 1.1799; that span is excluded by design.
- The symmetrical price projection is measured on the same convention — "this low to this body's high is the same thing from that body's high all the way up to this level".

**Example 2 — EURUSD, worked bearish example (`ICT-2020-OTE-EURUSD-EXAMPLE`, 01:37):**
- Three candles form one bearish order block containing the OTE.
- "Take particular attention to the candles bodies because that's going to be important in a moment."

## Common Mistakes

- **Anchoring to wicks.** The default on most charting tools is to snap to the high/low. Every level then shifts, including the stop at fib 1.0 — producing a different trade from the taught one while looking identical on the screen.
- **Applying the body rule to PD arrays.** Order-block boundaries start at the wick (`ICT-2020-OTE-VOL01`). Fib anchoring and PD-array anchoring are separate conventions; a codebase that picks one globally gets the other wrong.
- **Assuming the body extreme is a close.** It is whichever of open/close is more extreme. In the Primer's example the anchor is an **open**.
- **Treating this as cosmetic.** It changes `leg_size`, so it changes the OTE band, the stop, and every target. It is load-bearing, not a preference.

## Related Concepts

- [ict-fib-overview](ict-fib-overview.md) — the level set this anchoring feeds.
- [fib-62](fib-62.md), [fib-705](fib-705.md), [fib-79](fib-79.md) — the retracement levels computed from these anchors.
- [symmetrical-price-projections](symmetrical-price-projections.md) — measured on the same body-to-body convention.
- [fib-vs-ote](fib-vs-ote.md) — disambiguation of the tool from the setup.
- [ote-overview](../17-optimal-trade-entry/ote-overview.md), [ote-rules](../17-optimal-trade-entry/ote-rules.md) — the setup that consumes these levels.
- [bullish-order-block](../07-order-blocks/bullish-order-block.md) — the contrasting wick-anchored convention.

## Citations

- `ICT-2017-OTE` (35:36) — "we want to look at the price move on the bodies of the candles… the wicks are always going to be the thinnest price action"; (35:47) "across all different platforms and brokers, the part that's always different that throws everyone off is the wicks, because the broker is allowed to have some measure of flexibility"; (36:28) "we're going to put on the bodies of candles up here, this is the highest body right there… we're going to look at that as the open, so the open is 1.1799, so that's where our fib will be dropped"; (39:06) "this low to this body's high is the same thing from that body's high all the way up to this level".
- `ICT-2020-OTE-EURUSD-EXAMPLE` (01:37) — "Take particular attention to the candles bodies because that's going to be important in a moment."
- `ICT-2020-OTE-VOL01` (13:56) — "The order block is starting at the wick." Establishes the contrasting PD-array convention.
