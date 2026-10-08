# Bullish Structure Break

**Category:** 01-market-structure
**Aliases:** bullish break in market structure, bullish market structure break, Break of Structure / BOS (SMC term — "BOS" and "break of structure" are 0 hits in corpus; ICT says "break in market structure")
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FAIR-VALUATION, ICT-2016-LIQUIDITY-RUNS, ICT-2017-OTE, ICT-2017-OTE-FIBER-NYO, ICT-2022-MENTORSHIP-EP02, ICT-2016-REINFORCING-LIQUIDITY
**Tags:** structure, break, bullish, foundational

## Definition

ICT's term for this event is "break in market structure" / "market structure break," not "BOS" or "Break of Structure" — both acronym and expanded phrase are 0 hits across 153 2016-17/2020 packets and 41 2022 episodes (searched `\bBOS\b` and `break of structure`; `break in market structure` returns 12 hits in 11 raw packets, `market structure break` in `ICT-2017-OTE`). A bullish structure break is a candle trading through (2016-17) or closing beyond (2022, preferred) the relevant swing high. ICT uses the identical phrase for **both continuation and reversal** — it is not a continuation-only label. See Common Mistakes.

## Formal Criteria

- The reference swing high must be a confirmed swing high (3-bar pattern). ICT: "short term high" broken (`ICT-2017-OTE` [28:02]).
- 2016-17: names the event ("a market structure break of recent high," `ICT-2016-FAIR-VALUATION` [08:29]; "the point at which market structure broke," `ICT-2016-LIQUIDITY-RUNS` [16:32]) but states no close/trade-through rule either way in either packet.
- 2022: even here, ICT names the plain trade-through itself a break, with no close requirement in that example — "the market creates a short-term low here ... and then it breaks below that; this is key, this is called a break in Market structure" (`ICT-2022-MENTORSHIP-EP02` [27:37]) — and separately wants the breaking move to be energetic, with a close beyond the level stated as a preference, not a hard rule, in the EP06 teaching — see [mss](mss.md) and [displacement-definition](../09-displacement/displacement-definition.md).
- **No continuation-only restriction.** ICT uses "market structure break" for a continuation leg within an up-move ("we have another break above this short term high here," `ICT-2017-OTE` [28:23]) and for the break that follows a stop run at a low, i.e. a reversal context ("break in mark structure rally when we have that, anticipate some measure of buying," `ICT-2017-OTE` [40:37]–[40:56]; "So when this high is broken, that's a break in market structure," `ICT-2017-OTE-FIBER-NYO` [02:46]). One term covers both.
- **Breaking a higher-order (older/more significant) swing high is the MORE convincing break, not a disqualified "stale" one**: "this high being broken right there is much more convincing than this short term here ... so it's a market structure break on an intermediate term high ... much much more reliable" (`ICT-2017-OTE` [34:35]–[35:30]).

## Formula / Math

```
SH_ref = price of the relevant confirmed swing high

# 2016-17: trade-through qualifies (no close requirement stated)
# 2022: close beyond SH_ref is a stated preference, not a hard gate

bullish_structure_break(n) := price_trades_through_or_closes_beyond(SH_ref, n)

# NOT part of ICT's own rule:
#   a continuation-vs-reversal restriction on the term itself
#   a "stale swing" exclusion — the older/higher-order high being broken
#     is treated as MORE significant, not excluded
```

## Machine-Readable

```json
{
  "id": "bos-bullish",
  "category": "01-market-structure",
  "aliases": ["bullish-break-in-market-structure", "bullish-market-structure-break"],
  "criteria": [
    {"id": "c1", "expr": "price_trades_through_or_closes_beyond(SH_ref)"},
    {"id": "c2", "expr": "continuation_only_restriction == false"},
    {"id": "c3", "expr": "breaking_higher_order_swing == more_significant"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["bos-bearish","mss","swing-high","displacement-definition"],
  "sources": ["ICT-2016-FAIR-VALUATION","ICT-2016-LIQUIDITY-RUNS","ICT-2017-OTE","ICT-2017-OTE-FIBER-NYO","ICT-2022-MENTORSHIP-EP02","ICT-2016-REINFORCING-LIQUIDITY"]
}
```

## Visual Pattern

```
                    trade-through / close ✔
                         /
   SH_ref ─────────────┴────  ← prior swing high
              /\
             /  \
            /    \
                  \  /
                   \/
                  pullback
```

Same shape whether the break continues the prior trend or reverses it — ICT names both events "break in market structure."

## Timeframes

Every TF ICT teaches, M1 → W. Higher-TF breaks carry more weight.

## Examples

**Example 1 — continuation (2016-17 style, trade-through):**
- Prior trend bullish; a candle trades through the most recent confirmed swing high.
- → "break in market structure," continuation context (`ICT-2017-OTE` [28:23]).

**Example 2 — reversal, same term (ICT's actual usage):**
- Prior leg down into a stop run at a low; price then breaks the intermediate-term high above.
- → also called "break in market structure" by ICT (`ICT-2017-OTE` [40:37]–[40:56]) — not a separate "CHoCH" label.

## Common Mistakes

- **Treating "BOS" as ICT's acronym and reserving it for continuation only, with reversals relabeled "CHoCH."** Both "BOS"/"break of structure" and "CHoCH" are absent from both corpora; ICT uses one phrase, "break in market structure," for both contexts.
- **Requiring a close, not a trade-through.** 2016-17 material calls the break on the trade-through; 2022 states a close only as a preference. Neither corpus states a hard close-only rule.
- **Inventing an "internal vs. external BOS" distinction for structure breaks.** ICT's internal/external vocabulary applies to **liquidity** ("external range liquidity and internal range liquidity," `ICT-2016-REINFORCING-LIQUIDITY`), not to a separate class of structure break. Do not port that pairing onto this term; see [dealing-range](../05-pd-arrays/dealing-range.md) Common Mistakes for the same caveat.
- **Discounting a break of an older, higher-order swing high as "just continuation through stale structure."** ICT treats that break as MORE significant and reliable, not less (`ICT-2017-OTE` [34:35]–[35:30]).

## ICT vs Community

"BOS" (Break of Structure) and the practice of reserving it for continuation while reversals get "CHoCH" are Smart Money Concepts (SMC) vocabulary. ICT's own phrase, "break in market structure" (also "market structure break"), covers both continuation and reversal contexts and has no continuation-only restriction. This library keeps "BOS" as a labeled cross-reference for readers coming from SMC material, not as ICT's term.

## Related Concepts

- [bos-bearish](bos-bearish.md) — mirror.
- [mss](mss.md) — ICT's interchangeable "shift"/"break" terminology, including this event.
- [swing-high](swing-high.md) — the reference being broken.
- [displacement-definition](../09-displacement/displacement-definition.md) — the 2022 energetic/close-preference filter.

## Citations

- `ICT-2016-FAIR-VALUATION` [08:29] — "a market structure break of recent high" (Sep 2016).
- `ICT-2016-LIQUIDITY-RUNS` [16:32] — "the point at which market structure broke" (Sep 2016).
- `ICT-2017-OTE` [28:02]–[28:23], [34:20]–[35:30], [40:30]–[40:56] — continuation and reversal both called "market structure break"; higher-order break = more reliable.
- `ICT-2017-OTE-FIBER-NYO` [02:46] — "So when this high is broken, that's a break in market structure."
- `ICT-2022-MENTORSHIP-EP02` [27:37] — "this is called a break in Market structure," trade-through, taught in the 2022 mentorship.
- `ICT-2016-REINFORCING-LIQUIDITY` [02:42] — "first let's take a look at external range liquidity and internal range liquidity" — the internal/external pairing is liquidity, not a structure-break sub-taxonomy (Dec 2016).
