# Bearish Order Block

**Category:** 07-order-blocks
**Aliases:** bearish OB, BeOB, supply OB (SMC), supply zone (SMC), supply block (SMC)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-ORDERBLOCKS, ICT-2022-MENTORSHIP-EP12, ICT-2022-MENTORSHIP-EP18, ICT-2022-MENTORSHIP-EP19
**Tags:** order-block, bearish, foundational

⚠ **Rewritten 2026-10-08 against an audit of `raw/*/report.md` (153 packets) and `m22/ep*.txt`
(40 captioned episodes).** Mirror of [bullish-order-block](bullish-order-block.md); the same ERA-SPLIT and
fresh-zone corrections apply. See [order-block-criteria](order-block-criteria.md) for the shared
multi-candle/confirmation rules.

## Definition

ICT teaches the bearish OB as the direct mirror of the bullish one: "everything I say here you'll
just reverse for a bearish order block" (ICT-2016-ORDERBLOCKS [00:54]). **2016:** the highest candle
or price bar with an up close, having the most open-to-close range among candidates, near an HTF
resistance level (old high/low) — mirroring [00:59–01:08], [02:20–02:27].

**2022 (ERA-SPLIT):** specifics given for the bearish case — "these two up close candles represent a
bearish order block, so we can use the low of the lowest up close candle and its opening price — you
draw that out in time" (EP19 [20:46–21:17]); "it's one, two, three candles making one consecutive
bearish order block." (EP18 [38:26]); the candle nearest price is the live reference: "if it trades
up into this candle here, the bottom one, the last one of the three going up, that's enough for me"
(EP18 [42:22]). ICT rejects the "last candle" framing for both polarities in the same breath: "order
block theory is much more than just simply the last up close candle before down move **or the last
down closed candle before the up move** — that's not it" (EP12 [44:09]); see
[bullish-order-block](bullish-order-block.md) for the companion EP18 quote.

Bearish OBs are premium-array references when sitting above current price.

**"Supply OB" is not ICT's term.** Same rejection of the supply-and-demand framing applies: "that's
why it's not supply and demand" (EP18 [40:41]). Kept above only as an SMC-community alias.

## Formal Criteria

Mirror of [bullish-order-block](bullish-order-block.md):

- 2016: highest up-close candle, most open-to-close range, near an HTF resistance level.
- 2022: the up-close candle(s) nearest price in a run, qualified by an imbalance on the move away.
- **Levels** (2022): "you have the candle low, the open, the mean threshold half the order block, and
  you have the high — the high is the less likely" (EP19 [80:56–81:23]).
- **Not fresh-only** — same multi-touch tolerance as the bullish case (`order-block-criteria`).
- ⚠ **Usage restriction ICT states for bearish OBs specifically (2016):** don't sell bearish OBs
  against HTF bullish order flow — "that's when you want to avoid bearish order blocks, because
  you're standing in the way of the institutional order flow" (ICT-2016-ORDERBLOCKS [25:40]); "only
  using bearish order blocks to take profits when time of day is an impact" [34:58].

## Formula / Math

```
bearish_ob_high := close(n)      # since close > open for the OB candle
bearish_ob_low  := open(n)
bearish_ob_mt   := (close(n) + open(n)) / 2

candidate_ob := argmax(high) over up-close candles near an HTF resistance level,
                tie-broken by max(close - open)
```

## Machine-Readable

```json
{
  "id": "bearish-order-block",
  "category": "07-order-blocks",
  "aliases": ["bearish-OB", "BeOB", "supply-OB (SMC)", "supply-zone (SMC)", "supply-block (SMC)"],
  "criteria": [
    {"id": "c1", "expr": "candle is bullish (close > open), highest among candidates, max(close-open) range, near an HTF resistance level (2016)"},
    {"id": "c2", "expr": "2022: nearest-to-price up-close candle(s) in a run, qualified by an imbalance left on the move away"},
    {"id": "c3", "expr": "NOT fresh-only: HTF blocks and 2022 doctrine both permit repeated return visits"},
    {"id": "c4", "expr": "do not sell bearish OBs against HTF bullish institutional order flow"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["order-block-criteria","bullish-order-block","mitigated-order-block","unmitigated-order-block","mean-threshold","premium-array","bearish-fvg","propulsion-block"],
  "sources": ["ICT-2016-ORDERBLOCKS","ICT-2022-MENTORSHIP-EP12","ICT-2022-MENTORSHIP-EP18","ICT-2022-MENTORSHIP-EP19"]
}
```

## Visual Pattern

```
   bearish OB (2016 reading):

   ▲               ← highest up-close candle, most open-to-close range,
   ▲                 near an HTF resistance level
                   body: close at top, open at bottom
                   ▼
                   ▼   ← later candle trades through the OB candle's low (validation)
                   ▼
                       ▼
                       ▼   ← imbalance left behind (2022 validity requirement)
                       ▼

   On retest: entry at the body extreme nearest price (low/open), NOT at MT by default.
```

## Timeframes

M1 through monthly — same as [bullish-order-block](bullish-order-block.md).

## Examples

**Example 1 — H1 bearish OB (2016-style selection):**
- 09:00 NY H1 bullish candle, the highest among recent up-close candidates with the greatest
  open-to-close range, near an old daily high: O=1.0945, C=1.0955, H=1.0958, L=1.0944. Body:
  [1.0945, 1.0955]. MT = 1.0950.
- 10:00 NY: bearish displacement; later candle's low trades through 1.0944 (validation).
- Entry on retest at the candle's low/open, not at MT by default. SL above the candle's high/open.

## Common Mistakes

- **Calling it "the last candle before displacement."** See [bullish-order-block](bullish-order-block.md) Common Mistakes — ICT rejects this framing for both polarities.
- **Requiring freshness.** Both eras tolerate repeated visits.
- **Selling bearish OBs into HTF bullish order flow.** ICT names this a specific error (ICT-2016-ORDERBLOCKS [25:40]).

## Related Concepts

- [order-block-criteria](order-block-criteria.md), [bullish-order-block](bullish-order-block.md), [mitigated-order-block](mitigated-order-block.md), [unmitigated-order-block](unmitigated-order-block.md).
- [mean-threshold](../27-equilibrium/mean-threshold.md), [premium-array](../05-pd-arrays/premium-array.md).
- [bearish-fvg](../06-fair-value-gaps/bearish-fvg.md), [propulsion-block](propulsion-block.md).

## Citations

- `ICT-2016-ORDERBLOCKS` [00:54] "everything I say here you'll just reverse for a bearish order block"; [25:40], [34:58] don't sell bearish OBs against HTF bullish order flow.
- `ICT-2022-MENTORSHIP-EP12` [44:09] "order block theory is much more than just simply the last up close candle before down move or the last down closed candle before the up move — that's not it."
- `ICT-2022-MENTORSHIP-EP18` [38:26], [40:41–41:12], [42:22] multi-candle framing, imbalance/fresh-zone rejection.
- `ICT-2022-MENTORSHIP-EP19` [20:46–21:17], [80:56–81:23] bearish-specific levels and candle selection.
