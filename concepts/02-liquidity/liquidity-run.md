# Liquidity Run

**Category:** 02-liquidity
**Aliases:** run on liquidity, liquidity drive, run-and-reverse
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** liquidity, run, sweep, foundational

## Definition

A liquidity run is the broader, multi-bar move in which the algorithm drives price into a [liquidity-pool](liquidity-pool.md), takes the orders, and then either reverses (run-and-reverse) or continues through after harvesting the resting flow (run-and-continue). The run includes both the approach and the post-take behavior. A [liquidity-sweep](liquidity-sweep.md) is the single-candle event of taking the pool; a liquidity run is the full sequence around it.

## Formal Criteria

A liquidity run consists of:

1. **Approach** — directional move toward an identified pool, often after a contraction phase.
2. **Take** — the sweep candle (wick through the pool, with or without close beyond).
3. **Resolution** — either:
   - **Run-and-reverse:** displacement in the opposite direction, often leaving an FVG, often becoming an MSS / CHoCH.
   - **Run-and-continue:** displacement in the same direction, through the pool, with a true close beyond — the pool was fuel for continuation, not the destination.

## Formula / Math

```
liquidity_run := approach_phase
                  AND sweep_event(pool)
                  AND (
                    reverse_displacement_with_fvg
                    OR continue_displacement_through_pool
                  )
```

Resolution direction often determines whether the prior pool was the actual draw target (reverse) or just an interim refuel (continue).

## Machine-Readable

```json
{
  "id": "liquidity-run",
  "category": "02-liquidity",
  "aliases": ["run-on-liquidity", "liquidity-drive"],
  "criteria": [
    {"id": "c1", "expr": "approach_toward_pool == true"},
    {"id": "c2", "expr": "sweep_event_occurred == true"},
    {"id": "c3", "expr": "post_sweep_displacement_present == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["liquidity-sweep","liquidity-pool","draw-on-liquidity","stop-run-definition","judas-swing"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
  Run-and-reverse                Run-and-continue

         /\  ← sweep              ▲ ← sweep + close above
        /  \                      █
       /    \  reverse            █  continuation
      /      \  displacement      █
     /        \                   █
   approach    \                  █
                \                 ▲ approach
                 \                █
                  ─→ FVG          █
```

## Timeframes

Same as sweep. Most actionable on M5–H4.

## Examples

**Example 1 — Run-and-reverse (London open):**
- Asian high BSL at 1.0875.
- Approach: London opens, rallies into 1.0875.
- Take: M5 wicks 1.0880, closes 1.0871.
- Resolution: M5 displaces down 30 pips, leaves a 6-pip SIBI FVG.
- → run-and-reverse. The FVG is the entry zone for a short.

**Example 2 — Run-and-continue:**
- M15 has been bullish; sells off into PWL SSL at 1.0750.
- Take: wick to 1.0745, close at 1.0748 inside the level — but the next M15 candle prints a 25-pip body and closes at 1.0723.
- → run-and-continue (the SSL was fuel for the next bearish leg, not the destination).

## Common Mistakes

- **Reading every sweep as a reversal.** Run-and-continue is real and often costs traders who blind-fade sweeps. Wait for displacement direction.
- **Only watching one TF.** A run-and-continue on M5 may be inside a larger run-and-reverse on H1; align with HTF bias.
- **Conflating run with sweep.** Sweep = the one wick. Run = the full approach-take-resolution sequence.

## Related Concepts

- [liquidity-sweep](liquidity-sweep.md) — the one-candle event inside a run.
- [liquidity-pool](liquidity-pool.md) — what gets run.
- [draw-on-liquidity](draw-on-liquidity.md) — pool selection that drives runs.
- [stop-run-definition](../29-stop-runs/stop-run-definition.md) — overlapping concept.
- [judas-swing](../13-judas-swing/judas-swing.md) — the canonical session-open run.

## Citations

- `ICT-2017-CHARTER-OVERVIEW` — run-on-liquidity language.
- `ICT-2022-MENTORSHIP-OVERVIEW` — run-and-reverse vs run-and-continue framing.
