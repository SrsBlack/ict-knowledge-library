# Breaker Block

**Category:** 08-breaker-blocks
**Aliases:** BB, breaker
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-BREAKER-BLOCK, ICT-2016-TIMEFRAME-SELECTION, ICT-2016-INSTITUTIONAL-ORDER-FLOW, ICT-2017-INSTITUTIONAL-SWING-POINTS, ICT-2017-HTF-PD-ARRAYS, ICT-2017-TRADE-CONDITIONS, ICT-2020-OTE-VOL04, ICT-2022-MENTORSHIP-EP39
**Tags:** breaker, ob-flipped, foundational

⚠ **Rewritten 2026-10-08.** The prior definition omitted the defining antecedent (a liquidity/stop
run) and used a body-only break/zone; both are contradicted by the primary lecture. `Year Introduced`
corrected 2017 → 2016; the source had been a stub (`ICT-2017-CHARTER-OVERVIEW`) that never attested
the breaker.

## Definition

A **breaker block** is a swing point built around a **pre-existing swing high/low that later gets
run through by a stop run, then broken back through on the way back**. ⚠ **The breaker candle forms
BEFORE the run, sitting between the two lows (bullish case) or two highs (bearish case) — it is not
formed by the run itself.** For the bullish case: an old low exists; a swing high forms; price then
drops to a **lower low that runs the old low's stops** — "again, focusing on the high in between the
two lower lows, one low has to be traded below, and that is going to run out to sell stops"
(`ICT-2016-BREAKER-BLOCK` [02:11–02:24]). That intervening swing high is the breaker candle: "we
focus our attention on the short term high that is in between the two lows" [02:24]. Only afterward
does price rally back up and **break through that same swing high** — the structure break that
confirms the earlier drop was a stop run, not a new leg down: "wait for price to break through that
swing high to confirm that there has been a run on stops" [05:41]. The retest down into that swing
high's range is what confirms the pattern: "as price moves away, that confirms the breaker" [02:02].
The mirror (bearish case) is symmetric: "a bearish breaker is a bearish range or down close candle
in the most recent swing low **prior to** an old high being violated" [03:13].

**The liquidity run is mandatory, not optional** — omitting it makes the pattern something else: "a
breaker is a pattern where price runs out a pool of liquidity … and then it reverses" (EP39
[20:25]); ICT's own narrower definition of the breaker names the run explicitly (`ICT-2016-BREAKER-BLOCK`
[02:11–02:24], [05:41] above). **Separately, knowing the market's expected draw is also required** —
geometry alone is not sufficient: "it's not just simply we have this pattern here and that's all it
is — no, you must know what the market's likely to be reaching for. If you leave that out, it's not
a breaker — it's a gamble." (EP39 [20:25–20:50]). These are two distinct requirements, not one.

ICT frames the breaker itself as a form of mitigation: "this form of mitigation" (`ICT-2016-BREAKER-BLOCK`
[00:26]). It belongs to a closed two-item taxonomy of swing points: "there's really only two forms of
swing points … it's in the form of a stop run or a failure swing. That's it. There's nothing else."
(`ICT-2017-INSTITUTIONAL-SWING-POINTS` [01:37–01:51]). The breaker is the **stop-run** type; the
[mitigation-block](mitigation-block.md) is the **failure-swing** type — see
[breaker-vs-mitigation](breaker-vs-mitigation.md) for the full contrast.

The breaker is a **reversal** swing point, not a continuation reference: "this is a breaker where the
market will generally make a higher high, fail, then break down" (`ICT-2017-INSTITUTIONAL-SWING-POINTS`
[02:08–02:15], describing the bearish case). In the PD-array hierarchy it outranks every other array:
"the breaker is going to take precedence over everything on this list" (`ICT-2017-HTF-PD-ARRAYS`
[26:47]); "the breaker has precedence over everything, both bullish breaker and bearish breakers."
[31:45].

## Formal Criteria

- **The breaker candle exists BEFORE the run** — it is the swing high (bullish case) or swing low
  (bearish case) that sits **between two lows** (bullish) or **between two highs** (bearish): "again,
  focusing on the high in between the two lower lows" (`ICT-2016-BREAKER-BLOCK` [02:11]); "we focus
  our attention on the short term high that is in between the two lows" [02:24]; mirrored in the
  PD-array hierarchy lecture: "a bullish breaker is a up candle between two swing lows" (`ICT-2017-HTF-PD-ARRAYS`
  [27:48]).
- **The run happens after the breaker candle forms**, not before: one of the two lows (bullish case)
  is traded below, running the stops resting beneath it — "one low has to be traded below, and that
  is going to run out to sell stops" (`ICT-2016-BREAKER-BLOCK` [02:11–02:24]); "we view that initial
  drop down below the previous low as a potential false break or turtle soup long" [00:42–00:56].
- **Only then** does price break back through the pre-existing swing (the structure break) — the
  confirmation that the drop/rally was a stop run: "we have to wait for price to break through that
  swing high to confirm that there has been a run on stops" [05:41]. The break is of the **swing
  extreme**, not a body close through the candle; no wick-vs-close distinction for the break is
  stated anywhere in the corpus (searched "wick", "close through", "closing" across the
  breaker/swing-point/PD-array lectures and EP10/37/39: 0 hits) — do not add one.
- The breaker candle's zone is **the entire candle (full range)**, not its body: "why am I using this
  one and not this one here? Because this one was the highest one prior to the drop down and we're
  using the **entire range**." [09:17–09:19]; "a bearish breaker is a bearish range or down close
  candle in the most recent swing low prior to an old high being violated." [03:13]. See
  [bullish-breaker](bullish-breaker.md) / [bearish-breaker](bearish-breaker.md) for the per-side
  wording.
- On the retest, price returns to that candle's range; "as price moves away, that confirms the
  breaker" [02:02]. Telltale: "the rate on sell stops indicates sellers are trapped below the old
  low. The range expansion that takes out the short term high in between the two lows." [06:33–06:42].
- **Two independent requirements, not one:** (a) the liquidity run itself — "a breaker is a pattern
  where price runs out a pool of liquidity … and then it reverses" (EP39 [20:25]) — is structurally
  mandatory, evidenced by `ICT-2016-BREAKER-BLOCK` [02:11–02:24] and [05:41] above; (b) separately,
  ICT requires knowing the market's expected draw/narrative — "you must know what the market's
  likely to be reaching for; if you leave that out, it's not a breaker, it's a gamble" (EP39
  [20:25–20:50]). Do not use (b) as evidence for (a); they are different gates.

## Formula / Math

```
# Variables: two lows L1, L2 (bullish case; mirror: two highs H1, H2 for bearish), in time order.

intervening_swing := the swing high (bullish) / low (bearish) FORMED BETWEEN L1 and L2
                      # this candle EXISTS BEFORE the run — it is not produced by it
breaker_candle     := the candle forming intervening_swing
                       # bullish: "a bullish range or up close candle in the most recent swing high
                       #           prior to an old low being violated"
                       # bearish: "a bearish range or down close candle in the most recent swing low
                       #           prior to an old high being violated"
breaker_zone := [low(breaker_candle), high(breaker_candle)]   # ENTIRE RANGE, not the body

liquidity_run_event := L2 trades below L1 (bullish case), running the stops resting below L1
                        # happens AFTER breaker_candle has already formed
structure_break      := price (later) trades back THROUGH intervening_swing   # swing extreme, NOT a body close
                         # this is what CONFIRMS L2 was a stop run, not a new leg down

breaker_confirmed := liquidity_run_event AND structure_break   # BOTH required; the run alone is not enough
retest_reaction    := price returns into breaker_zone and moves away   # "as price moves away, that confirms the breaker"

# Separate narrative gate (does not change the geometry above):
narrative_known := trader can state what liquidity pool/draw the market is reaching for
                    # EP39: without this, "it's not a breaker — it's a gamble"
```

## Machine-Readable

```json
{
  "id": "breaker-block",
  "category": "08-breaker-blocks",
  "aliases": ["BB", "breaker"],
  "criteria": [
    {"id": "c1", "expr": "breaker_candle := the swing high/low BETWEEN two lows/highs, formed BEFORE the run (not produced by it)"},
    {"id": "c2", "expr": "liquidity_run_event := the second low/high trades through the first, AFTER breaker_candle has formed"},
    {"id": "c3", "expr": "structure_break := price later breaks back THROUGH breaker_candle's swing extreme, confirming the run"},
    {"id": "c4", "expr": "breaker_zone := ENTIRE RANGE (high to low) of breaker_candle, not the body"},
    {"id": "c5", "expr": "breaker is a stop-run-type swing point; takes precedence over every other PD array"},
    {"id": "c6", "expr": "breaker is a REVERSAL swing point, not a continuation reference"},
    {"id": "c7", "expr": "narrative_known := trader can state the expected liquidity draw — a SEPARATE requirement from the run itself"}
  ],
  "timeframes": ["M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["bullish-breaker","bearish-breaker","mitigation-block","breaker-vs-mitigation","bullish-order-block","bearish-order-block"],
  "sources": ["ICT-2016-BREAKER-BLOCK","ICT-2016-TIMEFRAME-SELECTION","ICT-2016-INSTITUTIONAL-ORDER-FLOW","ICT-2017-INSTITUTIONAL-SWING-POINTS","ICT-2017-HTF-PD-ARRAYS","ICT-2017-TRADE-CONDITIONS","ICT-2020-OTE-VOL04","ICT-2022-MENTORSHIP-EP39"]
}
```

## Visual Pattern

```
   bullish breaker (breaker candle forms FIRST, then the run, then the structure break):

   L1 ──╲                              ← old low #1 (forms first)
         ╲    ██                       ← breaker candle: the swing HIGH between L1 and L2
          ╲  ██ ██                        (ENTIRE RANGE, not just its body) — EXISTS BEFORE THE RUN
           ╲██   ╲
                  ╲
                   ╲→ L2               ← lower low RUNS the stops resting below L1 (the liquidity event)
                      ╲
                       ╲
                        ╲→ ██ ██        ← price rallies back up and BREAKS THROUGH the breaker
                           ██ ██  ↑         candle's swing high (structure break; confirms L2 was stops)
                                  │
                                  ╲→ retest DOWN into the breaker's full range, then rejects back up

   bearish mirror: a swing LOW between two highs (H1 then a higher H2 that runs H1's stops);
   price then breaks back DOWN through that swing low (structure break); retest UP, then rejects down.
```

## Timeframes

No floor is stated. ICT shows breakers on the monthly chart (`ICT-2017-TRADE-CONDITIONS` [10:05–10:11]
"we have a range up here, we also have this down candle which is a breaker"), the weekly chart
(`ICT-2016-TIMEFRAME-SELECTION` [36:12–36:20]), and the hourly chart: "here's trading up into that
area I outlined on the hourly chart where we can see that breaker" (`ICT-2020-OTE-VOL04` [04:57]).
No ceiling or floor is stated anywhere in the corpus.

## Examples

**Example 1 — bullish breaker (schematic, following the lecture sequence):**
- An old low (L1) exists; price rallies, forming a swing high — this is the breaker candle, and it
  exists before anything is run.
- Price then drops to a lower low (L2) that trades below L1, running the stops resting beneath it
  (the liquidity event).
- Price reverses and breaks back up through the swing high formed earlier — the structure break that
  confirms L2 was a stop run, not a new leg down.
- The up-close candle at that swing high is the breaker; its **entire range** (not just the body) is
  the reference zone.
- Retest: price returns into that range; moving away from it confirms the breaker.

## Common Mistakes

- **Treating any violated order block as a breaker.** A breaker requires the antecedent liquidity
  run (`ICT-2016-BREAKER-BLOCK` [02:11–02:24], [05:41]) AND the trader knowing the market's expected
  draw — without the latter, "it's not a breaker — it's a gamble" (EP39 [20:25–20:50]; the "gamble"
  clause is about the narrative, not the run itself).
- **Putting the breaker candle after the run.** It forms BEFORE the run, between the two lows/highs
  (`ICT-2016-BREAKER-BLOCK` [02:11], [02:24]; `ICT-2017-HTF-PD-ARRAYS` [27:48]) — the run and the
  later structure break both happen afterward.
- **Using the OB body as the breaker zone.** ICT states "we're using the entire range" (`ICT-2016-BREAKER-BLOCK`
  [09:17–09:19]); the body-only convention from [bullish-order-block](../07-order-blocks/bullish-order-block.md)
  does not carry over to breakers.
- **Calling the breaker a continuation reference.** It is a reversal swing point (the "stop run" type
  in ICT's two-item taxonomy); see [breaker-vs-mitigation](breaker-vs-mitigation.md).
- **Confusing breaker with mitigation block.** They're related but distinct — see
  [breaker-vs-mitigation](breaker-vs-mitigation.md).

## Related Concepts

- [bullish-breaker](bullish-breaker.md), [bearish-breaker](bearish-breaker.md) — directional variants.
- [mitigation-block](mitigation-block.md), [breaker-vs-mitigation](breaker-vs-mitigation.md).
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md).

## Citations

- `ICT-2016-BREAKER-BLOCK` [00:26] "this form of mitigation"; [00:42–00:56] "we view that initial drop down below the previous low as a potential false break or turtle soup long"; [01:24–01:36] the market structure shift taking out the intervening short-term high; [02:02] "as price moves away that confirms the breaker"; [02:11–02:24] the old low run to sell stops; [03:13–03:22] bearish breaker definition; [05:08] bullish breaker definition; [05:41] break through the swing high confirms the run; [06:33–06:42] trapped sellers / range expansion telltales; [09:17–09:19] "we're using the entire range".
- `ICT-2016-TIMEFRAME-SELECTION` [36:20], [44:05–44:11] breaker named a month before the dedicated lecture (Nov 2016), confirming the Dec-2016 (not 2017) dating.
- `ICT-2016-INSTITUTIONAL-ORDER-FLOW` [14:40–14:44], [25:12], [26:01] breaker as a bearish re-entry reference.
- `ICT-2017-INSTITUTIONAL-SWING-POINTS` [01:37–01:51] the two-item swing-point taxonomy (stop run vs failure swing); [02:08–02:15] breaker as a reversal pattern.
- `ICT-2017-HTF-PD-ARRAYS` [26:47], [31:45] breaker precedence over every other PD array.
- `ICT-2017-TRADE-CONDITIONS` [10:05–10:11] monthly-chart breaker: "we have a range up here, we also have this down candle which is a breaker."
- `ICT-2020-OTE-VOL04` [04:57] hourly-chart breaker: "here's trading up into that area I outlined on the hourly chart where we can see that breaker."
- `ICT-2022-MENTORSHIP-EP39` [20:25] run definition: "a breaker is a pattern where price runs out a pool of liquidity … and then it reverses and trades back down below that short-term low"; [20:25–20:50] SEPARATELY, the narrative gate: "notice that it's not just simply we have this pattern here and that's all it is — no, you must know what the market's likely to be reaching for; if you leave that out, it's not a breaker, it's a gamble." These are two distinct clauses in the same breath, not one; do not cite the "gamble" wording as proof of the liquidity-run requirement (it is about knowing the draw).
