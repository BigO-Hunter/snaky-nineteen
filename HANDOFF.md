# HANDOFF — bound-19 skeleton (Snaky 19-move proof, BigO verifier)

Branch `bound-19`, based on `darkhipo/snaky-twenty` @ `f6248dc3` (the verified
Bound-20 filing). This tree adapts the G2/G3 skeleton to N=19. The verifier
statement is `Race.bound : BigOSpeedrun.Snaky.Bound n` (smaller n wins); this
tree targets `Bound 19`. Pins unchanged: Lean v4.34.1, Mathlib `d13f23b7`.

**The only missing piece is the card table**: `Submission/CardTable19.lean` is a
placeholder whose table facts are `sorry`. Everything else compiles around it.

## Build status

**Verified 2026-11-03: `lake build Submission` succeeds** (712 jobs, exit 0) on
Lean v4.34.1 + Mathlib `d13f23b7`, Mathlib oleans via `lake exe cache get`.
Warnings are the 4 intended `declaration uses 'sorry'` from
`Submission/CardTable19.lean` plus pre-existing linter/deprecation noise (also
present at `f6248dc3`). `#print axioms Race.bound` = `[propext, sorryAx,
Classical.choice, Quot.sound]` — `sorryAx` enters **only** through the 4
placeholder declarations; `#check @Race.bound` : `BigOSpeedrun.Snaky.Bound 19`.
Replacing the placeholder with `decide +kernel` table facts removes `sorryAx`.

## What changed vs. f6248dc3

| File | Change |
|---|---|
| `Submission.lean` | `Race.bound : BigOSpeedrun.Snaky.Bound 19 := Snaky.race_bound_19` |
| `Submission/PlaneBound.lean` (G3) | `race_bound_20` → `race_bound_19`; horizon constants 20→19 (final-step indices 19→18); instantiation switched to `CardTable19.*`, root index **3468** |
| `Submission/PlanePolicy.lean` (G2) | `cardStrategy_wins_20` → `cardStrategy_wins_19` (horizon 20→19, last-round case `k = 19`→`k = 18`, `CardWitness (20-k)`→`(19-k)`); `snaky_plane_bound_win` re-instantiated (root 3468, horizon 19); import `Plane17` → `Plane` + `CardTable19` |
| `Submission/CardTable19.lean` | **NEW placeholder** — the four table declarations below, `sorry`-ed |
| `Submission/Gen17/` (81 files), `Submission/Result17.lean`, `Submission/Plane17.lean` | **deleted** — the 20-move table and its instantiations. Patterns preserved in git history at `f6248dc3` (`Result17.lean` shows how `root_height` + board results were stated; `Plane17.lean` the tree-form `PlaneWinsIn` deliverable) |
| `Submission/Plane.lean` | one stale doc-comment line (was naming Gen17/Plane17) |
| `README.md`, `lakefile.toml` | package identity 20→19 (Lake files are ignored by the verifier) |

**Untouched and still parametric** (no 20/19 literals inside): the whole card
world `Submission/{Game,Cards,CardsSound,Bounded,Controls}.lean`, the G1 plane
bridge `Submission/Plane.lean`, the statement `Submission/SnakyStatement.lean`
(vendored byte-for-byte; replace with the maintainer's posted statement on
filing day and re-verify), and every supporting G2/G3 lemma
(`witness_step`, `witness_step_final`, `cardStrategy`, `cardStrategy_fresh`,
`playState_fst_card`, `playState_snd_card`, `playState_disjoint`,
`playState_disjoint_final` — all quantify over the horizon).

## The exact interface `Submission/CardTable19.lean` must satisfy

Namespace `Snaky.CardTable19`, four declarations (types verbatim — they are what
the two call sites consume):

```lean
def tree : CTree
/-- MUST stay definitionally `tree.get`. -/
def getK : Nat → Option Card := tree.get

theorem tree_ok    : tree.all (cardOK getK) = true
theorem root_ok    : rootOK getK 17 17 3468 ⟨1, 0, 0, 1, 0, 0⟩ = true
theorem root_height : (getK 3468).all (fun c => decide (c.h ≤ 19)) = true
```

Why each is needed (call sites: `PlanePolicy.lean` `snaky_plane_bound_win`,
`PlaneBound.lean` `race_bound_19` — the ONLY two consumers):

- `tree_ok` → feeds `CTree.all_get CardTable19.tree_ok`, producing G2's
  `hall : ∀ j c, getK j = some c → cardOK getK c = true`. **Structural
  requirement: `getK` must be `tree.get` definitionally**, or this application
  does not typecheck.
- `root_ok` → root card 3468 has `A = []` (cert says |A|=0) and the identity
  placement `⟨1, 0, 0, 1, 0, 0⟩` (orient index 0, dx=dy=0 — the `snaky19.cards.txt`
  header `snaky-cards-txt-v1 17 17 3468 0 0 0`) fits the 17×17 board. Must be the
  finite-board `rootOK`, not `planeRootOK`: the call sites bridge with
  `planeRootOK_of_rootOK`. (Proving `planeRootOK getK 3468 ⟨1,0,0,1,0,0⟩ = true`
  directly and dropping the bridge at the two call sites is acceptable, but keep
  `rootOK` for parity with the generated `All.lean` pattern.)
- `root_height` → G2's `hk : (get i).all (fun c => decide (c.h ≤ 19)) = true`.
  The root card's `h` is 19.

All three facts were `decide +kernel` theorems for Gen17 (no `native_decide`) —
the house rule the verifier expects. `root_height` and `root_ok` live outside the
chunk theorems (cf. `Result17.lean` / `Gen17/All.lean` at `f6248dc3`).

## Filling the placeholder (suggested recipe, mirrors Gen17)

1. Generate the table from `/Volumes/Substrate-1/bigo/snaky19/snaky19.cards.txt`
   (3,469 cards, indices 0..3468; cert: root 3468, height 19, pivot (8, 8),
   |A|=0, |S|=249; already full-semantically-verified). The 20-move tree was
   generated by `tools/cards2lean.py --name=Gen17` into
   `Data*/Tree/Chunk*/All` modules (`getK := tree.get`, per-chunk
   `tN_ok : tN.all (cardOK getK) = true := by decide +kernel`, `tree_ok` as a
   `CTree.all_node` composition). Use `--name=Gen19` or keep `CardTable19` and
   re-point the two call-site namespaces.
2. Chunk sizing: Gen17 = 1,738 cards in 41 chunks (~60 cards each). 3,469 cards
   will need ~58 chunks. Kernel checking is the long pole (the Gen17 chunks each
   ran `set_option maxHeartbeats 0 in decide +kernel`); budget real time and
   expect a large Submission olean.
3. Prove `root_ok` and `root_height` by `decide +kernel`, exactly as
   `Gen17/All.lean` / `Result17.lean` did.
4. Delete the `sorry`s, `lake build Submission`, and confirm the tree is
   sorry-free (`grep -rn "sorry" Submission/` → empty). Only then is
   `Race.bound` a real proof.

## Verification checklist for the next mind

- `lake build Submission` green with **zero** `sorry` (currently 4 sorries, all in
  `Submission/CardTable19.lean`).
- `#check Race.bound` states `BigOSpeedrun.Snaky.Bound 19`.
- On filing day: replace `Submission/SnakyStatement.lean` byte-for-byte with the
  maintainer's posted statement (sha256 in README), rebuild, and file per the
  issue-#106 maintainer contract.
