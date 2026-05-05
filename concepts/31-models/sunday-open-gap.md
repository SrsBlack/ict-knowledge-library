# Sunday Open Gap

**Category:** 31-models
**Aliases:** Sunday gap, weekly open gap, SOG
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2024
**Source IDs:** ICT-2023-NDOG-NWOG
**Tags:** model, sunday-open, gap

## Definition

The Sunday Open Gap is the specific instance of [nwog](nwog.md) at the **broker-defined Sunday open** — typically 18:00 NY for FX. It is the start of the new trading week and frequently produces the week's structural reference points. Distinct from NWOG (which is a price-zone concept) — Sunday Open Gap emphasizes the **time-anchored event** and the price action immediately around it (Sunday evening through Monday Asia).

## Formal Criteria

- Time anchor: 18:00 NY Sunday (broker FX open) — sometimes 17:00 NY or 22:00 NY depending on broker.
- The gap (NWOG) is the price difference between Friday close and Sunday open.
- Setup behavior:
  - Sunday evening (18:00–00:00 NY) typically thin volume; chop / range-building.
  - Asian session begins ~18:00 (or after); ranges often form around the Sunday open.
  - Monday London open often raids the Sunday-Monday range.

## Formula / Math

```
sunday_open_event_window:
    [18:00 Sun NY, 03:00 Mon NY]    # broker-dependent

key_levels:
    sunday_open_price = open at 18:00 Sun NY
    monday_TDO        = open at 00:00 Mon NY (= sunday open + small drift)
    nwog_size         = abs(sunday_open - friday_close)
```

## Machine-Readable

```json
{
  "id": "sunday-open-gap",
  "category": "31-models",
  "aliases": ["Sunday-gap", "weekly-open-gap", "SOG"],
  "criteria": [
    {"id": "c1", "expr": "anchored at 18:00 NY Sunday (broker FX open)"},
    {"id": "c2", "expr": "produces the NWOG"},
    {"id": "c3", "expr": "Monday London open often raids the Sunday-Monday range"}
  ],
  "timeframes": ["M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2024",
  "related": ["nwog","ndog","true-week-open","vacuum-block","asian-range","london-open-killzone"],
  "sources": ["ICT-2023-NDOG-NWOG"]
}
```

## Visual Pattern

```
   Sunday Open Gap timeline:

   Friday 17:00 NY close: 1.0830
   ── (weekend) ──
   Sunday 18:00 NY open:  1.0858  ← Sunday Open
                          ↓
                          18:00 Sun → 00:00 Mon: thin Asian volume, range builds
                          ↓
                          02:00–05:00 Mon NY: London open raids one bound
                          ↓
                          frequently fills part of the NWOG by mid-Monday
```

## Timeframes

M15–H4.

## Examples

**Example 1 — Sunday Open Gap into Monday delivery:**
- Friday 17:00: 1.0830.
- Sunday 18:00 open: 1.0858.
- 18:00 Sun – 03:00 Mon NY: range builds 1.0850–1.0865.
- 02:55 Mon NY (London open Judas): M5 wicks 1.0846 (sweeps Sunday SSL), reverses up.
- 03:30+: bullish delivery; NWOG partially filled when price first drifts back to 1.0840.

## Common Mistakes

- **Trading Sunday evening.** Volume is thin; setups are noisy. Wait for London Monday.
- **Treating Sunday Open as a literal "gap" on FX charts.** Continuous-price brokers may show the gap as a fast move rather than a clean visual gap — same structural meaning.

## Related Concepts

- [nwog](nwog.md), [ndog](ndog.md), [true-week-open](../22-quarterly-theory/true-week-open.md), [vacuum-block](../07-order-blocks/vacuum-block.md), [asian-range](../14-asian-range/asian-range.md), [london-open-killzone](../10-killzones/london-open-killzone.md).

## Citations

- `ICT-2023-NDOG-NWOG`.
