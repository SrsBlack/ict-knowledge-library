# Algorithmic Price Delivery (APD)

**Category:** 03-order-flow
**Aliases:** APD, algorithmic delivery, the algorithm
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2018-IPDA, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** order-flow, algorithm, foundational

## Definition

Algorithmic Price Delivery is ICT's **core thesis**: that price in major liquid markets is **delivered by an algorithm**, not produced by a continuous random walk. The algorithm — sometimes called the IPDA ([ipda-definition](../23-ipda/ipda-definition.md)) — operates within structured rules: targeting liquidity pools, respecting PD arrays, executing within killzones and macro times, following AMD-X cycles. APD is the **explanatory framework** for every other ICT concept: every PD array, killzone, sweep, displacement, and bias shift is interpreted as algorithmic behavior, not coincidence.

## Formal Criteria

ICT's claims about APD:

- Price is **engineered** (sweeps, FVGs, displacement) rather than random.
- Time-of-day matters: killzones, macros, session opens are programmed delivery moments.
- Liquidity is targeted: BSL/SSL pools are destinations.
- PD arrays are decision points where the algorithm references prior structure.
- The same patterns repeat at every TF (fractal behavior).

The framework is **interpretive**: ICT does not claim to know the literal algorithm, only that price patterns are consistent with one. The value lies in the pattern recognition discipline.

## Formula / Math

APD has no single formula; it is a meta-framework that ties together:

```
apd_observable_patterns = [
    structural (BOS, CHoCH, MSS),
    pd_arrays  (FVG, OB, breaker, etc),
    liquidity  (sweeps, runs, pools),
    time       (killzones, macros, sessions, QT),
    bias       (HTF directional reads),
]

# All of these are different angles on the same algorithmic delivery.
```

## Machine-Readable

```json
{
  "id": "algorithmic-price-delivery",
  "category": "03-order-flow",
  "aliases": ["APD", "algorithmic-delivery", "the-algorithm"],
  "criteria": [
    {"id": "c1", "expr": "price is engineered not random"},
    {"id": "c2", "expr": "time-of-day matters"},
    {"id": "c3", "expr": "liquidity is the target; PD arrays are the decision points"},
    {"id": "c4", "expr": "fractal pattern repetition at every TF"}
  ],
  "timeframes": ["all"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["institutional-order-flow","bullish-order-flow","bearish-order-flow","order-flow-shift","smart-money-footprint","ipda-definition","quarterly-shift-theory"],
  "sources": ["ICT-2018-IPDA","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

APD is a meta-concept; its "visual pattern" is every other ICT pattern interpreted through this lens.

```
   APD interpretive view:

   any chart event (sweep, FVG, displacement)
        ↓
   read as algorithmic intent rather than randomness
        ↓
   align with HTF bias + time + liquidity context
        ↓
   produces the trader's setup hypothesis
```

## Timeframes

All TFs.

## Examples

**Example 1 — APD reading of a textbook setup:**
- 02:55 NY: Asian SSL swept (APD: algorithm raids stops).
- 03:05: M5 displacement up + FVG (APD: institutional positioning leaves orderbook imbalance).
- 03:30: H1 CHoCH up (APD: bias-flip signal at HTF).
- 04:00–11:00: distribution to PDH BSL (APD: delivery to targeted DOL).
- → every step interpreted as algorithmic, not random.

## Common Mistakes

- **Treating APD as literal orderbook claim.** It's a pattern-recognition framework, not a tape-reading method.
- **Forcing every wick into APD framing.** Some moves are genuinely noise; APD is best applied with context, not universally.
- **Skeptic vs believer dichotomy.** Even if APD is "just a useful pattern catalog," it produces tradeable edges; the philosophical question is separable from the practical value.

## Related Concepts

- [institutional-order-flow](institutional-order-flow.md), [bullish-order-flow](bullish-order-flow.md), [bearish-order-flow](bearish-order-flow.md), [order-flow-shift](order-flow-shift.md), [smart-money-footprint](smart-money-footprint.md).
- [ipda-definition](../23-ipda/ipda-definition.md), [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md).

## Citations

- `ICT-2018-IPDA`, `ICT-2022-MENTORSHIP-OVERVIEW`.
