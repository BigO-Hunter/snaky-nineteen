# SNAKY Bound-19 submission package

Filing package for the Big O Speedrun Snaky challenge (bigospeedrun/verifier,
issue #106): Maker forces a Snaky within 19 own claims against every legal
Breaker sequence — full `Bound 19` (win + exact card counts + disjointness).

**Status (bound-19 branch):** skeleton only — `Submission/CardTable19.lean` is a
placeholder with `sorry` table facts.  See `HANDOFF.md`.

## Layout (maintainer contract, 2026-11-02 18:53Z)

The ONLY source root is `Submission/`:

- `Submission/SnakyStatement.lean` — the maintainer's self-contained statement
  file, copied **byte-for-byte** from
  `bigospeedrun/verifier@1f893c0a3e4828675be3a8d268df0fddaa0fe9ba`
  `challenges/other-snaky/VerifierStatement.lean`
  (sha256 `49e630b3bab9a3d1006b373edd85cf196eba0f45bdb878e0126db16776ed780b`).
- `Submission.lean` (repo root) — solution module; exports exactly
  `theorem Race.bound : BigOSpeedrun.Snaky.Bound 19`.
- `Submission/{Game,Cards,CardsSound,Bounded,Controls}.lean` — the vendored
  gotrevor card world (Apache-2.0, see NOTICE).
- `Submission/CardTable19.lean` — the 3,469-card 19-move table (**placeholder**;
  replaced by the kernel-checked table, `decide +kernel`, no `native_decide`).
- `Submission/{Plane,PlanePolicy,PlaneBound}.lean` — the plane bridge
  (G1/G2) and the `Bound` bookkeeping pack (G3).

## Pins

Toolchain `leanprover/lean4:v4.34.1`; Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612` (the rev of
`profiles/lake-manifest.json` in the verifier repo at the statement commit).

Build locally: `lake update && lake exe cache get && lake build Submission`.
