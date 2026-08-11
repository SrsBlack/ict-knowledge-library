# Propulsion Block

**Category:** 07-order-blocks
**Aliases:** PB, propulsion candle, order block on an order block
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2024
**Source IDs:** ICT-2016-PROPULSION-BLOCK, ICT-2018-BLOCKS, ICT-2024-PROPULSION-BLOCKS
**Tags:** order-block, propulsion, nesting, mean-threshold, entry

⚠ **Definition reversed and re-dated 2026-08-10 against the primary source.** This page previously
defined the propulsion block as a **wide-body candle aligned with the displacement** — "the takeoff
candle, not the absorption candle" — introduced in **2018**. Both claims are contradicted by the
December-2016 lecture in which ICT names the concept: it is a **down-close candle that trades back
into a previous down-close candle** (bullish case) — direction-**opposite** to the displacement, an
order block sitting on an order block — and ICT coins the label in that lecture: "that's why I gave
you the name; it's a propulsion candle because it **propels price quickly and suddenly**"
(`ICT-2016-PROPULSION-BLOCK`, [07:20–07:28]). The former wide-body / minimal-wick / FVG-inside
criteria are **not supported by any primary source in this corpus** and have been removed. The two
later source IDs are retained as re-teach pointers only; they are registry stubs with no distilled
content behind them.

## Definition

A propulsion block is a **candle of the same colour as an existing order block that trades back into
that order block**, taking over its role at a higher (bullish) or lower (bearish) level. ICT:
"a propulsion block is a candle or bar that is previously traded down into a down candle or bullish
order block and **takes over the role of price support for higher price movement**"
(`ICT-2016-PROPULSION-BLOCK`, [00:31–00:38]).

The qualifying condition is the nesting, not the size: "what makes it propulsion is that it's already
dropped back down into an order block that's **already predisposed to go higher**" [01:02–01:11];
"all it is is a **down closed candle that trades down into a previous down closed candle**"
[04:39–04:46]. The result is a highly sensitive level whose defining behaviour is an immediate,
violent departure — "the market will show a **sudden and violent movement away** from that down
candle" [02:02–02:08] — with "**very little drawdown, immediate price responsiveness**" [07:28–07:31].

It is taught as part of the Dec-2016 order-block series: "we're going to be continuing our discussion
on **reinforcing order block theory**" [00:22].

## Formal Criteria

**Bullish propulsion block**

- A **bullish order block** already exists — the last down-close candle (or a run of consecutive
  down candles treated as one block) before an up move that trades through the highest of those down
  candles: "this candle here trades through the highest of the down candles, so that **confirms this
  is a bullish order block**" [03:40–03:48].
- A **later down-close candle trades back down into that order block**: "we have a new down close
  candle that trades right back into it… **that candle becomes a propulsion candle**" [00:51–01:02].
- The **underlying context must be bullish**: "what makes it a propulsion candle is that we are
  trading another down candle into a previous down candle **when the underlying context is bullish**"
  [04:00–04:07].
- **Entry reference is the propulsion candle's high**, not its body: "it just trades down into the
  **high of the candle** and it immediately explodes; it may go **a pip or two below the high** of
  that particular down candle" [01:51–02:02].
- The **mean threshold must hold**: "it should **never see the mean threshold break** — half of the
  body's height or the middle of the range of that candle's body; that mean threshold should **not
  give way**" [01:24–01:31]. A deeper fill to the mean threshold is *tolerated but not expected*:
  "we are willing to allow this still trade down in the middle of the range or mean threshold, but
  **it very most likely will never do that**" [01:41–01:51].
- **Invalidation:** "if this loses its mean threshold, chances are it's probably **not a good trade**"
  [05:21–05:26]. The consequence is stated explicitly: either sideline, or "many times **looking for a
  reversal to go short**" [05:34–05:41].

**Bearish propulsion block** — the exact mirror. Frame a higher **bearish order block** (the last
up-close candle before the down move); price moves lower, then "we trade right back to this order
block right here — **this candle becomes the propulsion candle**" [06:11–06:19]. Two entries are
shown: the **mean threshold** — "we can cut that candle in half right here… **mean threshold**,
trades immediately lower" [06:20–06:30] — and, at a later retest, the candle's **low**: "it doesn't
need to go up to the body; it's the **low of the candle** on the propulsion candle, it's going to be
very, very sensitive" [07:09–07:15].

**Stop-loss consequence.** Because the mean threshold is both the tolerance limit and the
invalidation line, "you can have a really **ultra tight stop loss** on your long entry, or you can
have **immediate feedback that you're on the wrong side** of the marketplace" [05:26–05:34].

## Formula / Math

```
# Variables: O_n, H_n, L_n, C_n = open/high/low/close of candle n.

# --- the underlying order block (bullish case) ---
OB := the last down-close candle, or a run of k consecutive down candles
      treated as ONE block, before an up move that satisfies
      max(H over the up move) > max(H_i for i in OB)      # "trades through the highest"
OB_high := max(O_i for i in OB)
OB_low  := min(C_i for i in OB)

# --- the propulsion candle ---
bullish_propulsion(n) :=
      C_n < O_n                        # a down-close candle
  AND L_n <= OB_high                   # it trades back down into the prior OB
  AND context_is_bullish == true

pb_high := O_n                         # body top of a down-close candle
pb_low  := C_n
pb_mt   := (O_n + C_n) / 2             # mean threshold

# --- entry and invalidation ---
entry_primary   := touch of H_n        # "trades down into the high of the candle"
entry_tolerated := touch of pb_mt      # allowed, but "most likely it will never do that"
overshoot_ok    := H_n - price <= ~2 pips
invalidated     := price < pb_mt       # mean threshold gives way -> stand aside or reverse

# Bearish mirror: C_n > O_n ; H_n >= OB_low ; entry at L_n or pb_mt ;
#                 invalidated when price > pb_mt.
```

## Machine-Readable

```json
{
  "id": "propulsion-block",
  "category": "07-order-blocks",
  "aliases": ["PB", "propulsion-candle", "order-block-on-an-order-block"],
  "criteria": [
    {"id": "c1", "expr": "candle_colour == colour_of_prior_order_block (down-close for bullish, up-close for bearish)"},
    {"id": "c2", "expr": "candle trades back into the range of a pre-existing order block of the same polarity"},
    {"id": "c3", "expr": "underlying_context aligned with that order block (bullish for a bullish PB)"},
    {"id": "c4", "expr": "entry_reference := high(n) for bullish, low(n) for bearish; overshoot of a pip or two permitted"},
    {"id": "c5", "expr": "mean_threshold := (open(n)+close(n))/2 is tolerated as a deeper fill but expected to hold"},
    {"id": "c6", "expr": "close beyond mean_threshold => trade invalid; stand aside or look for the reversal"},
    {"id": "c7", "expr": "expected behaviour := sudden violent departure with very little drawdown"},
    {"id": "c8", "expr": "prior order block may be a run of consecutive same-colour candles treated as one block"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2024",
  "related": ["bullish-order-block","bearish-order-block","order-block-criteria","mean-threshold","vacuum-block","pd-array-nesting","displacement-definition"],
  "sources": ["ICT-2016-PROPULSION-BLOCK","ICT-2018-BLOCKS","ICT-2024-PROPULSION-BLOCKS"]
}
```

## Visual Pattern

```
   BULLISH PROPULSION BLOCK  (an order block sitting on an order block)

      ▼ ▼ ▼        three consecutive down candles = ONE bullish OB
      ▼ ▼ ▼            ▲
                       ▲   up move trades through the HIGHEST of them
                       ▲   -> the OB is confirmed
                          ▼   <-- a NEW down-close candle drops back
                          ▼       into that OB = the PROPULSION CANDLE
      ─────────────── H_n  <-- entry reference (the candle's HIGH)
      ─ ─ ─ ─ ─ ─ ─ ─ MT   <-- tolerated depth AND the invalidation line
      ─────────────── C_n
                            ▲▲▲▲  sudden, violent departure,
                           ▲      very little drawdown

   BEARISH MIRROR: an up-close candle trading back up into a bearish OB.
   Entry at MT on the first touch, or at the candle's LOW on a later retest.
   "It doesn't need to go up to the body."
```

## Timeframes

The worked bullish example is a **15-minute chart**, with ICT noting he would have preferred a
higher tier: "this is a 15 minute time frame — I don't have a way of showing you a **45 minute
chart** here, but it's the same price action" [04:46–04:54]. No timeframe restriction is stated;
M15–D is the practical range for a construction that depends on candle bodies.

## Examples

**Example 1 — bullish, M15 (03:15–04:39):**
- Setup: three consecutive down candles into a level short of equilibrium, framed together as one
  bullish order block; the following candle "trades through the highest of the down candles",
  confirming it.
- Trigger: the next candle rallies, then the one after opens and trades down into that block and
  closes down — "when this candle creates the down close and closes, **this becomes a propulsion
  candle**".
- Retest: "this candle opens, trades down into it right there. **The open comes in at 133.45. The
  low on this candle comes in at 133.45.** Goes right to that candle."
- Outcome: "that's a bullish entry here with a propulsion candle."

**Example 2 — bearish (05:41–07:20):**
- Setup: a higher bearish order block; price trades up into it and breaks down. The last up candle
  before that break is itself a bearish order block referencing the higher one.
- Trigger: price moves lower, then returns to that order block — "this candle becomes the propulsion
  candle right there."
- Entry A: the mean threshold — "we can cut that candle in half right here. Boom. Hits it right
  there. Mean threshold. Trades immediately lower."
- Entry B: a later retest of the candle's **low**, after price has broken below it — "you have to see
  it break below this candle's low, which it does here… then trades right back up into this candle's
  low… hits it, immediate, quick responsiveness."

## Common Mistakes

- **Calling the displacement candle a propulsion block.** This is the error the previous version of
  this page encoded. The propulsion candle is **opposite** in colour to the move it launches — a
  *down* candle in a bullish context, an *up* candle in a bearish one.
- **Requiring a wide body, a small wick, or an FVG inside it.** None of these appear in the primary
  source. The only size-adjacent statement in the lecture concerns the *order block*'s framing, not
  the propulsion candle's.
- **Missing the nesting requirement.** A down-close candle that has **not** traded into a prior
  bullish order block is an ordinary order block, not a propulsion block. The nesting *is* the concept.
- **Entering at the body when the high is the reference.** ICT's bullish first-touch level is the
  candle's **high**; the mean threshold is the deeper allowance, not the plan.
- **Holding through a mean-threshold break.** The mean threshold is the invalidation. Its loss is
  treated as a signal to stand aside or reverse, not as a drawdown to absorb.
- **Framing the order block as a single candle when it is a run.** Consecutive same-colour candles
  before the move are framed as one block — "this is all one bullish order block because it is all
  down price movement" [03:34–03:37].

## Related Concepts

- [bullish-order-block](bullish-order-block.md), [bearish-order-block](bearish-order-block.md) — the block the propulsion candle nests into.
- [order-block-criteria](order-block-criteria.md) — the multi-candle framing and the "trades through the highest" confirmation rule.
- [mean-threshold](../27-equilibrium/mean-threshold.md) — the tolerance limit and invalidation line.
- [vacuum-block](vacuum-block.md) — the other named block from the same Dec-2016 series.
- [pd-array-nesting](../05-pd-arrays/pd-array-nesting.md) — the general array-inside-array principle this is a single-candle case of.
- [displacement-definition](../09-displacement/displacement-definition.md) — the move the propulsion candle precedes, not the move itself.

## Citations

- `ICT-2016-PROPULSION-BLOCK` (00:22) "we're going to be continuing our discussion on reinforcing order block theory"; (00:31–00:38) "a propulsion block is a candle or bar that is previously traded down into a down candle or bullish order block and takes over the role of price support for higher price movement"; (00:51–01:02) the new down-close candle trading back in "becomes a propulsion candle"; (01:02–01:11) "what makes it propulsion is that it's already dropped back down into an order block that's already predisposed to go higher"; (01:24–01:31) "it should never see the mean threshold break — half of the body's height or the middle of the range of that candle's body"; (01:41–01:51) the mean threshold tolerated but "very most likely it will never do that"; (01:51–02:02) entry at the candle's high, "a pip or two below" permitted; (02:02–02:08) "a sudden and violent movement away from that down candle"; (02:37–03:23) three consecutive down candles framed as one bullish order block; (03:40–03:48) "trades through the highest of the down candles, so that confirms this is a bullish order block"; (04:00–04:07) "when the underlying context is bullish"; (04:26–04:34) the 133.45 open-and-low retest; (04:39–04:46) "all it is is a down closed candle that trades down into a previous down closed candle"; (04:46–04:54) the 15-minute chart and the 45-minute preference; (05:21–05:41) mean-threshold loss as invalidation, sideline or reverse; (05:26–05:34) the ultra-tight stop; (05:41–06:30) the bearish mirror and the mean-threshold entry; (07:09–07:15) "it doesn't need to go up to the body; it's the low of the candle"; (07:20–07:31) "that's why I gave you the name… it propels price quickly and suddenly… very little drawdown, immediate price responsiveness".
- `ICT-2018-BLOCKS`, `ICT-2024-PROPULSION-BLOCKS` — registry stubs recording later re-teaches. ⚠ No distilled primary content sits behind either; do not quote criteria from them.
