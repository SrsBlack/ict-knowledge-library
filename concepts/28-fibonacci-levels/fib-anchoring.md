# Fib Anchoring — Bodies, Not Wicks

**Category:** 28-fibonacci-levels
**Aliases:** body anchoring, candle-body fib, where to drop the fib, fib attachment points
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2020
**Source IDs:** ICT-2017-OTE, ICT-2017-OTE-AUSSIE-NYO, ICT-2017-OTE-FIBER-NYO, ICT-2017-OTE-DRILL-FIBER, ICT-2017-OTE-DRILL-GOLD, ICT-2017-OTE-DRILL-USDJPY, ICT-2017-OTE-DRILL-USDCAD, ICT-2017-OTE-USDCAD-REVIEW, ICT-2017-OTE-LONDON-DEMO, ICT-2020-OTE-EURUSD-EXAMPLE, ICT-2020-OTE-VOL01, ICT-2020-OTE-VOL13
**Tags:** fibonacci, fib, ote, anchoring, candle-body, measurement

## Definition

When ICT drops a fib on a measured swing leg, the two attachment points are **candle-body extremes, not wick extremes**. The stated reason is data quality rather than theory: wicks are the part of a candle that differs most between brokers, so a wick-anchored measurement is not reproducible across feeds. Because every retracement and projection level is computed from `leg_size`, the anchoring choice propagates into the entire level set — the OTE band, the stop at fib 1.0, and every target. Two traders drawing "the same" fib on the same leg will disagree on every level if one anchors to wicks.

This rule governs the **fib tool only**. PD arrays keep their own anchoring conventions — an order block "is starting at the wick" (`ICT-2020-OTE-VOL01`).

⚠ **Scope narrowed 2026-08-11 — the bodies rule is stated for the *retracement*, and ICT names two places he uses wicks instead.** A sweep of the 21 remaining non-Core OTE packets found **eight independent restatements of the bodies rule and zero contradictions**, but two of those packets also carve out exceptions the library did not previously record:

1. **Target projections may incorporate wicks.** "It's real important — that's the reason why I'm doing it [not] on the wicks. Now, when I do **projections on targets**, sometimes I will **incorporate wicks**, but you'll learn that in the tutorials. But for now I'm kind of keep things germane and salient to the original rules — we're just using the body of the candles" (`ICT-2017-OTE-DRILL-GOLD`, 04:17–04:31). ⚠ The whisper transcript renders the first clause as "that's the reason why I'm doing it **now** on the wicks", which inverts the sentence; the surrounding clauses ("we're getting the measurement of the bulk of the volume", "we're just using the body of the candles") make "not on the wicks" the only coherent reading. Flagged rather than silently repaired. The exception is qualified — "sometimes" — and no rule is given for when.
2. **A late-entry validity ceiling uses the wick high, and ICT says so explicitly.** Having missed the ideal fill, he re-anchors: "**Now I'm using the high for this now. Not the body.** This is when you want to [bring] in the wicks from the point at which you draw the fib up to. You want to find the **highest high**. As long as we're at that level or below it, I would be OK with getting long on it" (`ICT-2017-OTE-USDCAD-REVIEW`, 13:28–13:44). This is a separate decision from where the fib attaches — the fib in that same video is body-anchored [11:32] — so it does not weaken the retracement rule; it means an implementation needs **two** swing-extreme functions, not one.

## Formal Criteria

- The leg-end anchor is the **highest body** (bullish leg) or **lowest body** (bearish leg) of the terminal swing — not the extreme of its wick.
- The leg-origin anchor is likewise the body extreme of the origin swing.
- For a candle whose body extreme is the anchor, the price used is that candle's **open or close**, whichever is the relevant extreme. In the Primer's worked example the highest body belongs to a down-close candle, so the anchor price is its **open**. Restated twice in the 2017 drills: "we're using the **highest open or close** down to the **lowest bodied open or close**" (`ICT-2017-OTE-DRILL-USDJPY`, 01:07); "it's the lowest close — it could be open down here as well, guys; it's not the close is [the] important factor" (`ICT-2017-OTE-DRILL-GOLD`, 04:02–04:10).
- Wick extremes are used for **structure and PD-array identification** (swing pivots, order-block boundaries) but not as fib attachment points. Two further wick uses are disclosed above: target projections (sometimes) and the late-entry ceiling.
- **Zone-tolerance is judged on bodies too.** When price overshoots the 0.79 boundary on a wick, the setup still stands if the bodies hold: "overshot just a little bit here, but here that's okay — now the **bodies are certainly respecting** that … area of high probability entry" (`ICT-2017-OTE-LONDON-DEMO`, 04:11–04:24).
- **Leg selection between two candidate swing highs is decided on bodies.** Given two adjacent highs, ICT takes the lower-wicked one when its body is the dominant one: "you can see this one's slightly higher than this one, but this one's where all the volume is, and you see that with the **bodies of candles versus this wick**" (`ICT-2020-OTE-VOL13`, 02:37–02:50).

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

# TWO wick-based references coexist with the body-anchored fib (2026-08-11):
#   projection_anchor  := MAY use high_n / low_n   (ICT-2017-OTE-DRILL-GOLD 04:17, "sometimes")
#   late_entry_ceiling := max(high_n) over terminal swing   # NOT body_high
#                         long is acceptable while price <= late_entry_ceiling
#                         (ICT-2017-OTE-USDCAD-REVIEW 13:28)
#
# zone tolerance is body-based:
#   valid_touch := body_low(n) within [0.62, 0.79]   # a wick beyond 0.79 does not void it
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
    {"id": "c3", "expr": "wick_extremes_used_as_retracement_fib_anchor == false"},
    {"id": "c4", "expr": "order_block_boundary_anchor == wick", "strength": "contrast"},
    {"id": "c5", "expr": "projection_anchor MAY include wick", "strength": "disclosed exception, 'sometimes'"},
    {"id": "c6", "expr": "late_entry_ceiling == max(high) over terminal swing", "strength": "disclosed exception"},
    {"id": "c7", "expr": "zone_tolerance judged on body, not wick"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2020",
  "related": ["ict-fib-overview","fib-62","fib-705","fib-79","fib-vs-ote","symmetrical-price-projections","ote-overview","ote-rules","bullish-order-block"],
  "sources": ["ICT-2017-OTE","ICT-2017-OTE-AUSSIE-NYO","ICT-2017-OTE-FIBER-NYO","ICT-2017-OTE-DRILL-FIBER","ICT-2017-OTE-DRILL-GOLD","ICT-2017-OTE-DRILL-USDJPY","ICT-2017-OTE-DRILL-USDCAD","ICT-2017-OTE-USDCAD-REVIEW","ICT-2017-OTE-LONDON-DEMO","ICT-2020-OTE-EURUSD-EXAMPLE","ICT-2020-OTE-VOL01","ICT-2020-OTE-VOL13"]
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
- **Voiding a setup because a wick pierced 0.79.** Tolerance is read on the bodies (`ICT-2017-OTE-LONDON-DEMO`, 04:17). A wick overshoot is expected, not disqualifying.
- **Generalising "bodies" to every fib on the chart.** The rule is stated for the *retracement*. ICT says projections sometimes use wicks, and he uses the wick high outright for the late-entry ceiling. A single global anchoring switch gets at least one of the three wrong.
- **Loose phrasing in the later videos is not a rule change.** `ICT-2021-OTE-PRICE-ACTION-LESSON` says only "if we take our fib and anchor it to the high, to the low" [04:07] with no body/wick qualifier. That is an unspecific description in a bias-focused lesson, not a restatement — no source located in the 43-video OTE population states a wick anchor for a retracement fib.

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
- `ICT-2017-OTE-AUSSIE-NYO` — the rule in full: lowest body, open or close whichever is lowest, dragged to the highest body.
- `ICT-2017-OTE-FIBER-NYO` — "lowest body portion" anchoring.
- `ICT-2017-OTE-DRILL-FIBER` — "I'm going to use this body open inside this swing"; "we're using the lowest body candle here."

Added 2026-08-11 from the 21 remaining non-Core OTE packets:

- `ICT-2017-OTE-DRILL-USDJPY` (01:07) — "we're using the **highest open or close** down to the **lowest bodied open or close**, and it takes us right up into 62% retracement level"; (02:27) "you can use this range down here to the **lowest bodied candle** right here."
- `ICT-2017-OTE-DRILL-USDCAD` (00:49–00:59) — "all we need to do is look at the **bodies of the candles** low up to the **bodies of the candle** here, high."
- `ICT-2017-OTE-DRILL-GOLD` (03:55–04:31) — "we take the low up to the **highest body** … it's the lowest close, it could be open down here as well, guys; it's not the close is [the] important factor … so we're getting the **measurement of the bulk of the volume**"; then the projection exception: "when I do projections on targets, sometimes I will incorporate wicks … but for now I'm kind of keep things germane and salient to the original rules — we're just using the body of the candles."
- `ICT-2017-OTE-USDCAD-REVIEW` (00:34, 00:48) — "I'm using this body here … I'm using this right here, the **open** on this candle here"; (11:32–11:45) "you can see I have the **body** on this swing low. The open on this candle is the lowest of the body. **Reference points open or close**"; (13:28–13:44) the wick-based late-entry ceiling — "now I'm using the high for this now, **not the body** … you want to find the highest high."
- `ICT-2017-OTE-LONDON-DEMO` (04:11–04:24) — "overshot just a little bit here, but here that's okay — now the **bodies are certainly respecting** that … area of high probability entry."
- `ICT-2020-OTE-VOL13` (02:37–02:50) — leg selection between two swing highs decided on bodies: "this one's slightly higher than this one, but this one's where all the volume is, and you see that with the **bodies of candles versus this wick**."
