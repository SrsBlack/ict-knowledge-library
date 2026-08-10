# Stop Run into FVG

**Category:** 29-stop-runs
**Aliases:** stop run + FVG entry, FVG-anchored stop run
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-FVG-REINFORCED, ICT-2017-BOND-SPLIT-SESSION
**Tags:** stop-run, fvg, entry

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2018`
sourced only to the placeholder IDs `ICT-2017-DISPLACEMENT` and
`ICT-2022-MENTORSHIP-OVERVIEW`. The **Month 04** (December 2016) lecture *ICT Fair Value
Gaps FVG* teaches the pairing in both roles. As a **draw**: "we have a low delineated for
potential liquidity run on sell stops below the low… and now we can expect to see what form?
A turtle soup, or a false break below an old low. Why would we reasonably expect it to go
back up to fill in that gap? Because we've already taken the sell-side liquidity out by
running an old low" (`ICT-2016-FVG-REINFORCED`, 06:42–07:09). As an **entry** — the sequence
this page describes: "now I'm going to show you what it looks like when we have a run above
an old high… so it's running buy stops, but also it's hitting that fair value gap also, so
it's trading into the fair value gap" (10:22–10:47), then "we can be a seller at a more
refined price level… we could be a seller at 104.70 on a limit; when price trades back up to
that level… there's your sell" (12:42–13:07). Re-dated to **2016**. ⚠ `Year Refined: 2022`
is retained but remains **uncited**.

## Definition

A "stop run into FVG" is the high-conviction sequence: stop run sweeps a known liquidity level, then a displacement candle leaves an FVG, providing the entry zone for a position aligned with the post-sweep direction. This is one of ICT's most-traded combinations — the stop run gives the entry the algorithmic anchor (where the institutional position got filled), and the FVG gives the precise retest level.

## Formal Criteria

The full sequence:

1. **Stop run event** — wick takes a known structural level.
2. **Displacement** — wide candle in the post-sweep direction (typically opposite to the sweep direction = Turtle Soup outcome; sometimes same direction = run-and-continue).
3. **FVG forms** — inside or after the displacement.
4. **Entry on FVG retest** at CE (per 2025 default).
5. **SL beyond the swept extreme**.

## Formula / Math

```
stop_run_into_fvg(setup):
    sweep_event_at_known_level
    AND displacement_after_sweep
    AND FVG forms
    AND entry at FVG CE on retest
    AND SL beyond sweep extreme + buffer
```

## Machine-Readable

```json
{
  "id": "stop-run-into-fvg",
  "category": "29-stop-runs",
  "aliases": ["stop-run-FVG-entry", "FVG-anchored-stop-run"],
  "criteria": [
    {"id": "c1", "expr": "sweep + displacement + FVG sequence"},
    {"id": "c2", "expr": "entry at FVG CE"},
    {"id": "c3", "expr": "SL beyond sweep extreme"}
  ],
  "timeframes": ["M5","M15","H1","H4"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["stop-run-definition","stop-run-into-ob","stop-run-into-breaker","fair-value-gap","ce-as-primary-entry","liquidity-sweep","silver-bullet-rules"],
  "sources": ["ICT-2016-FVG-REINFORCED","ICT-2017-BOND-SPLIT-SESSION"]
}
```

## Visual Pattern

```
   bullish stop run into FVG:

   ─── known SSL ─────
        │
        ▼  ← stop run wick (sweep)
        ╲╱
         ▲▲▲   ← displacement up
        ▲ █▲   ← bullish FVG inside displacement
       ▲ █ ▲
                       ↓
                       retest to FVG CE = entry
```

## Timeframes

M5–H4.

## Examples

**Example 1 — bullish stop run into FVG (London open):**
- HTF bullish; Asian SSL at 1.0850.
- 02:55 NY: M5 wicks 1.0846 (sweep).
- 03:05 NY: M5 18-pip green displacement, FVG at 1.0856–1.0860.
- 03:25 NY: M5 retests CE 1.0858. Long entry.
- SL 1.0844 (sweep low - 2-pip buffer); risk 14 pips.
- TP -1.5 SD or PDH.

## Common Mistakes

- **Pre-positioning at FVG before displacement.** The FVG zone must form *after* the sweep + displacement; entering earlier on a "near miss" is premature.
- **Stop run direction confusion.** Take direction from post-sweep displacement; the sweep direction is misleading.

## Related Concepts

- [stop-run-definition](stop-run-definition.md), [stop-run-into-ob](stop-run-into-ob.md), [stop-run-into-breaker](stop-run-into-breaker.md).
- [fair-value-gap](../06-fair-value-gaps/fair-value-gap.md), [ce-as-primary-entry](../06-fair-value-gaps/ce-as-primary-entry.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [silver-bullet-rules](../11-silver-bullet/silver-bullet-rules.md).

## Citations

- `ICT-2016-FVG-REINFORCED` (06:42–07:09) stop run below an old low as the reason the gap above gets filled; (10:22–10:47) "a run above an old high… it's running buy stops, but also it's hitting that fair value gap also, so it's trading into the fair value gap"; (12:42–13:07) the gap as the refined limit entry after the run; (07:58–08:08) "looking for stops and looking for fair value gaps" named as the range-bound trading style.
- `ICT-2017-BOND-SPLIT-SESSION` (13:37–13:47) "when there's a large opening range, we want to start looking for retracement ideas or fair value ideas — in other words, bullish order blocks, fair value gaps to be a buyer or seller in"; (14:02–15:15) the turtle soup below the 8–9 a.m. opening range, then "price trades down into, fills the fair value gap at 154.03 into 154.02… and price rallies from 154.02 all the way up into 154.10."
