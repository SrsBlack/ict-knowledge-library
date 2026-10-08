# Internal Range Liquidity (IRL)

**Category:** 02-liquidity
**Aliases:** IRL, internal liquidity
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-REINFORCING-LIQUIDITY, ICT-2016-ORDERBLOCKS, ICT-2017-INTRADAY-TOP-DOWN, ICT-2022-MENTORSHIP-EP03, ICT-2022-MENTORSHIP-EP06
**Tags:** liquidity, irl, internal, dealing-range

> ⚠ **Re-dated 2026-10-08.** Previously `Year Introduced: 2022`, contradicted — see [external-range-liquidity](external-range-liquidity.md) for the full dating note; same December 2016 / August 2017 origin.

## Definition

Internal Range Liquidity is liquidity that exists **inside** the current trading range — ICT pairs it with [external-range-liquidity](external-range-liquidity.md) as entry vs. exit: "predominantly, my entries are internal range liquidity entries, with exits at external range liquidity" (`ICT-2016-REINFORCING-LIQUIDITY`, 10:29–10:34). In 2016 its named members are liquidity voids, fair value gaps and order blocks inside the range: "when the current trading range is likely to remain, liquidity voids will fill in… fair value gaps will also fill in… order blocks inside the trading range will be populated with new buys and or sells" (01:39–02:31). The 2022 definition narrows to a stop/imbalance reading: "internal range liquidity is a short-term higher low with stops above or below it, or an imbalance in that same range of price action" (`ICT-2022-MENTORSHIP-EP03`, 35:03).

## Formal Criteria

- The reference is whichever **trading range** is currently in play (see `external-range-liquidity` — ICT gives no fixed swing-depth rule for the range bounds).
- IRL = liquidity inside that range: internal swing pivots with stops, FVGs, order blocks, or liquidity voids expected to fill while the range holds.
- **IRL is primarily ICT's entry side**, not a partial-target/staging-only zone: "predominantly, my entries are internal range liquidity" (`ICT-2016-REINFORCING-LIQUIDITY`, 10:30); it is also named as a partial/scale-out reference when exiting a trade already in progress: "so partials — internal range, external range — your trade" (`ICT-2022-MENTORSHIP-EP06`, 45:41).
- Classification is range-relative, not absolute — the same level can be IRL on one timeframe's range and ERL on another's (see `external-range-liquidity`, 05:59–06:04 / 11:58–12:08).
- "An IRL target taken does NOT flip HTF bias by itself — only ERL takes do" is **not in either corpus** (0 hits for "bias change/flip/shift" in this context). Do not present this as ICT's rule.
- "Internal trendline liquidity (touches all inside the range)" is **not in the corpus** — neither the Dec-2016 nor the 2022 IRL/ERL passages mention trendlines in this context.

## Formula / Math

ICT gives no fixed swing-depth formula for the range bounds; IRL is simply "inside the currently-referenced trading range."

```
is_IRL(level, range) := level is inside the currently-referenced trading range
                          AND level identifies as one of: internal-swing-with-stops | FVG | OB | liquidity-void
```

## Machine-Readable

```json
{
  "id": "internal-range-liquidity",
  "category": "02-liquidity",
  "aliases": ["IRL", "internal-liquidity"],
  "criteria": [
    {"id": "c1", "expr": "level inside the currently-referenced trading range (range-relative, not absolute)"},
    {"id": "c2", "expr": "level is internal-swing-with-stops, FVG, OB, or liquidity-void"},
    {"id": "c3", "expr": "IRL is predominantly ICT's entry side, not only a partial-target zone"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["external-range-liquidity","internal-structure","fair-value-gap","draw-on-liquidity","dealing-range","liquidity-pool"],
  "sources": ["ICT-2016-REINFORCING-LIQUIDITY","ICT-2016-ORDERBLOCKS","ICT-2017-INTRADAY-TOP-DOWN","ICT-2022-MENTORSHIP-EP03","ICT-2022-MENTORSHIP-EP06"]
}
```

## Visual Pattern

```
   range high ────────────────────────  ERL above (exit side)

       internal-swing   FVG          ← IRL (predominantly entry side)
              /\        ▒▒▒▒
             /  \       ▒▒▒▒
            /    \      ▒▒▒▒
                  OB
                  ░░░░  ← IRL
                  ░░░░

   range low  ────────────────────────  ERL below (exit side)
```

## Timeframes

Range-relative at every TF. On M1/M5 the reference range drifts rapidly and IRL/ERL distinctions blur; most coherent on H1+ where a stable trading range is being tracked.

## Examples

**Example 1 — IRL as entry:**
- Current trading range: range low 1.0800, range high 1.1000.
- Inside the range: a bullish order block at 1.0820–1.0830 and an FVG at 1.0870–1.0885.
- Entry is taken at the IRL order block; exit/partial is targeted at the ERL range high — "buying inside the range and selling it outside the range" (`ICT-2016-REINFORCING-LIQUIDITY`, 10:39–10:40).

## Common Mistakes

- **Treating IRL as only a partial-take/staging zone.** ICT states his entries are predominantly IRL — it is not merely a scale-out level.
- **Asserting a bias-flip rule for ERL vs. IRL takes.** Not in the corpus.
- **Citing "internal trendline liquidity" as an IRL category.** Not in the corpus.
- **Treating IRL/ERL as fixed properties of a level rather than range-relative.** See `external-range-liquidity` for the explicit same-level-both-ways example.

## Related Concepts

- [external-range-liquidity](external-range-liquidity.md) — exit-side counterpart; same range-relative classification.
- [internal-structure](../01-market-structure/internal-structure.md) — internal swings are IRL.
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md) — a named IRL form.
- [draw-on-liquidity](draw-on-liquidity.md) — IRL/ERL distinction shapes draw selection.
- [dealing-range](../05-pd-arrays/dealing-range.md) — the "current trading range" referenced by IRL/ERL.

## Citations

- `ICT-2016-REINFORCING-LIQUIDITY` (01:39–02:31) liquidity voids, FVGs and order blocks inside the range as IRL members; (10:29–10:40) "predominantly, my entries are internal range liquidity entries, with exits at external range liquidity… I'm buying inside the range and selling it outside the range."
- `ICT-2016-ORDERBLOCKS` (08:16–09:15) internal range liquidity as the entry level inside an order block.
- `ICT-2017-INTRADAY-TOP-DOWN` (36:56) "it's either going to be an internal range liquidity, optimal trade entry… or it's going to be external range liquidity run… basically it's turtle soup."
- `ICT-2022-MENTORSHIP-EP03` (00:17) episode titled "the internal range liquidity and market structure shift lecture"; (35:03) "internal range liquidity is a short-term higher low with stops above or below it, or an imbalance in that same range of price action."
- `ICT-2022-MENTORSHIP-EP06` (45:41) "so partials — internal range, external range — your trade."
