# Bullish Change of Character (CHoCH)

**Category:** 01-market-structure
**Aliases:** bullish CHoCH, bullish reversal break, character shift up
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2017-MSS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** structure, choch, bullish, reversal, foundational

## Definition

A bullish CHoCH is the **first** candle close above the most recent confirmed swing high after a prior bearish leg. It signals a **reversal** of short-term character: price has stopped making lower-highs / lower-lows and has just made the first higher-high relative to the bearish leg. Distinguished from BOS by what came before — a bullish close above a swing high is BOS only if the prior trend was already bullish; if the prior trend was bearish, the same close is a CHoCH.

## Formal Criteria

- The reference swing high `SH_ref` must be a confirmed swing high (3-bar pattern, candle after closed).
- The candle in question must close above `H(SH_ref)`.
- The prior structural shift on this TF must have been **bearish** (i.e., trend_prior = bearish).
- Once a CHoCH fires, all subsequent breaks of new swing highs in the same direction are BOS, not CHoCH.

## Formula / Math

```
SH_ref = most recent confirmed swing high formed during the bearish leg
trend_prior = direction of last structural shift

bullish_CHoCH := close > SH_ref AND trend_prior == "bearish"
```

After a CHoCH, `trend_prior` is updated to bullish.

## Machine-Readable

```json
{
  "id": "choch-bullish",
  "category": "01-market-structure",
  "aliases": ["bullish-choch", "character-shift-up"],
  "criteria": [
    {"id": "c1", "expr": "close > H(SH_ref)"},
    {"id": "c2", "expr": "trend_prior == bearish"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["choch-bearish","bos-bullish","mss","mss-vs-choch","swing-high"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2017-MSS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   prior bearish leg              first close above SH (CHoCH)
        \                              /
         \    SH_ref ────────────────┴──
          \      /\        /\
           \    /  \      /
            \  /    \    /
             \/      \  /
                      \/  ← lowest point of bearish leg
```

CHoCH is the **single** event that flips bias. Subsequent up-moves through new swing highs are BOS continuation events.

## Timeframes

Every TF M1 → W. CHoCH on a higher TF is more meaningful — an H4 CHoCH usually outweighs a counter-trend M5 CHoCH.

## Examples

**Example 1 — H1 reversal:**
- H1 in a bearish leg making lower-highs / lower-lows.
- Most recent confirmed H1 swing high at 1.0850 (formed during the down leg).
- Price drops, finds a low, rallies, closes at 1.0855.
- → bullish CHoCH. Bias flips bullish; next continuation high break would be a BOS.

## Common Mistakes

- **Calling every break-up a CHoCH.** Once the first CHoCH fires, subsequent up-breaks are BOS, not more CHoCHs.
- **Wick-only break.** Use candle close, not wick.
- **Wrong reference swing.** Use the swing high formed during the recent bearish leg, not an old one from previous structure.
- **Ignoring TF context.** A CHoCH on M1 inside a bearish H1 trend is still a CHoCH on M1, but it does not flip the H1 bias.

## Related Concepts

- [choch-bearish](choch-bearish.md) — mirror.
- [bos-bullish](bos-bullish.md) — same break, but in already-bullish context (continuation).
- [mss](mss.md) — a CHoCH that occurs with displacement (a stricter ICT term).
- [mss-vs-choch](mss-vs-choch.md) — disambiguation.
- [swing-high](swing-high.md) — the reference structure point.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — CHoCH introduced as reversal indicator.
- `ICT-2017-MSS` — relationship to MSS clarified.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational use for entries.
