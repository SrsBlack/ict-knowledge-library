# HTF PD Array Hierarchy

**Category:** 05-pd-arrays
**Aliases:** multi-TF PDA hierarchy, top-down PD arrays, HTF array prioritization
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2024
**Source IDs:** ICT-2017-HTF-PD-ARRAYS, ICT-2017-TRADE-CONDITIONS, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2024-MENTORSHIP-MODULE-LIST
**Tags:** pd-array, hierarchy, multi-tf, top-down, fallback

## Definition

HTF PD array hierarchy is the multi-timeframe extension of [pd-array-hierarchy](pd-array-hierarchy.md): higher-timeframe arrays carry more conviction than lower-timeframe arrays of the same type. ICT's discipline is **top-down analysis** — start from monthly / weekly / daily, identify the dealing range and highest-priority PD array on each TF, then descend to entry TF (H1 / M15 / M5) only inside the HTF array's price range.

The mechanism ICT gives it is a **fallback ladder**: when a PD array fails to hold, the next support is not a nearer level on the same chart but the equivalent array one timeframe up. "Any bullish order block or any supportive role from a PD array on a daily chart, if it is bullish but it fails to give you a buy signal or a support price, the next level you drop back to is a weekly PD array. So you're going to be looking for something bullish to support price on the weekly chart. If the weekly chart PD array has no support and it breaks, then you get back to the monthly support" (`ICT-2017-TRADE-CONDITIONS`, 18:45–19:11).

## Formal Criteria

The TF priority ladder ICT teaches:

1. **Monthly (MN)** — dealing range; if present, primary PD array is the conviction anchor.
2. **Weekly (W)** — sub-range; primary PD array.
3. **Daily (D)** — sub-range; primary PD array. Most ICT day-traders read bias from D.
4. **H4** — sub-range; entry refinement context.
5. **H1** — entry refinement.
6. **M15 / M5** — entry trigger only.

The principle: an entry TF setup is **valid only if the HTF array supports it**. A discount-side long setup on M5 when the D array says price is in premium = wrong-side trade.

**The fallback ladder (D → W → MN).** A daily array giving way is *expected behaviour*, not a failed read: "the retracement can go through what you see on the daily. The daily isn't going to support a monthly retracement, it just isn't going to do it. Sometimes this is going to give way, it's going to break through, it's going to pull all the way back to what you would otherwise not see unless you were looking at a monthly chart" (`ICT-2017-TRADE-CONDITIONS`, 19:17–19:34).

The diagnostic use: an unexplained surge is a jump to the next rung. "Usually when you see these big surges higher or lower in price and you're watching on a daily chart… quickly go out to a weekly chart and you'll see what they've done or what they're reaching for" (26:23–26:37). And after a stop-out: "if you go and look at the weekly chart, you can see that all that was is a return back to that weekly order block, and if it was starting to trade back up to this level here, you could be a buyer again" (26:53–27:07).

**When the ladder gets used.** The algorithm works the daily first and only escalates when the daily levels are spent: "the algorithm is going to work predominantly on a daily timeframe, but if the levels are already worked enough and already absorbed all of the potential liquidity because it's already been trading to them, it will go out to that larger open float and that usually will dip you into the weekly ranges" (27:32–27:49). Reaching a weekly array therefore signals magnitude: "then you'll know that you're probably going to have a really significant price move because of the weekly level — those large funds, banks and institutions, they're all going to dog pile on those levels" (27:55–28:11).

**Within each timeframe, the array order is identical.** Monthly, weekly and daily all use the same seven-array depth ordering from [pd-array-hierarchy](pd-array-hierarchy.md) — "the same hierarchy exists" (`ICT-2017-HTF-PD-ARRAYS`, 31:24). The timeframes stack; the list inside each does not change.

**Carry HTF levels onto the execution chart.** "You should always have in your platform… these monthly weekly levels on, regardless even if you're a day trader" (`ICT-2017-TRADE-CONDITIONS`, 19:53–20:00).

## Formula / Math

```
HTF_priority_chain = [MN, W, D, H4, H1, M15, M5]

valid_entry(setup) :=
    setup.entry_TF in HTF_priority_chain
    AND for each higher_TF in chain above setup.entry_TF:
        higher_TF_PDA is compatible with setup direction

# fallback ladder, on failure to hold
next_support(D_array_broken)  = W_array_same_direction
next_support(W_array_broken)  = MN_array_same_direction
next_support(MN_array_broken) = none   # bias itself is wrong

# escalation trigger
if all daily PD arrays already traded to and liquidity absorbed:
    draw moves to the weekly range      # expect outsized magnitude
```

"Compatible" means: setup is a long → higher-TF PDA is a discount array OR HTF bias is bullish; setup is a short → premium array OR bearish bias.

## Machine-Readable

```json
{
  "id": "htf-pd-array-hierarchy",
  "category": "05-pd-arrays",
  "aliases": ["multi-tf-PDA", "top-down-PD-arrays"],
  "criteria": [
    {"id": "c1", "expr": "HTF_array_supports_entry_TF_setup == true"},
    {"id": "c2", "expr": "TF_priority_order == [MN, W, D, H4, H1, M15, M5]"},
    {"id": "c3", "expr": "on_failure: D_array -> W_array -> MN_array (fallback ladder)"},
    {"id": "c4", "expr": "array depth ordering within each TF is identical across MN, W, D"},
    {"id": "c5", "expr": "daily levels exhausted -> draw escalates to weekly range, expect larger magnitude"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2024",
  "related": ["pd-array-definition","pd-array-hierarchy","pd-array-nesting","pd-array-confluence","htf-bias-framework","top-down-analysis","dealing-range","htf-daily-candle-entries","open-float-liquidity-pool"],
  "sources": ["ICT-2017-HTF-PD-ARRAYS","ICT-2017-TRADE-CONDITIONS","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2024-MENTORSHIP-MODULE-LIST"]
}
```

## Visual Pattern

```
   Daily dealing range
   ───────────────────────────  D LTH
                ▒▒  D bearish OB (premium, primary HTF array)
                ▒▒    │
   ─────────────────── D EQ
                       │
                       ↓ D is bullish bias only if price is below EQ
                       │
                ░░  D bullish OB (discount, primary HTF array)
                ░░  ───── inside this zone, drill down to H4...
   ───────────────────────────  D LTL

   Inside D bullish OB at 1.0820-1.0830:
     H4: contains a bullish FVG at 1.0823-1.0827
     M15: nested bullish OB at 1.0824-1.0826
     M5: entry trigger on M5 bullish FVG re-test inside the M15 OB
```

## Timeframes

The whole concept is multi-TF; every TF in the chain participates.

## Examples

**Example 1 — USDJPY, the daily array giving way to the weekly (`ICT-2017-TRADE-CONDITIONS`, 25:25–26:09):**
- A daily bullish order block forms; price returns to it and does **not** hold.
- Price continues down through it into the *higher* of two weekly bullish order blocks, then — on
  the November 2016 US election whipsaw — into the *lower* weekly bullish order block.
- "The daily chart was pushed aside and the values that's attributed to using daily timeframe,
  that wasn't sufficient enough. The banks went back to recapitalizing a level on the weekly
  chart."
- The weekly bearish order block then gave the upside objective to the pip: open 118.61, the high
  printed 118.66 — "that's precision. I mean, that's really, really tight for a weekly chart"
  (21:36–21:53).

**Example 2 — top-down chain:**
- MN: bullish dealing range, EQ at 1.0750. Current price 1.0890 = MN premium → MN says watch for shorts only at deep premium.
- W: bullish, EQ 1.0850, current 1.0890 = shallow W premium → W also leans toward HTF shorts.
- D: bearish CHoCH last week, current price approaching D bearish OB at 1.0900–1.0920 (premium of D range) → D says short setups valid here.
- H4 / H1: confirm with bearish MSS + FVG.
- → entry valid because all HTFs support the short.

## Common Mistakes

- **Skipping the top-down check.** Trading M5 setups against the daily PD-array context produces low-probability entries that win-rate poorly even when they "look textbook."
- **Mixing TFs incoherently.** A long setup with a discount-array M15 entry inside an HTF premium zone (against HTF bias) needs a very specific HTF reversal context — usually a CHoCH/MSS. Don't take such trades casually.
- **Overweighting MN/W.** MN/W context is structural background; D / H4 set the trade direction. Don't refuse a clean D setup just because MN is technically "in the other half."
- **Treating a broken daily array as a failed read.** It is the expected route to the weekly rung. ICT's instruction after a daily-level stop-out is to check the weekly, not to abandon the bias: "so if you lose a level on a daily, don't be concerned, just go out to a weekly chart and you'll see what they're reaching for" (`ICT-2017-TRADE-CONDITIONS`, 27:22–27:28).
- **Keeping HTF levels off the execution chart.** ICT insists the monthly and weekly levels stay drawn even for day traders.

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [pd-array-hierarchy](pd-array-hierarchy.md), [pd-array-nesting](pd-array-nesting.md), [pd-array-confluence](pd-array-confluence.md).
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [top-down-analysis](../25-htf-bias/top-down-analysis.md).
- [dealing-range](dealing-range.md).
- [htf-daily-candle-entries](../31-models/htf-daily-candle-entries.md) — the execution technique that requires an HTF draw.
- [open-float-liquidity-pool](../02-liquidity/open-float-liquidity-pool.md) — "that larger open float" the draw escalates into.

## Citations

- `ICT-2017-HTF-PD-ARRAYS` (00:00) — "lesson 6.1 of the January 2017 ICT Mentorship, Defining High Time Frame PD Arrays"; (29:48–31:24) the monthly, weekly and daily premium/discount array sets, "the same hierarchy exists."
- `ICT-2017-TRADE-CONDITIONS` (00:17) — "this is lesson 6.2 of January 2017 ICT mentorship… trade conditions and setup progression"; (18:45–19:11) the D → W → MN fallback ladder; (19:17–19:34) the daily cannot support a monthly retracement; (19:53–20:00) keep monthly/weekly levels on every chart; (21:36–21:53) the 118.61 / 118.66 weekly bearish order block; (25:25–26:09) the daily array pushed aside for the weekly; (26:23–27:07) using the weekly to explain a surge or a stop-out; (27:32–28:11) escalation to the weekly range signals magnitude.
- `ICT-2022-MENTORSHIP-OVERVIEW` — top-down analysis re-taught.
- `ICT-2024-MENTORSHIP-MODULE-LIST` — HTF-LTF alignment refined.
