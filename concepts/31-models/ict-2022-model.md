# ICT 2022 Model

**Category:** 31-models
**Aliases:** ICT 2022 setup, 2022 mentorship model, the 2022 model
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-EP02, ICT-2022-MENTORSHIP-EP06, ICT-2022-MENTORSHIP-EP12, ICT-2022-MENTORSHIP-EP14, ICT-2022-MENTORSHIP-EP17, ICT-2022-MENTORSHIP-EP18, ICT-2022-MENTORSHIP-EP20, ICT-2022-MENTORSHIP-EP24, ICT-2022-MENTORSHIP-EP25, ICT-2022-MENTORSHIP-EP41
**Tags:** model, 2022, mentorship, foundational

## Definition

The ICT 2022 Model is the multi-step institutional setup framework taught across the 2022 YouTube mentorship — a structured combination of HTF bias, a New York-session killzone, a liquidity sweep, a market-structure-shift trigger with a fair value gap, and a limit-order entry. ICT states the model explicitly: "So, what's the model teach? Trading when? The New York session." (ep18 [31:28–32:02]). Other sessions are optional extensions, not the model's own windows: "the same model you can use it in Asian session … you can trade it in London clothes [close] … the New York open like I'm teaching you and London open" (ep10 [26:23]); but, referring to the London-session walkthrough he had just given, "this is not an addition to the model" (ep20 [03:09]) — meaning that walkthrough is the trader's own choice, not part of what ICT teaches as the model.

## Formal Criteria

The 2022 Model's setup sequence:

1. **HTF bias** clear — "bias is bearish and we're looking at a daily chart, so you start your analysis there" (ep18 [07:49–08:18]); set via the weekly-candle read, "you're looking for swing highs and swing lows to get your liquidity" (ep02 [16:23]).
2. **New York session window active.** ⚠ **Not "London open / NY AM / London close."** The model is taught specifically for New York: forex "7:00 in the morning to 10:00 in the morning" (ep18 [31:28]); indices AM "8 30 to 11 o'clock window" (ep17 [25:38]); indices PM "1 30 to 4" (ep41 [05:53]). See [killzone-times-table](../10-killzones/killzone-times-table.md) for the full set.
3. **Liquidity sweep** of a known pool — "look for periods where price runs above an old high then it breaks down and then you look for this pattern" (ep06 [15:14]); "the run above a single high or multiple highs like a double top okay either one of those fits this criteria" (ep06 [15:40]).
4. **Market structure shift (MSS)** — the trigger step this page previously omitted. ICT's sequence requires a short-term high/low taken out with displacement: "find the nearest short term low because that right there is going to be your trigger … you have to see it go below that and displacement with the energetic move take out a short term low" (ep24 [33:30]); "you have to look for what the short-term low being broken that's your Market structure shift then you see price go up into that imbalance" (ep12 [37:16]).
5. **FVG inside the displacement leg** — the FVG must sit between the displacement's high and low: "where does that reside between the displacement high and the displacement low … if there isn't one there you don't have a trade" (ep06 [23:55–24:25]).
6. **Entry: limit order at the FVG edge.** ⚠ **Not "CE retest."** "put your limit order in to sell short right at that price right there or plus one pip" (ep18 [32:47]); "we're just going to use the actual candle high that would be your limit order entry" (ep20 [14:19]); "it doesn't have to completely close it if it trades up into it anywhere between here and here is good" (ep24 [36:15]). No source for "CE" or a 2025 default exists in this corpus — `consequent` has zero hits across the 41 episodes.
7. **SL: above the FVG candle or the swing high.** ⚠ **Not "beyond the swept extreme."** "where's your stop loss going to be above the high of candle number two or you can use above candle number one which creates a swing high okay whichever one you can afford" (ep06 [36:06]); "the rule is you want to use the candle that creates the fair value you got that high just above that okay one tick two ticks above that" (ep25 [43:39]); "your risk is going to be above this high" — the displacement-leg high (ep18 [32:47]).
8. **Targets: liquidity first, SD projections as a how-far gauge only.** Primary target is a liquidity pool: "partials internal range external range your trade" (ep06 [45:41]); "look for a run above fourteen thousand one sixty" (ep14 [00:01], an NQ liquidity target). Standard-deviation figures describe how far a move may go, not the primary target: "the projection is -1 1/2 standard deviation and there's your low" (ep12 [32:47]).

The model is **time-and-pattern combined** — both the New York killzone and the structural sequence must align.

## Formula / Math

```
ict_2022_model :=
    htf_bias_clear
    AND in_ny_session_window            # forex 07:00-10:00 | indices AM 08:30-11:00 | indices PM 13:30-16:00
    AND liquidity_sweep_just_occurred
    AND market_structure_shift          # short-term high/low broken with displacement — the missing step
    AND fvg_inside_displacement_leg
    AND entry_at_fvg_edge_by_limit_order   # NOT "CE"
    AND SL_above_fvg_candle_or_swing_high  # NOT "beyond the swept extreme"
    AND TP_at_liquidity_pool               # SD projection is a how-far gauge, not the primary target
```

## Machine-Readable

```json
{
  "id": "ict-2022-model",
  "category": "31-models",
  "aliases": ["ICT-2022-setup", "2022-mentorship-model"],
  "criteria": [
    {"id": "c1", "expr": "htf_bias + ny_session_window + sweep + MSS + fvg_in_displacement_leg + limit_order_entry_at_fvg_edge"},
    {"id": "c2", "expr": "all 8 steps required; killzone == NY session only (forex 07:00-10:00, indices AM 08:30-11:00, indices PM 13:30-16:00)"},
    {"id": "c3", "expr": "entry == limit_order_at_fvg_edge, NOT CE"},
    {"id": "c4", "expr": "SL == above_fvg_candle_or_swing_high, NOT beyond_swept_extreme"},
    {"id": "c5", "expr": "target_priority == liquidity_pool; SD_projection is a how-far gauge only"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2022",
  "related": ["htf-bias-framework","killzone-overview","liquidity-sweep","displacement-definition","fair-value-gap","mss"],
  "sources": ["ICT-2022-MENTORSHIP-EP02","ICT-2022-MENTORSHIP-EP06","ICT-2022-MENTORSHIP-EP12","ICT-2022-MENTORSHIP-EP14","ICT-2022-MENTORSHIP-EP17","ICT-2022-MENTORSHIP-EP18","ICT-2022-MENTORSHIP-EP20","ICT-2022-MENTORSHIP-EP24","ICT-2022-MENTORSHIP-EP25","ICT-2022-MENTORSHIP-EP41"]
}
```

## Visual Pattern

```
   ICT 2022 Model (bullish example, NY forex session):

   1. HTF bias bullish (D, W aligned via weekly-candle read)
   2. NY session window active (07:00-10:00 forex)
   3. M5 wicks below recent swing low (sweep)
   4. M5 breaks a short-term low with displacement (MSS — the trigger)
   5. FVG sits inside the displacement leg
   6. Limit order at the FVG edge (not a CE retest)
   7. SL above the FVG candle / swing high (not "beyond the sweep")
   8. Target: next liquidity pool; SD projection as a how-far gauge
```

## Timeframes

M5–H4 entry; D/W for bias.

## Examples

**Example 1 — bullish 2022 Model on NY forex session:**
- D bias bullish ✓; W bias bullish ✓ (HTF check, via weekly-candle read).
- 09:00 NY (NY forex session) ✓.
- 08:55: M5 wicks 1.0908 (recent low SSL swept) ✓.
- 09:05: M5 breaks the short-term low with an energetic displacement candle (MSS) ✓.
- FVG 1.0928–1.0932 sits inside the displacement leg ✓.
- Limit order at the FVG edge, 1.0930 ✓.
- SL above the displacement-leg swing high, 1.0952 ✓.
- TP: next liquidity pool above (e.g. PDH), SD used only to gauge how far the move may extend ✓.
- All 8 steps confirmed → high-conviction execution.

## Common Mistakes

- **Skipping a step.** The model is integrated — missing HTF bias OR missing the sweep OR missing the MSS trigger substantially reduces conviction.
- **Naming the killzones as "London open / NY AM / London close."** The model is taught for the **New York session only** (forex 07:00–10:00, indices AM 08:30–11:00, indices PM 13:30–16:00); other sessions are the trader's own extension, explicitly "not an addition to the model."
- **Entering at CE.** The 2022 teaching enters by **limit order at the FVG edge**; "CE" and a "2025 default" have no source in this corpus.
- **Placing the stop beyond the swept extreme.** The 2022 teaching places it above the **FVG candle or swing high**.
- **Requiring the entry to fill inside the killzone window.** "You don't need to have your entry filled inside that kill zone window. Your order idea and your order placement need to be considered at that time" (ep18 [48:30]) — this is a time-of-order-placement rule, not a pre/post-killzone disqualifier.
- **Skipping the MSS.** The model's trigger is a short-term high/low broken with displacement — "if there isn't one there you don't have a trade" applies to the FVG sitting inside that leg, and the leg itself requires the MSS.
- **Claiming downstream named models (Silver Bullet, Bread-and-Butter, Unicorn) "instantiate" this model.** Not in corpus — Bread & Butter is 2017 forex material predating the 2022 Model; Silver Bullet and Unicorn are absent from both corpora (see [silver-bullet-rules](../11-silver-bullet/silver-bullet-rules.md)).
- **Treating ICT 2022 Model as identical to Silver Bullet.** No corpus source links them; do not present one as a subset of the other.

## Related Concepts

- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [killzone-overview](../10-killzones/killzone-overview.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [displacement-definition](../09-displacement/displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [mss](../01-market-structure/mss.md) — the market-structure-shift trigger step.
- [killzone-times-table](../10-killzones/killzone-times-table.md) — the New York session windows this model keys on.
- [silver-bullet-rules](../11-silver-bullet/silver-bullet-rules.md) — a claimed downstream variant with no corpus link to this model.

## Citations

- `ICT-2022-MENTORSHIP-EP02` (16:23) "the only thing you're looking for is a likely movement higher or lower based on on the weekly candle … you're looking for swing highs and swing lows to get your liquidity."
- `ICT-2022-MENTORSHIP-EP06` (15:14) "look for periods where price runs above an old high then it breaks down and then you look for this pattern"; (15:40) "the run above a single high or multiple highs like a double top"; (22:35–24:25) FVG geometry and the "if there isn't one there you don't have a trade" admission test; (36:06) "where's your stop loss going to be above the high of candle number two or you can use above candle number one which creates a swing high"; (45:41) "partials internal range external range your trade."
- `ICT-2022-MENTORSHIP-EP12` (32:47) "the projection is -1 1/2 standard deviation and there's your low"; (37:16) "you have to look for what the short-term low being broken that's your Market structure shift then you see price go up into that imbalance."
- `ICT-2022-MENTORSHIP-EP14` (00:01) "look for a run above fourteen thousand one sixty" — NQ liquidity-pool target example.
- `ICT-2022-MENTORSHIP-EP17` (25:38) "if you're looking at a model that works in index futures you're looking at that 8 30 to 11 o'clock window and if you're trying to apply this model to fx it's seven o'clock in the morning to 10 o'clock in the morning."
- `ICT-2022-MENTORSHIP-EP18` (07:49–08:18) "bias is bearish and we're looking at a daily chart, so you start your analysis there"; (31:28–32:02) "So, what's the model teach? Trading when? The New York session. … In Forex, it's 7:00 in the morning to 10:00 in the morning."; (32:47) "put your limit order in to sell short right at that price right there or plus one pip … your risk is going to be above this high"; (48:30) "You don't need to have your entry filled inside that kill zone window."
- `ICT-2022-MENTORSHIP-EP20` (03:09) "understand this is not the model for my daughter this is not an addition to the model i'm just simply answering questions" — referring to the London-session walkthrough given earlier in the same episode; (14:19) "we're just going to use the actual candle high that would be your limit order entry."
- `ICT-2022-MENTORSHIP-EP24` (33:30) "find the nearest short term low because that right there is going to be your trigger … you have to see it go below that and displacement with the energetic move take out a short term low"; (36:15) "it doesn't have to completely close it if it trades up into it anywhere between here and here is good."
- `ICT-2022-MENTORSHIP-EP25` (43:39) "the rule is you want to use the candle that creates the fair value you got that high just above that okay one tick two ticks above that."
- `ICT-2022-MENTORSHIP-EP41` (05:53) "the 1 30 to 4 new york local time that's the pm session new york index pm."
