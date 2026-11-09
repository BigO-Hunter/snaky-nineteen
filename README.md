# SNAKY Bound-19 submission package

Filing package for the Big O Speedrun Snaky challenge (bigospeedrun/verifier,
issue #106): Maker forces a Snaky within 19 own claims against every legal
Breaker sequence — full `Bound 19` (win + exact card counts + disjointness).

**Status (bound-19 branch):** complete as of `880106a` — `Submission/CardTable19.lean`
holds the kernel-checked 3,469-card table (`decide +kernel`, zero `sorry`).
Credit for the 19-move construction belongs to `shjvandekamp/math@64e7eb1`
(2026-10-15); see `NOTICE.md` item 4.

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
- `Submission/CardTable19.lean` — the 3,469-card 19-move table (kernel-checked,
  `decide +kernel`, no `native_decide`).
- `Submission/{Plane,PlanePolicy,PlaneBound}.lean` — the plane bridge
  (G1/G2) and the `Bound` bookkeeping pack (G3).

## Pins

Toolchain `leanprover/lean4:v4.34.1`; Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612` (the rev of
`profiles/lake-manifest.json` in the verifier repo at the statement commit).

Build locally: `lake update && lake exe cache get && lake build Submission`.

---

## Why this repo is up

Reproducible verified bounds: the complete Bound-19 package (kernel-checked 3,469-card table) lets anyone rebuild and verify the 19-move result from the maintainer's spec.

[BigO-Hunter](https://github.com/BigO-Hunter) is the darkhipo swarm's tracking & packaging org for contributions toward [Big O Speedrun](https://bigospeedrun.com) — a companion, never the project. Org story: [profile](https://github.com/BigO-Hunter/.github) · [bigo-hunter.github.io](https://bigo-hunter.github.io).

## What work can be done here

Bound 19 is complete on the `bound-19` branch. Open work: independent rebuilds; main-branch integration; Bounds 18 and below.

## License

Licensed under the Copy-Free/Stays-Free (CFSF) License — see [LICENSE](LICENSE) ([github.com/darkhipo/cfsf](https://github.com/darkhipo/cfsf)). Vendored third-party material keeps its upstream license — see [NOTICE](NOTICE.md).
