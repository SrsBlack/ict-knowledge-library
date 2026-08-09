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
- **Range = high − low within that window.**
- **Size qualification: the ideal range is under 40 pips**, and "preferably the range
  should be no more than 20 to 30 pips in total range high to low" (`ICT-2017-CBDR`,
  04:39). A wide CBDR is not a usable one.
- Standard deviations **1, 2, 3 and 4** are projected by adding and subtracting the
  range height successively above the high and below the low.
- Expected behaviour: on buy days the **low of the day** tends to form between the CBDR
  and a standard deviation below it; the inverse applies on sell days.

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
    {"id": "c5", "expr": "asian_range_starts_at_cbdr_close == true"}
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
                                    ── SD_down(1)   ← buy-day low often here
                                    ── SD_down(2)
                                    ── SD_down(3)

   8pm NY: CBDR closes, Asian range begins.
```

## Timeframes

Built on M15–H1 within the 6-hour window; the projections are then read against the
next session's intraday action.

## Examples

**Example 1 — buy-day framing (`ICT-2017-CBDR`, 03:09–03:23):**
- CBDR forms 2 p.m.–8 p.m. NY with a qualifying range.
- Standard deviations are projected 1–4 above and below.
- The low of the day forms between the CBDR and a standard deviation below it, and the
  day trades up through the upside projections.

## Common Mistakes

- **Using a wide range.** Over 40 pips the range is disqualified, not merely weaker.
- **Using local clock time.** The window is New York time; ICT explicitly tells
  non-US traders to locate the 2 p.m. and 8 p.m. NY candles on their own charts.
- **Confusing CBDR with the Asian range.** They are consecutive windows — the Asian
  range starts when the CBDR closes at 8 p.m. NY.
- **Treating a projection as an entry.** The standard deviations frame where the day's
  extreme may form; they are not a setup.

## Related Concepts

- [asian-range](../14-asian-range/asian-range.md) — the window that begins at CBDR close.
- [standard-deviation-projections](../28-fibonacci-levels/standard-deviation-projections.md) — the same replicate-the-range mechanic applied to a fib leg.
- [ny-am-session](ny-am-session.md) — the session the projections are read against.

## Citations

- `ICT-2017-CBDR` (00:26) — "specifically teaching central bank dealers range"; (01:57–02:27) the range height "can be reproduced or replicated… in the form of a standard deviation, one standard deviation above and below would be the same range added to the high"; (02:57) "standard deviations 1, 2, 3 & 4"; (03:09–03:23) "most buy days will create the low of the day from the central bank dealers range down to the standard deviation"; (04:32) "the time period that frames the central bank dealers range is 2 p.m. to 8 p.m. New York time"; (04:39) "the ideal range is less than 40 pips, preferably the range should be no more than 20 to 30 pips in total range high to low"; (11:27) "at 8 p.m. starting the Asian range."
