# Killzone Times Table

**Category:** 10-killzones
**Aliases:** KZ table, killzone reference card
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-DEFINING-DAILY-RANGE, ICT-2022-MENTORSHIP-EP17, ICT-2022-MENTORSHIP-EP40, ICT-2022-MENTORSHIP-EP41, ICT-2016-MARKET-EFFICIENCY-PARADIGM, ICT-2016-WHAT-TO-FOCUS-ON
**Tags:** killzones, reference, table

## Definition

A single-page reference card for every ICT killzone time anchor in NY-clock time. Use as a quick lookup before any session. All times follow [dst-handling](../04-time-cycles/dst-handling.md) rules.

⚠ **The term "kill zone" exists in 2016; the clock does not.** "And you want to note what time of day that occurs, what kill zone." (`ICT-2016-WHAT-TO-FOCUS-ON`, 16:41, Sep-2016) uses the term without attaching a clock. `grep -iE "kill ?zone"` over the Months 1–7 mentorship packets (Sep 2016 – Mar 2017) returns zero hits with clock times; the earliest clocked killzone set in the corpus is the **April-2017** lecture cited below. Two real sets are recorded here instead: the **April-2017 mentorship** set and the **2022 YouTube mentorship** set, and they do **not** agree with each other. ICT frames the 2017 set as settled and corrects a widely-circulated reading by name: "folks that are using my **free tutorials**, they're waiting for 2 o'clock, 3 o'clock or 4 o'clock — **this is the actual killzone I use**, so the time window begins at **1 a.m.**, it ends at 5 a.m." (`ICT-2017-DEFINING-DAILY-RANGE`, 08:16). He also frames that lesson as settled: "this is the **definitive teaching** … if you've seen anything different in the past, **this is the real one**" (02:13–02:27). The 2022 set gives New York a different clock again — see below. See [ipda-true-day](../04-time-cycles/ipda-true-day.md) for the 2017 frame in full.

## Formal Criteria

**The 2022 YouTube mentorship set** — New York splits by market and no longer matches either the 2017 set or the widely-circulated "08:00–11:00" figure:

| Killzone | Window (NY) | Quote |
|---|---|---|
| London Open | 02:00 – 05:00 | "london open that's our kill zone that i teach here on the youtube channel it's two o'clock in the morning to five o'clock in the morning new york local time" (ep20 [08:09]) |
| New York (forex) | 07:00 – 10:00 | "fx predominantly you're working with seven o'clock in the morning to ten o'clock in the morning that's your new york open kill zone" (ep17 [23:54]) |
| New York (indices, AM) | 08:30 – 11:00 | "this is new york index am session operating hours or killzone if you want to call it that and it's 8 30 in the morning to 11" (ep41 [03:24]) |
| New York (indices, PM) | 13:30 – 16:00 | "the 1 30 to 4 new york local time that's the pm session new york index pm" (ep41 [05:53]) |
| London Close | 10:00 – 11:00 | "that time frame 10 to 11 that's london close … i've always taught that 10 o'clock until 11 o'clock in the morning is london closed profit taking hour" (ep40 [17:18], [18:14]); news days widen it "between 10 o'clock to noon" (ep40 [18:14]) |

No Asian killzone clock, no macro windows, and no Silver Bullet windows appear anywhere in the 2022 episodes (searched `macro` and `silver bullet` across all 40 captioned episodes; see [asian-range](../14-asian-range/asian-range.md) and [silver-bullet-rules](../11-silver-bullet/silver-bullet-rules.md)).

**The April-2017 mentorship set** (`ICT-2017-DEFINING-DAILY-RANGE`, 02:27–05:38):

| Window | 2017 mentorship | vs. 2022 set above |
|---|---|---|
| Asian range | 20:00 – 00:00 | no 2022 restatement; carried forward |
| ICT London killzone | 01:00 – 05:00 | 2022 narrows to 02:00 – 05:00 |
| London lunch | 05:00 – 07:00 | not restated in 2022; 2016 version runs to 08:00 instead (`ICT-2016-MARKET-EFFICIENCY-PARADIGM`, "between 5 o'clock in the morning to 8 o'clock in the morning in that time window, the market will go back into consolidation" [16:15]) |
| ICT New York killzone | 07:00 – 10:00 | matches the 2022 forex figure exactly |
| ICT London close killzone | 10:00 – 12:00 | 2022 narrows to 10:00 – 11:00 |
| IPDA true day | 00:00 – 15:00 | the containing interval; not a killzone |

**Macros and Silver Bullet windows are NOT IN CORPUS.** Searched `macro` in both corpora (153 2016-17/2020-21 packets + 40 captioned 2022 episodes): raw hits are all "macro economic"; the only 2022 hits name an unclocked "algorithm macro" (ep05 [32:15]) and a session-close "macro" (ep39 [72:50]) — no 20-minute windows anywhere. Silver Bullet windows: `grep -c -i "silver bullet"` across both corpora — 5 hits in 4 files, all idiomatic ("not going to give you a silver bullet that removes losing trades", ep10 [28:38]); no teaching of 03–04 / 10–11 / 14–15 windows exists (see [silver-bullet-rules](../11-silver-bullet/silver-bullet-rules.md) for the full count). Both are late-2022/2023 material outside this library's corpus. `# ICT gives no number for macros or Silver Bullet windows in this corpus.`

ICT's own ruling on fills vs windows: "Kill zones are when you determine your entry, and you place your orders, and you walk away. You don't need to have your entry filled inside that kill zone window" (ep18 [48:30]).

## Formula / Math

See individual concept files; this is a reference table only.

## Machine-Readable

```json
{
  "id": "killzone-times-table",
  "category": "10-killzones",
  "aliases": ["kz-table", "killzone-reference-card"],
  "criteria": [
    {"id": "c1", "expr": "lookup_table_only == true"},
    {"id": "c2", "expr": "no_2016_killzone_clock_exists_in_corpus == true"},
    {"id": "c3", "expr": "two_time_sets: mentorship_2017 vs youtube_2022"},
    {"id": "c4", "expr": "mentorship_2017: london_kz == [01:00,05:00], ny_kz == [07:00,10:00], london_close_kz == [10:00,12:00], asia == [20:00,24:00]"},
    {"id": "c5", "expr": "youtube_2022: london_kz == [02:00,05:00], ny_forex_kz == [07:00,10:00], ny_indices_am_kz == [08:30,11:00], ny_indices_pm_kz == [13:30,16:00], london_close_kz == [10:00,11:00]"},
    {"id": "c6", "expr": "macro_windows_and_silver_bullet_windows: not_in_corpus"}
  ],
  "timeframes": ["M1","M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["killzone-overview","asia-killzone","london-open-killzone","ny-am-killzone","london-close-killzone","ny-pm-killzone","macro-times-overview","silver-bullet-overview","ipda-true-day"],
  "sources": ["ICT-2017-DEFINING-DAILY-RANGE","ICT-2022-MENTORSHIP-EP17","ICT-2022-MENTORSHIP-EP40","ICT-2022-MENTORSHIP-EP41","ICT-2016-MARKET-EFFICIENCY-PARADIGM","ICT-2016-WHAT-TO-FOCUS-ON"]
}
```

## Visual Pattern

```
24h NY clock — 2022 YouTube mentorship set:

00 ─ 02 ─ 05 ─ 07 ─ 08:30 ─ 10 ─ 11 ─ 13:30 ─ 16 ─ 20 ─ 24

            ── London Open KZ ──
            02:00 – 05:00
                  ── NY (forex) KZ ──
                  07:00 – 10:00
                        ── NY (indices AM) KZ ──
                        08:30 – 11:00
                  ── London Close KZ ──
                  10:00 – 11:00
                                        ── NY (indices PM) KZ ──
                                        13:30 – 16:00

no macro sub-windows, no Silver Bullet windows in this corpus.
```

## Timeframes

Reference for any TF; the table itself is timeframe-agnostic.

## Examples

**Example 1 — pre-trade lookup (2022 set, forex):**
- Current time: 09:48 NY.
- Lookup: NY forex-KZ (07:00–10:00) ✔ active, closing in 12 min. London Close KZ (10:00–11:00) begins in 12 min.
- → session transition approaching; no macro or Silver Bullet sub-window applies in this corpus.

## Common Mistakes

- **Using broker / server time.** Always anchor to NY.
- **Quoting a 2016 killzone clock.** No clocked killzone exists before April 2017; attributing one to 2016 is not supported by either corpus.
- **Assuming one canonical set.** Quoting 02:00 as "the" London killzone start while working through 2017 mentorship material contradicts the source; quoting 08:00–11:00 for NY AM while working through 2022 material does the same — the 2022 figure is 07:00–10:00 (forex) or 08:30–11:00 (indices).
- **Inventing macro or Silver Bullet windows.** Neither has a clocked definition in this corpus; treat any such number as unverified.

## Related Concepts

- [ipda-true-day](../04-time-cycles/ipda-true-day.md) — the April-2017 time set in full, with the 00:00–15:00 frame it sits inside.
- [killzone-overview](killzone-overview.md) — KZ deep dive.
- Per-killzone files: [asia-killzone](asia-killzone.md), [london-open-killzone](london-open-killzone.md), [ny-am-killzone](ny-am-killzone.md), [london-close-killzone](london-close-killzone.md), [ny-pm-killzone](ny-pm-killzone.md).
- [macro-times-overview](../04-time-cycles/macro-times-overview.md) — macro deep dive (unverified; see note above).
- [silver-bullet-overview](../11-silver-bullet/silver-bullet-overview.md) — SB deep dive (unverified; see [silver-bullet-rules](../11-silver-bullet/silver-bullet-rules.md)).

## Citations

- `ICT-2017-DEFINING-DAILY-RANGE` (00:14) "lesson two of the April 2017 ICT mentorship"; (02:13–02:27) "this is the **definitive teaching** … if you've seen anything different in the past, **this is the real one**"; (02:27–02:41) Asian range **8 p.m. → midnight**; (03:06–03:24) London killzone **1 a.m. → 5 a.m.**; (03:57–04:17) New York killzone **7 a.m. → 10 a.m.**; (04:31–04:39) London close killzone **10 a.m. → 12 noon**; (05:07–05:38) IPDA true day **midnight → 3 p.m.**; (07:47) London lunch between the London and New York killzones; (08:16) "folks that are using my **free tutorials**, they're waiting for 2 o'clock, 3 o'clock or 4 o'clock — **this is the actual killzone I use**, so the time window begins at **1 a.m.**".
- `ICT-2022-MENTORSHIP-EP17` [23:54] "fx predominantly you're working with seven o'clock in the morning to ten o'clock in the morning that's your new york open kill zone"; [25:38] "if you're looking at a model that works in index futures you're looking at that 8 30 to 11 o'clock window and if you're trying to apply this model to fx it's seven o'clock in the morning to 10 o'clock in the morning".
- `ICT-2022-MENTORSHIP-EP40` [08:28] "seven o'clock in the morning new york time that's the beginning of my ict new york kill zone it's extended to 10 o'clock in the morning when it's 4x"; [17:18] "that time frame 10 to 11 that's london close"; [18:14] "i've always taught that 10 o'clock until 11 o'clock in the morning is london closed profit taking hour", news days "between 10 o'clock to noon"; [43:52] "between 1 30 and 4 o'clock in the afternoon new york local time".
- `ICT-2022-MENTORSHIP-EP41` [03:24] "this is new york index am session operating hours or killzone if you want to call it that and it's 8 30 in the morning to 11"; [05:53] "the 1 30 to 4 new york local time that's the pm session new york index pm".
- `ICT-2016-MARKET-EFFICIENCY-PARADIGM` [16:15] "Between 5 o'clock in the morning to 8 o'clock in the morning in that time window, the market will go back into consolidation" — the 2016 London-lunch figure (ends 08:00, not 07:00).
- `ICT-2016-WHAT-TO-FOCUS-ON` [16:41] "And you want to note what time of day that occurs, what kill zone." — the term in use in 2016, without a clock.
