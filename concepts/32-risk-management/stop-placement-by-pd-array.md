# Stop Placement by PD Array

**Category:** 32-risk-management
**Aliases:** structural SL, PD-array SL, invalidation-based SL
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2016-ORDERBLOCKS, ICT-2016-MITIGATE-LOSING-TRADES, ICT-2017-DAYTRADE-HIGH-PROBABILITY, ICT-2017-HTF-MONEY-MANAGEMENT, ICT-2017-SWING-REDUCE-RISK, ICT-2016-EQUILIBRIUM-PREMIUM, ICT-2017-OTE, ICT-2020-OTE-VOL01, ICT-2021-OTE-SCALPING-EXERCISE, ICT-2022-MENTORSHIP-EP06, ICT-2022-MENTORSHIP-EP07, ICT-2022-MENTORSHIP-EP12, ICT-2022-MENTORSHIP-EP13, ICT-2022-MENTORSHIP-EP22, ICT-2022-MENTORSHIP-EP25, ICT-2022-MENTORSHIP-EP38, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** risk, sl, pd-array, foundational

## Definition

⚠ **Rewritten 2026-10-08 after a primary-source audit found three table rows CONTRADICTED and one buffer figure invented.** See per-row corrections below; nothing in the old table should be trusted without checking against this version.

ICT teaches **structural SL placement**: the SL sits beyond the **PD array's invalidation level**, not at a level chosen independently of structure. But "structural" does not mean "tight," and it is **era-split**, not a single fixed-pip-vs-structure dichotomy:

- **2022 (structural, by PD array):** the stop sits beyond the array's own extreme — "where's your stop? Above this candle's high" for a bearish order block (`ICT-2022-MENTORSHIP-EP12`, 42:53); "my stop-loss must remain below this candle's low because it can dig into that candle, because it's going to act as a order block" (`ICT-2022-MENTORSHIP-EP13`, 25:05); "below the bullish order block is the location of a relatively safe stop loss placement" (`ICT-2016-ORDERBLOCKS`, 01:53).
- **2017 day-trade rules (structural reference + flat setup-keyed buffer):** ICT still references structure ("under the lowest low of the day," "below that low") but attaches a flat pip count rather than an array-specific distance — "your stop has to be 30 pips below that low. If you're trading the first retracement into a bullish order block, you have to be 10 pips under the lowest low of the day" (`ICT-2017-DAYTRADE-HIGH-PROBABILITY`, 15:15–15:19); mirrored on the sell side, "10 pips above the highest high of the day" (24:37); and a catch-all, "any other setup… 50% of the average daily range of the last five days" (15:58). `ICT-2017-HTF-MONEY-MANAGEMENT` gives a similar flat rule of thumb for intraday stops — "30 pips is a general rule of thumb, but about 35 pips is about the number one go-to number for me" (15:45).

A reader should not present either branch as *the* rule, and should not assume "structural" is always tighter — see Common Mistakes.

## Formal Criteria

SL placement by structure type. Every row below was checked against a primary-source quote on 2026-10-08; three were previously wrong and are marked:

| Structure | Bullish setup SL | Bearish setup SL | Status |
|---|---|---|---|
| Bullish OB | Below OB low (or wick low) | — | CONFIRMED |
| Bearish OB | — | Above OB high (or wick high) | CONFIRMED |
| FVG | **Above/below the candle that CREATES the gap** (the displacement candle's own extreme, or the swing extreme it created) — NOT the FVG's near/far edge | same, mirrored | ⚠ CORRECTED (see below) |
| OTE entry | **At the leg-origin extreme (fib 1.0), exactly** — never referenced to 0.79 | same, mirrored | ⚠ CORRECTED (see below) |
| Liquidity sweep entry | Below the sweep low, by a buffer that is **era-split** (not a fixed 2–5 pips) | same, mirrored | ⚠ CORRECTED (see below) |
| Bullish/bearish breaker | — | — | NOT IN CORPUS as a stop rule; no source states where a breaker's invalidation sits |

**FVG — corrected.** The taught invalidation is the candle that *created* the imbalance, which sits beyond the gap's own edge, not at it: "your stop loss if you're entering in this fair value got, your stop has to be above the very minimum the candle that creates the fair value gap" (`ICT-2022-MENTORSHIP-EP22`, 17:30); "where would your stop loss be? It would have to be at least above the candle that creates the fair[value] gap" (`ICT-2022-MENTORSHIP-EP25`, 41:46). In the standard three-candle FVG (candle 1 / candle 2 / candle 3), ICT offers two options: "place your stop right above can[dle] number one, or you can put it above candle number two" (`ICT-2022-MENTORSHIP-EP06`, 17:09–17:38) — candle 2 is the displacement candle whose range creates the gap (the tighter option); candle 1 is the swing extreme before it (the wider option). A separate worked example makes the same choice explicit with the roles reversed in presentation order: "where's your stop loss going to be? Above the high of candle number two, or you can use above candle number one, which creates a swing high" (`ICT-2022-MENTORSHIP-EP06`, 36:06) — i.e. candle 1 in that chart happens to be the candle that made the swing high. The FVG's own near edge is the *entry* reference (trading at or through the CE), not the invalidation.

**OTE entry — corrected.** No source anywhere in the OTE corpus references the stop to 0.79. ICT states it flatly for the Primer's own worked example — "my stop will be exactly at this low… not 10 pips or five pips below that" (`ICT-2017-OTE`, 12:32–12:39) — and the 2020–21 applied material derives the same stop from the leg-origin extreme, reported as a pip/tick distance. See [ote-overview](../17-optimal-trade-entry/ote-overview.md) and [ote-rules](../17-optimal-trade-entry/ote-rules.md) item 6.

**Liquidity sweep entry — corrected, era-split.** 2022: "that's where your stop would have to be — just below that, maybe one tick" (`ICT-2022-MENTORSHIP-EP07`, 16:04); "stop below the lower low" (`ICT-2022-MENTORSHIP-EP38`, 42:52). 2017 turtle-soup rule is a flat count instead: "your stop has to be 30 pips below that if you're buying that as a turtle suit" (`ICT-2017-DAYTRADE-HIGH-PROBABILITY`, 15:49).

**Breaker — not in corpus.** Searched both corpora for "breaker" near "stop": no source states where a breaker block's invalidation sits. Do not infer one by analogy to OB.

**Buffer size — era-split, no single number.** ⚠ *Corrected 2026-10-08: "always 2–5 pips" was invented; removed.* ICT's stated buffers span a wide range depending on era and instrument:
- 2022, tightest: "one tick, two ticks above that, that's sufficient enough" (`ICT-2022-MENTORSHIP-EP25`, 43:39); "that's where your stop would have to be — just below that, maybe one tick" (`ICT-2022-MENTORSHIP-EP07`, 16:04); "risk a stop one pip above the highest high of that candle" (`ICT-2017-SWING-REDUCE-RISK`, 23:36). *(Corrected 2026-10-08: this list previously cited `ICT-2022-MENTORSHIP-EP06` 35:31 — "just go one tick above that and removes all the doubt" — as a stop buffer. That line is about where to place the **entry** limit in a different worked example, not the stop; removed from here and from the FVG paragraph above.)*
- 2016, spread-sized: "you got at least 4 pips below that for spread to take you out" (`ICT-2016-EQUILIBRIUM-PREMIUM`, 20:49).
- 2017 day-trade, flat setup-keyed counts: 10, 30, or 40 pips depending on setup type (`ICT-2017-DAYTRADE-HIGH-PROBABILITY`, 15:15–25:06); 30–35 pips as an intraday rule of thumb (`ICT-2017-HTF-MONEY-MANAGEMENT`, 15:45).

A reader must state which convention is in use; "2–5 pips" is not a figure ICT gives.

## Formula / Math

```
sl_for_long = pd_array_invalidation_low - buffer
sl_for_short = pd_array_invalidation_high + buffer

# buffer is NOT a fixed 2-5 pips (see above) — state the convention:
#   2022 tight convention:   buffer = 1-2 ticks (1-2 pipettes on FX)
#   2016 spread convention:  buffer = ~4 pips
#   2017 day-trade rules:    buffer = 10 / 30 / 40 pips, keyed to setup type

# Example: bullish OB body 1.0820-1.0830, OB candle wick low 1.0815,
# using the 2022 tight convention (ICT's stated unit is 1-2 ticks, i.e.
# pipettes on FX; shown here rounded to a 1-pip buffer for simplicity):
# SL = 1.0815 - 1 pip = 1.0814
```

## Machine-Readable

```json
{
  "id": "stop-placement-by-pd-array",
  "category": "32-risk-management",
  "aliases": ["structural-SL", "PD-array-SL", "invalidation-based-SL"],
  "criteria": [
    {"id": "c1", "expr": "SL = pd_array_invalidation +/- buffer"},
    {"id": "c2", "expr": "buffer size is era-split (1-2 ticks / ~4 pips / 10-40 pips), NOT a fixed 2-5 pips"},
    {"id": "c3", "expr": "FVG SL = beyond the displacement candle's own extreme, NOT the FVG's near/far edge"},
    {"id": "c4", "expr": "OTE SL = leg_origin_extreme (fib 1.0), exactly — never referenced to 0.79"},
    {"id": "c5", "expr": "sweep-entry SL is era-split: ~1 tick (2022) vs a flat 30-pip count (2017 turtle soup)"},
    {"id": "c6", "expr": "breaker invalidation level: NOT IN CORPUS"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["risk-per-trade","r-multiple","position-sizing","fair-value-gap","bullish-order-block","breaker-block","mean-threshold","ce-as-primary-entry","ote-overview","ote-rules"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2016-ORDERBLOCKS","ICT-2016-MITIGATE-LOSING-TRADES","ICT-2017-DAYTRADE-HIGH-PROBABILITY","ICT-2017-HTF-MONEY-MANAGEMENT","ICT-2017-SWING-REDUCE-RISK","ICT-2016-EQUILIBRIUM-PREMIUM","ICT-2017-OTE","ICT-2020-OTE-VOL01","ICT-2021-OTE-SCALPING-EXERCISE","ICT-2022-MENTORSHIP-EP06","ICT-2022-MENTORSHIP-EP07","ICT-2022-MENTORSHIP-EP12","ICT-2022-MENTORSHIP-EP13","ICT-2022-MENTORSHIP-EP22","ICT-2022-MENTORSHIP-EP25","ICT-2022-MENTORSHIP-EP38","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish OB SL placement (confirmed):

   OB body  ─── 1.0830 (top, MT 1.0825)
            ─── 1.0820 (bottom of body)
            ─── 1.0815 (OB candle wick low) ← SL reference
                                              ↓
                                              SL = 1.0814 (1-pip buffer below wick low,
                                                            2022 tight convention)

   bullish FVG SL placement (corrected 2026-10-08):

   candle 1 ─┐
             │ gap (the tradable zone / CE)
   candle 2 ─┤  ← entry near here (CE), NOT the SL reference
             │
   candle 3 ─┘
   candle 2's low ──────────────────────  ← tighter SL option: the DISPLACEMENT
                                            candle's own extreme (the candle
                                            whose range creates the gap)
   candle 1's low ──────────────────────  ← wider SL option: the SWING-EXTREME
                                            candle before the displacement
   Neither option is the FVG's own near/far edge.
```

## Timeframes

All TFs.

## Examples

**Example 1 — structural SL on bullish OB (confirmed):**
- Setup: bullish OB body 1.0820–1.0830, OB candle wick low 1.0815.
- Entry at MT 1.0825.
- SL: 1.0815 − 1 pip (2022 tight convention) = 1.0814.
- Risk = 11 pips.

**Example 2 — structural SL on bullish FVG, corrected 2026-10-08:**
- Three-candle FVG: candle 1's low (swing extreme, earlier) = 1.0855, candle 2's low (the displacement candle, later — its low sits higher as the up-move is already underway) = 1.0858, gap 1.0860–1.0866, CE 1.0863.
- Entry at or near CE, 1.0863.
- Tighter SL: candle 2's low, 1.0858, minus a 1-pip buffer ≈ 1.0857 — **6 pips** risk. Wider SL: candle 1's low, 1.0855, minus a 1-pip buffer ≈ 1.0854 — **9 pips** risk. "Whichever one you can afford" (`ICT-2022-MENTORSHIP-EP06`, 36:06). **Neither** is "below the FVG low" (1.0860 − buffer), which this page previously taught.
- Both options are wider than, or at least no narrower than, the old (wrong) FVG-edge stop would have been, because the real invalidation sits one or two candles back from the gap's own edge. *(Corrected 2026-10-08: the prior draft had candle 2 farther from entry than candle 1, which inverted the tighter/wider labels. Fixed by raising candle 2's low above candle 1's — consistent with candle 2 occurring later in an upward displacement.)*

## Common Mistakes

- **Treating structural SLs as always tighter than fixed-pip ones.** ⚠ *Corrected 2026-10-08:* 2022's emphasis runs the other way — "oh but ICT, that's a lot, that's a big stop — well, look how volatile it is, you want to be knocked out of the trade prematurely [if it's too tight]" (`ICT-2022-MENTORSHIP-EP22`, 18:00); Vol.01 on OTE: "not jamming it up too tight and not giving the market room to breathe" (`ICT-2020-OTE-VOL01`, 53:14–53:19). A structural stop can be wider than a flat fixed-pip one.
- **No buffer.** Pixel-precise SLs at exact PD-array invalidation get wicked out on routine noise.
- ⚠ **Using "2–5 pips" as the buffer.** That figure was invented; removed 2026-10-08. State the actual convention — 1–2 ticks (2022), ~4 pips for spread (2016), or 10/30/40 pips (2017 day-trade rules) — see Definition.
- ⚠ **Wrong FVG invalidation reference.** The taught stop is beyond the candle that *creates* the gap (the displacement candle, or the swing extreme it produced) — not the FVG's own near/far edge. This page previously taught "below the FVG low," which is one candle short of the real invalidation.
- ⚠ **Referencing an OTE stop to 0.79.** The taught OTE stop is the leg-origin extreme, exactly — see [ote-overview](../17-optimal-trade-entry/ote-overview.md).
- **Inferring a breaker stop by analogy to OB.** No source states one; don't invent it.

## Related Concepts

- [risk-per-trade](risk-per-trade.md), [r-multiple](r-multiple.md), [position-sizing](position-sizing.md).
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [breaker-block](../08-breaker-blocks/breaker-block.md), [mean-threshold](../27-equilibrium/mean-threshold.md), [ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md).
- [ote-overview](../17-optimal-trade-entry/ote-overview.md), [ote-rules](../17-optimal-trade-entry/ote-rules.md) — the OTE stop this page's table row now matches.

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.

Added 2026-10-08 (full rewrite — table corrections, buffer figures, Year Introduced):

- `ICT-2016-ORDERBLOCKS` (01:53) "below the bullish order block is the location of a relatively safe stop loss placement"; (10:44) "your protective sell stop is going to be below the bullish order blocks low or below the close" — Year Introduced correction (Dec-2016, not 2017).
- `ICT-2016-MITIGATE-LOSING-TRADES` (04:49) "our stop loss is going to actually be below the order block that we're framing our trade around."
- `ICT-2017-DAYTRADE-HIGH-PROBABILITY` (15:15–15:19) "your stop has to be 30 pips below that low. If you're trading the first retracement into a bullish order block, you have to be 10 pips under the lowest low of the day"; (15:49) turtle-soup 30-pip stop; (15:58) "50% of the average daily range of the last five days" catch-all; (24:37) bearish-OB mirror, "10 pips above the highest high of the day."
- `ICT-2017-HTF-MONEY-MANAGEMENT` (15:45) "30 pips is a general rule of thumb, but about 35 pips is about the number one go-to number for me."
- `ICT-2017-SWING-REDUCE-RISK` (23:36) "we're going to risk a stop one pip above the highest high of that candle."
- `ICT-2016-EQUILIBRIUM-PREMIUM` (20:49) "you got at least 4 pips below that for spread to take you out."
- `ICT-2017-OTE` (12:32) the OTE leg-origin stop, exactly; see [ote-overview](../17-optimal-trade-entry/ote-overview.md).
- `ICT-2021-OTE-SCALPING-EXERCISE` (14:03–14:27) the leg-origin-plus-5-pips OTE stop formulation.
- `ICT-2022-MENTORSHIP-EP06` (17:09–17:38) FVG stop above the candle that creates the gap — "place your stop right above can[dle] number one, or you can put it above candle number two"; (36:06) the companion worked example, "above the high of candle number two, or you can use above candle number one, which creates a swing high." *(35:31's "just go one tick above that" is removed from this citation — it is about the entry limit in a different worked example, not the stop; see the Definition's buffer-list correction.)*
- `ICT-2022-MENTORSHIP-EP07` (16:04) sweep-entry stop, "maybe one tick."
- `ICT-2022-MENTORSHIP-EP12` (42:53) bearish OB stop, "above this candle's high."
- `ICT-2022-MENTORSHIP-EP13` (25:05) bullish OB stop, "below this candle's low."
- `ICT-2022-MENTORSHIP-EP22` (17:30) FVG stop, "above the very minimum the candle that creates the fair value gap"; (18:00) wide-stop-is-sometimes-correct remark.
- `ICT-2022-MENTORSHIP-EP25` (41:46) FVG stop; (43:39) "one tick, two ticks above that, that's sufficient enough."
- `ICT-2022-MENTORSHIP-EP38` (42:52) sweep-entry stop, "below the lower low."
- `ICT-2020-OTE-VOL01` (53:14–53:19) "not jamming it up too tight and not giving the market room to breathe" — cited in Common Mistakes above, added to header/JSON 2026-10-08 after being quoted without a formal source entry.
