# Gap Classification

**Category:** 09-displacement
**Aliases:** gap taxonomy, gap types, FVG vs VI vs liquidity-void
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-VACUUM-BLOCK, ICT-2016-LIQUIDITY-VOIDS, ICT-2016-FVG-REINFORCED, ICT-2016-REINFORCING-LIQUIDITY, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** displacement, gap, classification

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2018` sourced
only to the generic `ICT-2017-DISPLACEMENT` and `ICT-2022-MENTORSHIP-OVERVIEW` placeholders. The
**December-2016** mentorship lecture *ICT Vacuum Block* classifies gaps by role in the trend — "in
summary, **a vacuum block is nothing more than a breakaway gap**" [12:48] and "this could
potentially be an **exhaustion gap**. An exhaustion gap is typically a graphic depiction of
capitulation" [02:57] (`ICT-2016-VACUUM-BLOCK`). The same month's *Liquidity Voids* names the
**common gap** [12:37] and *ICT Fair Value Gaps FVG* refers forward to "fair value gaps and
**breakaway gaps** and **measuring gaps**" [08:36]. Re-dated to 2016.

⚠ **Factual correction 2026-08-10.** This page previously asserted that the FVG / VI / liquidity-void
triad *is* "the three primary types of price gaps that ICT teaches". The corpus contradicts that:
ICT's own named gap taxonomy in the Dec-2016 lectures is the classical **common / breakaway /
measuring / exhaustion** set (citations above). The FVG / VI / void triad is a **geometric**
disambiguation used by this library, not ICT's own gap classification, and the two taxonomies are
orthogonal — they classify different things (shape vs. role in the trend). Both are documented
below.

## Definition

Gap Classification covers **two orthogonal taxonomies** of unworked price regions.

**(1) By geometry** — this library's structural disambiguation between **Fair Value Gap (FVG)**, **Volume Imbalance (VI)**, and **Liquidity Void**. Each is a different geometric form of an unworked price region; conflating them produces sloppy analysis. This is the cross-reference disambiguation between the displacement-side framing of these concepts (here in `09-displacement`) and the FVG-/imbalance-side framings elsewhere in the library.

**(2) By role in the trend** — ICT's own named gap classes, taught in Dec 2016: **common gap** (an ordinary close-to-open body gap, expected to fill), **breakaway gap** (the vacuum block; marks initiation and may deliberately stay open), **measuring gap** (mid-move), and **exhaustion gap** (capitulation at the end of a run). A single gap carries one label from each taxonomy — e.g. a vacuum block is geometrically a body gap and, by role, a breakaway gap.

## Formal Criteria

### Taxonomy 1 — by geometry

The three gap types:

| Type | Geometry | Time scope | File |
|---|---|---|---|
| **FVG** | 3-candle wick non-overlap (`L_{n+1} > H_{n-1}`) | 3 candles | [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) |
| **Volume Imbalance** | body-vs-body gap (open(n) ≠ close(n-1)); wicks may overlap | 2 candles | [volume-imbalance](../06-fair-value-gaps/volume-imbalance.md) |
| **Liquidity Void** | multi-candle expansion span with one-sided dominance | 5+ candles | [liquidity-void](../02-liquidity/liquidity-void.md) |

Containment hierarchy:
- A liquidity void typically **contains** one or more FVGs and/or VIs.
- An FVG is the strictest pattern (3-candle wick rule).
- A VI is looser than FVG (allows wick overlap).

### Taxonomy 2 — by role in the trend (ICT's own named classes, Dec 2016)

| Class | What ICT says | Fill expectation |
|---|---|---|
| **Common gap** | "When we see a gap where price has closed from one candle and gaps into another opening of another candle … it creates a common gap" (`ICT-2016-LIQUIDITY-VOIDS`, [12:23–12:37]) | Expected to fill; body-only closure is sufficient ([13:03]) |
| **Breakaway gap** | "A vacuum block is nothing more than a breakaway gap" (`ICT-2016-VACUUM-BLOCK`, [12:48]) | May deliberately stay open — "not all gaps fill completely" ([12:58]); an order block inside the gap can halt the fill ([13:10]) |
| **Measuring gap** | Named alongside FVGs and breakaway gaps (`ICT-2016-FVG-REINFORCED`, [08:36]) | Not developed in the local corpus — see caveat below |
| **Exhaustion gap** | "This could potentially be an exhaustion gap. An exhaustion gap is typically a graphic depiction of capitulation" (`ICT-2016-VACUUM-BLOCK`, [02:57–03:06]) | Marks the last of the momentum in a prolonged trend |

### Gap risk — the position-holder's view of an unfilled gap

ICT names a third framing in the same month, orthogonal to both taxonomies above: not what a gap
*is*, but what it *does to an open position*.

- **Definition:** "gap risk is nothing more than simply when the market **quickly reprices to a level
  where there was very little or no trading**" (`ICT-2016-REINFORCING-LIQUIDITY`, [01:57–02:05]).
- **Both void and FVG carry it:** "when the current trading range is likely to remain, **liquidity
  voids will fill in**, and this is associated with gap risk. And when the current trading range is
  likely to remain, **fair value gaps will also fill in**, and this is attributed to gap risk"
  [01:34–01:57]. Both are listed there as forms of **internal range liquidity**.
- **The recognition cue:** "when we see a liquidity run to close in a range where there's only like
  **one candle, real long candle** — usually that's a gap fill" [02:05–02:14].
- **The exposure:** "whenever you're in a long and you have a **big gap underneath you, that's gap
  risk**. So the market many times will **reprice aggressively** to close in those ranges, and that's
  what you see **stops you out** as a trader" [02:14–02:29].
- **The inversion:** "**we look for them as opportunities**" [02:29–02:31] — the same unfilled region
  is the hazard to a held position and the draw that a new position targets.

⚠ **Measuring gap is under-sourced.** In the 153-packet local corpus the term appears exactly once,
in a forward reference to written study notes ("a lot of information about fair value gaps and
breakaway gaps and measuring gaps that's going to be coming your way in the form of the December
study notes"). No lecture in this corpus defines or works an example of it. Do not quote criteria
for it from this page.

## Formula / Math

```
fvg(n)            := 3-candle wick non-overlap
volume_imbalance(n) := 2-candle body gap (wicks may overlap)
liquidity_void(span)  := multi-candle expansion with directional dominance >= 80%
                          AND contains 1+ nested FVGs typically

# Containment:
liquidity_void ⊇ FVGs (often)
FVG ⊇ implied_VI (always — an FVG implies a body gap exists)
```

## Machine-Readable

```json
{
  "id": "gap-classification",
  "category": "09-displacement",
  "aliases": ["gap-taxonomy", "gap-types"],
  "criteria": [
    {"id": "c1", "expr": "FVG = 3-candle wick non-overlap"},
    {"id": "c2", "expr": "VI = 2-candle body gap (wicks may overlap)"},
    {"id": "c3", "expr": "liquidity_void = multi-candle expansion with directional dominance"},
    {"id": "c4", "expr": "containment: void contains FVGs; FVG implies VI"},
    {"id": "c5", "expr": "orthogonal role taxonomy: common | breakaway | measuring | exhaustion"},
    {"id": "c6", "expr": "gap_risk := an unfilled void or FVG against an open position; the market may reprice aggressively to close it"},
    {"id": "c7", "expr": "gap_risk cue := a range covered by a single long candle is a likely gap fill"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["displacement-definition","displacement-and-fvg","fair-value-gap","volume-imbalance","liquidity-void","liquidity-void-vs-fvg","imbalance-vs-fvg","internal-range-liquidity"],
  "sources": ["ICT-2016-VACUUM-BLOCK","ICT-2016-LIQUIDITY-VOIDS","ICT-2016-FVG-REINFORCED","ICT-2016-REINFORCING-LIQUIDITY","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   gap-type comparison:
   
   FVG (3-candle, wicks no overlap):
        ▲
        █  ← n+1
      ▲
      █  ← n
    ▲
    █  ← n-1
   wicks of n-1 and n+1 do not overlap.
   
   VI (2-candle, body gap, wicks may overlap):
   ▲
   █  ← n: opens above prior close
   O_n
   ───  body gap
   C_{n-1}
   █  ← n-1
   ▼
   wicks may overlap visually.
   
   Liquidity Void (5+ bars, one-sided dominance):
   ▲
   ██
   ██
   ██  ← 6 mostly-green bars
   ██   directional dominance >= 80%
   ██   contains 1-3 nested FVGs
   ██
```

## Timeframes

M5+.

## Examples

**Example 1 — gap-type identification:**
- Setup A: M15 with H_{n-1}=1.0860, L_{n+1}=1.0865 → FVG (5 pips, wick non-overlap).
- Setup B: M15 close 1.0855 next candle opens 1.0860, but wicks overlap at 1.0858 → Volume Imbalance, not FVG.
- Setup C: 6 consecutive H1 green candles, total 80 pips with 8% max pullback, contains 2 FVGs → Liquidity Void containing FVGs.

## Common Mistakes

- **Conflating all gap types as "FVG".** They have specific geometric definitions; mislabeling produces inconsistent analysis.
- **Treating a void as a single FVG.** A void usually contains multiple FVGs; treating the whole void as one FVG misses the precise entry levels.
- **Treating VI as FVG.** VIs are softer references; don't claim FVG-level conviction for VI-only setups.

## Related Concepts

- [displacement-definition](displacement-definition.md), [displacement-and-fvg](displacement-and-fvg.md).
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [volume-imbalance](../06-fair-value-gaps/volume-imbalance.md), [liquidity-void](../02-liquidity/liquidity-void.md), [liquidity-void-vs-fvg](../06-fair-value-gaps/liquidity-void-vs-fvg.md), [imbalance-vs-fvg](../26-imbalance/imbalance-vs-fvg.md).

## Citations

- `ICT-2016-VACUUM-BLOCK` — "Month 04 — ICT Vacuum Block", `shPGUz9pU-A` (Dec 2016). Exhaustion gap defined [02:57–03:06]; breakaway gap equated with the vacuum block [12:48]; "not all gaps fill completely" [12:58].
- `ICT-2016-LIQUIDITY-VOIDS` — "Month 04 — Liquidity Voids", `HTQgH11W37o` (Dec 2016). Liquidity void defined [00:57]; displacement equated with price imbalance [01:54]; common gap named [12:37].
- `ICT-2016-FVG-REINFORCED` — "Month 04 — ICT Fair Value Gaps FVG", `FgacYSN9QEo` (Dec 2016). FVG defined [00:33]; FVG↔liquidity-void timeframe relationship [05:14–05:33]; measuring/breakaway gaps referenced [08:36].
- `ICT-2016-REINFORCING-LIQUIDITY` — "Month 04 — Reinforcing Liquidity Concepts & Price Delivery", `npL3ZXJ5zOU` (Dec 2016). Supplies **gap risk**, the position-holder framing: defined [01:57–02:05]; both liquidity voids and fair value gaps named as internal range liquidity that will fill and is "attributed to gap risk" [01:34–01:57]; the single-long-candle recognition cue [02:05–02:14]; "whenever you're in a long and you have a big gap underneath you, that's gap risk… that's what you see stops you out as a trader" [02:14–02:29]; "we look for them as opportunities" [02:29–02:31].
- `ICT-2022-MENTORSHIP-OVERVIEW` — retained for the 2022 refinement only.
