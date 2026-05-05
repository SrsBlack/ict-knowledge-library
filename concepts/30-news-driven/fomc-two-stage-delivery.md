# FOMC Two-Stage Delivery

**Category:** 30-news-driven
**Aliases:** FOMC 2-stage, FOMC two-stage model, Sept-2025 FOMC framing
**ICT Confidence:** high
**Year Introduced:** 2025
**Year Refined:** 2025
**Source IDs:** ICT-2025-FOMC-2STAGE
**Tags:** news, fomc, 2025-refinement

## Definition

The **FOMC Two-Stage Delivery Model** is ICT's September 2025 framing of how the algorithm delivers price around FOMC announcements: FOMC produces **two distinct price legs** rather than a single move. **Stage 1** is the immediate post-announcement reaction (14:00–14:15 NY), typically a sharp spike or fake-out. **Stage 2** is the press-conference-driven move (~14:30 onwards), often the **opposite direction** of stage 1 as the algorithm reads conference tone and delivers the actual intended position. Recognizing the two stages separately prevents trading the wrong leg.

## Formal Criteria

The standard FOMC two-stage timeline:

| Stage | Window (NY) | Behavior |
|---|---|---|
| Pre | before 14:00 | quiet positioning, often tight range |
| Stage 1 | 14:00–14:15 | initial spike on announcement; often a fake-out |
| Bridge | 14:15–14:30 | retracement of Stage 1, FVG often forms |
| Stage 2 | 14:30+ | press conference begins; major directional delivery |
| Post | 16:00+ | move resolves into NY close |

The Stage 1 spike often **fakes the wrong direction** — the algorithm pumps stops on the announcement before delivering the actual move during Stage 2. Trade Stage 2, not Stage 1.

## Formula / Math

```
fomc_two_stage_windows_NY = {
    pre:        [13:30, 14:00],
    stage_1:    [14:00, 14:15],
    bridge:     [14:15, 14:30],
    stage_2:    [14:30, 16:00],
}

# Operational rule:
# - skip Stage 1 (don't trade the spike)
# - watch Stage 2 displacement direction
# - enter on FVG retest from Stage 2 displacement, aligned with HTF bias
```

## Machine-Readable

```json
{
  "id": "fomc-two-stage-delivery",
  "category": "30-news-driven",
  "aliases": ["FOMC-2-stage", "FOMC-two-stage-model"],
  "criteria": [
    {"id": "c1", "expr": "stage 1: 14:00-14:15 NY (announcement spike, often fake)"},
    {"id": "c2", "expr": "stage 2: 14:30+ NY (press conference, true delivery)"},
    {"id": "c3", "expr": "trade stage 2 FVG retests, not stage 1 spike"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2025",
  "year_refined": "2025",
  "related": ["news-driven-overview","nfp-protocol","cpi-protocol","news-blackout-rules","htf-bias-framework","macro-time-1450-1510"],
  "sources": ["ICT-2025-FOMC-2STAGE"]
}
```

## Visual Pattern

```
   FOMC two-stage delivery (bullish actual outcome):

   13:30 ──── 14:00 ──── 14:15 ──── 14:30 ──── 16:00 NY
   pre        Stage 1      bridge     Stage 2      post
              ▼                       ▲▲▲
              ▼ fake spike            ▲▲▲ press conf
              ▼ down                  ▲▲▲ delivers up
                                      ▲▲▲ FVG forms
                                          ↓
                              entry on FVG retest in Stage 2
```

## Timeframes

M1 / M5 / M15.

## Examples

**Example 1 — bullish FOMC Stage 2:**
- HTF bias bullish.
- 14:00 NY FOMC announcement: M5 spikes -25 pips down (Stage 1 fake-out).
- 14:15-14:30 NY: M5 retraces; pre-conference quiet.
- 14:30 NY press conf: dovish tone; M5 displaces +35 pips up; bullish FVG at 1.0925-1.0935.
- 14:50 NY (mid-PM macro): M5 retests CE 1.0930. Long entry.
- SL below Stage 1 low + buffer; target HTF DOL.

## Common Mistakes

- **Trading Stage 1.** The spike is the trap; trading it usually gets stopped out by Stage 2 reversal.
- **Treating Stage 1 direction as the day's direction.** Stage 1 is often opposite to the actual delivery.
- **Holding through 16:00.** FOMC days often have a final move 15:00-16:00 followed by chop into close; take profits before close.

## Related Concepts

- [news-driven-overview](news-driven-overview.md), [nfp-protocol](nfp-protocol.md), [cpi-protocol](cpi-protocol.md), [news-blackout-rules](news-blackout-rules.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [macro-time-1450-1510](../04-time-cycles/macro-time-1450-1510.md).

## Citations

- `ICT-2025-FOMC-2STAGE` — September 2025 ICT release.
