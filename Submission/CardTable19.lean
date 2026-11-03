import Submission.CardsSound

/-!
# The 19-move card table — PLACEHOLDER (interface only, facts `sorry`)

This module stands in for the kernel-checked 19-move card table (Nándor Sieben /
snaky19 construction; 3,469 cards, root index 3468, root height 19, pivot (8, 8),
`|A| = 0`, `|S| = 249`, source `snaky19.cards.txt`, format `snaky-cards-txt-v1`).

Everything the G2/G3 layers consume is declared here with its exact final type, so the
proof skeleton (`PlanePolicy.cardStrategy_wins_19`, `PlaneBound.race_bound_19`) compiles
unchanged once the `sorry`s below are replaced by the real generated table.  See
`HANDOFF.md` for what the real module must contain.

**The one structural requirement:** `getK` must remain *definitionally* `tree.get`
for some `tree : CTree` (that is how `CTree.all_get tree_ok` produces the
`hall : ∀ j c, getK j = some c → cardOK getK c = true` argument of
`cardStrategy_wins_19`).
-/

namespace Snaky.CardTable19

/-- Placeholder lookup tree.  Real module: the 3,469-card `CTree` generated from
`snaky19.cards.txt` (cf. `tools/cards2lean.py`, `--name=Gen19`). -/
def tree : CTree := sorry

/-- The lookup the checker reads.  MUST stay `tree.get` definitionally. -/
def getK : Nat → Option Card := tree.get

/-- Every card in the lookup tree is justified: `tree.all (cardOK getK) = true`.  Real module:
one `decide +kernel` theorem per chunk composed by `CTree.all_node`. -/
theorem tree_ok : tree.all (cardOK getK) = true := sorry

/-- The root card 3468 has `A = []` and fits the board under the identity placement
(`⟨1, 0, 0, 1, 0, 0⟩`, orient 0, dx 0, dy 0 — the `snaky19.cards.txt` header
`snaky-cards-txt-v1 17 17 3468 0 0 0`).  Real module: `by decide +kernel`. -/
theorem root_ok : rootOK getK 17 17 3468 ⟨1, 0, 0, 1, 0, 0⟩ = true := sorry

/-- The root card 3468 has height at most 19.  Real module: `by decide +kernel`. -/
theorem root_height : (getK 3468).all (fun c => decide (c.h ≤ 19)) = true := sorry

end Snaky.CardTable19
