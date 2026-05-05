# Order Flow Shift

**Category:** 03-order-flow
**Aliases:** flow shift, OF shift, bias-flip event
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-flow, shift, bias-change

## Definition

An **Order Flow Shift** is the structural event that **flips dominant order flow direction** — typically a CHoCH or MSS that breaks the prior trend's structure. ICT teaches order-flow shifts as the **primary reversal signal**: when committed bullish flow shifts to bearish (or vice versa), prior setups in the old direction stop working and new setups in the new direction take over. The shift itself is the trigger to re-read HTF bias.

## Formal Criteria

A bullish-to-bearish OF shift requires:

- Prior trend was bullish (HH/HL structure, bullish CHoCH/MSS recent, bullish FVGs).
- A **bearish CHoCH or MSS** prints (close beyond bullish-leg's swing low with displacement).
- Subsequent setups in the bearish direction confirm (LL/LH structure forming, bearish FVGs).

For bullish-to-bearish: bullish CHoCH/MSS prints; bullish setups confirm; HTF bias was bearish.

The shift doesn't always stick — sometimes order flow oscillates around a key level before committing. Confirmation comes from 2-3 follow-up bearish (or bullish) setups in the new direction.

## Formula / Math

```
of_shift_event(direction):
    counter_trend_CHoCH_or_MSS_at_relevant_TF
    AND prior_trend was opposite
    AND post-event displacement in new direction

of_shift_confirmed:
    of_shift_event
    AND 2-3 follow-up setups in new direction succeed
    AND HTF bias re-reads as new direction
```

## Machine-Readable

```json
{
  "id": "order-flow-shift",
  "category": "03-order-flow",
  "aliases": ["flow-shift", "OF-shift", "bias-flip-event"],
  "criteria": [
    {"id": "c1", "expr": "counter-trend CHoCH/MSS event"},
    {"id": "c2", "expr": "post-event displacement in new direction"},
    {"id": "c3", "expr": "confirmation = 2-3 follow-up setups succeed in new direction"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["institutional-order-flow","algorithmic-price-delivery","bullish-order-flow","bearish-order-flow","mss","choch-bullish","choch-bearish","bias-invalidation","htf-bias-framework"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish-to-bearish order flow shift:

   prior bullish:  ▲▲▲▲ HH HL
                       \
                        \  pullback
                         \
                          ─── CHoCH down (close below prior HL)
                            ↓
                            ▼  bearish displacement + FVG down
                            ▼
                            ↓  follow-up: LL prints, bearish OF confirmed
                            ▼▼▼  
```

## Timeframes

M15–D.

## Examples

**Example 1 — bearish order-flow shift:**
- D1 has been bullish for 2 weeks (bullish flow committed).
- D candle closes below recent D swing low at 1.0820 with bearish displacement.
- → CHoCH down event = potential OF shift.
- Next 2 days: H1 sets up 2 short setups (bearish FVG retests), both deliver.
- → OF shift confirmed; HTF bias flipped bearish.

## Common Mistakes

- **Single-CHoCH treatment.** A CHoCH is the trigger event; confirmation requires follow-up setups succeeding.
- **Trading the shift candle directly.** Wait for the post-CHoCH setup, not the CHoCH bar itself.
- **Ignoring shift on lower TFs.** A daily OF shift typically rolls into smaller TFs first; if you missed the daily, watch H4/H1 for the follow-through.

## Related Concepts

- [institutional-order-flow](institutional-order-flow.md), [algorithmic-price-delivery](algorithmic-price-delivery.md), [bullish-order-flow](bullish-order-flow.md), [bearish-order-flow](bearish-order-flow.md).
- [mss](../01-market-structure/mss.md), [choch-bullish](../01-market-structure/choch-bullish.md), [choch-bearish](../01-market-structure/choch-bearish.md), [bias-invalidation](../25-htf-bias/bias-invalidation.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
