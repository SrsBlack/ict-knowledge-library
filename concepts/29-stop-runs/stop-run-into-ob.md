# Stop Run into OB

**Category:** 29-stop-runs
**Aliases:** stop run + OB entry, OB-anchored stop run
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-ORDERBLOCKS, ICT-2016-TIMEFRAME-SELECTION, ICT-2017-BOND-SPLIT-SESSION, ICT-2017-INTRADAY-TOP-DOWN
**Tags:** stop-run, ob, entry

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2018`
sourced only to the placeholder IDs `ICT-2017-DISPLACEMENT` and
`ICT-2022-MENTORSHIP-OVERVIEW`. The composite is named as one of ICT's own setups in
**Month 03** (November 2016) — "I like a four-hour **turtle soup sell into a bearish order
block** that's seen on a daily chart" (`ICT-2016-TIMEFRAME-SELECTION`, 08:36–08:44) — and
the **Month 04** (December 2016) lecture *Orderblocks* works the entry exactly as this page
states it, at the order block's mean threshold: "I said that we would look for the **mean
threshold** of this down candle. Why? Because I didn't think we're going to get down to this
down candle — wasn't necessary, because I viewed this as a **run on stops**… but we traded
right back down into the middle point of this down candle for mean threshold"
(`ICT-2016-ORDERBLOCKS`, 32:46–33:05). Re-dated to **2016**. ⚠ `Year Refined: 2022` is
retained but remains **uncited**.

## Definition

A "stop run into OB" is the variant where the post-sweep displacement creates an order block — the **last opposite-color candle before the displacement** — and the OB body becomes the precise entry zone. Stop-run-into-OB setups are entered at the OB's MT (mean threshold) on retest, with SL beyond the sweep extreme. Mechanically similar to [stop-run-into-fvg](stop-run-into-fvg.md) but uses the OB body instead of an FVG as the algorithmic anchor.

## Formal Criteria

The sequence:

1. **Stop run event** — wick takes a known structural level.
2. **Last opposite-color candle** — qualifies as an OB per [order-block-criteria](../07-order-blocks/order-block-criteria.md).
3. **Displacement** breaks structure (BOS or CHoCH/MSS).
4. **Entry on OB retest at MT**.
5. **SL beyond the sweep extreme** (typically below OB low for longs, above OB high for shorts, with buffer).

## Formula / Math

```
stop_run_into_ob(setup):
    sweep_event
    AND last_opposite_color_candle qualifies as OB
    AND displacement_breaks_structure
    AND entry at OB MT on retest
    AND SL beyond sweep + buffer
```

## Machine-Readable

```json
{
  "id": "stop-run-into-ob",
  "category": "29-stop-runs",
  "aliases": ["stop-run-OB-entry", "OB-anchored-stop-run"],
  "criteria": [
    {"id": "c1", "expr": "sweep + OB qualification + displacement + BOS"},
    {"id": "c2", "expr": "entry at OB MT"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["stop-run-definition","stop-run-into-fvg","stop-run-into-breaker","bullish-order-block","bearish-order-block","mean-threshold","liquidity-sweep"],
  "sources": ["ICT-2016-ORDERBLOCKS","ICT-2016-TIMEFRAME-SELECTION","ICT-2017-BOND-SPLIT-SESSION","ICT-2017-INTRADAY-TOP-DOWN"]
}
```

## Visual Pattern

```
   bullish stop run into OB:

   ─── known SSL ─────
        │
        ▼  ← stop run wick
        ▼
        ▼   ← LAST bearish candle (this becomes the bullish OB)
            ▲▲▲   ← displacement up
           ▲▲▲▲   ← BOS through prior swing high
           ▲▲▲▲▲
                       ↓
                       retest to OB MT = entry
```

## Timeframes

M5–H4.

## Examples

**Example 1 — bullish stop run into OB:**
- HTF bullish; Asian SSL 1.0850.
- 02:55 NY: M15 wicks 1.0844; same M15 candle: O=1.0852, C=1.0848, L=1.0844, H=1.0855. Body [1.0848, 1.0852], MT 1.0850.
- 03:15 NY: next M15 = 22-pip green displacement, breaks prior M15 swing high (BOS).
- → bullish OB at 14:00 candle; on retest, entry at MT 1.0850; SL 1.0842 (sweep low - 2-pip buffer); risk 8 pips.

## Common Mistakes

- **Using a non-OB candle.** The candle must qualify per OB criteria (last opposite-color + displacement + structure-break).
- **Wide-range OBs.** OB body should be reasonably tight; wide OBs (large body, no clear MT) produce loose entries.
- **Waiting for an OB retest that ICT says will not come.** If the sweep runs without you and price then rallies *through* the short-term high, that high becomes a [bullish-breaker](../08-breaker-blocks/bullish-breaker.md) and the breaker — not the OB below it — is the entry. ICT is explicit that the deeper level is spent: "there may be a down-close candle down there, obviously… in many instances many folks will look for price to trade back down there and get to that order block; that's going to be below the breaker. **It's already been down there, and it's done its work**" (`ICT-2017-INTRADAY-TOP-DOWN`, 34:05–34:18). The bearish mirror scopes the same warning to the missed premium entry: "don't think at this moment there's going to be an optimal trade entry near where it says the sell level… a lot of folks get that screwed up thinking that they're going to have that range close in and get a retracement. They won't go that deep. Usually it's the breaker that stops it" (45:51–46:12). The bullish side denies the OTE at the *original* level in as many words — "so it's not going to be an **optimal trade entry from the buy level, the lower level of the discount array**; it's not going to retrace down into some discount array there because it's already ran the stops" (36:20–36:24). ⚠ But this is **not** a blanket "no OTE after a stop run" — on the bullish side ICT keeps the OTE, relocated: the breaker retest itself contains "a lower time frame … optimal trade entry, and it'll trade into a lower time frame bullish order block or a lower time frame discount array like a fair value gap" (34:47–35:10).

## Related Concepts

- [stop-run-definition](stop-run-definition.md), [stop-run-into-fvg](stop-run-into-fvg.md), [stop-run-into-breaker](stop-run-into-breaker.md).
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md), [mean-threshold](../27-equilibrium/mean-threshold.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md).

## Citations

- `ICT-2016-ORDERBLOCKS` (32:46–33:05) the mean-threshold entry taken *because* the move was read as a run on stops; (33:31–33:38) "waiting for confirmation that there is a displacement by smart money, and then simply waiting for those levels to be retraded down into."
- `ICT-2016-TIMEFRAME-SELECTION` (08:36–09:02) "a four hour turtle soup sell into a bearish order block that's seen on a daily chart", and the weekly/monthly version of the same composite; (43:31–44:11) the fallback when the turtle soup is missed — "there's other things you can trade, and they come in the way of breakers and bearish order blocks"; the down candle before the move up above the short-term high is taken as the entry instead.
- `ICT-2017-INTRADAY-TOP-DOWN` (36:20–36:24) the OTE denial, scoped to the original buy level; (36:37–36:56) the two-pattern taxonomy and the missed-entry contingency stated as ICT's own plan; (33:23–33:48) the missed-turtle-soup contingency — "I wait for price to rally through the short-term high, and now that short-term high becomes a bullish breaker… when price trades back down to the breaker, I'm going to use that as my entry"; (34:05–34:18) the OB below the breaker is spent; (34:47–35:10) the OTE survives on a lower timeframe at the breaker; (45:51–46:12) the bearish mirror; (46:14–46:22) the breaker as a pyramiding add if the original entry *was* filled.
- `ICT-2017-BOND-SPLIT-SESSION` (14:02–14:22) "it trades down, creates the Judas swing, and it creates a turtle soup, which is a move below the 154.02 level in the opening range… **that down-closed candle creates a bullish order block at that 154.02 level**"; (14:39–14:53) the two entries stated as alternatives — "a bullish order block during the a.m. session or a turtle soup, either or… or price trades back above that 154.03 level and then comes back down into the bullish order block."
