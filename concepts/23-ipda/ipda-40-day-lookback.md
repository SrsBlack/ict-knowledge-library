# IPDA 40-Day Lookback

**Category:** 23-ipda
**Aliases:** 40-day window, IPDA mid-horizon, ~2-month window
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2018-IPDA, ICT-2022-MENTORSHIP-OVERVIEW
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
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["ipda-definition","ipda-data-ranges","ipda-20-day-lookback","ipda-60-day-lookback","ipda-reference-points","draw-on-liquidity"],
  "sources": ["ICT-2018-IPDA","ICT-2022-MENTORSHIP-OVERVIEW"]
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

- `ICT-2018-IPDA`, `ICT-2022-MENTORSHIP-OVERVIEW`.
