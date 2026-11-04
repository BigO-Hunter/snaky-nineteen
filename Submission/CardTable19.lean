import Submission.Gen19.All

/-!
# The 19-move card table (generated)

The kernel-checked 19-move card table (construction: shjvandekamp,
shjvandekamp/math@64e7eb1 — a 19-move certificate built on Sieben's
20-move and Morris's 15×15 strategies; Lean table and verification
packaging: this campaign, Apache-2.0). 3,469 cards, root index 3468,
root height 19, `|A| = 0`, `|S| = 249`, source
`snaky19.cards.txt`, format `snaky-cards-txt-v1`).  The data lives in the
generated `Submission/Gen19/` modules (cf. `tools/gen19.py`): card literals in
`DataNN.lean`, the lookup tree in `Tree.lean`, per-chunk `decide +kernel`
justification proofs in `ChunkNNN.lean` composed into `Gen19.tree_ok`.

**The one structural requirement:** `getK` is *definitionally* `tree.get` (that
is how `CTree.all_get tree_ok` produces the `hall : ∀ j c, getK j = some c →
cardOK getK c = true` argument of `cardStrategy_wins_19`).
-/

namespace Snaky.CardTable19

/-- The 3,469-card lookup tree generated from `snaky19.cards.txt`. -/
def tree : CTree := Gen19.tree

/-- The lookup the checker reads.  MUST stay `tree.get` definitionally. -/
def getK : Nat → Option Card := tree.get

/-- Every card in the lookup tree is justified: `tree.all (cardOK getK) = true`,
composed from the per-chunk `decide +kernel` proofs by `CTree.all_node`. -/
theorem tree_ok : tree.all (cardOK getK) = true := Gen19.tree_ok

/-- The root card 3468 has `A = []` and fits the board under the identity placement
(`⟨1, 0, 0, 1, 0, 0⟩`, orient 0, dx 0, dy 0 — the `snaky19.cards.txt` header
`snaky-cards-txt-v1 17 17 3468 0 0 0`). -/
theorem root_ok : rootOK getK 17 17 3468 ⟨1, 0, 0, 1, 0, 0⟩ = true := by
  decide +kernel

/-- The root card 3468 has height at most 19. -/
theorem root_height : (getK 3468).all (fun c => decide (c.h ≤ 19)) = true := by
  decide +kernel

end Snaky.CardTable19
