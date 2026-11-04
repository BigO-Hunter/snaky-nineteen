NOTICE — provenance and licensing for the SNAKY package (Bound-19 and Bound-20)

1. `Submission/SnakyStatement.lean`
   Byte-for-byte copy of bigospeedrun/verifier
   `challenges/other-snaky/VerifierStatement.lean` at
   1f893c0a3e4828675be3a8d268df0fddaa0fe9ba (sha256
   49e630b3bab9a3d1006b373edd85cf196eba0f45bdb878e0126db16776ed780b).
   The statement's embedded model definitions are extracted unchanged from
   OpenAI SnakyTwentyOne.lean at
   1581d4cbdd69a0faf34b2089614fe2a814316a6a (Apache-2.0).

2. `Submission/{Game,Cards,CardsSound,Bounded,Controls}.lean` and
   `Submission/Gen17/*` — the 17x17 card world (1,738 verified cards,
   `decide +kernel`), vendored from the gotrevor research repository
   (branch plane-bridge of the campaign clone; upstream commits 1173345
   "Snaky wins 17 x 17 within 20 Black moves" and b18ed32).
   Chain of provenance: gotrevor <- Sieben's 17x17 card sequence
   (third_party/sieben/cards-17x17.txt, permission), shape parameterization
   from the OpenAI SnakyTwentyOne strategy (Apache-2.0).

3. `Submission/{Plane,Plane17,PlanePolicy,PlaneBound}.lean` and
   `Submission/Submission.lean` — original work of this campaign (the
   plane lift of the card soundness induction, the total fresh policy
   `cardStrategy Gen17.getK`, and the `playState` bookkeeping lemmas),
   2026-11-02. Apache-2.0.

4. `Submission/CardTable19.lean`, `Submission/Gen19/*` and `tools/snaky19.cards.txt`
   — the 19-move card table, and the credit for the 19-move bound.

   The 19-move construction and its card certificate are the work of
   **shjvandekamp**: `shjvandekamp/math@64e7eb1de4` (2026-10-15T10:59:29Z),
   `topics/snaky/certificate/snaky19.cards.txt`, 3,468 cards, sha256
   baf8774e1fc6eea60b1756437e8b3caae0ede5e001b10c0c3787aab51840782e.  It is
   public, dated nineteen days before this package, and is published in the
   `snaky-cards-txt-v1` format that reaches us through gotrevor from Sieben's
   card sequence (item 2).

   Our table is assembled from the same two public catalogs — the 20-move
   catalog and the 15x15 catalog — and re-tallies them rather than transcribing
   any existing file: 1,662 + 1,654 + 153 = 3,469 cards.  The card-by-card
   comparison against their certificate, including where it differs, is in
   bigospeedrun/verifier#142.  It is not a copy of their file; but it is also
   not an independent discovery of the bound, and this package does not claim to
   be one.

   **Correction.**  Earlier revisions of `Submission/CardTable19.lean` attributed
   this table to "Nándor Sieben / snaky19 construction".  That was wrong.
   Sieben's construction is the 20-move sequence (item 2), not the 19-move one,
   and this repository's own audit
   (`auto-research/audits/2026-10-23-ptweezy-snaky-19-move-lean-audit/NOTICE.md`
   in bigospeedrun/verifier) already attributed the 19-move result to
   `shjvandekamp/math`.  The credit line has been replaced accordingly.

Everything is Apache-2.0 (see LICENSE).  The bound-19 card certificate is
referred to, not vendored; its own repository states no license, so no license
is asserted over it here.
