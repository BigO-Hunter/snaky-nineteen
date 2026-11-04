NOTICE — provenance and licensing for the SNAKY Bound-19/20 package

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


4. `Submission/CardTable19.lean` and `Submission/Gen19/*` — the 3,469-card
   19-move table, DERIVED from the 19-move certificate
   `topics/snaky/certificate/snaky19.cards.txt` in shjvandekamp/math @
   64e7eb1 (first committed 2026-10-15; that repository carries no license;
   used per the construction author's public attribution request,
   shjvandekamp/math#8 and bigospeedrun/verifier#142). Measured derivation
   delta: 3,409 of the author's 3,468 cards appear unchanged (cell content,
   pass and reply shapes; card numbering and within-card cell order
   ignored), 59 cards replaced, 1 card inserted (3,469 total).
   Construction authorship: shjvandekamp — the certificate itself combines
   Nándor Sieben's public 20-move strategy (1,662 cards), Morris's public
   15×15 strategy (1,653 cards) and 153 newly constructed cards, per the
   certificate's own provenance notes. The Lean card table (literals,
   lookup tree, kernel-checked justifications) and the verification
   packaging are this campaign's work.
Everything else is Apache-2.0 (see LICENSE). Item 4's underlying
certificate remains the construction author's; this package adds no
license to it.
