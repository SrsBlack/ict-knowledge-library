# Turtle Soup

**Category:** 20-turtle-soup
**Aliases:** TS, false breakout, failed breakout, breakout-fade
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** turtle-soup, false-breakout, foundational

## Definition

A **Turtle Soup** is a **failed breakout** pattern — price briefly trades through a known liquidity level (a swing high/low or session extreme), traps breakout traders, and immediately reverses back inside. Named after the original "Turtle Trader" breakout strategy that this pattern explicitly defeats. The Turtle Soup is the price-action mirror of a [liquidity-sweep](../02-liquidity/liquidity-sweep.md): the sweep is the event, the Turtle Soup is the named pattern. ICT borrowed the term from Larry Connors' original 1998 work and integrated it into the ICT framework as a high-probability reversal setup.

## Formal Criteria

A bullish Turtle Soup (failed bearish breakout):

- Price has been respecting a known SSL (swing low, EQL, session low).
- Price wicks below the SSL.
- The same candle (or within 1–3 bars) closes back above the SSL.
- Subsequent displacement upward confirms the failed breakout.

For bearish: symmetric (failed bullish breakout).

## Formula / Math

```
bullish_turtle_soup := low(n) < known_SSL_level
                       AND close(n+k) > known_SSL_level   for k in [0, 3]
                       AND post-event displacement is up

bearish_turtle_soup := high(n) > known_BSL_level
                       AND close(n+k) < known_BSL_level   for k in [0, 3]
                       AND post-event displacement is down
```

## Machine-Readable

```json
{
  "id": "turtle-soup",
  "category": "20-turtle-soup",
  "aliases": ["TS", "false-breakout", "failed-breakout", "breakout-fade"],
  "criteria": [
    {"id": "c1", "expr": "wick_through_known_level == true"},
    {"id": "c2", "expr": "close_back_inside_within_few_bars == true"},
    {"id": "c3", "expr": "post-event displacement opposite to break direction"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["bullish-turtle-soup","bearish-turtle-soup","stop-hunt-pattern","liquidity-sweep","liquidity-run","stop-run-definition","rejection-block"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish Turtle Soup:                 bearish Turtle Soup:

   resistance level                     ▲   ← wick above resistance
   ─────────                            █   ← close back inside
        │                            ───────
        │  (price respecting)
   support level                        support level
   ─────────                            ─────────
   ──╲   ←  wick below                          (price respecting)
     ╲╱   ← close back above            ▼  resistance level
        ──→ rally up                    ─────────
                                        ──╲  wick above
                                          ╲╱  close back inside
                                              ──→ sell-off
```

## Timeframes

All TFs M5+.

## Examples

**Example 1 — bullish Turtle Soup at PWL:**
- PWL at 1.0850 (known SSL).
- M15 wicks 1.0846 (4 pips below PWL), closes 1.0855.
- Next M15 candle: 18-pip green displacement, FVG forms.
- → bullish Turtle Soup. Long entry on FVG retest at CE.

## Common Mistakes

- **Calling every wick a Turtle Soup.** The level must be **known** liquidity (swing high/low, EQH/EQL, session extreme); random wicks don't qualify.
- **No bias filter.** Counter-bias Turtle Soup setups fail more often than bias-aligned ones.
- **Holding through the close-back-inside.** A wick that doesn't close back inside within 3 bars is a continuation, not a Turtle Soup.

## Related Concepts

- [bullish-turtle-soup](bullish-turtle-soup.md), [bearish-turtle-soup](bearish-turtle-soup.md), [stop-hunt-pattern](stop-hunt-pattern.md).
- [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [liquidity-run](../02-liquidity/liquidity-run.md), [stop-run-definition](../29-stop-runs/stop-run-definition.md), [rejection-block](../19-rejection-blocks/rejection-block.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — turtle-soup terminology integrated into ICT framework.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational use refined.
