# Breaker Block

**Category:** 08-breaker-blocks
**Aliases:** BB, breaker, broken OB
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2023
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** breaker, ob-flipped, foundational

## Definition

A **breaker block** is an order block that **failed in its original direction** — price violated the OB by closing through it with displacement — and now **flips polarity**: a failed bullish OB becomes a bearish breaker (resistance); a failed bearish OB becomes a bullish breaker (support). ICT teaches breakers as **high-conviction continuation references in the new direction** because the failure is itself an institutional signal of intent change. Breakers are the OB-side analogue of [inversion-fvg](../06-fair-value-gaps/inversion-fvg.md).

## Formal Criteria

A bullish OB → bearish breaker transformation:

- An originally bullish OB existed (last bearish candle before bullish displacement).
- Price subsequently breaks below the OB body (close below the OB low) with displacement.
- A bearish CHoCH or BOS typically accompanies the break.
- On the retest from below, the original bullish OB body now acts as **resistance** (the bearish breaker zone).

Bearish OB → bullish breaker: symmetric.

## Formula / Math

```
breaker_break_event(ob) := close_t < low(ob_body)        # for bull→bear
                            AND displacement_present_in_break

breaker_active_after_retest(ob, retest) := high(retest) reaches low(ob_body)
                                            AND rejection with displacement
                                            in opposite direction
```

## Machine-Readable

```json
{
  "id": "breaker-block",
  "category": "08-breaker-blocks",
  "aliases": ["BB", "breaker", "broken-OB"],
  "criteria": [
    {"id": "c1", "expr": "original_OB_was_violated_by_close_with_displacement == true"},
    {"id": "c2", "expr": "OB_body_now_acts_as_opposite_polarity_zone == true"},
    {"id": "c3", "expr": "retest_with_displacement_confirms_new_polarity == true"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2023",
  "related": ["bullish-breaker","bearish-breaker","mitigation-block","breaker-vs-mitigation","failed-breaker","bullish-order-block","bearish-order-block","inversion-fvg"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish OB → bearish breaker:

   Step 1: bullish OB forms (last down candle, then bullish displacement)
          ▼
          ▼  ← original OB
                ▲▲▲▲

   Step 2: later, price breaks BELOW the OB with bearish displacement
                                ▼▼▼▼
                                ▼▼▼▼ ← decisive close below OB low

   Step 3: price retraces UP to the OB body
                                       ▲▲▲
                                       ▲▲▲ ← retest reaches OB body
                                            (now bearish breaker)

   Step 4: rejection at OB body with displacement down → confirmed breaker
                                            ▼▼▼▼
```

## Timeframes

M15+. M5 breakers exist but lower conviction.

## Examples

**Example 1 — H1 bull OB → bearish breaker:**
- H1 bullish OB formed at 14:00 NY: body 1.0820–1.0830.
- 03:00 NY next day: H1 closes at 1.0815 (below 1.0820) with bearish displacement; bearish CHoCH on H4.
- Hours later: H1 retraces up to 1.0828 (inside original OB body).
- Bearish reaction with displacement → confirmed bearish breaker.
- Short on retest at MT (1.0825), SL above OB high at 1.0833 (3-pip buffer). Risk = 8 pips.

## Common Mistakes

- **Wick-only break.** Wick through OB body without close-through doesn't qualify as a breaker.
- **No retest.** A break without subsequent retest is just a violated OB; the breaker action requires the retest with rejection.
- **Confusing breaker with mitigation block.** They're related but distinct — see [breaker-vs-mitigation](breaker-vs-mitigation.md).

## Related Concepts

- [bullish-breaker](bullish-breaker.md), [bearish-breaker](bearish-breaker.md) — directional variants.
- [mitigation-block](mitigation-block.md), [breaker-vs-mitigation](breaker-vs-mitigation.md), [failed-breaker](failed-breaker.md).
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md).
- [inversion-fvg](../06-fair-value-gaps/inversion-fvg.md) — FVG-side analogue.

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
