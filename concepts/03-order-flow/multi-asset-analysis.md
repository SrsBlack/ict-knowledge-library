# Multi-Asset Analysis

**Category:** 03-order-flow
**Aliases:** four asset classes, multi-asset class analysis, risk on risk off, asset-class decoupling, intermarket harmony
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-MULTI-ASSET, ICT-2017-BOND-TRENDING-DAYS, ICT-2017-BOND-CONSOLIDATION-DAYS, ICT-2017-LONGTERM-TOP-DOWN
**Tags:** order-flow, intermarket, risk-on-risk-off, bonds, equities, commodities, currencies, volatility, magnitude

## Definition

Multi-asset analysis is ICT's **regime filter**: reading **bonds, currencies, commodities and
stocks together** to decide how much magnitude the market is currently capable of delivering. It
does not select a pair and it does not produce an entry. It answers one question — is the market
**coupled** (all four behaving as they should relative to one another) or **decoupled** (each
doing its own thing)?

"The purpose of having multi-asset class analysis — that is the asset classes of the **bonds,
currencies, commodities, and stocks** — is by looking at them **as a whole**, how they're
interrelated" (`ICT-2017-MULTI-ASSET`, 00:56).

The consequence is a size and expectation setting, not a signal: "if they're not [behaving
seasonally], that means that we have a **decoupling**, and it's going to be **hard for the markets
to find a one-sided move with a great deal of magnitude**" (25:10).

## Formal Criteria

**The four classes** (00:56)

1. **Bonds / interest rates**
2. **Currencies**
3. **Commodities**
4. **Stocks**

**The risk-on / risk-off switch, read off the bond market** (02:33–03:09)

| Bond market | Regime | What follows |
|---|---|---|
| **going higher** | **risk off** — "a scenario where it's less risk interest… the market goes to buying bonds" | — |
| **going lower** | **risk on** | "risk on scenarios bring with it the **buying of stocks, the buying of foreign currencies**" |

- Foreign currencies "**rally when it's risk on, decline when it's risk off — and dollar will
  rally**" (06:56–07:03).

⚠ **This mapping conflicts with the bond-trending lecture of the same month.** See *Common
Mistakes* below — the two lectures give opposite dollar consequences for a rallying bond market.

⚠⚠ **A third lecture reverses the *stock* leg as well — two transmission channels, not one.**
`ICT-2017-LONGTERM-TOP-DOWN` (Aug 2017) reads bonds as a **discount-rate** signal where this
lecture reads them as a **risk-appetite** signal, and the two run opposite on both directions:

| Bond market | This lecture (`ICT-2017-MULTI-ASSET`, risk channel) | `ICT-2017-LONGTERM-TOP-DOWN` [08:07–08:33] (rate channel) |
|---|---|---|
| **going lower** | risk on → **buying of stocks** | rates rising → "**harder for stocks to maintain a bullish market**" |
| **going higher** | risk off | rates falling → "generally that's going to be **supportive of a bull market in stocks**" |

Verbatim: "Is the bond market moving lower? If it is going lower, that means interest rates are
going higher. It's going to be harder for stocks to maintain a bullish market. And if bond prices
are rallying, that means interest rates are going lower. And generally that's going to be
supportive of a bull market in stocks."

**Neither lecture ranks the two channels, and a reader cannot act on both at once.** Both are
recorded here rather than one being chosen, because the corpus does not choose. What the Aug-2017
lecture *does* assert is the primacy of the rate variable itself — "**interest rates are the
number one driver across the board on all asset classes**… if you don't understand interest rates,
you're not going to get anything out of any of the market analysis concepts provided thus far"
[09:40–09:50] — which independently corroborates this page's claim that the bond market gates the
other three classes, even while disagreeing about the sign.

**The coupling test** (20:15–21:41)

- **Two of four** behaving as they should → "**is that a very symmetrical market? No.**"
- **A third joins** → "that's now very interesting… we're starting to come out of this chaotic
  uncertainty. So therefore **more of smart money's money is being put to work**."
- **All four in harmony** → "when it's easy to make money… **all four asset classes will be
  working in harmony with one another**" (06:26–06:41), and the market produces "**big, huge,
  profitable market moves**" that "**are easy to see coming**" (13:34–13:45).
- **Decoupled** → "smart money is **not willing to make large contributions** to one side of the
  market or another, or **they're waiting on something**" (10:05–10:23).

**The mechanism — the bond market gates volatility for everything else**

- "**You can't get explosive price action without the participation in the interest rate**"
  (`ICT-2017-BOND-TRENDING-DAYS`, 12:25). "If you follow that and you follow the bond market, **it
  unlocks everything. It's like tumblers in a lock**" (12:36).
- Conversely: "**while the bond market is held in a narrow range, this will create a stranglehold
  on volatility for the other asset classes** on average"
  (`ICT-2017-BOND-CONSOLIDATION-DAYS`, 18:09).
- Operational consequence for an FX trader: "we can **reduce or limit our expectations on FX
  pairs' movement** and operate in a more reserved fashion, sticking to low-hanging fruit and
  small gains" (24:40).

**The standing survey** (17:43–18:12)

Four questions, asked periodically rather than watched continuously — "you don't have to be
staring at them all day long, **periodically check them**" (13:10):

1. Are **commodities** going higher or lower generally?
2. Are **interest rates** going up or down?
3. How is that affecting the **dollar** — up or down?
4. Are **equities** finding an ease to rally, or struggling and consolidating?

Plus a seasonal cross-check: "**what's their seasonal tendency? Are they behaving seasonally?**"
(25:04).

**Scope**

- The lecture is a **summary of the whole Month-10 asset-class series**, delivered on **Friday
  30 June 2017** (15:40), and it explicitly does **not** teach commodity mechanics: "I didn't
  give you a top-down, here's the crash course on trading commodities — **first notice day, last
  trading day of the month, contract rollover** — I didn't go into all those things. I went and
  talked about the **most salient, important things from each asset class**" (20:24–20:52).
- ICT states he trades FX only and still reads all four (03:37–03:49).

## Formula / Math

```
classes := {bonds, currencies, commodities, stocks}

# --- regime switch (as stated in this lecture) ---
regime := bonds_rising ? RISK_OFF : RISK_ON

RISK_ON  => stocks bid, foreign currencies bid
RISK_OFF => stocks sold, foreign currencies sold, dollar bid

# --- coupling score ---
n := count(c in classes where c behaves consistently with regime
                              AND with its own seasonal tendency)

n == 4   -> harmony      : expect large, one-sided, "easy to see coming" moves
n == 3   -> improving    : smart money putting money to work
n == 2   -> asymmetric   : not a symmetrical market
n <= 1   -> decoupled    : smart money on the sidelines / waiting
                           => reduce expectation of magnitude
                           => trades still exist; strong one-sided moves do not

# --- the volatility gate ---
bond_range == narrow  => stranglehold on volatility across all classes
bond_range == expanding => volatility unlocked across all classes

# --- what it outputs ---
supplies_bias  == false
supplies_entry == false
supplies_magnitude_expectation == true
```

## Machine-Readable

```json
{
  "id": "multi-asset-analysis",
  "category": "03-order-flow",
  "aliases": ["four-asset-classes", "risk-on-risk-off", "asset-class-decoupling", "intermarket-harmony"],
  "criteria": [
    {"id": "c1", "expr": "classes == {bonds, currencies, commodities, stocks}"},
    {"id": "c2", "expr": "bonds_rising => risk_off; bonds_falling => risk_on"},
    {"id": "c3", "expr": "risk_on => stocks and foreign currencies bought; risk_off => dollar bid"},
    {"id": "c4", "expr": "2 of 4 aligned == not symmetrical; 3 of 4 == smart money engaging; 4 of 4 == harmony and large moves"},
    {"id": "c5", "expr": "decoupled => smart money absent => expect small magnitude, not absence of trades"},
    {"id": "c6", "expr": "narrow bond range => volatility stranglehold across all classes"},
    {"id": "c7", "expr": "explosive price action requires interest-rate participation"},
    {"id": "c8", "expr": "survey := commodity direction, rate direction, dollar direction, equity ease-of-rally, plus seasonal conformance"},
    {"id": "c9", "expr": "checked periodically, not monitored continuously"},
    {"id": "c10", "expr": "supplies_bias == false; supplies_entry == false; supplies magnitude expectation only"}
  ],
  "timeframes": ["D","W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["dollar-index", "interest-rate-triad", "bond-yield-analysis", "macro-to-micro-framework", "relative-strength-analysis", "explosive-market-selection", "bond-trending-and-consolidation-days", "seasonal-tendency", "correlation-risk", "commitment-of-traders"],
  "sources": ["ICT-2017-MULTI-ASSET", "ICT-2017-BOND-TRENDING-DAYS", "ICT-2017-BOND-CONSOLIDATION-DAYS", "ICT-2017-LONGTERM-TOP-DOWN"]
}
```

## Visual Pattern

```
   THE COUPLING SCORE

   BONDS       ████  behaving         ┐
   CURRENCIES  ████  behaving         │  4 of 4  -> HARMONY
   COMMODITIES ████  behaving         │  big, one-sided, easy to see coming
   STOCKS      ████  behaving         ┘

   BONDS       ████                   ┐
   CURRENCIES  ████                   │  3 of 4  -> smart money engaging
   COMMODITIES ░░░░  not              │  "that's now very interesting"
   STOCKS      ████                   ┘

   BONDS       ████                   ┐
   CURRENCIES  ░░░░                   │  2 of 4  -> NOT a symmetrical market
   COMMODITIES ░░░░                   │
   STOCKS      ████                   ┘

   BONDS       ░░░░                   ┐
   CURRENCIES  ░░░░                   │  DECOUPLED
   COMMODITIES ░░░░                   │  smart money waiting
   STOCKS      ░░░░                   ┘  -> cut magnitude expectations

   ─────────────────────────────────────────────────────────────
   THE GATE

     bond range NARROW   ══╪══   stranglehold on volatility everywhere
     bond range EXPANDS  ──┼──►  "it's like tumblers in a lock"
```

## Timeframes

Daily, weekly and monthly. This is a regime read, checked periodically — there is no intraday
form and no entry attached to it.

## Examples

**Example 1 — a no-trade day called from the four classes (`ICT-2017-MULTI-ASSET`, 14:42–16:07):**
- Date: **Friday 30 June 2017**, ahead of the following Tuesday's 4 July holiday.
- A member expected a promised USDCAD trade. ICT: "**using the asset classes as a whole, all four
  of them, I didn't see a trade this morning. And there was no trade this morning.**"
- Reasons given: a consolidation day ahead of a widely followed US holiday; the week's downside
  objective had already been met and slightly exceeded, so there was nothing left to reach for;
  and nothing across the four classes indicated a new draw.

**Example 2 — the same read used positively (25:24–25:49):**
- ICT contrasts the decoupled state with "**the strong moves like we outlined this past Saturday
  that we saw come to fruition beautifully across many pairs. All of our targets were hit. And
  they weren't small moves — they were large moves. And it comes by way of looking at all four
  asset classes.**"

**Example 3 — the 2017 debt-market read as the standing regime
(`ICT-2017-BOND-CONSOLIDATION-DAYS`, 24:55–25:36):**
- Observation: the bond market had been range-bound for months through the first half of 2017.
- Read: "**this is the reason why the markets have been rather fickle** — because the bond market
  as a whole has been in a range-bound consolidation."
- Forward expectation: "when it leaves the range, it will have a protractionary state where it
  moves in a trend. That's when **salad days** are coming."

## Common Mistakes

- **⚠ Assuming a rallying bond market is dollar-bullish because it is "risk off".** The two
  Month-10 lectures give **opposite** consequences and the library records both:
  - `ICT-2017-MULTI-ASSET` (02:33–03:09, 06:56–07:03) — bonds higher = risk off; risk off = foreign
    currencies decline and **the dollar rallies**.
  - `ICT-2017-BOND-TRENDING-DAYS` (14:31–14:56) — "since we're seeing the bond market **rally**…
    the interest rates are actually decreasing… that's going to, more times than not, **pressure
    U.S. dollar down**, and foreign currencies will chase higher yield… so that way you see
    **higher foreign currencies when bond markets rally**."
  The yield-chasing mechanism is the one the rest of the library is built on (see
  [interest-rate-triad](interest-rate-triad.md), whose direction convention is rate-instrument
  price **up** = rates down = **bearish for the dollar**). Treat the risk-off phrasing as the
  broad-market framing and the rate/yield mechanism as the operative rule, and do not stack the
  two as if they agreed.
- **Treating "decoupled" as "do not trade".** ICT is explicit: "I'm not saying you won't see
  trades — it's just you won't see really strong moves."
- **Using it to pick a direction.** It sets **magnitude expectation**. Direction still comes from
  the ordinary bias tools.
- **Watching all four continuously.** The instruction is to check them periodically.
- **Expecting commodity mechanics from this month.** First notice day, last trading day and
  contract rollover were deliberately excluded.
- **Reading the lecture as motivational only.** Most of its runtime is exhortation, but the
  coupling test, the risk switch and the four-question survey are stated as rules.

## Related Concepts

- [interest-rate-triad](interest-rate-triad.md) — the mechanical form of "is the interest-rate market participating"; also the page whose direction convention resolves the contradiction above.
- [bond-trending-and-consolidation-days](../31-models/bond-trending-and-consolidation-days.md) — how the bond market's own day-type is forecast, which is the gate this page depends on.
- [bond-yield-analysis](bond-yield-analysis.md) — how the interest-rate class is judged trending or not.
- [macro-to-micro-framework](macro-to-micro-framework.md) — the 3–6 month debt-market outlook this regime read sits on top of.
- [relative-strength-analysis](relative-strength-analysis.md) — once the regime is coupled, this picks which member of a group to trade.
- [explosive-market-selection](../31-models/explosive-market-selection.md) — hallmark 1 is this page's coupling test in checklist form (≥2 of 4 trending, one from each group).
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — the seasonal-conformance cross-check.
- [dollar-index](dollar-index.md) — the hub every class is read against.
- [correlation-risk](../32-risk-management/correlation-risk.md) — the position-sizing consequence of a coupled market.
- [commitment-of-traders](commitment-of-traders.md) — the positioning evidence behind "smart money is waiting".

## Citations

- `ICT-2017-MULTI-ASSET` (00:21) "we have just finished the **June content for the ICT Mentorship**" — self-dates the lecture as the Month-10 wrap-up; (00:56–01:17) "the purpose of having multi-asset class analysis, that is the asset classes of the **bonds, currencies, commodities, and stocks**, is by looking at them **as a whole** — how they're interrelated"; (01:49) "**risk on and risk off**"; (02:33–02:56) "if there's a **decoupling** — in other words, if the **bond market is going higher**, that means that there's a scenario where it's less risk interest. **It's a risk off environment.** So the market goes to buying bonds"; (02:56–03:09) "**when the bond market is going lower, then there's a risk on scenario. Risk on scenarios bring with it the buying of stocks, the buying of foreign currencies**"; (03:18–03:26) "these back and forth ebb and flow type phenomenon have a **reverberation that goes through all four of the asset classes**"; (03:37–03:49) "all of you know **I only trade Forex** — and yet I still talk about the bond market, commodities, and stocks. **Because it matters**"; (04:02–04:26) "to be a specialist, you still have to understand what the general market is going to do… when all of the asset classes are doing as they should, **risk on environments, everything should rally**"; (06:23–06:41) "because there's a lot of **uncertainty** — and when it's easy to make money… **all four asset classes will be working in harmony with one another**"; (06:41–07:03) "dollar index goes higher. Commodities go lower. Stocks go higher. Risk on. Risk off. Stocks fall. **Currencies, foreign in nature, rally when it's risk on. Decline when it's risk off. And dollar will rally**" ⚠ (whisper renders this passage as short disconnected fragments; only the currency/dollar sentence is unambiguous); (07:38–07:46) "**will you understand when the large moves are going to take place and how long to hold on to them** based on those conditions, just looking at the euro? **No**"; (09:49–10:23) "if there is a decoupling and the markets are having erratic behavior… **smart money is not willing to make large contributions to one side of the market or another, or they're waiting on something**"; (13:10–13:21) "you don't have to be staring at them all day long. **Periodically check them**… they should be **moving in concert with one another**"; (13:27–13:45) "there's an **ebb and flow** that is necessary for the markets to be highly efficient. And when they're efficient, they create **big moves**… and **they're easy to see coming**"; (14:42–16:07) the Friday 30 June 2017 no-trade example — "**using the asset classes as a whole, all four of them, I didn't see a trade this morning. And there was no trade this morning**"; (17:07–17:24) "the way you [are] able to determine those conditions is by **rating the market in terms of risk on and risk off**, and you can't get that adequately enough by just looking at **one instrument, one pair**"; (17:43–18:12) the four-question survey — commodities, interest rates, the dollar, equities; (20:24–20:52) "I didn't give you a top-down… **first notice day, last trading day of the month, contract rollover** — I didn't go into all those things. I went and talked about the **most salient, important things from each asset class**"; (20:57–21:08) "the **likelihood of a directional move per asset class** and the importance of knowing what to look for and when it should happen"; (21:08–21:41) "what happens when you start seeing just **two of the four** asset class doing one thing but the other two aren't?… Is that a very symmetrical market? **No**. But what happens if we start seeing **a third** start doing it? Well, **that's now very interesting**… so therefore **more of smart money's money is being put to work**"; (23:00–23:17) "if I can't find them, if **they're not leaving clear tracks, I'm keeping my hands in my pocket**"; (25:04–25:24) "**what's their seasonal tendency? Are they behaving seasonally?** Because if they're not, that means that we have a **decoupling**, and it's going to be hard for the markets to find a **one-sided move with a great deal of magnitude**. Now, **I'm not saying you won't see trades** — it's just you won't see really strong moves"; (25:24–25:49) the contrasting week where "**all of our targets were hit… they were large moves**".
- `ICT-2017-BOND-TRENDING-DAYS` (12:25–12:41) "**you can't get explosive price action without the participation in the interest rate**… I said this on Baby Pips back in 2010: the key is knowing the interest rates. If you follow that and you follow the bond market, **it unlocks everything. It's like tumblers in a lock**"; (12:43–12:49) "if you're trading without this insight, **you're really trading blind**"; (14:31–14:56) "since we're seeing the bond market rally examples here, what that's showing is the **interest rates are actually decreasing**… that's going to, more times than not, **pressure U.S. dollar down**, and **foreign currencies will chase higher yield**… so that way you see **higher foreign currencies when bond markets rally**, and the dollar index generally looks for lower prices" — ⚠ the opposite dollar consequence to the risk-off framing above; (10:04–10:13) "when the interest rate market kicks off and it's allowed to move energetically, that's going to **promote the idea for all the asset classes to be able to move**".
- `ICT-2017-LONGTERM-TOP-DOWN` (08:07–08:33) ⚠ **the rate channel, which runs opposite to this lecture's risk channel on both directions** — "Is the bond market moving lower? If it is going lower, that means **interest rates are going higher. It's going to be harder for stocks to maintain a bullish market**. And if bond prices are rallying, that means interest rates are going lower. And generally that's going to be **supportive of a bull market in stocks**"; (09:40–09:50) "**interest rates are the number one driver across the board on all asset classes**… if you don't understand interest rates, you're not going to get anything out of any of the market analysis concepts provided thus far" — which corroborates this page's claim that the bond market gates the other three classes even while disagreeing about the sign. Neither lecture ranks the two channels; both are recorded rather than one chosen, because the corpus does not choose. See the second table under *Formal Criteria*.
- `ICT-2017-BOND-CONSOLIDATION-DAYS` (08:35–08:47) "the incorporation of the **interest rate markets and the bond market — that's that missing link**"; (08:47–08:56) "if we know that there's going to be a consolidation period in the bond market, we have to **reasonably expect the same thing occurring in the other asset classes**"; (18:09–18:32) "**while the bond market is held in a narrow range, this will create a stranglehold on volatility for the other asset classes** on average. So just because the bond market is in consolidation doesn't mean it's going to be the wild, wild west in the Japanese yen"; (24:40–24:55) "the use of this observation serves us well as forex traders, in that we can **reduce or limit our expectations on FX pairs' movement** and operate in a more reserved fashion, sticking to **low-hanging fruit and small gains**"; (24:55–25:36) the 2017 range-bound bond market as the reason "the markets have been rather fickle", and the expectation of a trending "protractionary state" on the way out.
