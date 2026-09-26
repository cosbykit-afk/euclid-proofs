# Book 7 — Classical Dynamics from the Certified Carrier: Extension Proofs

**Campaign:** Euclid book-proofs (`euclid-book-proofs`), worker for rewrite book 7.
**Source:** `~/workspace/r-theory-rewrite/book7/index.html` (working manuscript, lines 71–1283).
**Scope key:** PROVED (exact mathematics) · CHECKED (a completed numeric run) ·
ASSERTED (manuscript claim or assumption) · INCOMPLETE (failed/timed out/unfinished).
**Symbolic log:** exact SymPy run, 26/26 PASS, exit 0 —
`/home/hatch/workspace/.jarvis/workflow-runs/workflow-run-b4b24c5c566d490d92bad5fa51c906c1/work/book7_sympy_check.py`
(run log `book7_sympy_check.log` beside it). An exact symbolic verification of a
polynomial/trigonometric identity is counted here as PROVED, not as sampling.

**Substrate imports (not re-proved):**
- Standard mathematics per the volume dependency rule: trigonometric identities,
  differentiation, matrix algebra, Euler's formula, Hamiltonian/Lagrangian formalism
  after declaration. Counted as standard imports, not as Book 7 results.
- The campaign seed — Kit's double-angle (secant–cosecant) identity, PROVED
  analytically at `~/workspace/kit_theorems/secant-cosecant-identity/PROOF.md`:
  for sin x ≠ 0, cos x ≠ 0,
  `4/sin(2x) = (tan x + |sec x| − 1/(cot x + |csc x|)) + (cot x + |csc x| − 1/(tan x + |sec x|))`.
  (The campaign file `~/workspace/euclid_work/books/seed_double_angle.md` did not yet
  exist when this proof was written — the seed worker was still in flight — so the
  proved source is cited directly.)
- Euclid's Elements: used for the deductive *method* (definitions first, nothing used
  before it is proved), not for its propositions. See "Euclid boundary" at the end.

---

## 1. Definitions (in dependency order)

- **D1 (primitive scalar).** `x` is the primitive scalar coordinate (a real variable;
  no physical time/angle meaning is assigned — see the negative theorems).
- **D2 (primordial reciprocal functions).** `urx, uxp, srx, sxp, crx, cxp` are the
  primordial reciprocal functions of the transfer construction (Book 2 data).
- **D3 (saws).** `saw_r = 1/urx`, `saw_x = 1/uxp` (A-7.1).
- **D4 (orientation sign).** `ε = sgn(sin 2x)` (A-7.1: `saw_r + saw_x = ε`).
- **D5 (transfer coordinate).** On the principal chart,
  `λ = (1 + sin x − cos x)/2`, with `saw_r = ελ`, `saw_x = ε(1−λ)` (A-7.1).
- **D6 (sine carrier).** `H = (saw_r·saw_x)/(saw_r + saw_x)`; `P = sin(2x)/4`,
  `V = cos(2x)/2`.
- **D7 (carrier phase).** `C = cos(2x)`, `S = sin(2x) = 4H`, `Z = C + iS`,
  `φ_c = 2x`.
- **D8 (transfer pair).** On each open quadrant,
  `p = αcos x − βsin x`, `q = αsin x + βcos x` with `α = sgn(sin x)`, `β = sgn(cos x)`;
  `ζ = a + ib` with `a = q/√2`, `b = p/√2`.
- **D9 (parent pair).** `Σ = urx + uxp`, `Δ = (srx + crx) − (sxp + cxp)`.
- **D10 (projective coordinates).** `(Q, S) = (Δ/Σ, 4/Σ)`; `Q₂ = 2P`.
- **D11 (reciprocal/exponential coordinates).** `L₊ = |cot x|`, `L₋ = 1/L�₊`,
  `w = ln|cot x|`.

---

## 2. Claim inventory (scope labels)

| # | Claim | Label |
|---|-------|-------|
| 7.1.T1 | Sine carrier as signed balance product `H = ελ(1−λ)`, `|H| ≤ 1/4` sharp at λ=1/2 | PROVED (exact algebra, conditional on A-7.1) |
| 7.1.C1 | Endpoint/balance structure | PROVED (elementary) |
| 7.1.T2 | Companion cosine `cos2x = ε(1−2λ)√(1+4λ(1−λ))` | PROVED on principal chart; off-chart branches CHECKED (page's numerical run, 2.2e-13, not re-run here) |
| 7.1.C2 | Differential companion `cos2x = 2H′` | PROVED (calculus) |
| 7.1 D/N | `N = 4cot2x`, `D² − N² = 16` | PROVED (standard identity) |
| 7.1.T3 | Carrier phasor `Z = e^{2ix}`; quadrature `S′=2C, C′=−2S` | PROVED (Euler, standard import) |
| 7.1.T4 | Transfer–carrier quadratic map `U+iW = εζ²`; no independent phase | PROVED (exact αβ algebra, open quadrants) |
| 7.2.L1 | `sec²−tan² = csc²−cot² = 1` | standard import |
| 7.2.T1 | UNA reciprocal-sum `sin2x/4 = 1/(urx+uxp)` | PROVED (campaign seed + exact regrouping) |
| 7.2.T2 | Reciprocal-square `cos2x/4 = 1/(cxp+crx)² − 1/(srx+sxp)²` | PROVED (page's exact-algebra audit, accepted) |
| 7.3.T1 | Closed flow `P′=V, V′=−4P` | PROVED (exact differentiation) |
| 7.3.T2 | Conserved `E = V²+4P² = 1/4` | PROVED (exact) |
| 7.3.C2–C4 | Generator `A²=−4I`, `AᵀG+GA=0`, evolution operator, circular normalization | PROVED (exact matrix identities) |
| 7.3.T3 | Formal Hamiltonian `H=V²/2+2P²=1/8` after declaring `ω=dP∧dV` | PROVED, conditional on the declared two-form (A-7.3) |
| 7.4.T1 | Hyperbolic parent `Σ²−Δ²=16` | PROVED (one-line corollary of A-7.2) |
| 7.4.T2 | Projective completion: `(Q,S)` on doubled unit circle | PROVED (conditional on T1) |
| 7.4.T3–T5 | Parent flow, first integral, projective linearization to `S′=2Q, Q′=−2S` | PROVED (exact, conditional on A-7.2) |
| 7.4.T6–T7, C6–C10 | `L₊L₋=1`, `w′=−Σ/2`, rational `Q=(L²−1)/(L²+1)`, `S=2εL/(L²+1)`, Riccati `L′=−ε(1+L²)` | PROVED (exact, open quadrants, conditional on A-7.2) |
| 7.4.E1 | Conserved-level deformation + elliptic/parabolic/hyperbolic classification | ASSERTED as extension (classification math exact conditional on the extension hypothesis) |
| 7.4.CL2 | Printed `2λ−1 = cos x − sin x` | INCORRECT RESULT (sign slip, verified); corrected `2λ−1 = sin x − cos x` PROVED |
| negatives + clarifications (7.1.N1, 7.2.N1, 7.3.N1–N2, 7.4.N1, 7.1.CL1, 7.4.CL1, 7.4.CL2 coord part) | scope statements | PROVED (statements about the construction) |
| "certified" status of the core | status label | ASSERTED (manuscript's own term; page's own finding) |
| §7.4 closing link to Book 5 "Axiom Zero realized at doubled phase" | upstream inheritance | ASSERTED-conditional on Axiom Zero (Book 5 assumption per Volume I ledger) |

---

## 3. Proofs in dependency order

**Prop 7.1 (balance product; 7.1.T1 + 7.1.C1).** Given A-7.1,
`saw_r·saw_x = ε²λ(1−λ) = λ(1−λ)` and `saw_r+saw_x = ε(λ+1−λ) = ε`, so
`H = λ(1−λ)/ε = ελ(1−λ)` since `1/ε = ε`. Exact algebra. The bound:
`λ(1−λ) ≤ 1/4` with equality iff `λ = 1/2` is the vertex of a concave quadratic
(elementary). The equivalent primitive form `H = AB/((A+B)(AB−1))` is the same
parallel-sum algebra in un-normalized variables. **PROVED** (conditional on A-7.1).

**Lemma 7.2 (λ identities; principal chart).** From D5:
`1 − 2λ = 1 − (1+sin x−cos x) = cos x − sin x` (exact; symbolic check PASS).
`4λ(1−λ) = (1+(sin x−cos x))(1−(sin x−cos x)) = 1 − (sin x−cos x)² = sin 2x`
(exact; symbolic check PASS). In particular `2λ−1 = sin x − cos x`, so the book's
printed `cos x − sin x` in 7.4.CL2 is a sign error; the clarification's conclusion
(`2λ−1 ≠ cos2x`) is unaffected. **PROVED**; the slip is a verified finding.

**Prop 7.3 (companion cosine; 7.1.T2, principal chart).** On the principal chart
`ε = +1`, `λ ∈ (0,1)`. Square the right-hand side and use Lemma 7.2:
`RHS² = (cos x−sin x)²(1+sin 2x) = (1−sin 2x)(1+sin 2x) = 1−sin²2x = cos²2x`
(exact; symbolic check PASS). Sign: `√ ≥ 0`, so `sgn(RHS) = sgn(cos x−sin x)`;
`cos2x = (cos x−sin x)(cos x+sin x)` and `cos x+sin x > 0` on `(0,π/2)`, hence
`sgn(cos2x) = sgn(cos x−sin x) = sgn(RHS)`, so `RHS = cos2x`. **PROVED** on the
principal chart. Off-principal-chart branches: **CHECKED** — the page reports
numerical verification to 2.2e-13 on all four charts; not re-run here
(INCOMPLETE as an analytic branch proof; the gap is stated, not filled).

**Prop 7.4 (αβ computation; re-derives T2's key product independently).**
On each open quadrant `α² = β² = 1`. Then
`p² = cos²x − 2αβ sinx cosx + sin²x`, `q² = sin²x + 2αβ sinx cosx + cos²x`,
so `p²+q² = 2(cos²x+sin²x) = 2` (exact; symbolic check PASS), and
`pq = αβ(cos²x−sin²x) + (α²−β²)sinx cosx = αβcos2x`. Since
`αβ = sgn(sin x)sgn(cos x) = sgn(sin2x) = ε` on open quadrants, `pq = εcos2x`
exactly. This closes the manuscript's asserted derivation step noted in the
page's audit. **PROVED.**

**Prop 7.5 (squaring map; 7.1.T4).** With `a = q/√2`, `b = p/√2`:
`a²−b² = (q²−p²)/2`; `q²−p² = 4αβ sinx cosx = 2αβsin2x`, so
`a²−b² = αβsin2x = εsin2x` (exact; symbolic check PASS), and
`2ab = pq = αβcos2x = εcos2x` (Prop 7.4). Hence with `U = sin2x`, `W = cos2x`:
`U = ε(a²−b²)`, `W = 2εab`, i.e. `U+iW = ε(a+ib)² = εζ²` — the ordinary
two-to-one circle squaring map up to the quadrant sign. Negative corollary: every
quantity is a function of the single scalar `x`; no new continuous degree of
freedom and no independent U(1) phase is created (definitional observation).
**PROVED.**

**Prop 7.6 (phasor; 7.1.T3).** `C = cos2x`, `S = sin2x = 4H`; `C²+S² = 1` is the
Pythagorean identity. `Z = C+iS = e^{2ix}` is Euler's formula (standard import);
`2V+i4H = e^{2ix}` is substitution. `S′ = 2C`, `C′ = −2S` is exact differentiation.
The "frequency doubling" is pure bookkeeping (`φ_c = 2x`). **PROVED** (standard import).

**Prop 7.7 (differential companion; 7.1.C2 + D/N).** `cos2x = 2H′` is ordinary
differentiation of `H = sin2x/4`. `N = 4cot2x`, `D²−N² = 16(csc²2x−cot²2x) = 16`
by the standard identity. **PROVED.**

**Prop 7.8 (primitive decomposition; 7.2.T1–T2).** The campaign seed proves
`4/sin2x = (A−1/B)+(B−1/A)` with `A = tan x+|sec x|`, `B = cot x+|csc x|` via the
lemma `A−1/A = 2tan x`, `B−1/B = 2cot x` (exact, from `|sec|² = sec²`). The book
identifies the two summands with `urx, uxp` by exact absolute-value cancellation
(page's audit: exact algebra), giving `urx+uxp = 4/sin2x`, i.e.
`sin2x/4 = 1/(urx+uxp)`. **PROVED** (seed + exact book algebra). The square-share
decomposition `cos2x/4 = 1/(cxp+crx)² − 1/(srx+sxp)²` is the book's exact algebra
on `sin x ≠ 0, cos x ≠ 0` (page's audit; accepted here). **PROVED** (page's exact audit).

**Prop 7.9 (carrier flow; 7.3.T1–T2).** `P = sin2x/4`, `V = cos2x/2`:
`P′ = V`, `V′ = −4P` by exact differentiation (symbolic check PASS); the system
is closed (no new state variable). `E = V²+4P² = 1/4` is exact on the orbit
(symbolic check PASS). **PROVED.**

**Prop 7.10 (generator and evolution; 7.3.C2–C4).** With
`A = [[0,1],[−4,0]]`: `A² = −4I` and, for `G = diag(4,1)`, `AᵀG+GA = 0` are exact
matrix identities (symbolic check PASS). The evolution operator
`M(x) = [[cos2x, sin2x/2],[−2sin2x, cos2x]]` satisfies `dM/dx = AM`, `M(0) = I`
exactly (symbolic check PASS). With `Q₂ = 2P`, `Q₂²+V² = 1/4`: uniform rotation
on a circle of radius 1/2. **PROVED.**

**Prop 7.11 (formal Hamiltonian; 7.3.T3).** Declare the canonical two-form
`ω = dP∧dV` (A-7.3, explicit declaration — part of the result, not smuggled in).
Then `H = V²/2+2P² = 1/8` on the orbit, and Hamilton's equations give
`∂H/∂V = V = P′`, `−∂H/∂P = −4P = V′` (exact; symbolic check PASS); equivalently
a one-coordinate Lagrangian gives `P″+4P = 0`. **PROVED**, conditional on the
declared two-form. The book explicitly does not call `H` physical energy.

**Lemma 7.12 (primitive factorization; A-7.2, accepted on page audit).**
`Σ+Δ = 4cot x`, `Σ−Δ = 4tan x` — verified by the book exactly (SymPy) and
numerically (1.1e-10 relative). I did not re-derive this from the primitive
definitions; it is taken as an established lemma on the page's audit authority.

**Prop 7.13 (hyperbolic parent; 7.4.T1).** From Lemma 7.12,
`Σ²−Δ² = (Σ+Δ)(Σ−Δ) = 16cot x·tan x = 16` — a one-line corollary (symbolic check
PASS). **PROVED** (conditional on Lemma 7.12).

**Prop 7.14 (projective completion; 7.4.T2).** `(Q,S) = (Δ/Σ, 4/Σ)`:
`Q²+S² = (Δ²+16)/Σ² = (Δ²+Σ²−Δ²)/Σ² = 1` by Prop 7.13 (exact; symbolic check PASS).
**PROVED** (conditional on Prop 7.13).

**Prop 7.15 (parent flow and linearization; 7.4.T3–T5).** From Lemma 7.12,
`Σ = 2(cot x+tan x) = 4/sin2x` and `Δ = 2(cot x−tan x) = 4cos2x/sin2x`, whence
`Σ′ = −ΣΔ/2` and `Δ′ = −Σ²/2` by exact differentiation (symbolic check PASS).
The projective map linearizes exactly:
`Q′ = (Δ′Σ−ΔΣ′)/Σ² = −Σ(Σ²−Δ²)/(2Σ²) = −8/Σ = −2S`,
`S′ = −4Σ′/Σ² = 2Δ/Σ = 2Q` (exact; symbolic check PASS). **PROVED** (conditional
on Lemma 7.12). First integral: `d(Σ²−Δ²)/dx = 0` follows from the same ODEs.

**Prop 7.16 (reciprocal/exponential/rational coordinates; 7.4.T6–T7, C6–C10).**
`L₊L₋ = 1` by definition. `w = ln|cot x|`: `w′ = −1/(sin x cos x) = −2/sin2x = −Σ/2`
(exact; symbolic check PASS). Rational: with `L = L₊`,
`Q = (L²−1)/(L²+1)`, `S = 2εL/(L²+1)` satisfy `Q²+S² = 1` exactly (ε² = 1;
symbolic check PASS). Riccati law on open quadrants:
`L′ = sgn(cot x)(−csc²x) = −sgn(cot x)(1+L²)`, and `sgn(cot x) = sgn(cos x)sgn(sin x)
= sgn(sin2x) = ε`, so `L′ = −ε(1+L²)` exactly. **PROVED** (conditional on Lemma 7.12).

**Extension 7.17 (7.4.E1).** The autonomous parent ODE on a larger initial-data
space has conserved level `K = Σ²−Δ²`; the projective flow classifies as
elliptic/parabolic/hyperbolic by `sgn(K)`. This is a **lawful mathematical
extension**, explicitly labeled as such — not an inherited theorem. The certified
trigonometric carrier fixes `K = 16`. **ASSERTED as extension** (the classification
mathematics is exact conditional on the extension hypothesis).

**Negative theorems and clarifications.** 7.1.N1, 7.2.N1, 7.3.N1–N2, 7.4.N1:
scope statements — no physical time, energy, force law, gauge structure, or
independent U(1) phase is derived; each carrier coordinate is driven by the same
scalar `x` (definitional observation, per Props 7.1–7.16). 7.1.CL1: the bare
imbalance `2λ−1` is not the cosine — the envelope factor in Prop 7.3 is essential.
7.4.CL1: the signature firewall (no physical reading of `x, H, E, Σ²−Δ²`).
**PROVED** as statements about the construction.

---

## 4. New axioms / assumptions beyond Euclid + seed + earlier books

- **A-7.1 (Book 2 transfer data, ASSERTED import).** Principal-chart
  `λ = (1+sin x−cos x)/2`, `saw_r = ελ`, `saw_x = ε(1−λ)`,
  `saw_r+saw_x = ε = sgn(sin2x)`, `p = 1−2λ`. The page's own audit records a
  dependency-labeling defect on the "certified" λ in the Volume I Book 2 ledger
  and marks the transfer-construction sections as read but not independently
  checked — so this is an asserted upstream import, numerically grounded here
  (page: matches `ε·saw_r` on the principal chart to 3.3e-16).
- **A-7.2 (primitive factorization lemma).** `Σ+Δ = 4cot x`, `Σ−Δ = 4tan x`
  (Lemma 7.12) — accepted on the page's exact symbolic + numerical audit; not
  re-derived from the primitive definitions here.
- **A-7.3 (declared two-form).** `ω = dP∧dV` — an explicit declaration enabling
  Prop 7.11, stated as part of the result.
- **A-7.4.E1 (conserved-level extension).** Studying the parent ODE on a larger
  initial-data space with `K = Σ²−Δ²` as a level; the certified carrier fixes
  `K = 16`. Explicitly labeled a lawful extension, not an inherited theorem.
- **Conditional, not a new axiom:** the §7.4 closing link "Book 5 flow / Axiom Zero
  realized at doubled phase" inherits Book 5's Axiom Zero as an *assumption* (per
  the Volume I ledger); Book 7's use is conditional on it — ASSERTED-conditional.

No postulates or common notions of Euclid are added or altered.

---

## 5. Euclid boundary (honest statement)

R Theory Book 7 ("Classical Dynamics from the Certified Carrier") is the analytic
trigonometry of the double-angle carrier: parallel-sum balance, quadratic transfer
image, closed linear flow, hyperbolic parent and projective linearization. **No
proposition of Euclid's Elements — Book VII (elementary number theory) or any other
book — is used or needed by these proofs.** What Book 7 takes from Euclid is the
deductive method: definitions first, dependency order, nothing used before it is
proved. The mathematical substrate (trigonometric identities, differentiation,
matrix algebra, Euler's formula) is imported as standard background mathematics
under the volume dependency rule, and the synthetic-constructive stratum rests on
the campaign seed (Kit's double-angle identity, PROVED). This is an extension of a
synthetic-constructive stratum on its declared substrate — not wholesale
inheritance of the Elements.

## 6. Handoff to Book 8

Book 8 inherits the exact carrier mathematics: the reciprocal transfer, the paired
double-angle carrier, and the projective/hyperbolic representations. Book 7 supplies
no electromagnetic field, gauge curvature, charge, spacetime field dynamics, or
physical clock; any such structure in Book 8 requires its own declared extension
or import (per the page's §13 status, unchanged).
