# One Shot One Kill

**Category:** 31-models
**Aliases:** OSOK, one-shot-one-kill, ICT short-term trading model, weekly-range model
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-STT-ONE-SHOT-ONE-KILL, ICT-2017-STT-MONTHLY-WEEKLY-RANGES, ICT-2017-STT-LRLR-CONSOLIDATION, ICT-2017-STT-LRLR-TRENDING, ICT-2017-STT-MM-TEMPLATES
**Tags:** model, short-term-trading, weekly-range, capstone, procedure

## Definition

One shot one kill is ICT's **short-term trading model**: one setup per week, framed from monthly and weekly ranges, executed on the hourly chart, targeting a fixed pip objective rather than a full weekly range. "It's the practice of trading a duration of one week or a few days. We use both the monthly and weekly charts to frame the setups. We trade in the direction of the present or next week's probable range" (`ICT-2017-STT-MONTHLY-WEEKLY-RANGES`, 01:16–01:26).

Its duration is bounded explicitly at both ends: "one shot, one kill is **not** defined by getting in on a Monday and getting out on a Friday. One shot, one kill is a couple days of trading… It can be as little as one day and as long as a week" (`ICT-2017-STT-LRLR-CONSOLIDATION`, 22:29–22:46). Its purpose is one payout, not one trade: "One shot, one kill is you're looking for **one setup to pay you your weekly objective**" (`ICT-2017-STT-MM-TEMPLATES`, 39:31).

It is the March-2017 module's capstone and is delivered as **eight lessons**, of which this page is lesson 8 — the assembly procedure. ICT is explicit that it is not self-contained: "you have to know all the macro conditions and all the January content lessons… the prerequisite is to know those free tutorials" (`ICT-2017-STT-ONE-SHOT-ONE-KILL`, 00:35, 02:40).

## Formal Criteria

**The framing rule — opposing arrays, one timeframe apart.**
- "All we're doing is looking for a monthly PD array, whether it's discount or premium, based on our next logical price move… From that monthly array, you're going to look for an **opposing weekly array**. So if you're starting from a premium in a monthly basis, you're going to be looking for a weekly discount. That's your target" (`…-MONTHLY-WEEKLY-RANGES`, 09:30–10:10).
- The same construction one rung down *is* the setup: weekly premium → daily discount. "This, my friends, is the one shot, one kill setup. This is my bread and butter. This is the one that has consistent setups every single week" (23:12–23:17); mirrored for longs at 23:50.
- Between the two arrays, **every** premium array on W/D/H4 is a candidate short (mirrored for longs): "we're scanning for all of the premium arrays where we can take short-term trades from as a short" (16:25).
- The discount arrays on the way down must *break*: "we're looking for these arrays in the discount form to break. We want to see them break. And we want to see them continuously keep breaking until we get down to our weekly discount array" (14:46–14:55).
- **Execution timeframe is fixed:** "Our one hour chart is our executable time frame for one shot, one kills or short-term trading" (16:40), "and it has to drop down into a kill zone" (30:07). Asia's window is given plainly: "6 p.m. to 9 p.m. New York Standard Time" (30:34).

**The eleven-step procedure (lesson 8, 05:11–10:14).** In ICT's order:
1. Determine the current or next **quarterly shift**.
2. Identify the higher-timeframe **PD arrays in the IPDA data ranges** (20 / 40 / 60 days).
3. Read **interest-rate differentials and the rate market's own profile** — "If they're trending then you're going to get movement permitted in the euro dollar. If they're consolidated and tight it's going to be very hard for the market to move around" (07:00–07:05).
4. Scout **seasonal tendencies**.
5. Run **swing analysis** from the higher timeframes down to H1, classifying impulse / retracement / expansion legs.
6. Anticipate the **weekly profiles** that may unfold.
7. Select the matching **market maker manipulation templates**.
8. Locate the **premium and discount ranges**.
9. Wait for **volatility to signal range expansion** — "We want to be getting in and the market is quiet so that we can expand and get larger ranges" (09:05).
10. Confirm with **COT commercials versus large traders, and open interest**.
11. Frame the **low resistance liquidity run** with opposing PD arrays, converge a **fib** on the target array, and confirm with **intermarket analysis**.

**Confluence pattern.** ICT requires only two non-price agreements before technicals are consulted: "you really only need two things to couple for smart money — you have the seasonal tendency" and the commercial hedging read (21:06–21:12), and neither is sufficient alone: "without technicals aligning with that in a market environment that supports that idea, the seasonal tendency will get you in trouble" (22:34–22:42).

**COT construction.** The commercial line is re-based by hand: "I look at the last year… and I get the highest high and the lowest low of their commercial activity. In other words, I'm only tracking commercials" (14:38–14:51); "There is no indicator. Okay, what I actually do is I actually create this with paint" (14:57–15:03). Above the re-based line is bullish, below bearish (17:34–17:52).

**Level calibration.** "generally the rules are we round up to the nearest five or zero level" (23:41).

**Day-of-week gate.** "Day of week concept looking for the high or low to form on **Monday through Wednesday with the 70% odds** of it happening" (01:30–01:41) — see [monday-wednesday-range](../25-htf-bias/monday-wednesday-range.md).

## Formula / Math

```
# FRAMING — one timeframe apart, opposing polarity
origin  := PD_array(MN)               # or W, one rung down
target  := opposing_PD_array(next_lower_tf)      # MN premium -> W discount
                                                 # W  premium -> D discount
range   := |origin - target|                     # the whole tradable band

# CANDIDATE ENTRIES — every same-polarity array between the two
entries := { premium_array(tf) : tf in [W, D, H4] }      # bearish case
execute_on := H1  AND  time in killzone
              # Asia killzone == 18:00-21:00 America/New_York

# TARGET REFINEMENT
target_price := opposing_array(tf < entry_tf)  INTERSECT  fib(1.27 | 1.68 | 1.00)
target_price := round_to_nearest(5 or 0)

# CONFIRMATION LADDER (two non-price agreements minimum)
smart_money := seasonal_tendency AND commercial_hedging_extreme
tradeable   := smart_money AND technicals_agree AND intermarket_agrees

# COT re-based zero line
zero_line := midpoint( max(commercial_net, 12m), min(commercial_net, 12m) )

# OBJECTIVE
weekly_pip_target := 50..75            # ICT's own; beginners 30..50; cap 100
```

## Machine-Readable

```json
{
  "id": "one-shot-one-kill",
  "category": "31-models",
  "aliases": ["OSOK", "ict-short-term-trading-model", "weekly-range-model"],
  "criteria": [
    {"id": "c1", "expr": "duration in [1 day, 1 week]; NOT Monday-in Friday-out by definition"},
    {"id": "c2", "expr": "framing := PD array on tf X paired with the OPPOSING array on tf X-1"},
    {"id": "c3", "expr": "canonical setup == weekly premium -> daily discount (and mirror)"},
    {"id": "c4", "expr": "execution timeframe == H1, inside a killzone"},
    {"id": "c5", "expr": "asia killzone == 18:00-21:00 America/New_York"},
    {"id": "c6", "expr": "intervening opposing arrays must break on the way to the target"},
    {"id": "c7", "expr": "day-of-week gate: weekly high or low forms Mon..Wed with ~70% odds"},
    {"id": "c8", "expr": "two non-price agreements required (seasonal + COT commercials) before technicals"},
    {"id": "c9", "expr": "COT zero line re-based to the 12-month commercial high/low midpoint"},
    {"id": "c10", "expr": "levels rounded up to the nearest 5 or 0"},
    {"id": "c11", "expr": "weekly objective 50-75 pips (ICT); 30-50 for beginners; do not exceed 100"},
    {"id": "c12", "expr": "one setup per week is the goal, not one trade per day"}
  ],
  "timeframes": ["H1", "H4", "D", "W", "MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["weekly-range-profiles", "market-maker-manipulation-template", "low-resistance-liquidity-run", "monday-wednesday-range", "intraweek-market-reversal", "swing-trading-hallmarks", "commitment-of-traders", "seasonal-tendency", "quarterly-shift-theory", "ipda-data-ranges", "pd-array-matrix", "killzone-overview", "power-of-three"],
  "sources": ["ICT-2017-STT-ONE-SHOT-ONE-KILL", "ICT-2017-STT-MONTHLY-WEEKLY-RANGES", "ICT-2017-STT-LRLR-CONSOLIDATION", "ICT-2017-STT-LRLR-TRENDING", "ICT-2017-STT-MM-TEMPLATES"]
}
```

## Visual Pattern

```
  THE FRAMING — opposing arrays, one timeframe apart

  MONTHLY  ▓ premium array  ── origin ─────────────────────────────
              │
              │   candidate SHORT entries, every one of them:
              │      ▓ weekly premium array
              │      ▓ daily  premium array      <- execute each on H1,
              │      ▓ H4     premium array         inside a killzone
              │
              │   discount arrays on the way down must BREAK
              ▼
  WEEKLY   ▓ discount array ── target ─────────────────────────────
                                (round up to nearest 5 or 0)

  THE WEEK — where the setup is expected to appear

   S   M   T   W   T   F
       └───────┘                  low (bullish) or high (bearish) forms here, ~70%
               └───────┘          expansion into the weekly array
       └───────────┘              30-50% of the weekly range done by Wed London close
```

## Timeframes

Framed **monthly → weekly** (or weekly → daily), scanned on **W / D / H4**, executed on **H1** inside a killzone. H4 is the working chart for the setup itself; H1 for the fill. Below H1 the model is no longer this model: "Anything less than a 60 minute chart, you're really just day trading or you're scalping" (`ICT-2017-STT-LRLR-TRENDING`, 20:19).

## Examples

**Example 1 — EURUSD, last week of March 2017, the lesson's own live call (`ICT-2017-STT-ONE-SHOT-ONE-KILL`, 10:14–12:05, 30:24–35:21):**
- *Seasonal:* the euro's tendency declines from mid-March into the first week of April (13:47–14:06).
- *COT:* the euro made a higher high than January while "the commercials are actually selling aggressively in that rally" (19:14) — the two smart-money agreements are in place.
- *Intermarket:* DXY sitting on a **weekly discount array** (an old weekly high) with a daily mitigation block at **98.92**, rounded to **98.95**; EURGBP sold off all week into an H4 bullish order block.
- *Framing:* Monday's rally traded into the **weekly bearish order block** — high of the week assumed on Monday.
- *Entry / targets:* the London-to-New-York intraday swing fibbed to project **1.0908**; ICT published that number and 1.0650 in advance. "the actual high was 10909… I was one pip off" (10:36, 30:55).
- *Outcome:* the week's low printed **1.0655** on the recording's feed with 1.0650 hit on most platforms — "Being one pip off from the high of the week and only five pips off the low of the week" (35:16).
- *Interpretation of Monday:* "the initial rally here we saw on monday was a false rally. All that was was heavy selling — they engineered price higher built in a premium so they can sell it" (31:33–31:43), described as "the power three or dare I say it weekly Judas swing" (31:27, whisper renders "Judas" as "judith").

## Common Mistakes

- **Trading it as a Monday-open / Friday-close position.** ICT rules this out by definition.
- **Targeting an array on the same or a higher timeframe than the entry array.** The one-rung-apart rule is what bounds the hold to a week — see [market-maker-manipulation-template](market-maker-manipulation-template.md).
- **Demanding the exact weekly high or low.** "We don't try to go in here and time that weekly high… you can sell a very small portion on monday, and then if tuesday fails to make a higher high at least you have a small piece on the higher level" (29:36–29:56).
- **Chasing pips past the objective.** "just know that it's important not to get pip drunk trying to get a lion's portion of a move by Friday's close" (`ICT-2017-STT-LRLR-TRENDING`, 24:43).
- **Trading a seasonal or a COT reading on its own.** Both are probabilistic context; the technical array is the trigger.
- **Forcing a setup.** "If it's not obvious, if it's simply just not clear enough on your charts, just simply sit on your hands and wait. These types of setups form every single week" (`…-MONTHLY-WEEKLY-RANGES`, 02:07–02:22).
- **Treating the model as mechanical.** "There's not going to be a clear cut this is how you do it every single time. There's going to be potential decisions that you're going to have to make" (`…-ONE-SHOT-ONE-KILL`, 33:27–33:36).

## Related Concepts

- [weekly-range-profiles](../25-htf-bias/weekly-range-profiles.md) — step 6 of the procedure.
- [market-maker-manipulation-template](market-maker-manipulation-template.md) — step 7; the entry/target overlay.
- [low-resistance-liquidity-run](../02-liquidity/low-resistance-liquidity-run.md) — step 11; how the two arrays are located and graded.
- [monday-wednesday-range](../25-htf-bias/monday-wednesday-range.md) — the day-of-week gate and the 70 % figure.
- [intraweek-market-reversal](intraweek-market-reversal.md) — the model's principal failure mode.
- [swing-trading-hallmarks](swing-trading-hallmarks.md) — the discipline one rung up, whose setups overlap and outrank this one.
- [commitment-of-traders](../03-order-flow/commitment-of-traders.md), [seasonal-tendency](../04-time-cycles/seasonal-tendency.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md), [ipda-data-ranges](../23-ipda/ipda-data-ranges.md), [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md), [killzone-overview](../10-killzones/killzone-overview.md), [power-of-three](../12-power-of-three/power-of-three.md).

## Citations

- `ICT-2017-STT-ONE-SHOT-ONE-KILL` (00:00–00:22) "welcome to **lesson 8** one shot one kill trading model for the short term trading module for ICT mentorship — this is the last of **March's** content"; (00:35–02:13) the prerequisite list, including "**Day of week concept looking for the high or low to form on Monday through Wednesday with the 70% odds of it happening**" (01:30–01:41), power three on weekly candles, fibs for targeting, killzones, seasonals and COT; (02:25–03:07) the free tutorials as prerequisite; (05:11–10:14) the eleven-step procedure in order; (13:47–14:13) the euro's March seasonal decline; (14:26–15:12) the hand-built commercial line, "I actually create this with paint"; (16:00–17:05) the 12-month high/low of commercial net positions, commercials only; (17:34–17:52) above the line net long, below net short; (19:14–19:24) "the commercials are actually selling aggressively in that rally"; (21:06–22:42) two agreements are enough, but "without technicals aligning… the seasonal tendency will get you in trouble"; (23:05–23:48) the DXY weekly discount array, the 98.92 mitigation block and "we round up to the nearest five or zero level"; (26:20–27:10) EURGBP as the intermarket confirmation; (27:23–28:00) Monday's trade into the weekly bearish order block; (29:04–30:11) assuming Monday is the high of the week; (29:36–30:02) partial sizing rather than timing the exact high; (30:24–31:06) the intraday fib producing 1.0908 against an actual 1.0909; (31:27–31:48) "the power three or dare I say it weekly Judas swing" and Monday's rally as engineered supply; (33:27–33:36) the model is not mechanical; (34:58–35:21) "one pip off from the high of the week and only five pips off the low of the week".
- `ICT-2017-STT-MONTHLY-WEEKLY-RANGES` (00:00–00:24) "Welcome to **March 2017** content for the ICT Mentorship. This month, we're teaching short-term trading. This is **lesson one**, combining higher time frame monthly and weekly ranges"; (01:16–01:31) the definition and the weekly range as "the backbone"; (02:07–02:26) do not force a setup; (09:30–10:10) the opposing-array framing rule; (12:39–16:47) the monthly→weekly→daily→H4 scan and "Our one hour chart is our executable time frame"; (14:46–15:03) intervening discount arrays must break; (23:12–23:50) "This, my friends, is the one shot, one kill setup. This is my bread and butter"; (26:52–30:07) the general concept — seasonal, rates, COT, intermarket, then the Monday-to-Wednesday impulse/retracement/expansion, "and it has to drop down into a kill zone"; (30:34–30:53) the Asia killzone at 6 p.m.–9 p.m. New York; (34:27) "There is generally four weekly candles in every monthly candle"; (35:40) "There's generally five daily candles in every weekly candle".
- `ICT-2017-STT-LRLR-CONSOLIDATION` (22:29–22:46) the duration bounds — a day to a week, not Monday-to-Friday by definition.
- `ICT-2017-STT-LRLR-TRENDING` (07:09–07:27) the pip-objective ladder 30–50 → 50–75 → 75–100; (20:02–20:24) below H1 it is day trading or scalping; (24:43) "don't get pip drunk".
- `ICT-2017-STT-MM-TEMPLATES` (39:31–39:43) "One shot, one kill is you're looking for one setup to pay you your weekly objective. My objective is usually 50 to 75 pips a week."
