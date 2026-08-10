# IPDA 20-Day Lookback

**Category:** 23-ipda
**Aliases:** 20-day window, IPDA short-horizon, monthly IPDA
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-IPDA-DATA-RANGES, ICT-2017-QUARTERLY-SHIFTS, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2017-STT-BLENDING-IPDA-PD
**Tags:** ipda, lookback, 20-day

## Definition

The IPDA 20-day lookback is the **shortest of ICT's three canonical IPDA reference windows**, covering approximately the most recent **month of trading**. The 20-day high and low define the most-recent significant liquidity pool that the algorithm references for delivery decisions. ICT teaches the 20-day window as the **intraday-relevant** horizon: 20-day high BSL is a typical short-horizon DOL target; 20-day low SSL is a short-horizon SSL target.

## Formal Criteria

- Window: trailing 20 trading days (excludes weekends).
- 20-day high = max(high) over window (uses wick highs).
- 20-day low = min(low) over window.
- Active until swept; once swept, the next-most-recent unswept extreme becomes the new 20-day reference.

## Formula / Math

```
ipda_20_high = max(high(t)) for t in last 20 trading days
ipda_20_low  = min(low(t))  for t in last 20 trading days

# Active = not yet swept since formation
active_20_high := no future bar's high has exceeded ipda_20_high
active_20_low  := no future bar's low has fallen below ipda_20_low
```

## Machine-Readable

```json
{
  "id": "ipda-20-day-lookback",
  "category": "23-ipda",
  "aliases": ["20-day-window", "IPDA-short-horizon"],
  "criteria": [
    {"id": "c1", "expr": "trailing 20 trading days"},
    {"id": "c2", "expr": "high = max(high), low = min(low)"},
    {"id": "c3", "expr": "active until swept"}
  ],
  "timeframes": ["D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ipda-definition","ipda-data-ranges","ipda-40-day-lookback","ipda-60-day-lookback","ipda-reference-points","draw-on-liquidity","external-range-liquidity"],
  "sources": ["ICT-2017-IPDA-DATA-RANGES","ICT-2017-QUARTERLY-SHIFTS","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2017-STT-BLENDING-IPDA-PD"]
}
```

## Visual Pattern

```
   IPDA 20-day on a daily chart:
   
   ─── 20-day high ────  (~1 month back; active BSL DOL if untaken)
                /\  /\
               /  \/  \
   ────────── current price ──────
              /  /\  /
           /\/   /\
   ─── 20-day low ────  (~1 month back; active SSL DOL if untaken)
```

## Timeframes

D / W (the lookback unit is days).

## Examples

**Example 1 — 20-day reference for intraday setup:**
- Today: 2026-05-05.
- Past 20 trading days: 2026-04-07 to 2026-05-04.
- 20-day high = 1.0985 (printed 2026-04-22, untaken since).
- 20-day low = 1.0790 (printed 2026-04-15, untaken).
- Today's intraday DOL: bullish bias targets 1.0985 first (20-day BSL), then 40-day high above.

## Common Mistakes

- **Using calendar days.** 20 trading days ≈ 28 calendar days; using 20 calendar days gives a different (smaller) window.
- **Counting swept extremes.** Once the 20-day high is swept, that level no longer functions as the active reference; find the next-most-recent unswept high.

## Related Concepts

- [ipda-definition](ipda-definition.md), [ipda-data-ranges](ipda-data-ranges.md), [ipda-40-day-lookback](ipda-40-day-lookback.md), [ipda-60-day-lookback](ipda-60-day-lookback.md), [ipda-reference-points](ipda-reference-points.md), [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md), [external-range-liquidity](../02-liquidity/external-range-liquidity.md).

## Citations

- `ICT-2017-STT-BLENDING-IPDA-PD` (04:52–05:06) — **the month-equivalence stated verbatim**, previously asserted in this page's prose without a quote: "we break it into 20 trading days, which is essentially one month, 40 trading days, which is essentially two months, and 60 trading days, which is essentially three trading months" — here, **20 trading days, which is essentially one month**. ⚠ Pair [00:56] ("casting forward for a new set of 20, 40, and 60. Each new day, you shift that range forward") with [00:46] ("provides you a context to **look back**") if either is ever quoted: it is a **rolling lookback advancing one day at a time**, not a forward projection re-anchored daily.

- `ICT-2017-IPDA-DATA-RANGES` (81:03) — "It's January 12, 2017"; (27:52–28:27) "if you look back 60 days in the past, what was the highest high in the last 60 days? There's going to be buy stops above that high… Inside of the range of 20 days, 40 days, and 60 days."
- `ICT-2017-QUARTERLY-SHIFTS` (00:21) — "the January 2017 ICT Mentorship Long Term Analysis Lesson 1.1"; (22:22–23:41) "60 trading days, 40 trading days, and 20 trading days… and they're all trading days, not calendar days."
- `ICT-2022-MENTORSHIP-OVERVIEW` — the windows re-taught in the 2022 season.
