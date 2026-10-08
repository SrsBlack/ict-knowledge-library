# Fair Value Gap (FVG)

**Category:** 06-fair-value-gaps
**Aliases:** FVG, 3-candle imbalance, gap, fair value gap, ICT FVG
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FVG-REINFORCED, ICT-2016-REINFORCING-LIQUIDITY, ICT-2016-FAIR-VALUATION, ICT-2016-NO-FEAR-LOSING, ICT-2016-GROWING-SMALL-ACCOUNTS, ICT-2016-MMT-HEAD-SHOULDERS, ICT-2022-MENTORSHIP-EP02, ICT-2022-MENTORSHIP-EP03, ICT-2022-MENTORSHIP-EP06, ICT-2022-MENTORSHIP-EP16, ICT-2022-MENTORSHIP-EP18, ICT-2022-MENTORSHIP-EP20, ICT-2017-HTF-PD-ARRAYS
**Tags:** fvg, imbalance, foundational, pd-array

⚠ **Edited 2026-10-08 per the fair-value-gaps cluster audit.** Previously sourced only to the
stub `ICT-2016-FVG-INTRO`, with "Year Refined: 2025" resting on the stub IDs
`ICT-2024-FVG-CLASSIFICATION` / `ICT-2025-CE-PRIMARY-ENTRY`. Re-sourced to the evidenced Dec-2016
packets and 2022 Mentorship episodes below. Displacement was removed as a formal criterion — it
was never part of ICT's geometric definition (see Common Mistakes). "FVGs are ICT's most-cited
PD array and the primary entry zone" was removed: ICT's own Jan-2017 hierarchy lists the order
block before the FVG. Searched both corpora for `immediate rebalance|delayed rebalance`: 0 hits
both; the 2024/2025 classification material is outside this library's corpus and cannot be
verified here — `Year Refined` reverts to 2022, the latest refinement this corpus can confirm.

## Definition

A Fair Value Gap is a **3-candle wick-to-wick imbalance**: on candle n+1 the low trades above
candle n-1's high (bullish), or the high trades below candle n-1's low (bearish), leaving candle
n's range unworked in one direction. ICT's fullest statement of the geometry: "label number one
candle[,] the number two candle is always going to be where the gap resides[,] and then the
number three candle gives you the lower end[;] the upper end of the fair value gap is going to
be the low of candle number one[,] the lower end of the fair value gap is going to be the high of
candle number three" (`ICT-2022-MENTORSHIP-EP06` [16:41]–[17:09]). Identical geometry is taught
in the Dec-2016 mentorship: "we're delineating the low of the previous candle and the high of the
count [candle] to the right of the down candle that creates that little pocket of space"
(`ICT-2016-FVG-REINFORCED` [04:28]); "[the previous candle's] wick and this candle's wick. In
between there price was only delivered on the downside. So we have a fair value gap."
(`ICT-2016-REINFORCING-LIQUIDITY` [07:02]–[07:09]). ICT teaches the algorithm tends to return and
"rebalance" the gap: "[w]e're going to expect price to eventually want to trade back up into that
little gap area" (`ICT-2016-FVG-REINFORCED` [06:15]).

## Formal Criteria

- Three consecutive candles n-1, n, n+1.
- Bullish: `L_{n+1} > H_{n-1}` (wick-to-wick, not close-to-close).
- Bearish: `H_{n+1} < L_{n-1}`.
- The unworked region sits between the two outer wicks; candle n's body owns no boundary.
- Persists until price trades back through it.
- **Displacement on candle n is not part of this geometric definition.** It is a condition of the
  separate 2022 trade *model*, which looks for an FVG only after a displacement move has already
  occurred: "that range between here and here[,] that's displacement... [then] start watching to
  see if it creates a fair value gap" (`ICT-2022-MENTORSHIP-EP06` [20:58]–[21:29]); the model also
  requires price to move away from the FVG before entry — "it has to move away from the fear of a
  gap" (`ICT-2022-MENTORSHIP-EP20` [13:52]). Neither statement tests candle n's own shape. See
  Common Mistakes.

## Formula / Math

```
bullish_FVG(n) := L_{n+1} > H_{n-1}
fvg_low        := H_{n-1}
fvg_high       := L_{n+1}
fvg_size       := fvg_high - fvg_low

bearish_FVG(n) := H_{n+1} < L_{n-1}
fvg_low        := H_{n+1}
fvg_high       := L_{n-1}

# ICT gives no minimum fvg_size and no ATR-style filter anywhere in the corpus — see Common Mistakes.
```

## Machine-Readable

```json
{
  "id": "fair-value-gap",
  "category": "06-fair-value-gaps",
  "aliases": ["FVG", "3-candle-imbalance", "ICT-FVG"],
  "criteria": [
    {"id": "c1", "expr": "bullish: L_{n+1} > H_{n-1}"},
    {"id": "c2", "expr": "bearish: H_{n+1} < L_{n-1}"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["bullish-fvg","bearish-fvg","inversion-fvg","consequent-encroachment","ce-as-primary-entry","balanced-price-range","volume-imbalance","immediate-rebalance-fvg","delayed-rebalance-fvg","fvg-classification-2025","liquidity-void-vs-fvg","fvg-mitigation","nested-fvg","imbalance-definition","displacement-definition"],
  "sources": ["ICT-2016-FVG-REINFORCED","ICT-2016-REINFORCING-LIQUIDITY","ICT-2016-FAIR-VALUATION","ICT-2016-NO-FEAR-LOSING","ICT-2016-GROWING-SMALL-ACCOUNTS","ICT-2016-MMT-HEAD-SHOULDERS","ICT-2022-MENTORSHIP-EP02","ICT-2022-MENTORSHIP-EP03","ICT-2022-MENTORSHIP-EP06","ICT-2022-MENTORSHIP-EP16","ICT-2022-MENTORSHIP-EP18","ICT-2022-MENTORSHIP-EP20","ICT-2017-HTF-PD-ARRAYS"]
}
```

## Visual Pattern

```
   bullish FVG:                            bearish FVG:

         ▲                                    ▼
         █  ← n+1 (low > n-1 high)            ▼  ← n+1 (high < n-1 low)
         █                                    ▼
       ▲                                    █
       █  ← n                                █  ← n
       █                                    █
       █                                    █
     ▲                                    ▼
     █  ← n-1                              ▼  ← n-1
   ▲                                      ▼

   FVG region:                              FVG region:
   [H_{n-1}, L_{n+1}]                       [H_{n+1}, L_{n-1}]
   below n+1, above n-1                     above n+1, below n-1
```

## Timeframes

All TFs. ICT grades FVGs by higher-timeframe parentage, not by size: "[t]he higher time frame
imbalances are going to be parent to the subordinate smaller time frames"
(`ICT-2022-MENTORSHIP-EP18` [34:37]).

## Examples

**Example 1 — bullish M15 FVG, 2022 entry convention:**
- M15 candle n-1 high = 1.0860; candle n+1 low = 1.0865.
- → bullish FVG at [1.0860, 1.0865], 5 pips.
- ICT's stated entry is the near edge, not the midpoint: "the easiest entry would be trading just
  above candle number three's high[;] you can put a limit order right there... place your stop
  right above can[dle] number one or... number two" (`ICT-2022-MENTORSHIP-EP06` [17:09]–[17:38],
  stated for the bearish case; "everything i teach... is reversed the same way" [22:35]).
- A deeper fill toward the midpoint is possible but explicitly optional in the corpus, not
  required — see [consequent-encroachment](consequent-encroachment.md).

## Common Mistakes

- **Body-only FVG as the current rule.** ICT's Dec-2016 and 2022 definitions are wick-to-wick. An
  earlier (Sep-2016) lecture instead says "I define it by the body" (`ICT-2016-FAIR-VALUATION`
  [04:41]–[04:51]), and two Oct–Nov-2016 lectures use "fair value gap" for the order-block
  candle's open-to-high/body region (`ICT-2016-NO-FEAR-LOSING` [02:58]; `ICT-2016-GROWING-SMALL-ACCOUNTS`
  [18:31]–[18:37]; `ICT-2016-MMT-HEAD-SHOULDERS` [08:01]). Treat the body-based reading as an
  early-2016 usage superseded by Dec-2016/2022, not a current alternate rule.
- **Treating displacement as a geometric criterion.** It isn't — see Formal Criteria. Small gaps
  still count: "if you have a fair value gap and a small one right above it anticipate it likely
  trading up into you" (`ICT-2022-MENTORSHIP-EP16` [37:50]).
- **Filtering tiny FVGs by ATR.** No such filter exists in the corpus; ICT trades a 2-pip gap
  directly ("it's only two pips difference, but that creates a what? A gap. So we can be a seller
  at a more refined price level", `ICT-2016-FVG-REINFORCED` [12:37]–[12:42]) and repeatedly works
  "small little" FVGs in 2022. Selection runs on HTF parentage, not size (see Timeframes).
- **Assuming the FVG outranks the order block.** ICT's Jan-2017 PD-array hierarchy lists the
  order block first: "Then you have bearish order block, fair value gap, and then liquidity void,
  bearish breaker, and mitigation block" (`ICT-2017-HTF-PD-ARRAYS` [25:17]).
- **Using BISI / SIBI as 2016- or 2022-era ICT vocabulary.** Zero hits for `bisi|sibi` in either
  corpus. Treat as a later (2023+) label — see [bullish-fvg](bullish-fvg.md) Common Mistakes.

## Related Concepts

- [bullish-fvg](bullish-fvg.md), [bearish-fvg](bearish-fvg.md) — directional variants.
- [inversion-fvg](inversion-fvg.md) — flipped FVG after rebalance + reversal (term and rules unverified in corpus).
- [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md) — CE entry framework.
- [balanced-price-range](balanced-price-range.md) — overlapping bullish + bearish FVG (unverified in corpus).
- [volume-imbalance](volume-imbalance.md) — body-vs-body imbalance variant.
- [immediate-rebalance-fvg](immediate-rebalance-fvg.md), [delayed-rebalance-fvg](delayed-rebalance-fvg.md), [fvg-classification-2025](fvg-classification-2025.md).
- [liquidity-void-vs-fvg](liquidity-void-vs-fvg.md), [fvg-mitigation](fvg-mitigation.md), [nested-fvg](nested-fvg.md).
- [imbalance-definition](../26-imbalance/imbalance-definition.md), [displacement-definition](../09-displacement/displacement-definition.md).

## Citations

- `ICT-2016-FVG-REINFORCED` — "Month 04 — ICT Fair Value Gaps FVG" (Dec 2016). Wick-to-wick
  geometry [04:28]; rebalance expectation [06:15]; a 2-pip gap traded directly [12:37]–[12:42];
  FVG-to-liquidity-void link across timeframes [05:14].
- `ICT-2016-REINFORCING-LIQUIDITY` — "Month 04 — Reinforcing Liquidity Concepts" (Dec 2016).
  Wick-to-wick confirmation [07:02]–[07:09].
- `ICT-2016-FAIR-VALUATION` — "Month 1 — Fair Valuation" (Sep 2016). Body-defined era usage
  [04:41]–[04:51].
- `ICT-2016-NO-FEAR-LOSING` — "Month 02 — No Fear Of Losing" (Oct 2016). Order-block-candle FVG
  usage [02:58].
- `ICT-2016-GROWING-SMALL-ACCOUNTS` — "Month 02 — Growing Small Accounts" (Oct 2016).
  Body-of-candle FVG usage [18:31]–[18:37].
- `ICT-2016-MMT-HEAD-SHOULDERS` — "Month 03 — Market Maker Trap Head & Shoulders" (Nov 2016).
  Midway-point FVG usage [08:01].
- `ICT-2022-MENTORSHIP-EP02` — Year-introduced statement [30:04]; single-candle-pass imbalance
  description [38:14].
- `ICT-2022-MENTORSHIP-EP03` — Single-candle-pass description, mirror statement [13:43]–[14:14].
- `ICT-2022-MENTORSHIP-EP06` — Full 3-candle definition [16:41]–[17:09]; displacement framed as a
  model/search condition, not a candle-n test [20:58]–[21:29].
- `ICT-2022-MENTORSHIP-EP16` — Small FVGs traded directly [37:50].
- `ICT-2022-MENTORSHIP-EP18` — HTF-parent selection rule [34:37].
- `ICT-2022-MENTORSHIP-EP20` — Price must move away from the FVG before entry [13:52].
- `ICT-2017-HTF-PD-ARRAYS` — PD-array hierarchy places the order block before the FVG [25:17].
