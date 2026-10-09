# Market Structure Shift (MSS)

**Category:** 01-market-structure
**Aliases:** market structure shift, shift in market structure, break in market structure, market structure break, CHoCH (SMC term — not ICT's, 0 hits in corpus)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2022-MENTORSHIP-EP03, ICT-2022-MENTORSHIP-EP06, ICT-2022-MENTORSHIP-EP10, ICT-2022-MENTORSHIP-EP12, ICT-2017-HIGH-REWARD-SETUPS, ICT-2017-OPEN-FLOAT-L12, ICT-2016-BREAKER-BLOCK, ICT-2017-QUARTERLY-SHIFTS, ICT-2017-OTE
**Tags:** structure, mss, shift, break, displacement

## Definition

A market structure shift (MSS) is ICT's term for the violation of a swing point that signals a change in directional bias. ICT uses "market structure shift," "shift in market structure," "break in market structure," and "market structure break" for the **same event** — he states this explicitly: "a lot of people try to teach my concepts it'll talk about market structure breaks or shifts and we'll use that term interchangeably" (`ICT-2022-MENTORSHIP-EP03` [02:20]). The only distinction he draws is significance, not mechanism: "shift" names an intraday, lesser event, "break" a more significant one — "when i'm gonna lean on that term market structure break it means a little bit more in context versus an intraday shift" (EP03 [02:51]). There is no ICT concept named "CHoCH" (change of character) — the term has 0 hits across 153 2016-17/2020 packets and 40 captioned 2022 episodes — and ICT draws no MSS-is-a-stricter-CHoCH hierarchy. See [mss-vs-choch](mss-vs-choch.md).

## Formal Criteria

- A confirmed swing point (high or low) is violated. In 2016-17 this alone is the shift: "the old high that is violated that supports a market structure shift for bullishness" (`ICT-2016-BREAKER-BLOCK` [06:56]); "When price traded below that low, that was a break in market structure. ... So we had a market shift below that low." (`ICT-2017-OPEN-FLOAT-L12` [07:38]–[07:45]) — trade-through, not a hard close rule.
- 2022 ADDS a qualitative strength preference: the breaking move should be "energetic," not "lethargic," and "preferably" close beyond the level — "it's got to be energetic it can't be a little lethargic little move ... and preferably close below that" (`ICT-2022-MENTORSHIP-EP06` [19:05]). This is a conviction filter, not a separate required gate.
- **No FVG requirement, in either era.** A shift is valid without one: "that's how you know you have a shift in Market structure in this area here it doesn't have a fair value Gap that's okay" (`ICT-2022-MENTORSHIP-EP10` [37:43]). The FVG, when present, is searched for *inside* the shift's range afterward, to qualify a trade entry — it does not define the shift: "you're gonna be hunting your fair value gaps because that's exactly where it's going to form" (EP06 [20:29]).
- ICT also uses "market structure shift"/"break" for the quarterly-cycle (multi-month) turn, not only intraday events: "we look at the market with a quarterly perspective and allow the next shift in market structure to unfold" (`ICT-2017-HIGH-REWARD-SETUPS` [42:03], Oct 2016 content); `ICT-2017-QUARTERLY-SHIFTS` is the originating teaching of the quarterly form.
- Breaking a higher-order swing point (e.g. an intermediate-term high) is treated as the MORE significant break, not a lesser or "stale" one — see [bos-bullish](bos-bullish.md) Common Mistakes.

## Formula / Math

```
# ICT's own identical-event naming (EP03 [02:20], [02:51]):
market_structure_shift(n) := violates(relevant_swing_point, n)
market_structure_break(n) := market_structure_shift(n)   # same event; "break" used when more significant

# 2016-17: trade-through qualifies, no close requirement stated.
# 2022: "preferably" a close beyond the level, and the move should read as energetic —
#        both strength preferences, not hard gates (EP06 [19:05]).

# NOT part of is_mss(n):
#   fvg_in_break(n)   -- ICT: a shift can lack one (EP10 [37:43])
#   is_choch(n)        -- "CHoCH" is not an ICT term
```

## Machine-Readable

```json
{
  "id": "mss",
  "category": "01-market-structure",
  "aliases": ["market-structure-shift", "shift-in-market-structure", "break-in-market-structure", "market-structure-break"],
  "criteria": [
    {"id": "c1", "expr": "violates_relevant_swing_point(n) == true"},
    {"id": "c2", "expr": "era_2022_preference: energetic_and_preferably_closed(n)"},
    {"id": "c3", "expr": "fvg_requirement == false"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["mss-vs-choch","bos-bullish","bos-bearish","displacement-definition","swing-high","swing-low"],
  "sources": ["ICT-2022-MENTORSHIP-EP03","ICT-2022-MENTORSHIP-EP06","ICT-2022-MENTORSHIP-EP10","ICT-2022-MENTORSHIP-EP12","ICT-2017-HIGH-REWARD-SETUPS","ICT-2017-OPEN-FLOAT-L12","ICT-2016-BREAKER-BLOCK","ICT-2017-QUARTERLY-SHIFTS","ICT-2017-OTE"]
}
```

## Visual Pattern

```
   2016-17 (trade-through only):         2022 (energetic + preferably closed):

   SH_ref ──────┴──                      SH_ref ──────┴──
               \                                     ▲
                \  wick or close                      █  wide, energetic candle
                 \  through SH_ref                    █  preferably closes beyond
                  \                                   █  (FVG optional either way)
```

Both are the same event under ICT's naming; 2022 simply adds a quality preference for how convincing the break looks.

## Timeframes

All timeframes: "when you're looking at market structure shifts this is all time frames" (`ICT-2022-MENTORSHIP-EP06` [19:37]). ICT also applies the same word to the quarterly (multi-month) cycle, so "MSS" is not confined to intraday/entry timeframes.

## Examples

**Example 1 — 2016-17 style, trade-through only:**
- Price trades below the relevant swing low on a lower-timeframe chart.
- No displacement, no FVG required — the trade-through itself is the shift (`ICT-2017-OPEN-FLOAT-L12` [07:38]).

**Example 2 — 2022 style, energetic + preferred close:**
- M5 prints a wide, fast-moving candle through the swing high and closes beyond it.
- A fair value gap may or may not form inside the move; its presence strengthens the setup but is not required for the shift itself (`ICT-2022-MENTORSHIP-EP10` [37:43]).

## Common Mistakes

- **Requiring an FVG inside the break.** ICT explicitly allows a shift with no FVG (EP10 [37:43]); an engine that discards undisplaced, FVG-less shifts discards valid ICT events.
- **Requiring a hard close.** 2016-17 shifts are called on trade-through (`ICT-2017-OPEN-FLOAT-L12` [07:38]); 2022 states a close only as a preference ("preferably close below that," EP06 [19:05]). Neither era states a hard close rule.
- **Treating "MSS" and "CHoCH" as ICT's own nested taxonomy.** CHoCH has 0 hits in either corpus; it is SMC-community vocabulary layered onto ICT's single interchangeable term. See [mss-vs-choch](mss-vs-choch.md).
- **Assuming "MSS" means reversal and "BOS" means continuation.** ICT uses "market structure break" for continuation breaks too (`ICT-2017-OTE` [28:02]–[28:04]) and for post-stop-run reversals (`ICT-2017-OTE` [40:30]–[40:56]) with the same words.
- **Treating a higher-order swing break as "stale."** Breaking an older, higher-order swing point is the MORE significant event, not a disqualified one — see [bos-bullish](bos-bullish.md) Common Mistakes.

## ICT vs Community

"MSS" / "market structure shift" / "break in market structure" are ICT's own, used interchangeably by him. The CHoCH/BOS vocabulary — and the idea that MSS is a displacement-and-FVG-filtered subset of CHoCH — comes from the Smart Money Concepts (SMC) community, not ICT. Searches of 153 2016-17/2020 packets and 40 captioned 2022 Mentorship episodes for `choch`, `change of character`, `change in character`, and the bare word `character` returned 0 hits. This library keeps CHoCH as a cross-reference (tagged SMC) on [mss-vs-choch](mss-vs-choch.md) but does not present it as ICT's concept.

## Related Concepts

- [mss-vs-choch](mss-vs-choch.md) — disambiguation; explains why "every MSS is a CHoCH" is not ICT's claim.
- [bos-bullish](bos-bullish.md) / [bos-bearish](bos-bearish.md) — ICT's "market structure break" covers these too; see that page's own caveats.
- [displacement-definition](../09-displacement/displacement-definition.md) — the 2022 "energetic" preference, detailed.
- [swing-high](swing-high.md) / [swing-low](swing-low.md) — the reference points a shift violates.

## Citations

- `ICT-2016-BREAKER-BLOCK` [06:56] — "the old high that is violated that supports a market structure shift for bullishness" (Dec 2016).
- `ICT-2017-OPEN-FLOAT-L12` [07:38]–[07:45] — "When price traded below that low, that was a break in market structure. ... So we had a market shift below that low."
- `ICT-2017-HIGH-REWARD-SETUPS` [42:03] — quarterly-cycle shift, Oct 2016 content (misdated 2017 ID; see SOURCES.md note).
- `ICT-2017-QUARTERLY-SHIFTS` [05:01] — "I teach that there is a market structure shift that takes place every three to four months." Originating teaching of the quarterly-cycle shift, Jan 2017.
- `ICT-2017-OTE` [28:02]–[28:04], [34:20]–[34:35], [40:30]–[40:56] — "market structure break" used for continuation and for post-stop-run reversal.
- `ICT-2022-MENTORSHIP-EP03` [02:20], [02:51] — shift/break used interchangeably; break = more significant.
- `ICT-2022-MENTORSHIP-EP06` [19:05], [19:37], [20:29] — 2022 energetic/preferred-close filter; applies on all timeframes; FVG hunted after the shift.
- `ICT-2022-MENTORSHIP-EP10` [37:15]–[37:43] — a shift without a fair value gap is still valid.
- `ICT-2022-MENTORSHIP-EP12` [31:09] — a significant break (vs. a short-term-low break) distinguished by scope, not displacement.
