# Equilibrium — Definition

**Category:** 27-equilibrium
**Aliases:** EQ, equilibrium price, mid-range, fair price, 50% level
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-EQUILIBRIUM-DISCOUNT, ICT-2016-EQUILIBRIUM-PREMIUM, ICT-2017-HTF-PD-ARRAYS, ICT-2016-MITIGATION-BLOCKS, ICT-2017-MILLION-DOLLAR-SWING, ICT-2017-FILLING-NUMBERS, ICT-2016-ELEMENTS-OF-A-TRADE-SETUP, ICT-2022-MENTORSHIP-EP10, ICT-2022-MENTORSHIP-EP11, ICT-2022-MENTORSHIP-EP41
**Tags:** equilibrium, eq, foundational

## Definition

Equilibrium (EQ) is the **50% midpoint of any reference range** — a dealing range, a swing leg, or a void — and functions as ICT's algorithmic "fair price": above EQ is premium, below is discount. "Equilibrium is a midway point of a price move." (`ICT-2016-EQUILIBRIUM-DISCOUNT` [10:26]); "That is all equilibrium is, is 50% on the FIB, that is how I am describing it." (`ICT-2016-EQUILIBRIUM-PREMIUM` [03:57]); "In between these two reference points, the halfway point, this is always going to be referred to as equilibrium." (`ICT-2017-HTF-PD-ARRAYS` [18:01]); "here's 50, that's equilibrium" (`ICT-2022-MENTORSHIP-EP11` [01:27]).

## Formal Criteria

For any reference range bounded by `top` and `bot`:

- `EQ = (top + bot) / 2` — the geometric midpoint.
- Premium half = `(EQ, top]`: "Premium is defined by it has to be above the equilibrium price point or 50% level" (`ICT-2016-EQUILIBRIUM-PREMIUM` [09:28]); "above equilibrium is what the premium market" (`ICT-2022-MENTORSHIP-EP10` [04:00]).
- Discount half = `[bot, EQ)`: "Anything below equilibrium or 50% level is viewed as a discount." (`ICT-2016-EQUILIBRIUM-DISCOUNT` [18:26]); "Below 50% is a discount market" (EP10 [04:00]).
- ICT gives no numeric tolerance band around EQ in either corpus — treat EQ as an exact level, not a zone with a stated width.

EQ is computed for:

- The current dealing range (most common usage).
- An individual swing leg: "Equilibrium, or half of the impulse price swing, has to be at least touched" (`ICT-2016-EQUILIBRIUM-PREMIUM` [03:12]).
- A liquidity void: "Here's a mean threshold of the liquidity void." (`ICT-2016-MITIGATION-BLOCKS` [13:20]) — the 2016 name for a void's midpoint is **mean threshold**, not "consequent encroachment" (see Common Mistakes).
- A monthly/HTF range: "that range divided in half would give you a new equilibrium price point" (`ICT-2017-MILLION-DOLLAR-SWING` [26:41]).
- A "flout" (liquidity pool range): "shorting above the flout['s, ASR 'flouts'] equilibrium or 50% of the range" (`ICT-2017-FILLING-NUMBERS` [11:53]–[11:59]).

Note the 2016 teaching also waits for the swing itself to confirm before measuring: "As soon as we get three candles, then and only then will we start watching for price to come down to the equilibrium price point." (`ICT-2016-EQUILIBRIUM-DISCOUNT` [11:00]).

## Formula / Math

```
EQ(range) = (top(range) + bot(range)) / 2

dealing_range_EQ = (dealing_range_high + dealing_range_low) / 2   # see dealing-range.md
swing_leg_EQ      = (leg_start + leg_end) / 2
liquidity_void_EQ = (void_high + void_low) / 2                     # ICT's "mean threshold of the liquidity void"
```

ICT gives no `±ε` tolerance figure for an "equilibrium zone" in either corpus — EQ is a precise level in his own examples, not a banded zone.

## Machine-Readable

```json
{
  "id": "equilibrium-definition",
  "category": "27-equilibrium",
  "aliases": ["EQ", "equilibrium-price", "mid-range", "fair-price", "50-percent-level"],
  "criteria": [
    {"id": "c1", "expr": "EQ == (range_top + range_bot) / 2"},
    {"id": "c2", "expr": "applies_to_any_reference_range == true"},
    {"id": "c3", "expr": "tolerance_band: not given by ICT"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["mean-threshold","pd-array-definition","premium-array","discount-array","dealing-range"],
  "sources": ["ICT-2016-EQUILIBRIUM-DISCOUNT","ICT-2016-EQUILIBRIUM-PREMIUM","ICT-2017-HTF-PD-ARRAYS","ICT-2016-MITIGATION-BLOCKS","ICT-2017-MILLION-DOLLAR-SWING","ICT-2017-FILLING-NUMBERS","ICT-2016-ELEMENTS-OF-A-TRADE-SETUP","ICT-2022-MENTORSHIP-EP10","ICT-2022-MENTORSHIP-EP11","ICT-2022-MENTORSHIP-EP41"]
}
```

## Visual Pattern

```
   range_top ────────────  premium half
                █▒▒
                █▒▒  ← short PD arrays here
   ───────────────── EQ (50% midpoint)  ← decision pivot
                ░░
                ░░  ← long PD arrays here
   range_bot ────────────  discount half
```

## Timeframes

All TFs. ICT applies EQ from a monthly range (`ICT-2017-MILLION-DOLLAR-SWING` [26:41]) down to a single swing leg.

## Examples

**Example 1 — daily EQ as decision pivot:**
- Daily dealing range high/low measured; EQ = midpoint.
- Price below EQ → discount; bullish-bias setups valid here (`ICT-2022-MENTORSHIP-EP10` [04:00]).

**Example 2 — EQ on a void (mean threshold):**
- A liquidity void's own 50% level is its mean threshold, used as a target: "ultimately reaches down into our mean threshold of the liquidity void" (`ICT-2016-MITIGATION-BLOCKS` [14:40]).

**Example 3 — EQ as part of a multi-confluence OTE setup:**
- "is there a short term shift in market structure, yes; is there a gap, yes; ... that would be a 62 to 70 [re]tracement level less than equilibrium relative to the high and the low respectively" (`ICT-2022-MENTORSHIP-EP41` [18:21]).

## Common Mistakes

- **Using a stale range.** When the dealing range is re-measured (see [dealing-range](../05-pd-arrays/dealing-range.md)), EQ must be recomputed.
- **EQ-only entries.** EQ is a decision pivot, not a high-conviction entry by itself: "The order block that the market makers leave near or at the equilibrium price point" is what ICT actually looks for there (`ICT-2016-ELEMENTS-OF-A-TRADE-SETUP` [11:13]).
- **Citing "consequent encroachment" as ICT's name for an FVG's midpoint.** 0 hits in either corpus. ICT's 2016 name for a void's own 50% level is **mean threshold** (`ICT-2016-MITIGATION-BLOCKS` [13:20]), not "consequent encroachment" — that phrase is plausibly later/community vocabulary and is not attributed to ICT here.
- **Citing a numeric `±ε` tolerance band ("a few pips") around EQ as ICT's.** No such figure appears in either corpus.

## Related Concepts

- [mean-threshold](mean-threshold.md) — ICT's own name for a void's/order block's midpoint; related but not identical usage to dealing-range EQ.
- [pd-array-definition](../05-pd-arrays/pd-array-definition.md), [premium-array](../05-pd-arrays/premium-array.md), [discount-array](../05-pd-arrays/discount-array.md), [dealing-range](../05-pd-arrays/dealing-range.md).

## Citations

- `ICT-2016-EQUILIBRIUM-DISCOUNT` [10:24]–[11:09], [18:26] — midway-point definition; discount defined; 3-candle confirmation wait.
- `ICT-2016-EQUILIBRIUM-PREMIUM` [03:12], [03:57], [09:28] — "50% on the FIB"; premium defined; impulse-swing EQ.
- `ICT-2017-HTF-PD-ARRAYS` [18:01] — "the halfway point ... always going to be referred to as equilibrium" (Jan 2017).
- `ICT-2016-MITIGATION-BLOCKS` [10:25], [13:20], [14:40] — EQ of a liquidity void, named "mean threshold."
- `ICT-2017-MILLION-DOLLAR-SWING` [26:41] — EQ on a monthly range (Feb 2017).
- `ICT-2017-FILLING-NUMBERS` [11:53]–[11:59] — EQ of a flout/liquidity-pool range (May 2017).
- `ICT-2016-ELEMENTS-OF-A-TRADE-SETUP` [11:13] — EQ paired with an order block, not traded alone.
- `ICT-2022-MENTORSHIP-EP10` [04:00] — premium/discount above/below 50%.
- `ICT-2022-MENTORSHIP-EP11` [01:27] — EQ inside a dealing range, worked example.
- `ICT-2022-MENTORSHIP-EP41` [18:21] — EQ as one factor in a multi-confluence OTE setup.
