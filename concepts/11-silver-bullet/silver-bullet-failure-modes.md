# Silver Bullet — Failure Modes

**Category:** 11-silver-bullet
**Aliases:** SB failures, failed silver bullet, SB invalidation
**ICT Confidence:** high
**Year Introduced:** 2022
**Year Refined:** 2025
**Source IDs:** ICT-2022-SILVER-BULLET, ICT-2025-MACRO-PRECISION
**Tags:** silver-bullet, failure, risk

## Definition

Silver Bullet failure modes are the specific patterns by which an SB entry **fails to deliver the expected move**. ICT teaches failure-mode recognition as essential risk discipline: the SB rules produce many valid-looking setups, and learning the failure patterns prevents repeat losses on the same mistakes.

## Formal Criteria — The Four Common SB Failure Modes

1. **Counter-bias SB.** SB pattern fired in the wrong direction relative to HTF bias. Fails because the algorithm is going the other way regardless of the local sweep + FVG.
2. **Sweep-and-continue.** The "sweep" was actually run-and-continue (the swept liquidity was fuel, not a reversal trigger). Fails because the algorithm wanted that liquidity for the same-direction move that follows.
3. **Premature entry / no displacement.** Entered on the FVG before displacement-with-FVG was confirmed. Fails because there was no real algorithmic intent.
4. **Window-edge SB.** SB pattern fires at 10:55–11:00 NY (last 5 min) and rolls into the next session unfinished. Fails because the institutional SB participation ends with the window.

## Formula / Math

```
sb_failure_mode(setup):
  if not htf_bias_aligned(setup):     return "counter_bias"
  if not reversal_after_sweep(setup): return "sweep_and_continue"
  if not displacement_confirmed(setup): return "premature_entry"
  if window_minutes_remaining < 10:   return "window_edge"
```

## Machine-Readable

```json
{
  "id": "silver-bullet-failure-modes",
  "category": "11-silver-bullet",
  "aliases": ["SB-failures", "failed-silver-bullet"],
  "criteria": [
    {"id": "c1", "expr": "counter_bias is highest-frequency failure"},
    {"id": "c2", "expr": "sweep_and_continue is second"},
    {"id": "c3", "expr": "premature_entry and window_edge complete the four"}
  ],
  "timeframes": ["M1","M5"],
  "confidence": "high",
  "year_introduced": "2022",
  "year_refined": "2025",
  "related": ["silver-bullet-overview","silver-bullet-rules","htf-bias-framework","liquidity-run","liquidity-sweep","displacement-definition"],
  "sources": ["ICT-2022-SILVER-BULLET","ICT-2025-MACRO-PRECISION"]
}
```

## Visual Pattern

Failures are state-of-affairs descriptions, not chart patterns. See per-mode examples.

## Timeframes

M1 / M5.

## Examples

**Example 1 — counter-bias failure:**
- HTF bearish but trader took bullish-side SB at 10:00 because of a clean sweep + FVG up.
- Bias is wrong; algorithm continues down; SL hit at 1.0908.
- Lesson: the sweep was the start of the bearish move (run-and-continue), not a reversal.

**Example 2 — sweep-and-continue:**
- HTF bullish; Asian SSL swept at 03:00 (London SB).
- Trader long on FVG; expected reversal up.
- Instead: M5 continues down through the FVG; bullish FVG becomes IFVG.
- Lesson: this was a run-and-continue (HTF wasn't actually bullish — it was transitioning). Re-read HTF after failure.

**Example 3 — premature entry:**
- 10:00 NY: M5 wicks below recent low (looks like sweep). Trader pre-positions long at the FVG above.
- 10:05: M5 prints another red candle; no bullish displacement materializes; SL hit.
- Lesson: wait for the displacement candle to close before considering FVG entry.

**Example 4 — window-edge:**
- 10:50 NY: clean SB pattern forms.
- Trader enters at 10:55; expects continuation into 11:30+.
- 11:00–11:30: institutional volume drops; price stalls; SL/TP both miss; trade closes flat or small loss.

## Common Mistakes

- **Pattern-matching without bias.** Most SB failures trace back to a missing or wrong HTF bias check.
- **No post-failure reset.** A failed SB doesn't always mean "try again next window" — sometimes HTF bias has flipped and the next window will fail too.
- **Window-edge greed.** Skip late-window SBs unless conviction is exceptional.

## Related Concepts

- [silver-bullet-overview](silver-bullet-overview.md), [silver-bullet-rules](silver-bullet-rules.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [liquidity-run](../02-liquidity/liquidity-run.md), [liquidity-sweep](../02-liquidity/liquidity-sweep.md), [displacement-definition](../09-displacement/displacement-definition.md).

## Citations

- `ICT-2022-SILVER-BULLET`, `ICT-2025-MACRO-PRECISION`.
