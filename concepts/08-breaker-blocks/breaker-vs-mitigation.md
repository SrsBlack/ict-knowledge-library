# Breaker vs Mitigation Block — Disambiguation

**Category:** 08-breaker-blocks
**Aliases:** none (disambiguation page)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-BREAKER-BLOCK, ICT-2016-MITIGATION-BLOCKS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** breaker, mitigation, disambiguation, terminology

## Definition

Breaker blocks and mitigation blocks are often confused in ICT discussion. Both involve a violated OB area being retested later — but they differ in **what kind of structural break preceded the retest**.

**Short version:**
- **Breaker** = OB violated as part of a **CHoCH/MSS** (polarity flip; the bias has changed).
- **Mitigation block** = OB violated as part of a **BOS** (no polarity flip; trend continues).

Same retest geometry, different structural meaning. The distinction matters because breakers are reversal-context references while mitigation blocks are continuation references.

## Formal Criteria

### Breaker

- OB violated by close-through with displacement.
- The break was a **CHoCH or MSS**.
- Polarity FLIPS (bullish OB → bearish breaker, or vice versa).
- Retest reaction is in the new direction.

### Mitigation Block

- OB violated by close-through (or sometimes by a wick).
- The break was a **BOS** in the existing trend.
- Polarity DOES NOT flip (bullish OB stays a bullish reference for continuation).
- Retest reaction is in the same direction as the original OB.

### The Containment Relationship

```
Both: violated OB returning later as a structural reference.
Breaker:    new direction (polarity flip)
Mitigation: same direction (no flip)
```

## Formula / Math

```
classify(ob_violated):
    if break_was_CHoCH_or_MSS:
        return "breaker"   (polarity flips)
    elif break_was_BOS_in_existing_trend:
        return "mitigation_block"   (polarity persists)
```

## Machine-Readable

```json
{
  "id": "breaker-vs-mitigation",
  "category": "08-breaker-blocks",
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "breaker == polarity_flip after CHoCH/MSS"},
    {"id": "c2", "expr": "mitigation_block == same_polarity after BOS"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["breaker-block","bullish-breaker","bearish-breaker","mitigation-block","bullish-order-block","bearish-order-block","choch-bullish","choch-bearish","bos-bullish","bos-bearish"],
  "sources": ["ICT-2016-BREAKER-BLOCK","ICT-2016-MITIGATION-BLOCKS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Breaker (polarity flip):                  Mitigation block (same polarity):

   bullish OB ─▼▼                            bullish OB ─▼▼
              ▲▲                                          ▲▲▲ (BOS up - trend up)
              ▲▲ ▼ ← break DOWN                                 (no CHoCH)
                ▼▼ (CHoCH down)                          
                ▼▼                                          retest ↓ → bullish reaction
                                                                 (still long bias)
   retest ↑ → bearish reaction
   (now short bias)
```

## Timeframes

M15+.

## Examples

**Example A — breaker:**
- Bullish OB existed.
- Price closes below OB low; this break IS a bearish CHoCH (prior trend was bullish).
- → bullish OB → bearish breaker. Polarity flipped. Retest → short.

**Example B — mitigation block:**
- Bullish OB existed during an uptrend.
- Price wicks below OB low briefly (or closes barely below) but then immediately prints a higher-high BOS (uptrend continues).
- No CHoCH; trend stays bullish.
- → mitigation block. Polarity persists. Retest → long (continuation).

## Common Mistakes

- **Treating all violated OBs as breakers.** Many violated OBs in trending markets are mitigation blocks, not breakers — no polarity flip occurs.
- **Mislabeling the structural break.** The CHoCH-vs-BOS classification is the key — get that right and the breaker-vs-mitigation classification follows.
- **Trading retest without checking which type.** Breaker = trade the new direction; mitigation = trade the original direction. Mixing them up trades against the algorithm.

## Related Concepts

- [breaker-block](breaker-block.md), [bullish-breaker](bullish-breaker.md), [bearish-breaker](bearish-breaker.md), [mitigation-block](mitigation-block.md).
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md).
- [choch-bullish](../01-market-structure/choch-bullish.md), [choch-bearish](../01-market-structure/choch-bearish.md), [bos-bullish](../01-market-structure/bos-bullish.md), [bos-bearish](../01-market-structure/bos-bearish.md).

## Citations

- `ICT-2016-BREAKER-BLOCK` — the definitional Dec-2016 breaker lecture; breaker framed as "this form of mitigation" [00:26].
- `ICT-2016-MITIGATION-BLOCKS` — the Dec-2016 mitigation-block lecture; "an implication of order block theory" [00:28], and forward-refers to the breaker as not yet taught [01:50].
- `ICT-2022-MENTORSHIP-OVERVIEW` — 2022 restatement.
