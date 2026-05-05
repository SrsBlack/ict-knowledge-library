# CPI Protocol

**Category:** 30-news-driven
**Aliases:** CPI day, inflation-data protocol, PCE protocol (similar)
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2024
**Source IDs:** ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** news, cpi, inflation

## Definition

The **CPI (Consumer Price Index) Protocol** is ICT's handling for the monthly **inflation data release**, typically **08:30 NY** (mid-month). Since 2022, CPI has been one of the most market-moving releases (Fed-pivot context); ICT's protocol is similar to NFP but with **more emphasis on the post-release displacement direction matching HTF bias**, since CPI directly drives Fed-rate expectations. Same general window mechanics — skip the spike, wait for FVG, trade in bias direction with reduced size.

## Formal Criteria

CPI day timeline (similar to NFP):

| Window (NY) | Behavior |
|---|---|
| Before 08:30 | Pre-CPI positioning; tight ranges |
| 08:30 | Release; volatility spike (skip) |
| 08:30–08:40 | Volatility extends; FVG often forms |
| 08:40–09:30 | FVG retest setup window |
| 09:30+ | NY AM continuation if HTF aligned |

Reduced position sizing (50–75% of normal). Same protocol applies to PCE (Personal Consumption Expenditures) inflation data, released later in the month.

## Formula / Math

```
cpi_protocol:
    skip_window: [08:30, 08:40] NY      # slightly longer than NFP
    fvg_retest_window: [08:40, 09:30] NY
    entry_alignment: HTF bias AND post-CPI displacement
    position_size: 50-75% of normal
```

## Machine-Readable

```json
{
  "id": "cpi-protocol",
  "category": "30-news-driven",
  "aliases": ["CPI-day", "inflation-data-protocol", "PCE-protocol"],
  "criteria": [
    {"id": "c1", "expr": "08:30 NY release; skip 10-min window"},
    {"id": "c2", "expr": "post-CPI FVG retest entry"},
    {"id": "c3", "expr": "reduced position size"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2024",
  "related": ["news-driven-overview","nfp-protocol","fomc-two-stage-delivery","news-blackout-rules","htf-bias-framework"],
  "sources": ["ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   CPI day timeline:

   08:25 ──── 08:30 ──── 08:40 ──── 09:30 NY
   pre         spike      wait       FVG retest entry
   tight       (skip)     out        + NY AM continuation
   range                  10 min     window
```

## Timeframes

M1 / M5 / M15.

## Examples

**Example 1 — hot CPI in bearish-bias context:**
- HTF bias bearish (D, W).
- 08:30 NY: hot CPI surprise (above expected); M5 spikes -40 pips down (USD strength on hawkish-Fed expectation).
- 08:35–08:42: M5 prints bearish FVG at 1.0905–1.0912 inside the spike range.
- 09:00: M5 retests CE 1.0908. Short entry (50% normal size).
- SL above pre-CPI high; risk 28 pips.
- Target PDL or -1.5 SD → reasonable 2-3R.

## Common Mistakes

- **Treating CPI like a normal news release.** CPI's market impact has been Fed-driven since 2022; expect larger ranges than older norms.
- **Trading 08:30 candle directly.** Same as NFP — skip the spike.
- **Holding into FOMC weeks.** When CPI falls in an FOMC week, double-news context; reduce size further or skip.

## Related Concepts

- [news-driven-overview](news-driven-overview.md), [nfp-protocol](nfp-protocol.md), [fomc-two-stage-delivery](fomc-two-stage-delivery.md), [news-blackout-rules](news-blackout-rules.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2022-MENTORSHIP-OVERVIEW`.
