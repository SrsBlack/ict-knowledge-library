# Order Block — Criteria

**Category:** 07-order-blocks
**Aliases:** OB criteria, order block rules, OB qualification
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-OB-INTRO, ICT-2016-PROPULSION-BLOCK, ICT-2017-SWING-BEAR-SETUPS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-block, criteria, foundational, multi-candle, mean-threshold

## Definition

An Order Block (OB) is the **last opposite-direction candle before a displacement move that breaks structure**. ICT teaches OBs as the candles where institutions absorbed the opposite-side flow before driving price in their intended direction. The qualifying candle's body acts as the algorithmic reference zone for re-entry. This page defines the canonical OB qualification rules; the bullish and bearish variants are deep-dived in [bullish-order-block](bullish-order-block.md) and [bearish-order-block](bearish-order-block.md).

## Formal Criteria

A candle qualifies as an OB if ALL of:

1. **Last opposite candle.** It is the last candle of opposite color before a displacement move (bullish OB = last down-close before bullish displacement; bearish OB = last up-close before bearish displacement).
2. **Displacement follows.** The next 1–3 candles produce a clear directional displacement (wide bodies, minimal opposing wicks, an FVG is typically left in the displacement).
3. **Breaks structure.** The displacement breaks a recent swing high/low (BOS or CHoCH/MSS).
4. **Anchored at a swing pivot.** Best-quality OBs sit at swing highs (bearish) or swing lows (bullish) — pivots that already had structural significance.
5. **Fresh.** Has not yet been mitigated. ⚠ **Timeframe-dependent — see the multi-touch rule below.**

**Multi-candle framing — a run of same-colour candles is ONE block**

ICT frames consecutive same-colour candles before the move as a single order block, not as a
candidate list:

- Bullish: "we would take this as **one full bearish candle**, because it is **consecutively three
  down candles** — so the bullish order block is framed like this… this is all **one** bullish order
  block because it is all down price movement" (`ICT-2016-PROPULSION-BLOCK`, [02:37–03:37]).
- Bearish: "**all three of these candles together is one consecutive candle up** right before the down
  move — that's a potential bearish order block" (`ICT-2017-SWING-BEAR-SETUPS`, [13:56–14:09]).
- **The block's mean threshold is taken across the combined bodies**, not per candle: "the mean
  threshold of a bearish order block in here, but **combining both the bodies**" [05:53–05:58];
  "threshold of **both the bodies of these candles together**" [24:12–24:16].
- **Bodies only.** "The bodies only, **not the wicks**" [06:20–06:23].

**Confirmation — the move must trade through the block's far extreme**

"This candle here **trades through the highest of the down candles** — so that **confirms** this is a
bullish order block" (`ICT-2016-PROPULSION-BLOCK`, [03:40–03:48]). Mirrored for a bearish block.

**Body-quality rejection — the encapsulated candle**

A candidate is discarded when its body is small and contained inside the neighbouring same-colour
candle's body: "too **tiny of a body**, and it's also **encapsulated inside** this last up candle — in
other words, this little green candle's body is basically **inside** of this up candle, so we don't
look at that as an order block. We used a **big beefier body** candle"
(`ICT-2017-SWING-BEAR-SETUPS`, [19:05–19:26]). ⚠ The transcript renders "bullish order block" here
while the worked context is a bearish block framed on up candles; read it as the generic rule.

**Multi-touch tolerance on higher timeframes** ⚠ *qualifies criterion 5*

Monthly and weekly blocks are **not** consumed by first contact:

- "Weekly levels can be **retreated to**, monthly levels can be retreated to **several times**, because
  they're higher timeframe. **Why do we permit higher timeframe levels to be traded to multiple
  times?** Because **larger orders and larger positions are built** on monthly, weekly levels — so it
  may require them **multiple passes** into that level to capitalize that particular price level"
  (`ICT-2017-SWING-BEAR-SETUPS`, [29:36–29:59]).
- Precision is correspondingly looser: "we're **not looking for precision** always on a monthly and
  weekly basis, because there's going to be a **larger order block** there — so we could be trading
  into the **mean threshold**, or it could be using the **low**" [30:27–30:40].
- The stated consequence is that being stopped out at a layered M/W level does not retire the idea:
  "we have to be expecting **potential for maybe getting stopped out**, but **not forgetting the whole
  idea** of the trade… and take the next setup" [30:40–30:59].

**The diagnostic reading — every opposite candle should hold**

Beyond single-block qualification, the *series* is read as evidence of sponsorship: "notice how **all
up candles provide resistance** — that's what we're looking for… even if they end up getting broken at
a later time, they **still provide the measure of resistance** that we would look for for
**institutional sponsorship**" (`ICT-2017-SWING-BEAR-SETUPS`, [24:20–24:43]). Mirrored for down
candles in a bullish series.

## Formula / Math

```
ob_qualifies(candle_n) :=
    is_last_opposite_color_before_displacement(n)
    AND displacement_after_n_present
    AND structure_broken_by_displacement
    AND anchored_at_swing_pivot
    AND not_yet_mitigated

# Bullish OB body: open and close of the OB candle:
bullish_ob_high := open(n)       # since C < O for a bearish candle
bullish_ob_low  := close(n)
bullish_ob_mt   := (open(n) + close(n)) / 2     # mean threshold

# Bearish OB:
bearish_ob_high := close(n)      # since C > O for a bullish candle
bearish_ob_low  := open(n)
bearish_ob_mt   := (close(n) + open(n)) / 2

# --- multi-candle framing: a run of k same-colour candles is ONE block ---
block := longest run of consecutive down-close candles ending at n   # bullish case
bullish_ob_high := max(open(i)  for i in block)     # bodies only, wicks ignored
bullish_ob_low  := min(close(i) for i in block)
bullish_ob_mt   := (bullish_ob_high + bullish_ob_low) / 2   # across the COMBINED bodies

# confirmation: the displacement must clear the block's far extreme
confirmed := max(high over displacement) > max(high(i) for i in block)   # bullish
             # bearish mirror: min(low over displacement) < min(low(i) for i in block)

# --- body-quality rejection ---
encapsulated(n) := body(n) ⊂ body(n-1) of the same colour AND body(n) is small
reject(n) if encapsulated(n)        # prefer the "big beefier body" candle

# --- freshness, qualified by timeframe ---
consumed_on_first_touch := tf in {M1..H4}          # criterion 5 as written
multi_touch_permitted   := tf in {D, W, M}         # HTF blocks absorb repeated passes
# on M/W, tolerate a fill to the mean threshold or the block's far extreme,
# and treat a stop-out at a layered level as a re-entry cue, not an invalidation
```

## Machine-Readable

```json
{
  "id": "order-block-criteria",
  "category": "07-order-blocks",
  "aliases": ["OB-criteria", "OB-rules", "OB-qualification"],
  "criteria": [
    {"id": "c1", "expr": "last_opposite_color_before_displacement == true"},
    {"id": "c2", "expr": "displacement_present == true"},
    {"id": "c3", "expr": "structure_broken == true"},
    {"id": "c4", "expr": "anchored_at_swing_pivot == true"},
    {"id": "c5", "expr": "fresh_not_mitigated == true; qualified on D/W/M where repeated passes are permitted"},
    {"id": "c6", "expr": "a run of consecutive same-colour candles is framed as ONE block"},
    {"id": "c7", "expr": "block bounds and mean_threshold taken across the COMBINED bodies, wicks excluded"},
    {"id": "c8", "expr": "confirmation := displacement trades through the block's far extreme"},
    {"id": "c9", "expr": "reject a candidate whose small body is encapsulated inside an adjacent same-colour body"},
    {"id": "c10", "expr": "on M/W tolerate a fill to mean_threshold or the block extreme; precision is not expected"},
    {"id": "c11", "expr": "diagnostic: in a bearish series every up candle should act as resistance (mirrored for bullish)"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["bullish-order-block","bearish-order-block","mitigated-order-block","unmitigated-order-block","mean-threshold","displacement-definition","fair-value-gap","bos-bullish","bos-bearish","propulsion-block"],
  "sources": ["ICT-2016-OB-INTRO","ICT-2016-PROPULSION-BLOCK","ICT-2017-SWING-BEAR-SETUPS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish OB qualification:

   ▼               ← last DOWN candle before displacement
   ▼               (this is the bullish OB)
                   ▲
                   ▲ ← displacement candle 1
                   ▲
                       ▲
                       ▲ ← displacement candle 2 (FVG forms)
                       ▲     +  swing high broken (BOS / CHoCH)
   bullish OB body = OPEN to CLOSE of the marked down candle.
   MT = body midpoint.
```

## Timeframes

All TFs M5+. M1 OBs are too noisy.

## Examples

**Example 1 — H1 bullish OB:**
- H1 bearish candle at 14:00 NY: open 1.0830, close 1.0820, low 1.0815, high 1.0832.
- H1 candle 15:00 NY: bullish 22-pip displacement, leaves bullish FVG, breaks the prior H1 swing high (BOS).
- → 14:00 candle qualifies as bullish OB.
- OB body: [1.0820, 1.0830]. MT = 1.0825.
- Long entry on retest at MT (1.0825) with SL below 1.0815 (OB low + 3-pip buffer). Risk = 13 pips.

## Common Mistakes

- **Calling any down-candle an OB.** Without displacement-and-BOS following, it's not an OB — just a normal candle.
- **Skipping the structure-break check.** A "displacement" that doesn't break structure isn't significant enough; many practitioners include the BOS check explicitly.
- **Treating bodies vs ranges inconsistently.** Use OB body (open/close) by default; range version (high/low) is broader but less precise.
- **Stale OBs.** Once mitigated (price returned and reacted), the OB stops being a fresh entry zone — **on intraday timeframes**. Monthly and weekly blocks are explicitly permitted repeated passes because the positions behind them are built over several visits.
- **Picking one candle out of a run.** Consecutive same-colour candles before the move are **one** block; taking only the last of them understates the zone and mislocates the mean threshold.
- **Taking the mean threshold of a single candle inside a multi-candle block.** The threshold is computed across the **combined** bodies.
- **Using a small encapsulated body.** If the candidate's body sits inside its same-colour neighbour's body, use the beefier candle instead.
- **Demanding tick precision at a monthly or weekly block.** ICT expects the fill anywhere from the mean threshold to the block's far extreme there, and treats a stop-out at a layered level as a cue to take the next setup rather than to abandon the idea.

## Related Concepts

- [bullish-order-block](bullish-order-block.md), [bearish-order-block](bearish-order-block.md) — directional variants.
- [mitigated-order-block](mitigated-order-block.md), [unmitigated-order-block](unmitigated-order-block.md) — state.
- [mean-threshold](../27-equilibrium/mean-threshold.md) — MT entry depth.
- [displacement-definition](../09-displacement/displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [bos-bullish](../01-market-structure/bos-bullish.md), [bos-bearish](../01-market-structure/bos-bearish.md).

## Citations

- `ICT-2016-OB-INTRO`, `ICT-2022-MENTORSHIP-OVERVIEW`.
- `ICT-2016-PROPULSION-BLOCK` (Dec 2016) (02:37–02:47) "we would take this as one full bearish candle, because it is consecutively three down candles"; (02:47, 03:20–03:37) "so the bullish order block is framed like this… this is an order block as well together, all three candles… this is all one bullish order block because it is all down price movement"; (03:40–03:48) "this candle here trades through the highest of the down candles, so that confirms this is a bullish order block".
- `ICT-2017-SWING-BEAR-SETUPS` (Feb 2017) (05:24–05:36) mean thresholds delineated on "all of the bullish candles prior to a down move, which is a bearish order block"; (05:53–05:58) "the mean threshold of a bearish order block in here, but combining both the bodies"; (06:20–06:23) "the bodies only, not the wicks"; (13:56–14:20) "all three of these candles together is one consecutive candle up right before the down move — that's a potential bearish order block"; (19:05–19:26) the encapsulated-body rejection, "too tiny of a body… encapsulated inside this last up candle… we used a big beefier body candle"; (24:12–24:16) "threshold of both the bodies of these candles together"; (24:20–24:43) "notice how all up candles provide resistance… even if they end up getting broken at a later time, they still provide the measure of resistance that we would look for for institutional sponsorship"; (29:36–29:59) "why do we permit higher timeframe levels to be traded to multiple times? Because larger orders and larger positions are built on monthly, weekly levels — so it may require them multiple passes into that level"; (30:27–30:59) "we're not looking for precision always on a monthly and weekly basis… we could be trading into the mean threshold, or it could be using the low", and getting stopped out at a layered level without "forgetting the whole idea of the trade".
