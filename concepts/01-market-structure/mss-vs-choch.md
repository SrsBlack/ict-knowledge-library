# MSS vs CHoCH — Disambiguation

**Category:** 01-market-structure
**Aliases:** shift vs break, market structure shift vs market structure break
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-EP03, ICT-2022-MENTORSHIP-EP06, ICT-2022-MENTORSHIP-EP12, ICT-2022-MENTORSHIP-EP10, ICT-2017-QUARTERLY-SHIFTS, ICT-2017-HIGH-REWARD-SETUPS
**Tags:** structure, disambiguation, mss, choch, terminology, smc

## Definition

"CHoCH" (change of character) is **not an ICT term**. Searches of 153 2016-17/2020 mentorship packets and 40 captioned 2022 Mentorship episodes for `choch`, `change of character`, `change in character`, and the bare word `character` returned 0 hits in both corpora. It is Smart Money Concepts (SMC) community vocabulary, and the claim that "every MSS is a CHoCH, but not every CHoCH is an MSS" is an SMC overlay, not an ICT distinction. This page exists to document that overlay for readers coming from SMC material and to state the ONE hierarchy ICT actually draws between his own two words, "shift" and "break."

## Formal Criteria

### ICT's actual distinction: shift vs. break (significance, not displacement)

- ICT states the two words name the **same event**, and says he will use them interchangeably himself: "a lot of people try to teach my concepts it'll talk about market structure breaks or shifts and we'll use that term interchangeably" (`ICT-2022-MENTORSHIP-EP03` [02:20]) — this is ICT announcing his own usage, not criticizing other teachers' usage.
- When he does distinguish them, "break" is the MORE significant event and "shift" the lesser, more localized one — not the reverse: "when i'm gonna lean on that term market structure break it means a little bit more in context versus an intraday shift" (EP03 [02:51]). This is the terminology source for the shift-vs-break distinction. `ICT-2022-MENTORSHIP-EP12` [31:09] ("if we have a break below and any return low then we have what a significant break in Market structure — this is something that's more significant just simply than going into a chart saying okay well it took out a short-term low") is scope evidence for the same more-significant/less-significant pattern — note it contrasts a "significant break" against a short-term-low take-out and never uses the word "shift," so it supports the pattern without being a shift-vs-break statement itself.
- In the 2016-17 mentorship, "shift" also names the largest turn ICT teaches — the three-to-four-month quarterly shift: "So we look at the market with a quarterly perspective and allow the next shift in market structure to unfold." (`ICT-2017-HIGH-REWARD-SETUPS` [42:03], Oct 2016 content, misdated 2017 ID per SOURCES.md); `ICT-2017-QUARTERLY-SHIFTS` is the originating Jan-2017 teaching of the quarterly form. So "shift" is not reserved for small/intraday events either; scale depends on context, not a fixed rank.
- Displacement does not enter this distinction at all: a shift can lack a fair value gap and still be valid (`ICT-2022-MENTORSHIP-EP10` [37:43]).

### The SMC overlay this page replaces (kept only as a labeled cross-reference)

- SMC's CHoCH: first close beyond the most recent swing point, no displacement required.
- SMC's claim: "every MSS is a CHoCH, but not every CHoCH is an MSS" — i.e. MSS is a stricter, displaced CHoCH.
- This inverts the one hierarchy ICT actually states (break = MORE significant, EP12 [31:09]) and adds a displacement gate ICT never ties to the shift/break distinction.

## Formula / Math

```
# ICT's actual relationship (EP03 [02:20]/[02:51], EP12 [31:09]):
market_structure_shift(n) == market_structure_break(n)   # same event, used interchangeably
# when distinguished: "break" >= "shift" in significance, not displacement

# NOT ICT's: a CHoCH/MSS displacement-gated hierarchy
# is_choch(n) / is_mss(n) as nested SMC predicates are not used in this library's
# definitional claims; see mss.md for ICT's own (undisplaced-OK) criteria.
```

## Machine-Readable

```json
{
  "id": "mss-vs-choch",
  "category": "01-market-structure",
  "aliases": ["shift-vs-break"],
  "criteria": [
    {"id": "c1", "expr": "ict_shift_and_break_are_interchangeable == true"},
    {"id": "c2", "expr": "when_distinguished: break_significance >= shift_significance"},
    {"id": "c3", "expr": "choch_is_not_an_ict_term == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["mss","displacement-definition"],
  "sources": ["ICT-2022-MENTORSHIP-EP03","ICT-2022-MENTORSHIP-EP06","ICT-2022-MENTORSHIP-EP12","ICT-2022-MENTORSHIP-EP10","ICT-2017-QUARTERLY-SHIFTS","ICT-2017-HIGH-REWARD-SETUPS"]
}
```

## Visual Pattern — ICT's actual usage vs. the SMC overlay

```
ICT (shift == break; "break" sometimes      SMC overlay (not ICT's — do not cite as his):
more significant, not more displaced):
                                              CHoCH ⊃ MSS
   SH ──────┴──                                 (MSS = CHoCH + displacement + FVG)
            \
             \  trade-through or close,      This hierarchy is absent from both
              \  displacement optional,      corpora; "CHoCH" itself is absent.
               \  FVG optional
              "shift" / "break" — same event
```

## Timeframes

Applies on every timeframe ICT teaches structure on, including the multi-month quarterly cycle, where "shift" names the largest turn he discusses (`ICT-2017-HIGH-REWARD-SETUPS` [42:03]; `ICT-2017-QUARTERLY-SHIFTS`).

## Examples

**Example A — ICT's usage:**
- M15 bearish leg. A candle trades through the relevant swing high.
- ICT would call this a market structure shift (or break — interchangeably), regardless of whether it closed beyond the level or left an FVG behind.

**Example B — where the SMC overlay would diverge from ICT:**
- Same M15 event, a thin wick through the level that comes right back, no close beyond it.
- SMC overlay: "CHoCH only, not MSS" (displacement/FVG gate fails).
- ICT's own words: 2016-17 — valid shift on the trade-through alone; 2022 — ICT would call a lethargic wick-through "not all that convincing": "if we just go through this low a little bit like a wick and come back up ... that to me is not all that convincing, i want to see that it has absolutely displaced and then the candle closed" (`ICT-2022-MENTORSHIP-EP06` [19:37]) — a strength preference he states, still not a hard FVG gate (an undisplaced shift with no FVG is still a shift, `ICT-2022-MENTORSHIP-EP10` [37:43]).

## Common Mistakes

- **Citing "CHoCH" as ICT's word.** It is not — 0 hits in 153 packets and 40 captioned episodes.
- **Treating MSS as the stricter, displaced member of a CHoCH/MSS pair.** ICT's only stated hierarchy (shift vs. break) is about significance, and "break" is the MORE significant term — the opposite direction from "MSS = CHoCH + extra filter."
- **Assuming the distinction matters on HTF because every HTF reversal is displaced.** Not stated anywhere in either corpus; ICT applies "shift" at every timeframe including the quarterly cycle without a displacement caveat.

## ICT vs Community

CHoCH is Smart Money Concepts (SMC) community vocabulary. ICT uses "market structure shift" and "break in market structure" / "market structure break" interchangeably for the same event, with "break" reserved for the more significant case when he does distinguish them (`ICT-2022-MENTORSHIP-EP03` [02:20]–[02:51], `ICT-2022-MENTORSHIP-EP12` [31:09]). Readers arriving from SMC material should treat "CHoCH" as an external label this library does not attribute to ICT, not as a synonym he endorsed.

## Related Concepts

- [mss](mss.md) — ICT's own criteria (no displacement or FVG gate required).
- [displacement-definition](../09-displacement/displacement-definition.md) — the 2022 energetic/preferred-close quality filter, which is separate from the shift/break naming.

## Citations

- `ICT-2022-MENTORSHIP-EP03` [02:20], [02:51] — shift and break used interchangeably, by ICT's own stated usage; break = more significant in context.
- `ICT-2022-MENTORSHIP-EP06` [19:37] — lethargic wick-through "not all that convincing"; a strength preference, not an FVG gate.
- `ICT-2022-MENTORSHIP-EP12` [31:09] — scope evidence: "significant break in Market structure" vs. a short-term-low take-out (does not use the word "shift").
- `ICT-2022-MENTORSHIP-EP10` [37:43] — a shift without a fair value gap is still valid.
- `ICT-2017-HIGH-REWARD-SETUPS` [42:03] — quarterly-cycle shift, Oct 2016 content (misdated 2017 ID; see SOURCES.md note).
- `ICT-2017-QUARTERLY-SHIFTS` — originating teaching of the quarterly-cycle shift (Jan 2017 mentorship).
