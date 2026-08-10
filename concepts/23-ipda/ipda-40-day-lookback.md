# IPDA 40-Day Lookback

**Category:** 23-ipda
**Aliases:** 40-day window, IPDA mid-horizon, ~2-month window
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-IPDA-DATA-RANGES, ICT-2017-QUARTERLY-SHIFTS, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2017-STT-BLENDING-IPDA-PD
**Tags:** ipda, lookback, 40-day

## Definition

The IPDA 40-day lookback is the **mid-horizon** IPDA reference window, covering approximately **2 months of trading**. The 40-day high and low are swing-trade-relevant liquidity references — common targets after the 20-day extreme has been taken. Together with [ipda-20-day-lookback](ipda-20-day-lookback.md) and [ipda-60-day-lookback](ipda-60-day-lookback.md), the 40-day window forms the mid-tier of ICT's three-window IPDA framework.

## Formal Criteria

- Window: trailing 40 trading days.
- 40-day high = max(high), 40-day low = min(low).
- Often coincides with: PMH/PML, monthly Q-extremes.

## Formula / Math

```
ipda_40_high = max(high) over last 40 trading days
ipda_40_low  = min(low)  over last 40 trading days
```

## Machine-Readable

```json
{
  "id": "ipda-40-day-lookback",
  "category": "23-ipda",
  "aliases": ["40-day-window", "IPDA-mid-horizon"],
  "criteria": [
    {"id": "c1", "expr": "trailing 40 trading days"},
    {"id": "c2", "expr": "swing-trade horizon"}
  ],
  "timeframes": ["D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["ipda-definition","ipda-data-ranges","ipda-20-day-lookback","ipda-60-day-lookback","ipda-reference-points","draw-on-liquidity"],
  "sources": ["ICT-2017-IPDA-DATA-RANGES","ICT-2017-QUARTERLY-SHIFTS","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2017-STT-BLENDING-IPDA-PD"]
}
```

## Visual Pattern

```
   IPDA stack (20/40/60 day):
   
   ─── 60-day high ─────  longest-horizon BSL
   ─── 40-day high ────   mid-horizon BSL
   ─── 20-day high ──     short-horizon BSL
       ↑
       current price
       ↓
   ─── 20-day low ──
   ─── 40-day low ────
   ─── 60-day low ─────
```

## Timeframes

D / W.

## Examples

**Example 1 — 40-day after 20-day taken:**
- 20-day BSL at 1.0985 swept yesterday.
- 40-day high at 1.1050 still untaken.
- → next algorithmic DOL upside is 40-day high.

## Common Mistakes

- **Skipping the 40-day reference.** Many traders track only PWH/PMH; 40-day adds a precise mid-horizon level.
- **Calendar-day calculation.** 40 trading days ≈ 56 calendar days.

## Related Concepts

- [ipda-definition](ipda-definition.md), [ipda-data-ranges](ipda-data-ranges.md), [ipda-20-day-lookback](ipda-20-day-lookback.md), [ipda-60-day-lookback](ipda-60-day-lookback.md), [ipda-reference-points](ipda-reference-points.md), [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md).

## Citations

- `ICT-2017-STT-BLENDING-IPDA-PD` (04:52–05:06) — **the month-equivalence stated verbatim**, previously asserted in this page's prose without a quote: "we break it into 20 trading days, which is essentially one month, 40 trading days, which is essentially two months, and 60 trading days, which is essentially three trading months" — here, **40 trading days, which is essentially two months**. ⚠ Pair [00:56] ("casting forward for a new set of 20, 40, and 60. Each new day, you shift that range forward") with [00:46] ("provides you a context to **look back**") if either is ever quoted: it is a **rolling lookback advancing one day at a time**, not a forward projection re-anchored daily.

- `ICT-2017-IPDA-DATA-RANGES` (81:03) — "It's January 12, 2017"; (27:52–28:27) "if you look back 60 days in the past, what was the highest high in the last 60 days? There's going to be buy stops above that high… Inside of the range of 20 days, 40 days, and 60 days."
- `ICT-2017-QUARTERLY-SHIFTS` (00:21) — "the January 2017 ICT Mentorship Long Term Analysis Lesson 1.1"; (22:22–23:41) "60 trading days, 40 trading days, and 20 trading days… and they're all trading days, not calendar days."
- `ICT-2022-MENTORSHIP-OVERVIEW` — the windows re-taught in the 2022 season.
