# Flout

**Category:** 15-sessions
**Aliases:** the flout, flout range, combined CBDR-Asian range, flout standard deviations
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-FILLING-NUMBERS, ICT-2017-INTRADAY-TOP-DOWN
**Tags:** sessions, range, standard-deviations, day-trading, projections, cbdr, asian-range

## Definition

The flout is the **single range formed by the [central-bank-dealers-range](central-bank-dealers-range.md) and the [asian-range](../14-asian-range/asian-range.md) taken together** — "the flout is the central bank dealers range and the Asian range combined… that whole time window, the highest high and the lowest low" (`ICT-2017-INTRADAY-TOP-DOWN`, 12:56–13:07). It exists to supply a third, coarser set of standard-deviation projections for the coming day's high and low, alongside the two component ranges' own projections.

Its one distinguishing rule is the **half-range unit**: unlike the CBDR and the Asian range, whose standard deviation is the full range replicated, the flout's standard deviation is **half** its range, projected from the range's centre. ICT is emphatic that this is the whole of it — "you've probably been expecting some PhD level presentation, but it's not that hard" (12:51).

## Formal Criteria

- **Window.** From the CBDR open through the Asian range close at **midnight New York time** — "the range that starts in central bank dealers range opening all the way to Asian range close at midnight New York time" (`ICT-2017-INTRADAY-TOP-DOWN`, 13:22). ⚠ The two sources give different start times; see *Common Mistakes*.
- **Range.** Highest high to lowest low across that window. Compute it **twice** — once on the wicks and once on the bodies: "the highest high and the lowest low, or in the form of the wick and in the form of the bodies of the candles" (13:00), because "we always have to factor in the potential error by looking at retail data feeds" (`ICT-2017-FILLING-NUMBERS`, 12:39).
- **Standard deviation = half the range, not the range.** "It's half of the range that makes up central bank dealers range and Asian range in terms of time. Find the highest high and lowest low, divide that range in half, project that up… only half of the range that makes the standard deviation, it's **not** the full range high to low" (13:51–14:04).
- **Projected from the centre.** "I go from the centre point, go up one, that's one standard deviation — two, three, four, and so on" (13:42–13:48). Equivalently, `flout_high` and `flout_low` are themselves ±1 SD, per `ICT-2017-FILLING-NUMBERS` (12:04–12:14): "the equilibrium of the flout range to the high of the range of the flout as one standard deviation; the equilibrium of the flout range to the low of its range is counted as one standard deviation."
- **Unbounded deviation count.** "There isn't a rule-based idea like there is for central bank dealers range or Asian range. Asian range can go up one or two standard deviations and create a high… **flout can be many standard deviations** that have to keep being applied and added to as the daily range goes up. You keep adding another level of flout" (15:01–15:22).
- **A projection is not an entry.** A flout level is actionable only where it **overlaps a 15-to-60-minute PD array** in the right direction: bullish → "confluences of flout standard deviations and central bank dealers range and Asian range with **discount arrays on the 60 to 15 minute** is ideal for entries" (14:05–14:22); bearish → the same with **premium arrays** (14:22–14:41).
- **Accuracy claim.** Blending flout, CBDR and Asian-range deviations with the average daily range puts the projection "many times **within 10 pips** of the daily high and low" (18:41–19:02) — which is ICT's stated reason for banking profit ten pips early.

## Formula / Math

```
# Window (New York time). See Common Mistakes for the 14:00 vs 15:00 discrepancy.
W          := [CBDR_open .. 00:00 NY]

flout_high := max(high) over W          # compute a wick version AND a body version
flout_low  := min(low)  over W
R          := flout_high - flout_low
EQ         := (flout_high + flout_low) / 2

SD_unit    := R / 2                     # HALF the range — the flout's defining rule

SD_up(n)   := EQ + n * SD_unit          # n unbounded; SD_up(1) == flout_high
SD_down(n) := EQ - n * SD_unit          #              SD_down(1) == flout_low

# Contrast with its own components, where the unit is the FULL range:
#   CBDR:  SD_up(n) = CBDR_high + n * (CBDR_high - CBDR_low),  n in [1,4]
#   Flout: SD_up(n) = EQ        + n * (R / 2),                 n unbounded

actionable(level) := exists PD_array on M15..H1 overlapping level
                     AND array.side == discount if bullish else premium
```

## Machine-Readable

```json
{
  "id": "flout",
  "category": "15-sessions",
  "aliases": ["flout-range", "combined-cbdr-asian-range"],
  "criteria": [
    {"id": "c1", "expr": "window == [CBDR_open .. 00:00 America/New_York]"},
    {"id": "c2", "expr": "range computed on BOTH wicks and bodies"},
    {"id": "c3", "expr": "SD_unit == (flout_high - flout_low) / 2"},
    {"id": "c4", "expr": "SD(n) == equilibrium +/- n * SD_unit"},
    {"id": "c5", "expr": "SD_up(1) == flout_high AND SD_down(1) == flout_low"},
    {"id": "c6", "expr": "n unbounded (unlike CBDR n in [1,4] and asian_range n in [1,2])"},
    {"id": "c7", "expr": "actionable only where level overlaps an M15-H1 discount array (bullish) or premium array (bearish)"}
  ],
  "timeframes": ["M15","M30","H1"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["central-bank-dealers-range", "asian-range", "asian-range-projections", "standard-deviation-projections", "filling-the-numbers", "pd-array-matrix", "ict-day-trading-model"],
  "sources": ["ICT-2017-FILLING-NUMBERS", "ICT-2017-INTRADAY-TOP-DOWN"]
}
```

## Visual Pattern

```
                                     ── SD_up(4)   = EQ + 4*(R/2)
                                     ── SD_up(3)
                                     ── SD_up(2)
   CBDR open ┌─────────────────────┐
             │                     │  ── SD_up(1) = flout_high  ┐
             │   CBDR    │  ASIAN  │                            │
             │           │  RANGE  │  ── EQ  (centre)           │ R
             │                     │                            │
             └─────────────────────┘  ── SD_down(1) = flout_low ┘
                        00:00 NY
                                     ── SD_down(2)  = EQ - 2*(R/2)
                                     ── SD_down(3)
                                     ── SD_down(4)   ...and onward, no cap

   The unit is R/2, so SD_up(1) lands ON the flout high, not one range above it.
   Trade a level only where it overlaps an M15-H1 array on the correct side.
```

## Timeframes

Built from M15–H1 candles inside the overnight window; the projections are read against the following London and New York sessions. Entries are framed on **M15 to H1** arrays — ICT names no other timeframe for the confluence check.

## Examples

**Example 1 — the worked arithmetic (`ICT-2017-INTRADAY-TOP-DOWN`, 13:31–13:42):**
- Flout window highest high to lowest low = **40 pips**.
- "Half of that range is 20 — **20 pips is the standard deviation for flout**."
- From the centre: ±20 = the flout high and low; ±40, ±60, ±80 continue upward and downward as levels 2, 3, 4.

**Example 2 — how a level becomes tradeable (14:05–14:22, 18:41–19:02):**
- Setup: higher-timeframe read is bullish, so only downside flout levels are of interest.
- Filter: a flout deviation that also sits on a **CBDR deviation and an Asian-range deviation** — "when they get really close to a level and it lines up with a PD array, chances are you're probably going to be nailed very close to the high or low of the day" (12:31–12:47).
- Trigger: an M15–H1 **discount array** overlapping that cluster.
- Outcome: the projection lands "many times within 10 pips of the daily high and low"; ICT banks out roughly ten pips early rather than trading for the extreme.

## Common Mistakes

- **Using the full range as the standard deviation.** This is the single error the concept exists to prevent, and ICT states the negative explicitly: "it's **not** the full range high to low" (14:04). Using the full range doubles every level.
- **Projecting from the flout high and low instead of the centre.** SD(1) *is* the flout high or low. Stacking a half-range on top of the high produces SD(2), not SD(1).
- **Capping the deviations at four.** The CBDR is taught with deviations 1–4 and the Asian range with 1–2; the flout is deliberately open-ended — "you keep adding another level of flout" as the day expands (15:22).
- **Trading a bare projection.** ICT calls the deviations "assisting… they are not guaranteeing, they're not panaceas" (19:30–19:37). Without an overlapping M15–H1 array on the correct side there is no setup.
- **Computing only one version of the range.** Both sources ask for the wick range and the body range, precisely because retail feeds differ at the extremes.
- ⚠ **Assuming a single agreed start time.** `ICT-2017-INTRADAY-TOP-DOWN` (13:22) anchors the window to the **CBDR open**, which `ICT-2017-CBDR` fixes at **2 p.m. New York**. `ICT-2017-FILLING-NUMBERS` (12:25) instead states the range "is determined between **3 p.m. New York and midnight in New York**." The two 2017 lectures disagree by one hour and neither reconciles the other; the close (midnight NY) is common to both. This library records both readings rather than picking one.

## Related Concepts

- [central-bank-dealers-range](central-bank-dealers-range.md) — the first half of the window, and the source of the full-range-unit convention the flout departs from.
- [asian-range](../14-asian-range/asian-range.md) — the second half of the window.
- [asian-range-projections](../14-asian-range/asian-range-projections.md), [standard-deviation-projections](../28-fibonacci-levels/standard-deviation-projections.md) — the sibling projection frameworks the flout is blended with.
- [filling-the-numbers](../04-time-cycles/filling-the-numbers.md) — where the flout is used as one of the four reference levels a daily range fills.
- [pd-array-matrix](../05-pd-arrays/pd-array-matrix.md) — the overlap requirement that turns a projection into an entry.
- [ict-day-trading-model](../31-models/ict-day-trading-model.md) — the average-daily-range read the flout is combined with.

## Citations

- `ICT-2017-FILLING-NUMBERS` (11:47) "utilizing the flout — oh, we haven't talked about that yet, have we"; (11:59–12:14) "shorting above the flout's equilibrium or 50% of the range that creates the flout… you count the equilibrium of the flout range to the high of the range of the flout as one standard deviation; the equilibrium of the flout range to the low of its range is counted as one standard deviation"; (12:19–12:29) "the total flout range is projected on the basis of 50% of its complete range, and the range is determined between 3 p.m. New York and midnight in New York"; (12:29–12:44) the wick range and the body range both computed, "because we always have to factor in the potential error by looking at retail data feeds"; (13:13–13:32) one projected flout range down "constitutes level one of four numbers to fill for the day."
- `ICT-2017-INTRADAY-TOP-DOWN` (03:06–03:17) "the deviations on the flout, which is basically the Asian range and central bank dealers range… combined"; (12:48–12:56) "have you been dying for this one — flout… you've probably been expecting some PhD level presentation, but it's not that hard"; (12:56–13:07) "the flout is the central bank dealers range and the Asian range combined… that whole time window, the highest high and the lowest low, in the form of the wick and in the form of the bodies of the candles"; (13:12–13:22) "I look for overlapping in the total range of the central bank dealers range and Asian range that has been divided in half, and this makes one standard deviation"; (13:22–13:42) the window "starts in central bank dealers range opening all the way to Asian range close at midnight New York time", 40-pip range → "20 pips is the standard deviation for flout"; (13:42–13:48) "I go from the centre point, go up one, that's one standard deviation, two, three, four"; (13:57–14:04) "find the highest high and lowest low, divide that range in half, project that up… it's not the full range high to low"; (14:05–14:41) confluence with 60-to-15-minute discount arrays when bullish, premium arrays when bearish; (15:01–15:22) "there isn't a rule-based idea like there is for central bank dealers range or Asian range… flout can be many standard deviations… you keep adding another level of flout"; (18:41–19:02) "you'll get many times within 10 pips of the daily high and low, that's the reason why I want to get out 10 pips before"; (19:30–19:37) "the standard deviations are assisting, they are not guaranteeing."
