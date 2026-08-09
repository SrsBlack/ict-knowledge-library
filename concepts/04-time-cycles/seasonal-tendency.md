# Seasonal Tendency

**Category:** 04-time-cycles
**Aliases:** seasonals, seasonal tendencies, ideal seasonal tendency, annual tendency
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-SEASONAL-IDEAL, ICT-2017-SEASONAL-COMMODITY
**Tags:** time-cycles, seasonality, htf-bias, intermarket, dollar-index

## Definition

A seasonal tendency is a **recurring annual pattern** in an instrument's price — a
window of the calendar year in which that market has historically tended to rally
or decline. ICT teaches them as a higher-time-frame **bias input**, not a signal:
"seasonal tendencies are a tendency, they're not a panacea, they're not a be-all-in-all,
they're not an absolution — they're just **roadmaps of what has happened in the past**
with price action" (`ICT-2017-SEASONAL-IDEAL`). A tendency may fail in any given year
and carries no entry, stop, or target of its own.

An **ideal seasonal tendency** is the narrower, operational form: an FX pair's
seasonal chart compared against the **US Dollar Index** seasonal chart, selecting
the windows where the two are **most diametrically opposed**.

## Formal Criteria

- The tendency is read from a **seasonal chart** — historical average price path across
  the calendar year — not from the live chart.
- For FX, two charts are compared: the pair's own seasonal chart and the **US Dollar
  Index** seasonal chart (`ICT-2017-SEASONAL-IDEAL`).
- An **ideal** window is where the two are *most diametrically opposed* — the pair's
  strongest rally window aligning with the dollar index's decline window, or vice versa.
- The tendency sets **direction and approximate timing only**. It is a bias filter
  layered above a setup; it never supplies the entry.
- Failure in a given year is expected and does not invalidate the tendency: "doesn't
  mean every single year the seasonal tendency may or may not come to fruition… it's a
  general rule of thumb" (`ICT-2017-SEASONAL-IDEAL`).

## Formula / Math

```
seasonal_path(instrument, day_of_year) := historical average price path

ideal_window(pair) := argmax over calendar windows W of
                      opposition( seasonal_path(pair, W),
                                  seasonal_path(USDX, W) )

# Worked example (ICT-2017-SEASONAL-IDEAL, ~01:47-02:12), AUD:
#   AUD futures: strongest tendency to rally in MARCH, top in MAY
#   USDX       : declining across the same March-May window
#   -> diametric opposition -> ideal long-side seasonal window for AUD
```

No threshold is taught for "how opposed" qualifies. Treat window selection as
discretionary, not mechanical.

## Machine-Readable

```json
{
  "id": "seasonal-tendency",
  "category": "04-time-cycles",
  "aliases": ["seasonals", "ideal-seasonal-tendency"],
  "criteria": [
    {"id": "c1", "expr": "read_from_seasonal_chart == true"},
    {"id": "c2", "expr": "fx_ideal_window == max_opposition(pair_seasonal, USDX_seasonal)"},
    {"id": "c3", "expr": "supplies_entry_or_stop == false"},
    {"id": "c4", "expr": "per_year_failure_expected == true"}
  ],
  "timeframes": ["D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["htf-bias-framework", "dollar-index", "open-interest", "quarterly-shift-theory"],
  "sources": ["ICT-2017-SEASONAL-IDEAL", "ICT-2017-SEASONAL-COMMODITY"]
}
```

## Visual Pattern

```
   AUD seasonal chart              USD index seasonal chart
   (historical average path)       (historical average path)

        ╱‾‾╲  top ~May                  ╲
       ╱     ╲                           ╲___  declining
   ___╱ rally ╲                              ╲
      Mar                                Mar     May

   The two paths are diametrically opposed across Mar-May
   -> this is the "ideal" seasonal window for AUD longs.
```

## Timeframes

Daily, weekly and monthly context only. A seasonal window spans weeks to months and
is meaningless intraday.

## Examples

**Example 1 — AUD, March–May (`ICT-2017-SEASONAL-IDEAL`, 01:47–02:12):**
- AUD futures show their strongest seasonal tendency to rally in March and top in May.
- The US Dollar Index shows a decline across the same window.
- The opposition makes this an *ideal* seasonal window rather than merely a seasonal one.

## Common Mistakes

- **Trading the seasonal as a signal.** It supplies no entry, stop, or target. ICT is
  explicit that placing "all of your faith on seasonal tendencies" loses money
  (`ICT-2017-SEASONAL-COMMODITY`, 01:14).
- **Expecting it every year.** A tendency is a base rate over history, not a schedule.
- **Using the pair's seasonal chart alone in FX.** The *ideal* form is defined by
  opposition against the dollar index; a single chart is the weaker read.
- **Confusing it with quarterly theory.** Seasonals are annual and empirical;
  [quarterly theory](../22-quarterly-theory/quarterly-theory-overview.md) is a
  structural cycle model. Different objects.

## Related Concepts

- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md) — where a seasonal read belongs in the stack.
- [dollar-index](../03-order-flow/dollar-index.md) — the comparison instrument for the ideal form.
- [open-interest](../03-order-flow/open-interest.md) — the other non-price context input taught in the same mentorship year.
- [quarterly-theory-overview](../22-quarterly-theory/quarterly-theory-overview.md) — a different cycle concept, not a synonym.

## Citations

- `ICT-2017-SEASONAL-IDEAL` (00:37) — "seasonal tendencies are a tendency, they're not a panacea… they're just roadmaps of what has happened in the past with price action"; (01:10–01:26) "we're comparing the two seasonal tendency charts, we're looking for the most diametrically opposed price action between the two… an ideal seasonal tendency is when the underlying market is predisposed to go in a direction that seasonal tendency is being outlined"; (01:47–02:12) the AUD vs dollar-index March–May worked example.
- `ICT-2017-SEASONAL-COMMODITY` (00:56–01:19) — "guarantees don't exist in trading and certainly seasonal tendencies are not one… you can lose money if you try to place all of your faith on seasonal tendencies… it's like a road map."
