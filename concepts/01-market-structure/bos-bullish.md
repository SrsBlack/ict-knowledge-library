# Bullish Break of Structure (BOS)

**Category:** 01-market-structure
**Aliases:** bullish BOS, bullish structure break, continuation high break
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** structure, bos, bullish, continuation, foundational

## Definition

A bullish BOS is a candle close above the most recent confirmed swing high while the prevailing trend is already bullish. It **confirms continuation** of an existing uptrend — it is not a reversal signal. The swing high being broken is the reference structure point; the close (not the wick) crossing it makes the break official.

## Formal Criteria

- The reference swing high `SH_ref` must be a confirmed swing high (3-bar pattern, candle after it has closed).
- A bullish BOS occurs when a later candle has `close > H(SH_ref)`.
- The prior trend must be bullish — meaning the most recent structural shift on this TF was upward (a CHoCH or external BOS to the upside). If the prior trend was bearish, the same close-above-swing-high is a [choch-bullish](choch-bullish.md) instead.
- ICT distinguishes internal BOS (swing high inside the dealing range) from external BOS (swing high that bounds the range). Both follow the same close-above rule; they differ only in structural significance.

## Formula / Math

```
SH_ref = price of most recent confirmed swing high
trend_prior = direction of last structural break on this TF

bullish_BOS := close > SH_ref AND trend_prior == "bullish"
```

If `trend_prior == "bearish"`, the same close-above is a CHoCH, not a BOS.

## Machine-Readable

```json
{
  "id": "bos-bullish",
  "category": "01-market-structure",
  "aliases": ["bullish-bos", "bullish-structure-break"],
  "criteria": [
    {"id": "c1", "expr": "close > H(SH_ref)"},
    {"id": "c2", "expr": "trend_prior == bullish"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["bos-bearish","choch-bullish","mss","swing-high","internal-structure","external-structure"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
                    close>SH ✔ (BOS)
                         /
   SH_ref ─────────────┴────  ← prior swing high
              /\
             /  \
            /    \
                  \  /
                   \/
                  pullback
```

Trend was already up; pullback formed; next leg breaks the prior high → BOS.

## Timeframes

Every TF M1 → W. Higher-TF BOS carries more weight; an H4 BOS often supersedes a counter-trend M5 CHoCH.

## Examples

**Example 1 — H1 continuation:**
- H1 prior trend bullish (last shift was a CHoCH up two days ago).
- Most recent confirmed H1 swing high at 1.0920.
- A pullback to 1.0890 holds, then a candle closes at 1.0925.
- → bullish BOS. Bias remains bullish; next draw on liquidity is the next external high above.

## Common Mistakes

- **Wick-only break.** A wick above the swing high without a close above it is a stop-run, not a BOS. Use candle close.
- **Calling reversals BOS.** If the prior trend was bearish, a close above a swing high is a CHoCH, not a BOS. The naming matters because BOS = continuation, CHoCH = reversal.
- **Internal vs external confusion.** Internal BOS (inside the dealing range) does not flip HTF bias. External BOS (above the LTH bounding the range) does.
- **Stale references.** Always use the *most recent* confirmed swing high. Breaking an old, already-superseded swing high is not a BOS — it's just continuation through stale structure.

## Related Concepts

- [bos-bearish](bos-bearish.md) — mirror.
- [choch-bullish](choch-bullish.md) — bullish break when prior trend was bearish (reversal vs continuation).
- [mss](mss.md) — a specific kind of structure shift characterized by displacement.
- [swing-high](swing-high.md) — the reference being broken.
- [external-structure](external-structure.md) — when a BOS bounds the range.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — BOS terminology introduced.
- `ICT-2022-MENTORSHIP-OVERVIEW` — internal vs external BOS distinction operationalized.
