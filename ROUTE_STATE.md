# Snaky Route State (scouted 2026-11-06)

## Verdict: ROUTE IS OPEN — and we have already used it twice, successfully

This is the board the maintainer holds up as the template (nmamano on verifier #148:
routes open "in the same steps as for Snaky: trusted statement, closed profile,
maintainer smoke run, test"). Snaky is not waiting for a gate. It already has one.

## The route artifacts (verified in `bigospeedrun/verifier` @ main, challenges/other-snaky/)

- `Model.lean` — OpenAI's definition block, byte-copied from openai/math
  `SnakyTwentyOne.lean@1581d4cb` (Apache-2.0, sha256-pinned in provenance.json).
- `Statement.lean` — parameterized `Bound n` by fluorine + Codex (verifier PR #65).
- `VerifierStatement.lean` — the single self-contained file copied into submissions;
  only Mathlib imports; must not be modified by submitters.
- `Validation.lean` — statement checks (not part of the trusted target).
- Issue route opened **2026-11-03** (enablement = verifier issue #106: maintainer
  smoke fixture + negative controls). Bot confirms supported problems include `snaky`.
- Submission: `lean-submission.yml` issue template; verifier polls every 30 min,
  one proof at a time; bot posts derivation report → Lean checkpoint → final receipt.
- Pinned toolchain: lean4 v4.34.1, Mathlib `d13f23b7`.

## Our own track record on this exact route

- **Bound 20** — LV, issue #114, `darkhipo/snaky-twenty@f6248dc` (Nov 2-3).
- **Bound 19** — LV, issue #137, `darkhipo/snaky-nineteen@880106a` (Nov 3-4),
  packaging shjvandekamp's Oct-15 construction (license/collab arc: offer in
  shjvandekamp/math#8 → withdrawn as moot → credit settled by nmamano in #142).
- Method published as a free community kit: `darkhipo/bigospeedrun-agent-kit`
  (ACTIVATION_PLAYBOOK.md, AGENT_PROOF_KIT.md).

## Implication for the playbook

There is nothing to wait for. The prime-gaps pre-positioning pattern (hold ready
composition → file within minutes of gate-open) is moot here: the gate is open, and
the next row (18) is blocked purely by **missing mathematical content**, not by
process. Any 18 certificate that appears can be packaged and filed same-day with
existing machinery.
