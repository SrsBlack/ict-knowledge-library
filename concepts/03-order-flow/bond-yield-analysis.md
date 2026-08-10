# Bond Yield Analysis

**Category:** 03-order-flow
**Aliases:** 10-year note analysis, treasury yield analysis, 10Y/DXY read, bond-dollar correlation
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-10YR-HTF, ICT-2017-10YR-QUALIFYING
**Tags:** order-flow, intermarket, bonds, yields, dollar-index, seasonality, smt, regime

## Definition

Bond yield analysis is ICT's use of the **10-year treasury note — its futures price and
its yield — as the higher-timeframe context filter for the dollar index and, through the
dollar, for FX**. Its output is not an entry. It answers two questions: **which way** the
dollar is inclined, and, more importantly, **whether the environment is trending at all**.

The mechanism is the yield-seeking flow of capital: "as a general rule of thumb, long
term funds seek yield" (`ICT-2017-10YR-HTF`, 02:17), so a rising yield gives the dollar
index its easiest path higher and a falling yield its easiest path lower. Because note
**price** is inverted to **yield**, the two charts must be read as opposites.

## Formal Criteria

**The inversion (must be held straight before anything else)**

- "Treasury prices are inverted to its yield" (01:45). Note futures **down** = yield **up**;
  note futures **up** = yield **down**.
- Dollar index "can rally when the yields increase… and has its easiest or most opportune
  time to decline when yields decrease" (02:32–02:54).

**The two seasonal templates**

- **10-year note (futures price):** a **January–February high**, declining to a **low in the
  last week of May into early July**, then rallying into **December highs** (00:42–03:38).
  Bearish first half of the year, bullish second half.
- **Dollar index:** rally around **January–February**, a significant high **June–July**,
  then down for the rest of the year with a low around the **last week of October / first
  week of November** and a small November bounce (04:42–05:21).
- The two templates are deliberately **contrasting** — that opposition is the tradeable
  condition.

**The regime test (the primary output)**

- Notes and dollar index moving **in tandem** → "long-term indecisiveness"; both markets,
  and therefore FX, are in a **large consolidation** (10:16–10:48). Trade short-term and
  day trades; expect old highs and lows to be violated and price returned to mid-range.
  Position trades are "highly unlikely" to work (16:08–16:24).
- Notes moving **with their seasonal** while the dollar index moves **inversely** → a
  **directional long-term trend**; "that's where the large funds place their money"
  (11:18–11:47). Position and swing trades are favoured.

**Qualifying with a crack in correlation** (`ICT-2017-10YR-QUALIFYING`)

- Perfect symmetry is the null: 10-year notes making **lower lows** should be mirrored by
  the dollar index making **higher highs**. "It's going to be a mirror image of everything
  you see for perfect symmetry" (05:46).
- **When that symmetry breaks, the divergence is the signal:** "when that symmetry is
  broken it indicates there is an underlying trend or manipulation underway" (05:50). ICT
  calls the break a **crack in correlation** (02:08) and, later in the same lesson, names
  it explicitly as an **SMT divergence** between the dollar index and the 10-year note
  (08:03).
- Confirm visually on the **yield** chart, not only the futures chart (02:11, 03:54).
- Optional corroboration: **open interest**. A November-2016 decline in open interest is
  read as commercial **short covering** supporting the dollar rally (05:58).
- **Time horizon:** blend with quarterly shifts; ICT's stated horizon is **about three
  months**, with setups "generally … half that time frame" to complete (06:42–08:03).

**Data sources named** (01:26–01:40)

- 10-year treasury **prices / futures** — barchart.com.
- 10-year treasury **yields** — investing.com.

## Formula / Math

```
# --- inversion ---
yield(t)  ~  -price_10Y_futures(t)          # strictly inverse in direction

# --- directional inclination ---
yield rising   -> DXY has the easier path UP
yield falling  -> DXY has the easier path DOWN

# --- regime test (the main output) ---
tandem := sign(trend(price_10Y)) == sign(trend(DXY))

regime := tandem ? CONSOLIDATION      # range-bound; short-term / day trades only
                 : TRENDING           # position and swing trades favoured

# --- qualifying: crack in correlation (SMT between 10Y and DXY) ---
symmetric := (price_10Y makes lower_lows  AND DXY makes higher_highs)
          OR (price_10Y makes higher_highs AND DXY makes lower_lows)

crack_in_correlation := NOT symmetric
# e.g. 10Y equal lows while DXY makes higher highs   -> crack
#      10Y lower high  while DXY makes a lower low    -> crack

qualifying_condition := crack_in_correlation
                        AND seasonal_window_active
                        AND (optional) open_interest_confirms

horizon := ~3 months, typically resolving in ~1.5
```

## Machine-Readable

```json
{
  "id": "bond-yield-analysis",
  "category": "03-order-flow",
  "aliases": ["10-year-note-analysis", "treasury-yield-analysis", "bond-dollar-correlation"],
  "criteria": [
    {"id": "c1", "expr": "price_10Y inverse_to yield_10Y"},
    {"id": "c2", "expr": "yield_rising => DXY_bullish_bias; yield_falling => DXY_bearish_bias"},
    {"id": "c3", "expr": "seasonal_10Y: high Jan-Feb, low late-May..early-Jul, rally into Dec"},
    {"id": "c4", "expr": "seasonal_DXY: rally Jan-Feb, high Jun-Jul, low late-Oct..early-Nov"},
    {"id": "c5", "expr": "tandem(price_10Y, DXY) => consolidation_regime => short_term_trades_only"},
    {"id": "c6", "expr": "inverse(price_10Y, DXY) with seasonal => trending_regime => position_trades_favoured"},
    {"id": "c7", "expr": "crack_in_correlation == broken_mirror_symmetry(10Y, DXY) == SMT_divergence"},
    {"id": "c8", "expr": "confirm_on_yield_chart == true"},
    {"id": "c9", "expr": "time_horizon_months ~= 3 (typically resolves in ~1.5)"},
    {"id": "c10", "expr": "supplies_entry == false"}
  ],
  "timeframes": ["D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["dollar-index", "interest-rate-differentials", "seasonal-tendency", "smt-divergence", "index-smt", "open-interest", "quarterly-shift-theory", "explosive-market-selection"],
  "sources": ["ICT-2017-10YR-HTF", "ICT-2017-10YR-QUALIFYING"]
}
```

## Visual Pattern

```
  SYMMETRIC (no signal) — the mirror holds
     10Y notes  ╲___                 DXY      ___╱‾
                    ╲___                    ╱‾
        lower lows                      higher highs      -> nothing to qualify

  CRACK IN CORRELATION — the mirror breaks
     10Y notes  ═══ ═══  (equal lows)   DXY      ___╱‾ ╱‾‾
                                                ╱‾   ╱
        10Y refuses to make the lower low that DXY's higher high demands
        -> "underlying trend or manipulation underway"

  REGIME TEST
     price_10Y  ↑  and  DXY ↑     both up together  -> CONSOLIDATION (FX ranges)
     price_10Y  ↓  and  DXY ↓     both down together -> CONSOLIDATION (FX ranges)
     price_10Y  ↓  and  DXY ↑     proper inversion   -> TRENDING (position trades)
     price_10Y  ↑  and  DXY ↓     proper inversion   -> TRENDING (position trades)
```

## Timeframes

Daily, weekly and monthly only. This is a macro-context read feeding quarterly-scale bias;
it has no intraday application.

## Examples

**Example 1 — tandem move = consolidation (ZNU15, June–August 2015, `ICT-2017-10YR-HTF` 07:21–09:17):**
- Setup: the September 2015 10-year contract made its seasonal June low and rallied,
  which should have been bearish for the dollar index.
- Observation: the dollar index rallied at the same time — both markets up together.
- Read: **large consolidation**, not a trend. The dollar subsequently took out the
  May/June lows and moved sideways; FX pairs ranged.

**Example 2 — crack in correlation (June 2016, `ICT-2017-10YR-QUALIFYING` 02:58–04:11):**
- Setup: the 10-year note made **equal lows** into June 2016. Symmetry demanded **equal
  highs** in the dollar index.
- Observation: the dollar index made **higher highs** instead. "That's a crack in
  correlation there, therefore it is a qualifying condition that there is an underlying
  trade underway" (03:47).
- Confirmation: 10-year **yields** declining at the same time; the whole complex still
  inside a large consolidation, which is why FX ranged through mid-2016.

**Example 3 — trending regime (March-2017 contract, November 2016, both sources):**
- Setup: seasonal tendency for the March contract to top in November; the US presidential
  election supplied the catalyst. Ignoring the election wick, the note put in a **lower
  high** in early November against the mid-October high.
- Observation: the dollar index printed a **lower low** where a higher high was required —
  a crack. Open interest fell through November (commercial short covering).
- Read: notes trending down = yields rising = dollar trending up. The dollar rallied for
  "two complete months" (`ICT-2017-10YR-QUALIFYING`, 06:18).

## Common Mistakes

- **Confusing the note chart with the yield chart.** They move opposite. ICT keeps two
  data sources precisely to avoid this.
- **Treating tandem movement as confirmation.** It is the opposite — both markets moving
  the same way is the **consolidation warning**, and it is the single most actionable
  output of this page.
- **Assuming the seasonal always fires.** The lecture is explicit that it also covers
  "when the seasonal tendency doesn't have an influence… and when the market actually
  performs adversely" (00:56–01:21); when the June–July buy window fails, the fallback is
  to work from the seasonal **highs** instead (16:36–17:13).
- **Reading a crack in correlation as an entry.** It is a *qualifying* condition for a
  quarterly-shift idea; entries still come from the ordinary toolkit.
- **Letting a news wick define structure.** For the November 2016 example ICT instructs
  "dispel that for a moment, focus on the market structure alone without that wick"
  (`ICT-2017-10YR-QUALIFYING`, 04:49).
- **Treating this as the same thing as [interest-rate-differentials](interest-rate-differentials.md).**
  Rate differentials compare *policy rates between two central banks* to bias a pair; this
  page reads *one market's yield against the dollar index* to classify the regime.

## Related Concepts

- [dollar-index](dollar-index.md) — the market this read is aimed at.
- [interest-rate-differentials](interest-rate-differentials.md) — the other rate-based macro input; different mechanism, same month of the mentorship.
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — supplies both seasonal templates.
- [smt-divergence](../16-smt-divergence/smt-divergence.md), [index-smt](../16-smt-divergence/index-smt.md) — the crack in correlation is SMT applied to the 10Y/DXY pair.
- [open-interest](open-interest.md) — the short-covering corroboration.
- [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md) — the ~3-month horizon this feeds.
- [explosive-market-selection](../31-models/explosive-market-selection.md) — where the interest-rate asset class enters the trending-environment count.
- [mega-trade](../31-models/mega-trade.md) — the position-scale expression of a trending bond regime.

## Citations

- `ICT-2017-10YR-HTF` (00:00) "this is lesson 2.1 of January 2017 ITT mentorship… using 10-year yields in higher timeframe analysis"; (00:42–01:05) the two dominant seasonal cycles — January/February high to June low, June low into December highs; "bearish for the first half of the year and then bullish for the second part"; (00:56–01:21) the lecture also covers when the seasonal fails; (01:26–01:40) barchart.com for prices, investing.com for yields; (01:45–02:04) "treasury prices are inverted to its yield"; (02:17) "long term funds seek yield"; (02:32–02:54) dollar rallies on rising yields, declines on falling yields; (02:58–03:38) zoomed seasonal — last week of May into first week of July low; (04:42–05:21) the dollar index seasonal template; (07:21–09:17) the ZNU15 2015 tandem example; (10:16–10:48) "if that occurs, what we're looking at is long-term indecisiveness… the likelihood of a continued directional trade… is highly unlikely"; (11:18–11:47) seasonal alignment plus inverse dollar = "strong probability of a directional long-term trend… that's where the large funds place their money"; (13:00–14:48) the March-2017 contract / November election example; (16:08–16:32) consolidation → short-term trades and day trades; trending → position trades; (16:36–17:13) the fallback when the June–July buy signal is absent.
- `ICT-2017-10YR-QUALIFYING` (00:00) "this is lesson 2.2 of the … January 2017 ICT mentorship… qualifying trade conditions with the 10-year yields"; (00:54–01:04) qualify the swings against the dollar index; (01:35–01:46) "in the dollar index this is going to be ideally seen with a series of higher highs… that's how market symmetry should be posted and delivered in price"; (02:08–02:20) "this is a crack in correlation… we have confirmation now there is a trade idea unfolding"; (02:58–04:11) the June 2016 equal-lows example; (04:41–04:53) "dispel that [election] wick for a moment, focus on the market structure alone"; (05:46–05:58) "it's going to be a mirror image of everything you see for perfect symmetry — when that symmetry is broken it indicates there is an underlying trend or manipulation underway"; (05:58–06:10) open-interest decline as commercial short covering; (06:18) the dollar "was allowed to trade for two complete months"; (06:42–08:03) blend with quarterly shifts; three-month horizon typically resolving in half; (08:03–08:36) "qualifying SMT divergences between the dollar index and the 10 year note"; (09:00–09:20) the read puts swing, short-term and day trades in line with institutional order flow.
