# NY Lunch

**Category:** 15-sessions
**Aliases:** lunch hour, lunch session, NY midday, dead session
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2023
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2017-INDEX-PM-TREND, ICT-2017-BOND-SPLIT-SESSION
**Tags:** sessions, lunch, dead-session, consolidation

## Definition

NY Lunch is the 12:00 → 13:30 NY window during which institutional traders take a break and volume drops sharply. ICT teaches it as a **dead session** — characteristically narrow ranges, mean-reverting moves, and frequent setups that fail. Most ICT setups include a "skip lunch" rule. Price often consolidates and engineers liquidity for the upcoming NY PM delivery (see [ny-pm-session](ny-pm-session.md)).

## Formal Criteria

- Time window: 12:00 → 13:30 NY.
- Volatility: lowest of the trading day (after Asia).
- Behavior: tight ranges, overlapping candles, false breaks, equal highs / equal lows often form along the bounds.
- Lunch range: high and low of the 12:00–13:30 window often become liquidity pools the PM session sweeps.

**The window is elastic, and asset-class specific** (added 2026-08-10 from the June-2017 primaries)

- **Index futures.** Nominally **12:00 → 13:00**, but "it can actually be **as early as 11 a.m. to
  as late as 2 p.m.**" (`ICT-2017-INDEX-PM-TREND`, 02:41). The driver is the morning's pace: "if
  there's a **fast market in the morning**, traders are going to want to probably work through
  lunch, so **short lunch periods**… when the session in the morning was rather **lethargic**, the
  full lunch hour… **11 o'clock to 1 o'clock or even 2 o'clock** can be seen" (02:50–03:24).
- **Treasury bonds.** "New York lunch, around **11 o'clock to 1 o'clock** in the afternoon"
  (`ICT-2017-BOND-SPLIT-SESSION`, 07:54) — the bond AM session can therefore terminate at 11:00
  rather than noon.
- The 12:00–13:30 window above remains the FX-side definition. These are variants, not
  corrections.

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
    {"id": "c3", "expr": "engineered_liquidity_along_bounds == true"},
    {"id": "c4", "expr": "index futures: nominal [12:00,13:00] NY, elastic [11:00,14:00]; short on fast mornings, long on lethargic ones"},
    {"id": "c5", "expr": "treasury bonds: lunch == [11:00,13:00] NY"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2023",
  "related": ["ny-am-session","ny-pm-session","range-contraction","liquidity-pool","equal-highs","equal-lows","index-am-pm-trend","bond-split-session-rules"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2017-INDEX-PM-TREND","ICT-2017-BOND-SPLIT-SESSION"]
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
- **Treating the window as fixed across assets.** Bonds use 11:00–13:00; index futures nominally
  12:00–13:00 and elastically 11:00–14:00, set by how fast the morning traded.

## Related Concepts

- [ny-am-session](ny-am-session.md) — what precedes lunch.
- [ny-pm-session](ny-pm-session.md) — what follows.
- [range-contraction](../01-market-structure/range-contraction.md) — lunch is a textbook contraction.
- [liquidity-pool](../02-liquidity/liquidity-pool.md) — what lunch range bounds become.
- [equal-highs](../02-liquidity/equal-highs.md) / [equal-lows](../02-liquidity/equal-lows.md) — what often forms.
- [index-am-pm-trend](index-am-pm-trend.md) — the index-futures clock this window sits between.
- [bond-split-session-rules](bond-split-session-rules.md) — the bond-market 11:00–13:00 variant.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — lunch as dead session noted.
- `ICT-2022-MENTORSHIP-OVERVIEW` — "skip lunch" discipline taught explicitly.
- `ICT-2017-INDEX-PM-TREND` (00:24) "**June 2017 ICT mentorship, ICT index trading, lesson three, the PM trend**" — self-dates the lecture; (02:41–02:50) "while I say the New York lunch hour it's basically implying that lunch is **noon to 1 p.m.**, it can actually be **as early as 11 a.m. to as late as 2 p.m.**"; (02:50–03:24) "if there's a **fast market in the morning**, traders are going to want to probably work through lunch, so **short lunch periods** or short little periods of consolidation or retracement is typically seen in those conditions. When the session in the morning was rather **lethargic**, the full lunch hour could — by way of **11 o'clock to 1 o'clock or even 2 o'clock** — be seen"; (03:24–03:39) "generally you want to be expecting some measure of **consolidation or retracement** around the noon to 1 p.m. New York time"; (06:44–06:55) an order block formed **during the lunch hour** used as the PM entry. Earliest located primary source fixing the lunch window; the `ICT-2017-CHARTER-OVERVIEW` citation above is a placeholder ID.
- `ICT-2017-BOND-SPLIT-SESSION` (07:54–08:11) "we're also encountering what is referred to as **New York lunch, around 11 o'clock to 1 o'clock** in the afternoon… while I'm defining it in general terms, noon ends the AM session, just know that it **can end earlier around 11 o'clock** in the morning".
