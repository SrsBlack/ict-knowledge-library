# Relative Equal Highs / Lows (REH / REL)

**Category:** 02-liquidity
**Aliases:** REH, REL, near-equal highs, near-equal lows, approximate twin levels
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-DOUBLE-TOP-BOTTOM, ICT-2016-LIQUIDITY-POOLS, ICT-2020-OTE-VOL09
**Tags:** liquidity, eqh, eql, relative, near-equal

## Definition

Relative Equal Highs (REH) and Relative Equal Lows (REL) are pairs of swing highs or swing lows that fall within a small price tolerance but are not strictly equal. ICT treats them as functionally equivalent to [equal-highs](equal-highs.md) and [equal-lows](equal-lows.md) for liquidity-pool purposes — retail traders perceive them as "double tops/bottoms" and place stops accordingly, even though the levels differ by a few pips. The REH/REL terminology is the practical name; pure equality is rare on real charts.

⚠ **Dating corrected 2026-08-10.** This page previously carried `Year Introduced: 2018` sourced
only to the placeholder IDs `ICT-2017-CHARTER-OVERVIEW` and `ICT-2022-MENTORSHIP-OVERVIEW`, neither
of which is a lecture. The **Month 04** lecture *Double Bottom Double Top* (Dec 2016) teaches the
concept in full and opens on the near-equal case: "we have a drop down in price with **relatively
equal highs** in here" [00:52], with "these two highs here **in close proximity to one another**"
[02:06] and the retail reading spelled out — "the retail universe is going to see this as double
top ... let's get short and put a protective buy stop above these highs" [04:27]. The **Month 04**
lecture *Liquidity Pools* uses the page's exact term: "then seeking the sell stops below these
**relative equal lows**" [17:59]. Re-dated to 2016.

## Formal Criteria

For REH:

- Two or more swing highs within tolerance ε > 0 of each other.
- An intervening swing low must exist between them.
- Tolerance is TF- and instrument-specific:
  - FX majors on M15–H4: 1–4 pips.
  - FX majors on D/W: 5–15 pips.
  - Indices intra-day: a few points.
  - Metals: a few cents to a dollar.

REL is symmetric with swing lows.

## Formula / Math

```
REH(SH_1, SH_2) := 0 < |H(SH_1) - H(SH_2)| <= ε
                   AND exists(SL between SH_1 and SH_2)

REL(SL_1, SL_2) := 0 < |L(SL_1) - L(SL_2)| <= ε
                   AND exists(SH between SL_1 and SL_2)

# Strict EQH / EQL is the special case where |Δ| == 0.
```

## Machine-Readable

```json
{
  "id": "relative-equal-highs-lows",
  "category": "02-liquidity",
  "aliases": ["REH", "REL", "near-equal-highs", "near-equal-lows"],
  "criteria": [
    {"id": "c1", "expr": "0 < abs(level_1 - level_2) <= tolerance"},
    {"id": "c2", "expr": "intervening_opposite_pivot_exists == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["equal-highs","equal-lows","buy-side-liquidity","sell-side-liquidity","liquidity-sweep","liquidity-pool"],
  "sources": ["ICT-2016-DOUBLE-TOP-BOTTOM","ICT-2016-LIQUIDITY-POOLS","ICT-2020-OTE-VOL09"]
}
```

## Visual Pattern

```
   REH (within ε)                       REL (within ε)

         x   x'                              \  intervening
        /\  /\                                \  swing high
   ────/──\/──\────  REH                       \   /\
                                                \ /  \
                                          ───────y────y'──── REL
   x and x' differ by < ε                  y and y' differ by < ε
```

## Timeframes

All TFs.

## Examples

**Example 1 — H1 REH on EURUSD:**
- Two H1 swing highs, four hours apart, at 1.0875 and 1.0878. Pullback to 1.0840 between them.
- Tolerance 4 pips → REH. The 1.0878 area is a valid sweep target; retail will treat 1.0875–1.0878 as "the same high."

**Example 2 — D1 REL on indices:**
- Daily lows at 5210.5 and 5212.0 separated by a one-week rally to 5285.
- Tolerance 5 points (intraday-scale large index) → REL. 5210–5212 is the pool.

## Common Mistakes

- **Single tolerance for all instruments.** A 4-pip tolerance that works for EURUSD H1 is way too tight for XAUUSD or GBPJPY; calibrate.
- **Ignoring the pivot rule.** Two near-equal highs on consecutive bars without a swing low between them are not REH; they're just a flat top in a single uptrend.
- **Demanding exact equality.** Strict EQH is rare; insisting on it misses obvious REH that retail will treat as the same level.

## Related Concepts

- [equal-highs](equal-highs.md) / [equal-lows](equal-lows.md) — strict equality (special case).
- [buy-side-liquidity](buy-side-liquidity.md) / [sell-side-liquidity](sell-side-liquidity.md) — what REH/REL pools represent.
- [liquidity-sweep](liquidity-sweep.md) — sweep behavior at REH/REL.
- [liquidity-pool](liquidity-pool.md) — the broader category.

## Citations

- `ICT-2016-DOUBLE-TOP-BOTTOM` — the concept taught end-to-end: "relatively equal highs" [00:52],
  "two highs here in close proximity to one another" [02:06], retail's double-top reading and the
  buy stops it parks above them [04:27], and the algorithmic run through those stops [12:12].
- `ICT-2016-LIQUIDITY-POOLS` — the page's exact term in ICT's own words: "seeking the sell stops
  below these relative equal lows" [17:59].
- `ICT-2020-OTE-VOL09` — "relative equal highs" as a standing phrase in the 2020 public era:
  "it rallies all the way back above these relative equal highs, clearing that liquidity out" [01:50].
