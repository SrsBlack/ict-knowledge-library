# Low Resistance Liquidity Run

**Category:** 02-liquidity
**Aliases:** LRLR, low resistance liquidity run, liquidity run between arrays, quadrant grading
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-STT-LRLR-CONSOLIDATION, ICT-2017-STT-LRLR-TRENDING, ICT-2017-STT-BLENDING-IPDA-PD
**Tags:** liquidity, premium-discount, quadrants, consolidation, trending, short-term-trading

## Definition

A low resistance liquidity run is a **travel path between two opposing PD arrays with nothing in between to stop it**. ICT's method for finding one is not to look at the arrays first but to **grade the range**: define the last 60 trading days by candle *bodies*, halve it, halve each half, and halve those halves again, producing recursive premium/discount quadrants. Arrays that sit at or near a quadrant boundary, on the correct side of it, mark the departure and arrival points — "we're looking for low resistance liquidity runs from one PD array to another, from a discount to a premium" (`ICT-2017-STT-LRLR-CONSOLIDATION`, 20:00).

The same machinery is taught twice in the same month, once for a range-bound market (lesson 5) and once for a trending one (lesson 6), because "price is universally fractal, what could be a consolidation on one timeframe can be a trending environment in another" (`ICT-2017-STT-LRLR-TRENDING`, 01:27).

## Formal Criteria

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
    {"id": "c1", "expr": "range anchored on candle BODIES (highest open-or-close, lowest open-or-close), not wicks"},
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
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["liquidity-run", "draw-on-liquidity", "liquidity-void", "premium-array", "discount-array", "pd-array-matrix", "dealing-range-equilibrium", "ipda-60-day-lookback", "one-shot-one-kill", "market-maker-manipulation-template", "monday-wednesday-range", "mean-threshold"],
  "sources": ["ICT-2017-STT-LRLR-CONSOLIDATION", "ICT-2017-STT-LRLR-TRENDING", "ICT-2017-STT-BLENDING-IPDA-PD"]
}
```

## Visual Pattern

```
  60 trading days, anchored on BODIES (not wicks), halved three times:

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

Constructed on the **daily** (60 trading days), executed from the **H4** — "the four hour chart is, in my opinion, the easiest trading timeframe for one shot, one kill setups" (`…-TRENDING`, 03:54) — and refined on **H1**, which is the floor. On MT4, **Ctrl+Y on an H4 chart prints weekly dividers**, so a whole week's expected travel is visible at once: "every vertical dotted line here represents the beginning and end of a new trading week" (`…-TRENDING`, 04:59).

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

- **Anchoring the range on wicks.** ICT states the body rule twice in lesson 5 and repeats it in lesson 6: "Look at the highest high and the lowest low in the form of the bodies, not the wicks and define that" (`…-TRENDING`, 14:08).
- **Reusing an array price has already traded to.** Exhaustion is the filter that separates a low-resistance run from a re-run into old inventory.
- **Reading the grades as support/resistance.** ICT contrasts them with pivot points explicitly — pivots "came from floor traders and pit traders… that was like a self-fulfilling prophecy", whereas the grades "help you really discern where the market has its highest probable support or resistance without really having a logical old reference point" (`…-TRENDING`, 11:52–12:24).
- **Calling a premium range unbuyable.** "what would otherwise be deemed as overbought? We don't view it like that. This is why indicators do not work" (`…-CONSOLIDATION`, 13:07–13:11).
- **Trading the middle.** Chop is where an incorrectly defined range and exhausted arrays both bite.
- **Dropping below H1.** Below the hourly the impulse swing that builds the weekly range is no longer visible.

## Related Concepts

- [liquidity-run](liquidity-run.md) — the generic approach/sweep/resolution sequence; LRLR is the *unobstructed* case between opposing arrays.
- [draw-on-liquidity](draw-on-liquidity.md) — what the far end of the run is.
- [one-shot-one-kill](../31-models/one-shot-one-kill.md) — the model that trades these runs weekly.
- [market-maker-manipulation-template](../31-models/market-maker-manipulation-template.md) — the entry/target overlay applied at each end.
- [monday-wednesday-range](../25-htf-bias/monday-wednesday-range.md) — when in the week the run is expected to start.
- [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md), [premium-array](../05-pd-arrays/premium-array.md), [discount-array](../05-pd-arrays/discount-array.md), [ipda-60-day-lookback](../23-ipda/ipda-60-day-lookback.md).
- [dealing-range-equilibrium](../27-equilibrium/dealing-range-equilibrium.md), [mean-threshold](../27-equilibrium/mean-threshold.md), [liquidity-void](liquidity-void.md).

## Citations

- `ICT-2017-STT-LRLR-CONSOLIDATION` (00:00) "Welcome to **lesson 5** folks, short term trading… low resistance liquidity runs and consolidations"; (00:52–01:11) "for short term trading, we will excel in the range of the last three months. So the up to data range of 60 days is our look back period"; (02:47–03:22) the 60-day frame and the body-based range; (04:01–04:31) "I'm not using the lowest wick low in the highest wick high… the lowest open or close in the last 60 trading days"; (04:49–06:11) the three halvings and the premium/discount split; (09:04–09:36) quadrants each divided again; (12:08–12:21) the full recursion stated in one sentence; (13:07–13:30) "This is why indicators do not work"; (16:33–16:46) a discount inside an overall premium; (20:00–20:17) the definition — runs "from one PD array to another, from a discount to a premium", inside the three-month lookback; (21:03–21:51) best buys in the lowest quadrant, best sells in the last upper quadrant; (22:29–22:46) "One shot, one kill is a couple days of trading… as little as one day and as long as a week"; (22:57–24:07) the midrange chop zone; (23:11–23:44) exhausted arrays excluded because "the algorithm knows price has been there once before".
- `ICT-2017-STT-LRLR-TRENDING` (00:00) "ICT Mentorship Short-Term Trading **Lesson number 6**… low resistance liquidity runs in trending conditions"; (01:27–01:35) price is universally fractal; (03:54–04:04) H4 as the easiest one-shot-one-kill timeframe; (04:43–05:05) Ctrl+Y weekly dividers on MT4; (06:01–06:19) arrays at quadrant levels produce high-probability departures; (07:09–07:27) 30–50, then 50–75, then 75–100 pips a week, "I wouldn't try to go more than 100 pips"; (11:52–12:27) grades versus floor-trader pivot points; (14:08–14:19) bodies not wicks, restated, and "Very rarely do you see any midway points between the grades"; (19:06–19:39) the two-week worked example; (20:02–20:24) below H1 "you're really just day trading or you're scalping"; (23:37–23:48) 30–50 % of the weekly range completed by Wednesday's London close.
- `ICT-2017-STT-BLENDING-IPDA-PD` (04:14–04:37) exhausted arrays — "That PD array has now been exhausted. So you'd have to look for another discount PD array"; (05:56–06:20) "We don't force the idea of any of these PD arrays. They're either in the chart or they're not."
