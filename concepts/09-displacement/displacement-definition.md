# Displacement — Definition

**Category:** 09-displacement
**Aliases:** displacement, price imbalance (2016-17 name), higher time frame price displacement
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-LIQUIDITY-VOIDS, ICT-2016-INSTITUTIONAL-SPONSORSHIP, ICT-2016-ORDERBLOCKS, ICT-2022-MENTORSHIP-EP05, ICT-2022-MENTORSHIP-EP06, ICT-2022-MENTORSHIP-EP10, ICT-2022-MENTORSHIP-EP19, ICT-2022-MENTORSHIP-EP24, ICT-2022-MENTORSHIP-EP40
**Tags:** displacement, momentum, foundational

## Definition

Displacement is **a fast, forceful, directional price move**, which ICT treats as the visual signature of institutional/algorithmic intent: "you want to look for this energetic movement lower, that's displacement, where it's really animated" (`ICT-2022-MENTORSHIP-EP05` [20:14]). The term has an earlier, broader 2016-17 sense: an HTF institutional move or the price imbalance it leaves, used near-synonymously with "price imbalance" — "This causes a price imbalance or, as we call it, displacement." (`ICT-2016-LIQUIDITY-VOIDS` [01:54]); "This is higher time frame price displacement. ... That means there is clear evidence that there is a large entity entering the marketplace." (`ICT-2016-INSTITUTIONAL-SPONSORSHIP` [12:10]–[12:13]); "Now we have indications that there has been displacement in the marketplace. That means someone with a whole lot of money and a whole lot of interest wanting to see higher prices is now in play." (`ICT-2016-ORDERBLOCKS` [04:45]–[04:53]). By 2022, ICT teaches it at the single-candle level and ties the term explicitly to a quality judgment, not a geometric formula.

## Formal Criteria

ICT's quality test is **binary and verbal**, not a numeric candle-geometry filter:

- Energetic vs. weak: "does it have an energetic break below that? No, it's just a very weak anemic move lower." (`ICT-2022-MENTORSHIP-EP05` [20:40]).
- "it's got to be energetic, it can't be a little lethargic little move" (`ICT-2022-MENTORSHIP-EP06` [19:05]).
- "this little toe in the water type thing here — that's not enough, we want to see it fall in" (`ICT-2022-MENTORSHIP-EP40` [08:56]).
- "melted, didn't do anything above that oh[ld] low — there was no displacement, no energetic move" (`ICT-2022-MENTORSHIP-EP24` [23:30]; the caption's "oh" is the tail of "old," confirmed by the preceding line: "it's got to trade back above this old low," EP24 [22:52]).
- A loose visual description of the move's volume sitting inside the candle bodies: "the volume of the move is inside the bodies of the candle ... we always allow for some inherent price action with the wicks and the tails" (`ICT-2022-MENTORSHIP-EP19` [15:16]); a closing qualifier is part of the read: "a big beefy bearish candle that closes low below this level" (`ICT-2022-MENTORSHIP-EP06` [21:29]).
- ICT gives **no** percentage, ratio, or multiple-of-average-body threshold for displacement anywhere in either corpus.

## Formula / Math

```
# ICT gives no number for this.
# Displacement is a qualitative, binary judgment: energetic/animated vs.
# lethargic/anemic/weak ("toe in the water"). No body%, wick%, or
# multiple-of-average-body threshold appears in either corpus.

# The FVG is NOT the test for displacement — it is searched for
# AFTER displacement is identified, inside the displacement range
# (see Common Mistakes and fair-value-gap.md).
```

## Machine-Readable

```json
{
  "id": "displacement-definition",
  "category": "09-displacement",
  "aliases": ["displacement", "price-imbalance-2016-17-name"],
  "criteria": [
    {"id": "c1", "expr": "qualitative: energetic/animated, not lethargic/anemic"},
    {"id": "c2", "expr": "numeric_threshold: not given by ICT"},
    {"id": "c3", "expr": "fvg_is_searched_for_inside_displacement_after_the_fact, not a defining test"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["displacement-and-fvg","fair-value-gap","mss","range-expansion","liquidity-void","order-block-criteria"],
  "sources": ["ICT-2016-LIQUIDITY-VOIDS","ICT-2016-INSTITUTIONAL-SPONSORSHIP","ICT-2016-ORDERBLOCKS","ICT-2022-MENTORSHIP-EP05","ICT-2022-MENTORSHIP-EP06","ICT-2022-MENTORSHIP-EP10","ICT-2022-MENTORSHIP-EP19","ICT-2022-MENTORSHIP-EP24","ICT-2022-MENTORSHIP-EP40"]
}
```

## Visual Pattern

```
   energetic / animated (displacement):        lethargic / anemic (NOT displacement):

        ▲                                            ╱╲
       ██                                           ╱  ╲  ← slow, overlapping
       ██   wide, fast, few opposing wicks          ╱    ╲   candles, "toe in
       ██                                                    the water"
```

ICT's description is deliberately qualitative — "energetic," "animated," "a lot of momentum" vs. "lethargic," "weak," "anemic," "melted."

## Timeframes

All TFs ICT trades, M1 through HTF. The 2016-17 "higher time frame price displacement" usage is specifically about large, HTF institutional moves; the 2022 usage is taught on intraday charts (15-minute, with 1–5-minute drill-downs in the ep05/ep06/ep10 examples; ep24's worked example is itself on a 5-minute chart).

## Examples

**Example 1 — displacement confirmed, no numeric test applied (2022):**
- Price takes out a short-term low, then runs down with a close below that level: "how do you know it's displacement — how it closes down here below that low" (`ICT-2022-MENTORSHIP-EP06` [20:58]).
- ICT then hunts a fair value gap **inside** that displacement range for a trade; absence of displacement ("melted," EP24 [23:30]) rules out the setup before any FVG search begins.

**Example 2 — 2016-17 "higher time frame price displacement":**
- A large-entity HTF move leaves a clear imbalance. ICT reads this as institutional sponsorship evidence (`ICT-2016-INSTITUTIONAL-SPONSORSHIP` [12:10]–[12:52]), not as a single-candle geometry test.

## Common Mistakes

- **Citing a body%, wick%, or multiple-of-average-body number as ICT's displacement filter.** No such figures exist in either corpus; the judgment is verbal (energetic/animated vs. lethargic/anemic/weak).
- **Treating "leaves an FVG" as the definition or operational test of displacement, in either direction.** ICT's order is the reverse: displacement is judged first (by its energetic/closing character), and the FVG is then searched for *inside* the displacement range as a trade-entry gate — "once you see that, then you have a trade idea being birthed; you don't have a trade entry yet until you determine if it has a fair value gap" (`ICT-2022-MENTORSHIP-EP06` [23:55]); "if there isn't one there, you don't have a trade" ([24:25]). A shift/displacement can occur with **no** FVG and still be valid displacement (see [mss](../01-market-structure/mss.md)).
- **Ignoring the 2016-17 "price imbalance" sense.** Early material uses "displacement" for an HTF institutional move or the imbalance it causes, not for a single-candle geometric test.

## Related Concepts

- [displacement-and-fvg](displacement-and-fvg.md) — the FVG-inside-displacement trade-entry sequence.
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [mss](../01-market-structure/mss.md), [range-expansion](../01-market-structure/range-expansion.md), [liquidity-void](../02-liquidity/liquidity-void.md), [order-block-criteria](../07-order-blocks/order-block-criteria.md).

## Citations

- `ICT-2016-LIQUIDITY-VOIDS` [01:54] — "price imbalance or, as we call it, displacement" (Dec 2016).
- `ICT-2016-INSTITUTIONAL-SPONSORSHIP` [12:10]–[12:52] — "higher time frame price displacement," large-entity evidence (Nov 2016).
- `ICT-2016-ORDERBLOCKS` [04:45]–[04:53] — "indications that there has been displacement in the marketplace" (Dec 2016).
- `ICT-2022-MENTORSHIP-EP05` [20:14]–[20:40] — "energetic movement," weak/anemic contrast.
- `ICT-2022-MENTORSHIP-EP06` [19:05], [20:58], [21:29], [23:55], [24:25] — energetic/lethargic test; FVG hunted inside displacement, after the fact.
- `ICT-2022-MENTORSHIP-EP10` [37:15]–[37:43] — displacement without an FVG is still valid.
- `ICT-2022-MENTORSHIP-EP19` [15:16] — volume inside bodies, wicks/tails allowed.
- `ICT-2022-MENTORSHIP-EP24` [23:30] — "melted ... no displacement, no energetic move."
- `ICT-2022-MENTORSHIP-EP40` [08:56] — "toe in the water" vs. meaningful displacement.
