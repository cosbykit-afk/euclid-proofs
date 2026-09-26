# Book 21 — claim-by-claim table (trig-cumulative campaign)

**Book:** 21 — Fermion Composition, Color Closure, and Bound-State Geometry
(Volume 0).
**Source:** rewrite page `~/workspace/r-theory-rewrite/book21/index.html`
(principal theorems). **No `book21_proof.md` exists** (the earlier campaign
covered Books 0–20 only); every claim below is sourced from the rewrite
page, restated and verified from the page's content.
**Evaluated:** 2026-09-26. **Euclid boundary:** no proposition of Euclid's
*Elements* is a premise of any claim below (the page invokes none; the only
"Euclidean" occurrence is the phrase "Euclidean metric" for the A₂
realization layer). No ledger verification was therefore required.

## Claims

| # | Claim (restated) | Verdict | Scope | Folded in? | Notes |
|---|---|---|---|---|---|
| B21.1 | Composition firewall: Sym(V_A⊗V_B) = [Sym(V_A)⊗Sym(V_B)] ⊕ [Alt(V_A)⊗Alt(V_B)]; locally visible subsystem coordinates need not determine the full composite state | PROVED | PROVED | No — linear algebra, not a trig identity | Verified by dimension count: both sides have dimension mn(mn+1)/2 for dim V_A=m, dim V_B=n; the two summands are orthogonal subspaces of the symmetric sector. |
| B21.2a | Declared extension V₃ = ℂ³ (not derived from Book 0) | ASSERTED | ASSERTED | No — declaration | The book labels it DECLARED itself; a declaration cannot found a principle. |
| B21.2b | Three-state closure: from declared V₃, centered weights form an equilateral triangle in the sum-zero plane; pairwise differences give the A₂ root system (Cartan [[2,−1],[−1,2]], six roots, regular hexagon); one su(2) + one bridge closes to su(3) (minimal within the declared candidate class); the tetrahedral metric G=½(I+J) restricts to a scalar multiple of the Euclidean metric on the A₂ plane (compatible, not foundational) | PROVED | PROVED (given the declared V₃) | No — Lie algebra / root-system geometry, not a trig identity | Standard: weights e_i − ⅓Σe_j, differences e_i−e_j = 6 roots; simple roots generate su(3). The weight angles (30°, 150°, 270°) are representation coordinates, firewalled by the book itself as non-spatial. |
| B21.3 | Triadic color closure, conditional on the QCD import: 3⊗3̄ = 1⊕8, 3⊗3⊗3 = 1⊕8⊕8⊕10, ε-contraction exactly color-invariant; color/anticolor hexagon interlaces the root hexagon at an exact 30° offset. Obstruction kept: singlet representation theory does not derive confinement, couplings, or a Hamiltonian | PROVED | PROVED-conditional (asserted QCD import: quarks in 3, antiquarks in 3̄, gluons in 8, su(3) connection, plus the V₃↔color-carrier projection contract) | No — representation theory, not a trig identity | Dimension checks: 3·3 = 9 = 1+8; 27 = 1+8+8+10. The obstruction is a retained negative about what the exhibited tensors prove. |
| B21.4 | Two-fermion invariant: from supplied masses and ordinary special relativity, s = 2m₁m₂(cosh λ_m + cosh η) with λ_m = ln(m₁/m₂), q_m = tanh(λ_m/2), q_v = tanh(η/2); equivalently s/(m₁m₂) = [R(q_m)+R(q_m)⁻¹] + [R(q_v)+R(q_v)⁻¹], R(q) = (1+q)/(1−q). Guards: q_m, q_v are independent physical data; m₁/m₂ = R(q_m) is a coordinate change, not a mass-generation mechanism | PROVED | PROVED (exact; SR is background physics, masses supplied) | No — trig kernel already registered | R(q) = (1+q)/(1−q) is P30's Möbius map Q₊ in the q variable; R(q)+R(q)⁻¹ = 2(1+q²)/(1−q²) = 2cosh λ_m is a two-line corollary of P49; hence s/(2m₁m₂) = cosh λ_m + cosh η is exactly P51's premise form. Nothing new. Sanity: 2m₁m₂cosh λ_m = m₁²+m₂², so s = m₁²+m₂²+2m₁m₂cosh η is the standard 1+1 invariant. |
| B21.5 | Bound-mass coordinate: on the declared analytic branch η → iθ, u = tan(θ/2), u² = [(m₁+m₂)²−M²]/[M²−(m₁−m₂)²], M² = (m₁−m₂)² + 4m₁m₂/(1+u²); weak binding u² = B/(2μ) + O(B²); heavy-source limit u² → (m₂−E)/(m₂+E) | PROVED | PROVED (exact algebra; the expansion/limit are analysis) | No — u = tan(θ/2) is P19's Weierstrass form; the rest is algebra/analysis, not a trig identity | Verified: the two displayed forms are equivalent (cross-multiplication gives 4m₁m₂ + (m₁−m₂)² = (m₁+m₂)²); the weak-binding expansion and the m₁→∞ limit check out term by term. |
| B21.6 | Independent coordinate convergence: on the n_r = 0, κ < 0 heavy-source circular branch of the imported Dirac–Coulomb theory, |G/F|² = (m−E)/(m+E), so u_pair = |G/F| = sxp(x) exactly, from two independent routes with no fitted mass ratio. The n_r > 0 obstruction (ratio runs with radius; one global u cannot reconstruct a generic excited radial spinor) is part of the theorem | PROVED | PROVED-conditional (asserted imports: point-Coulomb Dirac equation; radial Dirac–Coulomb paper's circular-state theorem; declared state family) | No — trig content is P19/P17 under the import | |G/F| = tan(θ/2)-type half-angle tangent is P19's Weierstrass form; sxp(x) = tan(x/2) on the sine channel is P17. The convergence is the equality of two routes, conditional on the imports — not a new trig principle. |
| B21.7 | Verified numbers (recomputed 2026-09-19 from frozen inputs, cited): hydrogen q_m ≈ 0.99891135885, u_H(1S) ≈ 0.003648720323 with α/2 < u_H < u_C; deuteron B_d ≈ 2.22456637 MeV, q_m ≈ 0.00068873505, u_d ≈ 0.0487186123; muonium q_m ≈ 0.99037 | CHECKED | CHECKED (cited recomputation, not re-run per proof-over-sampling discipline) | No — empirical numbers, not a trig identity | — |
| B21.8a | Frozen failure: 81/32 is not exact — R_β = (m_n−m_p)/m_e ≈ 2.53098858276 vs 81/32 = 2.53125, residual ≈ −133.6 eV | CHECKED | CHECKED (numerical comparison) | No — negative result, not a trig identity | Must not be presented as an exact mass formula (the book's own guard). |
| B21.8b | Other frozen failures: fifth-lattice proximity is not mass quantization; closure defects are not musical commas; the order-five mass route failed | ASSERTED | ASSERTED (retained negatives, not re-derived here) | No — negatives, not trig | Inherited by any future flavor/mass program; may not be silently reversed. |
| B21.9 | Preregistration rule (constituent/bound-state/coordinate definitions, reference theory, provenance, uncertainty, Δ_op, failure criterion before testing a mass law) | ASSERTED | ASSERTED (methodology) | No — methodology, not a trig identity | — |
| B21.10 | Higher-carrier audit (E8(−24)): 248-direction reconstruction, zero-residual particle/mirror matching, su(2,3)⊕u(1)_Y centralizer, commuting SU(5) partner — cited to the project's Verification Ledger, not proved in this text; firewalled (no theorem of §§1–7 depends on it) | ASSERTED | ASSERTED (ledger-cited) | No — cited, not proved here | Cannot be stated as established until that ledger and its code are rerun. |
| B21.11 | Closure audit: Δ_op(Book 21) = ∅; null hypothesis C0 retained; color and mass architectures logically independent | ASSERTED | ASSERTED (the book's own conclusion) | No — meta, not a trig identity | — |

## Counts

- Evaluated: 13
- PROVED: 6 (B21.1, B21.2b, B21.3, B21.4, B21.5, B21.6 — three of them PROVED-conditional on named imports)
- CHECKED: 2 (B21.7, B21.8a)
- ASSERTED: 5 (B21.2a, B21.8b, B21.9, B21.10, B21.11)
- INCOMPLETE: 0
- New principles folded: **0** — every claim with trigonometric content is a corollary or restatement of already-registered principles (P17, P19, P30, P49, P51); the rest is Lie algebra, representation theory, analysis, empirics, imports, or negatives.

**status: complete**
