# NFP Protocol

**Category:** 30-news-driven
**Aliases:** NFP day, Non-Farm Payrolls protocol, jobs-day handling
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** news, nfp, foundational

## Definition

The **NFP (Non-Farm Payrolls) Protocol** is ICT's handling for the monthly **first-Friday-of-the-month US jobs report**, released **08:30 NY**. NFP is one of the most-volatile FX events; ICT teaches a specific protocol: skip the spike, wait for the post-NFP FVG to form, trade in HTF-bias direction. NFP days frequently produce the week's HOD/LOD — execution discipline matters more than usual.

## Formal Criteria

NFP day timeline:

| Window (NY) | Behavior |
|---|---|
| Before 08:30 | Pre-NFP positioning; tight ranges |
| 08:30 | Release; volatility spike (skip) |
| 08:30–08:35 | Continued volatility; usually FVG forms |
| 08:35–09:00 | FVG retest setup window |
| 09:00–11:00 | NY AM SB-style continuation if HTF aligned |

Position sizing reduced versus normal days (NFP unpredictability adds tail risk).

## Formula / Math

```
nfp_protocol:
    skip_window: [08:30, 08:35] NY
    fvg_retest_window: [08:35, 09:30] NY
    entry_direction: aligned with HTF bias AND post-NFP displacement
    position_size: 50-75% of normal (reduced for volatility)
```

## Machine-Readable

```json
{
  "id": "nfp-protocol",
  "category": "30-news-driven",
  "aliases": ["NFP-day", "Non-Farm-Payrolls-protocol", "jobs-day"],
  "criteria": [
    {"id": "c1", "expr": "08:30 NY release; skip 5-min window"},
    {"id": "c2", "expr": "post-NFP FVG retest entry"},
    {"id": "c3", "expr": "reduced position size (50-75% of normal)"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["news-driven-overview","cpi-protocol","fomc-two-stage-delivery","news-blackout-rules","htf-bias-framework","macro-time-0950-1010"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   NFP day timeline:

   08:25 ──── 08:30 ──── 08:35 ──── 09:00 ──── 11:00 NY
   pre         spike      wait       FVG        SB-style
   tight       (skip)     out        retest     continuation
   range                  for FVG    entry      window
```

## Timeframes

M1 / M5 / M15.

## Examples

**Example 1 — bullish-aligned NFP:**
- HTF bullish.
- 08:30 NY: positive NFP (jobs above estimate); M5 spikes +30 pips up.
- 08:35–08:40: M5 prints bullish FVG at 1.0925–1.0935 inside the spike candle's range.
- 09:00: M5 retests CE 1.0930. Long entry (50% normal size for NFP-day).
- SL below pre-NFP low at 1.0905; risk 25 pips.
- Target NY AM SB extension; +60 pips → 2.4R.

## Common Mistakes

- **Pre-NFP positioning.** Tight stops 5-15 min before release usually wick out on pre-news positioning.
- **Trading the spike.** 08:30 candle is typically too volatile for a clean entry; wait 5 min minimum.
- **Full position size.** NFP volatility produces 2-3× normal stop excursions; halve size.
- **Counter-bias NFP trades.** When NFP direction conflicts with HTF bias, expect chop; skip.

## Related Concepts

- [news-driven-overview](news-driven-overview.md), [cpi-protocol](cpi-protocol.md), [fomc-two-stage-delivery](fomc-two-stage-delivery.md), [news-blackout-rules](news-blackout-rules.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [macro-time-0950-1010](../04-time-cycles/macro-time-0950-1010.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
