# Timeframe Selection

**Category:** 25-htf-bias
**Aliases:** timeframe selection, defining setups, trading style selection, TF-to-style map
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-TIMEFRAME-SELECTION
**Tags:** timeframes, trading-style, model-definition, setup-selection, framework

## Definition

Timeframe selection is ICT's **mapping of chart timeframe to trading style**, plus the
instruction to narrow to a **small fixed set of setups** that the individual trader can
actually see. It answers "which timeframe do I *operate* on?" — a different question from
[top-down-analysis](top-down-analysis.md), which prescribes the descent every trader
performs regardless of style.

The selection criterion ICT gives is not technical. "Your comfort level and your
psychological makeup as a trader has to align with that… your patience level, your
aptitude and your life" (`ICT-2016-TIMEFRAME-SELECTION`, 09:34–09:42). The lecture is
explicit that the mentor's own choice is not the answer: "don't think that I'm trying to
force you into a specific trading model" (10:26).

## Formal Criteria

**Timeframe → style map** (03:03–07:12)

| Timeframe | Style | Cadence |
|---|---|---|
| Monthly | long-term position trading | setups unfold over many months |
| Weekly | swing trading | "one or two trades within a three month period" (02:58) |
| Daily | short-term trading | holds of roughly one to five days |
| 4 hours or less | day trading | intraday, exits by 14:00 NY |

**Five trader models** (13:12–17:30)

1. **Trend trader** — trades only in the direction of the monthly and weekly charts, holds long.
2. **Swing trader** — trades daily intermediate-term price action; long waits, large payouts.
3. **Contrarian** — trades **reversal patterns at market extremes**, including capitulation
   or blow-off moves; does not require capitulation, a run above a previous month's high
   can serve.
4. **Short-term trader** — trades the **weekly range**, holds "typically about one to five
   days in duration" (17:16).
5. **Day trader** — intraday swing trading "with exits by 2 p.m. New York time" (17:22).

**Starting point**

- Regardless of intended end style, **start on the daily chart** (19:39–20:08). It carries
  the higher-timeframe reference points, supplies the directional bias, and is the chart
  ICT names as his own pick if forced to one: "it gives you the best of both worlds" (04:22).

**Setup selection — the three ICT trades** (39:30–47:13)

ICT reduces his own repertoire to three, all of which "exist in **all** timeframes" (47:04):

1. **Return into an exposed range** — price rallies or drops leaving a
   [liquidity void](../02-liquidity/liquidity-void.md), then retraces into it and expands
   again. This is the family that includes optimal trade entry.
2. **Order block** — sell into a bearish order block, buy into a bullish one.
3. **Stop run / turtle soup** — sell into a false break above a previous high (or buy a
   false break below a previous low).

- **One is sufficient:** "you only need one good pattern" (45:20).
- The setup a trader adopts should be the one they can *see*, not the one others discuss:
  "if you're seeing other people talk about their ability to do certain things and you feel
  frustrated… but you can see the turtle soup run on stops — **that's your pattern**. Don't
  force it" (47:25–47:43).

**Framing sequence within the chosen style** (35:39–39:26)

- Establish the range on the higher timeframe (a known high and a known low).
- Refine it on the next timeframe down.
- Lay a fib across the two reference points to **grade the swing**; the resulting levels
  are "areas at which the market should see new setups form" (38:17).
- The range is known **before** it trades, so setups can be anticipated rather than chased.

## Formula / Math

No quantitative criterion is taught. Selection is a procedure over trader constraints:

```
select_timeframe(trader):
    style := match(trader.available_screen_time,
                   trader.patience,
                   trader.tolerance_for_intraday_volatility)
    tf    := { position   -> Monthly
             , swing      -> Weekly
             , short_term -> Daily
             , day_trade  -> H4 or lower }
    return tf

select_setups(trader):
    # from exactly three; one is enough
    return subset_of({ return_to_exposed_range,   # liquidity void / OTE
                       order_block,
                       stop_run })                # turtle soup
    # invariant: each is valid on every timeframe

frame_trade(tf_high, tf_low):
    range   := (known_high, known_low) on tf_high
    grades  := fib(range)                 # 25% / EQ / etc. as setup zones
    setups  := look for selected_setups near grades on tf_low
```

## Machine-Readable

```json
{
  "id": "timeframe-selection",
  "category": "25-htf-bias",
  "aliases": ["defining-setups", "trading-style-selection", "tf-to-style-map"],
  "criteria": [
    {"id": "c1", "expr": "Monthly => position_trading"},
    {"id": "c2", "expr": "Weekly => swing_trading (1-2 trades per 3 months)"},
    {"id": "c3", "expr": "Daily => short_term_trading (hold 1-5 days)"},
    {"id": "c4", "expr": "TF <= H4 => day_trading (exit by 14:00 NY)"},
    {"id": "c5", "expr": "selection_driver == trader_psychology_and_schedule, not market state"},
    {"id": "c6", "expr": "recommended_starting_tf == Daily regardless of target style"},
    {"id": "c7", "expr": "setup_repertoire subset_of {return_to_exposed_range, order_block, stop_run}"},
    {"id": "c8", "expr": "each_setup valid_on all_timeframes"},
    {"id": "c9", "expr": "range_defined_on_higher_tf before setups_sought_on_lower_tf"}
  ],
  "timeframes": ["H4","D","W","M"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["top-down-analysis", "htf-bias-framework", "monthly-bias", "weekly-bias", "daily-bias", "turtle-soup", "liquidity-void", "ote-overview", "ict-day-trading-model"],
  "sources": ["ICT-2016-TIMEFRAME-SELECTION"]
}
```

## Visual Pattern

```
   TIMEFRAME                STYLE                 CADENCE
   ─────────────────────────────────────────────────────────────────
   Monthly     ┐
               ├─ position trading      setups unfold over months
   Weekly      ┘                        1-2 trades per quarter
   ─────────────────────────────────────────────────────────────────
   Daily       ── short-term trading     holds of 1-5 days
   ─────────────────────────────────────────────────────────────────
   H4 and below ─ day trading            intraday, out by 14:00 NY

   THE SAME THREE SETUPS APPLY AT EVERY ROW:

     return to exposed range      order block            stop run
      ╲                            ────█────              ──┐ ╱╲
       ╲___                             ╲                   │╱  ╲___
       ╱░░░╱  <- void refilled           ╲___              old high swept
      ╱  then expansion resumes                            then reversal
```

## Timeframes

The page is *about* timeframes. Every timeframe from monthly to M15 appears; the operating
choice is the trader's, and the three setups are timeframe-invariant by construction.

## Examples

**Example — EURUSD, monthly → weekly → daily (20:39–44:57):**
- **Monthly:** price consolidated ~600–700 pips, broke down below the last up candle's
  low, leaving a **bearish order block**. Over a year passed before price returned to it.
- **Setup:** on the return to that block, equal lows sat far below — "too clean" (31:18) —
  identifying long-term fund stops as the objective. Range known in advance:
  ~1.5100 down to ~1.2200, "over 2,900 pips" (35:39).
- **Timing:** ~13 months to set up, ~6 months to deliver — "half the time it took … to set
  up" (33:21).
- **Refinement:** the same swing on the weekly showed a breaker and a bearish order block
  as re-entries; on the daily, a fib graded the range and repeated **turtle soup / breaker
  / bearish OB / OTE** entries formed near the grades.
- **Point of the example:** one monthly read supplied months of setups across every style —
  position, swing, short-term and day — without changing the analysis.

## Common Mistakes

- **Copying the mentor's timeframe.** ICT states his own preference is H4-and-below and
  immediately warns "do not let me convince you or try to talk you into that's the best way
  to go, because it's not, it's not for everyone" (18:42).
- **Collecting every tool.** "Do we have to know all these things? No" (10:06). The stated
  benefit of modular study is discovering which few concepts resonate.
- **Benchmarking against other traders' setups** — called out explicitly as something
  traders "really shouldn't be doing" (47:13).
- **Confusing this with [top-down-analysis](top-down-analysis.md).** Top-down is the
  mandatory HTF→LTF descent; timeframe selection chooses the row you *trade* on. Both use
  the monthly, for different reasons.
- **Waiting for a setup the chosen timeframe cannot produce.** A weekly turtle soup into a
  monthly order block is a real pattern but, in ICT's words, "I would never have any
  trading opportunities because they don't happen that often" (09:04).
- **Reading the style table as a holding-period rule.** It maps the timeframe the *setup*
  is defined on; entries are routinely refined lower.

## Related Concepts

- [top-down-analysis](top-down-analysis.md) — the descent sequence; the complement to this page.
- [htf-bias-framework](htf-bias-framework.md) — where the directional read comes from.
- [monthly-bias](monthly-bias.md), [weekly-bias](weekly-bias.md), [daily-bias](daily-bias.md) — the per-timeframe reads.
- [ict-day-trading-model](../31-models/ict-day-trading-model.md) — the H4-and-below row, taught in full.
- [turtle-soup](../20-turtle-soup/turtle-soup.md), [liquidity-void](../02-liquidity/liquidity-void.md), [order-block-criteria](../07-order-blocks/order-block-criteria.md) — the three setups.
- [ote-overview](../17-optimal-trade-entry/ote-overview.md) — the fib-graded form of "return into an exposed range".

## Citations

- `ICT-2016-TIMEFRAME-SELECTION` (00:38) "this is the first of eight teachings in the third month of the ICT Mentorship… time frame selection and defining setups for your model"; (01:03) monthly for position trading; (02:54–03:08) "the weekly chart, we use that for swing trading… typically a one or two trades within a three month period"; (04:22–05:51) the daily chart "gives you the best of both worlds", ICT's own pick; (07:09) "four hours or less is day trading"; (09:34–09:49) selection driven by comfort level, psychological makeup, patience and life; (10:06) "do we have to know all these things? No"; (13:12–17:30) the five trader models — trend, swing, contrarian, short-term ("one to five days"), day trader ("exits by 2 p.m. New York time"); (18:42–18:49) "do not let me convince you… it's not for everyone"; (19:39–20:08) start on the daily chart; (20:39–35:47) the EURUSD monthly example — bearish order block, "too clean" equal lows, long-term fund stops, 13 months to set up and 6 to deliver, "over 2,900 pips"; (36:01–39:26) weekly and daily refinement, fib grading of the known range; (39:30–39:55) the three setups named — optimal trade entry, order blocks, stop runs "which we classically call the turtle soup"; (45:20–45:24) "you only need one good pattern"; (47:04–47:43) the three exist in all timeframes; "that's your pattern, don't force it".
