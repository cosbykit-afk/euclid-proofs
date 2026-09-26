# Book 10 extension proofs — R Theory, "Quantum Kinematics and the Measurement Boundary"

**Source:** `~/workspace/r-theory-rewrite/book10/index.html` (Volume II, Book 10 rewrite;
restructured audit; every theorem/import/contract/status label below comes from the
manuscript page, no mathematics added).
**Method:** definitions first, dependency order, nothing used before it is proved.
Scope labels: PROVED / CHECKED / ASSERTED / INCOMPLETE (see standing rules).
**Generated:** 2026-09-22, by workflow agent `euclid-book-proofs` (book-10).

## 0. Citation availability (disclosed limitation)

This worker's filesystem contained **no** `~/workspace/euclid_work/books/seed_double_angle.md`
and no `book0_proof.md` .. `book6_proof.md` at write time (parallel campaign phases had not
landed). Where Book 10 rests on Volume I material, the dependency basis cited is the
rewrite page's own §6 dependency audit, which quotes the Volume I theorem ledger
(`~/workspace/wolfram/theorem_ledger.md`) verbatim. Pure-mathematics identities
re-stated below (rapidity ratio identities, ground-sector constant, wedge scaling,
meridian rank) were independently re-verified by this worker's run
(`/tmp/b10_check.py`, exit 0, all errors ≤ 4.3e-15). The campaign seed's double-angle
identity is cited as stated in the task brief, not re-read from the file.

Euclid's *Elements* citations refer to the inventoried
`~/workspace/euclid_work/ledger/book1_ledger.md` .. `book13_ledger.md`. Per the
book10 ledger §7 (verified negative result: full-text search of rewrite books 0–22
for incommensurable/apotome/bimedial/medial found zero relevant hits), **no
proposition of Euclid's Book 10 is extended by any R Theory claim** — R Theory takes
the real continuum as declared substrate (P4.1) rather than constructing irrationals
à la 10.1–10.115. No-Euclid-wholesale boundary (4.X.H): wholesale inheritance of the
Elements is not claimed; only the cited items below enter.

## 1. Definitions

- **D1 (chart).** A (real) chart on a set M is an injective parametrization of a
  nonempty open subset by real coordinates; the number of coordinates is the local
  (real) dimension where the chart is differentiable with constant full rank.
- **D2 (CP¹ chart).** The complex projective state space ℂP¹ has the local chart
  (x, φ) with ψ = (cos(x/2), e^{iφ} sin(x/2))ᵀ: two real local coordinates,
  x the population (meridian) coordinate, φ the relative phase.
- **D3 (Projection meridian).** The one-parameter curve q = tan(x/2) (the reciprocal
  half-angle coordinate `sxp`), x ∈ (0, π): one real degree of freedom. dq/dx =
  1/(2cos²(x/2)) > 0 on (0, π), so the map is an injective immersion — a genuine
  meridian, rank 1 everywhere.
- **D4 (physics import).** A named standard result from outside the R Theory chain,
  admitted as a conditional premise: 10.III.P1 (free Dirac equation + positive-energy
  spinors), 10.IV.P1 (radial Dirac–Coulomb system with components F, G),
  10.VII.P1 (left-chiral projector + V–A structure).
- **D5 (projection contract).** A declared identification of R Theory coordinates with
  an imported structure, granted as axiom, not proved: 10.III.PC1 identifies q = sxp
  with the rapidity chart.
- **D6 (negative theorem).** A delimiting statement about the dependency chain: that
  no derivation of X was supplied by the chain (not a proof that no derivation can
  exist). 10.VII.N1, 10.VIII.N1 are of this form.

## 2. Claim inventory (from the book page)

| # | Claim | Book label | Worker scope |
|---|---|---|---|
| C1 | 10.II.T1 — projective-rank obstruction: ℂP¹ needs 2 real local coordinates; the meridian supplies 1 | checked proof | **PROVED** |
| C2 | 10.II.C1 — q alone selects a 1-dim subfamily or supplies a silent phase rule | checked proof | **PROVED** |
| C3 | 10.III.P1 — free-Dirac import; ratio identities pc/(E+mc²) = √((E−mc²)/(E+mc²)) = tanh(α/2) | standard imported theorem | import (identity identities **CHECKED** by this run) |
| C4 | 10.III.PC1 — rapidity-contract identification q = sxp | assumption/axiom (contract) | **ASSERTED** (declared contract) |
| C5 | 10.III.T1 — exact free-spinor ratio correspondence, conditional on C3+C4 | completed numerical check | **CHECKED** |
| C6 | 10.IV.P1 — radial Dirac–Coulomb import; ground-sector constant ratio \|G/F\| = Zα/(1+γ) | standard imported theorem | import (constant form **CHECKED** by this run on the analytic ground state) |
| C7 | 10.IV.T1 — ground-sector half-angle correspondence \|G/F\| = tan(x/2), conditional on C6 | completed numerical check | **CHECKED** |
| C8 | 10.IV.N1 — no universal constant half-angle for excited states (n=2, κ=−1 confirmed) | manuscript assertion, not independently verified | **ASSERTED** |
| C9 | 10.V.T1 — Prüfer completion: F = A cos Θ, G = A sin Θ regular through nodes | standard imported theorem | import (reconstruction exact; this run does not re-verify regularity) |
| C10 | 10.VI.T1 — shared symplectic form ω_spin = 4·dF∧dG; du∧dv = 2·dF∧dG for (u,v) = (F−G, F+G) | completed symbolic check | **PROVED** (exact algebra; claim noted close to definitional) |
| C11 | 10.VII.P1 — left-chiral projector + V–A import | standard imported theorem | import |
| C12 | 10.VII.N1 — chirality not selected upstream (no P_L/P_R derivation in the chain) | manuscript assertion, not independently verified | **ASSERTED** |
| C13 | 10.VIII.N1 — representation does not imply measurement ontology | manuscript assertion, not independently verified | **ASSERTED** |
| C14 | 10.IX — closure; Δ_op(Book 10) = ∅ | manuscript assertion | **ASSERTED** |

## 3. Proofs in dependency order

### 3.1 Meridian rank vs. chart rank (C1, C2) — PROVED

From D3: dq/dx = 1/(2cos²(x/2)) is finite and nonzero on all of (0, π) — so the
meridian map x ↦ q is an immersion; its image is a one-dimensional submanifold
(local rank exactly 1; this run verified dq/dx finite and nonzero on a 20,001-point
grid of (0, π)). From D2: the (x, φ) chart of ℂP¹ has two real coordinates with
independent partial derivatives, so local real dimension 2.

A map of constant rank 1 cannot be locally surjective onto a 2-dimensional chart
domain: in a neighborhood where the chart is a diffeomorphism to an open set of ℝ²,
the image of a 1-parameter immersion is 1-dimensional. Hence the meridian cannot
cover the chart: the generic projective state ψ(x, φ) genuinely needs the
independent relative phase φ. ∎ (PROVED — exact dimension/rank argument; the book's
own SVD check (rank 1 vs rank 2) is the numerical witness of the same fact.)

**C2 corollary — PROVED.** By C1, writing ψ with q alone fixes x and leaves φ
undetermined; either φ is left free (a one-dimensional subfamily of ℂP¹) or some
phase rule is imposed. Imposing a rule is an extra declaration — by D5 a contract,
not a theorem squeezed from the meridian. ∎

Euclid contact: none beyond definitional chart theory; no Elements proposition is
used. (The book-10 ledger §7 records the verified negative: no R Theory claim
extends any of 10.1–10.115.)

### 3.2 Free-Dirac ratio identities within the import (C3 identities) — CHECKED

C3 is admitted as a standard import (D4); what this worker checks independently is
the *algebraic content* of its ratio identities. On the mass shell
E = mc²cosh α, pc = mc²sinh α:

pc/(E+mc²) = tanh(α/2) — identity via sinh α/(cosh α + 1) = tanh(α/2);
pc/(E+mc²) = √((E−mc²)/(E+mc²)) — by E²−p²c² = m²c⁴.

This run (`/tmp/b10_check.py`, exit 0): 500 random rapidity pairs,
max |pc/(E+mc²) − tanh(α/2)| = 3.3e-16;
max |√((E−mc²)/(E+mc²)) − pc/(E+mc²)| = 4.3e-15.
The identities are exact trigonometry; the measured errors are floating-point
roundoff. ∎ (CHECKED — the identities, not the Dirac theory itself, which remains
a named import, i.e. ASSERTED as premise.)

### 3.3 The rapidity contract (C4) — ASSERTED

The identification of the inherited coordinate q with the rapidity chart (PC1) is
declared on the book page as a contract "not a derivation." In Euclid's register:
an axiom granted by stipulation, proved by nothing. Any dependence on C4 is
explicitly conditional; the contract's content cannot exceed its statement. ∎

### 3.4 Exact free-spinor ratio correspondence (C5) — CHECKED, conditional

Given C3 (import) and C4 (contract), set x = 2·arctan(r) with r = pc/(E+mc²).
Then tan(x/2) = r is an exact inverse-of-inverse identity on (0, π) — the
double-angle seed's inversion, exactly established. Under the declared
identification q = sxp, the reciprocal coordinate reads the relativistic spinor
ratio. What is *not* established (book states this explicitly): the Dirac equation
itself, the mass shell, spin one-half, or any interpretation of the components.
Those remain behind the import C3. ∎ (CHECKED — conditional identity; the
condition is carried, not discharged.)

### 3.5 Ground-sector constant ratio (C6 import content) — CHECKED

C6 is a standard import (D4). Its checkable content — that the imported circular
Dirac–Coulomb ground state has r-independent G/F = −Zα/(1+γ) — was re-verified by
this run on the analytic ground state (Z=1, α=1/137.035999177):
γ = √(1−(Zα)²) = 0.9999733739683032; |G/F| = Zα/(1+γ) = 0.003648724857697569;
x = 2·arctan(|G/F|) = 0.007297417331534783 rad; |tan(x/2) − |G/F|| = 0.0.
∎ (CHECKED — on the analytic imported ground state; the import itself remains
ASSERTED as premise.)

### 3.6 Ground-sector half-angle correspondence (C7) — CHECKED, conditional

From C5's checked conditional identity tan(x/2) = r and the C6 checked constant
ratio r = |G/F|: |G/F| = tan(x/2) = sxp(x) at the fixed half-angle
x ≈ 0.007297 rad. The chain is: identity (checked) applied to an imported
constant (checked on the analytic ground state). ∎ (CHECKED — conditional on C6.)

### 3.7 No universal constant half-angle for excited states (C8) — ASSERTED

The book page labels this a manuscript assertion "not independently verified,"
with the n=2, κ=−1 case numerically confirmed in its own audit
(F has one node at r ≈ 274; G/F non-constant with a pole at the node; no fixed
angle fits). This worker did not re-run the radial-Dirac integrator, so the
conclusion is reported at the book's own scope: ASSERTED. Precision note (from the
book, §8): circular excited states (n_r = 0, e.g. 2P_{3/2}) have constant but
*state-dependent* G/F — the universal fixed-angle law fails for them too. ∎

### 3.8 Prüfer completion (C9) — import; reconstruction exact

Standard ODE theory (D4): F = A cos Θ, G = A sin Θ with P = A² is a smooth
reparametrization wherever (F, G) is smooth; tan Θ = G/F wherever finite, and the
angle is regular through sign changes because (A, Θ) are polar coordinates of the
(F, G) plane — a definitional fact, no singularity at a node. The book's audit
verified reconstruction to 1e-9 on both states and min A² > 0 on its grids;
this worker does not re-verify regularity numerically. ∎ (standard import;
book's regularity check not re-run here.)

### 3.9 Shared symplectic form (C10) — PROVED (exact)

For (u, v) = (F−G, F+G): Jacobian matrix [[1, −1],[1, 1]], determinant = 2 exactly
(this run: det = 2.0). Hence du∧dv = 2·dF∧dG and 4·dF∧dG = 2·du∧dv, exact. ∎
(PROVED — exact algebra. Scope note retained from the book: the claim's
substantive content is close to definitional, since all four charts are functions
on the same (F, G) plane; the manuscript disclaims any quantum commutator, ℏ,
canonical quantization, or path-integral measure — and so does this proof.)

### 3.10 Chirality firewall (C12) — ASSERTED

Given D6: the dependency chain of this book (C1–C10) contains no derivation
selecting P_L over P_R. That is a true observation about the chain as built —
the symmetric carrier admits the representation of left-chiral weighting (after
import C11) but supplies no selection mechanism. It is not a proof that no such
derivation could exist. ∎ (ASSERTED — structural observation, correctly scoped by
the book to the chain.)

### 3.11 Measurement firewall (C13) — ASSERTED

Given D6: nothing in C1–C10 derives the Born rule, collapse, decoherence,
uncertainty relations, entanglement protocols, path-integral measure, Grassmann
variables, fermionic statistics, the spin-statistics theorem, a QFT vacuum, or
physical spin-one-half dynamics. Hence no nonempty operational prediction set
Δ_op follows from the representation correspondence alone: a normalized complex
vector may be compared with a quantum state only after a quantum-state contract is
declared; squared magnitudes become probabilities only after the Born rule is
imported. ∎ (ASSERTED — true statement about the absence of a supplied derivation,
not an impossibility proof; the book's §8 states this scoping explicitly.)

### 3.12 Closure (C14) — ASSERTED

The book retains: C1/C2 (proved), C3/C6/C9/C11 (imports), C5/C7 (checked
conditional correspondences), C8 (asserted), C10 (proved exact scaling),
C12/C13 (asserted firewalls). No Born rule, collapse law, QFT ontology,
fermionic statistics, or new spin dynamics is obtained — consistent with the
firewalls. Δ_op(Book 10) = ∅ is status bookkeeping, consistent with C12/C13. ∎

## 4. New axioms/assumptions beyond Euclid + seed + earlier books

Only items introduced by Book 10 itself (earlier-book axioms A0.1/A0.2, P4.1,
real carriers, the reciprocal coordinate `sxp` are inherited and not re-listed):

1. **A10.1 — Projection Contract 10.III.PC1.** Declared identification of the
   inherited coordinate q = sxp with the rapidity chart. ASSERTED (contract);
   every claim downstream of it (C5) is conditional on it.
2. **Import I1 — 10.III.P1.** Free Dirac equation + positive-energy spinors
   (named standard import; its ratio identities CHECKED §3.2, the theory itself
   ASSERTED as premise).
3. **Import I2 — 10.IV.P1.** Radial Dirac–Coulomb system with F, G (named standard
   import; constant-ratio content CHECKED §3.5 on the analytic ground state).
4. **Import I3 — 10.VII.P1.** Left-chiral projector + V–A structure (named standard
   import, used only for the comparison in C12).

No new Euclidean postulate, no new common notion, and no extension of any
Elements Book 10 proposition is involved (ledger book10_ledger.md §7 negative
result). The real continuum used by the analysis is the declared substrate P4.1,
inherited from Book 4 — explicitly *not* derived à la Euclid 10.1–10.115.

## 5. Counts

- PROVED: 4 (C1, C2, C10, plus the exact trig/ratio identities underpinning C5 —
  counted as proved identities inside the checked claims; claim-level count: C1, C2, C10)
- CHECKED: 4 (C3 identities, C5, C6 constant-ratio content, C7)
- ASSERTED: 6 (C4, C8, C9-import, C11-import, C12, C13, C14 — imports C9/C11 counted
  as asserted premises)
- INCOMPLETE: 0 — every check this worker attempted ran to completion
  (`/tmp/b10_check.py`, exit 0, no timeouts, worst error 4.3e-15).

Claim-level tally: proved 3 (C1, C2, C10) · checked 4 (C3-id, C5, C6-ratio, C7) ·
asserted 7 (C4, C8, C9, C11, C12, C13, C14) · incomplete 0.
