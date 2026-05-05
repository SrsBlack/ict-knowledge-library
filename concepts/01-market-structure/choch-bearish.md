# Bearish Change of Character (CHoCH)

**Category:** 01-market-structure
**Aliases:** bearish CHoCH, bearish reversal break, character shift down
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2017-MSS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** structure, choch, bearish, reversal, foundational

## Definition

A bearish CHoCH is the **first** candle close below the most recent confirmed swing low after a prior bullish leg. It signals a **reversal** of short-term character: the sequence of higher-highs / higher-lows just produced its first lower-low relative to the bullish leg. Mirror of [choch-bullish](choch-bullish.md).

## Formal Criteria

- The reference swing low `SL_ref` must be a confirmed swing low formed during the prior bullish leg.
- The candle must close below `L(SL_ref)`.
- The prior structural shift on this TF must have been bullish.
- After a CHoCH, subsequent breaks of new swing lows in the same direction become BOS.

## Formula / Math

```
SL_ref = most recent confirmed swing low formed during the bullish leg
trend_prior = direction of last structural shift

bearish_CHoCH := close < SL_ref AND trend_prior == "bullish"
```

After CHoCH, `trend_prior` flips to bearish.

## Machine-Readable

```json
{
  "id": "choch-bearish",
  "category": "01-market-structure",
  "aliases": ["bearish-choch", "character-shift-down"],
  "criteria": [
    {"id": "c1", "expr": "close < L(SL_ref)"},
    {"id": "c2", "expr": "trend_prior == bullish"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["choch-bullish","bos-bearish","mss","mss-vs-choch","swing-low"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2017-MSS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   prior bullish leg
              /\
             /  \
            /    \
           /      \    /\
          /        \  /
   SL_ref ──────────\/────  ← swing low formed during bull leg
                           \
                            \  close<SL ✔ (CHoCH)
```

The first close below the bull-leg swing low = CHoCH. Further down-breaks are BOS.

## Timeframes

Every TF M1 → W. HTF CHoCH is more meaningful.

## Examples

**Example 1 — Daily reversal:**
- Daily in a bullish leg of higher-highs / higher-lows.
- Recent confirmed daily swing low at 1.0850 (formed during up-leg).
- Price tops out, sells off, closes at 1.0840.
- → bearish CHoCH. Bias flips bearish.

## Common Mistakes

- **First-vs-subsequent break.** Only the first close below the reference SL is a CHoCH; everything after is BOS.
- **Wick break.** Spike-and-recover is a sweep, not a CHoCH.
- **Wrong SL reference.** Use the swing low from the recent bullish leg, not an older SL.

## Related Concepts

- [choch-bullish](choch-bullish.md) — mirror.
- [bos-bearish](bos-bearish.md) — same break, but already in a bearish trend (continuation).
- [mss](mss.md) — CHoCH with displacement.
- [mss-vs-choch](mss-vs-choch.md) — disambiguation.
- [swing-low](swing-low.md) — the reference.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — CHoCH introduced.
- `ICT-2017-MSS` — relation to MSS.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operationalized.
