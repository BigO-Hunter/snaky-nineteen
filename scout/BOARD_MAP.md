# Snaky Board Map (scouted 2026-11-06)

## Problem (exact, from verifier `challenges/other-snaky/Statement.lean` + README)

Maker–Breaker game on the infinite square grid ℤ×ℤ. Maker moves first; each side claims
one cell per move. The winning shape is the **six-cell** Snaky polyomino
`{(0,0),(1,0),(2,0),(3,0),(3,1),(4,1)}` in any of 8 orientations, any translation.
NOT the snakes-in-a-box / self-avoiding-walk line — verified against the trusted statement.

`BigOSpeedrun.Snaky.Bound n` := ∃ a single Maker policy σ (never claims an occupied cell)
such that against **every** legal Breaker sequence, after n Maker moves Maker's cells
contain a Snaky, with exact card counts and pairwise disjointness bookkeeping at every
intermediate k < n. Smaller n is better. **Floor: n ≥ 6** (need 6 cells in n claims).
No board-size envelope is imposed (infinite board).

## Scoring

Quantity = upper bound on Maker moves needed to win. Lower is better. Single leaderboard
table, evidence levels: Claimed < Human Verified < Lean Verified. Rows on the live page
(data updated 2026-11-06 5:17 PM PT):

| Bound | Evidence | Holder | Date |
|---|---|---|---|
| 19 | Lean Verified (#137) | shjvandekamp + MultiAgency swarm (darkhipo) | Nov 3 |
| =1 19 | Claimed | shjvandekamp | Oct 15 |
| 3 20 | Lean Verified (#114) | MultiAgency swarm (darkhipo) | Nov 2 |
| =3 20 | Claimed | Nándor Sieben (strategy) + gotrevor | Oct 7 |
| 5 21 | Agent breakthrough | OpenAI | Oct 6 |

**We (darkhipo) hold the top row jointly** and the first LV row. Rank 1 attribution was
settled by maintainer ruling (verifier #142): shjvandekamp = 19-move construction +
card certificate; Dmitri I. Arkhipov = Lean verification package.

## Proof scope of the LV rows

Verifier checks `Race.bound : BigOSpeedrun.Snaky.Bound (19)` at
`darkhipo/snaky-nineteen@880106a` (and Bound 20 at `darkhipo/snaky-twenty@f6248dc`).

## Separate sub-race (NOT scored on this board)

Board-size question: smallest Maker-winning square side, currently 10 ≤ side ≤ 15.
Tracked only as a "relevant repo" link (gotrevor/snaky-15x15; 9×9 Breaker claim has
certificate + Python checker, no Lean). shjvandekamp's "Open work" also lists the
empty 14×14 / 10×10 questions. Formalizing these scores **no row** here.
