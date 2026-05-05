# NY Lunch

**Category:** 15-sessions
**Aliases:** lunch hour, lunch session, NY midday, dead session
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2023
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** sessions, lunch, dead-session, consolidation

## Definition

NY Lunch is the 12:00 → 13:30 NY window during which institutional traders take a break and volume drops sharply. ICT teaches it as a **dead session** — characteristically narrow ranges, mean-reverting moves, and frequent setups that fail. Most ICT setups include a "skip lunch" rule. Price often consolidates and engineers liquidity for the upcoming NY PM delivery (see [ny-pm-session](ny-pm-session.md)).

## Formal Criteria

- Time window: 12:00 → 13:30 NY.
- Volatility: lowest of the trading day (after Asia).
- Behavior: tight ranges, overlapping candles, false breaks, equal highs / equal lows often form along the bounds.
- Lunch range: high and low of the 12:00–13:30 window often become liquidity pools the PM session sweeps.

## Formula / Math

```
lunch_window = [12:00, 13:30] NY

lunch_high = max(high(t)) for t in lunch_window
lunch_low  = min(low(t))  for t in lunch_window
lunch_range = lunch_high - lunch_low
```

## Machine-Readable

```json
{
  "id": "ny-lunch",
  "category": "15-sessions",
  "aliases": ["lunch-hour", "ny-midday", "dead-session"],
  "criteria": [
    {"id": "c1", "expr": "time_in [12:00, 13:30] NY"},
    {"id": "c2", "expr": "low_volatility_consolidation == true"},
    {"id": "c3", "expr": "engineered_liquidity_along_bounds == true"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2023",
  "related": ["ny-am-session","ny-pm-session","range-contraction","liquidity-pool","equal-highs","equal-lows"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   12:00 ──────────────────────── 13:30 NY

   lunch high ─────────────────── ← BSL pool for PM
                /\  /\  /\
               /  \/  \/  \   ← tight, overlapping
              /            \
   lunch low  ───────────────── ← SSL pool for PM
```

## Timeframes

M1 / M5 only — anything higher aggregates over the entire window and loses session detail.

## Examples

**Example 1 — typical lunch contraction → PM expansion:**
- NY AM rallied 60 pips into a HOD at 1.0925.
- 12:00–13:30 lunch: M5 oscillates in a 12-pip range between 1.0918 and 1.0930.
- 13:30 NY PM opens; sweeps 1.0930 BSL on a wick, then displaces down 25 pips.
- → lunch high engineered, swept on PM open, reversal delivered the PM move.

## Common Mistakes

- **Treating lunch trades like AM/PM trades.** Setups inside lunch typically chop and stop. Most ICT day-traders explicitly skip 12:00–13:30.
- **Ignoring lunch range bounds.** The lunch high/low almost always becomes the next sweep target on PM open.
- **Wrong DST handling.** The 12:00 / 13:30 NY anchors shift relative to GMT — always anchor to NY clock.

## Related Concepts

- [ny-am-session](ny-am-session.md) — what precedes lunch.
- [ny-pm-session](ny-pm-session.md) — what follows.
- [range-contraction](../01-market-structure/range-contraction.md) — lunch is a textbook contraction.
- [liquidity-pool](../02-liquidity/liquidity-pool.md) — what lunch range bounds become.
- [equal-highs](../02-liquidity/equal-highs.md) / [equal-lows](../02-liquidity/equal-lows.md) — what often forms.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — lunch as dead session noted.
- `ICT-2022-MENTORSHIP-OVERVIEW` — "skip lunch" discipline taught explicitly.
