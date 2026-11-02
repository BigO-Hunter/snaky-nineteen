NOTICE — provenance and licensing for the SNAKY Bound-20 package

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

Everything is Apache-2.0 (see LICENSE).
