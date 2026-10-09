# Bearish Structure Break

**Category:** 01-market-structure
**Aliases:** bearish break in market structure, bearish market structure break, Break of Structure / BOS (SMC term — "BOS" and "break of structure" are 0 hits in corpus; ICT says "break in market structure")
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-OPEN-FLOAT-L12, ICT-2022-MENTORSHIP-EP12, ICT-2016-USDX-SMT, ICT-2017-OTE
**Tags:** structure, break, bearish, foundational

## Definition

Mirror of [bos-bullish](bos-bullish.md). ICT's term is "break in market structure" / "market structure break," not "BOS" or "Break of Structure" (both 0 hits in 153 2016-17/2020 packets and 40 captioned 2022 episodes). A bearish structure break is a candle trading through (2016-17) or closing beyond (2022, preferred) the relevant swing low. ICT uses the identical phrase for both continuation and reversal contexts.

## Formal Criteria

- The reference swing low must be a confirmed swing low.
- 2016-17: called on the trade-through — "When price traded below that low, that was a break in market structure. ... So we had a market shift below that low." (`ICT-2017-OPEN-FLOAT-L12` [07:38]–[07:45]).
- 2022: energetic move preferred, close stated as a preference, not a hard rule (see [mss](mss.md)).
- **No continuation-only restriction.** ICT's significance distinction is scope, not direction: "if we have a break below and any return low then we have what — a significant break in Market structure — this is something that's more significant just simply than going into a chart saying okay well it took out a short-term low" (`ICT-2022-MENTORSHIP-EP12` [31:09]).
- A break below a short-term low is read as a liquidity event (stop run) that can precede a reversal higher, not automatically "continuation": "when the market trades back below that short-term low it's going to gather up sell stops to pair new buying with and it'll most likely trade higher and make a new higher high" (`ICT-2016-USDX-SMT` [04:59]–[05:05]).
- Breaking a higher-order (older) swing low is the MORE significant break, mirroring the bullish case (`ICT-2017-OTE` [34:35]–[35:30]).

## Formula / Math

```
SL_ref = price of the relevant confirmed swing low

bearish_structure_break(n) := price_trades_through_or_closes_beyond(SL_ref, n)

# NOT part of ICT's own rule:
#   a continuation-vs-reversal restriction on the term itself
#   an "internal vs external BOS" sub-taxonomy (ICT's internal/external
#     vocabulary applies to liquidity, not to structure breaks — see
#     bos-bullish Common Mistakes)
```

## Machine-Readable

```json
{
  "id": "bos-bearish",
  "category": "01-market-structure",
  "aliases": ["bearish-break-in-market-structure", "bearish-market-structure-break"],
  "criteria": [
    {"id": "c1", "expr": "price_trades_through_or_closes_beyond(SL_ref)"},
    {"id": "c2", "expr": "continuation_only_restriction == false"},
    {"id": "c3", "expr": "break_can_precede_reversal == true"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["bos-bullish","mss","swing-low","displacement-definition"],
  "sources": ["ICT-2017-OPEN-FLOAT-L12","ICT-2022-MENTORSHIP-EP12","ICT-2016-USDX-SMT","ICT-2017-OTE"]
}
```

## Visual Pattern

```
              \/
              /\
             /  \
            /    \
   SL_ref ──┴──────── ← prior swing low
                   \
                    \
                     trade-through / close ✔
```

Same shape whether read as continuation or as a stop run that precedes a reversal — ICT names the event "break in market structure" either way.

## Timeframes

Every TF M1 → W. HTF breaks carry more structural weight.

## Examples

**Example 1 — the break event itself (2016-17 style):**
- Price trades below the relevant confirmed swing low.
- → "break in market structure" / "market shift below that low" (`ICT-2017-OPEN-FLOAT-L12` [07:38]–[07:45]), regardless of whether the prior leg was up or down.

**Example 2 — break read as a stop run, not automatic continuation:**
- Price trades below a short-term low, gathering sell stops.
- ICT: this "most likely" sets up new buying and a higher high (`ICT-2016-USDX-SMT` [04:59]–[05:05]) — the opposite of a continuation-only reading.

## Common Mistakes

- **Treating "BOS" as ICT's acronym, reserved for continuation, with reversals relabeled "CHoCH."** Neither "BOS"/"break of structure" nor "CHoCH" appears in either corpus; ICT uses one phrase for both.
- **Requiring a close, not a trade-through.** See [bos-bullish](bos-bullish.md) Common Mistakes — the same era-split applies here.
- **Assuming a break below a swing low is automatically bearish continuation.** ICT reads it as a liquidity/stop-run event that often precedes a higher high (`ICT-2016-USDX-SMT` [04:59]–[05:05]).
- **Inventing "internal vs external BOS."** ICT's internal/external vocabulary names liquidity, not structure breaks.
- **Stale swing low.** The most recent swing low is the default reference; a break of an older, higher-order low is a more significant event, not a disqualified one.

## ICT vs Community

Same note as [bos-bullish](bos-bullish.md): "BOS" and the continuation/CHoCH split are SMC vocabulary, kept here only as a labeled cross-reference, not attributed to ICT.

## Related Concepts

- [bos-bullish](bos-bullish.md) — mirror.
- [mss](mss.md) — ICT's interchangeable "shift"/"break" terminology.
- [swing-low](swing-low.md) — the reference.
- [displacement-definition](../09-displacement/displacement-definition.md) — the 2022 energetic/close-preference filter.

## Citations

- `ICT-2017-OPEN-FLOAT-L12` [07:38]–[07:45] — "break in market structure" on trade-through below a swing low (Jan 2017).
- `ICT-2022-MENTORSHIP-EP12` [31:09] — significance distinction is scope, not continuation/reversal.
- `ICT-2016-USDX-SMT` [04:59]–[05:05] — a break below a short-term low read as a stop run preceding a higher high (Nov 2016).
- `ICT-2017-OTE` [34:35]–[35:30] — breaking the higher-order swing is the more significant/reliable break.
