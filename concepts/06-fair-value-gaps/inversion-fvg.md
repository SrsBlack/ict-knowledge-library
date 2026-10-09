# Inversion FVG (IFVG)

**Category:** 06-fair-value-gaps
**Aliases:** IFVG, inverted FVG, flipped FVG, polarity-flip FVG
**ICT Confidence:** medium
**Year Introduced:** 2018
**Year Refined:** 2024
**Source IDs:** ICT-2018-IFVG, ICT-2024-IFVG-FORMALIZED, ICT-2022-MENTORSHIP-EP09, ICT-2022-MENTORSHIP-EP18, ICT-2022-MENTORSHIP-EP23
**Tags:** fvg, ifvg, inversion, polarity-flip, unverified

⚠ **UNVERIFIABLE per 2026-10-08 audit — read before using.** The term "inversion FVG" and every
stated rule (close-through-with-displacement, formal retest-with-displacement confirmation) have
**zero hits** in this library's local corpus. Searched both corpora (153 2016-17/2020-21 packets,
40 captioned 2022 Mentorship episodes) for `inversion|inverted|invert|inverse|polarity|flip|flipped|old gap|failed gap|gap fail`:
20 "inverted"/5 "inversion" hits in the raw corpus are all head-and-shoulders, yield-curve or
USDCAD-correlation usage, none FVG-related; 3 "inverted" hits in the 2022 corpus are a pyramid
metaphor (ep13) and dollar/euro correlation (ep20, ep21), again none FVG-related. Both cited
Source IDs (`ICT-2018-IFVG`, `ICT-2024-IFVG-FORMALIZED`) are one-line registry stubs with no
video behind them. This content is plausibly 2023+ ICT material outside this library's corpus —
kept here as an unverified placeholder, not as a confirmed definition. `ICT Confidence` is set to
`medium` and will move to `high` only once a real, dated source is located and quoted.

## Definition

An Inversion FVG is commonly described as a previously-formed FVG that price has traded through
and that then **flips polarity** — a bullish FVG that fails as support becomes resistance on
retest, and vice versa. **No definition, name, or rule for this exists in the 153-packet
2016-17/2020-21 corpus or the 40-captioned-episode 2022 Mentorship corpus searched here.** The closest
precursor located is a 2022 statement with no name attached, describing an FVG's low used as
resistance after price has fallen through it: "now i can revisit the bottom and under that fair
value gap and bump it kind of like a support resistance idea and that would be a shorting
opportunity if it were to do that" (`ICT-2022-MENTORSHIP-EP23` [03:09]). This is evidence that
the *idea* of a broken FVG acting as the opposite role existed informally in 2022 — it is not
evidence for the named, rule-bound "Inversion FVG" concept, its 2018 date, or its 2024
formalization.

## Formal Criteria

No criteria below are corpus-confirmed; they describe the commonly circulated (non-ICT-sourced,
in this library) IFVG rule for reference only, pending a located primary source:

- The original FVG (`L_{n+1} > H_{n-1}` bullish, or `H_{n+1} < L_{n-1}` bearish) was formed.
- A later candle trades through the original FVG's far edge.
- Price subsequently retests the original FVG zone from the opposite side.
- On retest, the zone is claimed to act with the opposite polarity.

One corpus data point cuts against the "close-through invalidates" framing commonly attached to
this rule: a 2022 example where price traded below an FVG's boundary and ICT states this did
**not** invalidate it, because he reads the FVG against the candle **body**, not the wick: "does
this invalidate the fair value Gap[?] no it does not[;] the idea is the fair value gap[]... we
look at the body of this candle here[,] isn't that respecting that" (`ICT-2022-MENTORSHIP-EP09`
[25:24]). This is a non-invalidation example, not an inversion rule, but it is the only corpus
statement on what does or doesn't break an FVG's relevance.

## Formula / Math

```
# No formula in the corpus. The following is the commonly circulated (non-ICT-sourced) convention,
# included for reference only — not verified against any located ICT statement:

inversion_break := price_t trades through H_{n-1}_orig   # for bull→bear inversion
                                                            # (UNVERIFIED; no close- or
                                                            # displacement-requirement stated)
ifvg_act_as_resistance := high_retest reaches L_{n+1}_orig AND price rejects down   # UNVERIFIED
```

## Machine-Readable

```json
{
  "id": "inversion-fvg",
  "category": "06-fair-value-gaps",
  "aliases": ["IFVG", "inverted-FVG", "flipped-FVG"],
  "criteria": [
    {"id": "c1", "expr": "UNVERIFIED: original_FVG_was_traded_through == true"},
    {"id": "c2", "expr": "UNVERIFIED: later_candle_trades_through_far_edge == true"},
    {"id": "c3", "expr": "UNVERIFIED: retest_acts_with_opposite_polarity == true"}
  ],
  "timeframes": ["M5","M15","H1","H4","D"],
  "confidence": "medium",
  "year_introduced": "2018",
  "year_refined": "2024",
  "related": ["fair-value-gap","bullish-fvg","bearish-fvg","fvg-mitigation","breaker-block","consequent-encroachment"],
  "sources": ["ICT-2018-IFVG","ICT-2024-IFVG-FORMALIZED","ICT-2022-MENTORSHIP-EP09","ICT-2022-MENTORSHIP-EP18","ICT-2022-MENTORSHIP-EP23"]
}
```

## Visual Pattern

```
   Commonly circulated bullish FVG -> bearish IFVG transformation (UNVERIFIED in this corpus):

   Step 1: Original bullish FVG forms
          ▲
          █  ← n+1
        ▲
        █  ← n
        █
       ▲
       █  ← n-1
   Step 2: Later, price trades below the FVG
   Step 3: Price retraces UP into the original FVG zone
          → claimed to act as RESISTANCE (bearish IFVG) — no corpus confirmation
```

## Timeframes

Not stated in the corpus. The commonly circulated convention applies it M5+.

## Examples

No corpus-sourced example exists. The following illustrates the commonly circulated convention
only, and should not be read as an ICT-cited case:

**Example 1 — bullish→bearish IFVG (illustrative, not corpus-sourced):**
- M15 bullish FVG forms at 1.0860–1.0865.
- Price later trades through 1.0860.
- Price retraces up into 1.0863 and rejects down.
- Commonly read as a confirmed bearish IFVG — this reading has no located ICT source.

## Common Mistakes

- **Citing this page as confirmed ICT doctrine.** It is UNVERIFIABLE in this library's corpus —
  see the warning above. Treat every rule here as provisional.
- **Calling every wick-through an inversion.** Even under the commonly circulated convention, a
  wick alone is not treated as decisive; and the one corpus statement on this question says a
  trade through an FVG's boundary did **not** invalidate it, judged by the body
  (`ICT-2022-MENTORSHIP-EP09` [25:24]).
- **Confusing IFVG with breaker.** ICT does separate an FVG from a breaker in 2022: "[m]any of you
  would see that as my bearish breaker[.] [M]hm, it's not, okay?... [is it] the discount low of
  the fair value gap? In other words, this candle's high" (`ICT-2022-MENTORSHIP-EP18` [01:53]–[02:29]).
  This confirms the two are treated as distinct objects, though it says nothing about inversion.

## Related Concepts

- [fair-value-gap](fair-value-gap.md), [bullish-fvg](bullish-fvg.md), [bearish-fvg](bearish-fvg.md).
- [fvg-mitigation](fvg-mitigation.md), [consequent-encroachment](consequent-encroachment.md).
- [breaker-block](../08-breaker-blocks/breaker-block.md) — analogous polarity-flip on swings;
  distinct from FVG per `ICT-2022-MENTORSHIP-EP18` above.

## Citations

- `ICT-2018-IFVG` — registry stub, no video, no quotation behind it. Retained only as the
  claimed-origin pointer; not corpus-evidenced.
- `ICT-2024-IFVG-FORMALIZED` — registry stub, no video, no quotation behind it. Same caveat.
- `ICT-2022-MENTORSHIP-EP09` — non-invalidation example, body-based reading [25:24].
- `ICT-2022-MENTORSHIP-EP18` — FVG-vs-breaker distinction [01:53]–[02:29].
- `ICT-2022-MENTORSHIP-EP23` — nameless 2022 precursor, broken-FVG-as-resistance idea [03:09].
