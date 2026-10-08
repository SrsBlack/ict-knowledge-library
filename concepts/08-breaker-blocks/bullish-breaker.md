# Bullish Breaker

**Category:** 08-breaker-blocks
**Aliases:** bullish breaker block, BBB
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-BREAKER-BLOCK, ICT-2017-HTF-PD-ARRAYS, ICT-2017-OTE-DRILL-AUSUSD
**Tags:** breaker, bullish

⚠ **Rewritten 2026-10-08; geometry and an EP39 misattribution corrected in review.** The prior "close
above the OB high with displacement" rule and the 2017/2023 dating are both contradicted by the
primary lecture — see [breaker-block](breaker-block.md) for the shared evidence and the corrected
candle-order.

## Definition

A bullish breaker is **"a bullish range or up close candle in the most recent swing high prior to an
old low being violated"** (`ICT-2016-BREAKER-BLOCK` [05:08]). Equivalently, from the PD-array
hierarchy lecture: "a bullish breaker is a up candle between two swing lows and the most recent swing
low would be lower. Normally, you're seeing a stop run in the past, and the high — the swing high
that it forms between the two lows — that up candle is going to be your bullish breaker."
(`ICT-2017-HTF-PD-ARRAYS` [27:48–28:02]).

**The breaker candle forms BEFORE the run, not after.** Required sequence, in time order: an old low
(L1) exists → price rallies and forms a swing high — this up-close candle is the breaker candle,
already in place → price then drops to a lower low (L2) that trades below L1, running the stops
resting beneath it: "again, focusing on the high in between the two lower lows, one low has to be
traded below, and that is going to run out to sell stops" (`ICT-2016-BREAKER-BLOCK` [02:11–02:24]) →
only then does price break back up **through that same, already-existing swing high** — the
structure break that confirms L2 was a stop run, not a trend change down: "we have to wait for price
to break through that swing high to confirm that there has been a run on stops"
(`ICT-2016-BREAKER-BLOCK` [05:41]). The market structure shift this produces is explicit: "the old
high that is violated — that supports a market structure shift for bullishness" [06:56]. The retest
from above, into the breaker candle's range, offers support.

Already named in a 2017 pattern-recognition drill: "stop run here, which is a bullish breaker — it's
an ICT bullish breaker" (`ICT-2017-OTE-DRILL-AUSUSD` [00:42]).

## Formal Criteria

- **The breaker candle (an up-close candle) forms first** — it sits at the swing high **between two
  lows**, before either low is run: "a up candle between two swing lows" (`ICT-2017-HTF-PD-ARRAYS`
  [27:48]).
- **Only afterward** is an old low run: the second, lower low trades through the first, running the
  stops beneath it (`ICT-2016-BREAKER-BLOCK` [02:11–02:24]).
- **Only then** does price break back through the pre-existing swing high — the structural
  confirmation that the low run was a stop run, not a reversal ([05:41]).
- The breaker candle's zone is its **entire range**, not its body alone (see
  [breaker-block](breaker-block.md) [09:17–09:19]).
- On retest from above, the zone offers support.
- No "close above the OB high" rule and no displacement requirement are stated for the break itself —
  the requirement is that price *break through the swing high*, which can be read on the wick/swing
  extreme.

## Formula / Math

```
# L1, L2 = two lows in time order (L2 is the lower, later one).

bullish_breaker_candle := the up-close candle forming the swing high BETWEEN L1 and L2
                           # this candle EXISTS BEFORE L2 forms — it is not produced by the run
bullish_breaker_zone := [low(candle), high(candle)]     # ENTIRE RANGE

old_low_run := L2 trades below L1, running the stops resting beneath L1   # happens AFTER the candle above
swing_high_break := price (later) breaks back through bullish_breaker_candle's high
                     # confirms L2 was stops, not a reversal

bullish_breaker_confirmed := old_low_run AND swing_high_break
retest_support := price returns into bullish_breaker_zone from above, then rallies away
```

## Machine-Readable

```json
{
  "id": "bullish-breaker",
  "category": "08-breaker-blocks",
  "aliases": ["bullish-breaker-block", "BBB"],
  "criteria": [
    {"id": "c1", "expr": "breaker_candle := the up-close candle at the swing high BETWEEN two lows, formed BEFORE either low is run"},
    {"id": "c2", "expr": "old_low_run := the second, lower low trades below the first, AFTER breaker_candle has formed"},
    {"id": "c3", "expr": "swing_high_break := price later breaks back through breaker_candle's high (structure break)"},
    {"id": "c4", "expr": "breaker_zone := ENTIRE RANGE of breaker_candle, not the body"},
    {"id": "c5", "expr": "retest from above acts as support"}
  ],
  "timeframes": ["M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["breaker-block","bearish-breaker","bearish-order-block","mitigation-block"],
  "sources": ["ICT-2016-BREAKER-BLOCK","ICT-2017-HTF-PD-ARRAYS","ICT-2017-OTE-DRILL-AUSUSD"]
}
```

## Visual Pattern

```
   bullish breaker formation (candle forms FIRST, then the run, then the structure break):

   Step 1: old low L1 forms; price rallies, forming a swing high — THIS up-close candle
           is the bullish breaker, already in place (ENTIRE RANGE, not just its body)
   Step 2: price drops to a LOWER low L2, trading below L1 — runs the stops beneath L1
           (the liquidity event — happens AFTER Step 1, not before)
   Step 3: price rallies back and BREAKS THROUGH the swing high from Step 1
           (structure break; confirms L2 was stops, not a reversal — market structure shift up)
   Step 4: retest from above -> rejection up -> confirmed support
```

## Timeframes

No floor stated — see [breaker-block](breaker-block.md).

## Examples

**Example 1 — schematic, following the lecture sequence:**
- An old low (L1) forms; price rallies to a swing high — the (future) bullish breaker candle.
- Price later drops to a lower low (L2), trading below L1 and running the stops beneath it.
- Price reverses and breaks back up through the Step-1 swing high — confirming a stop run, not a
  trend change down.
- The up-close candle at that swing high is the bullish breaker; its full range is the reference.
- Later retest from above holds and price rallies away.

## Common Mistakes

- **"Close above the OB high" as the break rule.** Not ICT's wording; the requirement is that price
  break through the pre-existing swing high.
- **Putting the breaker candle after the run.** It forms BEFORE the low run, not as a result of it —
  see [breaker-block](breaker-block.md) Common Mistakes.
- **Citing EP39's "gamble" line as proof the liquidity run is mandatory.** In context, "that" refers
  to knowing the market's expected draw, not the run: "you must know what the market's likely to be
  reaching for; if you leave that out, it's not a breaker — it's a gamble" (EP39 [20:25–20:50]). The
  run itself is evidenced instead by `ICT-2016-BREAKER-BLOCK` [02:11–02:24] ("one low has to be
  traded below") and [05:08] ("prior to an old low being violated").
- **Reversed polarity.** A bullish breaker's candle sits at a swing **high** (not a swing low),
  between two lows, in anticipation of support on a return from above.
- **Treating displacement on the break as required.** Not stated; the requirement is the structural
  break of the swing extreme itself.

## Related Concepts

- [breaker-block](breaker-block.md), [bearish-breaker](bearish-breaker.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [mitigation-block](mitigation-block.md).

## Citations

- `ICT-2016-BREAKER-BLOCK` [02:11–02:24] "again, focusing on the high in between the two lower lows, one low has to be traded below, and that is going to run out to sell stops"; [05:08] "for a bullish breaker, it is a bullish range or up close candle in the most recent swing high prior to an old low being violated"; [05:41] break through the swing high confirms the stop run; [06:56] market structure shift for bullishness.
- `ICT-2017-HTF-PD-ARRAYS` [27:48–28:02] "a bullish breaker is a up candle between two swing lows … that up candle is going to be your bullish breaker."
- `ICT-2017-OTE-DRILL-AUSUSD` [00:42] "stop run here, which is a bullish breaker — it's an ICT bullish breaker" (already named by 2017, independent of the Dec-2016 dating).
