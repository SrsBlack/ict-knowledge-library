# Reversal Order Block

**Category:** 07-order-blocks
**Aliases:** reversal OB, ROB, MSS-anchored OB
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2023
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-block, reversal, mss

## Definition

A reversal order block is the OB that forms **at the structural shift point** — typically the OB associated with the displacement that produced a CHoCH or MSS. The defining feature: this OB sits at the swing pivot that *defined the reversal*. ICT teaches reversal OBs as the highest-conviction OB type because they're anchored to the moment HTF intent flipped. Counterpart: [continuation-order-block](continuation-order-block.md).

## Formal Criteria

- A CHoCH or MSS just occurred ([choch-bullish](../01-market-structure/choch-bullish.md), [choch-bearish](../01-market-structure/choch-bearish.md), [mss](../01-market-structure/mss.md)).
- The OB is the last opposite-color candle before the reversal-direction displacement.
- The OB anchors at the swing pivot that the CHoCH/MSS broke (or one swing pivot before).
- Fresh / unmitigated.

## Formula / Math

```
reversal_ob(n) := order_block(n) is true (per order-block-criteria)
                   AND CHoCH_or_MSS_just_occurred_in_displacement
                   AND ob_anchored_at_pivot_where_reversal_started
```

## Machine-Readable

```json
{
  "id": "reversal-order-block",
  "category": "07-order-blocks",
  "aliases": ["reversal-OB", "ROB", "MSS-anchored-OB"],
  "criteria": [
    {"id": "c1", "expr": "OB qualifies per standard criteria"},
    {"id": "c2", "expr": "associated_with_CHoCH_or_MSS == true"},
    {"id": "c3", "expr": "anchored_at_reversal_pivot == true"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2023",
  "related": ["bullish-order-block","bearish-order-block","continuation-order-block","order-block-criteria","mss","choch-bullish","choch-bearish"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish reversal OB (post-CHoCH-up):

   recent bearish leg:
   ────────────
              \                  prior swing high  ─── (broken below)
               \                /
                \              /        ← CHoCH up: close above prior SH
                 \            /
                  \    ▼     /  ← reversal OB (last bearish candle before
                   \   ▼    /     the displacement-up candle)
                    \  ▼   /
                     \ ▲▲ /  ← displacement-up candle that triggered CHoCH
                      \▲ /
                       \/
```

## Timeframes

M15+ for meaningful structural context.

## Examples

**Example 1 — H1 bullish reversal OB:**
- H1 in bearish leg.
- 14:00 NY: H1 bearish candle (small body) at the recent swing low area.
- 15:00 NY: H1 bullish 28-pip displacement, breaks the prior bear-leg swing high → bullish CHoCH.
- → 14:00 candle is a reversal OB.
- High-conviction long entry on retest at MT, since this OB anchors the bias flip.

## Common Mistakes

- **Calling ALL OBs "reversal."** Most OBs are continuation OBs (from BOS, not CHoCH). Reversal OBs are specifically tied to the CHoCH/MSS event.
- **Wrong anchor.** A CHoCH-related OB that's NOT at the reversal pivot is a continuation OB in the new direction, not a reversal OB.

## Related Concepts

- [bullish-order-block](bullish-order-block.md), [bearish-order-block](bearish-order-block.md), [continuation-order-block](continuation-order-block.md), [order-block-criteria](order-block-criteria.md).
- [mss](../01-market-structure/mss.md), [choch-bullish](../01-market-structure/choch-bullish.md), [choch-bearish](../01-market-structure/choch-bearish.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
