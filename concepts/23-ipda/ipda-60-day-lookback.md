# IPDA 60-Day Lookback

**Category:** 23-ipda
**Aliases:** 60-day window, IPDA quarterly, long-horizon IPDA
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2025
**Source IDs:** ICT-2018-IPDA, ICT-2025-ADV-LIQUIDITY
**Tags:** ipda, lookback, 60-day, quarterly

## Definition

The IPDA 60-day lookback is the **longest-horizon** IPDA reference window, covering approximately **3 months / one calendar quarter** of trading. The 60-day high and low are major HTF liquidity references and align with the **quarterly IPDA rotation** ICT formalized in 2025 ([quarterly-shift-2025](../22-quarterly-theory/quarterly-shift-2025.md)). Often function as ERL targets when 20-day and 40-day extremes have already been taken.

## Formal Criteria

- Window: trailing 60 trading days (~ 12 weeks).
- 60-day high / low define the longest-horizon active liquidity references.
- Often coincide with: prior calendar-quarter extremes, monthly LTH/LTL pairings.

## Formula / Math

```
ipda_60_high = max(high) over last 60 trading days
ipda_60_low  = min(low)  over last 60 trading days

# Approximately one calendar quarter
60_trading_days ≈ 12 weeks ≈ 84 calendar days
```

## Machine-Readable

```json
{
  "id": "ipda-60-day-lookback",
  "category": "23-ipda",
  "aliases": ["60-day-window", "IPDA-quarterly", "long-horizon-IPDA"],
  "criteria": [
    {"id": "c1", "expr": "trailing 60 trading days (~12 weeks)"},
    {"id": "c2", "expr": "longest IPDA reference horizon"},
    {"id": "c3", "expr": "aligns with quarterly IPDA rotation"}
  ],
  "timeframes": ["W","MN"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2025",
  "related": ["ipda-definition","ipda-data-ranges","ipda-20-day-lookback","ipda-40-day-lookback","ipda-reference-points","quarterly-shift-2025","external-range-liquidity"],
  "sources": ["ICT-2018-IPDA","ICT-2025-ADV-LIQUIDITY"]
}
```

## Visual Pattern

```
   IPDA 60-day on weekly chart:
   
   ─── 60-day high ────  ~12 weeks ago, untaken (ERL target)
                ▲▲
               ▲▲▲▲
              /\    \
             /  \    \
            /    \    \  ← weekly chart over ~3 months
   ─── current price ──
            \
             \
   ─── 60-day low ─────  ~12 weeks ago (SSL ERL)
```

## Timeframes

W / MN.

## Examples

**Example 1 — 60-day as terminal DOL:**
- 20-day BSL at 1.0985 taken last week.
- 40-day BSL at 1.1050 taken yesterday.
- 60-day BSL at 1.1180 still untaken → next algorithmic DOL upside.
- Until 60-day is taken, weekly bullish-bias setups continue targeting up.

## Common Mistakes

- **Treating 60-day as "always relevant."** When IPDA is in IRL-targeting mode (per quarterly-shift-2025), 60-day extremes may be ignored for weeks while internal PD arrays get filled.
- **Confusing 60-day with calendar quarter.** 60 trading days ≈ 12 weeks; calendar quarter = 13 weeks. Close but not identical.

## Related Concepts

- [ipda-definition](ipda-definition.md), [ipda-data-ranges](ipda-data-ranges.md), [ipda-20-day-lookback](ipda-20-day-lookback.md), [ipda-40-day-lookback](ipda-40-day-lookback.md), [ipda-reference-points](ipda-reference-points.md), [quarterly-shift-2025](../22-quarterly-theory/quarterly-shift-2025.md), [external-range-liquidity](../02-liquidity/external-range-liquidity.md).

## Citations

- `ICT-2018-IPDA`, `ICT-2025-ADV-LIQUIDITY`.
