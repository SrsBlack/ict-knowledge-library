# SMT Confirmation

**Category:** 16-smt-divergence
**Aliases:** SMT-confirmed setup, divergence confirmation, SMT confluence
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2017-HIGH-REWARD-SETUPS, ICT-2016-USDX-SMT, ICT-2022-MENTORSHIP-OVERVIEW
**Tags:** smt, confirmation, confluence

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2018` sourced only to
the placeholder IDs `ICT-2017-CHARTER-OVERVIEW` and `ICT-2022-MENTORSHIP-OVERVIEW`. The **Month 02**
lecture *The Secrets To Selecting High Reward Setups* (`ICT-2017-HIGH-REWARD-SETUPS`, Oct 2016) already
makes SMT a *required confluence element* rather than a setup, at **[44:02]** — "you have to have your
dollar index giving you an indication that it's showing you a crack in correlation, or correlated pair
SMT is giving you insight" — one of three things that "must come by way of these three areas of study"
[43:48]. Re-dated to **2016**.

## Definition

SMT Confirmation is the use of SMT divergence as a **confluence signal added to an existing ICT setup**. ICT teaches SMT as the **single highest-quality confluence factor** for entries — when an SB / OTE / FVG setup also has SMT divergence, conviction increases substantially. SMT alone is not an entry; it is a confirmation that the algorithmic intent matches the bias direction at this specific structural level.

## Formal Criteria

A setup is **SMT-confirmed** when:

- A standard ICT setup is forming (SB / OTE / FVG / OB retest).
- At the structural level being entered, an SMT divergence exists between two correlated assets.
- The divergence direction agrees with the entry direction (bullish SMT for longs, bearish SMT for shorts).
- Both assets are at meaningful structural extremes (not random points).

## Formula / Math

```
setup_with_smt_confirmation := standard_ICT_setup
                                AND smt_divergence_at_entry_level
                                AND smt_direction_aligns_with_entry_direction
                                AND structural_extreme_for_both_assets

# Conviction modifier: typically +1 confluence factor in pd-array-confluence scoring
```

## Machine-Readable

```json
{
  "id": "smt-confirmation",
  "category": "16-smt-divergence",
  "aliases": ["SMT-confirmed-setup", "divergence-confirmation", "SMT-confluence"],
  "criteria": [
    {"id": "c1", "expr": "standard_setup_present == true"},
    {"id": "c2", "expr": "smt_divergence_aligned_with_entry_direction == true"},
    {"id": "c3", "expr": "structural_extreme_at_smt_event == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["smt-divergence","correlated-pairs-smt","index-smt","smt-failure","pd-array-confluence","silver-bullet-rules","ote-rules"],
  "sources": ["ICT-2017-HIGH-REWARD-SETUPS","ICT-2016-USDX-SMT","ICT-2022-MENTORSHIP-OVERVIEW"]
}
```

## Visual Pattern

```
   SMT-confirmed bullish SB:

   EURUSD (entry asset):                  GBPUSD (correlation asset):
                                          
   ─── known SSL ────────                 ─── known SSL ────────
       │                                      │
       ╲ ← wick (new low)                    ╲╱ ← wick (higher low — divergence)
        ╲╱                                       ▲ no new low
         ▲ ← bullish FVG                         ▲
   ─── displacement up                    ─── B does NOT confirm new low

   → bullish SMT confirms long bias on EURUSD.
```

## Timeframes

M5–D.

## Examples

**Example 1 — SMT-confirmed NY AM SB:**
- HTF bullish; setup forming on EURUSD at 10:05 NY.
- EURUSD wicks new session low; bullish FVG forms in displacement.
- Same M5: GBPUSD did NOT confirm the new low (made higher low).
- → SMT-confirmed bullish SB. Long EURUSD with extra conviction; SL at SMT-divergent low + buffer; targets via SD + DOL.

## Common Mistakes

- **SMT alone as entry trigger.** SMT is a confluence factor, not a standalone setup. Always pair with PD-array + bias.
- **Mismatched correlation.** Using EURUSD-USDJPY as SMT pair has weak/inverted correlation; signal is unreliable.
- **Ignoring structural context.** SMT at a random pair of bars is noise; require structural extremes.

## Related Concepts

- [smt-divergence](smt-divergence.md), [correlated-pairs-smt](correlated-pairs-smt.md), [index-smt](index-smt.md), [smt-failure](smt-failure.md), [pd-array-confluence](../05-pd-arrays/pd-array-confluence.md), [silver-bullet-rules](../11-silver-bullet/silver-bullet-rules.md), [ote-rules](../17-optimal-trade-entry/ote-rules.md).

## Citations

- `ICT-2017-HIGH-REWARD-SETUPS` (43:48) "three things must come by way of these three areas of study — correlation analysis, time and price theory, and the IPTA … preferably you have to have at least one from each"; (44:02) "you have to have your dollar index giving you an indication that it's showing you a crack in correlation, or correlated pair SMT is giving you insight." SMT is positioned as one confluence input among three, not a standalone trigger. ⚠ ID carries a `2017` token but the lecture is Month 02 = **October 2016** — see the registry note on [correlated-pairs-smt](correlated-pairs-smt.md).
- `ICT-2016-USDX-SMT` (02:47) "when the dollar index makes a lower low, foreign currencies we expect that to make a higher high; when we see this this confirms current price action" — the confirm / does-not-confirm framing this page rests on.
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational use in the 2022 re-teaching (basis for `Year Refined`).
