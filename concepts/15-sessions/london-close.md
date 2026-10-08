# London Close

**Category:** 15-sessions
**Aliases:** London close window, European close, LDN close
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-DEFINING-DAILY-RANGE, ICT-2022-MENTORSHIP-EP40, ICT-2017-BREAD-BUTTER-BUY, ICT-2016-MARKET-EFFICIENCY-PARADIGM, ICT-2017-BOND-OPENING-RANGE, ICT-2017-DAYTRADE-ESSENTIALS, ICT-2017-BOND-SPLIT-SESSION, ICT-2022-MENTORSHIP-EP17, ICT-2022-MENTORSHIP-EP41
**Tags:** sessions, london-close, overlap, reversal

## Definition

London Close is an ERA-SPLIT window. The **2017 mentorship** clocks it 10:00 → 12:00 NY: "every day at 10 a.m. … begins the London close kill zone every day at 12 p.m. noon New York time ends" (`ICT-2017-DEFINING-DAILY-RANGE`, 04:31–04:39). The **2022 YouTube mentorship** narrows it to 10:00 → 11:00 NY and calls it a profit-taking hour: "that time frame 10 to 11 that's london close … i've always taught that 10 o'clock until 11 o'clock in the morning is london closed profit taking hour" (`ICT-2022-MENTORSHIP-EP40`, 17:18, 18:14); news days widen it to 10:00–noon. Both windows are recorded; do not collapse them into one figure. ICT's framing is profit-taking plus reversal: "london close is the time of day where we look to really bank our positions … london close can be incorporated as a entry point for longer term one shot one kill" (`ICT-2017-DAYTRADE-ESSENTIALS`, 14:52–15:21).

## Formal Criteria

- Time window: **10:00 → 12:00 NY (2017)** or **10:00 → 11:00 NY (2022, widening to 10:00–noon on news days)**.
- **Abuts, does not overlap, the forex NY killzone.** The forex NY killzone ends exactly where London close begins: "every day at 7 a.m. … begins the New York kill zone every day at 10 a.m. … ends" (`ICT-2017-DEFINING-DAILY-RANGE`, 03:57–04:17); "fx predominantly you're working with seven o'clock in the morning to ten o'clock in the morning that's your new york open kill zone" (`ICT-2022-MENTORSHIP-EP17`, 23:54); London close then "begins" at that same 10 a.m. (`ICT-2017-DEFINING-DAILY-RANGE`, 04:31). There is no shared minute in either era for forex.
- **Overlaps only the 2022 index AM window.** "8 30 in the morning to 11" (`ICT-2022-MENTORSHIP-EP41`, 03:24) runs through the 10:00–11:00 London close window — not the "07:00–10:00 forex / 08:30–11:00 indices" pairing this page previously carried as if both overlapped, and not the "08:00–12:00" figure, which belongs to bond-market NY AM hours.
- Behavior: often a reversal of London-open's direction, frequently producing the **opposing end of the daily range** — "between 10 a.m. and noon in New York time we expect the high of the daily range to form" (`ICT-2017-BREAD-BUTTER-BUY`, 11:38); "usually that's when it creates the opposing end of the daily range" (`ICT-2022-MENTORSHIP-EP40`, 17:18). 2016: "Then we go into London close, which is another reversal condition" (`ICT-2016-MARKET-EFFICIENCY-PARADIGM`, 14:38).

## Formula / Math

```
london_close_window_2017 = [10:00, 12:00] NY
london_close_window_2022 = [10:00, 11:00] NY   # widens to [10:00, 12:00] on news days

ny_forex_kz   = [07:00, 10:00] NY   # abuts london_close at 10:00, does NOT overlap it
ny_indices_am_kz = [08:30, 11:00] NY   # DOES overlap london_close, 10:00-11:00
# NOT [08:00, 12:00] -- that figure is bond-market NY AM hours, not the general NY killzone.
```

## Machine-Readable

```json
{
  "id": "london-close",
  "category": "15-sessions",
  "aliases": ["london-close-window", "european-close", "ldn-close"],
  "criteria": [
    {"id": "c1", "expr": "time_in [10:00,12:00] NY (2017) OR [10:00,11:00] NY (2022, news days [10:00,12:00])"},
    {"id": "c2", "expr": "ny_forex_kz [07:00,10:00] ABUTS london_close at 10:00, no overlap; ny_indices_am_kz [08:30,11:00] OVERLAPS london_close [10:00,11:00]; NOT [08:00,12:00]"}
  ],
  "timeframes": ["M1","M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["london-session","ny-am-session","session-overlaps","london-close-reversal"],
  "sources": ["ICT-2017-DEFINING-DAILY-RANGE","ICT-2022-MENTORSHIP-EP40","ICT-2017-BREAD-BUTTER-BUY","ICT-2016-MARKET-EFFICIENCY-PARADIGM","ICT-2017-BOND-OPENING-RANGE","ICT-2017-DAYTRADE-ESSENTIALS","ICT-2017-BOND-SPLIT-SESSION","ICT-2022-MENTORSHIP-EP17","ICT-2022-MENTORSHIP-EP41"]
}
```

## Visual Pattern

```
   07:00         08:30    10:00 ── 11:00 ──────── 12:00 NY
   ──forex NY KZ────        |       |              |
                   ──idx AM KZ──    |              |
                                ████████ ─────────  London close (2017, to noon)
                                ████████            London close (2022, "profit taking hour")
                     ↑       |       |
              forex KZ ABUTS |       |
              close at 10:00 |       |
                     idx AM KZ OVERLAPS close 10:00-11:00
```

## Timeframes

M5 / M15 / H1.

## Examples

**Example 1 — London-close reversal (2017 window, 10:00–12:00):**
- London-open delivered a 60-pip rally on EURUSD; HOD 1.0925 set at 09:30 NY.
- 10:00–11:00 NY: M5 sweeps 1.0925 BSL, closes 1.0918.
- 11:30 NY (inside the 2017 window, outside the narrower 2022 10:00–11:00 window): M5 displaces 30 pips down, leaves bearish FVG.
- → London-close reversal; rest of NY continues back into Asian range.

## Common Mistakes

- **Collapsing the two eras into one window.** 2017 = 10:00–12:00 NY; 2022 = 10:00–11:00 NY (profit-taking hour), widening to noon only on news days. Quoting one figure as "the" London close window contradicts the other era's source.
- **Claiming "one of the highest-volume windows of the trading day."** Not in corpus for London close generally — searched `highest volume|volume` near `london close`: the only volume statement in either corpus is bond-specific, "the highest volume is going to be seen between 8 a.m. and 9.30 a.m." (`ICT-2017-BOND-OPENING-RANGE`), which describes the bond AM opening range, not London close.
- **Claiming "European positions are squared" / "European institutional book unwinds."** Not in corpus — searched `unwind|square|book` near `london close`: no hits. ICT's own framing is profit-taking plus reversal, as quoted above.
- **Citing "08:00–12:00" as the NY AM window London close overlaps.** That figure is the bond-market NY AM session — "New York AM session is defined by 8 AM New York time to noon New York time" (`ICT-2017-BOND-SPLIT-SESSION`, 01:53) — not the general ICT NY killzone (07:00–10:00 forex, which abuts rather than overlaps; 08:30–11:00 indices, which does overlap).
- **Citing a "10:00–11:00 NY AM Silver Bullet" overlap.** Not in corpus — see [silver-bullet-rules](../11-silver-bullet/silver-bullet-rules.md), which is itself UNVERIFIABLE in this corpus.
- **Confusing London close with London session close.** "London Close" in ICT means the killzone window where the close-out happens — not the moment the London exchange physically closes.
- **Ignoring DST.** London-close clock-time vs NY shifts twice a year; always anchor to NY clock.

## Related Concepts

- [london-session](london-session.md) — the broader window London close is the tail of.
- [ny-am-session](ny-am-session.md) — overlapping session.
- [session-overlaps](session-overlaps.md) — disambiguation of overlap windows.
- [london-close-reversal](../31-models/london-close-reversal.md) — named setup model.
- [killzone-times-table](../10-killzones/killzone-times-table.md) — full ERA-SPLIT reference.

## Citations

- `ICT-2017-DEFINING-DAILY-RANGE` (04:31–04:39) "every day at 10 a.m. … begins the London close kill zone every day at 12 p.m. noon New York time ends."
- `ICT-2022-MENTORSHIP-EP40` (17:18) "that time frame 10 to 11 that's london close … usually that's when it creates the opposing end of the daily range"; (18:14) "i've always taught that 10 o'clock until 11 o'clock in the morning is london closed profit taking hour", news days "between 10 o'clock to noon."
- `ICT-2017-BREAD-BUTTER-BUY` (11:38) "between 10 a.m. and noon in New York time we expect the high of the daily range to form."
- `ICT-2016-MARKET-EFFICIENCY-PARADIGM` (14:38) "Then we go into London close, which is another reversal condition."
- `ICT-2017-BOND-OPENING-RANGE` (03:16) "the highest volume is going to be seen between 8 a.m. and 9.30 a.m." — bond-specific, cited here only to show the "highest-volume window" claim does not belong to London close generally.
- `ICT-2017-DAYTRADE-ESSENTIALS` (14:52–15:21) "london close is the time of day where we look to really bank our positions … london close can be incorporated as a entry point for longer term one shot one kill."
- `ICT-2017-BOND-SPLIT-SESSION` (01:53) "New York AM session is defined by 8 AM New York time to noon New York time" — the bond-specific 08:00–12:00 figure this page does not use for the general NY killzone.
- `ICT-2022-MENTORSHIP-EP17` (23:54) "fx predominantly you're working with seven o'clock in the morning to ten o'clock in the morning that's your new york open kill zone."
- `ICT-2022-MENTORSHIP-EP41` (03:24) "this is new york index am session operating hours or killzone if you want to call it that and it's 8 30 in the morning to 11."
