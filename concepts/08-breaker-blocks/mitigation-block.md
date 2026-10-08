# Mitigation Block

**Category:** 08-breaker-blocks
**Aliases:** MB, mitigation
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-MITIGATION-BLOCKS, ICT-2017-HTF-PD-ARRAYS, ICT-2016-INSTITUTIONAL-ORDER-FLOW, ICT-2017-SWING-BEAR-SETUPS
**Tags:** mitigation-block, breaker-related, foundational

⚠ **Rewritten 2026-10-08, confidence raised medium → high; candle colour and zone corrected again in
review.** The 2026-10-08 first pass still had the mitigation candle's colour backwards in places and
drew the zone on the wick range; both are fixed below. See
[breaker-vs-mitigation](breaker-vs-mitigation.md) for the breaker/mitigation-block contrast.

## Definition

A mitigation block forms after a **failure swing** that produces a **market structure shift** — the
"M pattern": "referred to as an M pattern … why? Because it looks like a giant M. Okay, well, when you
have this pattern here, it's a **failure swing** with a **confirmation break in market structure**."
(`ICT-2016-MITIGATION-BLOCKS` [02:44–03:01]; ⚠ "M pattern" is ICT's own term for the bearish case —
the mirror bullish case is this page's inferred label "W pattern", not attested anywhere in the
corpus). Once that shift posts, attention moves to the **last DOWN candle** inside the low framed by
the failure swing: "once price posts a market structure shift lower, your attention as the trader
moves to this specific low in price. Inside that low, what we're going to be focusing on is the
**last down candle**. Because the last down candle is where the buying took place right before that
little short-term rally up." [04:00–04:23]. ⚠ **This candle — the LAST DOWN candle — is the
mitigation candle** (not an up candle: a prior pass at this page described it as "last up-colour",
which is backwards). It DOES flip polarity: "that last down candle will give us a bearish level to
sell into." [05:02]; "what we're seeing is the classic support broken turns resistance." [08:57].
Jan-2017 confirms the failure-swing lineage: "that short term little swing low at the failure swing —
that's going to be what? A potential mitigation block. That means any orders that were used to go
long but failed to make another pass at that old high, they're underwater now."
(`ICT-2017-HTF-PD-ARRAYS` [07:46–07:53]).

**"Mitigating" refers to trapped counter-trend positions being closed, not trend-following hedges:**
"the long positions taken from A to B price swing will have an opportunity to liquidate or mitigate
their losses" [05:33–05:53]; the behaviour is named "buyer's remorse": "every time price moves back
to an old low, [what's] actually happening is it's referred to as buyer's remorse." [09:04].

**The zone is the candle's body**, not its full wick-to-wick range, and the hallmark is that the body
holds on the return: "it's inside the body of the candle, which is what a mitigation block
represents" [12:32]; "the bodies, the whole entire candle is used, not just the bottom" [13:51];
"notice the body of the candle is not violated. **This is the hallmark characteristics of a
mitigation block.**" [14:29–14:32]. Stop placement sits **above the candle's high** (bearish case):
"our stop has to be somewhere above the down candle … that high on this candle comes in at 112.89,
so it needs to be above that." [14:01–14:09].

Mitigation blocks sit lower in the array stack than breakers and are grouped with them: "mitigation
and breakers are basically mitigation blocks, but generally mitigation blocks can occur lower than
breakers." (`ICT-2017-HTF-PD-ARRAYS` [20:55–20:58]); "small little bounces in bear markets would be a
mitigation block, basically." [21:03]. ICT groups the bearish mitigation block among the premium
arrays a bear-market practitioner checks: "and any bearish mitigation block" (`ICT-2017-SWING-BEAR-SETUPS`
[01:37–02:14]); Nov-2016 attests the body-wick distinction a month earlier: "so this wick down to the
body is a mitigation block." (`ICT-2016-INSTITUTIONAL-ORDER-FLOW` [19:11]).

## Formal Criteria

- A **failure swing** occurs — the extreme in the prior direction is never reached, forming the
  "M pattern" (ICT's own term, bearish case) — or its mirror (this page's inferred, unattested "W
  pattern" label, bullish case).
- The failure swing produces a **market structure shift**.
- Attention shifts to the **last DOWN-close candle** inside the low framed by the failure swing
  (bearish case; mirror: last UP-close candle inside the high, for the bullish case).
- That candle's **body** — "the whole entire candle … not just the bottom" — is the mitigation zone,
  not its wick-to-wick range.
- **Polarity flips**: the down candle, formerly a bullish-looking reference, becomes a **sell**
  level — classic support-broken-turns-resistance.
- **Hallmark confirmation**: on the return visit, the candle's **body is not violated** — a close
  through the body invalidates the read.
- Stop sits beyond the candle's far extreme — **above its high**, for the bearish case.

## Formula / Math

```
failure_swing := prior-direction extreme NOT reached, confirmed by a market structure shift
                  ("M pattern" — ICT's term, bearish case; mirror bullish case has no attested name)

mitigation_candle := the LAST DOWN-CLOSE candle inside the low framed by the failure swing
                      (bearish case; mirror: last UP-close candle inside the high, bullish case)
mitigation_zone := [min(open,close), max(open,close)]     # the candle's BODY, not low(n)/high(n)

polarity_flip := true      # the candle's role REVERSES (classic support broken -> resistance)

hallmark := on retest, close does NOT violate the candle's body
stop := above high(mitigation_candle)     # bearish case; mirror: below low(candle), bullish case

mitigation_confirmed := failure_swing AND structure_shift AND hallmark
```

## Machine-Readable

```json
{
  "id": "mitigation-block",
  "category": "08-breaker-blocks",
  "aliases": ["MB", "mitigation"],
  "criteria": [
    {"id": "c1", "expr": "a failure swing (M pattern, bearish case) produces a market structure shift"},
    {"id": "c2", "expr": "mitigation_candle := the LAST DOWN-CLOSE candle inside the low framed by the failure swing (bearish case; mirror: last up-close candle, bullish case)"},
    {"id": "c3", "expr": "mitigation_zone := the candle's BODY only (min/max of open,close), NOT the wick-to-wick range"},
    {"id": "c4", "expr": "POLARITY FLIPS (classic support broken turns resistance, and mirror)"},
    {"id": "c5", "expr": "hallmark: on retest the candle's body is NOT violated by a close"},
    {"id": "c6", "expr": "stop placed above the candle's high (bearish case; mirror: below the low, bullish case)"}
  ],
  "timeframes": ["M30"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["breaker-block","breaker-vs-mitigation","bullish-order-block","bearish-order-block","mitigated-order-block"],
  "sources": ["ICT-2016-MITIGATION-BLOCKS","ICT-2017-HTF-PD-ARRAYS","ICT-2016-INSTITUTIONAL-ORDER-FLOW","ICT-2017-SWING-BEAR-SETUPS"]
}
```

## Visual Pattern

```
   mitigation block ("M pattern" -> bearish mitigation block):

        ╱╲            ← failure swing: second high fails to exceed the first (M)
       ╱  ╲                market structure shift DOWN confirms it
      ╱    ╲___
     ╱         ▼  ← the LAST DOWN-CLOSE candle inside the low framed by the
    ╱          ▼     failure swing = the mitigation candle; its BODY (not the
                ▼     wick-to-wick range) is the zone
                 ╲
                  ╲→ price returns; body holds (not violated) -> sell reaction
                      (classic support broken turns resistance)
```

## Timeframes

The lecture's worked example is explicitly a **30-minute chart**: "let's take a look at a 30 minute
chart on the same price action." [13:13]. No other timeframe is named in this lecture (searched
"minute|hour|daily|weekly": the only hit); no floor or ceiling is otherwise stated.

## Examples

**Example 1 — bearish mitigation block (schematic, following the lecture's M-pattern, worked on the
30-minute chart):**
- An M-pattern failure swing posts a market structure shift down.
- The last DOWN-close candle inside the low framed by that failure swing becomes the mitigation
  candle; ICT's worked example pins its high at 112.89.
- Price returns later; the candle's body holds (not violated) — the hallmark confirmation.
- Sell reaction confirmed; stop placed above 112.89.

## Common Mistakes

- **"No polarity flip; continuation reference."** Contradicted directly — "classic support broken
  turns resistance" [08:57] is a flip.
- **"BOS, not CHoCH, precedes it."** `CHoCH`/`BOS` are SMC-community terms with 0 hits in either
  corpus; ICT's own term for the antecedent is a **market structure shift** at a **failure swing**.
- **Mitigation candle is an up-close candle.** It is the last **DOWN**-close candle (bearish case) —
  a prior pass of this page had this backwards.
- **Drawing the zone on the wick-to-wick range.** The zone is the candle's **body** only; a wick
  violation does not disqualify the read, only a close through the body does.
- **Calling it a continuation/hedge reference.** "Mitigating" names trapped counter-trend positions
  unwinding (buyer's remorse), not trend-following hedges.
- **Alias "hedge block."** Not attested anywhere in either corpus; "hedging" appears only in an
  unrelated reclaimed-order-block discussion.
- **"W pattern" as ICT's term for the bullish mirror.** Not attested; ICT only names the bearish-case
  "M pattern" in this lecture. Treat "W pattern" as this page's inferred label, not ICT's vocabulary.

## Related Concepts

- [breaker-block](breaker-block.md), [breaker-vs-mitigation](breaker-vs-mitigation.md), [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [mitigated-order-block](../07-order-blocks/mitigated-order-block.md).

## Citations

- `ICT-2016-MITIGATION-BLOCKS` [00:28] "an implication of order block theory"; [02:44–03:01] the M pattern / failure swing with a confirmation break in market structure; [04:00–04:23] attention moves to the last DOWN candle inside the low, "because the last down candle is where the buying took place"; [05:02] "that last down candle will give us a bearish level to sell into"; [05:33–05:53] trapped longs liquidating/mitigating; [08:57] "classic support broken turns resistance"; [09:04] "buyer's remorse"; [12:32] "it's inside the body of the candle, which is what a mitigation block represents"; [13:13] worked on a 30-minute chart; [13:51] "the bodies, the whole entire candle is used, not just the bottom"; [14:01–14:09] stop above the candle's high; [14:29–14:32] "notice the body of the candle is not violated — this is the hallmark characteristics of a mitigation block."
- `ICT-2017-HTF-PD-ARRAYS` [07:46–07:53] failure-swing lineage, orders underwater; [20:55–21:03] mitigation blocks grouped with and occurring lower than breakers.
- `ICT-2016-INSTITUTIONAL-ORDER-FLOW` [19:11] "this wick down to the body is a mitigation block" (Nov 2016, one month before the dedicated lecture).
- `ICT-2017-SWING-BEAR-SETUPS` [01:37–02:14] bearish mitigation block enumerated among the premium PD arrays.
