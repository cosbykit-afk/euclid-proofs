# Book 14 — claim-by-claim evaluation (trig-cumulative campaign)

**Source book proof file:** `~/workspace/euclid_work/books/book14_proof.md`
**Rewrite page:** `~/workspace/r-theory-rewrite/book14/index.html`
(*Book 14 — Two-Fermion Mass Geometry and the Spinor Bridge*;
sections 14.0–14.XIII, matching the proof file's inventory item for item —
checked: all Part II theorem/corollary/proposition/negative labels on the
page map onto the inventory's 24 rows.)
**Evaluated:** 2026-09-22.

**Verification method:** every proof in `book14_proof.md` §C was restated
and re-derived in full here; every proof step feeding a folded principle
was additionally recomputed independently (sympy/numpy check script in the
workflow scratch: 17 checks, exit 0, all OK — the 14.II.T1 and 14.III.T1
numerators, the 14.III.T2 inversion, the 14.IV exact num/den factors, the
14.VI.C1 rewrite and its derivative, the 14.V.T1 limit and half-angle form,
the spin-1 expectations at five angles, the σᵢ⁽²⁾ = Jᵢ lift rule on five
random Hermitian K, and the Q_xz orthogonality witness). No proof step
failed or timed out.

## Claim table

| # | Claim (restated) | Verdict | Scope | Folded-in? | Notes |
|---|---|---|---|---|---|
| 1 | 14.I.T1: `q_m = tanh(λ_m/2)`; inverse `m₁/m₂ = (1+q_m)/(1−q_m)` | proof sound (tanh from exp defs; algebra exact) | PROVED | yes → **P17** | hyperbolic half-angle + inversion |
| 2 | 14.I.C1: `cosh λ_m = (1+q_m²)/(1−q_m²)`, `sinh λ_m = 2q_m/(1−q_m²)` | proof sound (substitution + expansion exact) | PROVED | yes → **P18** | |
| 3 | 14.I.C2: `tanh η = 2q/(1+q²)`, `sech η = (1−q²)/(1+q²)`, `tanh²+sech²=1` with `q=tanh(η/2)` | proof sound | PROVED | yes → **P19** | seed double-angle lineage (hyperbolic instance of P0's Lemma 1) |
| 4 | 14.II.P1: `p₁·p₂ = m₁m₂ cosh η`, `s = m₁²+m₂²+2m₁m₂ cosh η` | imported, not proved | ST (ASSERTED) | no | kinematics import; its exact algebraic consequence `s/(2m₁m₂)=cosh λ_m+cosh η` is used as the premise of P21 |
| 5 | 14.II.T1: `s/(4m₁m₂) = (1−q_m²q_v²)/((1−q_m²)(1−q_v²))` | proof sound | PROVED (conditional on the P1 import) | yes → **P21** | genuine two-cosh hyperbolic identity, exact given the premise |
| 6 | 14.II.N1: no mass-only rule determines relative velocity/dynamics | correctly scoped negative | ASSERTED | no | manuscript scoping declaration; no trig content |
| 7a | 14.III.E1 math: `η=iθ` sends `cosh η ↦ cos θ = (1−u²)/(1+u²)`, `u=tan(θ/2)` | proof sound | PROVED | yes → **P20** | circular half-angle rational form |
| 7b | 14.III.E1 physical caveat: continuation is mathematics, not dynamics | correctly scoped | ASSERTED | no | kept out of P20 |
| 8 | 14.III.T1: `M²/(4m₁m₂) = (1+q_m²u²)/((1−q_m²)(1+u²))` as `q_v²→−u²` | proof sound | PROVED | yes → **P22** | hyperbolic/circular bridge formula |
| 9 | 14.III.T2: `u² = [(m₁+m₂)²−M²]/[M²−(m₁−m₂)²]`, invertible both ways | proof sound | PROVED | no | pure algebraic coordinate inverse of P22; no trig content beyond P22 |
| 10 | 14.IV exact `u² = B[2(m₁+m₂)−B]/[(2m₁−B)(2m₂−B)]`; weak binding `u² = B/(2μ)+O(B²)` with monotone R(B) | proof sound (factorization + Cauchy-bound derivative exact) | PROVED | no | mass algebra and an asymptotic expansion; no trig content |
| 11 | 14.IV conditional Coulomb check `u ≈ Zα/(2n)` | book's own NC report (5.2e-06 relative); not re-run here | CHECKED | no | conditional on the imported Coulomb law (ST); not a trig identity |
| 12 | 14.IV.N1: binding is independent data | correctly scoped negative | ASSERTED | no | manuscript scoping declaration |
| 13 | 14.V.T1: heavy-source limit `u² → (m₂−E)/(m₂+E) = tan²(χ_E/2)`, monotone decreasing | proof sound (limit + derivative exact) | PROVED | no | monotone mass limit; its trig kernel is the half-angle identity already in P20/P23 |
| 14 | 14.V.P1: Dirac–Coulomb `\|G/F\|² = (m₂−E)/(m₂+E)` on circular branch | imported, not proved | ST (ASSERTED) | no | physics import |
| 15 | 14.V.T2: `u = \|G/F\| = sxp(χ_E)` by transitivity, conditional on P1 | proof sound | PROVED (conditional) | no | transitivity of two half-angle constructions; no new trig identity |
| 16 | 14.V.N1: no extension to excited radial states | correctly scoped negative | ASSERTED | no | manuscript scoping declaration |
| 17 | 14.VI.T1: `M²/(m₁+m₂)² = ⟨χ_u\|K_m\|χ_u⟩` | proof sound | PROVED | no | operator identity (linear algebra); its trig content is C1 → P23 |
| 18 | 14.VI.C1: `(1+q_m²u²)/(1+u²) = (1+q_m²)/2 + (1−q_m²)cos(2α)/2`, `d/dα = −(1−q_m²)sin(2α)` | proof sound | PROVED | yes → **P23** | double-angle Fourier form |
| 19 | 14.VII.T1: `cos(2θ_m) = q_m = tanh(λ_m/2)`, `sin(2θ_m) = √(1−q_m²) = sech(λ_m/2)` | proof sound | PROVED | yes → **P24** | hyperbolic/circular double-angle bridge |
| 20 | 14.VII.D1: `ν₂(χ_m) = (m₁,√(2m₁m₂),m₂)^T/(m₁+m₂)` | proof sound | PROVED | no | Veronese coordinate formula (projective algebra), not trig |
| 21 | 14.VII.CL1: Veronese conic does not by itself derive three generations | correctly scoped clarification | ASSERTED | no | manuscript clarification |
| 22 | 14.VIII.T1: `⟨Φ\|K⁽²⁾\|Φ⟩ = ⟨χ\|K\|χ⟩` for `Φ = χ⊙χ`, general K | proof sound (analytic, from D8) | PROVED | no | general linear-algebra identity; no trig content |
| 23 | 14.VIII: `K_m⁽²⁾ = diag(1,(1+q_m²)/2,q_m²)`; `⟨Φ_u\|J_z\|Φ_u⟩ = cos(2α)`, `⟨Φ_u\|J_x\|Φ_u⟩ = sin(2α)` | proof sound | PROVED | yes → **P25** (spin-1 expectation identities only; the diagonal `K_m⁽²⁾` form is linear algebra, not folded) | |
| 24 | 14.IX lift rule `K⁽²⁾ = k₀I + ½kᵢJᵢ` (`σᵢ⁽²⁾ = Jᵢ` entry by entry); T1 one-body lift image exactly `1⊕3`, quadrupole `5` absent (conditional on standard `1⊕3⊕5`, ST) | proof sound | PROVED (conditional) | no | representation theory, not trig |
| 25 | 14.X–14.XIII, 14.0: empirical-control ladder, `Δ_op(Book 14) = ∅`, closure, retirement/handoff | correctly scoped | ASSERTED | no | status declarations |

## Per-book counts

| Scope | Count | Rows |
|---|---|---|
| PROVED | 16 | 1, 2, 3, 5 (conditional), 7a, 8, 9, 10, 13, 15 (conditional), 17, 18, 19, 20, 22, 23 |
| CHECKED | 1 | 11 (book's own NC report; Coulomb law imported ST; not re-run here) |
| ASSERTED | 8 | 4 (ST), 6, 7b, 12, 14 (ST), 16, 21, 25 |
| INCOMPLETE | 0 | — |

Totals: 16 + 1 + 8 + 0 = 25 (the 24-row inventory with 14.III.E1 split into
its proved mathematics and its asserted physical caveat). Every analytic
claim the book tags CP is proved in full; nothing the book tags CP was left
at ASSERTED; nothing was promoted to PROVED beyond what the proofs derive.
ST imports are counted under ASSERTED with their ST label kept.

## Folded principles

Nine new Principles added to `cumulative_trig_proof.md`: **P17–P25**
(P17 tanh half-angle/inverse; P18 cosh/sinh in half-angle tangent;
P19 tanh double-angle/sech; P20 circular half-angle rational form;
P21 two-cosh sum, conditional on the ST import; P22 bound-state
continuation form; P23 double-angle Fourier form + derivative;
P24 mass double-angle bridge; P25 spin-1 Veronese expectation identities).
All PROVED (P21 conditional on the named import). Dependency order
respected: each cites only earlier Principles and definitions. No Euclid
*Elements* proposition is a premise of any folded principle (the 13 ledgers
were grepped; none supplies hyperbolic identities) — stated plainly in the
chapter, consistent with the book proof file's documented boundary.

## Not folded — plain reasons

- **Imports (ST):** rows 4, 14 — stated, not derived; cannot found a
  proved principle.
- **Manuscript negatives/declarations (ASSERTED):** rows 6, 7b, 12, 16,
  21, 25 — no trigonometric content; scoping kept.
- **Pure algebra / non-trig mathematics:** rows 9 (coordinate inverse),
  10 (mass algebra + asymptotic expansion), 17 (operator identity),
  20 (projective algebra), 22 (linear algebra), 24 (representation
  theory) — proved, but no identity about trig functions, angles, or
  circular measure.
- **Conditional physics check (CHECKED):** row 11 — not a trig identity.
- **Physics limits with no new trig kernel:** rows 13, 15 — the
  half-angle identity they rest on is already P20/P23.

status: complete
