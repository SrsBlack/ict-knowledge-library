# Mitigation Block

**Category:** 08-breaker-blocks
**Aliases:** MB, mitigation, hedge block
**ICT Confidence:** medium
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2018-BLOCKS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** mitigation-block, breaker-related, foundational

## Definition

A mitigation block is a structural reference closely related to a breaker but distinguished by **what came before**: a mitigation block forms when an OB-zone is **failed without first triggering a CHoCH/BOS in the breaker direction** — instead, it forms during a continued trend where institutions are presumed to be hedging or "mitigating" earlier positions taken at the OB. ICT's framing of mitigation blocks varies; the concept is less standardized than breakers. Often used as a continuation reference in trending markets where price returns to a prior failed-OB area without flipping bias.

## Formal Criteria

A mitigation block forms when:

- An OB-like zone existed.
- Price violated the OB but the structural break was a **BOS in the existing trend** (not a CHoCH).
- The OB body now serves as a **continuation reference** (same direction as before).
- Distinct from a breaker because there's no polarity flip — direction stays the same.

Operationally fuzzy; many practitioners use "mitigation block" and "breaker" interchangeably. ICT's specific 2018 framing kept them distinct via the BOS-vs-CHoCH context.

## Formula / Math

```
mitigation_block(ob) := ob was violated
                         AND structural_break_was_BOS (existing trend)
                         AND OB_acts_as_same_polarity_continuation_zone
```

## Machine-Readable

```json
{
  "id": "mitigation-block",
  "category": "08-breaker-blocks",
  "aliases": ["MB", "mitigation", "hedge-block"],
  "criteria": [
    {"id": "c1", "expr": "OB violated"},
    {"id": "c2", "expr": "break_was_BOS_not_CHoCH == true"},
    {"id": "c3", "expr": "no_polarity_flip == true"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["breaker-block","breaker-vs-mitigation","bullish-order-block","bearish-order-block","mitigated-order-block","mitigation-definition"],
  "sources": ["ICT-2018-BLOCKS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish mitigation block (in continuing uptrend):

   ▲▲▲ ▼ ▼ ▲▲▲▲   ← uptrend with pullback OB at ▼▼
                ▲▲▲    ← BOS continuation through the OB area
                       (no CHoCH; trend stays bullish)
                            ↓
                       price returns to OB area later
                       acts as continuation support (same polarity)
```

## Timeframes

M15+.

## Examples

**Example 1 — bullish mitigation block in trend:**
- H1 bullish OB formed at body 1.0820–1.0830 during a clean uptrend.
- Hours later H1 wicks below 1.0820 (briefly, no decisive close) on a deep pullback, then prints a strong bullish BOS to a new high.
- The OB is "violated" but trend stays bullish.
- → mitigation block. On future return to 1.0825, treat as continuation long support.
- Distinct from a breaker because there was no CHoCH-up; the trend was already up.

## Common Mistakes

- **Treating MB as a breaker.** Breaker requires polarity flip; MB doesn't.
- **Loose qualification.** Without a clear OB lineage and BOS context, MB classification is arbitrary.
- **Over-relying on MB.** They're lower-conviction than fresh OBs; some practitioners skip MBs entirely in favor of cleaner setups.

## Related Concepts

- [breaker-block](breaker-block.md), [breaker-vs-mitigation](breaker-vs-mitigation.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [mitigated-order-block](../07-order-blocks/mitigated-order-block.md), [mitigation-definition](../18-mitigation/mitigation-definition.md).

## Citations

- `ICT-2018-BLOCKS`, `ICT-2022-MENTORSHIP-OVERVIEW`.

> Confidence is `medium` because mitigation-block usage varies widely across the ICT community; the boundary with breakers is taught inconsistently.
