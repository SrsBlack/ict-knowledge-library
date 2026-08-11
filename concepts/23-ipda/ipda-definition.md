# IPDA — Definition

**Category:** 23-ipda
**Aliases:** Interbank Price Delivery Algorithm, the algorithm, the algo
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2025
**Source IDs:** ICT-2016-ELEMENTS-OF-A-TRADE-SETUP, ICT-2017-IPDA-DATA-RANGES, ICT-2017-QUARTERLY-SHIFTS, ICT-2022-MENTORSHIP-OVERVIEW, ICT-2025-ADV-LIQUIDITY

⚠ **Re-dated 2017 → 2016 on 2026-08-10, splitting the algorithm from its measurement windows.**
Two concurrent passes disagreed: one dated this page to the Jan-2017 IPDA lectures, the other
located the algorithm's definition a year earlier. The earlier evidence wins — ICT defines IPDA in
**Sep 2016**: "the **interbank price delivery algorithm** … is the actual, basically artificial
intelligence. **It's a price engine** … 90 % done by electronic algorithms"
(`ICT-2016-ELEMENTS-OF-A-TRADE-SETUP` [04:44–05:12]). The **20/40/60-day data ranges** remain
**2017** — see [ipda-data-ranges](ipda-data-ranges.md). The algorithm and its measurement windows
are taught a year apart and should not share one date.
**Tags:** ipda, algorithm, foundational

## Definition

IPDA — the **Interbank Price Delivery Algorithm** — is ICT's name for the institutional algorithm he claims governs price delivery in major markets. It is the conceptual backbone of the entire ICT framework: every concept (PD arrays, killzones, macro times, liquidity sweeps, Quarterly Theory) is taught as a pattern produced by IPDA's behavior. ICT teaches that price is not random but algorithmically delivered, and that the analyst's job is to read IPDA's intent. IPDA references **20 / 40 / 60-day lookback windows** to identify levels of interest, and (per 2024–2025 refinements) rotates its delivery focus between External Range Liquidity and Internal Range Liquidity on a ~quarterly cadence.

## Formal Criteria

ICT's claims about IPDA:

- Operates in major liquid markets (FX, indices, metals).
- Uses 20 / 40 / 60 trading-day lookback ranges to identify reference highs/lows ([ipda-data-ranges](ipda-data-ranges.md)).
- Delivers price toward liquidity pools (BSL/SSL) using PD arrays as decision points.
- Rotates between ERL- and IRL-targeting on ~3-4 month cycles (2024–2025 refinement, see [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md)).
- Operates within session structure: accumulation in Asia, manipulation at session opens, distribution in NY AM.

The concept is **interpretive**: IPDA is not a publicly documented institutional protocol. ICT's framework treats it as an **explanatory model** for observed price patterns. Confidence is `high` for the *pattern recognition value* of IPDA-as-mental-model; confidence is lower for any literal claim about "the actual algorithm."

## Formula / Math

IPDA's behavior is described qualitatively rather than algorithmically. Operationally, the analyst tracks:

```
IPDA_lookback_levels = {
  "20_day_high":  highest high over last 20 trading days,
  "20_day_low":   lowest low over last 20 trading days,
  "40_day_high":  highest high over last 40 trading days,
  "40_day_low":   lowest low over last 40 trading days,
  "60_day_high":  highest high over last 60 trading days,
  "60_day_low":   lowest low over last 60 trading days
}

IPDA references these to identify untaken liquidity at ERL and IRL.
```

## Machine-Readable

```json
{
  "id": "ipda-definition",
  "category": "23-ipda",
  "aliases": ["Interbank-Price-Delivery-Algorithm", "the-algorithm"],
  "criteria": [
    {"id": "c1", "expr": "uses_20_40_60_day_lookbacks == true"},
    {"id": "c2", "expr": "delivers_price_to_liquidity_via_PD_arrays == true"},
    {"id": "c3", "expr": "rotates_ERL_IRL_targeting_quarterly == true"}
  ],
  "timeframes": ["D","W","MN"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2025",
  "related": ["ipda-data-ranges","ipda-20-day-lookback","ipda-40-day-lookback","ipda-60-day-lookback","ipda-reference-points","quarterly-shift-theory","internal-range-liquidity","external-range-liquidity","draw-on-liquidity","algorithmic-price-delivery"],
  "sources": ["ICT-2016-ELEMENTS-OF-A-TRADE-SETUP","ICT-2017-IPDA-DATA-RANGES","ICT-2017-QUARTERLY-SHIFTS","ICT-2022-MENTORSHIP-OVERVIEW","ICT-2025-ADV-LIQUIDITY"]
}
```

## Visual Pattern

```
   IPDA conceptual model:

   ─── 60-day high ──── (ERL: long-horizon BSL)
   ─── 40-day high ──── (medium-horizon BSL)
   ─── 20-day high ──── (short-horizon BSL)
                ↑
                IPDA references these as upside DOL targets.
   ── current price ──
                ↓
                IPDA references these as downside DOL targets.
   ─── 20-day low ──── (short-horizon SSL)
   ─── 40-day low ──── (medium-horizon SSL)
   ─── 60-day low ──── (ERL: long-horizon SSL)
```

## Timeframes

D / W / MN are the natural TFs for IPDA-level reference. Lookback ranges are measured in trading-day units.

## Examples

**Example 1 — IPDA as explanatory model:**
- EURUSD has been ranging between 1.0750 and 1.1100 for 8 weeks (2 months).
- 60-day high = 1.1100; 40-day high = 1.1080; 20-day high = 1.0950.
- The next algorithmic delivery target is the unswept 20-day high (1.0950) for medium-bias-bullish — once that's taken, the 40-day and 60-day highs become the next ERL targets.
- ICT framing: "IPDA is delivering price toward 20-day liquidity, with 40-day and 60-day as further-out destinations."

## Common Mistakes

- **Treating IPDA as a literal published algorithm.** It is not. It is ICT's mental model. Treat it as a useful framework for pattern recognition, not as ground truth about what institutional code is doing.
- **Ignoring the lookback windows.** ICT teaches 20/40/60 specifically; using random lookbacks (10, 50, 100) doesn't replicate the framework.
- **Static IPDA mode.** ICT's 2024–2025 work emphasizes that IPDA's *targeting mode* (ERL vs IRL) rotates quarterly. Don't assume what worked last quarter still works.

## Related Concepts

- [ipda-data-ranges](ipda-data-ranges.md), [ipda-20-day-lookback](ipda-20-day-lookback.md), [ipda-40-day-lookback](ipda-40-day-lookback.md), [ipda-60-day-lookback](ipda-60-day-lookback.md), [ipda-reference-points](ipda-reference-points.md).
- [quarterly-shift-theory](../04-time-cycles/quarterly-shift-theory.md) — IPDA quarterly rotation.
- [internal-range-liquidity](../02-liquidity/internal-range-liquidity.md), [external-range-liquidity](../02-liquidity/external-range-liquidity.md), [draw-on-liquidity](../02-liquidity/draw-on-liquidity.md).
- [algorithmic-price-delivery](../03-order-flow/algorithmic-price-delivery.md) — broader framing.

## Citations

- `ICT-2016-ELEMENTS-OF-A-TRADE-SETUP` (04:44–05:12) the earliest located definition of the algorithm itself — "it's a price engine… 90 % done by electronic algorithms".

- `ICT-2017-IPDA-DATA-RANGES` (81:03) — "It's January 12, 2017"; (21:38–21:46) "IPTA is the Interbank Price Delivery Algorithm"; (27:52–28:27) "if you look back 60 days in the past, what was the highest high in the last 60 days? There's going to be buy stops above that high… Inside of the range of 20 days, 40 days, and 60 days."
- `ICT-2017-QUARTERLY-SHIFTS` (00:21) — "the January 2017 ICT Mentorship Long Term Analysis Lesson 1.1"; (22:22–23:41) "60 trading days, 40 trading days, and 20 trading days… and they're all trading days, not calendar days."
- `ICT-2022-MENTORSHIP-OVERVIEW` — operational use refined.
- `ICT-2025-ADV-LIQUIDITY` — quarterly rotation refinement.
