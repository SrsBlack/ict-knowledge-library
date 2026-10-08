# Bearish Breaker

**Category:** 08-breaker-blocks
**Aliases:** bearish breaker block, BeBB
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-BREAKER-BLOCK, ICT-2017-HTF-PD-ARRAYS, ICT-2022-MENTORSHIP-EP18, ICT-2022-MENTORSHIP-EP39
**Tags:** breaker, bearish

⚠ **Rewritten 2026-10-08; geometry and an EP39 misattribution corrected in review.** The prior "close
below the OB body with displacement" rule and the 2017/2023 dating are both contradicted by the
primary lecture — see [breaker-block](breaker-block.md) and [bullish-breaker](bullish-breaker.md)
for the shared evidence and the corrected candle-order.

## Definition

A bearish breaker is **"a bearish range or down close candle in the most recent swing low prior to an
old high being violated. The buyers that buy this low and later see this same swing low violated
will look to mitigate the loss."** (`ICT-2016-BREAKER-BLOCK` [03:13–03:22]). The antecedent is a run
on an old high: "what we are looking for is an old high to be ran out, or a false break above an old
high." [04:20]. Jan-2017 restates the sequence directly: "when an old high is taken out, that down
candle right before the second high is made, taking out an old high — or turtle soup, in other words
— that down candle, if it's retraded to, that's going to be a bearish breaker."
(`ICT-2017-HTF-PD-ARRAYS` [21:14–21:23]). 2022: "this down closed candle — the lowest one prior to
[the] move up clearing that short-term high" (EP39 [20:50]).

**The breaker candle forms BEFORE the run, not after.** Required sequence, in time order: an old
high (H1) exists → price drops and forms a swing low — this down-close candle is the breaker candle,
already in place ("in the most recent swing low **prior to** an old high being violated" [03:13]) →
price then rallies to a higher high (H2) that trades above H1, running the stops resting above it →
only then does price break back down **through that same, already-existing swing low** — the
structure break that confirms H2 was a stop run, not a continuation up. The consequence for the longs
trapped at the first low is explicit: "the low that is violated here once market structure is broken
down, and all future retracements will be viewed as new selling opportunities." [04:48]. The retest
from below, into the breaker candle's range, offers resistance.

On one worked 2022 chart, ICT rejects a candidate that looks like a bearish breaker by eye — see
Examples and Common Mistakes for that passage (EP18 [02:29]). It is not generalised here into a
separate formal gate; the Formal Criteria below are the run/break/zone/retest sequence only.

## Formal Criteria

- **The breaker candle (a down-close candle) forms first** — it sits at the swing low **between two
  highs**, before either high is run.
- **Only afterward** is an old high run: the second, higher high trades through the first, running
  the stops above it.
- **Only then** does price break back through the pre-existing swing low — the structural
  confirmation that the high run was a stop run, not a continuation up.
- The breaker candle's zone is its **entire range**, not body only.
- On retest from below, the zone offers resistance.

## Formula / Math

```
# H1, H2 = two highs in time order (H2 is the higher, later one).

bearish_breaker_candle := the down-close candle forming the swing low BETWEEN H1 and H2
                           # this candle EXISTS BEFORE H2 forms — it is not produced by the run
bearish_breaker_zone := [low(candle), high(candle)]     # ENTIRE RANGE

old_high_run := H2 trades above H1, running the stops resting above H1   # happens AFTER the candle above
swing_low_break := price (later) breaks back through bearish_breaker_candle's low
                    # confirms H2 was stops, not a continuation up

bearish_breaker_confirmed := old_high_run AND swing_low_break
retest_resistance := price returns into bearish_breaker_zone from below, then sells off
```

## Machine-Readable

```json
{
  "id": "bearish-breaker",
  "category": "08-breaker-blocks",
  "aliases": ["bearish-breaker-block", "BeBB"],
  "criteria": [
    {"id": "c1", "expr": "breaker_candle := the down-close candle at the swing low BETWEEN two highs, formed BEFORE either high is run"},
    {"id": "c2", "expr": "old_high_run := the second, higher high trades above the first, AFTER breaker_candle has formed"},
    {"id": "c3", "expr": "swing_low_break := price later breaks back through breaker_candle's low (structure break)"},
    {"id": "c4", "expr": "breaker_zone := ENTIRE RANGE of breaker_candle, not the body"},
    {"id": "c5", "expr": "retest from below acts as resistance"}
  ],
  "timeframes": ["M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["breaker-block","bullish-breaker","bullish-order-block","mitigation-block"],
  "sources": ["ICT-2016-BREAKER-BLOCK","ICT-2017-HTF-PD-ARRAYS","ICT-2022-MENTORSHIP-EP18","ICT-2022-MENTORSHIP-EP39"]
}
```

## Visual Pattern

```
   bearish breaker formation (candle forms FIRST, then the run, then the structure break):

   Step 1: old high H1 forms; price drops, forming a swing low — THIS down-close candle
           is the bearish breaker, already in place (ENTIRE RANGE, not just its body)
   Step 2: price rallies to a HIGHER high H2, trading above H1 — runs the stops above H1
           (the liquidity event — happens AFTER Step 1, not before)
   Step 3: price breaks back DOWN through the swing low from Step 1
           (structure break; confirms H2 was stops, not a continuation up)
   Step 4: retest from below -> rejection down -> confirmed resistance
```

## Timeframes

No floor stated — see [breaker-block](breaker-block.md).

## Examples

**Example 1 — schematic, following the lecture sequence:**
- An old high (H1) forms; price drops to a swing low — the (future) bearish breaker candle.
- Price later rallies to a higher high (H2), trading above H1 and running the stops above it.
- Price reverses and breaks back down through the Step-1 swing low — confirming a stop run, not a
  continuation up.
- The down-close candle at that swing low is the bearish breaker; its full range is the reference.
- Later retest from below holds and price sells off.

**Example 2 — a cautionary one, from ICT's own 2022 chart:** ICT points at a candidate on his chart
that an audience member might call a bearish breaker by eye, and rejects it: "many of you would see
that as my bearish breaker — mhm, it's not, okay? So, look at this here. Which is lower? Is it this
low here, or the discount low of the fair value gap? In other words, this candle's high." (EP18
[02:29]). On that specific chart the true lower reference was a different level entirely (a nearby
candle's high, lower than the candidate's own low) — a one-off worked correction, not a separate
formal gate on top of the run/break/zone/retest criteria above.

## Common Mistakes

- **"Close below the OB body" as the break rule.** Not ICT's wording; the requirement is the break of
  the pre-existing swing low itself.
- **Putting the breaker candle after the run.** It forms BEFORE the high run, not as a result of it —
  see [breaker-block](breaker-block.md) Common Mistakes.
- **Citing EP39's "gamble" line as proof the liquidity run is mandatory.** As on
  [bullish-breaker](bullish-breaker.md): in context "that" refers to knowing the market's expected
  draw, not the run. The run itself is evidenced by `ICT-2016-BREAKER-BLOCK` [04:20] ("an old high to
  be ran out") and [03:13] ("prior to an old high being violated").
- **Treating ICT's chart-specific correction (Example 2) as a universal formal gate.** EP18 [02:29]
  is ICT rejecting one candidate on one chart by pointing to a lower competing level — it is not a
  general "check the lowest nearby reference" criterion to add to every bearish breaker.
- **Mistaken polarity.** A bearish breaker's candle sits at a swing **low** (not a swing high),
  between two highs, in anticipation of resistance on a return from below.

## Related Concepts

- [breaker-block](breaker-block.md), [bullish-breaker](bullish-breaker.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [mitigation-block](mitigation-block.md).

## Citations

- `ICT-2016-BREAKER-BLOCK` [03:13–03:22] "a bearish breaker is a bearish range or down close candle in the most recent swing low prior to an old high being violated"; [04:20] "an old high to be ran out, or a false break above an old high"; [04:48] "the low that is violated here … all future retracements will be viewed as new selling opportunities."
- `ICT-2017-HTF-PD-ARRAYS` [21:14–21:23] "when an old high is taken out, that down candle … that's going to be a bearish breaker."
- `ICT-2022-MENTORSHIP-EP18` [02:29] "many of you would see that as my bearish breaker … mhm, it's not, okay? So, look at this here. Which is lower? Is it this low here, or the discount low of the fair value gap? In other words, this candle's high." — a technical comparison against a competing lower level, not a narrative judgment.
- `ICT-2022-MENTORSHIP-EP39` [20:50] "this down closed candle, the lowest one prior to move up clearing that short-term high" (candle-selection detail only; the "gamble" clause from this episode is cited on [breaker-block](breaker-block.md) and [bullish-breaker](bullish-breaker.md) as a separate narrative-gate requirement, not evidence for the liquidity-run requirement here).
