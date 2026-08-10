# Market Maker Manipulation Template

**Category:** 31-models
**Aliases:** manipulation template, MM manipulation template, weekly manipulation template, the playbook
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-STT-MM-TEMPLATES, ICT-2017-STT-WEEKLY-PROFILES, ICT-2017-STT-BLENDING-IPDA-PD
**Tags:** weekly, template, entry, target, fib-extension, short-term-trading

## Definition

A market maker manipulation template is the **entry-and-target overlay** ICT places on each [weekly range profile](../25-htf-bias/weekly-range-profiles.md). The profile says *which day* makes the weekly extreme; the template says *what array is traded at that extreme* and *where the opposing leg terminates*. ICT calls the set "basically the playbook that I use when I go about trying to find my one shot, one kills… The weekly range, you'll find it generally will be one of these templates" (`ICT-2017-STT-MM-TEMPLATES`, 38:01–38:14).

Every template resolves to the same two-part answer, and the second part carries the load-bearing rule of the whole month: **the target array must sit on a timeframe *lesser* than the timeframe of the array used for entry.**

## Formal Criteria

**The lesser-timeframe target rule (universal).**
- "the key is, is you're looking for a timeframe lesser than the discount liquidity pool that you use to buy off of. For an example, if you bought a monthly liquidity pool, you're going to be looking for a weekly or daily premium PD array to trade up into" (02:50–03:11).
- Rationale is duration, not precision: "we're using a lesser time frame to take our targets because we don't want to hold for what would many times take greater than a week to unfold for a move moving off of a monthly or weekly level" (08:37).

**The entry-array menu.** Each profile admits three or four entry types, listed by ICT in this order:
1. an **old monthly / weekly / daily high or low** run as a liquidity pool (stop run);
2. an **old monthly / weekly / daily high or low retested from the other side** (broken structure now acting as support or resistance);
3. an **order block** — monthly, weekly, daily or H4 — optionally located at a *swing grade* (below);
4. a **fair value gap or liquidity void** filled on the way to the extreme.

**The fib overlay.** Entry types 2, 3 and 4 add a projection requirement, type 1 does not:
- Levels: **127 or 168 extension**, or a **"perfect symmetrical price swing"** — "Basically, a 100% duplication or measured move of the price swing" (06:29–06:44).
- Anchor (the **swing projection fulcrum**): the swing that runs *into* the weekly extreme. "Tuesdays low to Wednesday's high, that price swing up, that's what you're going to be anchoring your FIB on. And the extensions below Tuesday's low would be a projection of 127 to 168" (21:38–21:47). For the midweek-rally template the fulcrum is instead the pre-retracement high: "The swing projection fulcrum is the highest high at which the market starts to retrace from" (27:33).
- Confluence, not the level alone: "We're not just simply looking for 127 and 168 extensions. We're doing that also and coupling it with… a lesser time frame PD array that's contrary to what we use to enter the trade" (16:12–16:20).
- No tool required: "you don't need a Fibonacci overlay tool for this… whatever that is in terms of pips times that by 1.27 and that'll give you your range that you subtract from Wednesday's high" (30:53–31:27), and the same with 1.68.

**Swing grading (the four stages).** "when we look at price swings or targets and trades, we graduate it into four stages. First stage, second stage takes us to equilibrium, third stage or third swing grade, and then the fourth is **terminus** where the end of the trade takes effect" (17:22–17:37). The third swing grade is "the halfway point between the equilibrium and the ultimate objective" (05:51), and it behaves differently: "Generally, you don't see a stop run in the third swing grade… but you do get a bullish order block sometimes that you can trade off of" (06:00–06:21).

**Profile-specific bindings.**
- *Classic Tuesday low/high, Wednesday low/high* — hold the position into **Thursday's New York session**, optionally Friday: "generally you want to look for the high to form for the week by Thursday's New York session… just look for Thursday as the lines portion of the weekly range" (02:29–02:38).
- *Consolidation Thursday reversal* — the entry is a **turtle soup**. "This false break becomes a turtle soup long and you're looking for the market to trade up into where the weekly buy stops are" (23:55); bearish mirror at 26:02. Position sizing is capped: "very, very small position, wait for the initial knee jerk reaction, put your limit order down below the low" (24:47).
- *Seek and destroy* — **not traded**: "Again, we're not looking to trade this. We're looking for it to unfold" (35:14). Its use is as a reversal alert: "You're waiting for it to get up to a daily or weekly premium PD array. Once it does that, we are expecting a reversal" (34:15–34:22).
- *Wednesday weekly reversal* — driven by news at an old structural level: "we're looking for an old low or retail support and high or medium impact news drives price down below that… then once it drives down below that, the market discounts that news and reverses" (36:15–36:37).

## Formula / Math

```
entry_tf   := timeframe of the array traded at the weekly extreme      # MN, W, D, or H4
target_tf  := any timeframe strictly LESSER than entry_tf              # HARD RULE
target     := opposing_PD_array(target_tf)  INTERSECT  fib_projection

fib_projection in { 1.27 * R, 1.68 * R, 1.00 * R }   # R = fulcrum swing range
  bearish:  level = high_of_swing - k * R
  bullish:  level = low_of_swing  + k * R
  where R = |swing_high - swing_low| of the leg running INTO the weekly extreme
  and k in {1.27, 1.68, 1.00}   # 1.00 == "perfect symmetrical price swing"

# Swing grading of the larger move:
stage1 -> stage2 == EQUILIBRIUM -> stage3 == third_swing_grade -> stage4 == TERMINUS
third_swing_grade = (equilibrium + terminus) / 2
assert stop_run NOT expected at third_swing_grade    # order block still possible

# Worked, verbatim: entry on a MONTHLY liquidity pool
#   -> target must be a WEEKLY or DAILY premium array, never another monthly one.
```

## Machine-Readable

```json
{
  "id": "market-maker-manipulation-template",
  "category": "31-models",
  "aliases": ["manipulation-template", "mm-manipulation-template", "weekly-manipulation-template"],
  "criteria": [
    {"id": "c1", "expr": "target_array_timeframe < entry_array_timeframe (strict)"},
    {"id": "c2", "expr": "entry menu == [liquidity_pool_run, old_level_retest, order_block, fvg_or_liquidity_void]"},
    {"id": "c3", "expr": "fib overlay in {1.27, 1.68, 1.00} where 1.00 == perfect symmetrical price swing"},
    {"id": "c4", "expr": "fib anchored on the swing running INTO the weekly extreme (swing projection fulcrum)"},
    {"id": "c5", "expr": "fib level alone insufficient; must overlap a lesser-TF opposing PD array"},
    {"id": "c6", "expr": "swing grades == [stage1, equilibrium, third_swing_grade, terminus]"},
    {"id": "c7", "expr": "third_swing_grade == midpoint(equilibrium, terminus); no stop run expected there"},
    {"id": "c8", "expr": "consolidation_thursday_reversal entry IS a turtle soup, small size only"},
    {"id": "c9", "expr": "seek_and_destroy templates are observed, never traded"},
    {"id": "c10", "expr": "hold window for Tue/Wed profiles == into Thursday New York session"}
  ],
  "timeframes": ["H1", "H4", "D", "W", "MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["weekly-range-profiles", "one-shot-one-kill", "monday-wednesday-range", "low-resistance-liquidity-run", "symmetrical-price-projections", "turtle-soup", "liquidity-pool", "bullish-order-block", "bearish-order-block", "liquidity-void", "mean-threshold", "dealing-range-equilibrium"],
  "sources": ["ICT-2017-STT-MM-TEMPLATES", "ICT-2017-STT-WEEKLY-PROFILES", "ICT-2017-STT-BLENDING-IPDA-PD"]
}
```

## Visual Pattern

```
  BEARISH TEMPLATE — classic Tuesday high of the week (H1)

  M      T      W      T      F
         ╱▔╲   <- WEEKLY high: old DAILY high run (entry array TF = D)
        ╱   ╲
   ────╱     ╲──────────────────  fulcrum swing = Mon low -> Tue high  (= R)
  ╱             ╲
                 ╲______          <- 1.27 R below Tue high
                        ╲____     <- 1.68 R below Tue high
                             ▓▓   <- H4 discount array  (target TF = H4 < D  ✓)
                                     TARGET = fib level AND array, overlapping

  The rule that makes it a template and not a guess:
      entry array on D  ->  target array must be H4 or H1.
      entry array on MN ->  target array may be W or D.
      Never target the same or a higher timeframe than the entry array.
```

## Timeframes

Entry arrays are read on **monthly, weekly, daily and H4**; targets on any strictly lower timeframe, in practice **H4 and H1**. All template diagrams are drawn on **H1** (01:22).

## Examples

**Example 1 — bearish gap-open template, walked verbatim (`ICT-2017-STT-MM-TEMPLATES`, 12:01–13:17):**
- Setup: Sunday gaps lower, Monday trades higher, Tuesday London or New York makes the weekly high filling a fair value gap into a **daily bearish order block**.
- Trigger: short at the daily order block. Entry TF = D.
- Target: "we would be looking for a four hour discount PD array to take our profits, but it has to overlap with a projection on that fair value or liquidity void swing that's going up into Tuesday… measure your FIB from that low up to the highest one on Tuesday and your projections down in the form of 127 or 168."

**Example 2 — AUDUSD, March 2017, template applied live (`ICT-2017-STT-BLENDING-IPDA-PD`, 13:44–15:02):**
- Setup: weekly high on Tuesday at an old daily high — "It traded slightly above Monday's high. Rejected it."
- Entry TF = daily ("that's a liquidity pool raid on a daily high", 14:41).
- Target: "we're going to drop down to a four hour and or a one hour chart to look for a discount PD array. It comes in the form of a liquidity void. Taking us down into 76.05 was our objective." Short framed at 76.80.

## Common Mistakes

- **Targeting the same or a higher timeframe than the entry array.** This is the single rule ICT restates in every one of the twelve templates. A monthly-array entry targeted at another monthly array is a multi-week hold, not a one-shot-one-kill.
- **Taking the 127/168 as a standalone target.** The extension must overlap a lesser-timeframe opposing PD array; ICT names the pairing "a high confluence level where we have both time and price in a green where the algo may very easily reach for those levels" (29:05).
- **Anchoring the fib on the wrong swing.** The fulcrum is the leg that runs *into* the weekly extreme (Tuesday's low → Wednesday's high, for a Wednesday high), not the whole week and not the prior swing.
- **Trading the seek-and-destroy templates.** They are diagnostic only.
- **Sizing the Thursday-reversal turtle soup normally.** "Don't put a lot of money on this type of trade because if it's FOMC, you can get really crushed if it's a lot of whipsaw on it" (24:33).
- **Demanding the exact high or low.** "you may not get the actual highest high to short from or the lowest low to buy from. And that's not important. Once we have the range defined and we see the characteristics that outline a potential direction going into Friday's close, that in itself can be your one shot, one kill" (39:00–39:21).

## Related Concepts

- [weekly-range-profiles](../25-htf-bias/weekly-range-profiles.md) — the twelve shapes these templates are laid over.
- [one-shot-one-kill](one-shot-one-kill.md) — the model these templates serve; weekly objective 50–75 pips.
- [symmetrical-price-projections](../28-fibonacci-levels/symmetrical-price-projections.md) — the "perfect symmetrical price swing" leg of the overlay.
- [turtle-soup](../20-turtle-soup/turtle-soup.md) — the consolidation-Thursday-reversal entry.
- [low-resistance-liquidity-run](../02-liquidity/low-resistance-liquidity-run.md) — how the entry and target arrays are located within the range.
- [monday-wednesday-range](../25-htf-bias/monday-wednesday-range.md), [liquidity-pool](../02-liquidity/liquidity-pool.md), [liquidity-void](../02-liquidity/liquidity-void.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [mean-threshold](../27-equilibrium/mean-threshold.md), [dealing-range-equilibrium](../27-equilibrium/dealing-range-equilibrium.md).

## Citations

- `ICT-2017-STT-MM-TEMPLATES` (00:00) "this is **lesson 3**, short term trading… teaching market maker manipulation templates"; (00:22–01:14) the templates blend onto lesson 2's weekly profiles; (01:22–01:38) every diagram is a 60-minute chart; (02:29–03:11) hold into Thursday's New York session, and the lesser-timeframe target rule stated in full; (03:35–03:55) 127 / 168 / "a 100% symmetrical price swing or what I classify as a perfect market structure swing"; (05:29–06:44) order-block entries at first swing grade, equilibrium or third swing grade, and the 100% measured move; (06:00–06:21) no stop run expected at the third swing grade; (08:37–08:53) why the target must be a lesser timeframe; (12:01–13:17) the bearish gap-open worked template; (16:12–16:28) "we're not just simply looking for 127 and 168 extensions"; (17:22–17:42) the four swing stages ending at terminus; (21:38–21:57) the fulcrum anchored Tuesday's low to Wednesday's high; (23:55–24:47) the consolidation-Thursday-reversal turtle soup and its position-size cap; (26:02) "This is a turtle soup short"; (27:33–27:48) the swing projection fulcrum for midweek rallies; (29:05–29:19) confluence of fib and lesser-TF array; (30:53–31:42) the manual 1.27 and 1.68 arithmetic; (34:15–35:18) seek and destroy observed, not traded, and used as a reversal alert; (35:58) "this is not the same as the Wednesday low of the week templates"; (36:15–37:23) the Wednesday weekly reversal driven by news at retail support/resistance; (38:01–38:14) "basically the playbook that I use"; (39:00–39:43) the exact extreme is not required, and "My objective is usually 50 to 75 pips a week".
- `ICT-2017-STT-WEEKLY-PROFILES` (10:47) "We will be giving you more insights about this when we start looking at the market maker templates" — the forward reference from lesson 2.
- `ICT-2017-STT-BLENDING-IPDA-PD` (13:44–15:02) the AUDUSD template applied live: daily-high liquidity raid on Tuesday, H4/H1 discount array as the objective; (15:02) "we get a combination of elements of time and price blending and using the market maker manipulation templates in accordance to our market profiles that we used and learned in lesson two".
