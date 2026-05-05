# SMT Failure

**Category:** 16-smt-divergence
**Aliases:** failed SMT, SMT invalidated, SMT continuation
**ICT Confidence:** high
**Year Introduced:** 2018
**Year Refined:** 2022
**Source IDs:** ICT-2017-CHARTER-OVERVIEW, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** smt, failure, risk

## Definition

An SMT failure is when both correlated assets **eventually confirm the new extreme** — the divergence is closed, and the SMT signal that suggested reversal becomes invalidated. ICT teaches SMT-failure recognition as essential risk management: when SMT-confirmed setups are entered and the second asset later catches up to the first asset's new extreme, the original divergence is gone and the trade premise is invalid.

## Formal Criteria

For a previously-bullish SMT setup that fails:

- Asset A made a new low (typical).
- Asset B did NOT confirm initially (higher low — bullish SMT).
- LATER, Asset B closes through its prior low — the divergence is gone.
- The bullish SMT signal is invalidated; reversal hypothesis is failing.

For bearish SMT failure: symmetric (Asset B catches up to new high).

## Formula / Math

```
smt_failure(asset_A, asset_B, original_divergence_direction):
    if bullish_smt was the signal:
        smt_failed := asset_B.subsequent_low < asset_A.previously_new_low_at_smt_time
    if bearish_smt was the signal:
        smt_failed := asset_B.subsequent_high > asset_A.previously_new_high_at_smt_time
```

## Machine-Readable

```json
{
  "id": "smt-failure",
  "category": "16-smt-divergence",
  "aliases": ["failed-SMT", "SMT-invalidated", "SMT-continuation"],
  "criteria": [
    {"id": "c1", "expr": "second asset eventually confirms new extreme"},
    {"id": "c2", "expr": "divergence closed; signal invalidated"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2018",
  "year_refined": "2022",
  "related": ["smt-divergence","correlated-pairs-smt","index-smt","smt-confirmation","htf-bias-framework"],
  "sources": ["ICT-2017-CHARTER-OVERVIEW","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   bullish SMT failure (B catches up):

   Time T:                              Time T+k:

   Asset A: new low                      Asset A: continues lower or holds
   Asset B: higher low (divergence)      Asset B: NOW prints new low — confirms
                                                        → SMT divergence closed
                                                        → bullish setup invalidated
```

## Timeframes

M5–D.

## Examples

**Example 1 — failed bullish SMT:**
- 09:00 NY: EURUSD new low 1.0840; GBPUSD higher low 1.2655 (bullish SMT).
- Trader long EURUSD on bullish FVG; SL 1.0835.
- 09:30 NY: GBPUSD prints 1.2640 (below its prior low); the divergence has closed.
- 09:45 NY: EURUSD continues down to 1.0832; SL hit.
- → SMT failed; HTF bias may be flipping bearish.

## Common Mistakes

- **Ignoring SMT failure on open trades.** When SMT closes (divergence gone), reassess the trade premise — don't blindly hold for SL.
- **Adding to losing SMT-confirmed trades.** SMT-failed setups have lost their primary confluence; don't pyramid against the failure.
- **Confusing slow SMT-close with continuation.** Some SMT divergences resolve slowly; differentiate between gradual confirmation and quick continuation by watching displacement quality.

## Related Concepts

- [smt-divergence](smt-divergence.md), [correlated-pairs-smt](correlated-pairs-smt.md), [index-smt](index-smt.md), [smt-confirmation](smt-confirmation.md), [htf-bias-framework](../25-htf-bias/htf-bias-framework.md).

## Citations

- `ICT-2017-CHARTER-OVERVIEW`, `ICT-2022-MENTORSHIP-OVERVIEW`.
