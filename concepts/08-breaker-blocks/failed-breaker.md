# Failed Breaker

**Category:** 08-breaker-blocks
**Aliases:** broken breaker, breaker failure, BB invalidated
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2018-BLOCKS, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** breaker, failure, invalidation

## Definition

A failed breaker is a breaker block whose retest **did not produce the expected new-polarity reaction** — instead, price went through the breaker zone in the original direction. The failure is a structural signal that the algorithmic intent assumed by the breaker has changed; usually accompanied by a new CHoCH or BOS in the failure direction. ICT teaches failed breaker recognition as essential risk-management discipline: don't add to a losing breaker hoping it'll work; reassess HTF bias.

## Formal Criteria

For a bullish breaker that fails:

- A bullish breaker had formed (originally bearish OB violated upward, retest expected to act as support).
- On the retest, price did NOT bounce — instead **closed below the breaker zone** with bearish displacement.
- Often a bearish CHoCH/BOS confirms the failure.

For a bearish breaker that fails: symmetric.

## Formula / Math

```
bullish_breaker_failure := close_t < low(breaker_zone)
                            AND bearish_displacement_after
                            AND ideally bearish_CHoCH_or_BOS confirms

bearish_breaker_failure := close_t > high(breaker_zone)
                            AND bullish_displacement_after
                            AND ideally bullish_CHoCH_or_BOS confirms
```

## Machine-Readable

```json
{
  "id": "failed-breaker",
  "category": "08-breaker-blocks",
  "aliases": ["broken-breaker", "breaker-failure", "BB-invalidated"],
  "criteria": [
    {"id": "c1", "expr": "breaker existed and was retested"},
    {"id": "c2", "expr": "retest closed through breaker zone in original (failure) direction"},
    {"id": "c3", "expr": "displacement_after_failure_present == true"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["breaker-block","bullish-breaker","bearish-breaker","mitigation-block","htf-bias-framework"],
  "sources": ["ICT-2018-BLOCKS","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish breaker failure:

   originally bearish OB → bullish breaker (after CHoCH up)
                       │
                       ↓ retest from above
   ─── breaker zone ─── ← expected: bullish bounce
                       │
                       ↓ INSTEAD: close below with bearish displacement
                       ↓
                       ▼▼▼▼ ← bearish CHoCH/BOS confirms failure
```

## Timeframes

M15+.

## Examples

**Example 1 — failed bullish breaker:**
- Bullish breaker formed at 1.0945–1.0955 (originally bearish OB that flipped).
- HTF bullish at the time of formation.
- On retest, H1 closes at 1.0938 (below 1.0945); subsequent bearish 25-pip H1 displacement; H4 prints bearish CHoCH.
- → bullish breaker failed. HTF bias flipping bearish; long bias should be abandoned. Don't add to longs hoping for a recovery — reassess.

## Common Mistakes

- **Adding to a losing breaker entry.** Once the breaker fails (close-through with displacement), the trade premise is invalidated. Don't average down.
- **No HTF reassessment.** Failed breakers often herald HTF bias shifts; failing to re-read HTF leads to repeated same-direction failures.
- **Tight invalidation.** A wick through the breaker zone followed by recovery is NOT a failure — require a closing print + displacement.

## Related Concepts

- [breaker-block](breaker-block.md), [bullish-breaker](bullish-breaker.md), [bearish-breaker](bearish-breaker.md), [mitigation-block](mitigation-block.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2018-BLOCKS`, `ICT-2022-MENTORSHIP-OVERVIEW`.
