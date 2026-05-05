# Killzone Times Table

**Category:** 10-killzones
**Aliases:** KZ table, killzone reference card
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-KILLZONES, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** killzones, reference, table

## Definition

A single-page reference card for every ICT killzone time anchor in NY-clock time. Use as a quick lookup before any session. All times follow [dst-handling](../04-time-cycles/dst-handling.md) rules.

## Formal Criteria

The five canonical killzones, with their nested macro and silver-bullet sub-windows:

| Killzone | Window (NY) | Inside it: |
|---|---|---|
| Asia | 20:00 – 00:00 | Asian range high/low forming |
| London Open | 02:00 – 05:00 | macro 02:50–03:10; silver-bullet-london 03:00–04:00 |
| NY AM | 08:00 – 11:00 | macro 09:50–10:10; silver-bullet-ny-am 10:00–11:00 |
| London Close | 10:00 – 12:00 | overlaps NY AM 10:00–11:00; contains silver-bullet-ny-am |
| NY PM | 13:30 – 16:00 | macro 13:50–14:10; silver-bullet-ny-pm 14:00–15:00; macro 14:50–15:10 |

Macros (precision sub-windows, NY time):

| Macro | Window | Inside |
|---|---|---|
| London early | 00:50 – 01:10 | end of Asia / pre-LO-KZ |
| London open | 02:50 – 03:10 | LO-KZ |
| NY pre-open | 09:50 – 10:10 | NY AM-KZ |
| NY first PM | 13:50 – 14:10 | NY PM-KZ |
| NY mid-PM | 14:50 – 15:10 | NY PM-KZ |

Silver Bullet windows (NY time):

| SB | Window | Inside |
|---|---|---|
| London | 03:00 – 04:00 | LO-KZ |
| NY AM | 10:00 – 11:00 | NY AM-KZ + LC-KZ overlap |
| NY PM | 14:00 – 15:00 | NY PM-KZ |

## Formula / Math

See individual concept files; this is a reference table only.

## Machine-Readable

```json
{
  "id": "killzone-times-table",
  "category": "10-killzones",
  "aliases": ["kz-table", "killzone-reference-card"],
  "criteria": [
    {"id": "c1", "expr": "lookup_table_only == true"}
  ],
  "timeframes": ["M1","M5","M15","H1"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["killzone-overview","asia-killzone","london-open-killzone","ny-am-killzone","london-close-killzone","ny-pm-killzone","macro-times-overview","silver-bullet-overview"],
  "sources": ["ICT-2016-KILLZONES","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
24h NY clock:

00 ─ 02 ─ 05 ─ 08 ─ 10 ─ 11 ─ 12 ─ 13:30 ─ 16 ─ 18 ─ 20 ─ 24

█           │   │   │       │
└Asia KZ────┘   │   │       │     ──── NY PM KZ ────
20:00–24:00     │   │       │     13:30 – 16:00
   ───── London Open KZ ────│
   02:00 – 05:00            │
                ──── NY AM KZ ────
                08:00 – 11:00
                    ──── London Close KZ ────
                    10:00 – 12:00

macros: 00:50-01:10, 02:50-03:10, 09:50-10:10, 13:50-14:10, 14:50-15:10
silver-bullets: 03:00-04:00 (LDN), 10:00-11:00 (NY AM), 14:00-15:00 (NY PM)
```

## Timeframes

Reference for any TF; the table itself is timeframe-agnostic.

## Examples

**Example 1 — pre-trade lookup:**
- Current time: 09:48 NY.
- Lookup: NY AM-KZ (08:00–11:00) ✔ active. Macro 09:50–10:10 starts in 2 min. Silver Bullet 10:00–11:00 starts in 12 min.
- → high-density window approaching; setups starting now hit confluence.

## Common Mistakes

- **Using broker / server time.** Always anchor to NY.
- **Confusing macros and silver bullets.** Macros are 20-min precision; silver bullets are 60-min setup windows. They overlap but are distinct.

## Related Concepts

- [killzone-overview](killzone-overview.md) — KZ deep dive.
- Per-killzone files: [asia-killzone](asia-killzone.md), [london-open-killzone](london-open-killzone.md), [ny-am-killzone](ny-am-killzone.md), [london-close-killzone](london-close-killzone.md), [ny-pm-killzone](ny-pm-killzone.md).
- [macro-times-overview](../04-time-cycles/macro-times-overview.md) — macro deep dive.
- [silver-bullet-overview](../11-silver-bullet/silver-bullet-overview.md) — SB deep dive.

## Citations

- `ICT-2016-KILLZONES`, `ICT-2022-MENTORSHIP-OVERVIEW`.
