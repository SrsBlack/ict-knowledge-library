# Mitigation of Breaker

**Category:** 18-mitigation
**Aliases:** breaker mitigation, breaker tested, BB retest
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2023
**Source IDs:** ICT-2016-BREAKER-BLOCK, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** mitigation, breaker

## Definition

Mitigation of a breaker is when price **retests the breaker zone** (the body of the originally-violated OB) and produces the new-polarity reaction the breaker setup expects. The mitigation event is what activates the breaker as a tradeable level — a breaker without retest is just a violated OB; a mitigation event with rejection-with-displacement turns it into a confirmed entry zone.

## Formal Criteria

For a bullish breaker (bull-side support after originally-bearish OB):

- Price retraces down into the breaker zone (the originally-bearish OB's body).
- Bullish reaction occurs (bullish wick rejection, FVG, or LTF MSS up).
- The mitigation is "successful" if displacement-up follows; if not, the breaker is failing ([failed-breaker](../08-breaker-blocks/failed-breaker.md)).

For a bearish breaker: symmetric.

## Formula / Math

```
breaker_mitigation(bb, retest_candle):
  if bullish_breaker:
    low(retest_candle) reaches into breaker_zone
    AND post-retest displacement is up
    AND optionally bullish_FVG forms
  if bearish_breaker:
    high(retest_candle) reaches into breaker_zone
    AND post-retest displacement is down
    AND optionally bearish_FVG forms
```

## Machine-Readable

```json
{
  "id": "mitigation-of-breaker",
  "category": "18-mitigation",
  "aliases": ["breaker-mitigation", "breaker-tested"],
  "criteria": [
    {"id": "c1", "expr": "price retests breaker zone"},
    {"id": "c2", "expr": "new-polarity rejection with displacement confirms"},
    {"id": "c3", "expr": "absent confirmation = failed breaker, not mitigation"}
  ],
  "timeframes": ["M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2023",
  "related": ["mitigation-definition","breaker-block","bullish-breaker","bearish-breaker","failed-breaker","mitigation-of-ob","mitigation-of-fvg"],
  "sources": ["ICT-2016-BREAKER-BLOCK","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish breaker mitigation:

   originally bearish OB (1.0945-1.0955)
     ↓ violated UPWARD with bullish CHoCH
   ─── breaker zone (now bullish support) ───
                                          ↓ retest from above
                                          ▼ touches into 1.0950
                                          ▲▲▲ bullish reaction + FVG up
                                          → mitigation successful
```

## Timeframes

M15+.

## Examples

**Example 1 — successful bullish breaker mitigation:**
- Bullish breaker zone 1.0945–1.0955.
- H1 retraces; wicks 1.0948, prints bullish hammer-style candle, leaves bullish FVG up.
- → mitigation successful. Long entry on FVG retest.

## Common Mistakes

- **No-rejection touch.** A wick into the zone without rejection isn't a complete mitigation; wait for displacement direction.
- **Treating failure as mitigation-pending.** Once a close-through with opposite displacement happens, abandon the trade — see [failed-breaker](../08-breaker-blocks/failed-breaker.md).

## Related Concepts

- [mitigation-definition](mitigation-definition.md), [breaker-block](../08-breaker-blocks/breaker-block.md), [bullish-breaker](../08-breaker-blocks/bullish-breaker.md), [bearish-breaker](../08-breaker-blocks/bearish-breaker.md), [failed-breaker](../08-breaker-blocks/failed-breaker.md), [mitigation-of-ob](mitigation-of-ob.md), [mitigation-of-fvg](mitigation-of-fvg.md).

## Citations

- `ICT-2016-BREAKER-BLOCK` (01:39–01:46) "there is going to be orders inside that high that will be looking to be mitigated"; (05:56) the retest entry taken "with the expectation that there is going to be a mitigation that is taking place".
- `ICT-2022-MENTORSHIP-OVERVIEW` — 2022 restatement.
