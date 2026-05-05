# Market Structure Shift (MSS)

**Category:** 01-market-structure
**Aliases:** structural shift, shift, displacement-driven CHoCH
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-MSS, ICT-2017-DISPLACEMENT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** structure, mss, shift, displacement, reversal

## Definition

An MSS is a CHoCH that occurs **with displacement** — a structural break against the prior trend, accompanied by a strong, fast-traveling candle (or sequence) that creates a fair value gap as it crosses the structure level. ICT uses MSS specifically to mark **algorithmic intent to reverse**: the displacement is treated as the institutional signature behind the break, distinguishing it from a CHoCH that drifts through structure with no momentum.

Every MSS is a CHoCH. Not every CHoCH is an MSS — a CHoCH without displacement is just a CHoCH.

## Formal Criteria

For a bullish MSS:

- A bullish CHoCH event has occurred (close above the swing high formed in the prior bearish leg).
- The displacement candle (the candle that broke the swing high, or the candle immediately after) qualifies as displacement: a wide-range candle with strong directional intent and minimal opposing wick.
- The displacement leaves a [bullish-fvg](../06-fair-value-gaps/bullish-fvg.md) in its wake (this is the most common operational test ICT uses).

Symmetric for a bearish MSS.

## Formula / Math

```
bullish_MSS := bullish_CHoCH(n)
                AND displacement(n) == bullish
                AND fvg_left_behind(n) == bullish

bearish_MSS := bearish_CHoCH(n)
                AND displacement(n) == bearish
                AND fvg_left_behind(n) == bearish
```

The "and FVG" test is the operational shortcut ICT teaches publicly.

## Machine-Readable

```json
{
  "id": "mss",
  "category": "01-market-structure",
  "aliases": ["structural-shift", "displacement-driven-choch"],
  "criteria": [
    {"id": "c1", "expr": "is_choch(n) == true"},
    {"id": "c2", "expr": "is_displacement(n) == true"},
    {"id": "c3", "expr": "fvg_in_break(n) == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["choch-bullish","choch-bearish","bos-bullish","bos-bearish","mss-vs-choch","displacement-definition","fair-value-gap"],
  "sources": ["ICT-2017-MSS","ICT-2017-DISPLACEMENT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
                        ▲ wide displacement candle
                        █  closes well above SH
                        █
   SH_ref ─────────────█── ← prior swing high
              /\        █
             /  \       ↑ FVG inside the displacement
            /    \      |
                  \    /
                   \  /
                    \/
```

The break candle is wide, fast, leaves an FVG: that combination is what makes the CHoCH an MSS.

## Timeframes

Most operational on entry timeframes M5 / M15 / H1 — these are where ICT teaches MSS for trade setups. HTF MSS is conceptually identical but rarer.

## Examples

**Example 1 — M5 bullish MSS:**
- M5 in a bearish leg, recent SH at 1.0850.
- After a sweep below the next M5 STL, an M5 candle prints a 22-pip body, closes at 1.0858, and leaves a 4-pip FVG inside the move.
- → bullish MSS. The FVG becomes the entry zone for a long.

## Common Mistakes

- **Calling every CHoCH an MSS.** A drifting CHoCH without displacement and without an FVG is just a CHoCH. ICT reserves "MSS" for the displaced version.
- **Ignoring the FVG test.** The FVG-in-break is the practical filter; if the break candle has no FVG, treat it as CHoCH only.
- **Mixing up MSS and BOS.** MSS is reversal context (CHoCH-like). A displacement break in the same direction as prior trend is a displacement-confirmed BOS, not an MSS.

## Related Concepts

- [choch-bullish](choch-bullish.md) / [choch-bearish](choch-bearish.md) — broader category MSS belongs to.
- [bos-bullish](bos-bullish.md) / [bos-bearish](bos-bearish.md) — continuation breaks.
- [mss-vs-choch](mss-vs-choch.md) — disambiguation page.
- [displacement-definition](../09-displacement/displacement-definition.md) — what makes a candle displacing.
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) — the FVG test for MSS.

## Citations

- `ICT-2017-MSS` — MSS terminology introduced.
- `ICT-2017-DISPLACEMENT` — displacement criteria.
- `ICT-2022-MENTORSHIP-OVERVIEW` — MSS operationalized for setups.
