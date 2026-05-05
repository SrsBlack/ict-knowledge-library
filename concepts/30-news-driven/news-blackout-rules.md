# News Blackout Rules

**Category:** 30-news-driven
**Aliases:** news blackout, no-trade window, pre-news cutoff
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2024
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** news, blackout, risk

## Definition

News Blackout Rules define **when not to trade** around scheduled high-impact news. ICT teaches a strict pre-and-post-news no-trade window to avoid the wicks, gaps, and unpredictable spikes that occur as the algorithm pre-positions for and reacts to releases. Most prop firms enforce news blackout rules as well — typically 2-5 minutes before and after high-impact red-folder news. ICT's rules are similar but more conservative on certain releases.

## Formal Criteria

Recommended blackout windows:

| News type | Pre-blackout | Post-blackout | Total |
|---|---|---|---|
| FOMC announcement | 30 min before | 60 min after | 90 min |
| FOMC press conf | 5 min before | 60 min after | 65 min |
| NFP (08:30) | 15 min before | 30 min after | 45 min |
| CPI (08:30) | 15 min before | 30 min after | 45 min |
| Other tier-1 | 5 min before | 15 min after | 20 min |

Rules:

1. Don't open new positions during blackout.
2. Don't trail SL tight during blackout.
3. Existing positions: either close before, widen SL to invalidation level, or accept SL risk.
4. Prop-firm constraints often add additional blackout windows (sometimes ±5 min around all red-folder news).

## Formula / Math

```
in_blackout(t, news_event):
    return t in [news_event.time - pre_blackout, news_event.time + post_blackout]

protocol:
    if in_blackout: no_new_entries
    if in_blackout AND open_position: close OR widen SL OR accept risk
```

## Machine-Readable

```json
{
  "id": "news-blackout-rules",
  "category": "30-news-driven",
  "aliases": ["news-blackout", "no-trade-window", "pre-news-cutoff"],
  "criteria": [
    {"id": "c1", "expr": "no new entries during blackout windows"},
    {"id": "c2", "expr": "blackout durations vary by news type"},
    {"id": "c3", "expr": "existing positions: close, widen SL, or accept"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2024",
  "related": ["news-driven-overview","fomc-two-stage-delivery","nfp-protocol","cpi-protocol","risk-per-trade"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   FOMC blackout window example:

   13:30 ──── 14:00 ──── 14:15 ──── 14:30 ──── 15:00 NY
                        ████████████████████████ blackout
                       blackout (30 min before + 60 min after)
                       
   No new entries during shaded zone.
   Open positions: close or widen SL.
```

## Timeframes

All TFs.

## Examples

**Example 1 — pre-FOMC management:**
- Bullish position open at 1.0860, SL 1.0848 (12 pips).
- 13:30 NY: 30-min FOMC blackout begins.
- Options:
  - Close at market (lock in current P&L).
  - Move SL to wider invalidation (e.g. 1.0830) to survive Stage 1 spike.
  - Accept SL risk (size was small enough that the loss is acceptable).

## Common Mistakes

- **Holding tight stops into blackout.** Tight SLs during high-impact news = stop-out by routine pre-news positioning.
- **Pre-news new entries.** Even with HTF conviction, new entries 5-10 min before release usually get wicked.
- **Ignoring prop-firm blackouts.** Prop firms often have additional rules; entries during firm blackout = rule violation, not just bad practice.

## Related Concepts

- [news-driven-overview](news-driven-overview.md), [fomc-two-stage-delivery](fomc-two-stage-delivery.md), [nfp-protocol](nfp-protocol.md), [cpi-protocol](cpi-protocol.md), [risk-per-trade](../32-risk-management/risk-per-trade.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
