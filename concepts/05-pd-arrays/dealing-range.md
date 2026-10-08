# Dealing Range

**Category:** 05-pd-arrays
**Aliases:** trading range (2016 name for the same reference band), short-term dealing range
**ICT Confidence:** medium
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-OTE-USDCAD-REVIEW, ICT-2020-OTE-VOL09, ICT-2022-MENTORSHIP-EP11, ICT-2022-MENTORSHIP-EP19, ICT-2022-MENTORSHIP-EP32, ICT-2022-MENTORSHIP-EP33, ICT-2022-MENTORSHIP-EP34, ICT-2022-MENTORSHIP-EP35, ICT-2022-MENTORSHIP-EP38, ICT-2016-FAIR-VALUATION, ICT-2017-HTF-PD-ARRAYS, ICT-2016-EQUILIBRIUM-DISCOUNT
**Tags:** range, dealing-range, pd-array

## Definition

A dealing range is the price band ICT measures a swing leg across to derive premium/discount and equilibrium. The term "dealing range" itself is **not** 2016-17 Core Content vocabulary — it has 0 hits across all 110 `MONTH-*` Core Content packets. Its earliest located corpus hit is `ICT-2017-OTE-USDCAD-REVIEW` [08:46] ("It's being held in a rather tight dealing range," Nov 2017) — but that is the loose, "held in consolidation" sense of the phrase, not yet the measured premium/discount band this page defines. The measurement sense — a range you derive equilibrium and premium/discount from — first appears at `ICT-2020-OTE-VOL09` [03:14] ("standard deviation of the dealing range used for the fib"), and is used extensively and operationally in the 2022 Mentorship. In 2016-17, the equivalent measured object is called the "most recent trading range" / "impulse price swing" / "price move": "The total range you're trading in, the equilibrium price point relative to the most recent trading range, high and low." (`ICT-2016-FAIR-VALUATION` [22:34], Sep 2016); "the most recent trading range that the market has moved from an old high to an old low" (`ICT-2017-HTF-PD-ARRAYS` [17:46], Jan 2017); "Equilibrium is a midway point of a price move." (`ICT-2016-EQUILIBRIUM-DISCOUNT` [10:26], cited via [equilibrium-definition](../27-equilibrium/equilibrium-definition.md)).

## Formal Criteria

- ICT anchors the dealing range on the **most recent energetic 3-candle swing low → swing high** (or high → low), not on a depth-3 LTH/LTL pair: "so i'm just going to move over to the most recent swing low ... that swing low, that one here to here, that's my daily dealing range" (`ICT-2022-MENTORSHIP-EP19` [77:10]); "that's your dealing range, okay, i'm using that because it's the most energetic most recent low and high" (EP19 [93:22]).
- The leg chosen is the current, impulsive/expansion leg in the trade direction, not an arbitrary high-to-low span: "you're looking at expansion swings, okay, or impulsive price swings in the direction you're trying to trade — you don't want to use a price leg ... measuring something that you're trying to go long" against (`ICT-2022-MENTORSHIP-EP34` [17:03]).
- Re-anchored on the most recent market-structure swing when it shifts: "i'm going to use this one here for market structure — so market structure swing low here to swing high — that's my dealing range" (`ICT-2022-MENTORSHIP-EP38` [21:23]).
- Plain statement: "what's a dealing range? well, dealing range would be like from this high down to that low" (`ICT-2022-MENTORSHIP-EP32` [05:28]).
- EQ = midpoint of the dealing range (confirmed): "here's 50, that's equilibrium inside this dealing range high and low" (`ICT-2022-MENTORSHIP-EP11` [01:27]); "this dealing range here, i measured the low to the high, 50 is equilibrium" (`ICT-2022-MENTORSHIP-EP35` [04:23]).
- No LTH/LTL (depth-3) bounding rule, and no "external BOS ends the range" rule, appear in either corpus — ICT's range-reset is simply re-measuring from the most recent relevant swing (EP19 [93:22], EP38 [21:23]), not a stated "external BOS" trigger. (ICT's internal/external vocabulary names liquidity, not a range-ending BOS condition — see [bos-bullish](../01-market-structure/bos-bullish.md) Common Mistakes.)

## Formula / Math

```
# ICT's bounds: the most recent energetic 3-candle swing (low -> high or
# high -> low) in the trade direction — re-measured when structure shifts.
dealing_range = [swing_low, swing_high]   # most recent, most energetic
EQ            = (swing_low + swing_high) / 2

# ICT gives no LTH/LTL (depth-3) bounding rule and no numeric "external
# BOS ends the range" trigger for this. Both are absent from both corpora.
```

## Machine-Readable

```json
{
  "id": "dealing-range",
  "category": "05-pd-arrays",
  "aliases": ["trading-range", "short-term-dealing-range"],
  "criteria": [
    {"id": "c1", "expr": "bounds == most_recent_energetic_3candle_swing(low, high)"},
    {"id": "c2", "expr": "re-anchored on the most recent relevant market-structure swing"},
    {"id": "c3", "expr": "LTH/LTL depth-3 bounding: not stated by ICT"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "medium",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["pd-array-definition","premium-array","discount-array","equilibrium-definition","swing-high","swing-low"],
  "sources": ["ICT-2017-OTE-USDCAD-REVIEW","ICT-2020-OTE-VOL09","ICT-2022-MENTORSHIP-EP11","ICT-2022-MENTORSHIP-EP19","ICT-2022-MENTORSHIP-EP32","ICT-2022-MENTORSHIP-EP33","ICT-2022-MENTORSHIP-EP34","ICT-2022-MENTORSHIP-EP35","ICT-2022-MENTORSHIP-EP38","ICT-2016-FAIR-VALUATION","ICT-2017-HTF-PD-ARRAYS","ICT-2016-EQUILIBRIUM-DISCOUNT"]
}
```

## Visual Pattern

```
   swing_high ──────────────────  ← upper bound (most recent energetic swing)
            (premium half)
   ──────────────────────────  ← EQ (50% midpoint)
            (discount half)
   swing_low  ──────────────────  ← lower bound
```

## Timeframes

ICT does not restrict the term to H1+. He names a short-term dealing range explicitly on a lower-TF scrub: "if you're looking at it from the relationship of short-term dealing range — this swing High, That Swing Low — we have our fair value Gap here" (`ICT-2022-MENTORSHIP-EP33` [13:56]), and works one on a 5-minute chart (`ICT-2022-MENTORSHIP-EP35` [03:08]).

## Examples

**Example 1 — 2022 worked example, swing-to-swing anchoring:**
- "i want to use this most recent one and this is my dealing range, the short-term low, the short-term high" (`ICT-2022-MENTORSHIP-EP35` [03:08]).
- EQ is then the midpoint of that leg, not of a wider LTH/LTL span (EP35 [04:23]).

**Example 2 — short-term dealing range on a lower TF:**
- A swing high to swing low on a scrubbed-down chart is itself called a (short-term) dealing range, with its own FVG inside it (`ICT-2022-MENTORSHIP-EP33` [13:56]).

## Common Mistakes

- **Bounding the dealing range with LTH/LTL (depth-3 swings).** ICT's own worked examples anchor on the most recent energetic 3-candle swing, not a higher-order LTH/LTL pair — using LTH/LTL systematically picks an older, less current range than ICT's.
- **Requiring H1+ for a "meaningful" dealing range.** ICT names dealing ranges on scrubbed-down lower timeframes, including a 5-minute chart; "M5/M15 is too noisy" is not stated anywhere in either corpus.
- **Inventing an "external BOS ends the range" rule.** Not in either corpus; ICT simply re-measures from the current relevant swing when structure shifts (EP19 [93:22], EP38 [21:23]).
- **Missing the rebalanced-imbalance route to ITH/ITL status.** When a dealing range's bound is itself an intermediate-term swing, ICT's 2022 "rebalanced imbalance ⇒ ITH/ITL" rule is a second, non-geometric route to that status — see [swing-high](../01-market-structure/swing-high.md) / [swing-low](../01-market-structure/swing-low.md).

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [premium-array](premium-array.md), [discount-array](discount-array.md), [equilibrium-definition](../27-equilibrium/equilibrium-definition.md).
- [swing-high](../01-market-structure/swing-high.md), [swing-low](../01-market-structure/swing-low.md) — the anchors ICT actually uses.

## Citations

- `ICT-2017-OTE-USDCAD-REVIEW` [08:44]–[08:48] — earliest corpus use of "dealing range," in the loose consolidation sense (Nov 2017).
- `ICT-2020-OTE-VOL09` [03:14]–[03:18] — "standard deviation of the dealing range used for the fib" — first corpus hit of the measurement sense this page defines.
- `ICT-2016-FAIR-VALUATION` [22:34] — "the equilibrium price point relative to the most recent trading range" (Sep 2016).
- `ICT-2017-HTF-PD-ARRAYS` [17:46] — "the most recent trading range that the market has moved from an old high to an old low" (Jan 2017).
- `ICT-2016-EQUILIBRIUM-DISCOUNT` [10:26] — "Equilibrium is a midway point of a price move" (Sep 2016).
- `ICT-2022-MENTORSHIP-EP11` [01:27] — EQ as the dealing range's 50% midpoint.
- `ICT-2022-MENTORSHIP-EP19` [77:10], [93:22] — anchored on the most recent energetic 3-candle swing.
- `ICT-2022-MENTORSHIP-EP32` [05:28] — "dealing range would be like from this high down to that low."
- `ICT-2022-MENTORSHIP-EP33` [13:56] — short-term dealing range on a scrubbed lower TF.
- `ICT-2022-MENTORSHIP-EP34` [17:03] — impulsive/expansion leg in the trade direction, not an arbitrary leg.
- `ICT-2022-MENTORSHIP-EP35` [03:08]–[04:23] — swing-to-swing anchoring, including on a 5-minute chart.
- `ICT-2022-MENTORSHIP-EP38` [21:23] — re-anchored on the most recent market-structure swing.
