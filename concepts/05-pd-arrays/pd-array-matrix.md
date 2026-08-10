# PD Array Matrix

**Category:** 05-pd-arrays
**Aliases:** PDA matrix, PD array map, multi-TF PDA grid
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2024
**Source IDs:** ICT-2017-PD-ARRAY-MATRIX, ICT-2017-LONGTERM-TOP-DOWN, ICT-2017-INTERMEDIATE-TOP-DOWN, ICT-2017-TOPDOWN-SHORT-TERM, ICT-2017-INTRADAY-TOP-DOWN, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2024-MENTORSHIP-MODULE-LIST
**Tags:** pd-array, matrix, mapping, calibration

## Definition

The PD array matrix is the **PDA-side counterpart of the [liquidity-matrix](../02-liquidity/liquidity-matrix.md)**: a structured pre-trade tabulation of every relevant PD array across multiple timeframes, sorted by price, listing TF / array type / depth (premium or discount with its depth value) / freshness / direction. It is a working document the analyst maintains during the session — adding new arrays as they form, marking arrays as "tested" or "mitigated" once price interacts with them.

ICT positions it as the thing that makes everything else usable, and as the reason his public tutorials did not transfer: "everybody asks the same questions — **which order block do I buy, which one am I looking at?** All that's answered with the PD array matrix" (`ICT-2017-TOPDOWN-SHORT-TERM`, 31:52–32:10); "without understanding the PD array matrix, and understanding how we work from a higher timeframe down to a lower timeframe… **you will never be consistent with my concepts**" (`ICT-2017-INTRADAY-TOP-DOWN`, 46:53).

⚠ **Dating and confidence corrected 2026-08-10.** This page previously carried `Year Introduced: 2022` and `ICT Confidence: medium`, with a footnote calling the term "community-popularized". Both are wrong. The **February-2017** swing-trading lecture already defines the split in these words — "every array above market price is the **premium spectrum**… and every array below current market action is the **discount spectrum**" (`ICT-2017-PD-ARRAY-MATRIX`, 04:23–04:27) — the earliest matrix usage in the corpus, and a source this page was not citing at all. ICT then names the PD array matrix repeatedly, as a numbered step in his own routine, throughout the **August-2017** capstone — "and then I look at the **PD array matrix**" (`ICT-2017-LONGTERM-TOP-DOWN`, 10:41), "next is I break down the **PD array matrix** on weekly" (`ICT-2017-INTERMEDIATE-TOP-DOWN`, 07:14), "it's all about the **PD array matrix**; if you don't use that or understand it, you're not going to be consistent with my stuff" (`ICT-2017-INTRADAY-TOP-DOWN`, 10:11). Re-dated to **2017**, confidence raised to `high`, and the community-attribution footnote removed.

## Formal Criteria

A complete matrix lists, for the current symbol:

- Above and below current price, every PD array on M15 / H1 / H4 / D / W.
- For each array: TF, type (OB / FVG / breaker / etc.), price range, premium-or-discount + depth, freshness (unmitigated / partially / fully mitigated), polarity (bullish / bearish).
- Sorted by price for navigation.
- Optional: HTF-LTF nesting indicators (which arrays nest inside others).

**Build rules ICT states directly** (`ICT-2017-LONGTERM-TOP-DOWN`, 32:21–35:07):

- **The matrix is built inside a chosen range**, not over the whole chart. Pick the portion of market structure the trade will be framed in, then split *that* into premium and discount.
- **Most arrays will be absent, and that is expected.** "Not every price range will have every possible premium and or discount array — I just note the ones that are obvious" (32:42); "because I gave you the PD arrays, it doesn't mean not every price range is going to have every single one of them… chances are they're not going to be there" (49:22). In the worked AUDUSD example only three discount arrays existed — a bullish order block, a rejection block and the old low — with no liquidity void, no vacuum gap and no breaker present. ICT calls the outcome **definitive, not ambiguous**: "is this ambiguous? No. It's definitive. It actually tells you exactly what you're looking for" (49:57).
- **Resolution increases as you descend.** "Any PD array that didn't exist in the monthly may now materialize in the weekly chart, because you're going to get much more definition" (`ICT-2017-INTERMEDIATE-TOP-DOWN`, 07:22).

**Calibration — the rounding rule** (`ICT-2017-LONGTERM-TOP-DOWN`, 33:54–35:07; repeated at each of the four tiers)

Once the arrays are identified, each is rounded to a **whole, five or ten level** to become a *key price level*:

- **Premium arrays above market price → round DOWN.** "I don't ever want to round up to it. **I want that low hanging fruit**" (34:36).
- **Discount arrays below market price → round UP.** Again "to the nearest objective" (35:04).
- Equivalently: **always round toward current price**, never past the array.
- Pick whichever of the zero / five / ten levels lands closest — "it's going to be a matter of preference, whichever gets closer to the actual PD array" (34:08).
- If the array already sits on such a level, leave it. Worked example: an order-block open at **7380** needs no adjustment because "it's right at 80, it's at a zero level"; had it been **7382** it would be moved to **7385** (50:26–50:48).

## Formula / Math

```
matrix(t) = sort_by_price([
  { tf: M15 | H1 | H4 | D | W,
    type: OB | FVG | breaker | mitigation | rejection | propulsion | vacuum | EQ,
    price_range: [low, high],
    side: premium | discount,
    depth: float in [0, 1],
    polarity: bullish | bearish,
    fresh: bool,
    nested_with: [list of other matrix entries it overlaps]
  }
  for every identified array
])

# Calibration to key price levels — round TOWARD current price, never past the array.
grid(p)          := nearest of {..., x0, x5, x10, ...} levels
calibrate(array) :=
    if array.side == premium and array.price > current_price:
        floor_to_grid(array.price)        # round DOWN  ("low hanging fruit")
    if array.side == discount and array.price < current_price:
        ceil_to_grid(array.price)         # round UP
    # already on a grid level -> unchanged

# worked example (AUDUSD monthly bullish order block, below market):
#   7380 -> 7380   (already a zero level)
#   7382 -> 7385   (discount array, rounds UP to the nearest five level)
```

## Machine-Readable

```json
{
  "id": "pd-array-matrix",
  "category": "05-pd-arrays",
  "aliases": ["PDA-matrix", "PDA-map"],
  "criteria": [
    {"id": "c1", "expr": "every_array_listed_with_tf_type_depth == true"},
    {"id": "c2", "expr": "matrix_sorted_by_price == true"},
    {"id": "c3", "expr": "matrix built inside a chosen structural range, not the whole chart"},
    {"id": "c4", "expr": "absent array types are normal; only arrays actually present are listed"},
    {"id": "c5", "expr": "array resolution increases on lower timeframes"},
    {"id": "c6", "expr": "calibrate premium_array_above_price := floor to nearest 0/5/10 level"},
    {"id": "c7", "expr": "calibrate discount_array_below_price := ceil to nearest 0/5/10 level"},
    {"id": "c8", "expr": "rounding always moves TOWARD current price, never past the array"}
  ],
  "timeframes": ["M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2024",
  "related": ["pd-array-definition","pd-array-hierarchy","pd-array-nesting","pd-array-confluence","htf-pd-array-hierarchy","liquidity-matrix","top-down-analysis","ict-core-patterns"],
  "sources": ["ICT-2017-PD-ARRAY-MATRIX","ICT-2017-LONGTERM-TOP-DOWN","ICT-2017-INTERMEDIATE-TOP-DOWN","ICT-2017-TOPDOWN-SHORT-TERM","ICT-2017-INTRADAY-TOP-DOWN","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2024-MENTORSHIP-MODULE-LIST"]
}
```

## Visual Pattern

A tabular view, not a chart pattern. Sample matrix for a bullish-bias EURUSD intraday session:

```
TF   Type      Range            Side    Depth  Polarity  Fresh  Nest
──   ───────   ──────────────   ──────  ─────  ────────  ─────  ────
W    OB        1.0950–1.0970    premium 0.71   bear      yes    -
D    FVG       1.0935–1.0945    premium 0.40   bear      yes    nested in W OB
D    EQ        1.0900           --      0.50   --        --     -
H4   OB        1.0840–1.0850    discount 0.50  bull      yes    -
H4   FVG       1.0825–1.0835    discount 0.71  bull      yes    -
H1   OB        1.0820–1.0830    discount 0.78  bull      yes    nested in H4 FVG
─── current price 1.0855 ───
H1   FVG       1.0808–1.0815    discount 0.92  bull      yes    -
D    OB        1.0790–1.0800    discount 0.95  bull      yes    -
```

## Timeframes

The matrix is multi-TF by definition. Don't include arrays from below your minimum entry TF (clutter).

## Examples

**Example 1 — using the matrix:**
- HTF (D, W) bullish bias.
- Matrix shows nested H4-FVG / H1-OB at 1.0820–1.0835 (deep discount, fresh).
- Pre-trade plan: long entry on retest of 1.0820–1.0830 with SL below H1 OB (1.0815), TP1 at D EQ (1.0900), TP2 at D FVG (1.0935), final at W OB premium (1.0970).

## Common Mistakes

- **Listing everything.** Too many entries make the matrix unusable. Cap by TF (M15+) and by freshness (unmitigated only).
- **Static matrix.** Refresh as price interacts with arrays — once an array is mitigated or invalidated by a BOS, mark it as such.
- **Skipping nesting markers.** Nested arrays often produce the strongest setups; explicitly note which arrays overlap.
- **Hunting for the missing array types.** A range that holds only an order block, a rejection block and an old low is a *complete* matrix for that range. "People make this a lot harder than it has to be" (`ICT-2017-LONGTERM-TOP-DOWN`, 49:22).
- **Rounding past the array.** Rounding a premium level *up* or a discount level *down* moves the objective further away and gives up the low-hanging fruit — ICT rules it out by name.
- **Calibrating before the range is chosen.** Rounding is the last step: identify the structural range, then the arrays inside it, then round.

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [pd-array-hierarchy](pd-array-hierarchy.md), [pd-array-nesting](pd-array-nesting.md), [pd-array-confluence](pd-array-confluence.md), [htf-pd-array-hierarchy](htf-pd-array-hierarchy.md).
- [liquidity-matrix](../02-liquidity/liquidity-matrix.md) — analogous tool for liquidity pools.
- [top-down-analysis](../25-htf-bias/top-down-analysis.md) — the matrix is step 4 of the shared spine, run once per tier.
- [ict-core-patterns](../31-models/ict-core-patterns.md) — what the calibrated levels are handed to.

## Citations

- `ICT-2017-PD-ARRAY-MATRIX` (03:49–03:57, 04:23–04:27) — the earliest matrix statement in the corpus: "framing the PD arrays above market price is in the premium spectrum, and the arrays below market price is the discount spectrum… every array above market price is the premium spectrum, and every array below current market action is the discount spectrum." ⚠ Partial read; this library has distilled only selected passages of that lecture.
- `ICT-2017-LONGTERM-TOP-DOWN` (10:41–11:14) "and then I look at the PD array matrix… I want to define the market in terms of a premium and discount… relative to the PD array matrix and those reference points I will calibrate the levels and come up with key price levels as a result"; (32:21–32:57) the matrix built inside a chosen structural range, "not every price range will have every possible premium and or discount array — I just note the ones that are obvious"; (33:54–35:07) the rounding rule — nearest ten, zero or five level, premium arrays above price rounded down, discount arrays below price rounded up, "I want that low hanging fruit"; (48:44–49:57) the AUDUSD discount set of exactly three arrays, "you're only left with three choices… is this ambiguous? No. It's definitive"; (50:26–50:48) 7380 left alone as a zero level, 7382 would become 7385.
- `ICT-2017-INTERMEDIATE-TOP-DOWN` (07:14–07:43) "next is I break down the PD array matrix on weekly… any PD array that didn't exist in the monthly may now materialize in the weekly chart because you're going to get much more definition"; (18:26–18:51) the same rounding rule restated for the weekly tier.
- `ICT-2017-TOPDOWN-SHORT-TERM` (31:52–32:12) "it's the PD array matrix, where we are in terms of that premium and discount array… everybody asks the same questions — which order block do I buy, which one am I looking at? All that's answered with the PD array matrix. You have to work from the higher timeframe down"; (24:48–25:02) the rounding slide reached for the third time.
- `ICT-2017-INTRADAY-TOP-DOWN` (10:11–10:19) "it's all about the PD array matrix; if you don't use that or understand it, you're not going to be consistent with my stuff — it's simple as that"; (17:12–17:25) "I calibrate those levels from the PD array matrix to the nearest 10 level or 5 level, and we've already seen this slide three other times"; (46:53–47:08) "without understanding the PD array matrix… you will never be consistent with my concepts."
- `ICT-2022-MENTORSHIP-OVERVIEW`, `ICT-2024-MENTORSHIP-MODULE-LIST` — later restatements; the tabular presentation used in this page's *Visual Pattern* is a library convention, not ICT's own format.
