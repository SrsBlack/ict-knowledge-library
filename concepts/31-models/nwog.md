# NWOG (New Week Opening Gap)

**Category:** 31-models
**Aliases:** NWOG, weekly gap, weekend gap
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2024
**Source IDs:** ICT-2023-NDOG-NWOG
**Tags:** model, nwog, weekend-gap

## Definition

NWOG (New Week Opening Gap) is the **price gap between Friday's NY close and Sunday's session open** (or Monday's open, depending on broker convention). NWOGs are typically larger than NDOGs because the weekend break is ~65+ hours and FX markets are closed. ICT teaches NWOG as a structural weekly reference: weekend gaps frequently get filled within the first 1–2 trading days of the new week, providing entry/target levels for the early-week setup.

## Formal Criteria

NWOG identification:

- Reference: closing price at 17:00 NY Friday (FX) or 16:00 NY Friday (futures).
- New open: 18:00 NY Sunday (FX broker) or Monday 00:00 NY (some FX brokers / futures).
- Gap = open - friday_close (signed).
- Bullish / bearish per direction; zone = [min, max] of the two prices.

NWOGs are larger and more reliable as fill-targets than NDOGs because of the longer weekend window.

## Formula / Math

```
friday_close = close at 17:00 NY Friday (FX)
weekend_open = open at 18:00 NY Sunday (FX) or 00:00 NY Monday

nwog_size = abs(weekend_open - friday_close)
nwog_zone = [min, max]
nwog_dir  = "bullish" if weekend_open > friday_close else "bearish"
```

## Machine-Readable

```json
{
  "id": "nwog",
  "category": "31-models",
  "aliases": ["NWOG", "weekly-gap", "weekend-gap"],
  "criteria": [
    {"id": "c1", "expr": "gap between Friday close and Sunday/Monday open"},
    {"id": "c2", "expr": "typically larger than NDOG"},
    {"id": "c3", "expr": "tendency to fill within first 1-2 trading days"}
  ],
  "timeframes": ["H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2024",
  "related": ["ndog","sunday-open-gap","true-week-open","vacuum-block","time-of-day-pivots"],
  "sources": ["ICT-2023-NDOG-NWOG"]
}
```

## Visual Pattern

```
   bullish NWOG (Sunday open above Friday close):

   Friday 17:00 NY close ──── 1.0830
                                    ▲
                                    █
                                    █  ← NWOG zone [1.0830, 1.0858]
                                    █     28 pips
                                    █
   Sunday 18:00 NY open  ──── 1.0858
                                    ↓
                                    Mon-Tue: price often fills back
                                    toward 1.0830 area.
```

## Timeframes

H1 / H4 / D.

## Examples

**Example 1 — bullish NWOG fill:**
- Friday 17:00 NY close: 1.0830.
- Sunday 18:00 NY open: 1.0858.
- NWOG: [1.0830, 1.0858], 28 pips bullish.
- Monday Asia: price drifts down toward 1.0840.
- Monday London open: M15 wicks 1.0832 (fills most of NWOG).
- → NWOG largely filled by mid-Monday.

## Common Mistakes

- **Trading the weekend gap immediately.** Sunday-Monday open volume is thin; wait for London volume on Monday for cleaner setups.
- **Different broker times.** NWOG references vary slightly by broker (some open 18:00 Sunday, others 22:00 Sunday, some 00:00 Monday). Specify broker convention.
- **Treating partial fills as failures.** NWOG fill to ~75% is common; full fill happens but isn't required.

## Related Concepts

- [ndog](ndog.md), [sunday-open-gap](sunday-open-gap.md), [true-week-open](../22-quarterly-theory/true-week-open.md), [vacuum-block](../07-order-blocks/vacuum-block.md), [time-of-day-pivots](../04-time-cycles/time-of-day-pivots.md).

## Citations

- `ICT-2023-NDOG-NWOG`.
