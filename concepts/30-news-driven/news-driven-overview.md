# News-Driven — Overview

**Category:** 30-news-driven
**Aliases:** news trading, high-impact news, event-driven setups
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2025
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2025-FOMC-2STAGE
**Tags:** news, foundational

## Definition

News-driven trading is the discipline of operating around **scheduled high-impact economic releases** — FOMC, NFP, CPI, central bank rate decisions. ICT teaches news as **algorithmic delivery accelerators**, not exogenous shocks: the institutional algorithm uses news releases to inject volatility that completes pre-positioned setups. ICT's rule of thumb: do not fade news; trade in the direction of HTF bias when the news catalyst aligns. Specific protocols apply per news type.

## Formal Criteria

ICT teaches three news-handling postures:

1. **Avoid the candle:** for high-impact unscheduled news (geopolitical shocks, surprise rate decisions), step aside.
2. **Trade after the move:** for scheduled releases (08:30 NY data, 14:00 NY FOMC), wait for the post-news displacement to complete, then trade the FVG retest in the resulting bias direction.
3. **Pre-position with HTF bias:** when a news release is expected to confirm HTF bias (e.g. dovish Fed in bullish-bias environment), HTF setups can be entered hours before with awareness of the news catalyst.

The 2025 refinement formalized **two-stage FOMC delivery** — see [fomc-two-stage-delivery](fomc-two-stage-delivery.md).

## Formula / Math

```
news_response_window_minutes = {
    NFP/CPI/retail_sales/PPI: 5-30 min after 08:30 NY release,
    FOMC_announcement: 5-15 min after 14:00 NY release,
    FOMC_press_conf: 30-60 min after 14:30 NY conference start,
}

ict_news_protocol(release_time):
    skip_window = [release_time, release_time + 5_min]   # don't trade in the spike
    setup_window = [release_time + 5_min, release_time + 30_min]   # FVG retest setups
```

## Machine-Readable

```json
{
  "id": "news-driven-overview",
  "category": "30-news-driven",
  "aliases": ["news-trading", "high-impact-news", "event-driven-setups"],
  "criteria": [
    {"id": "c1", "expr": "trade_after_news_displacement_in_HTF_bias_direction"},
    {"id": "c2", "expr": "skip_window during news spike"},
    {"id": "c3", "expr": "specific protocols per news type"}
  ],
  "timeframes": ["M1","M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2025",
  "related": ["fomc-two-stage-delivery","nfp-protocol","cpi-protocol","news-blackout-rules","htf-bias-framework"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2025-FOMC-2STAGE"]
}
```

## Visual Pattern

```
   typical 08:30 NY news handling:

   08:25 ── 08:30 ── 08:35 ── 08:50 ── 09:00 NY
   pre-news  spike     wait       FVG       continuation
   (avoid    skip      out 5 min  retest    (HTF-aligned)
   tight     window    for FVG    entry
   stops)              to form    zone
```

## Timeframes

M1 / M5 / M15 / H1.

## Examples

**Example 1 — bullish-aligned NFP setup:**
- HTF (D, W) bullish.
- 08:30 NY NFP releases positive.
- 08:30–08:35: wide bullish displacement candle on M5; spike avoided.
- 08:40: bullish FVG forms at 1.0925–1.0935.
- 09:00: M5 retests CE 1.0930. Long entry.
- SL below pre-news low; target HTF DOL.

## Common Mistakes

- **Trading the spike candle.** Pre-news positioning OR fading the spike usually loses; the post-news FVG-retest is the standard ICT entry.
- **Ignoring HTF bias.** News-direction does not always match HTF bias; conflicting catalysts produce whipsaw — skip those.
- **Holding through pre-news.** Tight stops within 30 min of release usually get wicked by pre-news positioning; either widen stops or exit before.

## Related Concepts

- [fomc-two-stage-delivery](fomc-two-stage-delivery.md), [nfp-protocol](nfp-protocol.md), [cpi-protocol](cpi-protocol.md), [news-blackout-rules](news-blackout-rules.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`, `ICT-2025-FOMC-2STAGE`.
