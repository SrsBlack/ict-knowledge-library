# Commitment of Traders (COT)

**Category:** 03-order-flow
**Aliases:** COT, COT report, commitments of traders, commercial positioning, net traders position
**ICT Confidence:** high
**Year Introduced:** 2017
**Year Refined:** 2017
**Source IDs:** ICT-2017-COT
**Tags:** order-flow, futures, commercials, positioning, htf-bias, cftc

## Definition

The Commitment of Traders report is a **weekly CFTC release** breaking futures
positioning into three participant classes. ICT reads it for one thing: what the
**commercials** — the hedgers with a physical or balance-sheet interest — are doing,
because their net position reveals whether the market is in an accumulation
("buy program") or distribution ("sell program") phase at the macro scale.

It is a **higher-time-frame bias input**, not a signal: commercials net long for six
months "doesn't mean you just buy — there's other things you have to look at… but by
itself it means that they are in a **buy program**" (`ICT-2017-COT`, 07:41).

## Formal Criteria

- **Futures positions only.** ICT ignores the options side entirely: "I look at only
  the futures positions" (01:53).
- **Read the commercial column** — the centre column of the report (02:01).
- **Net position = long contracts − short contracts.** Positive is net long, negative
  net short (02:32).
- **Zero line is the phase boundary:** commercials above it = **buy program**; below it
  = **sell program** (08:48).
- **Lookback is 12 to 6 months** — "we look back a year to see what they've done" —
  recording the highest and lowest net long reading *above* the zero line and the
  highest and lowest net short reading *below* it (08:13–08:41). Current positioning is
  judged against that year's own range, not against an absolute number.
- **Duration matters:** commercials net long "for over six months" marks a macro buy
  program rather than a passing hedge (07:34).
- Commercials also run **hedging programs** inside a buy program — selling some while
  accumulating — so short bursts against the net position are expected (08:03, 08:52).

## Formula / Math

```
net_commercial(t) := commercial_long(t) - commercial_short(t)     # futures only

phase(t) := BUY_PROGRAM  if net_commercial(t) > 0
            SELL_PROGRAM if net_commercial(t) < 0

# Judged against the market's OWN 12-month range, not an absolute level:
band_above := [min(net > 0 over 12m), max(net > 0 over 12m)]
band_below := [min(net < 0 over 12m), max(net < 0 over 12m)]

# Worked example (ICT-2017-COT, 02:36-02:49), Japanese yen:
#   commercial long - commercial short = +67,024 contracts  -> net long
```

No numeric threshold for "extreme" is taught. The read is positional within the
year's range, and discretionary.

## Machine-Readable

```json
{
  "id": "commitment-of-traders",
  "category": "03-order-flow",
  "aliases": ["COT", "commercial-positioning"],
  "criteria": [
    {"id": "c1", "expr": "source == weekly CFTC report"},
    {"id": "c2", "expr": "futures_positions_only == true"},
    {"id": "c3", "expr": "net_commercial == commercial_long - commercial_short"},
    {"id": "c4", "expr": "net_commercial > 0 => buy_program"},
    {"id": "c5", "expr": "lookback_months in [6, 12]"},
    {"id": "c6", "expr": "supplies_entry == false"}
  ],
  "timeframes": ["W","M"],
  "confidence": "high",
  "year_introduced": "2017",
  "year_refined": "2017",
  "related": ["open-interest", "institutional-order-flow", "seasonal-tendency", "dollar-index"],
  "sources": ["ICT-2017-COT"]
}
```

## Visual Pattern

```
   Net Traders Position line chart (plotted beneath price):

     +  ┤        ╱‾‾‾‾╲            commercials  = RED
        │   ╱‾‾‾╱      ╲           large traders = GREEN
     0  ┼──╱──────────────╲─────   small specs   = BLUE
        │                  ╲___
     -  ┤

   Commercials above the zero line for 6+ months  -> buy program
   Commercials below the zero line                -> sell program
   Position is read against that market's OWN 12-month high/low band.
```

## Timeframes

Weekly and monthly only — the report is released weekly and describes macro
positioning. It has no intraday application.

## Examples

**Example 1 — Japanese yen net position (`ICT-2017-COT`, 01:41–02:49):**
- Open the yen COT report, futures section, commercial column.
- Long minus short = **+67,024 contracts** → commercials net long.
- Above the zero line, so the market is in a commercial buy program.

**Example 2 — duration read (07:34–07:46):**
- Commercials have held a net long position for over six months.
- That marks a macro buy program; it is not by itself an instruction to buy.

## Common Mistakes

- **Including options positions.** ICT reads futures only.
- **Reading large or small speculators as the signal.** They are plotted for contrast
  (green and blue); the commercial line (red) is the one that carries the read.
- **Treating an absolute contract count as extreme.** Extremity is relative to that
  market's own 12-month band.
- **Trading it directly.** COT is macro context; it supplies no entry, stop, or target.
- **Reading a hedging burst as a phase change.** Commercials sell inside a buy program
  by design.

## Related Concepts

- [open-interest](open-interest.md) — the other futures-only positioning read, from the same commodity lesson series.
- [institutional-order-flow](institutional-order-flow.md) — the broader directional read this feeds.
- [seasonal-tendency](../04-time-cycles/seasonal-tendency.md) — the other HTF context input taught alongside it.
- [dollar-index](dollar-index.md) — intermarket context for the same bias stack.

## Citations

- `ICT-2017-COT` (00:54) — "ICT commodity trading lesson one, commitment of traders, how I use the data"; (01:08) "the raw data comes by way of a weekly report released by the CFTC"; (01:53) "I look at only the futures positions"; (02:01) "you want to be looking in the center column here where it says commercial"; (02:32–02:49) net = long − short, yen example at +67,024 contracts net long; (03:44–03:50) commercials red, large traders green, small speculators blue; (07:34–07:46) "the commercials have been net long for over six months… by itself it means that they are in a buy program"; (08:13–08:41) the 12-to-6-month lookback and the high/low readings above and below the zero line; (08:48) "there's a buy program when they're above the zero line and a sell program when they're below it."
