# Market Maker Trap

**Category:** 31-models
**Aliases:** MM trap, market maker traps, false pattern, retail pattern trap, classical pattern fade
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-MMT-FALSE-FLAG, ICT-2016-MMT-FALSE-BREAKOUT, ICT-2016-MMT-TRENDLINE, ICT-2016-MMT-HEAD-SHOULDERS
**Tags:** models, retail-trap, classical-patterns, liquidity, contrarian, order-blocks, turtle-soup

## Definition

A market maker trap is **a classical retail chart pattern printed by the algorithm in the
direction opposite to higher-timeframe order flow**, so that the pattern's textbook trigger
point becomes the liquidity pool the real move is reaching for. ICT does not teach the
patterns themselves — "they can be found on the internet, I'm not going to teach that…
what I'm actually going to tell you is **how you can capitalize on these patterns when they
appear** and our higher-timeframe premise indicates the opposite direction is unfolding"
(`ICT-2016-MMT-HEAD-SHOULDERS`, 02:24–02:38).

**One page, four sources.** The mentorship taught four variants across two consecutive
months as a deliberate series — "we're going to be attacking a lot of the retail-minded
classical chart patterns throughout this ICT mentorship" (`ICT-2016-MMT-HEAD-SHOULDERS`,
17:17). They share one mechanism and are documented together rather than as four pages.

## Formal Criteria

**The shared mechanism**

1. Higher-timeframe order flow (daily / weekly / monthly PD arrays) establishes the true
   direction.
2. A lower timeframe prints a **classical pattern pointing the other way**.
3. Retail's trigger — the neckline break, the flag breakout, the third trendline touch, the
   range break — is where the stops sit.
4. The algorithm runs that level to **pair orders**, then delivers in the HTF direction.
5. The trader **fades the pattern**, entering at an ordinary PD array (order block, breaker,
   fair value gap) or on the stop run itself as a turtle soup.

**Variant 1 — False flag** (`ICT-2016-MMT-FALSE-FLAG`)

- A bull flag (impulse leg + small consolidation) forming in a **mature bull trend or at a
  higher-timeframe premium / distribution level** fails instead of delivering its measured move.
- Mirror: a bear flag at a higher-timeframe **discount / accumulation** level fails.
- "Not all sudden price rallies that move into a short-term consolidation are bull flags" (01:40).
- The tell is HTF position, not the pattern: ICT's own early failures came from trading the
  pattern "for the sake of patterns" without a premium/discount read (02:24–03:14).
- On the breakout, check what price actually reached: in the worked example it "only… traded
  just above this old high" — a stop run, not an expansion (11:17–11:25).

**Variant 2 — False breakout of a consolidation** (`ICT-2016-MMT-FALSE-BREAKOUT`)

- In a **bullish** market: price repeatedly drops **below consolidation** to run sell stops,
  then expands up to the buy stops above the old high. Every such break is read as a false
  breakout and an accumulation event (16:00–16:11).
- In a **bearish** market: the mirror — breaks **above** consolidation neutralise buy stops.
- **The diagnostic:** "every time the market goes into consolidation, which side of the market
  they [are] reaching for, and then where's the market going after it happens" (13:28). One
  side being run repeatedly, followed by expansion the other way, identifies the true bias.
- **Read the bodies, not the wicks** — "all the volume is seen in… the bodies of the candles,
  so the liquidity is going to rest above it" (09:02–09:25).
- Objectives can be projected as **measured moves** from the first stop-run low to the first
  swing high, repeated from each subsequent stop run (16:41–18:04).

**Variant 3 — Trendline phantom** (`ICT-2016-MMT-TRENDLINE`)

- ICT rejects diagonal trendline support/resistance outright: "there's **no statistical edge**
  that I've been able to build with use of diagonal support or resistance" (02:24); "**price
  has no awareness of your trendline**… price only respects where the actual liquidity is"
  (03:20–03:32).
- The trap: retail buys the **third touch** of an ascending line (or sells the third touch of
  a descending one); that influx of weak-handed money is the liquidity.
- **The counter-entry (the operational rule):** on a *bullish* trendline, target the **high
  formed between touch 2 and touch 3** — take a bearish order block there, or allow a brief
  poke above it for a turtle soup short (07:58–09:01). On a *bearish* trendline, target the
  **low formed between high 2 and high 3** for a bullish order block or a turtle soup long
  (10:06–10:58).
- **Point 2 is where the stops are** — expect a run through the second touch, not the third
  (11:00–11:45).

**Variant 4 — False head and shoulders** (`ICT-2016-MMT-HEAD-SHOULDERS`)

- Genuine H&S / inverted H&S form "at **intermediate or long-term highs only**"; retail hunts
  them on lower timeframes, often at a significant low (01:36–02:12).
- **Head and shoulders in a bullish HTF environment** → the neckline break is a **turtle soup
  long**: "I'll buy the sell stops below those equal lows… and then I'll look for the head or
  the highest peak to be violated" (06:31–06:54). Target = the buy stops above the head.
- **Inverted H&S in a bearish HTF environment** → the neckline break is a **run on buy stops**
  to sell into; target = the sell stops below the head (06:57–07:34).
- **First profit can be taken at the right shoulder** on both patterns (07:34).

**Standing constraint**

- ICT explicitly does **not** pick long-term tops and bottoms: "even seasoned pros don't do
  that… as it relates to long term tops and bottoms, I try to avoid that"
  (`ICT-2016-MMT-HEAD-SHOULDERS`, 04:18–04:45). The trap is traded as a liquidity event inside
  an established HTF bias, not as a reversal call.

## Formula / Math

```
market_maker_trap :=
    HTF_order_flow_direction  = D           # from monthly/weekly/daily PD arrays
    retail_pattern_direction  = NOT D       # flag, H&S, trendline, range break
    retail_trigger_level      = neckline / flag breakout / 3rd touch / range bound
    => retail_trigger_level IS the liquidity pool

entry := PD_array in direction D            # order block, breaker, FVG
      OR turtle_soup at retail_trigger_level

# --- variant-specific targets ---
head_and_shoulders(bullish HTF):
    entry  := sell stops below the neckline / equal lows
    target := buy stops above the HEAD
    first_partial := right shoulder

inverted_HS(bearish HTF):
    entry  := buy stops above the neckline
    target := sell stops below the HEAD

trendline(bullish line, bearish HTF):
    entry  := bearish OB at the HIGH between touch_2 and touch_3
           OR turtle soup just above that high
    note   := stops rest at touch_2, not touch_3

false_breakout(bullish market):
    every break BELOW consolidation := sell-stop run, accumulation
    target := buy stops above the old high (measured off candle BODIES)
    projection := measured move of the first impulse leg, repeated per stop run
```

## Machine-Readable

```json
{
  "id": "market-maker-trap",
  "category": "31-models",
  "aliases": ["mm-trap", "false-pattern", "retail-pattern-trap"],
  "criteria": [
    {"id": "c1", "expr": "retail_pattern_direction == opposite(HTF_order_flow)"},
    {"id": "c2", "expr": "retail_trigger_level == liquidity_pool"},
    {"id": "c3", "expr": "entry := PD_array in HTF direction OR turtle_soup at the trigger"},
    {"id": "c4", "expr": "variant_false_flag := flag at HTF premium (bull) or discount (bear) fails its measured move"},
    {"id": "c5", "expr": "variant_false_breakout := repeated consolidation breaks on one side + expansion the other way identifies bias"},
    {"id": "c6", "expr": "variant_trendline := fade at the high between touch_2 and touch_3 (mirror for bearish lines); stops rest at touch_2"},
    {"id": "c7", "expr": "variant_head_shoulders := neckline break traded as turtle soup; target = liquidity beyond the HEAD; first partial at right shoulder"},
    {"id": "c8", "expr": "liquidity measured from candle BODIES, not wicks"},
    {"id": "c9", "expr": "diagonal_trendline_support_resistance has no taught edge"},
    {"id": "c10", "expr": "not_used_for picking long-term tops and bottoms"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["turtle-soup", "trendline-liquidity", "market-efficiency-paradigm", "liquidity-pool", "order-block-criteria", "breaker-block", "stop-run-definition", "top-down-analysis", "premium-array", "discount-array"],
  "sources": ["ICT-2016-MMT-FALSE-FLAG", "ICT-2016-MMT-FALSE-BREAKOUT", "ICT-2016-MMT-TRENDLINE", "ICT-2016-MMT-HEAD-SHOULDERS"]
}
```

## Visual Pattern

```
  1 FALSE FLAG                        2 FALSE BREAKOUT (bullish market)
      ╱‾╲                                 ▭▭▭▭        ▭▭▭▭
     ╱   ▭▭▭  <- "flag"                  ╱    ╲__╱‾╲ ╱    ╲__╱‾
    ╱        ╲___                       ╱   ▼ run sell stops ▼
   flagpole   ▼ fails at HTF PREMIUM    each dip below the range = accumulation,
              no measured move          each expansion = reach for buy stops

  3 TRENDLINE PHANTOM                 4 FALSE HEAD & SHOULDERS (bullish HTF)
        ●3  <- retail BUYS here             H
       ╱ ▼ FADE the HIGH between        LS ╱ ╲ RS
      ●2   touch 2 and touch 3         ╱‾╲╱   ╲╱‾╲
     ╱  (bearish OB / turtle soup)   ──────────────── neckline
    ●1     stops rest at ●2, not ●3      ▼ retail SHORTS the break
                                         ▲ ICT BUYS it — turtle soup long,
                                           target = buy stops above the HEAD

  ─────────────────────────────────────────────────────────────────
  In every variant: retail's trigger IS the liquidity. Direction comes
  from the higher timeframe, never from the pattern.
```

## Timeframes

The patterns are spotted on M5–H1; the bias that invalidates them is read on H4, daily,
weekly and monthly. A trap is only a trap relative to a higher-timeframe read.

## Examples

**Example 1 — false H&S, GBPUSD 12 August 2015 (`ICT-2016-MMT-HEAD-SHOULDERS`, 07:45–12:14):**
- Daily: price traded down into a **bullish order block** (a down candle violated on 10 August,
  high 1.5546) — bullish HTF premise.
- Hourly: a high, higher high and lower high with two equal lows beneath — a textbook **head
  and shoulders**. Retail's measured objective was ~1.5495.
- ICT's read: the break of the neckline is a **sell-stop run**, not an expansion. Buy at
  ~1.5550, target 1.5620 — the buy stops above the head, ~70 pips.
- Outcome: price ran below the lows four more times gathering stops, then expanded through 1.5620.

**Example 2 — false inverted H&S, GBPUSD October (12:14–16:46):**
- Daily: price returned into a **breaker** around 1.5345–1.5350 — bearish HTF premise.
- Lower timeframe: a low, lower low, higher low — **inverted H&S**, read by retail as bullish.
- ICT's read: sell the break above the neckline into the buy stops; using candle **bodies**,
  the sell level was 1.5502. Objective: the sell stops below the head. Both the initial run and
  a later retest of 1.5502 delivered.

**Example 3 — trendline phantom, December 2015 (`ICT-2016-MMT-TRENDLINE`, 12:56–17:04):**
- Daily reference: a fair value gap left by an impulse swing down; the low of the origin candle
  marked at 1.5234 as a future reactionary level.
- 11 December, 15-minute: price hit 1.5234 while an ascending trendline gave retail a clean
  one-two-three touch and a continuation story.
- ICT's read: the rally had only returned into the last up candle — a **bearish order block** —
  with the daily objective a liquidity void below. The "support" was a phantom; price broke lower.

**Example 4 — false breakout sequence (`ICT-2016-MMT-FALSE-BREAKOUT`, 05:27–12:19):**
- Repeating cycle: consolidation → break below to run sell stops (1.0895, then 1.0885) →
  expansion up into buy stops above the old high (1.0940, then 1.0945–1.0950).
- Read: the same side is run every time and price expands the other way — the market is
  **building a buy model**; each downside break is a false breakout by construction.

## Common Mistakes

- **Trading the pattern instead of the bias.** "Price does not move based on any kind of
  pattern" (`ICT-2016-MMT-FALSE-FLAG`, 03:02). Without the HTF read there is no trap, only a
  coin flip.
- **Using trendlines as support or resistance.** ICT rejects the premise; the only thing a
  trendline reliably marks is where retail's stops are.
- **Fading at the third touch instead of between touches 2 and 3.** The entry zone is the
  swing point *between* them; the stops sit at touch 2.
- **Measuring liquidity off wicks.** Bodies carry the volume, so the pools rest beyond bodies.
- **Hunting H&S on low timeframes at extremes.** Genuine ones form at intermediate and
  long-term highs; the low-timeframe versions are the trap.
- **Turning this into top- and bottom-picking.** ICT explicitly avoids calling long-term tops
  and bottoms; the trap is a liquidity event inside an existing bias.
- **Assuming every consolidation break is a trap.** It is a trap when it runs *against* the
  established HTF direction and the market has repeatedly expanded away from that side.

## Related Concepts

- [turtle-soup](../20-turtle-soup/turtle-soup.md) — the entry all four variants resolve to.
- [trendline-liquidity](../02-liquidity/trendline-liquidity.md) — the stop-cluster view of variant 3.
- [market-efficiency-paradigm](../03-order-flow/market-efficiency-paradigm.md) — the premise ICT invokes in three of the four lectures.
- [liquidity-pool](../02-liquidity/liquidity-pool.md), [stop-run-definition](../29-stop-runs/stop-run-definition.md) — what the retail trigger actually is.
- [order-block-criteria](../07-order-blocks/order-block-criteria.md), [breaker-block](../08-breaker-blocks/breaker-block.md) — the entry arrays used to fade.
- [premium-array](../05-pd-arrays/premium-array.md), [discount-array](../05-pd-arrays/discount-array.md) — where a false flag is expected to fail.
- [top-down-analysis](../25-htf-bias/top-down-analysis.md) — supplies the bias without which no pattern is a trap.
- [timeframe-selection](../25-htf-bias/timeframe-selection.md) — the stop-run setup family this belongs to.

## Citations

- `ICT-2016-MMT-FALSE-FLAG` (00:30) "this is lesson seven of eight of the second month of the mentorship… the market maker trap of false flags"; (01:40–01:47) "not all sudden price rallies that move into a short term consolidation are bull flags"; (01:51–02:08) false bull flags print "in a mature bull trend or in higher time frame distribution levels"; (02:24–02:39) higher-timeframe premium understanding as the discriminator; (03:02–03:14) "price does not move based on any kind of pattern"; (03:40–04:24) false bear flags at accumulation levels; (04:24–05:29) the textbook bull-flag / flagpole measured move; (11:01–11:25) the failed breakout "only… traded just above this old high"; (11:39–13:47) the daily bearish order block, the fib showing a premium/distribution area, and the four-hour bearish order block between two liquidity voids.
- `ICT-2016-MMT-FALSE-BREAKOUT` (00:30) "the eighth and final teaching for the second month… **month October**… market maker traps of false breakouts"; (00:58–01:58) false breakouts above consolidation manifest in primarily bearish markets and neutralise buy stops; (02:18–03:02) the bullish mirror; (04:34–05:21) sell stops below consolidation are used to pair long orders, then price expands to the buy stops; (09:02–09:25) "all the volume is seen in… the bodies of the candles, so the liquidity is going to rest above it"; (13:28–13:41) the diagnostic — which side is reached for, and where price goes afterwards; (16:00–16:19) "expect every drop down below an old area of consolidation… to be a false breakout and anticipate accumulation of long positions"; (16:41–18:04) the measured-move projections off each stop run.
- `ICT-2016-MMT-TRENDLINE` (00:30) "teaching number 7 of 8 for the month of **November 2016**… trendline phantoms or false trendlines"; (00:55–02:04) how retail primes and trades diagonal support and resistance; (02:08–02:32) "there's no basis on trendline theory… no statistical edge that I've been able to build"; (03:09–03:32) "price has no awareness of your trendline… price only respects where the actual liquidity is in the marketplace"; (04:56–05:00) the subjectivity objection; (07:28–07:58) the influx of weak-handed money at the line "provides liquidity for the market maker"; (07:58–09:01) fade the high between touch 2 and touch 3 with a bearish order block or turtle soup; (09:37–10:58) the bearish-trendline mirror, buying the low between high 2 and high 3; (11:00–11:45) "that's where everyone's stop loss is going to be" — point 2, not point 3; (12:44–12:50) "price is delivered to engineer efficiency for the smart money entities only"; (12:56–17:04) the December-2015 worked example.
- `ICT-2016-MMT-HEAD-SHOULDERS` (00:30) "for the month of **November 2016**… false tops and bottom patterns as it relates to classical head and shoulders"; (00:43–01:34) the textbook pattern, neckline and measured objective; (01:36–02:12) genuine patterns form "at intermediate or long-term highs only" while retail hunts them on lower timeframes; (02:24–02:38) "what I'm actually going to tell you is how you can capitalize on these patterns… [when] our higher timeframe premise indicates the opposite direction is unfolding"; (04:18–04:45) "we don't pick tops and bottoms"; (05:32–06:12) the neckline as a retail trap in a bullish institutional environment; (06:21–06:54) "I see that as a turtle soup long that took out two previous lows… I'll buy the sell stops below those equal lows… [target] the buy stops above the highest high"; (06:57–07:34) the inverted-H&S mirror; (07:34–07:41) first profit at the right shoulder; (07:45–12:14) the 12 August 2015 GBPUSD example; (12:14–16:46) the October inverted-H&S example using candle bodies at 1.5502; (17:17–17:27) "we're going to be attacking a lot of the retail-minded classical chart patterns throughout this ICT mentorship".
