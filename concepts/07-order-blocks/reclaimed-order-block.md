# Reclaimed Order Block

**Category:** 07-order-blocks
**Aliases:** reclaimed block, reinforcing order block, reclaimed OB
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-RECLAIMED-OB
**Tags:** order-blocks, market-maker-model, hedging, reclaim, curve

## Definition

A reclaimed order block is an order block **left behind on the wrong side of the
move**, which price later returns to and uses again — in the opposite role from the
one it originally served. In a market maker buy model, the bullish order blocks formed
during the *decline* mark where hedging occurred; when price later trades back down
into one of them, that block is **reclaimed for new longs**.

ICT's summary of the bearish case: "a bearish reclaimed order block is a candle or bar
that was previously used to sell price… in the sell side of the curve, these old blocks
will be **reclaimed shorts or new entries for short positions**"
(`ICT-2016-RECLAIMED-OB`, 08:38–08:51).

The lecture teaches this as **"reinforcing order block theory and reclaimed blocks"**
(00:43) — the reclaim reinforces the original block rather than invalidating it.

## Formal Criteria

- Read on a **market maker model curve**: "the curve is basically a price swing lower
  that trades higher — that's all a market maker buy profile is" (03:50).
- **Bullish reclaim (buy model):** during the decline, mark every **bullish order block**
  — the down-close candle immediately before a small move higher (03:42). Each marks
  hedging inside the sell-off (04:33). On the buy side of the curve, "these old blocks or
  down candles will be **reclaimed for new longs**" (05:14).
- **Bearish reclaim (sell model):** mirrored — a candle previously used to sell price is
  revisited and taken as a new short (07:19, 08:38).
- The block must have been **created on the opposing leg** of the curve. A block formed
  in the direction of the current move is an ordinary order block, not a reclaim.
- Confirmation is **symmetry across the curve**: "everything will match up with the down
  candles on **both sides** of the market maker buy model" (04:56).
- The reclaimed level may coincide with "a filled void or closing in on a fair value gap"
  (01:08).

## Formula / Math

```
# Market maker BUY model (curve: swing lower, then higher)

sell_side_blocks := { bullish OB formed during the decline }
                    # down-close candle immediately before a minor rally
                    # each marks hedging inside the sell-off

reclaim_long(B) := price returns to B on the BUY side of the curve
                   -> B becomes a long entry reference

# Market maker SELL model: mirrored
sell_side := { bearish OB formed during the advance }
reclaim_short(B) := price returns to B -> new short

# Confirmation:
symmetry := blocks on the decline align with blocks on the advance
```

No numeric tolerance is taught for "returns to" — the reclaim is read, not gated.

## Machine-Readable

```json
{
  "id": "reclaimed-order-block",
  "category": "07-order-blocks",
  "aliases": ["reclaimed-block", "reinforcing-order-block"],
  "criteria": [
    {"id": "c1", "expr": "context == market_maker_model_curve"},
    {"id": "c2", "expr": "block_formed_on_opposing_leg == true"},
    {"id": "c3", "expr": "bullish_reclaim == down_close_candle_before_minor_rally_during_decline"},
    {"id": "c4", "expr": "price_returns_to_block_on_other_side_of_curve => new_entry_reference"},
    {"id": "c5", "expr": "confirmation == symmetry_of_blocks_both_sides_of_curve"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["bullish-order-block", "bearish-order-block", "mitigated-order-block", "unmitigated-order-block", "order-block-criteria"],
  "sources": ["ICT-2016-RECLAIMED-OB"]
}
```

## Visual Pattern

```
   Market maker BUY model:

   price
     │╲                                        ╱
     │ ╲  ▓ <- bullish OB (hedging)          ╱
     │  ╲___╱╲                              ╱
     │        ╲  ▓ <- bullish OB           ╱
     │         ╲___╲                      ╱
     │              ╲___                 ╱
     │                  ╲______╱‾‾╲____╱   <- buy side of the curve
     │                                ▲
     │                    price returns to the SAME down candles
     │                    -> RECLAIMED for new longs
     └──────────────────────────────────────────►

   ▓ = down-close candle before a minor rally, formed during the decline
```

## Timeframes

M15 through daily. The concept needs a visible market maker curve, so it does not apply
to a chart showing only one directional leg.

## Examples

**Example 1 — bullish reclaim (`ICT-2016-RECLAIMED-OB`, 05:53–06:24):**
- During the decline, a down candle preceded a small rally — a bullish order block
  marking hedging.
- After the low, price traded back down to that same down candle and was reclaimed there.
- Two such reclaimed bullish order blocks are shown on the same curve.

**Example 2 — bearish reclaim (07:19, 08:51):**
- A candle previously used to sell price is revisited on the sell side of the curve.
- It is taken as a new short entry reference.

## Common Mistakes

- **Reclaiming a same-direction block.** The block must have formed on the *opposing*
  leg of the curve; otherwise it is an ordinary
  [bullish-order-block](bullish-order-block.md) or
  [bearish-order-block](bearish-order-block.md).
- **Confusing it with mitigation.** A
  [mitigated-order-block](mitigated-order-block.md) has been traded through and spent;
  a reclaimed block is deliberately re-used in the opposite role.
- **Reading it without the curve.** No market maker model, no reclaim — the concept is
  defined relative to the curve's two sides.
- **Ignoring the symmetry check.** ICT's confirmation is that blocks match on both sides;
  a single isolated reclaim is weaker.

## Related Concepts

- [order-block-criteria](order-block-criteria.md) — what qualifies as a block in the first place.
- [bullish-order-block](bullish-order-block.md), [bearish-order-block](bearish-order-block.md) — the base directional forms.
- [mitigated-order-block](mitigated-order-block.md), [unmitigated-order-block](unmitigated-order-block.md) — the mitigation axis, distinct from reclaiming.

## Citations

- `ICT-2016-RECLAIMED-OB` (00:35) "teaching 3.4 of 8 of December 2016 ICT Mentorship"; (00:43) "the reinforcing order block theory and reclaimed blocks"; (01:08) the level may coincide with a filled void or FVG; (03:42) marking bullish order blocks — down candles before a minor rally — during the decline; (03:50–03:57) "the curve is basically a price swing lower that trades higher… that's all market maker buy profile is"; (04:25–04:33) each block indicates hedging; (04:56) "everything will match up with the down candles on both sides of the market maker buy model"; (05:04–05:14) "what is a bullish reclaimed block… these old blocks or down candles will be reclaimed for new longs"; (05:53–06:24) two worked bullish reclaims; (07:19) "that bearish order block is going to be reclaimed and you can take that as a new short"; (08:38–08:51) the bearish summary.
