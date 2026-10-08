# Order Block — Criteria

**Category:** 07-order-blocks
**Aliases:** OB criteria, order block rules, OB qualification
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-ORDERBLOCKS, ICT-2016-PROPULSION-BLOCK, ICT-2017-SWING-BEAR-SETUPS, ICT-2022-MENTORSHIP-EP03, ICT-2022-MENTORSHIP-EP09, ICT-2022-MENTORSHIP-EP13, ICT-2022-MENTORSHIP-EP18, ICT-2022-MENTORSHIP-EP19, ICT-2022-MENTORSHIP-EP40
**Tags:** order-block, criteria, foundational, multi-candle, mean-threshold

⚠ **Rewritten 2026-10-08.** The prior "last opposite candle / displacement in 1–3 candles / breaks
structure / ALL of" criteria are **not ICT's definition in either era** — see
[bullish-order-block](bullish-order-block.md) for the EP12/EP18 quotes rejecting the last-candle
framing outright. This page's multi-candle, confirmation, body-quality, and multi-touch content was
audited and is CONFIRMED verbatim; it is kept. A misquoted word is corrected below (see Citations).

## Definition

An order block (OB) is ICT's reference zone for the institutional candle(s) that precede a
directional move. **2016:** the extreme candle (lowest down-close for bullish, highest up-close for
bearish) with the greatest open-to-close range among candidates, sitting near an HTF support/
resistance level — see [bullish-order-block](bullish-order-block.md). **2022:** "it's just [a] change
in the state of delivery" (ICT-2022-MENTORSHIP-EP03 [24:16]) — the block is a run of same-colour
candles whose **opening price**, once violated, flips the algorithm's delivery state; the live
reference is refined to the candle nearest price in that run. Qualification requires an **imbalance**
on the move away (2022) — see below. This page defines the canonical qualification rules shared by
both directions; the bullish and bearish variants are deep-dived in
[bullish-order-block](bullish-order-block.md) and [bearish-order-block](bearish-order-block.md).

## Formal Criteria

- **Not "the last opposite candle before a displacement that breaks structure."** ICT rejects this
  framing outright: "order block theory is much more than just simply the last up close candle
  before down move or the last down closed candle before the up move — that's not it" (EP12
  [44:09]); "it does not need to get up into this last up close candle … that's what everybody says
  an order block is. It is not that." (EP18 [40:13–40:41]).
- **2016 selection rule:** the extreme candle (lowest down-close / highest up-close) with the
  greatest open-to-close range among candidates, near an HTF support/resistance level
  (ICT-2016-ORDERBLOCKS [00:59–01:08], [02:20–02:27]).
- **2022 validity rule — imbalance is mandatory, not "typical":** "what makes an order block valid?
  It has to have an imbalance. Without the imbalance, there is no order block." (EP18 [40:41]);
  "consecutive down closed candles right before a price surge that has an imbalance — that's how you
  find your order blocks" (EP09 [07:16]); "that is how you determine your high probability bullish
  order block — it must have the imbalance coupled with the down closed candle and the underlying
  narrative that it's likely to go higher" (EP13 [17:22–17:52]).
- **Market structure shift is a quality marker, not a defining criterion.** "Why is this a good …
  bearish order block? Because it has that gap, and it's taken liquidity, and there's a market
  structure shift — there's your … high probability bearish order block." (EP03 [23:40], eliding the
  auto-caption's garbled "height frequency high power" between "your" and "high probability").
- **Anchored near an HTF support/resistance level** (2016 "near a support level" [01:08]; old
  high/low [02:20–02:27]).
- **Not fresh-only.** Qualified by timeframe — see the multi-touch rule below; 2022 rejects the
  fresh-zone premise outright (`bullish-order-block.md`, EP18 [40:41–41:12]).

**Multi-candle framing — a run of same-colour candles is ONE block**

ICT frames consecutive same-colour candles before the move as a single order block, not as a
candidate list:

- Bullish: "we would take this as **one full bearish candle**, because it is **consecutively three
  down candles** — so the bullish order block is framed like this… this is all **one** bullish order
  block because it is all down price movement" (`ICT-2016-PROPULSION-BLOCK`, [02:37–03:37]).
- Bearish: "**all three of these candles together is one consecutive candle up** right before the down
  move — that's a potential bearish order block" (`ICT-2017-SWING-BEAR-SETUPS`, [14:03–14:09]).
- **The block's mean threshold is taken across the combined bodies**, not per candle: "we have the
  mean threshold of bullish order block in here, but **combining both the bodies**" [05:53–05:58];
  "threshold of **both the bodies of these candles together**" [24:12–24:16].
- **Bodies only.** "The bodies only, **not the wicks**" [06:20–06:23].
- 2022 confirms the same framing: "see these down closed candles — see that, that's all one
  continuous order block" (EP03 [14:43]); "these last three down closed candles — that's one
  consecutive order block" (`ICT-2022-MENTORSHIP-EP40` [33:31]).
- **Refine to the candle nearest price (2022).** Within a multi-candle block, the live reference
  narrows to the one closest to current price: "the low of the lowest up close candle and its
  opening price" (EP19 [21:17]).

**Confirmation — the move must trade through the block's far extreme**

"This candle here **trades through the highest of the down candles** — so that **confirms** this is a
bullish order block" (`ICT-2016-PROPULSION-BLOCK`, [03:40–03:48]). Mirrored for a bearish block.

**Body-quality rejection — the encapsulated candle**

A candidate is discarded when its body is small and contained inside the neighbouring same-colour
candle's body: "too **tiny of a body**, and it's also **encapsulated inside** this last up candle — in
other words, this little green candle's body is basically **inside** of this up candle, so we don't
look at that as a **bullish** order block. We used a **big beefier body** candle"
(`ICT-2017-SWING-BEAR-SETUPS`, [19:05–19:26]). ⚠ The transcript says "bullish order block" here while
the worked context is a bearish block framed on up candles; read it as the generic rule — do not
silently drop the word to make the quote read more consistently, as a prior version of this page did.

**Multi-touch tolerance on higher timeframes** ⚠ *qualifies the freshness criterion*

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
- 2022 states this for all timeframes, not only HTF — see
  [bullish-order-block](bullish-order-block.md) ("fresh zones … that's nonsense").

**The diagnostic reading — every opposite candle should hold**

Beyond single-block qualification, the *series* is read as evidence of sponsorship: "notice how **all
up candles provide resistance** — that's what we're looking for… even if they end up getting broken at
a later time, they **still provide the measure of resistance** that we would look for for
**institutional sponsorship**" (`ICT-2017-SWING-BEAR-SETUPS`, [24:20–24:43]). Mirrored for down
candles in a bullish series — stated directly in 2022: in a bullish regime, "down closed candles
should not be violated … they're going to act as support" (EP13 [13:11]).

## Formula / Math

```
ob_qualifies(candle_n) :=
    ( is_extreme_candidate(n) AND max_open_to_close_range(n) AND near_HTF_level(n) )   # 2016
    OR
    ( n in nearest_candle_of_a_same_colour_run AND imbalance_present_on_move_away(n) )  # 2022

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
live_reference  := the candle in block nearest to current price (2022 refinement)

# confirmation: the displacement must clear the block's far extreme
confirmed := max(high over displacement) > max(high(i) for i in block)   # bullish
             # bearish mirror: min(low over displacement) < min(low(i) for i in block)

# --- body-quality rejection ---
encapsulated(n) := body(n) ⊂ body(n-1) of the same colour AND body(n) is small
reject(n) if encapsulated(n)        # prefer the "big beefier body" candle

# --- freshness, qualified by timeframe ---
multi_touch_permitted := tf in {M1 .. MN}   # 2022: fresh-zone premise rejected at every timeframe;
                                             # HTF (D/W/M) additionally expects MULTIPLE passes,
                                             # not merely tolerates them
```

## Machine-Readable

```json
{
  "id": "order-block-criteria",
  "category": "07-order-blocks",
  "aliases": ["OB-criteria", "OB-rules", "OB-qualification"],
  "criteria": [
    {"id": "c1", "expr": "2016: extreme candle (lowest down-close / highest up-close), max open-to-close range among candidates, near an HTF support/resistance level"},
    {"id": "c2", "expr": "2022: candle nearest price within a same-colour run, qualified by an imbalance on the move away"},
    {"id": "c3", "expr": "market structure shift is a QUALITY marker on the move away, not a defining criterion"},
    {"id": "c4", "expr": "anchored near an HTF support/resistance level"},
    {"id": "c5", "expr": "NOT fresh-only at any timeframe (2022); HTF additionally expects multiple passes"},
    {"id": "c6", "expr": "a run of consecutive same-colour candles is framed as ONE block"},
    {"id": "c7", "expr": "block bounds and mean_threshold taken across the COMBINED bodies, wicks excluded"},
    {"id": "c8", "expr": "confirmation := displacement trades through the block's far extreme"},
    {"id": "c9", "expr": "reject a candidate whose small body is encapsulated inside an adjacent same-colour body"},
    {"id": "c10", "expr": "on M/W tolerate a fill to mean_threshold or the block extreme; precision is not expected"},
    {"id": "c11", "expr": "diagnostic: in a bearish series every up candle should act as resistance (mirrored for bullish — down candles act as support)"},
    {"id": "c12", "expr": "2022: within a multi-candle block, refine the live reference to the candle nearest current price"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["bullish-order-block","bearish-order-block","mitigated-order-block","unmitigated-order-block","mean-threshold","displacement-definition","fair-value-gap","propulsion-block"],
  "sources": ["ICT-2016-ORDERBLOCKS","ICT-2016-PROPULSION-BLOCK","ICT-2017-SWING-BEAR-SETUPS","ICT-2022-MENTORSHIP-EP03","ICT-2022-MENTORSHIP-EP09","ICT-2022-MENTORSHIP-EP13","ICT-2022-MENTORSHIP-EP18","ICT-2022-MENTORSHIP-EP19","ICT-2022-MENTORSHIP-EP40"]
}
```

## Visual Pattern

```
   bullish OB qualification (2022 refinement within a multi-candle block):

   ▼ ▼ ▼           ← run of down-close candles framed as ONE block
                   (live reference = the one nearest price)
                   ▲
                   ▲ ← displacement candle, leaves an imbalance (mandatory, 2022)
                   ▲
                       ▲
                       ▲ ← move trades through the block's far extreme (confirmation)
                       ▲
   bullish OB body = OPEN to CLOSE of the combined block (bodies only).
   MT = midpoint of the COMBINED bodies.
```

## Timeframes

M1 through monthly — no timeframe floor is stated by ICT, and 2022 trades M1 blocks directly: "we're
looking at one minute candles — that is the order block with a fair value — got buy it there" (EP19
[103:45]); "if you look at it on the two minute chart, see that it becomes one order block" (EP03
[29:42]).

## Examples

**Example 1 — H1 bullish OB:**
- H1 bearish candle at 14:00 NY: open 1.0830, close 1.0820, low 1.0815, high 1.0832, sitting near an
  old daily low.
- H1 candle 15:00 NY: bullish displacement, leaves a fair value gap (the 2022 validity requirement).
- Later candle's high trades through 1.0832 (confirmation).
- → 14:00 candle qualifies as bullish OB. Body: [1.0820, 1.0830]. MT = 1.0825.
- Entry on retest at the body extreme nearest price (the high/open, ~1.0830), not at MT; MT is the
  depth tolerance. SL below the candle's close/low.

## Common Mistakes

- **Calling it "the last opposite candle before a displacement that breaks structure."** ICT rejects
  this framing explicitly (EP12 [44:09], EP18 [40:13–40:41]). Use the 2016 selection rule or the 2022
  imbalance-qualified, nearest-to-price refinement instead.
- **Treating the FVG/imbalance as merely "typical."** In 2022 it is mandatory: "without the
  imbalance, there is no order block" (EP18 [40:41]).
- **Treating a market structure shift as a defining criterion.** It is a quality marker on the move
  away, not a gate (EP03 [23:40]).
- **Demanding freshness.** 2022 rejects the fresh-zone premise outright at every timeframe, not only
  on HTF.
- **Picking one candle out of a run without refining to the nearest.** Consecutive same-colour
  candles before the move are **one** block, but the 2022 live trading reference narrows to the
  candle nearest current price (EP19 [21:17]).
- **Taking the mean threshold of a single candle inside a multi-candle block.** The threshold is
  computed across the **combined** bodies.
- **Using a small encapsulated body.** If the candidate's body sits inside its same-colour neighbour's
  body, use the beefier candle instead.
- **Demanding tick precision at a monthly or weekly block.** ICT expects the fill anywhere from the
  mean threshold to the block's far extreme there, and treats a stop-out at a layered level as a cue
  to take the next setup rather than to abandon the idea.
- **Assuming M1 is too noisy.** ICT trades M1 and M2 order blocks directly in 2022 (EP19 [103:45],
  EP03 [29:42]).

## Related Concepts

- [bullish-order-block](bullish-order-block.md), [bearish-order-block](bearish-order-block.md) — directional variants.
- [mitigated-order-block](mitigated-order-block.md), [unmitigated-order-block](unmitigated-order-block.md) — state.
- [mean-threshold](../27-equilibrium/mean-threshold.md) — tolerance depth, not the default entry.
- [displacement-definition](../09-displacement/displacement-definition.md), [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md).

## Citations

- `ICT-2016-ORDERBLOCKS` (Dec 2016) [00:59–01:08], [02:20–02:27] 2016 selection rule.
- `ICT-2016-PROPULSION-BLOCK` (Dec 2016) (02:37–02:47) "we would take this as one full bearish candle, because it is consecutively three down candles"; (02:47, 03:20–03:37) "so the bullish order block is framed like this… this is an order block as well together, all three candles… this is all one bullish order block because it is all down price movement"; (03:40–03:48) "this candle here trades through the highest of the down candles, so that confirms this is a bullish order block".
- `ICT-2017-SWING-BEAR-SETUPS` (Feb 2017) (05:24–05:36) mean thresholds delineated on "all of the bullish candles prior to a down move, which is a bearish order block"; (05:53–05:58) ⚠ verbatim transcript reads "we have the mean threshold of **bullish** order block in here, but combining both the bodies" — the prior version of this page silently altered this to "bearish"; the surrounding context ([05:24] "all of the bullish candles prior to a down move, which is a bearish order block") supports the page's *rule*, but the quotation itself is now corrected to match the transcript; (06:20–06:23) "the bodies only, not the wicks"; (14:03–14:09) "all three of these candles together is one consecutive candle up right before the down move — that's a potential bearish order block"; (19:05–19:26) the encapsulated-body rejection, "too tiny of a body… encapsulated inside this last up candle… we used a big beefier body candle"; (24:12–24:16) "threshold of both the bodies of these candles together"; (24:20–24:43) "notice how all up candles provide resistance… even if they end up getting broken at a later time, they still provide the measure of resistance that we would look for for institutional sponsorship"; (29:36–29:59) "why do we permit higher timeframe levels to be traded to multiple times? Because larger orders and larger positions are built on monthly, weekly levels — so it may require them multiple passes into that level"; (30:27–30:59) "we're not looking for precision always on a monthly and weekly basis… we could be trading into the mean threshold, or it could be using the low", and getting stopped out at a layered level without "forgetting the whole idea of the trade".
- `ICT-2022-MENTORSHIP-EP03` [14:43], [23:40], [24:16–24:45], [29:42], [15:12] change-in-state-of-delivery definition, MSS as quality marker, M2 order block.
- `ICT-2022-MENTORSHIP-EP09` [07:16] imbalance-qualified consecutive candles.
- `ICT-2022-MENTORSHIP-EP13` [13:11], [17:22–17:52] down-closed candles as support in a bullish regime; imbalance requirement.
- `ICT-2022-MENTORSHIP-EP18` [40:13–41:12], [42:22] rejects the last-candle framing and the fresh-zone premise; imbalance mandatory.
- `ICT-2022-MENTORSHIP-EP19` [21:17], [103:45] refine to the nearest candle; M1 order block traded directly.
- `ICT-2022-MENTORSHIP-EP40` [33:31] multi-candle framing confirmed.
