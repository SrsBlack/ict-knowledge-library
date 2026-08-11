# Nested FVG

**Category:** 06-fair-value-gaps
**Aliases:** nested FVGs, FVG-in-FVG, multi-TF FVG nest
**ICT Confidence:** medium
**Year Introduced:** 2017
**Year Refined:** 2025
**Source IDs:** ICT-2017-SWING-BULL-SETUPS, ICT-2017-SWING-BEAR-SETUPS, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2025-ADV-LIQUIDITY

⚠ **Dated to its nearest antecedent 2026-08-10, and confidence downgraded `high` → `medium`.**
The page previously claimed 2022 while citing only 2022 and 2025 sources. The corpus teaches
*array-inside-array* nesting in Feb 2017 — "daily bullish discount arrays **at or nested in** weekly
discount arrays … a weekly liquidity void **or fair value gap**" (`ICT-2017-SWING-BULL-SETUPS`
[04:01–04:41]) — but the strict **same-polarity FVG-inside-FVG** construction this page formalises
is **not located verbatim anywhere in the corpus**, which ends Aug 2017. Same treatment as
[judas-swing-failure](../13-judas-swing/judas-swing-failure.md): dated to the antecedent ICT does
teach, marked `medium`, with the gap stated rather than papered over.

⚠ **Confirmed against the bear-market counterpart 2026-08-11 — the caveat above stands, on a full
read and an exhaustive count.** `ICT-2017-SWING-BEAR-SETUPS` (lesson 5) is the sell-side mirror of the
lesson-4 passage this page rests on. It was read in full and every relevant mention enumerated, not
sampled:

- **"nested" occurs exactly 4 times**, and all four are *lower-timeframe array inside
  higher-timeframe array*: "sell **daily** bearish premium arrays at or nested in **weekly** premium
  arrays"; "sell **four hour** bearish premium arrays at **daily** and or nested in **weekly**";
  "sell all **daily** bearish premium arrays at or nested in the **monthly**"; "sell **four hour**
  bearish premium arrays at **weekly** and or nested in **monthly**" [02:31–03:25].
- **All four name no array type on either side** — the noun is the generic "premium arrays". The bear
  lecture is therefore *less* specific than its bull sibling, which at least named candidate types for
  the outer slot.
- **"fair value gap" occurs exactly twice in 31 minutes**, and **neither is a nest**: once as one
  member of the premium-array enumeration [02:02], once as a standalone entry — "we have a fair value
  gap right between here, this is a potential selling opportunity" [17:47–17:54].
- In that enumeration the fair value gap and the liquidity void are **separate members of the same
  list** [01:37–02:14], which is the set "nested" ranges over.

**Conclusion:** the Feb-2017 antecedent supports **any array inside any array, across timeframes**,
and does not narrow toward same-polarity FVG containment. Two independent lectures, one construction,
zero instances of an FVG nested in an FVG. The caveat is correct, `medium` confidence stays, and the
strict construction this page formalises remains unsourced in the corpus. ✔ **What the corpus *does*
confirm is this page's timeframe direction** — the nest always runs LTF-inside-HTF, never the reverse.
**Tags:** fvg, nesting, multi-tf, confluence

## Definition

A **nested FVG** is when a smaller FVG (typically on a lower timeframe) sits inside the price range of a larger FVG (on a higher timeframe). ICT teaches nested FVGs as **high-conviction confluence zones**: when price returns to fill the HTF FVG, the LTF FVG provides a precise entry trigger inside the broader zone. Nested FVGs are a special case of [pd-array-nesting](../05-pd-arrays/pd-array-nesting.md) and one of the cleanest applications of the 2025 strengthening principle.

## Formal Criteria

A valid nested-FVG setup:

- **HTF FVG** (e.g., H4 or H1) defines the broad zone.
- **LTF FVG** (e.g., M15 or M5) of the **same polarity** sits entirely (or mostly) within the HTF FVG range.
- Both unmitigated.
- Same direction (bullish HTF FVG nests bullish LTF FVG; not mixed).
- Optionally: the LTF FVG straddles or sits at the HTF FVG's CE (highest-conviction nest position).

## Formula / Math

```
nested_fvg(htf_fvg, ltf_fvg) :=
    ltf_fvg.polarity == htf_fvg.polarity
    AND ltf_fvg.range ⊂ htf_fvg.range  (or substantially overlaps)
    AND both_unmitigated == true

# Conviction bonus when LTF FVG sits at HTF CE:
nested_at_ce := abs(ltf_fvg.center - htf_fvg.ce) <= small_tolerance
```

## Machine-Readable

```json
{
  "id": "nested-fvg",
  "category": "06-fair-value-gaps",
  "aliases": ["nested-FVGs", "FVG-in-FVG", "multi-tf-FVG-nest"],
  "criteria": [
    {"id": "c1", "expr": "ltf_fvg_inside_htf_fvg_range"},
    {"id": "c2", "expr": "same_polarity == true"},
    {"id": "c3", "expr": "both_fresh_unmitigated == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2017",
  "year_refined": "2025",
  "related": ["fair-value-gap","pd-array-nesting","htf-pd-array-hierarchy","consequent-encroachment","ce-as-primary-entry","pd-array-confluence"],
  "sources": ["ICT-2017-SWING-BULL-SETUPS","ICT-2017-SWING-BEAR-SETUPS","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2025-ADV-LIQUIDITY"]
}
```

## Visual Pattern

```
   nested bullish FVG (H1 contains M15):

   ──── H1 FVG high ────
        ▒▒▒▒
        ▒▓▓▒  ← M15 FVG nested inside (same polarity)
        ▒▓▓▒
        ▒▒▒▒
   ──── H1 FVG low ─────

   When price returns into H1 FVG zone, the M15 FVG provides
   a precise entry trigger inside the broader HTF zone.
```

## Timeframes

Multi-TF by definition. Common pairings: H4-FVG with M15-FVG nested; H1-FVG with M5-FVG nested.

## Examples

**Example 1 — nested H1 + M15 bullish FVGs:**
- H1 bullish FVG: 1.0850–1.0875 (CE 1.08625).
- M15 bullish FVG: 1.0858–1.0866 (inside H1 FVG, near CE).
- HTF (D) bullish.
- Setup: long entry on M15 FVG CE retest at 1.0862. SL below H1 FVG low at 1.0848.
- Risk = 14 pips. Tight relative to the broader H1 zone — entry trigger is M15-precise but the structural zone is H1-wide.
- Conviction: high (nested + same polarity + HTF bias agree + LTF FVG sits at HTF CE).

## Common Mistakes

- **Cross-polarity "nesting."** A bullish FVG inside a bearish FVG is a **conflict zone**, not a nest. Same direction required.
- **One mitigated, one fresh.** If the HTF FVG is already mitigated (touched at CE), the nest's confluence weakens — re-evaluate.
- **Demanding exact containment.** Substantial overlap (~70%+) is enough; ~100% containment is not required.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [pd-array-nesting](../05-pd-arrays/pd-array-nesting.md), [htf-pd-array-hierarchy](../05-pd-arrays/htf-pd-array-hierarchy.md), [consequent-encroachment](consequent-encroachment.md), [ce-as-primary-entry](ce-as-primary-entry.md), [pd-array-confluence](../05-pd-arrays/pd-array-confluence.md).

## Citations

- `ICT-2017-SWING-BULL-SETUPS` (04:01–04:41) the buy-side nesting passage — "daily bullish discount arrays at or nested in weekly discount arrays… a weekly liquidity void or fair value gap… overlapping or having a confluence of levels". ⚠ Partial read.
- `ICT-2017-SWING-BEAR-SETUPS` (01:37–02:14) the premium-array enumeration in which the fair value gap and the liquidity void are listed as separate members; (02:31–02:50) the sell-side mirror — "sell daily bearish premium arrays at or nested in weekly premium arrays… sell four hour bearish premium arrays at daily and or nested in weekly bearish premium arrays"; (28:58–29:05) "the more levels that converge around a specific price level, the more likely it's going to probably be sensitive".
- `ICT-2022-MENTORSHIP-OVERVIEW`, `ICT-2025-ADV-LIQUIDITY`.
