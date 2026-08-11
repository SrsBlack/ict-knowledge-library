# Low Resistance Liquidity Run

**Category:** 02-liquidity
**Aliases:** LRLR, low resistance liquidity run, liquidity run between arrays, quadrant grading
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2017
**Source IDs:** ICT-2016-LIQUIDITY-RUNS, ICT-2017-STT-LRLR-CONSOLIDATION, ICT-2017-STT-LRLR-TRENDING, ICT-2017-STT-BLENDING-IPDA-PD
**Tags:** liquidity, premium-discount, quadrants, consolidation, trending, short-term-trading

## Definition

A low resistance liquidity run is a stretch of chart in which price can reach the next pool of
resting stops **with almost nothing standing in the way**. The concept has two distinct
constructions in the corpus, a year apart, and they should not be conflated.

**The 2016 original — structural.** Introduced in Month 1 of the mentorship alongside its dual,
[high-resistance-liquidity-run](high-resistance-liquidity-run.md). Low resistance is the region
opened up by a sharp one-way expansion: "if there is a very sharp or one-way type direction,
very little retracement of any kind, when we see this, once that market breaks below an old
low… This area of price action is deemed low resistance" (`ICT-2016-LIQUIDITY-RUNS`,
11:44–12:50). Inside it, every newly formed short-term high carries buy stops that price can
reach cheaply — "if we get a buy signal after a retracement, we know that there's going to be
very little resistance for that move to go higher, running out the buy stops just above these
short-term highs" (13:13–13:26). The region has a hard boundary: it ends where the expansion
began. "Once it gets back to this old low over here, the market goes into what is referred to
as a high resistance liquidity run" (14:20–14:39).

**The 2017 restatement — fractional.** In the short-term-trading module the same label is
attached to a **travel path between two opposing PD arrays with nothing in between to stop it**,
found by grading the range rather than by counting obstacles: define the last 60 trading days by
candle *bodies*, halve it, halve each half, and halve those halves again, producing recursive
premium/discount quadrants. Arrays at or near a quadrant boundary, on the correct side of it,
mark the departure and arrival points — "we're looking for low resistance liquidity runs from
one PD array to another, from a discount to a premium" (`ICT-2017-STT-LRLR-CONSOLIDATION`,
20:00).

The 2017 machinery is taught twice in the same month, once for a range-bound market (lesson 5)
and once for a trending one (lesson 6), because "price is universally fractal, what could be a
consolidation on one timeframe can be a trending environment in another"
(`ICT-2017-STT-LRLR-TRENDING`, 01:27).

⚠ The 2016 lecture contains **no range measurement, no fraction, no percentage and no quadrant**
— and no use of the word "array", which appears in none of the Sep–Dec 2016 packets. The
grading apparatus below is 2017 material only.

## Formal Criteria

### The 2016 construction — count the obstacles

**Bullish region.** Bounded below by the old low the expansion broke, bounded above by the
short-term high whose break started the climb back: "from that point at which it breaks the old
low until it gets through a short-term high… this run here begins its climb back up into the
range" (12:06–12:35). Every retracement inside it is a buy toward the next short-term high's
buy stops (13:51–14:20).

**Bearish region.** The mirror: "once the market starts trading below an old low, the market
will have a very easy time trading back down into the point at which the short-term high was
broken on the upside… That's where you would begin your point, which it's deemed a low
resistance liquidity run" (15:22–15:55). Every retracement inside it is a sell toward the next
short-term low's sell stops (15:58–16:11).

**Decay at the boundary.** "the probabilities fall off precipitously once we get back to the
area at which the range is defined in terms of low resistance, then it becomes a high resistance
liquidity run" (13:38–13:51).

### The 2017 construction — grade the range

**Step 1 — define the range by bodies, over 60 trading days.**
- "you look back three months or 60 trading days, which is the relative IPTA data range that we use for maximum definition of look back" (`…-CONSOLIDATION`, 02:47).
- "we define the range in the form of its highest and lowest candlestick body. We're not concerned about the wicks so much, but we're primarily looking at the bodies of the candles" (03:10).
- "I'm not using the lowest wick low in the highest wick high. I'm looking for the highest body on the candles, either it's an open or close. I don't care which one it is… And I'm looking for the lowest open or close in the last 60 trading days" (04:07–04:27).

**Step 2 — grade the range recursively.**
- Halve → premium above, discount below (04:49, 05:53).
- Halve each half → quadrants: "the lower quadrant can be divided into equal halves as well. And that in itself can be viewed from a premium and discount format" (09:21).
- Halve again: "We have the overall consolidation. We divide it in half, then we divide those halves into halves as well. So we have quadrants then. Those quadrants are divided in half as well" (12:08–12:15).
- Reactions cluster on the grade lines: "Very rarely do you see any midway points between the grades that I've already given you here" (`…-TRENDING`, 14:14).

**Step 3 — pair an array with its quadrant position.**
- "if that occurs or forms near a divider level or a quadrant level, as I call it, you'll be able to see high probability movement away from that level and then reach for an opposing level" (`…-TRENDING`, 06:01).
- Rank order: "the best buys are going to be in the lower portion or lower half of the overall consolidation and in the lower quadrant… the highest probability trades for selling short or taking long exits are going to be in the premium range divided by the upper portion. So in other words, that last quadrant, that's going to be your best sells" (`…-CONSOLIDATION`, 21:03–21:44).
- A discount *within* an overall premium is still a valid long: "it's a discount market in a overall premium market that still has room to go up" (16:33).

**Step 4 — reject exhausted arrays.**
- "if it's already been traded to, the likelihood of it being a bullish order block with high probability falls off because it's already been used. We want to use a new PD array in a discount or premium market that has not been traded to because the algorithm knows price has been there once before. So it's going to seek new liquidity" (`…-CONSOLIDATION`, 23:11–23:36). Restated in `ICT-2017-STT-BLENDING-IPDA-PD`, 04:14–04:37.

**Exclusions.**
- The middle of the range is the chop zone: "if you're trading in this range here, you're going to get chopped up a lot" (`…-CONSOLIDATION`, 22:57–24:04).
- Below H1 the concept degrades: "Anything less than a 60 minute chart, you're really just day trading or you're scalping" (`…-TRENDING`, 20:19).

## Formula / Math

```
# ---- 2016 form: structural, no measurement ----
# bullish region, after a sharp one-way DOWN leg that broke old_low
lrlr_lower_bound := old_low_that_was_broken
lrlr_upper_bound := first_short_term_high_broken_on_the_way_back_up
inside(P) := lrlr_lower_bound < P < lrlr_upper_bound
  -> every retracement is a buy toward the next short-term high's buy stops
  -> above lrlr_lower_bound (the violated low, retested as resistance):
     condition flips to high resistance

# bearish form is the mirror, bounded by the broken old_high above and the
# short-term low whose break started the decline below
```

```
# ---- 2017 form: fractional grading ----
# 1. Range, by BODIES, over 60 trading days
H_body = max(max(open_i, close_i)) for i in last 60 trading days
L_body = min(min(open_i, close_i)) for i in last 60 trading days
R      = H_body - L_body

# 2. Recursive grading (three halvings -> 8 grade lines)
EQ      = L_body + R/2                    # premium above, discount below
EQ_up   = L_body + 3R/4 ; EQ_dn = L_body + R/4        # quadrant boundaries
then each quadrant halved again -> {1/8, 3/8, 5/8, 7/8} of R

# 3. Trade ranking
best_long   := discount PD array in the LOWEST eighth      # deepest discount
best_short  := premium  PD array in the HIGHEST eighth     # deepest premium
valid_long  := discount PD array in the LOWER half of ANY quadrant, even a premium one
chop_zone   := neighbourhood of EQ

# 4. Exhaustion filter
usable(array) := NOT already_traded_to(array)

# 5. The run itself
LRLR := path(entry_array -> opposing_array) with no unexhausted opposing array between
```

## Machine-Readable

```json
{
  "id": "low-resistance-liquidity-run",
  "category": "02-liquidity",
  "aliases": ["LRLR", "quadrant-grading", "range-grading"],
  "criteria": [
    {"id": "c0a", "expr": "2016 form: region opened by a sharp one-way expansion that broke an old low (or high), bounded by that broken level and the first short-term high (or low) broken on the way back"},
    {"id": "c0b", "expr": "2016 form: inside the region every retracement targets the next short-term high's buy stops (or low's sell stops)"},
    {"id": "c0c", "expr": "2016 form: probability falls off precipitously at the boundary; beyond it the condition is high resistance"},
    {"id": "c0d", "expr": "2016 form uses no range measurement, fraction, percentage, quadrant or the word 'array'"},
    {"id": "c1", "expr": "2017 form: range anchored on candle BODIES (highest open-or-close, lowest open-or-close), not wicks"},
    {"id": "c2", "expr": "lookback == 60 trading days (IPDA maximum)"},
    {"id": "c3", "expr": "range halved three times -> halves, quadrants, eighths"},
    {"id": "c4", "expr": "reactions occur at grade lines; midway points between grades are rare"},
    {"id": "c5", "expr": "best_long := discount array in the lowest eighth; best_short := premium array in the highest eighth"},
    {"id": "c6", "expr": "a discount sub-range inside an overall premium range is still a valid long"},
    {"id": "c7", "expr": "arrays already traded to are exhausted and excluded"},
    {"id": "c8", "expr": "midrange == chop zone, avoid"},
    {"id": "c9", "expr": "minimum useful timeframe == H1; H4 preferred"},
    {"id": "c10", "expr": "same construction applies to consolidating and trending markets (fractal)"}
  ],
  "timeframes": ["H1", "H4", "D", "W", "MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2017",
  "related": ["high-resistance-liquidity-run", "liquidity-run", "draw-on-liquidity", "liquidity-void", "premium-array", "discount-array", "pd-array-matrix", "dealing-range-equilibrium", "ipda-60-day-lookback", "one-shot-one-kill", "market-maker-manipulation-template", "monday-wednesday-range", "mean-threshold"],
  "sources": ["ICT-2016-LIQUIDITY-RUNS", "ICT-2017-STT-LRLR-CONSOLIDATION", "ICT-2017-STT-LRLR-TRENDING", "ICT-2017-STT-BLENDING-IPDA-PD"]
}
```

## Visual Pattern

```
  2016 form — the region opened by a one-way expansion:

   old high ─╮
             ╲                       broken low, retested as resistance:
              ╲                      ── boundary; ABOVE here = HIGH resistance
               ╲   ╱╲   ╱╲   ╱╲
    old low ────╲─╱──╲─╱──╲─╱──╲     each short-term high carries buy stops
                 V    V    V         and is reached with LITTLE resistance
                  one-way leg,
                  very little
                  retracement        <- this is what creates the region
```

```
  2017 form — 60 trading days, anchored on BODIES (not wicks), halved three times:

  H_body ──────────────────────────────  1.000   ▓ premium array  <- BEST SELLS
                                          .875
         ──────────────────────────────   .750   quadrant line
                                          .625
  EQ     ══════════════════════════════   .500   <- CHOP ZONE, avoid
                                          .375
         ──────────────────────────────   .250   quadrant line
                                          .125
  L_body ──────────────────────────────   .000   ▓ discount array <- BEST BUYS

  A low resistance liquidity run is the leg between an unexhausted array
  on one side and an unexhausted opposing array on the other, with no
  untraded opposing array standing in between:

      ▓ discount OB (.06)  ────────────────────────►  ▓ bearish OB (.74)
        entry                                            target
```

## Timeframes

In its **2016** form the classification is timeframe-agnostic — "this is not specific to any timeframe, it's universal" (`ICT-2016-LIQUIDITY-RUNS`, 07:15) — and the lecture names no chart interval anywhere.

In its **2017** form it is constructed on the **daily** (60 trading days), executed from the **H4** — "the four hour chart is, in my opinion, the easiest trading timeframe for one shot, one kill setups" (`…-TRENDING`, 03:54) — and refined on **H1**, which is the floor. On MT4, **Ctrl+Y on an H4 chart prints weekly dividers**, so a whole week's expected travel is visible at once: "every vertical dotted line here represents the beginning and end of a new trading week" (`…-TRENDING`, 04:59).

## Examples

**Example 1 — GBPUSD, 60-day consolidation, early 2017 (`ICT-2017-STT-LRLR-CONSOLIDATION`, 08:26–19:12):**
- Setup: cable in consolidation; range drawn body-to-body, graded into quadrants.
- Trigger: "the fair value gap and bearish order block in the premium level around the February time period of 2017", paired with "a weekly bullish order block mean threshold in the discount in March of 2017".
- Outcome: from the daily bullish order block mean threshold, "we had a 100 pip move that we called for in our day to day meetings", terminating at "the daily bearish order block and it also overlaps with the premium 50% level".

**Example 2 — GBPUSD, trending fractal inside the same consolidation (`ICT-2017-STT-LRLR-TRENDING`, 06:19–10:56, 19:06–19:39):**
- Setup: 14–15 March low formed in a deep discount, at a daily fair value gap plus a breaker.
- Trigger: long on the return to the breaker / fair value gap.
- Outcome: week 1 ran to a bearish order block; week 2 traded down to "the equilibrium price point of the total macro range from the daily chart", retested an old bullish order block, then closed in a February fair value gap.

## Common Mistakes

- **Back-dating the quadrant grading to 2016.** The label is 2016; the 60-day body-anchored range, the eighths and the exhaustion filter are 2017. `ICT-2016-LIQUIDITY-RUNS` measures nothing — it counts obstacles.
- **Losing the dual.** In 2016 the term is introduced *in the same breath* as [high-resistance-liquidity-run](high-resistance-liquidity-run.md), and the pair is the point: the same chart is low resistance one way and high resistance the other (`ICT-2016-LIQUIDITY-RUNS`, 20:15–20:29).
- **Anchoring the range on wicks.** ICT states the body rule twice in lesson 5 and repeats it in lesson 6: "Look at the highest high and the lowest low in the form of the bodies, not the wicks and define that" (`…-TRENDING`, 14:08).
- **Reusing an array price has already traded to.** Exhaustion is the filter that separates a low-resistance run from a re-run into old inventory.
- **Reading the grades as support/resistance.** ICT contrasts them with pivot points explicitly — pivots "came from floor traders and pit traders… that was like a self-fulfilling prophecy", whereas the grades "help you really discern where the market has its highest probable support or resistance without really having a logical old reference point" (`…-TRENDING`, 11:52–12:24).
- **Calling a premium range unbuyable.** "what would otherwise be deemed as overbought? We don't view it like that. This is why indicators do not work" (`…-CONSOLIDATION`, 13:07–13:11).
- **Trading the middle.** Chop is where an incorrectly defined range and exhausted arrays both bite.
- **Dropping below H1.** Below the hourly the impulse swing that builds the weekly range is no longer visible.

## Related Concepts

- [high-resistance-liquidity-run](high-resistance-liquidity-run.md) — the dual, introduced in the same 2016 lecture.
- [liquidity-run](liquidity-run.md) — the generic approach/sweep/resolution sequence; LRLR is the *unobstructed* case between opposing arrays.
- [draw-on-liquidity](draw-on-liquidity.md) — what the far end of the run is.
- [one-shot-one-kill](../31-models/one-shot-one-kill.md) — the model that trades these runs weekly.
- [market-maker-manipulation-template](../31-models/market-maker-manipulation-template.md) — the entry/target overlay applied at each end.
- [monday-wednesday-range](../25-htf-bias/monday-wednesday-range.md) — when in the week the run is expected to start.
- [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md), [premium-array](../05-pd-arrays/premium-array.md), [discount-array](../05-pd-arrays/discount-array.md), [ipda-60-day-lookback](../23-ipda/ipda-60-day-lookback.md).
- [dealing-range-equilibrium](../27-equilibrium/dealing-range-equilibrium.md), [mean-threshold](../27-equilibrium/mean-threshold.md), [liquidity-void](liquidity-void.md).

## Citations

- `ICT-2016-LIQUIDITY-RUNS` — ⚠ **the origin of the term, a year before the quadrant grading.** (11:18–11:25) "that comes by way of trading in low resistance liquidity runs"; (11:44–12:06) "if there is a very sharp or one-way type direction, very little retracement of any kind, when we see this, once that market breaks below an old low"; (12:06–12:42) the region's two boundaries — the broken low and the first short-term high broken on the way back; (12:42–12:50) "This area of price action is deemed low resistance"; (12:50–13:13) each new short-term high before the broken low is retested carries buy-stop liquidity; (13:13–13:26) "we know that there's going to be very little resistance for that move to go higher"; (13:26–13:51) "the probabilities fall off precipitously once we get back to the area at which the range is defined in terms of low resistance, then it becomes a high resistance liquidity run"; (14:01–14:09) "This expansion, okay, that's the easiest part of trading when we can trade inside that range"; (14:20–14:39) the boundary restated — "Anything higher than this price point here becomes a high resistance liquidity run"; (14:59–15:55) the sell-side mirror, bounded by the short-term high broken on the upside; (15:35–15:46) "This is the easiest time to trade in the marketplace right in here"; (16:38–16:53) "this is the easiest area to trade in price action. Because you have very little resistance allowing price to just cut through all that"; (17:31–17:36) "It's like a hot knife through butter"; (20:15–20:29) the duality with the high-resistance case. ⚠ Contains **no** range measurement, fraction, quadrant or the word "array".
- `ICT-2017-STT-LRLR-CONSOLIDATION` (00:00) "Welcome to **lesson 5** folks, short term trading… low resistance liquidity runs and consolidations"; (00:52–01:11) "for short term trading, we will excel in the range of the last three months. So the up to data range of 60 days is our look back period"; (02:47–03:22) the 60-day frame and the body-based range; (04:01–04:31) "I'm not using the lowest wick low in the highest wick high… the lowest open or close in the last 60 trading days"; (04:49–06:11) the three halvings and the premium/discount split; (09:04–09:36) quadrants each divided again; (12:08–12:21) the full recursion stated in one sentence; (13:07–13:30) "This is why indicators do not work"; (16:33–16:46) a discount inside an overall premium; (20:00–20:17) the definition — runs "from one PD array to another, from a discount to a premium", inside the three-month lookback; (21:03–21:51) best buys in the lowest quadrant, best sells in the last upper quadrant; (22:29–22:46) "One shot, one kill is a couple days of trading… as little as one day and as long as a week"; (22:57–24:07) the midrange chop zone; (23:11–23:44) exhausted arrays excluded because "the algorithm knows price has been there once before".
- `ICT-2017-STT-LRLR-TRENDING` (00:00) "ICT Mentorship Short-Term Trading **Lesson number 6**… low resistance liquidity runs in trending conditions"; (01:27–01:35) price is universally fractal; (03:54–04:04) H4 as the easiest one-shot-one-kill timeframe; (04:43–05:05) Ctrl+Y weekly dividers on MT4; (06:01–06:19) arrays at quadrant levels produce high-probability departures; (07:09–07:27) 30–50, then 50–75, then 75–100 pips a week, "I wouldn't try to go more than 100 pips"; (11:52–12:27) grades versus floor-trader pivot points; (14:08–14:19) bodies not wicks, restated, and "Very rarely do you see any midway points between the grades"; (19:06–19:39) the two-week worked example; (20:02–20:24) below H1 "you're really just day trading or you're scalping"; (23:37–23:48) 30–50 % of the weekly range completed by Wednesday's London close.
- `ICT-2017-STT-BLENDING-IPDA-PD` (04:14–04:37) exhausted arrays — "That PD array has now been exhausted. So you'd have to look for another discount PD array"; (05:56–06:20) "We don't force the idea of any of these PD arrays. They're either in the chart or they're not."
