# Six Percent Monthly Model

**Category:** 32-risk-management
**Aliases:** 6% per month, doubling model, growing small accounts, 20-pip model
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-GROWING-SMALL-ACCOUNTS
**Tags:** risk, compounding, position-sizing, r-multiple, small-accounts, targets

## Definition

The six percent monthly model is ICT's **starter growth target for a small account**: compound
6 % of equity per month, which doubles the account in a year. Its point is how little is
required to hit it — "It only takes you **20 pips per week** to do it and it only requires
**1.5 % risk** and it only requires **1 to 1 ratio** to do it" (`ICT-2016-GROWING-SMALL-ACCOUNTS`,
15:37–15:48). One qualifying trade a week is the whole workload: "even with low reward to risk
ratios, 1 to 1, you can still find 1.5 % return payouts per week, one trade that's all you need"
(16:40–16:53).

ICT presents it as deliberately unglamorous — "it doesn't sound sexy. It doesn't give you the
willies" (15:34–15:37) — and as the antidote to the account-blowing alternative: "Nobody gets
broke by taking profits. But they all go broke by taking too much risk" (05:15–05:18).

⚠ The model is **not** a claim about ICT's own returns. It is the floor he sets for a new
student. His own stated cadence is separate and larger — 50–75 pips a week (14:33).

## Formal Criteria

**The model.**

| Parameter | Value | Quote |
|---|---|---|
| Risk per trade | **1.5 %** | 15:41 |
| Reward:risk | **1:1** | 15:45 |
| Stop / target | **20 pips each way** | 15:49–15:53 |
| Trades needed | **one per week** | 16:47 |
| Monthly compounding | **6 %** | 15:26–15:33 |
| Annual outcome | **doubles the account** | 17:00–17:04 |

Worked at $1,000: "your risk per trade is going to be 1.5 % or **$15**… what you'd be risking is
20 pips from your entry price and your profit will be taken at 20 pips for a 1.5 % return"
(17:04–17:30). Ten years of it, unfunded further, is the closing claim: "a thousand dollars
becomes over two thousand dollars after 12 months… guess what that does in 10 years if you stick
to it and never add another penny out of your pocket? It's over a million dollars" (28:40–28:52).
⚠ Stated as an illustration; ICT supplies no track record for it.

**Where the setup comes from.** The daily chart, on the Month-1 material: "the 6 % per month
setups, they form specifically and the easiest ones to find are looking at your daily chart…
you're going to be looking for the things that I talked about in the very first month of this
mentorship. One specific is an **order block**" (17:39–18:03).

**The win-rate → minimum-R table** (07:40–09:08). ICT enumerates the accuracy each reward:risk
ratio can survive:

| Accuracy | Minimum reward:risk |
|---|---|
| 75 % | "very low" — no ratio given |
| 60 % | lower still — no ratio given |
| **50 %** | **1:1** |
| **40 %** | **1.5:1** |
| **33 %** | **2:1** |
| **25 %** | **3:1** |

"At 25 % accuracy… If 75 % of the trades that you take are losing trades, the minimum ratio for
profitability is you have to look for trades that pay out 3 to 1" (08:51–09:08). ⚠ This is the
**exact arithmetic breakeven** `1/(1+R)`, quoted by ICT himself — see
[r-multiple](r-multiple.md), whose earlier claim that every accuracy figure ICT quotes sits
*above* the arithmetic breakeven is contradicted by this table.

**The risk ceiling.** "Two percent ideally if you're a new trader, but **no more than two
percent** on an average. You don't need to have any more risk than that to build wealth"
(03:45–03:55).

**Scaling out, not all-or-nothing** (22:38–27:28). At the first 1:1 the whole position can be
closed for the week's 1.5 %; or half comes off for 0.75 % and the remainder runs to the mapped
buy stops. "At this point here, after your second multiple is reached, your stop needs to be at
break even" (24:47–24:52). The worked scale-out totals "over four percent just in that trade"
(27:21–27:27).

**What to avoid** (00:38–03:23, as four numbered rules): do not chase pips or percent returns;
do not open yourself to large risk hoping for large returns; do not assume small risk cannot
grow an account; do not sacrifice equity to poor planning.

## Formula / Math

```
# The model
risk_per_trade  := 0.015 * equity
stop            := 20 pips
target          := 20 pips                 # R = 1
trades_per_week := 1
=> weekly return ~ 1.5 %
=> monthly return ~ 6 %        # ICT: "a little bit more than 6%"   (16:53)
=> 1.06 ^ 12 = 2.01            # doubles in a year

# $1,000 worked
risk_$ = 1000 * 0.015 = 15     # 20-pip stop
# ICT's 10-year illustration: 1000 * (2 ** 10) ~ 1,024,000

# The accuracy / ratio pairing ICT enumerates
minimum_R(accuracy):
    0.50 -> 1.0
    0.40 -> 1.5
    0.33 -> 2.0
    0.25 -> 3.0
# each row satisfies  accuracy == 1 / (1 + R)  to within rounding:
#   1/(1+1.0) = 0.500     1/(1+1.5) = 0.400
#   1/(1+2.0) = 0.333     1/(1+3.0) = 0.250
# i.e. the table IS the arithmetic breakeven curve, stated as minima.

# Ceiling
max_risk_per_trade := 0.02
```

## Machine-Readable

```json
{
  "id": "six-percent-monthly-model",
  "category": "32-risk-management",
  "aliases": ["6-percent-per-month", "doubling-model", "growing-small-accounts"],
  "criteria": [
    {"id": "c1", "expr": "risk_per_trade == 1.5% of equity"},
    {"id": "c2", "expr": "reward_to_risk == 1:1, stop and target both 20 pips"},
    {"id": "c3", "expr": "one qualifying trade per week is sufficient"},
    {"id": "c4", "expr": "monthly compounding target == 6%; annual outcome == doubling"},
    {"id": "c5", "expr": "setups sourced from the DAILY chart using Month-1 material (order block, turtle soup, buy-stop mapping)"},
    {"id": "c6", "expr": "hard ceiling on risk per trade == 2%"},
    {"id": "c7", "expr": "minimum_R by accuracy: 50%->1:1, 40%->1.5:1, 33%->2:1, 25%->3:1"},
    {"id": "c8", "expr": "the accuracy table equals the arithmetic breakeven 1/(1+R); 25% at 3:1 is quoted explicitly"},
    {"id": "c9", "expr": "partial exits permitted at each R multiple; stop to break even after the second multiple"},
    {"id": "c10", "expr": "the 50%-in-one-month and 10-year-to-$1m figures are illustrations, not standards"}
  ],
  "timeframes": ["H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["r-multiple", "risk-per-trade", "position-sizing", "partial-takes", "loss-mitigation-half-size-reentry", "one-shot-one-kill", "institutional-sponsorship", "bullish-order-block", "turtle-soup"],
  "sources": ["ICT-2016-GROWING-SMALL-ACCOUNTS"]
}
```

## Visual Pattern

```
   The model, one week at a time:

   equity ──────────────────────────────────────────────►
     1.000 ┐
           │ +1.5 %  ┐
           │         │ +1.5 %  ┐
           │         │         │ +1.5 %  ┐
           │         │         │         │ +1.5 %
           └─ wk 1 ──┴─ wk 2 ──┴─ wk 3 ──┴─ wk 4 ──►  ≈ +6 % / month
                                                       1.06^12 = 2.01x / year

   One trade per week, framed on the daily:

     ▓ daily bullish OB
     entry 0.7542  (OB open + 5 pip spread)
     stop  0.7522  (20 pips, below the OB mean threshold)
     ──────────────────────────────────────────────
     1R  0.7562   ← 1.5 % banked; week is done
     2R  0.7582   ← stop to break even
     3R  0.7602   ← first pool of buy stops cleared
     5R  0.7642   ← equal highs / final buy stops
```

## Timeframes

Setups are **framed on the daily** and refined on the hourly: "our trade is being framed on the
daily chart. It's not a five minute setup. It's based on a institutional level on a daily chart"
(20:47–20:56). The lecture's worked example drops from the daily to a **one-hour** chart for the
entry (19:16).

## Examples

**Example 1 — the worked 5:1 (`ICT-2016-GROWING-SMALL-ACCOUNTS`, 17:53–28:22):**
- Setup: daily bullish order block at **0.7512**; on the hourly, price drives below an old low
  into the sell stops and slams into that level — "Now we are in turtle soup conditions"
  (19:46–19:49). Buy stops mapped above the equal highs before entry (20:12–20:33).
- Trigger: price trades up through the down candle, validating it; limit entry at the candle
  open plus a 5-pip spread = **0.7542**, stop **0.7522** (21:02–22:38).
- Outcome: 1R = 1.5 % (22:38–22:48). Half off at 1R = 0.75 % banked; stop to break even after the
  second multiple; the position runs to a fifth multiple as the buy stops above the equal highs
  are cleared (23:21–25:26). Scaled out, "you're over four percent just in that trade"
  (27:21–27:27). "This is a five to one setup. This is what a **one shot, one kill** looks like"
  (28:04–28:07).

**Example 2 — the 50 %-in-a-month illustration (10:58–14:54):**
- Setup: a $5,000 account, one month, "highly selective setups" (12:00–12:04).
- Outcome: "The profit actually grows over **$2,500**" (13:01–13:10), from **10 trades** with an
  average win of **51.80 pips** and a total haul of **518 pips** (14:33–14:54), logged in "the
  MyFX book for this mentorship" (12:48). ⚠ ICT immediately fences it: "That is what is possible
  **but not a standard**. Do not expect this as a normal every single month type thing"
  (13:14–13:24).

## Common Mistakes

- **Reading 6 % as ICT's performance.** It is the beginner's floor. His own stated cadence is
  50–75 pips a week (14:33), and he warns against exceeding his own sweet spot — "Every time I
  try to do that, I get a King Kong feeling" (15:06–15:13).
- **Trading every day to hit 20 pips.** Explicitly rejected: "I am not trying to instill an
  action warrior hero where you go in there and you're trying to prove to the world that you can
  trade every single day… If you do, you're inviting losses" (16:13–16:38).
- **Using 1:1 as the standard ratio.** "I'm not advocating looking for 1 to 1 ratio trades but
  I'm going to show you by example how easy it is to get that" (16:00–16:07). 1:1 is the
  *sufficiency proof*, not the target.
- **Sizing above 2 %.** The ceiling is stated flatly at 03:45.
- **Quoting the $1,000 → $1m figure as an expectation.** It is a compounding illustration with
  no track record attached.
- **Importing later vocabulary.** The word "array" appears nowhere in this lecture, nor in any
  Sep–Dec 2016 packet.

## Related Concepts

- [r-multiple](r-multiple.md) — the accuracy/ratio table above is this concept's primary source, and it corrects the earlier reading there.
- [risk-per-trade](risk-per-trade.md) — the 1.5 % working figure and the 2 % ceiling.
- [position-sizing](position-sizing.md), [partial-takes](partial-takes.md) — the scaling arithmetic in the worked example.
- [loss-mitigation-half-size-reentry](loss-mitigation-half-size-reentry.md) — the Month-2 lesson four teachings later, which halves down from these same percentages.
- [one-shot-one-kill](../31-models/one-shot-one-kill.md) — named at 28:05 as what the worked setup is.
- [institutional-sponsorship](../03-order-flow/institutional-sponsorship.md) — the reason ICT gives for the daily-framed setup working (28:11–28:22).
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [turtle-soup](../20-turtle-soup/turtle-soup.md) — the two Month-1 components the setup is built from.

## Citations

- `ICT-2016-GROWING-SMALL-ACCOUNTS` (00:23–00:31) "This is month two of the ICT Mentorship. This is **teaching one of eight of the second month of twelve**" — the dating anchor; (00:38–03:23) the four things to avoid; (02:25–02:41) "Once I understood the compound interest factor, it doesn't take much time at all for your money to grow… You can start on a shoestring budget even as little as **$100**"; (03:45–03:55) ⚠ "**Two percent ideally if you're a new trader, but no more than two percent** on an average"; (04:40–05:18) greed into fear, "Nobody gets broke by taking profits. But they all go broke by taking too much risk"; (05:23–05:40) "Identify trade setups that permit **three reward multiples to one risk or higher**"; (07:20–07:33) "accuracy is not even necessary in terms of high end accuracy to make money… but you do need **time**"; (07:40–09:08) ⚠ **the accuracy → minimum-ratio table** — 75 %, 60 %, 50 % ("you got to start risking $1 for $1"), 40 % ("$1.50 for every $1"), 33 % ("$2 for every $1 risk"), and **25 % ("the minimum ratio for profitability is you have to look for trades that pay out 3 to 1")**; (09:08–09:41) "we can be wrong 75 % of the time and still be net profitable"; (10:58–11:12) a 50 % monthly return framed as "a pretty good feat"; (11:12–11:18) "I'm not advocating that everyone's going to be able to make 50 % return in one month. It's not going to happen"; (12:00–12:04) "it doesn't take many trades to do that, but it does take **highly selective setups**"; (12:43–13:10) the MyFX book record — over 50 % return, "The profit actually grows over **$2,500**" on a $5,000 account; (13:14–13:24) ⚠ "That is what is possible **but not a standard**"; (14:11–14:33) "our goal is to have little to no drawdown… The idea in this mentorship is to avoid large drawdown"; (14:33–14:54) "my average goal for the week is **50 to 75 pips a week**… the average win is **51.80 pips** and with **10 trades** total haul of **518 pips** for the month"; (15:06–15:13) the King Kong warning against exceeding his own sweet spot; (15:26–15:48) ⚠ **the model** — "**6 % of your equity compounding per month**… It only takes you **20 pips per week** to do it and it only requires **1.5 % risk** and it only requires **1 to 1 ratio**"; (16:00–16:07) "I'm not advocating looking for 1 to 1 ratio trades"; (16:13–16:38) against daily trading; (16:40–16:56) one trade a week suffices, "you're actually going to have a little bit more than 6 %"; (17:00–17:04) "It doubles your money every single year and I don't care what your equity size is"; (17:04–17:30) the $1,000 worked case — 1.5 % = **$15**, 20 pips each way; (17:39–18:03) "the 6 % per month setups… are looking at your **daily chart**… the things that I talked about in the very first month of this mentorship. One specific is an **order block**"; (19:01–19:16) fractality and the drop to the hourly; (19:16–19:49) the 0.7512 daily level, the run below the old low, "Now we are in **turtle soup** conditions"; (20:02–20:07) "we're going to wait to see if the bank sponsors that level"; (20:12–20:33) mapping the buy stops above equal highs before entry; (20:47–20:56) "It's not a five minute setup. It's based on a institutional level on a daily chart"; (21:02–21:23) entry at the order-block open plus a 5-pip spread, 0.7542; (22:02–22:38) the 20-pip stop at 0.7522, framed below the down candle's midpoint; (22:38–22:48) 1R = 1.5 %; (23:21–23:27) half off at the first objective = 0.75 %; (24:47–24:52) "after your second multiple is reached, your stop needs to be at break even"; (25:22–25:26) the fifth multiple clears the buy stops; (27:01–27:27) the scale-out totalling "over four percent just in that trade"; (28:04–28:22) "This is a five to one setup. This is what a **one shot, one kill** looks like… **It's going to give you institutional sponsorship**… The banks trade off of daily levels"; (28:40–28:52) the $1,000 → $2,000 → "over a million dollars" compounding illustration.
