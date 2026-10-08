# Relative Equal Highs / Lows (REH / REL)

**Category:** 02-liquidity
**Aliases:** REH, REL
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-DOUBLE-TOP-BOTTOM, ICT-2016-LIQUIDITY-POOLS, ICT-2020-OTE-VOL09, ICT-2022-MENTORSHIP-EP05, ICT-2022-MENTORSHIP-EP16
**Tags:** liquidity, eqh, eql, relative, near-equal

## Definition

Relative Equal Highs (REH) and Relative Equal Lows (REL) are pairs of swing highs or swing lows that fall in close proximity to each other. ICT treats them as **the same thing as** [equal-highs](equal-highs.md) and [equal-lows](equal-lows.md), not a looser second tier — "relatively equal highs in here" (`ICT-2016-DOUBLE-TOP-BOTTOM`, 00:52); "these two highs here in close proximity to one another" (02:06); the retail reading and the stops it draws: "the retail universe is going to see this as double top… let's get short and put a protective buy stop above these highs" (04:27–04:37); "then seeking the sell stops below these relative equal lows" (`ICT-2016-LIQUIDITY-POOLS`, 17:59); "it rallies all the way back above these relative equal highs, clearing that liquidity out" (`ICT-2020-OTE-VOL09`, 01:50).

⚠ **Dating corrected 2026-08-10.** Re-dated 2018 → 2016; see citations below.

## Formal Criteria

- Two or more swing highs (REH) or swing lows (REL) print in **close proximity** to each other.
- An intervening opposite pivot must exist between them — **library convention, not stated by ICT**; "intervening" is 0/0 in both corpora, though trivially true of two distinct pivots.
- ICT applies "relative equal" to pairs **including exact-tick matches**, not only loose ones — he calls an identical high "relative equal high": "it's 45145, this candle trades to 4514A5, exactly the same high… but look closer, we have relative equal high" (`ICT-2022-MENTORSHIP-EP05`, 15:31). And he states the terms are interchangeable regardless of exactness: "relatively equal, not exactly — that's why I named them relatively equal lows" (`ICT-2022-MENTORSHIP-EP16`, 04:13).
- There is **no strict-equal-vs-relative-equal split** in ICT's usage. "Equal highs" (`equal-highs`) and "relative equal highs" (this page) name the same phenomenon; keep both pages but do not treat one as the `ε == 0` special case of the other.

## Formula / Math

ICT gives **no pip/tick tolerance** for REH/REL in either corpus (0 hits for "tolerance," "few pips," "pip tolerance" in a REH/REL context across 153 2016-17/2020-21 packets and 41 2022 episodes). The only numbers found near "equal highs" are price levels themselves or the *reach beyond* a level once taken (10–20 pips typical, see [liquidity-sweep](liquidity-sweep.md)) — never a tolerance *between* the two highs/lows.

```
REH(SH_1, SH_2) := H(SH_1) "in close proximity to" H(SH_2)   [ICT gives no number for this]
                   AND exists(SL between SH_1 and SH_2)

REL(SL_1, SL_2) := L(SL_1) "in close proximity to" L(SL_2)   [ICT gives no number for this]
                   AND exists(SH between SL_1 and SL_2)
```

The library's prior formula `0 < |Δ| <= ε` (excluding the exact-match case) is **contradicted**: ICT labels an exact-tick match "relative equal high" (EP05, 15:31). Do not exclude `|Δ| == 0`. Any specific pip/point/cent tolerance table (e.g. "1–4 pips M15–H4, 5–15 pips D/W") is the library's own convention, not ICT's — present it only if clearly labelled as unverified.

## Machine-Readable

```json
{
  "id": "relative-equal-highs-lows",
  "category": "02-liquidity",
  "aliases": ["REH", "REL"],
  "criteria": [
    {"id": "c1", "expr": "level_1 close_in_proximity_to level_2 — ICT gives no numeric tolerance, and does not exclude an exact match"},
    {"id": "c2", "expr": "intervening_opposite_pivot_exists == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["equal-highs","equal-lows","buy-side-liquidity","sell-side-liquidity","liquidity-sweep","liquidity-pool"],
  "sources": ["ICT-2016-DOUBLE-TOP-BOTTOM","ICT-2016-LIQUIDITY-POOLS","ICT-2020-OTE-VOL09","ICT-2022-MENTORSHIP-EP05","ICT-2022-MENTORSHIP-EP16"]
}
```

## Visual Pattern

```
   REH (close proximity)                 REL (close proximity)

         x   x'                              \  intervening
        /\  /\                                \  swing high
   ────/──\/──\────  REH                       \   /\
                                                \ /  \
                                          ───────y────y'──── REL
   x and x' "in close proximity"           y and y' "in close proximity"
   (an exact match also counts)            (an exact match also counts)
```

## Timeframes

All TFs.

## Examples

**Example 1 — H1 REH on EURUSD:**
- Two H1 swing highs, four hours apart, at 1.0875 and 1.0878, with a pullback to 1.0840 between them — in close proximity by ICT's own (non-numeric) standard.
- The 1.0878 area is a valid sweep target; retail will treat 1.0875–1.0878 as "the same high."

**Example 2 — D1 REL on indices:**
- Daily lows at 5210.5 and 5212.0 separated by a one-week rally to 5285 — again, close proximity, no ICT-given numeric bound.
- 5210–5212 is the pool.

## Common Mistakes

- **Inventing a pip/tick tolerance table.** ICT gives none; "close proximity" is judgment, not a formula.
- **Treating REH/REL as the loose counterpart to a "strict" EQH/EQL.** ICT uses the terms interchangeably, including for exact matches.
- **Ignoring the pivot rule.** Two near-equal highs on consecutive bars without a swing low between them are not REH; they're a flat top in a single uptrend.

## Related Concepts

- [equal-highs](equal-highs.md) / [equal-lows](equal-lows.md) — the same phenomenon, not a stricter special case.
- [buy-side-liquidity](buy-side-liquidity.md) / [sell-side-liquidity](sell-side-liquidity.md) — what REH/REL pools represent.
- [liquidity-sweep](liquidity-sweep.md) — sweep behavior at REH/REL.
- [liquidity-pool](liquidity-pool.md) — the broader category.

## Citations

- `ICT-2016-DOUBLE-TOP-BOTTOM` (00:52) "relatively equal highs in here"; (02:06) "these two highs here in close proximity to one another"; (04:27–04:37) retail's double-top reading and the buy stop it parks above the highs; (12:12) the algorithmic run through those stops.
- `ICT-2016-LIQUIDITY-POOLS` (17:59) "seeking the sell stops below these relative equal lows."
- `ICT-2020-OTE-VOL09` (01:50) "it rallies all the way back above these relative equal highs, clearing that liquidity out."
- `ICT-2022-MENTORSHIP-EP05` (15:31) "it's 45145… exactly the same high… but look closer, we have relative equal high."
- `ICT-2022-MENTORSHIP-EP16` (04:13) "relatively equal, not exactly — that's why I named them relatively equal lows."
