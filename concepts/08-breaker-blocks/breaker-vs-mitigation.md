# Breaker vs Mitigation Block — Disambiguation

**Category:** 08-breaker-blocks
**Aliases:** none (disambiguation page)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2016
**Source IDs:** ICT-2016-BREAKER-BLOCK, ICT-2016-MITIGATION-BLOCKS, ICT-2017-INSTITUTIONAL-SWING-POINTS, ICT-2017-HTF-PD-ARRAYS
**Tags:** breaker, mitigation, disambiguation, terminology

⚠ **Rewritten 2026-10-08.** The prior CHoCH-vs-BOS / flip-vs-no-flip axis is contradicted: both
constructions involve a market structure shift, and **both flip polarity**. ICT's actual axis is
which kind of **swing point** precedes the retest.

## Definition

Breaker blocks and mitigation blocks share the retest geometry — a structural reference, violated
earlier, returned to later — but they are built from the **two different swing-point types** ICT
names as the only two that exist: "there's really only two forms of swing points in the marketplace
as it relates to institutional trading. It's in the form of a **stop run** or a **failure swing**.
That's it. There's nothing else." (`ICT-2017-INSTITUTIONAL-SWING-POINTS` [01:37–01:51]).

**The axis:**
- **Breaker** = built on a **stop-run swing point**: an old high/low is run first, then the
  intervening swing is broken. "We view that initial drop down below the previous low as a potential
  false break or turtle soup long" (`ICT-2016-BREAKER-BLOCK` [00:42–00:56]).
- **Mitigation block** = built on a **failure-swing point**: the prior extreme is never reached; the
  "M pattern" forms instead. "That short term little swing low at the failure swing — that's going
  to be what? A potential mitigation block." (`ICT-2017-HTF-PD-ARRAYS` [07:46–07:51]).

**Both flip polarity and both involve a market structure shift.** The breaker's confirming break IS a
market structure shift ([01:24–01:36]); the mitigation block's M-pattern failure swing also carries
"a confirmation break in market structure" (`ICT-2016-MITIGATION-BLOCKS` [02:44–03:08]). Both then
reverse the candle's role: the breaker lecture itself calls the breaker "this form of mitigation"
(`ICT-2016-BREAKER-BLOCK` [00:26]), and the mitigation-block lecture states the flip outright:
"classic support broken turns resistance" (`ICT-2016-MITIGATION-BLOCKS` [08:57]).

**Not a reversal-vs-continuation split either.** ICT's mitigation block is itself the first array met
after a reversal — "small little bounces in bear markets would be a mitigation block, basically"
(`ICT-2017-HTF-PD-ARRAYS` [21:03]) — and the two are grouped, differing mainly in depth: "mitigation
and breakers are basically mitigation blocks, but generally mitigation blocks can occur lower than
breakers." [20:55–20:58]; "a bearish breaker will keep your ability to get to a bearish order block,
which will be resting higher up in the premium." [21:07].

## Formal Criteria

### Breaker

- Built on a **stop-run** swing point: old high/low run first, then the intervening swing broken.
- Polarity **flips**.
- Zone = the **entire candle** (full range) at the intervening swing.
- See [breaker-block](breaker-block.md).

### Mitigation Block

- Built on a **failure-swing** point: the prior extreme is never reached; an "M"/"W" pattern forms,
  confirmed by its own market structure shift.
- Polarity **also flips** — "classic support broken turns resistance."
- Zone = the **body** of the last DOWN-close candle at the failure-swing low (bearish case; mirror
  for bullish); hallmark is that the **body is not violated** on the return.
- See [mitigation-block](mitigation-block.md).

### The relationship

```
Both: a swing point, broken or failed, forms a reference candle that LATER flips its role.
Breaker:    antecedent = STOP RUN (liquidity taken, then the swing broken)
Mitigation: antecedent = FAILURE SWING (the extreme never reached; "M"/"W" forms instead)
Both involve a market structure shift and BOTH flip polarity. Mitigation blocks generally
sit lower (closer to the current price) than breakers in the array stack.
```

## Formula / Math

```
classify(swing_point):
    if swing_point.type == "stop_run":        # old high/low run, then intervening swing broken
        return "breaker"           # zone = entire candle range; polarity flips
    elif swing_point.type == "failure_swing":  # extreme never reached; M/W pattern + MSS
        return "mitigation_block"  # zone = candle BODY; polarity flips; hallmark = body unviolated
    # there is no third type — ICT: "there's really only two forms of swing points"
```

## Machine-Readable

```json
{
  "id": "breaker-vs-mitigation",
  "category": "08-breaker-blocks",
  "aliases": [],
  "criteria": [
    {"id": "c1", "expr": "breaker := built on a STOP-RUN swing point (old high/low run, then intervening swing broken); zone = entire candle range"},
    {"id": "c2", "expr": "mitigation_block := built on a FAILURE-SWING point (extreme never reached, M/W pattern); zone = candle body"},
    {"id": "c3", "expr": "BOTH flip polarity; BOTH involve a market structure shift"},
    {"id": "c4", "expr": "mitigation blocks generally sit lower (nearer current price) in the array stack than breakers"}
  ],
  "timeframes": ["M15","H1","H4","D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2016",
  "related": ["breaker-block","bullish-breaker","bearish-breaker","mitigation-block","bullish-order-block","bearish-order-block"],
  "sources": ["ICT-2016-BREAKER-BLOCK","ICT-2016-MITIGATION-BLOCKS","ICT-2017-INSTITUTIONAL-SWING-POINTS","ICT-2017-HTF-PD-ARRAYS"]
}
```

## Visual Pattern

```
   Breaker (stop-run swing point):            Mitigation block (failure-swing point):

   old low RUN first                           prior high never retested ("M")
        ╲                                           ╱╲
         ╲→ swing high BROKEN                      ╱  ╲___ ← failure swing + MSS down
           (structure break confirms the run)     ╱       ▼  ← last DOWN-colour candle's BODY
           candle's ENTIRE RANGE = breaker zone  ╱        ╲     (NOT up-colour)
                                                             ╲→ body holds on retest (hallmark)

   Both: retest later -> polarity FLIPS (the candle's role reverses either way).
```

## Timeframes

No floor stated for either — see [breaker-block](breaker-block.md) and [mitigation-block](mitigation-block.md).

## Examples

**Example A — breaker:**
- An old low is run (stop-run swing point).
- Price breaks back up through the intervening swing high — structure break confirms the run.
- The candle at that swing high (entire range) = bullish breaker; retest from above holds as support.

**Example B — mitigation block:**
- Price fails to retest a prior high; an "M pattern" failure swing posts a market structure shift
  down.
- The last DOWN-close candle inside the low framed by that failure swing = mitigation candle (body
  only); retest later holds (body not violated) as resistance.

## Common Mistakes

- **CHoCH-vs-BOS as the axis.** `CHoCH`/`BOS` are SMC-community terms — 0 hits in either corpus, and
  not ICT's distinction regardless; both constructions involve a market structure shift, and the
  real axis is stop-run vs failure-swing point.
- **"Mitigation block doesn't flip polarity."** It does — "classic support broken turns resistance"
  (`ICT-2016-MITIGATION-BLOCKS` [08:57]).
- **Treating them as reversal-vs-continuation references.** The mitigation block IS itself a
  reversal-adjacent array, sitting closer to price than the breaker — not a continuation tool.
- **Trading retest without checking which type.** Both are traded in the **post-shift direction** —
  there is no "trade the original direction" case for either.

## Related Concepts

- [breaker-block](breaker-block.md), [bullish-breaker](bullish-breaker.md), [bearish-breaker](bearish-breaker.md), [mitigation-block](mitigation-block.md).
- [bullish-order-block](../07-order-blocks/bullish-order-block.md), [bearish-order-block](../07-order-blocks/bearish-order-block.md).

## Citations

- `ICT-2016-BREAKER-BLOCK` [00:26] "this form of mitigation"; [00:42–00:56] stop-run antecedent; [01:24–01:36] structure break.
- `ICT-2016-MITIGATION-BLOCKS` [00:28] "an implication of order block theory"; [02:44–03:08] M-pattern failure swing with a confirmation break in market structure; [08:57] "classic support broken turns resistance."
- `ICT-2017-INSTITUTIONAL-SWING-POINTS` [01:37–01:51] "there's really only two forms of swing points … a stop run or a failure swing."
- `ICT-2017-HTF-PD-ARRAYS` [07:46–07:51] failure-swing lineage of the mitigation block; [20:55–21:07] mitigation blocks and breakers grouped, mitigation generally lower/nearer price.
