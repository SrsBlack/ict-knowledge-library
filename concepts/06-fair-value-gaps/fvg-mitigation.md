# FVG Rebalance / Fill (sometimes called "FVG Mitigation")

**Category:** 06-fair-value-gaps
**Aliases:** FVG fill, FVG close-in, FVG rebalance, FVG mitigation (later label)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FAIR-VALUATION, ICT-2016-FVG-REINFORCED, ICT-2016-LIQUIDITY-VOIDS, ICT-2016-MITIGATION-BLOCKS, ICT-2022-MENTORSHIP-EP12, ICT-2022-MENTORSHIP-EP16, ICT-2022-MENTORSHIP-EP19
**Tags:** fvg, rebalance, fill, status

⚠ **Edited 2026-10-08 per audit.** ICT does not apply the word "mitigation" to an FVG's state in
either corpus — his words are **rebalance**, **closed in**, and **fill**. "CE mitigation (2025
framing)" and the fresh/partial/mitigated state machine are not in the corpus (the cited
`ICT-2025-CE-PRIMARY-ENTRY` is a stub outside this library's range) and have been replaced with
what the corpus actually supports: full close-in as completion, with partial fills described
informally, not as a named state. "Year Introduced: 2017" is corrected to 2016 — closing-in of an
FVG is taught from the Sep-2016 mentorship.

## Definition

The state change that occurs when price returns to an FVG and trades back through it has no
single named-state framework in the corpus. ICT's verbs for it are **rebalance**, **closed in**,
and **fill**, not "mitigation": "we're just going to close in the range between this up candle
and this up candle here, which is a fair value gap" (`ICT-2016-FAIR-VALUATION` [22:23], Sep
2016); "[e]ventually, price does in fact trade back up, closes the fair value gap in. That trade
or that idea is now complete." (`ICT-2016-FVG-REINFORCED` [07:18]–[07:24], Dec 2016); "it
completely closes in all the imbalance that's between this low and this high of that candle[,] it
rebalanced all that" (`ICT-2022-MENTORSHIP-EP16` [13:10]). For a body-based gap, a body-only
close-in is already sufficient — see [volume-imbalance](volume-imbalance.md).

## Formal Criteria

- **Completion, as the corpus states it, is a full close-in** (price trading back through the
  zone), not a touch at a midpoint. No "CE mitigation" rule exists in the corpus — see
  [consequent-encroachment](consequent-encroachment.md).
- Partial fills are discussed informally, not as a named status: "maybe it partially fills it[,]
  maybe it goes halfway" (`ICT-2022-MENTORSHIP-EP19` [06:55]).
- **No time limit on an FVG's closure is stated in the corpus for FVGs specifically**; the
  closely related liquidity void is stated to have none either (`ICT-2016-LIQUIDITY-VOIDS` [02:19]).
- A rebalanced FVG is not described as "consumed." Its stated structural consequence is to become
  a new reference point: "anytime a imbalance like this big candle up is rebalanced[,] that
  becomes an intermediate term low" (`ICT-2022-MENTORSHIP-EP12` [16:58]); and a re-visited FVG is
  still actively used a second time in the same 2016 lecture (see Common Mistakes).

## Formula / Math

```
# ICT gives no numeric mitigation threshold (no CE-touch rule, no fill-percentage rule).
# The corpus-supported completion rule is binary (not a staged threshold); partial fills are
# described too, just not formalized as a named status:

rebalanced(fvg) := exists candle k after fvg.formed_bar such that price(k) fully closes in the gap

# Partial fill is described but never formalized as a threshold or named status.
```

## Machine-Readable

```json
{
  "id": "fvg-mitigation",
  "category": "06-fair-value-gaps",
  "aliases": ["FVG-fill", "FVG-close-in", "FVG-rebalance"],
  "criteria": [
    {"id": "c1", "expr": "completion == full close-in (no CE-touch rule in corpus)"},
    {"id": "c2", "expr": "no formal fresh/partial/mitigated state machine in corpus; partial fill discussed informally only"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["fair-value-gap","consequent-encroachment","ce-as-primary-entry","imbalance-rebalance","mitigation-of-fvg","inversion-fvg","mitigated-order-block"],
  "sources": ["ICT-2016-FAIR-VALUATION","ICT-2016-FVG-REINFORCED","ICT-2016-LIQUIDITY-VOIDS","ICT-2016-MITIGATION-BLOCKS","ICT-2022-MENTORSHIP-EP12","ICT-2022-MENTORSHIP-EP16","ICT-2022-MENTORSHIP-EP19"]
}
```

## Visual Pattern

```
   What the corpus actually supports — binary, not a staged lifecycle:

   FVG forms ──┬── open
               │
               ↓ price trades back through the zone, fully
               │
          "closed in" / "rebalanced" / "filled" (ICT's own words)
               │
               ↓ (informally) may leave a new intermediate high/low behind
               │
          referenced again later, not discarded (see Common Mistakes)
```

## Timeframes

All TFs. Not discussed by timeframe specifically in the corpus.

## Examples

**Example 1 — full close-in, per the 2016 corpus:**
- M15 bullish FVG forms at 1.0860–1.0866.
- Price later trades back down through 1.0860 (the full zone).
- Per `ICT-2016-FVG-REINFORCED` [07:18]–[07:24], the FVG is now "closed... in" and the idea is
  "complete" — no midpoint rule applies.
- The same 2016 lecture shows price revisiting the same 104.75 level a **second** time after the
  first close-in, still as an active reference — "[h]ere's the first time it trades up into that
  104.75 level... [a]nd then here's the second time it trades up into it." (`ICT-2016-FVG-REINFORCED`
  [11:51]–[11:57]).

## Common Mistakes

- **Calling this "FVG mitigation."** ICT's own words are rebalance / closed in / fill; "mitigation"
  in the corpus refers to the separate **mitigation block** object, not an FVG's status
  (`ICT-2016-MITIGATION-BLOCKS`; see [mitigation-of-ob](../18-mitigation/mitigation-of-ob.md)).
- **Applying a "CE mitigation" rule.** No touch-at-midpoint completion rule exists in the corpus —
  see [consequent-encroachment](consequent-encroachment.md).
- **Treating fresh/partial/mitigated as a named three-state system.** The corpus discusses partial
  fills informally ("maybe it goes halfway," `ICT-2022-MENTORSHIP-EP19` [06:55]) but never names
  or formalizes three states.
- **Assuming a rebalanced FVG is "structurally consumed" and dropped from use.** ICT's stated
  consequence is structural re-use, not disposal: a rebalanced imbalance becomes "an intermediate
  term low" (`ICT-2022-MENTORSHIP-EP12` [16:58]), and the same zone can be revisited and traded a
  second time (`ICT-2016-FVG-REINFORCED` [11:51]–[11:57]).

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md).
- [imbalance-rebalance](../26-imbalance/imbalance-rebalance.md), [mitigation-of-fvg](../18-mitigation/mitigation-of-fvg.md), [inversion-fvg](inversion-fvg.md), [mitigated-order-block](../07-order-blocks/mitigated-order-block.md).

## Citations

- `ICT-2016-FAIR-VALUATION` — "Month 1 — Fair Valuation" (Sep 2016). Earliest located close-in
  statement [22:23].
- `ICT-2016-FVG-REINFORCED` — "Month 04 — ICT Fair Value Gaps FVG" (Dec 2016). Full close-in as
  completion [07:18]–[07:24]; a second, later revisit of the same closed-in zone [11:51]–[11:57].
- `ICT-2016-LIQUIDITY-VOIDS` — "Month 04 — Liquidity Voids" (Dec 2016). No time limit on closure,
  stated for the closely related liquidity void [02:19].
- `ICT-2022-MENTORSHIP-EP12` — Rebalance leaves a new intermediate high/low, not "consumption"
  [16:58], [48:15].
- `ICT-2022-MENTORSHIP-EP16` — Full close-in restated in 2022 [13:10].
- `ICT-2022-MENTORSHIP-EP19` — Informal partial-fill language, no named state [06:55].
- `ICT-2016-MITIGATION-BLOCKS` — "Month 04 — Mitigation Blocks" (Dec 2016). Mitigation block
  framed as an "implication of order block theory" [00:28] — a distinct PD array, not an FVG
  state.
