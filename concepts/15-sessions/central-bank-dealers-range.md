# Central Bank Dealers Range (CBDR)

**Category:** 15-sessions
**Aliases:** CBDR, dealers range, central bank dealer range
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-CBDR
**Tags:** sessions, range, standard-deviations, day-trading, projections

## Definition

The Central Bank Dealers Range is the high-to-low range price makes between
**2:00 p.m. and 8:00 p.m. New York time**, used as the anchor for standard-deviation
projections that frame the following trading day's high and low. It is a component of
ICT's day-trading model: once the range is fixed, its height is replicated above and
below to produce projection levels, and the next session's extreme is expected to form
at one of them.

The CBDR ends where the [asian-range](../14-asian-range/asian-range.md) begins — "at
8 p.m., starting the Asian range" (`ICT-2017-CBDR`, 11:27) — so the two are
consecutive, not overlapping.

## Formal Criteria

- **Window: 2:00 p.m. → 8:00 p.m. New York time.** Traders outside that timezone must
  identify the candles corresponding to 2 p.m. and 8 p.m. NY on their own chart and
  mark them, rather than using local clock times (`ICT-2017-CBDR`, 04:51–05:30).
- **Range = high − low within that window**, calibrated from either the wicks or the
  bodies. ICT gives both calibrations but **prefers bodies**: "we can use the range in
  pips by calibration from high to low or using the wicks or alternatively we can use
  the range in the highest body and the lowest body" (`ICT-2017-CBDR`, 06:03–06:11);
  "I like to use the bodies predominantly because the wicks are always going to show
  erroneous price because of your dealing spread" (09:03–09:14) — though "we still have
  to look at the ranges with the wicks included" (10:36) when sizing the move.
- **Size qualification: the ideal range is under 40 pips**, and "preferably the range
  should be no more than 20 to 30 pips in total range high to low" (`ICT-2017-CBDR`,
  04:39); "larger than 30 pips can tend to be unfruitful for projections" (05:53). A wide
  CBDR is not a usable one.
- Standard deviations **1, 2, 3 and 4** are projected by adding and subtracting the
  range height successively above the high and below the low.
- Expected behaviour: **most buy days form the low of the day somewhere in the band
  from the CBDR out to the third standard deviation below it** — "most buy days will
  create the low of the day from the central bank dealers range down to the **third**
  standard deviation" (03:18–03:23). Within that band, the **ideal** depth is shallower,
  capped at the second deviation, often only the first: "ideal buy days will create the
  low the day no less than two standard deviations below … many times you'll see it
  just go one standard deviation below" (03:40–03:52). ⚠ **"No less than" is the same
  rule misspoken** — the literal wording is quoted above because it is what ICT says,
  but the sell-day mirror fixes the intended sense: "ideally sell days create the high
  the day no more than two standard deviations above central bank dealers range, many
  times just one standard deviation" (03:28–03:35). Read together: **ideal depth is no
  MORE than SD2, often just SD1** — not a minimum of SD2. "Four standard deviations
  above for a high the day is going to be on the heels of a very high impact news event"
  (03:55–04:04). The buy/sell description is symmetric.

## Formula / Math

```
CBDR_high := max(high) over 14:00-20:00 New York
CBDR_low  := min(low)  over 14:00-20:00 New York
R         := CBDR_high - CBDR_low            # qualify: R < 40 pips, ideally 20-30

SD_up(n)   := CBDR_high + n * R              # n = 1, 2, 3, 4
SD_down(n) := CBDR_low  - n * R

# The projections replicate the range, they do not scale it:
#   SD_up(1) = CBDR_high + R
#   SD_up(2) = SD_up(1)  + R

# Most buy days: low somewhere between CBDR_low and SD_down(3).
# Ideal buy-day low: no DEEPER than SD_down(2), many times only SD_down(1).
# (ICT's literal "no less than two standard deviations below" is a misspeech,
#  fixed by the sell-day mirror: "no more than two ... many times just one.")
# SD(4) only on the heels of a very high impact news event.
```

## Machine-Readable

```json
{
  "id": "central-bank-dealers-range",
  "category": "15-sessions",
  "aliases": ["CBDR", "dealers-range"],
  "criteria": [
    {"id": "c1", "expr": "window == 14:00-20:00 America/New_York"},
    {"id": "c2", "expr": "range_pips < 40", "strength": "qualification"},
    {"id": "c3", "expr": "ideal_range_pips in [20, 30]", "strength": "preference"},
    {"id": "c4", "expr": "SD(n) == CBDR_edge +/- n * range, n in [1,2,3,4]"},
    {"id": "c5", "expr": "asian_range_starts_at_cbdr_close == true"},
    {"id": "c6", "expr": "range_calibration prefers bodies over wicks (wicks show dealing-spread error)"},
    {"id": "c7", "expr": "most_buy_days: low in band [CBDR_low, SD_down(3)]; ideal depth NOT DEEPER than SD_down(2), many times only SD_down(1); SD(4) only on high-impact news"}
  ],
  "timeframes": ["M15","M30","H1"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["asian-range", "standard-deviation-projections", "ny-am-session", "london-open-killzone"],
  "sources": ["ICT-2017-CBDR"]
}
```

## Visual Pattern

```
                                    ── SD_up(3)
                                    ── SD_up(2)
                                    ── SD_up(1)
        2pm NY ┌───────────┐ 8pm NY
               │   CBDR    │  R = high - low, ideally 20-30 pips
               └───────────┘
                                    ── SD_down(1)   ← many times ideal buy-day low stops here
                                    ── SD_down(2)   ← ideal buy-day low goes no DEEPER than this
                                    ── SD_down(3)   ← most buy days: low somewhere in this band

   8pm NY: CBDR closes, Asian range begins.
```

## Timeframes

Built on M15–H1 within the 6-hour window; the projections are then read against the
next session's intraday action.

## Examples

**Example 1 — buy-day framing (`ICT-2017-CBDR`, 03:09–03:23):**
- CBDR forms 2 p.m.–8 p.m. NY with a qualifying range.
- Standard deviations are projected 1–4 above and below.
- The low of the day forms somewhere between the CBDR and its **third** standard
  deviation below (most buy days); the **ideal** depth is no deeper than the second,
  often just the first — and the day trades up through the upside projections.

## Common Mistakes

- **Using a wide range.** Over 40 pips the range is disqualified, not merely weaker.
- **Using local clock time.** The window is New York time; ICT explicitly tells
  non-US traders to locate the 2 p.m. and 8 p.m. NY candles on their own charts.
- **Confusing CBDR with the Asian range.** They are consecutive windows — the Asian
  range starts when the CBDR closes at 8 p.m. NY.
- **Treating a projection as an entry.** The standard deviations frame where the day's
  extreme may form; they are not a setup.
- **Treating the ideal buy-day depth (no deeper than SD2) as the typical extent of the move.** Most buy days range across the whole band from the CBDR to SD_down(3); the no-deeper-than-SD2 figure is the *ideal*, not a ceiling on where price actually goes.
- **Reading "no less than two standard deviations below" literally as a minimum depth.** Taken alone it would mean the ideal low never stops above SD2 — the opposite of what ICT teaches. The sell-day mirror ("no more than two … many times just one") shows it is the same rule misspoken; the ideal is a cap at SD2, not a floor.
- **Using wicks as the default calibration.** ICT states a preference for **bodies**
  ("the wicks are always going to show erroneous price because of your dealing
  spread"), while still checking the wick-included range when sizing the move.

## Related Concepts

- [asian-range](../14-asian-range/asian-range.md) — the window that begins at CBDR close.
- [standard-deviation-projections](../28-fibonacci-levels/standard-deviation-projections.md) — the same replicate-the-range mechanic applied to a fib leg.
- [ny-am-session](ny-am-session.md) — the session the projections are read against.

## Citations

- `ICT-2017-CBDR` (00:26) — "specifically teaching central bank dealers range"; (01:57–02:27) the range height "can be reproduced or replicated… in the form of a standard deviation, one standard deviation above and below would be the same range added to the high"; (02:57) "standard deviations 1, 2, 3 & 4"; (03:18–03:23) "most buy days will create the low of the day from the central bank dealers range down to the **third** standard deviation"; (03:28–03:35) sell-day mirror, "ideally sell days create the high the day no more than two standard deviations above central bank dealers range, many times just one standard deviation" — fixes the sense of the buy-day line below; (03:40–03:52) "ideal buy days will create the low the day no less than two standard deviations below … many times you'll see it just go one standard deviation below" (a misspeech for "no more than," per the mirror); (03:55–04:04) "four standard deviations above for a high the day is going to be on the heels of a very high impact news event"; (04:32) "the time period that frames the central bank dealers range is 2 p.m. to 8 p.m. New York time"; (04:39) "the ideal range is less than 40 pips, preferably the range should be no more than 20 to 30 pips in total range high to low"; (05:53) "larger than 30 pips can tend to be unfruitful for projections"; (06:03–06:11) "we can use the range in pips by calibration from high to low or using the wicks or alternatively we can use the range in the highest body and the lowest body"; (09:03–09:14) "I like to use the bodies predominantly because the wicks are always going to show erroneous price because of your dealing spread"; (10:36) "we still have to look at the ranges with the wicks included"; (11:27) "at 8 p.m. starting the Asian range."
