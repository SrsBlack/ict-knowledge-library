# Mitigation of OB

**Category:** 18-mitigation
**Aliases:** OB mitigation, OB tested, OB consumed
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-OB-INTRO, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** mitigation, ob, foundational

## Definition

OB mitigation is the act of price returning to an order block and **reaching at least the OB's MT** (body midpoint). Once mitigated, the OB transitions from fresh to tested; the highest-conviction entry is the first touch at MT. Subsequent retests are progressively lower-probability.

## Formal Criteria

- The OB qualifies per [order-block-criteria](../07-order-blocks/order-block-criteria.md).
- Price returns and reaches at least the OB's MT.
- "Reach" includes wick touches (not just closes).
- After mitigation, the OB is no longer "fresh."

## Formula / Math

```
ob_mt = (open(ob_candle) + close(ob_candle)) / 2

is_ob_mitigated(ob) := exists future candle k
                        such that
                          (bullish OB) low(k) <= ob_mt
                          OR (bearish OB) high(k) >= ob_mt
```

## Machine-Readable

```json
{
  "id": "mitigation-of-ob",
  "category": "18-mitigation",
  "aliases": ["OB-mitigation", "OB-tested"],
  "criteria": [
    {"id": "c1", "expr": "price reaches OB MT (body midpoint)"},
    {"id": "c2", "expr": "wick touch counts"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["mitigation-definition","mitigated-order-block","unmitigated-order-block","mean-threshold","bullish-order-block","bearish-order-block","partial-vs-full-mitigation"],
  "sources": ["ICT-2016-OB-INTRO","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish OB mitigation:

   ▼ ← OB formed (body 1.0820-1.0830, MT 1.0825)
        ▲▲▲ displacement away
              .......... price returns ..........
                           ↓
                          1.0825 ← MT reached → MITIGATED
                          ↓ (or could continue down to 1.0820 = full)
```

## Timeframes

All TFs M5+.

## Examples

**Example 1 — bullish OB mitigation entry:**
- H1 bullish OB body 1.0820–1.0830, MT 1.0825.
- Price returns; H1 wicks 1.0824 (just past MT), then prints bullish reaction.
- → mitigation triggered; first-touch entry valid.

## Common Mistakes

- **Far-edge fixation.** Some practitioners insist on price reaching the OB low (full mitigation) before entry; ICT's standard is MT.
- **Excessively tight MT.** Use a small buffer; pixel-precision causes missed fills.
- **Re-entering on a re-test of an already-mitigated OB.** Conviction drops sharply after first mitigation.

## Related Concepts

- [mitigation-definition](mitigation-definition.md), [mitigated-order-block](../07-order-blocks/mitigated-order-block.md), [unmitigated-order-block](../07-order-blocks/unmitigated-order-block.md), [mean-threshold](../27-equilibrium/mean-threshold.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [partial-vs-full-mitigation](partial-vs-full-mitigation.md).

## Citations

- `ICT-2016-OB-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
