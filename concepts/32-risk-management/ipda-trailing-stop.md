# IPDA Trailing Stop

**Category:** 32-risk-management
**Aliases:** 40-day trailing stop, 20-day trailing stop, data-range trailing stop, position trade stop trail
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-POSITION-TRADE-MGMT
**Tags:** risk, stop-loss, trailing, ipda, position-trading, daily

## Definition

The IPDA trailing stop trails a position behind the **lowest low of the last 40 trading days**
(for longs) or the **highest high of the last 40 trading days** (for shorts), tightening to a
**20-day** lookback only once the trade has covered a defined fraction of its expected range.
"You're going to be trailing your stop loss below the lowest low in the last 40 trading days"
(`ICT-2017-POSITION-TRADE-MGMT`, 05:50).

The rationale is drawn straight from the [IPDA data ranges](../23-ipda/ipda-data-ranges.md): in an
uptrend the algorithm is reaching for 40-day *highs*, so 40-day *lows* are the levels it is least
likely to revisit. "Because if we're looking for a bullish move, the market will most likely not
want to go back 40 trading days to find a low. It's going to be looking for the highs in the last
40 trading days" (06:03–06:14). Re-measured **every trading day** (11:22).

## Formal Criteria

**Phase 1 — entry to the tighten trigger:**
long → stop below `min(low)` of the last 40 trading days; short → stop above `max(high)` of the
last 40 trading days.

**Phase 2 — after the tighten trigger:** switch the lookback to **20 trading days**, same rule.

**The tighten trigger is stated two ways in the same lecture.** The slide gives **three quarters**
of the expected monthly/weekly range: "once it moves to about three quarters of the range that you
anticipate seeing, then what you're going to be doing is you're going to be looking for the
highest high in the last 20 trading days" (13:56–14:05). The worked chart example uses the
**halfway point**: "above halfway point you want to start trailing your stop loss tighter below
the low of the last 20 trading days, but prior to the equilibrium or halfway move you want to be
40 trading days back" (25:05–25:22). The demonstrated behaviour is the 50% version. Both readings
are recorded here because the lecture does not reconcile them.

**Range reference:** the "range" is the monthly and/or weekly swing being traded, gridded with a
Fibonacci from its low to its high (16:24, 24:09–24:21) — not the daily range.

**Stated reason for the tighten** (14:10–14:35): a deep retracement near the objective can become
the actual reversal. "Think like optimal trade entry — it could go 79% of the total move you
expect to see, but then fail and go the other direction, and you would just be knocked out with a
great deal of more larger loss by using that trailing 40 day stop loss."

**Hard prohibitions:** no break-even move, no ultra-tight trail. "In this time frame you are not
looking to trail your stop loss ultra tight… you can't demand really ultra tight stops in
long-term trading" (06:42–06:54). "Break even on long-term trading is just the worst thing they
possibly ever consider — you don't want to do that" (13:18–13:23).

## Formula / Math

```
# on the DAILY chart, recomputed each trading day
range_low, range_high := the weekly/monthly swing being traded
progress := (price - entry) / (range_high - range_low)      # long

if progress < TIGHTEN:
    stop_long  = min(low)  over last 40 trading days   - buffer
    stop_short = max(high) over last 40 trading days   + buffer
else:
    stop_long  = min(low)  over last 20 trading days   - buffer
    stop_short = max(high) over last 20 trading days   + buffer

TIGHTEN = 0.50   # per the worked example
TIGHTEN = 0.75   # per the slide text — unreconciled in-lecture
```

## Machine-Readable

```json
{
  "id": "ipda-trailing-stop",
  "category": "32-risk-management",
  "aliases": ["40-day-trailing-stop", "20-day-trailing-stop", "data-range-trailing-stop"],
  "criteria": [
    {"id": "c1", "expr": "phase1_stop_long == min(low, 40 trading days)"},
    {"id": "c2", "expr": "phase1_stop_short == max(high, 40 trading days)"},
    {"id": "c3", "expr": "tighten to 20-day lookback once trade covers 0.50 (example) or 0.75 (slide) of expected range"},
    {"id": "c4", "expr": "recomputed every trading day"},
    {"id": "c5", "expr": "break_even_move == forbidden"},
    {"id": "c6", "expr": "range measured on the weekly/monthly swing, not the daily"}
  ],
  "timeframes": ["D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["stop-placement-by-pd-array","risk-per-trade","r-multiple","partial-takes","capital-allocation-30-percent","ipda-data-ranges","ipda-40-day-lookback","ipda-20-day-lookback"],
  "sources": ["ICT-2017-POSITION-TRADE-MGMT"]
}
```

## Visual Pattern

```
   SHORT position, daily chart

   entry ──┐
           │   <-- 40 trading days -->
   ────────┼───●──────────────────────  stop ABOVE the 40-day high
           │    ╲                        (wide; algorithm is hunting
           ▼     ╲  ╱╲                    the 40-day LOWS, not highs)
                  ╲╱  ╲
                       ╲   ┄┄┄ 50% of expected range ┄┄┄
                        ╲
                         ╲   <-20 days->
                    ──────╲──●───────────  stop tightens to the
                           ╲                20-day high
                            ╲
                             ╲___ objective (weekly bearish OB)
```

## Timeframes

Daily chart execution; the range being graded is the weekly and/or monthly swing. ICT is explicit
that this is not transferable to intraday sizing — the demonstrated stop is 260 pips.

## Examples

**Example 1 — USDJPY short, ~8R (`ICT-2017-POSITION-TRADE-MGMT`, 17:25–21:02):**
- Entry: sell into a weekly bearish order block; candle open 121.69, high 121.72 — "only three
  pips higher than this opening price."
- 40-day high from the entry day sets the stop: "so you have a stop loss of 250 pips, you got to
  be above that, say 260 pips."
- Result at the objective: "we have eight times 260 pips… that's a massive move."
- ICT pre-empts the reaction: "some of you are probably cringing with that 260 pips. Good grief,
  it's long term trading, folks."

**Example 2 — USDJPY long through the US election (`ICT-2017-POSITION-TRADE-MGMT`, 22:38–23:08):**
- Long from a weekly bullish order block before the November 2016 election.
- The election whipsaw is survived because the stop sits below the 40-day low: "even with this
  wild whipsaw… 40 trading days back your stop has to be below here. So you're not knocked out
  long term, you're in there."
- Later legs: lowest low in the last 40 days = 109.19 across two candidate candles.

## Common Mistakes

- **Trailing on a 20-day lookback from the start.** That is the phase-2 rule. Used early it
  produces exactly the premature stop-out the method exists to prevent — "the worst thing that can
  happen is get knocked out prematurely and then the market moves take place and you miss out on
  that move" (06:32–06:42).
- **Moving to break-even.** Explicitly prohibited.
- **Grading progress against the daily range.** The 50%/75% fraction is of the weekly/monthly
  swing objective, not the day's range.
- **Trailing weekly instead of daily.** "Every trading day you're going to keep looking back —
  what was the highest high in the last 40 trading days" (11:22–11:36).
- **Assuming the 20-day switch guarantees a profit.** ICT's framing is comparative, not absolute:
  "if it does knock you out and goes to below a 20 day low, chances are you probably made a really
  handsome profit or you probably saved yourself a complete reversal" (15:39–15:52).

## Related Concepts

- [stop-placement-by-pd-array](stop-placement-by-pd-array.md) — the structural alternative used for initial placement on lower timeframes.
- [capital-allocation-30-percent](capital-allocation-30-percent.md) — the sizing regime this stop is built for.
- [ipda-data-ranges](../23-ipda/ipda-data-ranges.md), [ipda-40-day-lookback](../23-ipda/ipda-40-day-lookback.md), [ipda-20-day-lookback](../23-ipda/ipda-20-day-lookback.md) — the windows the stop reads.
- [partial-takes](partial-takes.md) — scaling out is taught alongside the trail.
- [r-multiple](r-multiple.md) — the 8R example above.

## Citations

- `ICT-2017-POSITION-TRADE-MGMT` (00:15) — "welcome back folks this is lesson 8 of the January 2017 ICT mentorship… possession trade management"; (05:50–06:14) the 40-day trail and its IPDA rationale; (06:32–06:54) premature stop-outs and no ultra-tight trailing; (07:19–07:54) the bullish tighten statement; (11:22–11:36) recompute every trading day; (13:18–13:23) break-even is "the worst thing"; (13:45–14:05) the bearish tighten statement at three quarters; (14:10–14:35) the 79%-retracement rationale; (15:39–15:52) what a 20-day stop-out means; (16:24, 24:09–24:21) the Fibonacci over the weekly/monthly range; (17:25–21:02) the 121.69 entry, 260-pip stop and 8R outcome; (22:38–23:08) surviving the election whipsaw; (25:05–25:22) "above halfway point you want to start trailing your stop loss tighter."
