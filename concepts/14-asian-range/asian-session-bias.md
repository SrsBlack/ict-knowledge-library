# Asian Session Bias

**Category:** 14-asian-range
**Aliases:** Asia bias, AR bias, Asian session direction
**ICT Confidence:** medium
**Year Introduced:** 2017
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** asian-range, bias, direction

## Definition

Asian session bias is the directional read derived from how price behaved during the Asia session — most commonly: which side of the prior day's NY-session range did Asia trade in, and which side of the Asian range did the close-of-Asia gravitate toward. ICT teaches this as a **secondary bias input** that supplements (does not replace) HTF bias. Some operators use Asian bias to predict which range bound London will sweep first.

## Formal Criteria

Several heuristics ICT and the ICT community use:

- **Asian close inside top-half of Asian range:** weak-bullish; possible Judas-up before bullish continuation OR Judas-up before reversal.
- **Asian close inside bottom-half of range:** weak-bearish; mirror logic.
- **Asia trading above prior day's NY close:** mildly bullish into London.
- **Asia trading below prior day's NY close:** mildly bearish.
- **Asia gap from Friday close (Sunday open):** see [sunday-open-gap](../31-models/sunday-open-gap.md).

These are heuristics, not rules. Asian bias is **subordinate to HTF bias**.

## Formula / Math

```
asian_close              = close at end of Asia window (e.g., 03:00 NY)
asian_range_eq           = (asian_high + asian_low) / 2
prior_day_ny_close       = close at 17:00 NY of prior trading day

asian_bias_within_range :=
  "weak_bullish" if asian_close > asian_range_eq
  "weak_bearish" if asian_close < asian_range_eq
  "neutral"      otherwise

asian_bias_vs_prior_day :=
  "bullish_lean" if asian_close > prior_day_ny_close
  "bearish_lean" if asian_close < prior_day_ny_close
```

## Machine-Readable

```json
{
  "id": "asian-session-bias",
  "category": "14-asian-range",
  "aliases": ["asia-bias", "asian-direction"],
  "criteria": [
    {"id": "c1", "expr": "uses_asian_close_relative_to_range_eq_or_prior_day_close"}
  ],
  "timeframes": ["M15","H1","H4"],
  "confidence": "medium",
  "year_introduced": "2017",
  "year_refined": "2022",
  "related": ["asian-range","asian-range-high","asian-range-low","htf-bias-framework","sunday-open-gap","ndog"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   asian_high ──────────────
          ↑ "weak bullish": close in top half
          asian_eq
          ↓ "weak bearish": close in bottom half
   asian_low  ──────────────
```

## Timeframes

M15 / H1 — read at the end of Asia (~03:00 NY).

## Examples

**Example 1 — confirmation of bullish HTF:**
- HTF (D) bias bullish.
- Asian range 1.0848–1.0876; close at 03:00 NY = 1.0870 (top half).
- Prior day NY close = 1.0865.
- Asian close above prior NY close + in top half = mildly bullish lean.
- → confirms HTF bias; expect Asian-low Judas sweep then continuation up.

**Example 2 — Asian bias against HTF (warning sign):**
- HTF bullish but Asian close = 1.0852 (bottom half), below prior day close.
- Conflict — possible HTF reversal forming, or Asia is engineering a Judas-down before bullish continuation.
- Lower conviction; require additional confirmation (PD-array, killzone behavior).

## Common Mistakes

- **Trading Asian bias against HTF.** Asian bias is secondary; never override HTF bias with an intra-Asia read.
- **Treating heuristics as rules.** "Close in top half = bullish" is a tendency, not a guarantee. Confirm with London KZ behavior.
- **Wrong window.** Asian close at 03:00 NY (KZ end) vs 03:00 NY (full session end) can differ; specify which.

## Related Concepts

- [asian-range](asian-range.md), [asian-range-high](asian-range-high.md), [asian-range-low](asian-range-low.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md), [sunday-open-gap](../31-models/sunday-open-gap.md), [ndog](../31-models/ndog.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.

> Confidence is `medium` because Asian-bias heuristics are taught informally across the ICT community with several variants; ICT's own framing emphasizes HTF bias as primary.
