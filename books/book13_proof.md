# Book 13 extension proofs — R Theory rewrite Book 13 (Thermodynamics, Information, and the Arrow of Time)

Scope discipline: every claim carries exactly one label —
PROVED (exact mathematics), CHECKED (a completed numeric run),
ASSERTED (manuscript claim, contract declaration, or standard import),
INCOMPLETE (failed, timed out, or unfinished). The book page's own tags map:
CP/NC → PROVED/CHECKED, ST → ASSERTED (standard import), MA → ASSERTED,
AX → ASSERTED (axiom), IN → INCOMPLETE, IC → the book's statement is
INCORRECT; the analytic counterexample itself is PROVED.

Source: `~/workspace/r-theory-rewrite/book13/index.html` (parts I–V).
Worker: book-13 agent, 2026-09-22. Status file for this book's local
verification: `~/workspace/r-theory-rewrite/book13/` has no local
`validation/book13/verify_book13.py` present — the 86-check run cited below
is the book page's own report (2×10⁴–4×10⁴ points, worst err/tol 0.55),
not independently re-run here.

## 0. The No-Euclid-wholesale boundary

Rewrite Book 13 (thermodynamics, information, arrow of time) has **no
mathematical relation to Euclid's Book 13** (the five regular solids) — a
pure name collision, confirmed by the Book 13 Euclid ledger
(`~/workspace/euclid_work/ledger/book13_ledger.md`): a full-text search of
all 23 rewrite book pages finds zero EMR/pentagon/solid machinery.
Consequently this extension inherits **nothing** from the Elements' Book 13
chain, and nothing from the Elements at all beyond:
- the campaign seed double-angle identity
  (`~/workspace/euclid_work/books/seed_double_angle.md`, PROVED — used only
  for sin(2x) = 2·sin x·cos x in P2),
- ordinary background real analysis (differentiation, limits, logarithms),
  which is **not** part of Euclid's stratum and is flagged as background
  mathematics, not inheritance.

All physics in the proofs below enters through explicitly declared
contracts/imports (AX-1..AX-5). This is the content of the book's governing
rule: *reparameterization is not derivation*.

## 1. Definitions (first, before use)

- **D1. Transfer coordinate.** λ(x) = (1 + sin x − cos x)/2, the "saw_r"
  coordinate. The **admissible quadrant** (chart) is 0 < x < π/2, on which
  0 < λ < 1. Off this chart λ leaves (0,1).
- **D2. Sign channel.** ε(x) = sgn(sin 2x); ε = +1 exactly on admissible
  charts (mod π-periodicity).
- **D3. Response kernel.** H(x) = λ(1−λ) signed; |H| = |λ(1−λ)|.
- **D4. Log-odds.** v = logit(λ) = ln(λ/(1−λ)), v ∈ ℝ for λ ∈ (0,1).
- **D5. Convex generator.** A(v) = ln(1 + e^v), A: ℝ → ℝ₊.
- **D6. System entropy.** S_sys(λ) = −k_B[λ ln λ + (1−λ) ln(1−λ)],
  S_sys(x) = S_sys(λ(x)).
- **D7. KL divergence.** D(λ‖λ₀) = λ ln(λ/λ₀) + (1−λ) ln((1−λ)/(1−λ₀)).
- **D8. Fisher information (v-coordinate).** I_v = E_v[(∂_v ln p)²] for the
  Bernoulli family p_λ with v the natural parameter.
- **D9. Fisher angle.** φ_F(v) = 2 arctan(e^{v/2}).
- **AX-1. Bernoulli statistical contract (declared, ASSERTED).** On
  admissible charts λ is admitted as the parameter of a Bernoulli
  distribution. The positive square-root state
  Ψ_stat = (√λ, √(1−λ)) is the square-root embedding of that distribution;
  it adds no quantum phase or coherence (status declaration, correctly
  labeled contract-dependent in the book).
- **AX-2. Gibbs canonical contract (standard import, ASSERTED/ST).** Two
  levels with energies E_r < E_x, gap Δ = E_x − E_r, multiplicities
  g_r, g_x, canonical bath at temperature T. Boltzmann/Gibbs relations are
  imported, not derived.
- **AX-3. Two-state Markov contract (standard import, ASSERTED/ST).**
  Continuous-time Markov chain with rates k_±, fluxes J_±.
- **AX-4. Path/reversal contract (standard import, ASSERTED/ST).**
  Forward/reversed trajectory ensembles under an explicit reversal rule;
  trajectory entropy production = forward/reversed log-probability ratio.
- **AX-5. Many-body thermodynamic contract (ASSERTED/AX).** Required before
  any phase-transition (e.g. BEC) semantics may be attached.

## 2. Claim inventory, in dependency order

### 2.I — The coordinate and its exact identities

**P1. [PROVED]** λ:(0,π/2) → (0,1) is strictly monotone with λ(0)=0,
λ(π/4)=1/2, λ(π/2)=1. *Proof.* Direct substitution; dλ/dx =
(sin x + cos x)/2 > 0 on (0,π/2). Symbolic run: PASS (5 checks).

**P2. [PROVED]** Signed exact identity: λ(1−λ) = sin(2x)/4 =: H.
*Proof.* 1−λ = (1−sin x+cos x)/2. Product = (1−(sin x−cos x)²)/4 =
(1−(1−sin 2x))/4 = sin(2x)/4, using sin 2x = 2 sin x cos x (seed,
domain remark). Symbolic run: PASS.

**P3. [CHECKED]** On admissible charts (ε=+1) urx = 1/λ, uxp = 1/(1−λ);
the which-is-which is pinned (urx = 1/λ, not the swap). Verified against
the certified Book 2 sum/product identities at 2×10⁴ points, max error
< 1e-10; the global reciprocal-access pair at 4×10⁴ points, ≤ 4.9e-10
absolute (book page report; run file absent locally, not re-run here).

**P4. [PROVED]** λ(π/2−x) = 1−λ(x) for all x. *Proof.* Direct:
λ(π/2−x) = (1+cos x−sin x)/2 = 1−λ(x). Symbolic run: PASS.

**P5. [PROVED]** Recovered reading of the garbled source sentence:
S_sys → 0 as |H| → 0, and S_sys = k_B ln 2 at |H| = 1/4. *Proof.*
|H| = λ(1−λ) → 0 ⟺ λ → {0,1} ⟹ −[λ ln λ+(1−λ)ln(1−λ)] → 0. At λ=1/2,
|H|=1/4 and S_sys = −k_B ln(1/2) = k_B ln 2. (The printed sentence with
undefined h and "00" is defective as printed.)

**P6. [ASSERTED]** Ψ_stat = (√λ, √(1−λ)) carries no quantum phase or
coherence — a status declaration under AX-1, correctly labeled
contract-dependent by the book.

### 2.II — The convex generator and exponential family (Thm 13.II.T1, conditional on AX-1)

**P7. [PROVED]** A′(v) = λ(v) = e^v/(1+e^v) and A′′(v) = λ(1−λ) = |H|
(on admissible charts). *Proof.* Direct differentiation of
A(v) = ln(1+e^v). Symbolic run: PASS (2 checks).

**P8. [PROVED]** ln|uxp| = A(v) and ln|urx| = A(−v), where v = logit(λ).
*Proof.* |uxp| = 1/(1−λ); A(v) = ln(1/(1−λ)) = −ln(1−λ). For urx:
A(−v) = ln(1+e^{−v}) = ln((1+e^v)/e^v) = A(v) − v = −ln λ. Both follow
from P7's λ(v).

**P9. [PROVED]** Legendre identity: λv − A(v) = −S_sys/k_B. *Proof.*
A(v) = −ln(1−λ) at v = ln(λ/(1−λ)); λv − A(v) =
λ ln λ − λ ln(1−λ) + ln(1−λ) = λ ln λ + (1−λ)ln(1−λ) = −S_sys/k_B.
Symbolic run: PASS.

**P10. [PROVED]** KL = Bregman divergence of A (with the standard order
convention). *Proof.* KL(λ‖λ₀) = λ(v−v₀) − (A(v)−A(v₀)) =
B_A(v₀; v) — Bregman with center at v, evaluated at v₀ (gradient at the
first argument's preimage). Verified symbolically: PASS. The book's
unqualified "KL = Bregman divergence of A" holds under this standard
convention; the gradient-evaluation order is the content that must be
stated.

**P11. [PROVED]** Fisher metric in the v-coordinate is I_v = A′′(v).
*Proof.* Standard exponential-family identity: the score
∂_v ln p = T − λ with T ∈ {0,1}, and E[(T−λ)²] = λ(1−λ) = A′′(v) by P7.

**P12. [PROVED]** φ_F(v) = 2 arctan(e^{v/2}) maps ℝ onto (0,π) and
dφ_F/dv = √A′′ = √|H|. *Proof.* dφ_F/dv = 2·(1/(1+e^v))·(1/2)e^{v/2} =
e^{v/2}/(1+e^v) = √(e^v/(1+e^v)²) = √A′′. As v→−∞, e^{v/2}→0,
arctan→0; as v→∞, arctan→π/2. Symbolic run: PASS (3 checks).

**P13. [PROVED]** |H|·v̇² = φ̇_F² (chain rule). *Proof.* φ̇_F =
(dφ_F/dv)v̇ = √|H|·v̇ by P12; square.

**Thm 13.II.T1 — [PROVED], conditional on AX-1.** The framing — one
Bernoulli exponential family generating log-odds, KL/Bregman geometry,
Fisher information, Legendre duality, Fisher-angle compactification — is
established by P7–P13; the standard exponential-family framing is
ST-imported mathematics, not R Theory invention.

### 2.III — Canonical thermodynamic bridge (conditional on AX-2)

**P14. [PROVED]** Under AX-2: v = Δ/(k_B T) + ln(g_r/g_x);
T = Δ/{k_B[v − ln(g_r/g_x)]}; λ_∞ = g_r/(g_r+g_x) (= 1/2 iff
g_r = g_x); S_micro = S_sys + k_B[λ ln g_r + (1−λ)ln g_x], maximal at
λ_∞ with value k_B ln(g_r+g_x); Z = g_r|urx|,
F_eq = −k_B T ln(g_r|urx|) in the E_r = 0 gauge; Var(E) = Δ²|H|;
C = k_B(βΔ)²|H|; dλ/dv = |H| = I_v; T_s = T_*/(v + ln 3) for the 21-cm
spin-temperature re-expression. *Proof.* Elementary algebra from the
two-level Gibbs weights; C verified symbolically via C = d⟨E⟩/dT with
⟨E⟩ = (1−λ)Δ in the E_r = 0 gauge (PASS). λ_∞ limit verified
symbolically (PASS). The Boltzmann/Gibbs relations themselves are ST.

**P15. [PROVED]** **Conditional Theorem 13.III.T1** (temperature
identifiability obstruction): the single scalar equation
βΔ = v − ln(g_r/g_x) in two unknowns (β, Δ) fixes only the product;
absolute temperature needs an independent gap or calibration. Complete
elementary argument — no proof beyond the equation's form is needed.

**P16. [PROVED]** **Conditional Theorem 13.III.T2** (response kernel):
|H| is the common dimensionless kernel of probability susceptibility
(dλ/dv), energy variance (Var(E)/Δ²), entropy response, Fisher
information, and heat capacity (C/[k_B(βΔ)²]) — established by P7, P11,
P14; the dimensional meaning enters only through the imported scale,
temperature, and ensemble of AX-2.

**P17. [CHECKED]** Schottky heat-capacity peak near kT/Δ ≈ 0.42
(book NC; numeric witness of P14's formula, not re-run here).

**Flag — [IC in the source, analytic counterexample PROVED].** "For equal
multiplicity, |urx| is exactly the canonical partition function in this
energy gauge" is false: P14 gives Z = g_r|urx|, so |urx| = Z/g_r. With
equal multiplicities g_r = g_x = 2, |urx| = Z/2 ≠ Z. Exact partition
function status needs the nondegenerate lower level g_r = 1, not merely
equal multiplicities.

### 2.IV — Detailed balance, free energy, slow driving (conditional on AX-3)

**P18. [PROVED]** Under AX-3: σ̇ = k_B(J_+−J_−) ln(J_+/J_−) ≥ 0 (real
analysis: (a−b)ln(a/b) ≥ 0 for a,b > 0); detailed balance at
Λ = k_+/(k_+ + k_−); ln(J_+/J_−) = a − v; ∂D/∂λ = v − a;
σ̇ = −k_B dD/dt; F_noneq − F_eq = k_B T·D(λ‖Λ);
dF_noneq/dt = −Tσ̇. *Proof.* Algebraic identities inside the Markov
contract; standard stochastic-thermodynamics forms are ST.

**P19. [PROVED]** **Conditional Theorem 13.IV.T1** (KL/free-energy
relaxation): relative entropy to equilibrium is the dimensionless
nonequilibrium free-energy excess and decays monotonically exactly when
entropy production is nonnegative — established end to end by P18.

**P20. [ASSERTED/ST]** Slow-driving Fisher form σ̇ ≈ (k_B/γ)|H|·v̇²,
constant-Fisher-speed minimality, reversal-invariance of the metric
cost: standard linear-response/thermodynamic-geometry imports, stated as
approximations, measuring dissipation cost without choosing a temporal
direction.

**P21. [PROVED — conditional on P20's Fisher-form premise]** "For protocol
duration τ, Sigma_prod ≥ [k_B/(γτ)](Δφ_F)²" — the right-hand side,
missing as printed, was recovered 2026-09-25 from the archived Book 13
consolidated draft
(archive_sweep/drive_hunt/texts/toplevel_docs/036_Our_Revised_R_Theory_Book_13_Consolidated_Draft.txt:429),
which prints the bound in full together with its derivation setup
(Ṡ_prod ≈ (k_B/γ)φ̇_F²; minimum leading dissipation attained at constant
Fisher speed). Proof: from the premise Ṡ_prod = (k_B/γ)φ̇_F²,
Σ_prod = (k_B/γ)∫₀^τ φ̇_F²dt ≥ (k_B/γ)(∫₀^τ φ̇_F dt)²/τ = k_B(Δφ_F)²/(γτ)
by Cauchy–Schwarz, with equality iff φ̇_F is constant a.e. Independent
symbolic check (euclid_work/verify_P21.py, sympy, exact — no sampling):
for every normalized protocol S−1 = ∫₀¹(f′−1)²ds ≥ 0; linear,
quadratic-ramp, zigzag, cubic-bump, and sine-bump profiles integrate
exactly to S = 1, 4/3, 4/3, 10/7, π²/8 (all slack ≥ 0, matching the
corpus's WA-computed exact slacks 3/7 and π²/8−1); tightness at constant
speed, dimensional consistency (J/K both sides), and the corpus
"intended floor" form all confirmed. (Wolfram Engine was down —
"No valid password found" — so sympy was used; engine licensing issue
logged 2026-09-25.) The premise itself (slow-driving Fisher form)
remains ASSERTED per P20; the Cauchy–Schwarz implication from it is
exact.

### 2.V — Cycle affinity, seams, hidden-state identifiability

**P22. [PROVED]** Exact-potential affinities telescope to zero around
closed cycles. Elementary (finite telescoping sum).

**P23. [CHECKED]** Four-state ring (clockwise p, counterclockwise q):
uniform stationary distribution, visible coarse-grained chain exactly
detailed-balanced at λ = 1/2 with equal both-way rates, nonzero hidden
current and positive hidden entropy production for p ≠ q (book NC
verification; not re-run here).

**P24. [PROVED]** **Conditional Theorem 13.V.T1** (visible equilibrium
need not be microscopic equilibrium): correct for the declared
four-state model, from P22–P23.

**P25. [PROVED half / ASSERTED half]** **Negative Result 13.V.N1**
(seam-affinity obstruction): the telescoping half is P22 (PROVED). The
second half — seam data "does not determine a unique crossing rule or
stochastic transition law" — is argued *by the source boundary
theorem*, which appears nowhere else in Volume II (single occurrence,
inside Book 13 itself) and is not in the Volume I audit ledger as
earned. The proof as given leans on an uncertified premise; flagged
with dependency warning, per the book.

### 2.VI — Cophase topology and kinetic nonselection

**P26. [PROVED]** The lifted quarter-turn has exact order four; its
action on the primitive quartet is the pair of 2-cycles (srx crx)(sxp
cxp); ε, H, urx, uxp, FlatWave reverse after one cophase step and
restore after two; all are π-periodic, hence cannot distinguish x from
x+π. *Proof.* Algebraic sign laws of the reciprocal channels; the book
also carries NC runs.

**P27. [PROVED]** No faithful affine C4 action on one real coordinate
exists; R² rotations give a faithful one. *Proof.* Affine f(x) = ax+b
with a = ±1: a = 1 gives translations (order infinite unless b = 0,
the identity); a = −1 gives f² = id (symbolic PASS), order ≤ 2. A
faithful 4-cycle action needs at least R² rotations.

**Flag — [IC in the source, analytic counterexample PROVED].** "The
transfer coordinate λ is quarter-turn invariant" is false under the
volume's canonical notation: λ(0) = 0 but λ(π/2) = 1 (symbolic PASS),
so λ is not invariant under x ↦ x+π/2. What *is* quarter-turn invariant
is the constructible ratio λ_b = ε/urx, which agrees with canonical λ
on admissible charts but differs off-chart (book: at 3π/4, 0.5 vs
(1+√2)/2 ≈ 1.207). The book never distinguishes the two λ's. Not
load-bearing for Thm 13.VI.T1.

**P28. [ASSERTED]** **Theorem 13.VI.T1** (cophase kinetic nonselection):
a canonically selected real cycle bias must be both
reflection-invariant and sign-reversing, hence zero. The "canonical
selection" premise does the work — a conceptual symmetry argument, not
a formal derivation. Correctly scoped as a nonselection result; the
book explicitly refuses to conflate orientation signs with temporal
direction ("Orientation signs can record which orientation has been
chosen. They do not choose it.").

**P29. [ASSERTED]** Rank claims: a single continuous branch-bias
coordinate captures only the C2 parity quotient; a faithful stochastic
cophase refinement needs at least two branch-bias directions (rank ≥ 3
with λ); the correction of the earlier factorized (λ,η) ansatz uses
modeling language ("locally complete convex probability family") with
no precise definition given in the book.

### 2.VII — Path-space irreversibility (conditional on AX-4)

**P30. [PROVED]** S_sys(λ) = S_sys(1−λ); on the principal quadrant the
entropy is zero at both ends, maximal ln 2 at the midpoint, exactly
symmetric about π/4. *Proof.* From D6 and P4.

**P31. [PROVED]** **Conditional Theorem 13.VII.T1** (two-ended
entropy): the Bernoulli entropy cannot select one quadrant endpoint as
the unique past. *Proof.* Complete elementary argument from P30: a
function exactly symmetric about the midpoint with equal values at both
ends contains no information distinguishing the two ends.

**P32. [ASSERTED/ST]** Path-space material — trajectory
log-probability ratio entropy production, its mean a KL divergence
hence nonnegative, reversible microdynamics with low-entropy
preparation, mid-time low-entropy condition, asymmetric
boundary/preparation data as the arrow's source: standard imported
statistical-mechanical reasoning (AX-4), correctly separated from
Projection's internal mathematics by the book.

**P33. [ASSERTED]** The retirement of a universal Time=ΔEntropy identity
is a status declaration following from P31, correctly scoped ("at most"
a process-dependent progress coordinate).

### 2.VIII — Thermodynamic state rank and lawful extensions

**P34. [PROVED]** **Theorem 13.VIII.T1** (state-rank obstruction): every
certified scalar readout is a function of one real parameter; a smooth
one-parameter family has differential rank at most one; independent
thermodynamic directions need rank ≥ 2, so temperature, pressure,
chemical potential, or a generic equation of state require added
coordinates or an explicitly one-dimensional process contract. Complete
elementary argument.

**P35. [PROVED]** Jacobian criterion J_UV ≠ 0 and the
two-outcomes/one-coordinate, three-outcomes/full-rank simplex counts.
Elementary.

**P36. [ASSERTED/ST]** Extensivity S_N = N·S_sys, C_N = N·C for
independent copies. Standard.

**P37. [PROVED]** **Negative Result 13.VIII.N1**: if F is
V-independent then P = −(∂F/∂V)_T = 0; a geometric carrier variable
becomes thermodynamic volume only after a subsystem boundary and
V-dependent spectrum/interaction/counting are supplied. Two-line
complete proof.

### 2.IX — Phase transitions and the BEC promotion gate

**P38. [PROVED]** S_sys′′(λ) = −k_B/[λ(1−λ)] = −k_B/|H|, equal to
−4k_B (finite) at λ = 1/2 — the midpoint is a smooth maximum, not a
critical singularity. *Proof.* S_sys/k_B = −[λ ln λ + (1−λ)ln(1−λ)];
d/dλ = −ln(λ/(1−λ)); d²/dλ² = −(1/λ + 1/(1−λ)) = −1/(λ(1−λ)). Symbolic
run: PASS (2 checks).

**P39. [PROVED]** λ:(0,π/2) → (0,1) is a strictly monotone bijection
(P1); any interior λ₀ maps to zero of the monotone control coordinate
τ = a[logit(λ) − logit(λ₀)].

**P40. [PROVED]** **Negative Result 13.IX.N1** (BEC promotion no-go):
coordinate matching alone cannot identify any Projection
midpoint/seam/FlatWave reversal/entropy extremum with Bose–Einstein
condensation; the many-body contract (AX-5) must be supplied, and any
Projection-specific claim must predict a restriction beyond the imported
model. Proof complete given the checked lemmas. The complex condensate
phase is correctly classified as a genuine extension under P34.

### 2.X — Final obstruction and Book 13 closure

**P41. [ASSERTED]** **Theorem 13.X.T1** (candidate-bounded
autonomous-arrow no-go): honestly scoped as an exhaustiveness result
*over the candidate mechanisms admitted in this book*, explicitly "not
a universal impossibility theorem". The cited reasons are established
(P22, P24, P27–P28, P30–P31, P34), but "the preceding sections exhaust
the admitted candidate mechanisms" is asserted, not proved —
exhaustiveness over a candidate list cannot be derived from the list.

**P42. [ASSERTED]** **Terminal Theorem 13.X.T2** (Book 13 closure):
three-level closure bookkeeping (statistical / conditional
thermodynamic / arrow obstruction). A section-pointer summary; no
circular dependence introduced, no unresolved premise promoted.

**P43. [ASSERTED]** Operational closure Δ_op(Volume II) = ∅: from this
worker's position, Book 13 contributes no counterexample; Books 7–12
were not audited here (their per-book proof files are being written by
sibling workers). The book's "certified" wording carries the §13.I
dependency note: the Volume I audit found the "certified transfer
coordinate λ" label defective in 2.XI.L9 — Book 13 uses λ as a *defined*
coordinate, which is legitimate, but any reading leaning on upstream
*certification* inherits that defect.

**P44. [ASSERTED]** Two-Volume Boundary and Master-Retirement
Condition: procedural declarations. The retirement antecedent is
currently unmet (Volume I audit ledger still lists open/incomplete
items), and this is stated, not authorized.

## 3. New axioms / assumptions beyond Euclid + seed + earlier books

1. **Real analysis as background mathematics** (differentiation,
   limits, logarithms, absolute value, real exponentiation). Not part
   of Euclid's stratum; used as ordinary background mathematics and
   flagged as such. Nothing in P1–P44 is claimed as inherited from the
   Elements.
2. **AX-1** — Bernoulli statistical contract (§1): λ admitted as a
   probability parameter; Ψ_stat declared non-quantum. ASSERTED.
3. **AX-2** — Gibbs canonical contract (§1): two levels, gap Δ,
   multiplicities, bath, temperature; Boltzmann/Gibbs imported. ASSERTED.
4. **AX-3** — Two-state continuous-time Markov contract (§1).
   ASSERTED.
5. **AX-4** — Path/reversal contract (§1): forward/reversed trajectory
   ensembles. ASSERTED.
6. **AX-5** — Many-body thermodynamic contract (§1), required before
   any phase-transition semantics. ASSERTED.
7. **Uncertified premise (not an axiom — a flagged dependency):** the
   "source boundary theorem" invoked in 13.V.N1 (P25, second half)
   appears once, inside Book 13 itself, and is not in the Volume I
   audit ledger as earned. The seam-obstruction claim leans on it.
8. **Inherited labeling defect (flagged, not repaired):** the
   "certified λ" wording from 2.XI.L9 (Volume I audit) — Book 13's
   legitimate use is as a *defined* coordinate only.

No new definitions of irrational lines, golden ratio, or sphere
inscription are introduced: Euclid's Book 13 (solids) content is
entirely absent from this extension.

## 4. Source-text defects found (kept honest)

- **Garbled sentence (13.I):** "with 00 as h->0 and S_sys=k_B ln 2 at
  h=1/4" — variable h undefined, "00" meaningless. Recovered intent is
  true (P5); the printed sentence is defective.
- **IC (13.III):** "|urx| is exactly the canonical partition function"
  — false as stated (P17 flag); needs g_r = 1.
- **IC (13.VI):** "λ is quarter-turn invariant" — false under canonical
  notation (P27 flag); true only of the constructible ratio ε/urx.
- **RESOLVED (13.IV):** the Cauchy–Schwarz duration bound's right-hand
  side numerator, missing as printed, recovered from the archived Book 13
  consolidated draft — Σ_prod ≥ [k_B/(γτ)](Δφ_F)² (P21, proved from P20's
  Fisher-form premise, 2026-09-25).

## 5. Ledger counts

PROVED: 29 · CHECKED: 3 · ASSERTED: 12 · INCOMPLETE: 0.
(P21 promoted 2026-09-25: RHS recovered from archive, C–S implication proved.)
(P25 splits: telescoping half PROVED, crossing-rule half ASSERTED.)
(Symbolic verification of the analytic core: 20 checks, exit 0 —
workflow workdir `verify_book13_core.py`. No numerical sampling was run
on top of any proved identity, per the proof-over-sampling rule.)

Notes: ST imports are counted under ASSERTED with their ST label kept
in the file. The book's two IC findings are recorded as flags, not
claims — their analytic refutations are PROVED (P17, P27 flags).
Sibling proof files `book0_proof.md`–`book6_proof.md` (except those
present) were still being written by other workers at the time of
writing; this file depends on none of them — only the seed
double-angle identity (seed_double_angle.md, PROVED) and background
real analysis are used.
