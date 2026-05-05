# Bearish Break of Structure (BOS)

**Category:** 01-market-structure
**Aliases:** bearish BOS, bearish structure break, continuation low break
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** structure, bos, bearish, continuation, foundational

## Definition

A bearish BOS is a candle close below the most recent confirmed swing low while the prevailing trend is already bearish. It **confirms continuation** of an existing downtrend, not a reversal. Mirror of [bos-bullish](bos-bullish.md).

## Formal Criteria

- The reference swing low `SL_ref` must be a confirmed swing low.
- A bearish BOS occurs when a later candle has `close < L(SL_ref)`.
- The prior trend must already be bearish; if it was bullish, the same close-below is a [choch-bearish](choch-bearish.md).
- Internal vs external distinction applies (same as bullish BOS).

## Formula / Math

```
SL_ref = price of most recent confirmed swing low
trend_prior = direction of last structural break on this TF

bearish_BOS := close < SL_ref AND trend_prior == "bearish"
```

## Machine-Readable

```json
{
  "id": "bos-bearish",
  "category": "01-market-structure",
  "aliases": ["bearish-bos", "bearish-structure-break"],
  "criteria": [
    {"id": "c1", "expr": "close < L(SL_ref)"},
    {"id": "c2", "expr": "trend_prior == bearish"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["bos-bullish","choch-bearish","mss","swing-low","internal-structure","external-structure"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
              \/
              /\
             /  \
            /    \
   SL_ref ──┴──────── ← prior swing low
                   \
                    \
                     close<SL ✔ (BOS)
```

Trend was already down; rally pulled back up; next leg breaks the prior low → BOS.

## Timeframes

Every TF M1 → W. HTF BOS dominates LTF counter-signals.

## Examples

**Example 1 — Daily continuation:**
- Daily trend bearish (last structural shift was a CHoCH down).
- Most recent confirmed daily swing low at 1.0750.
- After a pullback to 1.0820, a daily candle closes at 1.0735.
- → bearish BOS. Continuation confirmed; next draw is sell-side liquidity below.

## Common Mistakes

- **Wick-only break.** Spike below SL with a close back above is a sweep, not a BOS.
- **Reversal vs continuation naming.** If the prior trend was bullish, this is a CHoCH bearish.
- **Stale swing low.** Always use the most recent confirmed swing low.

## Related Concepts

- [bos-bullish](bos-bullish.md) — mirror.
- [choch-bearish](choch-bearish.md) — same close-below pattern when prior trend was bullish.
- [mss](mss.md) — displacement-driven structure shift.
- [swing-low](swing-low.md) — the reference.
- [external-structure](external-structure.md) — when a BOS bounds the range.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — BOS terminology.
- `ICT-2022-MENTORSHIP-OVERVIEW` — internal vs external operationalized.
