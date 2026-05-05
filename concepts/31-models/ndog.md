# NDOG (New Day Opening Gap)

**Category:** 31-models
**Aliases:** NDOG, midnight gap, daily open gap
**ICT Confidence:** high
**Year Introduced:** 2023
**Year Refined:** 2024
**Source IDs:** ICT-2023-NDOG-NWOG
**Tags:** model, ndog, opening-gap

## Definition

NDOG (New Day Opening Gap) is the **price gap between the prior day's NY-close range and the current day's midnight (00:00 NY) open** — the True Day Open. ICT teaches NDOG as a structural reference: gaps frequently get filled within the same trading day, providing entry/target levels. NDOG is most relevant on FX (where 17:00 close and midnight open create the gap zone) and on continuous-trade futures.

## Formal Criteria

NDOG identification:

- Reference: closing price at 17:00 NY (forex) or 16:00 NY (equities/futures close).
- New open: 00:00 NY (True Day Open).
- Gap = TDO - prior_close (signed).
- Bullish NDOG: gap is positive (open above prior close).
- Bearish NDOG: gap is negative.

The NDOG zone is the price range between prior close and TDO; it functions as a vacuum block / opening-gap reference.

## Formula / Math

```
prior_close = close at 17:00 NY of prior day (FX) or 16:00 NY (futures)
tdo         = open at 00:00 NY of current day

ndog_size   = abs(tdo - prior_close)
ndog_zone   = [min(prior_close, tdo), max(prior_close, tdo)]
ndog_dir    = "bullish" if tdo > prior_close else "bearish"
```

## Machine-Readable

```json
{
  "id": "ndog",
  "category": "31-models",
  "aliases": ["NDOG", "midnight-gap", "daily-open-gap"],
  "criteria": [
    {"id": "c1", "expr": "gap between prior close and TDO at 00:00 NY"},
    {"id": "c2", "expr": "zone = [min, max] of the two prices"},
    {"id": "c3", "expr": "tendency to fill within same day"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2023",
  "year_refined": "2024",
  "related": ["nwog","sunday-open-gap","true-day-open","vacuum-block","time-of-day-pivots"],
  "sources": ["ICT-2023-NDOG-NWOG"]
}
```

## Visual Pattern

```
   bullish NDOG (TDO above prior close):

   17:00 prior day close ──── 1.0850
                                    ▲
                                    █  ← NDOG zone [1.0850, 1.0860]
                                    █
   00:00 current TDO       ──── 1.0860
                                    ↓
                                    intraday: NDOG often fills back
                                    to 1.0850 area at some point.
```

## Timeframes

M15 / H1 / H4 / D.

## Examples

**Example 1 — bullish NDOG fill:**
- 17:00 prior day NY close: 1.0850.
- 00:00 TDO: 1.0860.
- NDOG zone: [1.0850, 1.0860], 10 pips bullish.
- During Asia / London: price wicks back to 1.0852 (filling most of the NDOG).
- → NDOG mostly filled before NY AM.

## Common Mistakes

- **Treating NDOG fill as guaranteed.** ~70% of NDOGs partially or fully fill same day; ~30% don't.
- **Wrong reference times.** FX close is 17:00 NY (some brokers 16:55); equities/futures close is 16:00 NY. Use the correct close for the instrument.
- **Confusing NDOG with simple FVG.** NDOG is a single-bar opening gap (close-to-open), not a 3-candle wick FVG.

## Related Concepts

- [nwog](nwog.md), [sunday-open-gap](sunday-open-gap.md), [true-day-open](../22-quarterly-theory/true-day-open.md), [vacuum-block](../07-order-blocks/vacuum-block.md), [time-of-day-pivots](../04-time-cycles/time-of-day-pivots.md).

## Citations

- `ICT-2023-NDOG-NWOG`.
