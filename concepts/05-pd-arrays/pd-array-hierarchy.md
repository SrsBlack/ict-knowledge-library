# PD Array Hierarchy

**Category:** 05-pd-arrays
**Aliases:** PD array tier ranking, array conviction order, PDA stack
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2017-HTF-PD-ARRAYS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** pd-array, hierarchy, ranking, premium, discount

## Definition

The PD array hierarchy is ICT's **ordered list of the arrays price encounters as it travels from
equilibrium out to an extreme**. It answers one question, asked from wherever price currently sits:
*what is the next array I should expect it to reach?* "I'm putting them in an order of
significance. When you're at equilibrium or if you're moving up from discount, your expectations
are to look for the very first thing you look for in the list as prices going up"
(`ICT-2017-HTF-PD-ARRAYS`, 24:00–24:21).

The list is a **distance ranking**, not a quality ranking: position on it says how deep into
premium or discount the array sits, which is what determines the order of arrival.

## Formal Criteria

**The canonical order, equilibrium → premium** (`ICT-2017-HTF-PD-ARRAYS`, 18:35–19:22, 25:04–25:23).
Price working up from equilibrium meets them bottom-first:

| # | Array (bearish / premium side) | Depth into premium |
|---|---|---|
| 1 | **Mitigation block** | shallowest — first thing encountered |
| 2 | **Bearish breaker** | |
| 3 | **Liquidity void** | |
| 4 | **Fair value gap** | |
| 5 | **Bearish order block** | |
| 6 | **Rejection block** (above the candle *bodies*, not the wicks) | |
| 7 | **Old high / old low** | deepest — "that's as high as you can get" |

Mirror for the discount side: mitigation block → bullish breaker → liquidity void → fair value gap
→ bullish order block → rejection block → old low / old high.

**The breaker precedence rule.** A breaker overrides everything further out on the list: "if
there's a breaker, forget about closing in the void and forget about getting up to that gap
because the breaker is going to take precedence over everything on this list when you're below it
in terms of market price" (24:42–24:52). Also stated as "whenever you see bearish breakers, just
don't expect the bearish order block to be hit" (21:35).

**Old lows can be premium and old highs can be discount.** Position on the list is measured by
distance travelled, not by nominal price: "if you're on a very low end of a downtrend on a higher
timeframe monthly chart, you may be rallying up to an old low. And if it gets to that old low,
even though it's an old low in terms of price, it's really high up in the premium" (23:22–23:42).

**Walking the list is a checklist, not an expectation that all seven exist.** "Where's the nearest
mitigation block? There may not be one. Okay, check that off. Where's the nearest bearish breaker?
There may not be one of those either… The next thing, is there a fair value gap? Again, that might
not exist either. Go to the next thing. Bearish order block. That's probably going to be there"
(19:46–20:39).

Modifiers that raise conviction *within* a type:

- Freshness: unmitigated > mitigated.
- HTF confluence (a level that aligns with a higher-TF array) — see [htf-pd-array-hierarchy](htf-pd-array-hierarchy.md).
- Time-of-day alignment (formed inside or aligned with a killzone).

⚠ **Correction, 2026-08-10.** This page previously listed a different ranking (OB > breaker > FVG >
mitigation block > rejection block > equilibrium > generic level) attributed to
`ICT-2017-CHARTER-OVERVIEW` with no quotation. It is close to inverted against ICT's own taught
order above: he places the mitigation block *first* and the rejection block *outside* the order
block. The list in this section is the one ICT states and walks through on charts in
`ICT-2017-HTF-PD-ARRAYS`.

## Formula / Math

```
# depth rank, equilibrium (0) out to the extreme (7)
depth_rank = {
    mitigation_block : 1,
    breaker          : 2,
    liquidity_void   : 3,
    fair_value_gap   : 4,
    order_block      : 5,
    rejection_block  : 6,
    old_high_old_low : 7,
}

# next expected destination from current price
next_array(price) := min(depth_rank[a] for a in arrays_present
                         if depth_rank[a] > depth_rank_at(price))

# precedence: a breaker caps the excursion
if breaker exists between price and target:
    expected_reach = breaker          # arrays beyond it stay untraded
```

Depth is measured from equilibrium of the dealing range, so an "old low" reached by a long rally is
a premium array despite its nominal price.

## Machine-Readable

```json
{
  "id": "pd-array-hierarchy",
  "category": "05-pd-arrays",
  "aliases": ["PDA-stack", "array-conviction-order"],
  "criteria": [
    {"id": "c1", "expr": "depth order from EQ outward: mitigation_block < breaker < liquidity_void < fair_value_gap < order_block < rejection_block < old_high_old_low"},
    {"id": "c2", "expr": "breaker takes precedence over every array beyond it"},
    {"id": "c3", "expr": "depth measured from equilibrium, not nominal price"},
    {"id": "c4", "expr": "rejection_block is read off candle BODIES, not wicks"},
    {"id": "c5", "expr": "fresh > mitigated"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["pd-array-definition","premium-array","discount-array","pd-array-nesting","htf-pd-array-hierarchy","pd-array-confluence","bullish-order-block","breaker-block","fair-value-gap","liquidity-void","rejection-block","mitigation-block"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2017-HTF-PD-ARRAYS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   range top ─────────────────────  old high / old low        7  deepest premium
           ▓▓  rejection block (above the BODIES)             6
           ▒▒  bearish order block                            5
           ░░  bearish fair value gap                         4
           ▒▒  liquidity void                                 3
           ██  bearish breaker      ← caps the excursion      2
           ▓▓  mitigation block     ← met FIRST               1

   ────── EQ ──────────────────────────────────────────────   0

           ▓▓  mitigation block     ← met FIRST               1
           ██  bullish breaker      ← caps the excursion      2
           ▒▒  liquidity void                                 3
           ░░  bullish fair value gap                         4
           ▒▒  bullish order block                            5
           ▓▓  rejection block (below the BODIES)             6
   range bot ─────────────────────  old low / old high        7  deepest discount

   Price leaving EQ meets 1 first and 7 last.
   If 2 is present, expect 3-7 to stay untraded.
```

## Timeframes

Identical on monthly, weekly and daily — "the same things we just outlined for the monthly is seen
for the weekly, both premium and discount. The same hierarchy in how you would expect to see these
arrays occur in price action, this is the way they are seen. And obviously, the same thing is said
for a daily chart. Nothing's changed" (`ICT-2017-HTF-PD-ARRAYS`, 31:04–31:24). Which TF's arrays
govern is [htf-pd-array-hierarchy](htf-pd-array-hierarchy.md).

## Examples

**Example 1 — walking the list up from equilibrium (`ICT-2017-HTF-PD-ARRAYS`, 19:46–20:39):**
- Price at equilibrium, already moving down from premium; the analyst looks *up* for the reselling
  level.
- Nearest mitigation block? None → check it off.
- Nearest bearish breaker? None → check it off.
- Liquidity void to close in? Not clear → check it off.
- Fair value gap? Not present → check it off.
- Bearish order block? "That's probably going to be there. Chances are it's very strong that it's
  going to be there." → that is the destination.

**Example 2 — a breaker capping the move (`ICT-2017-HTF-PD-ARRAYS`, 21:14–21:41, 28:16–28:30):**
- A bearish breaker sits between price and an unfilled liquidity void higher up.
- Expectation: price reaches the breaker and turns; the void stays open. "If there's a breaker
  below a liquidity void, the liquidity void may stay open, basically. That range may stay open."

## Common Mistakes

- **Reading it as a quality ranking.** It is a *distance* ranking. A mitigation block sitting first
  does not mean it is the weakest array; it means price meets it first.
- **Expecting the order block after a breaker.** The single most consequential rule on the page:
  "whenever you see bearish breakers, just don't expect the bearish order block to be hit… because
  it's going to most likely keep price lower" (`ICT-2017-HTF-PD-ARRAYS`, 21:35–21:44).
- **Requiring all seven arrays.** Most of the list will be absent on any given chart; ICT walks it
  as a checklist and skips what is not there.
- **Drawing the rejection block off the wicks.** It is read off the candle **bodies** — "the
  rejection block would be just above the candle's body, not the wicks" (18:49).
- **Assuming an old high is always premium.** Depth is measured from equilibrium; a rallied-into
  old *low* can be the deepest premium array on the chart.
- **Skipping HTF confluence.** An LTF-only array without HTF support is a low-conviction entry
  regardless of its single-TF position.

## Related Concepts

- [pd-array-definition](pd-array-definition.md), [premium-array](premium-array.md), [discount-array](discount-array.md).
- [pd-array-nesting](pd-array-nesting.md), [pd-array-confluence](pd-array-confluence.md), [htf-pd-array-hierarchy](htf-pd-array-hierarchy.md) — multi-array structures.
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [breaker-block](../08-breaker-blocks/breaker-block.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [liquidity-void](../02-liquidity/liquidity-void.md), [rejection-block](../19-rejection-blocks/rejection-block.md), [mitigation-block](../08-breaker-blocks/mitigation-block.md) — the seven array types in order.
- [htf-daily-candle-entries](../31-models/htf-daily-candle-entries.md) — the entry technique that consumes this list.

## Citations

- `ICT-2017-HTF-PD-ARRAYS` (00:00) — "Welcome back folks, this is lesson 6.1 of the January 2017 ICT Mentorship, Defining High Time Frame PD Arrays"; (02:01) "this teaching is to teach you the hierarchy on the tools that I use for framing the trades"; (18:35–19:22) the premium list in order, rejection block above the bodies; (19:46–20:39) walking the checklist; (20:41–21:03) "a mitigation block is going to be first considered before you get to the bearish order block… mitigation blocks can occur lower than breakers"; (21:14–21:44) the breaker precedence rule; (23:22–23:42) old lows as premium; (25:04–25:23) the depth ordering restated; (26:53–28:30) the discount-side mirror; (31:04–31:24) identical on monthly, weekly and daily.
- `ICT-2017-CHARTER-OVERVIEW` — array types taught across the 2017 charter material.
- `ICT-2022-MENTORSHIP-OVERVIEW` — the same arrays re-taught for entry selection in the 2022 season.
