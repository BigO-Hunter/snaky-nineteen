# Composition-Shaped Gap Analysis: Snaky 18 (scouted 2026-11-06)

## The prime-gaps anatomy, applied

Prime-gaps 246 = (a) published library (PrimeGapsLib) + (b) proven deep lemma
(kimihiro64's BV) + (c) our assembly. For Snaky's next row (18):

**(a) Library — EXISTS, and it is ours.**
`darkhipo/snaky-nineteen` is a table-agnostic bridge, proven end-to-end twice:
vendored gotrevor card world (`Game/Cards/CardsSound/Bounded/Controls`), kernel-checked
card table via `decide +kernel` (no native_decide), plane bridge G1/G2 + `Bound`
bookkeeping pack G3, byte-for-byte statement vendoring with sha256 re-check.
Swapping `CardTable19.lean` → `CardTable18.lean` is a ~day-scale task
(our Nov 3 board post: "proven end-to-end for 20 in ~10 hours from activation").

**(b) Deep lemma — MISSING. Nobody public has an 18.**
- GitHub repo search "snaky 18 moves": 0 results. No claimed-18 row on the board.
- **Key signal:** shjvandekamp/math README, "Open work" section (line 155):
  "Snaky: an 18-move strategy, and the empty 14×14 and 10×10 board-size questions."
  The only person who has ever shaved a move (20→19, via Sieben-extension + Trevor
  Morris tactics) has **18 on his own declared roadmap**. It is open work, not done.
- Our own measured evidence (board post Nov 3, `inc19-probe` branch of snaky-twenty):
  the Gen17 card table is exactly tight at root height 20; the 19 required
  shjvandekamp's material — 3 frontier positions (cards 1036/1608/1701) needing
  re-proofs at h=16; naive reduced AND-OR search measured-infeasible (~1e17–1e18
  nodes). **18 is strictly deeper. From-scratch agent search is a NO-GO** by our
  own measurement, not a guess.

**(c) Assembly — ready.** Table-agnostic; hours once a certificate exists.

## Where the pieces can come from

1. **shjvandekamp completes his 18** (most likely single source; he has the methods
   lineage: Sieben 20 + Morris tactics → 19; 18 = one more shave).
2. A third party discovers an 18 (nothing in public signals this today).
3. Us from scratch: ruled out by the h=16 frontier measurements.

## Verdict

**(b)-variant: route-open, top row held, composition buildable, deep lemma not yet in
the world.** This inverts the prime-gaps situation — there is no gate to beat. The
playbook that DOES transfer is **watch + ready-bridge**: the bridge already exists;
what needs standing is a tripwire and a day-one license/collab posture
(the #8 arc showed credit-first treatment works and was honored by nmamano's #142 ruling).

## What would change the verdict

- shjvandekamp/math: any commit/README change in `topics/snaky/` or "Open work"
  dropping the 18 line → re-scout within hours, open collab thread same day.
- Board: any Claimed-18 row or new snaky repo by a third party → bridge offer.
- Verifier: any new statement parameterization or profile change → re-vendor statement.

## Cost control

Pre-positioning cost here is ~zero: the machinery is already public and proven.
No new build should start absent tripwire (a) or (b).
