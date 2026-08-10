# Anticipatory Setup Development

**Category:** 25-htf-bias
**Aliases:** the next setup, monthly order block range, anticipatory skill, monthly range definition
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-ANTICIPATORY
**Tags:** htf-bias, monthly, order-blocks, range-definition, top-down, anticipation

## Definition

Anticipatory setup development is a **mechanical procedure for defining the current trading
range from the monthly chart** — one down candle, one up candle — so that setups can be
located *before* they form rather than reacted to. It answers "where is the next setup?" with
two levels that are fixed in advance and then refined downward.

The premise is that only institutional size moves a monthly candle: "the monthly chart is only
going to move with a great deal of money behind these price swings… **retail can't move
price**" (`ICT-2016-ANTICIPATORY`, 01:00–01:33). ICT frames the payoff as removing the blank
stare at the chart: "it gives you a context to actually look into the marketplace with a
specific mindset, not just waiting for a neon sign to jump off at you" (14:50).

## Formal Criteria

**Step 1 — mark the monthly reference points**

- Note the **open, high, low and close of each of the last three monthly candles** (01:46–02:24).
- Transpose those levels onto the lower timeframes. Overlapping opens and closes are expected
  and acceptable (02:37–02:46).

**Step 2 — define the range with two candles** (02:46–03:44, 14:00–14:08)

- Find the **most recent down-close candle**.
- Find the nearest **up-close candle above it** whose **low is higher than that down candle's
  high**.
- Those two candles bound the range. This is the whole definition — "just that quick, we've
  delineated a range on the monthly chart" (03:31).

**Step 3 — decide which candle is armed** (14:08–14:39)

- If price has traded **above the down candle's high**, that down candle becomes a **bullish
  order block**. Buy the return to it; the objective is the up candle above (a monthly bearish
  order block).
- If price has traded **below the up candle's low**, that up candle becomes a **bearish order
  block**. Sell the return to it; the objective is the down candle below.
- The rule ICT states for locating the target: "you just simply look for **the contrary order
  block** on the monthly chart" (14:32).

**Step 4 — refine downward** (03:53–06:17, 14:39–14:44)

- Carry the two monthly levels onto the **weekly**, then **daily**, then **hourly**.
- On the weekly, the monthly down candle may resolve into two adjacent down candles activated
  together as the block.
- On the daily, use the **body** of the largest down candle as the block's origin and its
  **mean threshold** as the refined entry (10:19–10:50).
- Refining downward is what reduces risk — the monthly range supplies the objective, the lower
  timeframe supplies the entry.

**What it is not**

- It supplies **range and objective**, not a trigger. ICT calls it "basically a top-down
  approach that leads you right into trade setups that you otherwise wouldn't know they were
  there" (15:05).

## Formula / Math

```
# --- Step 2: range definition on the MONTHLY chart ---
D := most recent down-close candle
U := nearest up-close candle above D such that  low(U) > high(D)

range := [ low(U) , high(D) ]           # the two institutional reference points

# --- Step 3: which one is armed ---
if price traded above high(D):
    D  := bullish order block           # buy the return
    target := U                          # the contrary (bearish) monthly block

if price traded below low(U):
    U  := bearish order block           # sell the return
    target := D                          # the contrary (bullish) monthly block

# --- Step 4: refinement ---
entry_tf := W -> D -> H1
entry    := body of the origin candle, or its mean threshold
            mean_threshold := (high(body) + low(body)) / 2
```

## Machine-Readable

```json
{
  "id": "anticipatory-setup-development",
  "category": "25-htf-bias",
  "aliases": ["the-next-setup", "monthly-order-block-range", "anticipatory-skill"],
  "criteria": [
    {"id": "c1", "expr": "mark OHLC of the last 3 monthly candles"},
    {"id": "c2", "expr": "D := most recent down-close monthly candle"},
    {"id": "c3", "expr": "U := nearest up-close candle above D with low(U) > high(D)"},
    {"id": "c4", "expr": "range := [low(U), high(D)]"},
    {"id": "c5", "expr": "price above high(D) => D is a bullish order block; target := U"},
    {"id": "c6", "expr": "price below low(U) => U is a bearish order block; target := D"},
    {"id": "c7", "expr": "target := the contrary monthly order block"},
    {"id": "c8", "expr": "refine entry on W -> D -> H1 using body / mean_threshold"},
    {"id": "c9", "expr": "supplies range and objective, not a trigger"}
  ],
  "timeframes": ["H1","D","W","M"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["top-down-analysis", "timeframe-selection", "monthly-bias", "bullish-order-block", "bearish-order-block", "mean-threshold", "order-block-criteria", "dealing-range"],
  "sources": ["ICT-2016-ANTICIPATORY"]
}
```

## Visual Pattern

```
   MONTHLY CHART — two candles define everything

        ┃  U   <- most recent UP candle whose LOW is above D's HIGH
        ┃         (bearish order block; upside objective)
        ┃
     low(U) ─────────────────────────────────────────────  ceiling
                                                    ↑
                          THE RANGE                 │
                                                    ↓
    high(D) ─────────────────────────────────────────────  floor
        ┃
        ┃  D   <- most recent DOWN candle
        ┃         (bullish order block once price trades ABOVE its high)

   ARMED WHEN:
     price traded ABOVE high(D)  ->  buy the return to D, target U
     price traded BELOW low(U)   ->  sell the return to U, target D

   THEN REFINE:   Monthly ──► Weekly ──► Daily ──► Hourly
                  (range)              (body / mean threshold = entry)
```

## Timeframes

Defined on the **monthly**; refined on weekly, daily and hourly. The two levels stay fixed
while the entry timeframe descends.

## Examples

**Example 1 — USDCAD (`ICT-2016-ANTICIPATORY`, 02:37–08:49):**
- Monthly: the most recent down candle had a high of 1.3144; the qualifying up candle sat above it.
- Weekly: two adjacent down candles were traded through, activating them together as a
  **bullish order block**; the monthly open, rounded to **1.3080**, became the downside objective.
- Daily: price dipped into 1.3080 and "responds aggressively off of that."
- Outcome: upside continued, with 1.3800 named as the next objective and the monthly bearish
  order block still above.

**Example 2 — USDJPY (09:06–11:31):**
- Monthly: most recent down candle high **104.35**; the qualifying up candle gave a range of
  **103.26 to 106.28** — about 300 pips.
- Arming: price traded above the down candle's high, so 103.26 and below became the buy zone.
- Daily refinement: the largest down-candle body marked the block's origin; its **mean
  threshold was never challenged**, even on the US-election knee-jerk.
- Outcome: two separate buys (the dip, then the election candle), then a rally toward the old
  and equal highs — "we've already seen that happen with 300 pips plus."

**Example 3 — NZDUSD, the bearish mirror (11:32–13:48):**
- Monthly: price moved away from the most recent up candle, arming it as a **bearish order block**.
- Weekly: price traded back up into it, through the candle's body but sloppily.
- Objective: **0.6983–0.7005** (the candle bodies and close) — roughly 120 pips, with a further
  0.6780 flagged as ICT's personal view.
- Daily: the bearish block was refined to a lower-timeframe block for a tighter entry.

## Common Mistakes

- **Picking any down candle.** It must be the **most recent** one, and the up candle must have
  its **low above that candle's high** — otherwise there is no range.
- **Skipping the arming test.** A monthly candle is only an order block once price has traded
  through the opposing side; before that it is just a candle.
- **Entering on the monthly.** The monthly supplies the range and objective; entering without
  descending to the weekly, daily or hourly leaves an unnecessarily wide stop.
- **Using wicks for the refined entry.** The daily refinement works off the **body** and its
  mean threshold.
- **Expecting a signal.** This locates *where* a setup should appear, not *when* to press the
  button.
- **Discarding the range on a news spike.** The USDJPY example survives the US election
  untouched at its mean threshold — that is the point of using monthly reference points.

## Related Concepts

- [top-down-analysis](top-down-analysis.md) — the general descent; this is its monthly-anchored, mechanical form.
- [timeframe-selection](timeframe-selection.md) — the framing sequence (define the range high, refine lower) taught in the same month.
- [monthly-bias](monthly-bias.md) — the directional read this procedure operationalises.
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md) — what the two monthly candles become.
- [mean-threshold](../27-equilibrium/mean-threshold.md) — the refined entry level on the daily.
- [dealing-range](../05-pd-arrays/dealing-range.md) — the general range concept this instantiates from two monthly candles.

## Citations

- `ICT-2016-ANTICIPATORY` (00:30) "this is the fourth teaching of eight of the **November 2016** content for the ICT Mentorship… anticipatory skill sets… using institutional order flow to help you find new setups"; (01:00–01:33) "the monthly chart is only going to move with a great deal of money behind these price swings… retail is not going to have it… retail can't move price"; (01:46–02:24) note the open, high, close and low of every monthly candle over the last three months; (02:37–02:46) overlapping opens and closes are acceptable; (02:46–03:31) find the most recent down candle, then the up candle above it whose low exceeds that candle's high — "just that quick, we've delineated a range on the monthly chart"; (03:53–04:12) transposing the two reference points onto the weekly; (04:43–05:06) two weekly down candles activated together as a bullish order block; (05:06–05:28) the 1.3080 monthly level; (06:14–07:12) the daily view and the aggressive response off 1.3080; (07:54–07:59) the 1.3800 objective; (08:05–08:49) the takeaway restated — find the most recent down candle and the most recent up candle, "there's your range"; (09:06–09:59) the USDJPY range 103.26–106.28, "so basically 300 pips… as soon as this candle trades above the down candle's high, this down candle becomes a bullish order block"; (10:19–11:12) the daily refinement using the larger body and its mean threshold, untouched on the election reaction; (11:32–13:48) the NZDUSD bearish mirror with the 0.6983 / 0.7005 objective; (13:48–14:44) "we're using the monthly chart to give us our bullish and bearish order blocks and define our range… you just simply look for the contrary order block on the monthly chart… and you find them down into a weekly, into a daily, and down to an hourly chart"; (14:50–15:05) "it gives you a context… not just waiting for a neon sign to jump off at you… it's basically a top-down approach that leads you right into trade setups that you otherwise wouldn't know they were there".
