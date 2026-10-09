# Consequent Encroachment (CE)

**Category:** 06-fair-value-gaps
**Aliases:** CE, FVG midpoint, 50% of FVG, fair value midpoint
**ICT Confidence:** medium
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2018-CE, ICT-2016-MITIGATION-BLOCKS, ICT-2022-MENTORSHIP-EP06, ICT-2022-MENTORSHIP-EP18, ICT-2022-MENTORSHIP-EP19
**Tags:** ce, fvg, midpoint, unverified-term

⚠ **UNVERIFIABLE (term) / ERA-SPLIT (role) per 2026-10-08 audit.** `consequent|encroach*` has
**zero hits** in either corpus (153 2016-17/2020-21 packets, 40 captioned 2022 Mentorship episodes). The
*midpoint* idea exists without this name in both eras (see Definition), but "CE is the primary
entry zone" is contradicted for this corpus's era — ICT's 2022 statements enter at the FVG's
**near edge**, not its midpoint, and explicitly decline the midpoint as a requirement. The
"most-frequent stopping point" / "median rebalance depth" claims and the formal "CE rebalance
event" definition are not in the corpus and have been removed. `ICT-2025-CE-PRIMARY-ENTRY`
(cited on [ce-as-primary-entry](ce-as-primary-entry.md)) is a registry stub outside this
library's corpus — do not read it back onto 2016/2022-sourced material.

## Definition

The term "consequent encroachment" does not appear in this library's corpus. The *midpoint of an
imbalance* is taught without that name in both eras. Dec-2016: "there's equilibrium of that
liquidity void[,] body to body[-]end, or is it open and close? And we're going to highlight that
reference point here[,] so[,] halfway point of this equilibrium... ultimately [price] goes down
into our mean threshold of the liquidity void" (`ICT-2016-MITIGATION-BLOCKS` [10:13]–[10:25],
[12:58]). Note ICT's own stated uncertainty about **which** boundaries define the midpoint —
wicks, or open/close — which the `(fvg_low + fvg_high)/2` formula below resolves to wicks as one
choice, not a choice ICT states outright. 2022: "trades back into another gap[,] trades into the
midpoint of that[,] rallies up" (`ICT-2022-MENTORSHIP-EP19` [103:45]); "maybe it partially fills
it[,] maybe it goes halfway" (`ICT-2022-MENTORSHIP-EP19` [06:55]); and explicitly as optional,
not required: "you can be greedy and try to trade all the way up into the middle point or deep
into it, maybe even complete closure. I don't need that." (`ICT-2022-MENTORSHIP-EP18` [08:49]).
By analogy, ICT applies the same halfway concept at the order-block scale under the name "mean
threshold": "there is the mean threshold[,] mean threshold is the half point[,] okay[,] or median
of a[n] order block" (`ICT-2022-MENTORSHIP-EP19` [78:54]) — CE, as used in this library, is the
FVG-scale name for that same halfway idea.

## Formal Criteria

- `ce = (fvg_low + fvg_high) / 2` — a convention adopted by this library using wick boundaries,
  not a boundary choice ICT states outright (see Definition).
- No frequency, "median rebalance depth," or formal "CE rebalance event" definition exists in the
  corpus. ICT's only statements on how deep a rebalance goes are informal and optional: "maybe it
  partially fills it maybe it goes halfway" (`ICT-2022-MENTORSHIP-EP19` [06:55]).
- CE is **not** stated as the primary or required entry — see Common Mistakes and
  [ce-as-primary-entry](ce-as-primary-entry.md) for the separate, unverified 2025 claim.

## Formula / Math

```
ce = (fvg_low + fvg_high) / 2

# For bullish FVG with low=H_{n-1}, high=L_{n+1}:
ce_bullish_fvg = (H_{n-1} + L_{n+1}) / 2

# For bearish FVG with low=H_{n+1}, high=L_{n-1}:
ce_bearish_fvg = (H_{n+1} + L_{n-1}) / 2

# ICT gives no stated frequency or probability of price reaching this level — see Common Mistakes.
```

## Machine-Readable

```json
{
  "id": "consequent-encroachment",
  "category": "06-fair-value-gaps",
  "aliases": ["CE", "FVG-midpoint", "50%-of-FVG"],
  "criteria": [
    {"id": "c1", "expr": "ce == (fvg_low + fvg_high) / 2 (library convention, boundary choice not stated by ICT)"},
    {"id": "c2", "expr": "applies_to_any_FVG == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "medium",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["fair-value-gap","bullish-fvg","bearish-fvg","ce-as-primary-entry","equilibrium-definition","mean-threshold","imbalance-rebalance","fvg-mitigation"],
  "sources": ["ICT-2018-CE","ICT-2016-MITIGATION-BLOCKS","ICT-2022-MENTORSHIP-EP06","ICT-2022-MENTORSHIP-EP18","ICT-2022-MENTORSHIP-EP19"]
}
```

## Visual Pattern

```
   bullish FVG with CE marked (price retraces DOWN into the gap from above):

   ─── L_{n+1} (FVG high / near edge) ────  ← ICT's 2022 stated entry sits here (candle 3's low)


   ─── CE = midpoint ───────────────────  ← an optional deeper target, not the stated entry


   ─── H_{n-1} (FVG low / far edge) ────
```

## Timeframes

All TFs. Not discussed by timeframe in the corpus.

## Examples

**Example 1 — midpoint reached but not required (M15 bullish FVG):**
- M15 bullish FVG: low 1.0860, high 1.0866. CE = 1.0863.
- ICT's 2022 convention enters at the near edge (1.0866 = candle n+1's low, the FVG high) with
  the stop beyond candle n-1 or n — see [fair-value-gap](fair-value-gap.md) Examples.
- Price reaching CE (1.0863) is possible and sometimes occurs, per `ICT-2022-MENTORSHIP-EP19`
  [06:55], but the corpus states no rule requiring it.

## Common Mistakes

- **Treating "consequent encroachment" as ICT's own 2016/2022 term.** 0 hits in either corpus.
- **Citing CE as "the primary entry zone" for the 2016/2022 material.** ICT's stated 2022 entry is
  the FVG's near edge: "the easiest entry would be trading just above candle number three's
  high... place your stop right above can[dle] number one or... number two"
  (`ICT-2022-MENTORSHIP-EP06` [17:09]–[17:38]); and he explicitly declines the midpoint: "you can
  be greedy and try to trade all the way up into the middle point... I don't need that"
  (`ICT-2022-MENTORSHIP-EP18` [08:49]). The "CE as primary entry" framing belongs only to the
  separate, unverified `ICT-2025-CE-PRIMARY-ENTRY` stub — see [ce-as-primary-entry](ce-as-primary-entry.md).
  Do not back-date it onto this page's 2016/2022 sources.
- **Claiming a stated CE "hit frequency" or "median rebalance depth."** No such statistic exists
  anywhere in the corpus.
- **Asserting a boundary convention (wicks vs. open/close) as ICT's rule.** ICT states the
  question without resolving it: "body to body[-]end, or is it open and close?"
  (`ICT-2016-MITIGATION-BLOCKS` [10:13]–[10:25]). The wick-based formula here is this library's
  convention, not a quoted ICT rule.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [bullish-fvg](bullish-fvg.md), [bearish-fvg](bearish-fvg.md).
- [ce-as-primary-entry](ce-as-primary-entry.md) — separate, unverified 2025 claim; do not conflate
  with this page's corpus-confirmed midpoint concept.
- [equilibrium-definition](../27-equilibrium/equilibrium-definition.md), [mean-threshold](../27-equilibrium/mean-threshold.md) — the analogous halfway concept at range and order-block scale.
- [imbalance-rebalance](../26-imbalance/imbalance-rebalance.md), [fvg-mitigation](fvg-mitigation.md).

## Citations

- `ICT-2018-CE` — registry stub, no video, no quotation behind it. Retained only as the
  claimed-origin pointer for the *name*; the midpoint concept itself is evidenced separately
  below under a different name and era.
- `ICT-2016-MITIGATION-BLOCKS` — "Month 04 — Mitigation Blocks" (Dec 2016). Equilibrium/mean
  threshold of a liquidity void, with ICT's own boundary uncertainty [10:13]–[10:25], [12:58].
- `ICT-2022-MENTORSHIP-EP06` — Near-edge entry convention, contradicting midpoint-as-default
  [17:09]–[17:38].
- `ICT-2022-MENTORSHIP-EP18` — Midpoint explicitly declined as unnecessary [08:49].
- `ICT-2022-MENTORSHIP-EP19` — Midpoint/halfway usage [103:45], [06:55]; mean-threshold-as-median
  analogy at order-block scale [78:54].
