# Equal Highs (EQH)

**Category:** 02-liquidity
**Aliases:** EQH, double top liquidity, relative equal highs (REH)
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-WHAT-TO-FOCUS-ON, ICT-2016-EQUILIBRIUM-DISCOUNT, ICT-2016-DOUBLE-TOP-BOTTOM, ICT-2022-MENTORSHIP-EP02, ICT-2022-MENTORSHIP-EP03, ICT-2022-MENTORSHIP-EP05, ICT-2022-MENTORSHIP-EP16
**Tags:** liquidity, eqh, buyside, foundational

## Definition

Equal highs are two or more swing highs at (approximately) the same price level — the most concentrated form of [buy-side-liquidity](buy-side-liquidity.md). ICT considers EQH a high-probability sweep target because retail reads it as a double top and places stops accordingly: "the retail universe is going to see this as double top. Therefore, there's resistance. Let's get short and put a protective buy stop above these highs" (`ICT-2016-DOUBLE-TOP-BOTTOM`, 04:27–04:37); "retail traders see this and they trust it as… resistance, so the books always say put your buy stop" (`ICT-2022-MENTORSHIP-EP02`, 24:14); "relative equal highs above that is buy stops" (`ICT-2022-MENTORSHIP-EP03`, 01:17).

## Formal Criteria

- Two or more swing highs (STH or higher) print in **close proximity** to each other — ICT's own qualifier, not a numeric tolerance: "two equal highs that formed in close proximity to one another" (`ICT-2016-WHAT-TO-FOCUS-ON`, 15:27); "areas where it's too clean, equal highs and equal lows in close proximity to one another" (`ICT-2016-WHAT-TO-FOCUS-ON`, 18:31); "they're too clean, the market's going to want to run there" (`ICT-2016-EQUILIBRIUM-DISCOUNT`, 51:27–51:29).
- ICT does **not** give a pip/tick tolerance for how close is close enough — see Formula / Math.
- ICT uses "equal highs" and "relative equal highs" **interchangeably**, not as a strict-vs-loose dichotomy: he labels an exact-tick match "relative equal high" — "it's 45145, this candle trades to 4514A5, exactly the same high… but look closer, we have relative equal high" (`ICT-2022-MENTORSHIP-EP05`, 15:31). See [relative-equal-highs-lows](relative-equal-highs-lows.md).

## Formula / Math

ICT gives **no numeric tolerance** for equal highs in either corpus (0 hits for "tolerance" across 153 2016-17/2020-21 packets and 41 2022 episodes). His qualifiers are verbal: "close proximity," "too clean." Any pip/tick figure (e.g. "2 pips on EURUSD H1") is the library's own convention, not ICT's — do not present it as sourced.

```
equal_highs(SH_1, SH_2) := H(SH_1) "in close proximity to" H(SH_2)   [no ICT-given numeric bound]
```

The library's prior "strict EQH when ε==0, REH when ε>0" dichotomy is **contradicted**: ICT calls an exact match "relative equal high" (EP05, 15:31) and says plainly "relatively equal, not exactly — that's why I named them relatively equal lows" (`ICT-2022-MENTORSHIP-EP16`, 04:13). Equal and relative-equal are the same thing in ICT's usage.

## Machine-Readable

```json
{
  "id": "equal-highs",
  "category": "02-liquidity",
  "aliases": ["EQH", "double-top-liquidity", "REH"],
  "criteria": [
    {"id": "c1", "expr": "H(SH_1) close_in_proximity_to H(SH_2) — ICT gives no numeric tolerance"},
    {"id": "c2", "expr": "equal and relative-equal are used interchangeably by ICT, not a strict/loose dichotomy"}
  ],
  "timeframes": ["M1","M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["equal-lows","buy-side-liquidity","relative-equal-highs-lows","liquidity-sweep","liquidity-pool","swing-high"],
  "sources": ["ICT-2016-WHAT-TO-FOCUS-ON","ICT-2016-EQUILIBRIUM-DISCOUNT","ICT-2016-DOUBLE-TOP-BOTTOM","ICT-2022-MENTORSHIP-EP02","ICT-2022-MENTORSHIP-EP03","ICT-2022-MENTORSHIP-EP05","ICT-2022-MENTORSHIP-EP16"]
}
```

## Visual Pattern

```
        SH_1            SH_2          ← equal / relative-equal highs
   ──────┬──────────────┬─────────  EQH liquidity pool
        /\              /\
       /  \            /  \
      /    \          /    \
                \    /
                 \  /
                  \/             ← intervening swing low
```

Two same-priced (or close-in-proximity) peaks separated by a valley = EQH.

## Timeframes

Every TF. EQH on D / H4 are major liquidity targets; EQH on M5 are common intra-session sweep setups.

## Examples

**Example 1 — H1 EQH on EURUSD:**
- H1 prints highs at 1.0875 and 1.0876 four hours apart, with a clear pullback to 1.0840 between them — in ICT's terms, in close proximity.
- The 1.0876 area becomes a high-probability BSL sweep target; expect price to wick above before a possible reversal.

## Common Mistakes

- **Inventing a numeric tolerance.** ICT gives none; "close proximity" is a judgment call, not a pip formula.
- **Treating "equal" and "relative equal" as different strictness levels.** ICT uses them interchangeably, including for exact-tick matches.
- **No intervening pivot.** Two consecutive bars at the same high in a single uptrend are not EQH — they're a small consolidation. EQH require a pullback between them.
- **Treating sweep as guaranteed reversal.** EQH being swept is high-probability for *some* reaction; whether that reaction is a full reversal depends on PD-array confluence, session, and HTF bias.

## Related Concepts

- [equal-lows](equal-lows.md) — mirror.
- [buy-side-liquidity](buy-side-liquidity.md) — what EQH represents.
- [relative-equal-highs-lows](relative-equal-highs-lows.md) — same concept, not a separate strictness tier.
- [liquidity-sweep](liquidity-sweep.md) — sweep behavior at EQH.
- [liquidity-pool](liquidity-pool.md) — EQH is the densest pool form.
- [swing-high](../01-market-structure/swing-high.md) — building block.

## Citations

- `ICT-2016-WHAT-TO-FOCUS-ON` (15:27) "two equal highs that formed in close proximity to one another"; (18:31) "areas where it's too clean, equal highs and equal lows in close proximity to one another."
- `ICT-2016-EQUILIBRIUM-DISCOUNT` (51:20–51:21) "there's your stop run on equal highs"; (51:27–51:29) "they're too clean, the market's going to want to run there."
- `ICT-2016-DOUBLE-TOP-BOTTOM` (04:27–04:37) "the retail universe is going to see this as double top… put a protective buy stop above these highs."
- `ICT-2022-MENTORSHIP-EP02` (24:14) "retail traders see this and they trust it as… resistance, so the books always say put your buy stop."
- `ICT-2022-MENTORSHIP-EP03` (01:17) "relative equal highs above that is buy stops."
- `ICT-2022-MENTORSHIP-EP05` (15:31) "it's 45145… exactly the same high… but look closer, we have relative equal high."
- `ICT-2022-MENTORSHIP-EP16` (04:13) "they're relatively equal, not exactly — that's why I named them relatively equal lows."
