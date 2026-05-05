# Judas Swing Failure

**Category:** 13-judas-swing
**Aliases:** Judas failure, failed Judas, no-reversal open, Judas trap
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** judas, failure, false-judas, risk

## Definition

A Judas swing failure is when the expected Judas pattern **does not reverse**: the session-open directional move continues in the same direction, taking out the opposite-side liquidity pool with displacement, instead of reversing back through the range. The "Judas" was actually **the real delivery**. ICT teaches Judas-failure recognition as critical because mistaking a real delivery for a fake-out leads to entries against the actual move.

## Formal Criteria

A Judas-swing failure shows:

- A session-open move that sweeps one bound (looks like a Judas).
- **No reversal** within the killzone — instead, the same-direction move continues.
- Displacement extends, takes the opposite bound's liquidity (turns sweep into BOS).
- Often signals the **opposite of HTF bias has briefly taken control** — either HTF bias is genuinely flipping, or this is a "high-volatility trap" day where neither side gets clean delivery.

## Formula / Math

```
judas_failure := initial_move_swept_one_pool == true
                  AND no_reversal_within_kz == true
                  AND continues_same_direction_with_displacement == true
                  AND eventually_takes_opposite_bound == true
```

The simplest live tell: by 30–45 minutes into the killzone, if the price is **still extending in the initial direction** without any meaningful pullback or displacement reversal, treat the Judas hypothesis as failed.

## Machine-Readable

```json
{
  "id": "judas-swing-failure",
  "category": "13-judas-swing",
  "aliases": ["judas-failure", "failed-judas", "judas-trap"],
  "criteria": [
    {"id": "c1", "expr": "initial_move_swept_pool == true"},
    {"id": "c2", "expr": "no_reversal_within_kz == true"},
    {"id": "c3", "expr": "continuation_same_direction_with_displacement == true"}
  ],
  "timeframes": ["M1","M5","M15"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["judas-swing","london-judas-swing","ny-judas-swing","liquidity-run","htf-bias-framework"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   Expected Judas:                   Failed Judas:

   ↑ initial direction               ↑ initial direction
   ↑ (fake)                          ↑
   ↑                                 ↑ (continues — NO reversal)
   ↓ reversal                        ↑
   ↓                                 ↑
   ↓ true delivery                   ↑ same direction extends
                                     ↑
                                     ↑ takes opposite bound
                                     ↑ eventually
```

## Timeframes

M1 / M5 / M15.

## Examples

**Example 1 — failed bullish Judas:**
- HTF bias bullish; trader expects low-side sweep + bullish reversal.
- 02:25 NY: Asian SSL swept at 1.0846; close 1.0852 — looks textbook.
- 02:50 NY: instead of displacement up, M5 prints another -8-pip candle, close 1.0844. No bullish FVG, no reversal.
- 03:15: continues down, takes 1.0830 (PDL SSL).
- → Judas failed; the "Judas" was real bearish delivery. HTF may be flipping bearish, or this is a high-volatility trap day.

## Common Mistakes

- **Insisting on Judas reversal.** Once the failure is evident (no reversal by ~45 min into KZ), abandon the Judas hypothesis. Don't keep adding to a long position waiting for a reversal that isn't coming.
- **Over-trading failed sessions.** When Judas fails, the day's character is often choppy or strongly trending in the unexpected direction — neither is great for textbook ICT setups. Reduce size or skip.
- **Confusing failure with run-and-continue.** Some sweeps are deliberate "fuel" for continuation in the same direction (run-and-continue, see [liquidity-run](../02-liquidity/liquidity-run.md)). That's not a failure of Judas — it's a different setup type that the analyst should have read from HTF.

## Related Concepts

- [judas-swing](judas-swing.md) — the expected pattern.
- [london-judas-swing](london-judas-swing.md), [ny-judas-swing](ny-judas-swing.md) — variants.
- [liquidity-run](../02-liquidity/liquidity-run.md) — run-and-continue alternative read.
- [htf-bias-framework](../25-htf-bias/htf-bias-framework.md) — Judas-failure often signals HTF bias is flipping.

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
