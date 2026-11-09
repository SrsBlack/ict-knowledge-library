# Mitigation — Definition

**Category:** 18-mitigation
**Aliases:** mitigation, mitigate (a loss / a position)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-MITIGATE-LOSING-TRADES, ICT-2016-INSTITUTIONAL-ORDER-FLOW, ICT-2016-BREAKER-BLOCK, ICT-2016-MITIGATION-BLOCKS, ICT-2016-FVG-REINFORCED, ICT-2022-MENTORSHIP-EP16
**Tags:** mitigation, foundational, terminology

⚠ **Rewritten 2026-11-09 against ICT's own words.** The prior version defined mitigation as a
zone's **state change** from "fresh" to "tested", with per-structure thresholds (FVG at CE, OB at
mean threshold, breaker at the body) and a rule that a second visit is lower-probability. **None of
that is in the corpus.** Outside the PD-array name ("mitigation block", sometimes shortened to
"mitigation"), every corpus use of "mitigate" is about **a position or a loss**, never a price zone's
state. Searched `mitigat*` across 153 2016-17/2020-21 packets and 40 captioned 2022 Mentorship episodes:
the 2022 episodes use it only in the block name (ep16 [34:25], ep25 [51:33], [52:54]); the 2016-17
packets use it for traders closing losing positions or for recovering one's own loss (2016 lectures
below; same sense in 2017, e.g. the packet "Pattern Recognition - Failed OTE & FOMC Mitigation
Example" [08:17], "my loss … was completely mitigated"). The nearest non-position wording, "Every rally
that sees lower prices needs to be mitigated" (`ICT-2016-MITIGATION-BLOCKS` [11:49]), reads as the
positions behind the rally from context ([11:58], sell on the return). No packet calls a gap, block or
zone "mitigated" or "unmitigated". The fresh/tested state machine is a community convention. Re-dated 2017 → 2016.

## Definition

**Mitigation** in ICT's vocabulary is **reducing or offsetting a loss**. He uses it in two senses:

1. **Market participants mitigating losing positions** — traders (or "smart money") who are
   underwater wait for price to come back to their entry and close there. This is the mechanism ICT
   gives for why old swing points and blocks react on a return:
   - "The buyers that buy this low and later see this same swing low violated will look to mitigate
     the loss." (`ICT-2016-BREAKER-BLOCK` [03:22])
   - "They'll wait for price to get back to an area where they can mitigate those shorts and add new
     longs." (`ICT-2016-BREAKER-BLOCK` [09:39]); the breaker itself is "this form of mitigation" ([00:26]).
   - "the long positions taken from A to B price swing will have an opportunity to liquidate or
     mitigate their losses" (`ICT-2016-MITIGATION-BLOCKS` [05:33]–[05:53]); "They're going to want to
     mitigate those losses at that candle." ([13:39])
   - "So they're mitigating the longs they use to buy the price higher. They take those orders off."
     (`ICT-2016-INSTITUTIONAL-ORDER-FLOW` [15:11]–[15:15]); "the shorts that they have on, they have
     to take those off and mitigate them" ([19:06]).
2. **The trader mitigating their own losing trade** — risk-management sense, recovering a prior loss
   on the next trade: "our losing trade that we just had using half of the initial risk is already
   mitigated" (`ICT-2016-MITIGATE-LOSING-TRADES` [07:39]); "Once it's been mitigated, you're going to
   lock that in." ([09:42]). See
   [loss-mitigation-half-size-reentry](../32-risk-management/loss-mitigation-half-size-reentry.md).

What ICT does **not** do is call a zone "mitigated" after price touches it. For an FVG his words are
"rebalance", "close in" and "fill" — see [fvg-mitigation](../06-fair-value-gaps/fvg-mitigation.md).

## Formal Criteria

- Sense 1 is an **explanation of behaviour** at a [breaker-block](../08-breaker-blocks/breaker-block.md)
  or [mitigation-block](../08-breaker-blocks/mitigation-block.md), not a separate chart event. The
  observable event is the **return of price to that block**; "mitigation" is ICT's account of who
  trades there and why.
- ICT gives **no** per-structure "mitigated" threshold (CE, mean threshold, body touch) and no
  fresh → tested → consumed lifecycle.
- A re-visited zone is not retired: ICT trades the 104.75 level a second time while "it's hitting that
  fair value gap also … trading into the fair value gap" (`ICT-2016-FVG-REINFORCED` [10:04],
  [10:42]–[10:47]); "Here's the first time it trades up into that 104.75 level. Closing that fair value
  gap. And then here's the second time it trades up into it." ([11:51]–[11:57]).

## Formula / Math

```
# ICT's usage (2016 corpus): mitigate = close / offset a losing position
participant_mitigates(position) := position.underwater
                                   AND price returns to position.entry_area
                                   AND position is closed there

# NOT ICT's (removed 2026-11-09, no corpus source):
#   default_mitigation_threshold = {FVG: CE, OB: MT, breaker: body}
#   state in {fresh, tested, consumed}; "second visit = lower probability"
```

Any zone-state machine is the user's own convention and should be labelled that way.

## Machine-Readable

```json
{
  "id": "mitigation-definition",
  "category": "18-mitigation",
  "aliases": ["mitigation", "mitigate"],
  "criteria": [
    {"id": "c1", "expr": "mitigate == traders close or offset a losing position (usually at its entry on a return of price)"},
    {"id": "c2", "expr": "ICT gives no per-structure 'mitigated' threshold or fresh/tested lifecycle"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["mitigation-block","breaker-block","fvg-mitigation","loss-mitigation-half-size-reentry","mitigation-of-ob","mitigation-of-fvg","mitigation-of-breaker","partial-vs-full-mitigation"],
  "sources": ["ICT-2016-MITIGATE-LOSING-TRADES","ICT-2016-INSTITUTIONAL-ORDER-FLOW","ICT-2016-BREAKER-BLOCK","ICT-2016-MITIGATION-BLOCKS","ICT-2016-FVG-REINFORCED","ICT-2022-MENTORSHIP-EP16"]
}
```

## Visual Pattern

```
   Bearish mitigation block (ICT-2016-MITIGATION-BLOCKS):

        A  old high (not re-taken: failure swing)
       / \      B
      /   \    / \
     /     \  /   \         longs bought A->B are now underwater
            \/     \
                    \  C    price returns to their entry candle;
                     \/     they "mitigate those losses" there -> sell
```

## Timeframes

All.

## Examples

- **Breaker** (`ICT-2016-BREAKER-BLOCK` [03:22]–[03:29]): buyers of a swing low that is later violated
  "will look to mitigate the loss. When price returns back to the swing low this is a bearish trade
  setup worth considering."
- **Own trade** (`ICT-2016-MITIGATE-LOSING-TRADES` [07:29]–[07:39]): a half-size re-entry reaches the
  R multiple that repays the prior loss, and the loss is "already mitigated".

## Common Mistakes

- **Calling a zone "mitigated" when price touches it.** That is community vocabulary, not ICT's.
- **Treating the old CE / MT / body thresholds as ICT's rule.** They were this library's own and have
  been removed. Child pages ([mitigation-of-ob](mitigation-of-ob.md),
  [mitigation-of-fvg](mitigation-of-fvg.md), [mitigation-of-breaker](mitigation-of-breaker.md),
  [partial-vs-full-mitigation](partial-vs-full-mitigation.md)) have **not yet been audited** and may
  still use the zone-state sense.
- **Counting "mitigation" as an extra signal.** It is ICT's explanation of a return to a block, not
  an additional observation.

## Related Concepts

- [mitigation-block](../08-breaker-blocks/mitigation-block.md), [breaker-block](../08-breaker-blocks/breaker-block.md), [fvg-mitigation](../06-fair-value-gaps/fvg-mitigation.md), [loss-mitigation-half-size-reentry](../32-risk-management/loss-mitigation-half-size-reentry.md).
- Unaudited: [mitigation-of-ob](mitigation-of-ob.md), [mitigation-of-fvg](mitigation-of-fvg.md), [mitigation-of-breaker](mitigation-of-breaker.md), [partial-vs-full-mitigation](partial-vs-full-mitigation.md).

## Citations

- `ICT-2016-BREAKER-BLOCK` [00:26], [03:22]–[03:29], [09:39].
- `ICT-2016-MITIGATION-BLOCKS` [05:33]–[05:53], [13:39].
- `ICT-2016-INSTITUTIONAL-ORDER-FLOW` [15:11]–[15:15], [19:06].
- `ICT-2016-MITIGATE-LOSING-TRADES` [07:29]–[07:39], [09:42].
- `ICT-2016-FVG-REINFORCED` [10:04], [10:42]–[10:47], [11:51]–[11:57].
- `ICT-2022-MENTORSHIP-EP16` [34:25].
