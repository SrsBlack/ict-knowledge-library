# Loss Mitigation By Half-Size Re-Entry

**Category:** 32-risk-management
**Aliases:** mitigating a losing trade, half-size re-entry, loss recovery ladder, second stab
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-MITIGATE-LOSING-TRADES
**Tags:** risk, drawdown, r-multiple, position-sizing, re-entry, order-blocks

## Definition

A mechanical rule for recovering a stop-out **on the same setup, at half the risk**. When a
trade is stopped out but the directional premise is still intact, ICT teaches re-entering on the
next order block with **half the position size used on the losing trade**, and with the stop
moved from the mean threshold to **below the whole order block**. Because a half-size trade
reaching **2R** returns exactly the full original loss, the drawdown is erased without ever
increasing risk: "our losing trade that we just had using half of the initial risk is already
mitigated" (`ICT-2016-MITIGATE-LOSING-TRADES`, 07:39–07:46).

The rule inverts the instinct it is designed to replace: "You don't need to do it by scaling up
your risk. You actually do it by **scaling back** your risk" (16:46–16:51).

⚠ This is arithmetic and position-sizing procedure, not trading psychology. The lecture's one
psychological passage is a forward reference to a different lesson (17:25).

## Formal Criteria

**Trigger.** A full stop-out on a setup whose premise has not been invalidated. ICT's diagnosis
of the typical cause is stop placement, not analysis: "just because it swept us out below the
mean threshold on our initial try going long, it doesn't mean the trade's completely no longer
viable. It just means that we probably were just inaccurate in terms of where our stop loss was
placed" (03:33–03:56).

**Re-entry level.** The next order block, validated the standard way — "With this down candle,
price trades away through it on this candle right here. It trades above that down candle. So
when it does that, that authorizes any new return to this down candle as a buying opportunity"
(04:03–04:19). Entry is at the **top / opening of the down candle** (05:53–06:20).

**Stop.** Moved outward, deliberately: "This time, our stop loss is going to actually be **below
the order block** that we're framing our trade around" (04:49–04:54) — not below the
[mean-threshold](../27-equilibrium/mean-threshold.md), which is what got hit the first time.

**Size.** Halved, every time: "we're going to go long with **one half of the position size** we
used on the initial loss. So, for instance, if we took a initial loss of 2 % on the first trade,
we have to go down to 1 %. If we were trading with 1 % and we took a full loss on the initial
trade, we would have to drop down to one half of 1 % of our total equity base" (05:20–05:44).
The ladder continues on a second failure: after 2 % then 1 %, "You would have to go down to one
half 1 %" (14:14–14:18).

**Recovery ladder at half size.**

- **R1** — "we got half of our initial loss back in open profit" (07:22–07:29).
- **R2** — the loss is fully mitigated (07:29–07:46). This is the decision point.
- **R3** — "in my opinion, that's about where you want to take your profits and square it off"
  (10:08–10:20).

**Exit discipline at R2 — two stages of trader development.**

1. *Developing:* take it off. "Sometimes, it's just good to get back to even and relax and then
   regroup, especially if you're late in the week… Close the week flat. **Do not go into the
   weekend with a net loss**" (07:56–08:23).
2. *Next stage:* if you stay in, trail to the mitigation point and never give it back. "this is
   where you want to trail the stop loss up to where you can no longer lose back below open
   profit of the 2 % loss. Once it's been mitigated, you're going to lock that in" (09:23–09:44).

**The reason for halving, stated as a risk-of-ruin argument.** "if, say, for instance, that your
first hit at 2 %, you took a 2 % loss. How do you know that's not a beginning of a 10-string
losing? In other words, what's to say you don't get nine more losing trades in a row?…
So if you do that and you keep going at 2 % or worse, you increase your risk. You're throwing
good money after bad" (16:51–17:15).

**Recovery does not require the original objective.** "notice that we're already able to mitigate
the initial loss of a total 2 % hit on our equity. And it hasn't even really fully moved to our
objectives" (09:01–09:11); the buy stops above the old highs are never reached (08:45–09:01).

## Formula / Math

```
# Ladder
risk(attempt 1) := r0                       # e.g. 0.02 of equity
risk(attempt n) := r0 / 2^(n-1)             # 2% -> 1% -> 0.5% -> ...

# Mitigation point of attempt n, expressed in R of attempt n
loss_carried(n) := sum(risk(1) .. risk(n-1))          # in equity fraction
R_to_break_even(n) := loss_carried(n) / risk(n)

#   n = 2:  loss_carried = r0,          risk = r0/2   -> 2R
#   n = 3:  loss_carried = 1.5 * r0,    risk = r0/4   -> 6R
#   ^ ICT works only the n = 2 case numerically; the n = 3 case is the
#     ladder's own consequence and is NOT quoted in the lecture.

# Trade construction on the re-entry
entry := open / top of the validated down candle (bullish OB)
stop  := below the ORDER BLOCK        # NOT below the mean threshold
valid := the OB has been traded through on the upside before the return   (04:03-04:19)

# Decision rule
if R >= 2:                    # loss mitigated
    developing_trader -> flatten
    experienced       -> trail stop to the R2 price, never permit a give-back
if R >= 3:                    # ICT's stated square-off zone
    take profit
```

⚠ Note the asymmetry the rule buys: at half size, **2R** repays a full-size **1R** loss, and
ICT's argument is that 2R–3R setups are common enough to make that trivial — "how many times
have we talked about opportunities, how there's so many opportunities of the frame 3 to 1 or 5
to 1 or even more throughout the week, you don't need very much to get that losing trade back"
(10:42–10:54).

## Machine-Readable

```json
{
  "id": "loss-mitigation-half-size-reentry",
  "category": "32-risk-management",
  "aliases": ["half-size-re-entry", "loss-recovery-ladder", "mitigating-a-losing-trade"],
  "criteria": [
    {"id": "c1", "expr": "trigger == full stop-out with the directional premise still intact"},
    {"id": "c2", "expr": "risk(attempt n) == risk(attempt 1) / 2^(n-1); worked ladder 2% -> 1% -> 0.5%"},
    {"id": "c3", "expr": "re-entry level == next order block, validated by price trading through it first"},
    {"id": "c4", "expr": "entry == open/top of the down candle (bullish case)"},
    {"id": "c5", "expr": "stop == below the whole order block, NOT below the mean threshold"},
    {"id": "c6", "expr": "at half size, R2 repays the full prior loss exactly"},
    {"id": "c7", "expr": "R1 == half the prior loss recovered in open profit"},
    {"id": "c8", "expr": "R3 == ICT's stated square-off zone"},
    {"id": "c9", "expr": "at R2 a developing trader flattens; an experienced trader trails to the R2 price and never gives it back"},
    {"id": "c10", "expr": "do not carry a net loss into the weekend if the market offers the recovery"},
    {"id": "c11", "expr": "never increase risk after a loss; the halving is a risk-of-ruin argument against a losing string"},
    {"id": "c12", "expr": "mitigation does not require reaching the original objective"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["r-multiple", "risk-per-trade", "position-sizing", "partial-takes", "stop-placement-by-pd-array", "six-percent-monthly-model", "mean-threshold", "bullish-order-block", "mitigated-order-block"],
  "sources": ["ICT-2016-MITIGATE-LOSING-TRADES"]
}
```

## Visual Pattern

```
   attempt 1 — 2 % risk, stop under the MEAN THRESHOLD
   ┌──────────────────────────┐
   │ ▓ bullish OB             │  entry
   │ ─ ─ mean threshold ─ ─   │  stop  <- swept out here
   │                          │
   └──────────────────────────┘   result: -2.0 %

   attempt 2 — 1 % risk, stop under the WHOLE ORDER BLOCK
   ┌──────────────────────────┐
   │ ▓ next bullish OB (top)  │  entry
   │ ─ ─ mean threshold ─ ─   │  (no longer the stop)
   │ ▁▁▁▁▁ OB low ▁▁▁▁▁▁▁▁▁▁  │  stop
   └──────────────────────────┘

        R1 ──────  +0.5 %   half the loss back
        R2 ──────  +1.0 %   ← LOSS FULLY MITIGATED. flatten, or trail to here.
        R3 ──────  +1.5 %   ← net new equity high; ICT's square-off
                             (buy stops above the old highs never needed)
```

## Timeframes

The lecture works one order-block setup without naming a chart interval; the mechanics are
timeframe-agnostic and follow whatever timeframe the original setup was framed on. The
weekly-close rule at 07:56–08:23 is calendar-based, not timeframe-based.

## Examples

**Example 1 — the worked case (`ICT-2016-MITIGATE-LOSING-TRADES`, 00:56–09:11):**
- Setup: bullish order block identified, mean threshold marked, hypothetical long taken on the
  secondary order block at 2 % risk with the stop just below the mean threshold.
- Trigger: the mean threshold is violated; full 2 % loss (01:42–02:17).
- Re-entry: the next down candle is traded through on the upside, authorising the return
  (04:03–04:19). Long at the top of that candle, **1 %** risk, stop below the order block.
- Outcome: R1 = +0.5 % (half the loss back); **R2 = the full 2 % mitigated**; R3 = a new equity
  high, all inside one setup — and reached before the buy stops above the old highs are touched.

**Example 2 — the second rung of the ladder (13:14–14:18):**
- Setup: same chart, but the trader is stopped out twice — 2 % on the first attempt, then 1 % on
  a second attempt whose stop was again placed at the mean threshold.
- Trigger: the third return into the order block.
- Outcome: risk drops to **one half of 1 %**, with the stop below the low and the entry at that
  candle's opening. ⚠ The transcript degrades into repeated numeric fragments from 14:41 to
  16:28; only the setup and the closing statement at 16:29 are legible, so no R-figure for this
  third attempt is quoted here.

## Common Mistakes

- **Increasing size to "win it back".** The rule is the exact inverse, and ICT frames it as
  protection against a losing string, not as a mood-management technique (16:51–17:15).
- **Re-entering with the same tight stop.** The stop that got swept is the diagnosed cause; the
  re-entry moves it below the whole order block, and the halved size is what pays for the wider
  stop.
- **Treating R2 as arbitrary.** At half size R2 is exactly the prior loss. The number falls out
  of the halving; it is not a preference.
- **Re-entering on an invalidated premise.** The rule applies only while the directional read
  still holds — the entry level must still be an order block price has traded through.
- **Carrying the drawdown into the weekend when the market has offered it back** (08:19–08:34).
- **Reading this page as psychology.** The lecture's psychological content is one forward
  reference at 17:25 to a prior lesson on fear-based trading.

## Related Concepts

- [r-multiple](r-multiple.md) — the R-units the recovery ladder is denominated in.
- [risk-per-trade](risk-per-trade.md) — the base percentage the ladder halves from; the 2 % ceiling comes from [six-percent-monthly-model](six-percent-monthly-model.md).
- [position-sizing](position-sizing.md) — the calculation the halving feeds.
- [stop-placement-by-pd-array](stop-placement-by-pd-array.md) — the mean-threshold-versus-whole-block choice this lecture makes explicit.
- [mean-threshold](../27-equilibrium/mean-threshold.md) — the level whose violation triggers the rule.
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [mitigated-order-block](../07-order-blocks/mitigated-order-block.md) — the re-entry level and its validation.
- [partial-takes](partial-takes.md) — the scaling method used on the recovery leg.

## Citations

- `ICT-2016-MITIGATE-LOSING-TRADES` (00:24) "This is **teaching number five in the second month** of the ICT mentorship" — the dating anchor; (00:56–01:11) the standard markup: bullish order block, mean threshold, hypothetical long on the secondary order block; (01:33–01:53) "understanding the mean threshold, we don't want to see the middle of the down candle on a bullish order block be violated… you'll probably take the trade and want to have a stop loss just a little bit below this mean threshold"; (02:11–02:35) the 2 % stop-out, and a warning against sizing above it; (03:33–03:56) "it doesn't mean the trade's completely no longer viable. It just means that we probably were just inaccurate in terms of where our stop loss was placed"; (04:03–04:19) order-block validation — "It trades above that down candle. So when it does that, **that authorizes any new return to this down candle as a buying opportunity**"; (04:25–04:49) allow more movement against you, do not chase an ultra-tight stop; (04:49–04:54) "**our stop loss is going to actually be below the order block** that we're framing our trade around"; (05:20–05:44) ⚠ **the halving rule** — "we're going to go long with **one half of the position size** we used on the initial loss… 2 % → 1 %… 1 % → one half of 1 %"; (05:53–06:33) entry at the opening / top of the down candle, stop below the order block, "we're using half of the leverage and position size that we used on the initial loss"; (07:05–07:29) R1 returns half the loss; (07:29–07:46) ⚠ **R2 mitigates the loss entirely** at half size; (07:46–08:06) at R2 a new trader should consider taking the trade off; (07:56–08:34) "**Close the week flat. Do not go into the weekend with a net loss**"; (08:45–09:11) the recovery completes before the buy stops above the old highs are reached; (09:11–09:23) 3R is "new territory"; (09:23–09:50) the trail-to-mitigation rule for a trader who stays in; (10:08–10:20) "Once we get a multiple of R3… that's about where you want to take your profits and square it off"; (10:20–10:42) "you only need a multiple of R2 to get that trade paid back to you"; (10:42–11:02) 3:1 and 5:1 opportunities recur weekly, "They're easy to get back"; (11:33–11:58) the two stages of trader development at R2; (12:07–12:26) at 1 % risk an R2 recovery of a 2 % loss leaves "a new equity high, all in the same trade"; (13:14–14:18) the second rung — 2 % then 1 % then "one half 1 %", stop below the low; ⚠ (14:41–16:28) whisper output degrades into repeated "1 %" / "2 %" fragments and is not cited; (16:29–16:51) "Getting to that R3, you can get back your full 2 %… You don't need to have increased leverage… you do have to have patience"; (16:46–17:15) ⚠ "You actually do it by **scaling back** your risk… How do you know that's not a beginning of a 10-string losing?"; (17:25–17:30) forward/back reference to the fear-based-trading lesson — the only psychological passage in the lecture.
