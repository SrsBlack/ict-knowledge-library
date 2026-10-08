# External Range Liquidity (ERL)

**Category:** 02-liquidity
**Aliases:** ERL, external liquidity
**ICT Confidence:** high
**Year Introduced:** 2016
**Year Refined:** 2022
**Source IDs:** ICT-2016-REINFORCING-LIQUIDITY, ICT-2016-ORDERBLOCKS, ICT-2017-INTRADAY-TOP-DOWN, ICT-2022-MENTORSHIP-EP06, ICT-2022-MENTORSHIP-EP12
**Tags:** liquidity, erl, external, dealing-range

> ⚠ **Re-dated 2026-10-08.** Previously `Year Introduced: 2022` with the IRL/ERL split described as "formalized in 2022 mentorship" — contradicted. ERL/IRL is taught verbatim in the December 2016 lecture *Reinforcing Liquidity Concepts & Price Delivery* and again in the August 2017 *Intraday Top-Down* lecture; the 2022 mentorship reuses the 2016-17 term and wording unchanged. See citations.

## Definition

External Range Liquidity is liquidity that sits outside the **current trading range** — ICT's own term, not "LTH/LTL": "the current trading range will have buy side liquidity above the range high… sell side liquidity below the range or low" (`ICT-2016-REINFORCING-LIQUIDITY`, 00:54–01:02). 2022 restates it unchanged: "what is the stops below these lows down here? External range liquidity" (`ICT-2022-MENTORSHIP-EP06`, 45:41). ERL is the algorithmic full-delivery/exit destination: "predominantly, my entries are internal range liquidity entries, with exits at external range liquidity… I'm buying inside the range and selling it outside the range" (`ICT-2016-REINFORCING-LIQUIDITY`, 10:29–10:40); "so partials — internal range, external range — your trade" (EP06, 45:41); "external range liquidity, turtle soup, running out stops, and fading that move" (`ICT-2017-INTRADAY-TOP-DOWN`, 46:46). Mirror concept to [internal-range-liquidity](internal-range-liquidity.md).

## Formal Criteria

- The reference is whichever **trading range** is currently in play, not a fixed LTH/LTL swing depth — ICT gives no swing-depth rule for the range's bounds (see Formula / Math).
- ERL = buy-side liquidity above the range high, or sell-side liquidity below the range low.
- **Classification is range-relative, not absolute**: "in the context from this high to this low, it's internal range liquidity. But from this low to this high, it's external range liquidity" (`ICT-2016-REINFORCING-LIQUIDITY`, 05:59–06:04). The same stop level can be ERL on one timeframe/range and IRL on another: "that is a run on external range liquidity on this timeframe, being the daily. But on the monthly chart, it's still internal range liquidity" (11:58–12:08).
- 2022 also uses a long-term-high-to-long-term-low framing specifically for **targeting**: "the range between this long-term high and this long-term low — that range is going to be used for targeting purposes" (`ICT-2022-MENTORSHIP-EP12`, 25:56).
- "Taking ERL = external BOS = bias change" is **not in either corpus** — searched "external bos," "external break of structure," "external structure," "bias change/flip/shift" (0/0 each). ICT's ERL "take" is the exit of a trade or the [turtle-soup](../20-turtle-soup/turtle-soup.md) fade, not a stated bias-flip trigger.

## Formula / Math

ICT gives **no fixed swing-depth formula** (e.g. depth-2 ITH/ITL) for where the reference range's bounds sit; the range is whichever one the analysis is framed on, and the ERL/IRL label is relative to it.

```
is_ERL(level, range) := level is outside the currently-referenced trading range
                          [the range itself is reference-relative, not a fixed depth]
```

## Machine-Readable

```json
{
  "id": "external-range-liquidity",
  "category": "02-liquidity",
  "aliases": ["ERL", "external-liquidity"],
  "criteria": [
    {"id": "c1", "expr": "level outside the currently-referenced trading range (range-relative, not absolute)"},
    {"id": "c2", "expr": "ERL = exit/full-delivery side; IRL = entry side (see internal-range-liquidity)"}
  ],
  "timeframes": ["M5","M15","H1","H4","D","W"],
  "confidence": "high",
  "year_introduced": "2016",
  "year_refined": "2022",
  "related": ["internal-range-liquidity","external-structure","draw-on-liquidity","dealing-range","liquidity-pool","bos-bullish","bos-bearish"],
  "sources": ["ICT-2016-REINFORCING-LIQUIDITY","ICT-2016-ORDERBLOCKS","ICT-2017-INTRADAY-TOP-DOWN","ICT-2022-MENTORSHIP-EP06","ICT-2022-MENTORSHIP-EP12"]
}
```

## Visual Pattern

```
   ─── BSL ERL: above the range high ───  ← exit / full-delivery target

        (current trading range)
                                            same level is IRL on a
   ─── SSL ERL: below the range low ───     higher timeframe's range
```

## Timeframes

Range-relative at every TF. What is ERL on a daily range can be IRL on the monthly range viewing the same level — always name the reference TF/range.

## Examples

**Example 1 — range-relative ERL/IRL:**
- On the daily chart, a stop cluster below a short-term low sits outside the current daily range → daily ERL.
- The same level sits inside the current monthly range → monthly IRL.
- → "it's a run on external range liquidity on the daily, but on the monthly chart it's still internal range liquidity" (`ICT-2016-REINFORCING-LIQUIDITY`, 11:58–12:08).

## Common Mistakes

- **Calling it LTH/LTL-bounded by rule.** ICT's term is "current trading range"; no fixed swing-depth definition is given in either corpus.
- **Asserting "ERL take = external BOS = bias change."** Not in the corpus; don't present this as ICT's rule. His stated ERL use is exit/partial or the turtle-soup fade.
- **Treating ERL/IRL as absolute properties of a level.** They are range-relative — the same level can be both, depending on which range is being referenced.

## Related Concepts

- [internal-range-liquidity](internal-range-liquidity.md) — entry-side counterpart.
- [external-structure](../01-market-structure/external-structure.md) — related but not equated with "taking ERL" in the corpus.
- [draw-on-liquidity](draw-on-liquidity.md) — ERL is a common full-delivery DOL target.
- [dealing-range](../05-pd-arrays/dealing-range.md) — the "current trading range" whose extremes are ERL.
- [turtle-soup](../20-turtle-soup/turtle-soup.md) — one of the two named patterns alongside IRL/OTE (`ICT-2017-INTRADAY-TOP-DOWN`).

## Citations

- `ICT-2016-REINFORCING-LIQUIDITY` (00:54–01:02) "the current trading range will have buy side liquidity above the range high… sell side liquidity below the range or low"; (05:59–06:04) range-relative classification; (10:29–10:40) "predominantly, my entries are internal range liquidity entries, with exits at external range liquidity… I'm buying inside the range and selling it outside the range"; (11:58–12:08) the same level as ERL (daily) / IRL (monthly).
- `ICT-2016-ORDERBLOCKS` (08:16–08:41) internal vs external range liquidity introduced in the order-block context.
- `ICT-2017-INTRADAY-TOP-DOWN` (46:40–46:46) "internal range liquidity, optimal trade entry… or external range liquidity, turtle soup, running out stops, and fading that move."
- `ICT-2022-MENTORSHIP-EP06` (45:41) "what is the stops below these lows down here? External range liquidity… so partials, internal range, external range, your trade."
- `ICT-2022-MENTORSHIP-EP12` (25:56) "the range between this long-term high and this long-term low — that range is going to be used for targeting purposes."
