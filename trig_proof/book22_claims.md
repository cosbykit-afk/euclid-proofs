# Book 22 — claim-by-claim table (trig-cumulative campaign)

**Book:** 22 — Canonical Spin–Geometry and the Primitive Symplectic Atlas
(Volume 0).
**Source:** rewrite page `~/workspace/r-theory-rewrite/book22/index.html`
(principal theorems). **No `book22_proof.md` exists** (the earlier campaign
covered Books 0–20 only); every claim below is sourced from the rewrite
page, restated and verified from the page's content.
**Evaluated:** 2026-09-26. **Euclid boundary:** no proposition of Euclid's
*Elements* is a premise of any claim below (the page invokes none). No
ledger verification was therefore required.
**Standing note:** "promotion" of earlier results means restriction to a
specialized setting with reuse of existing proofs — a status-preserving
operation, never a status upgrade and never new evidence (the book's own
rule, kept).

## Claims

| # | Claim (restated) | Verdict | Scope | Folded in? | Notes |
|---|---|---|---|---|---|
| B22.1 | Imported machinery and declared contracts: radial coframe e^a (flat at η=0, defect δ_e = e^0−dr), torsion-free spin connection, Dirac spinor Ψ in the projected chart; contract C6a (radial two-component chart Ψ → (r,F,G,…)); contract C6b (F and G independent on open sets) | ASSERTED | ASSERTED (imports + declared contracts) | No — imports/contracts | The book labels these IMPORT/declared itself. |
| B22.2 | Obstruction: the spherical-to-Cartesian map is not a global diffeomorphism (origin and polar axis excluded) | PROVED | PROVED (negative) | No — differential geometry, not a trig identity | Standard: the map fails injectivity/regularity at r = 0 and on the polar axis. |
| B22.3 | C6a/C6b fix the *reading* of the geometry but not the *physical meaning* of F and G; importing the radial Dirac–Coulomb paper promotes the chart, never the book's own assumptions | ASSERTED | ASSERTED (methodological) | No — methodology | — |
| B22.4 | Prüfer canonical pair (exact conditional): the transport operator on (F,G) has exact zero trace, giving the radial invariant FF′ + GG′ = −A²/(2r); Prüfer angle Θ = arg(G+iF) and spin density A² = F²+G² form a canonical pair on the radial-spinor phase plane with symplectic form ω_spin = 4 dF∧dG, regular on open sets under C6a/C6b. Obstruction kept: does not derive the Dirac equation, spin-½, spin-statistics, or α | PROVED | PROVED-conditional (imported radial Dirac equations + C6a/C6b) | No — differential geometry of the (F,G) phase plane, not a trig identity | The page states the zero-trace input and the invariant as consequence; internal consistency verified: (A²)′ = 2(FF′+GG′) = −A²/r. The angle Θ enters only as a phase-plane coordinate; no identity about trig functions is proved. |
| B22.5 | Primitive symplectic atlas (the volume's strongest exact result): p_sxp = 2F², p_srx = −2G², p_cxp = (F−G)², p_crx = −(F+G)² are four Darboux-compatible charts on the same (F,G) plane with common one-form p_Q dQ = −2G dF + 2F dG and common symplectic form ω_spin = 4 dF∧dG; chart transition identities, reciprocal relations, and amplitude-ratio readings are exact; on the circular Dirac–Coulomb branch the charts cross-check the radial paper's spinor-ratio theorem | PROVED | PROVED (exact internal theorem; conditional only on the declared C6a/C6b chart and the imported radial dynamics) | No — a representation theorem in (F,G) variables, not a trig identity | The "reciprocal/complementary identities" are differential identities of the atlas charts, not identities about sin/cos/tan. The book states it changes no prediction of the imported theory. |
| B22.6 | Spherical defect reduction (conditional reconstruction): exact reduction of the imported first-order Einstein–Hilbert action in the defect variables (δ_e, δ_f, δ_ω) under declared regularization η²(r)dr on (r_UV,∞) and asymptotically flat falloff; on-shell defect action vanishes in the massless flat defect-free limit. Obstruction kept: does not derive the Einstein field equations, Newton's constant, or the mass parameter | PROVED | PROVED-conditional (imported first-order EH action + declared regularization/falloff contracts) | No — gravitational variational calculus, not a trig identity | — |
| B22.7 | Conditional channels: (a) gauge — radial electric charge as cyclic radial momentum p_Φ conjugate to the radial gauge phase (Maxwell dynamics and e imported); (b) rotation — angular momentum as p_Ω conjugate to frame dragging (imported Kerr channel); (c) spin (Einstein–Cartan) — axial contorsion exactly auxiliary, torsion solved algebraically for the spin current | PROVED | PROVED-conditional (respective imports: Maxwell, Kerr geometry, Einstein–Cartan) | No — representation of imported physics in canonical coordinates, not trig | None derives its import (the book's own guard). |
| B22.8 | Kerr/Kerr–Newman half-angle identities: on the imported Kerr geometry the horizon radii satisfy exact half-angle identities in the book's coordinates, extending to Kerr–Newman after the electromagnetic import; guards: valid on the declared regular domain (coordinate singularities excluded), consequences of the imported metric, no new black-hole physics | PROVED | PROVED-conditional (imported Kerr/KN geometry + declared chart domain) | No — conditional coordinate identities; the explicit formula is not stated on the rewrite page, so no trig identity could be verified or folded | What would close the formula gap: the half-angle identity as stated in the source T6 essay-book or the Kerr-geometry derivation. |
| B22.9 | Spherical-spin obstruction (the book's hardest negative): spherical symmetry forces the total spin current to integrate to zero over the sphere, so the canonical spin apparatus cannot be promoted to a theory of spin in the spherical sector | PROVED | PROVED (negative theorem) | No — symmetry argument, not a trig identity | Proof: a non-zero total spin vector would select a preferred spatial direction, contradicting rotation invariance of the spherically symmetric configuration; hence the integrated spin current vanishes. |
| B22.10 | Does-not-establish ledger (Dirac equation, spin-½, α, Coulomb, EFE, G, Maxwell, e, Kerr metric, EC coupling, masses, couplings, new observables — none derived); book closure Δ_op = ∅, C0 retained; forward boundary (C0 defeated only by a future Class-C model with a measurement contract). The source's Yang–Mills attribution is not repeated (absent from the cited text) | ASSERTED | ASSERTED (the book's own ledger/conclusions) | No — meta, not a trig identity | — |

## Counts

- Evaluated: 10
- PROVED: 7 (B22.2, B22.4, B22.5, B22.6, B22.7, B22.8, B22.9 — five of them PROVED-conditional on named imports/contracts)
- CHECKED: 0
- ASSERTED: 3 (B22.1, B22.3, B22.10)
- INCOMPLETE: 0
- New principles folded: **0** — the book's exact content is differential/symplectic geometry of the (F,G) phase plane and conditional reconstructions of imported physics; no claim yields a new identity, lemma, or exact relation about trigonometric functions, angles, or circular measure.

**status: complete**
