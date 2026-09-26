# Book 20 — Relativistic and Spinor Witnesses: Extension Proofs

Source: `~/workspace/r-theory-rewrite/book20/index.html` (Volume 0; rebuilt
standalone from the former T4 essay-book). Every theorem, import, and status
qualification below comes from the book page; no mathematics has been added.
What this file does is re-order them Euclid-style — definitions first,
dependency order, nothing used before it is proved — and scope each claim
honestly.

Written 2026-09-22. Method: Euclid (definitions first, dependency order),
Ptolemy (compute, don't assume), Polya (understand, plan, carry out, look
back). Scope labels: PROVED (exact mathematics shown here), CHECKED (a
completed numeric run), ASSERTED (manuscript claim or assumption),
INCOMPLETE (failed/timed-out/unfinished), ST (standard imported theorem,
stated not proved here — counted under ASSERTED unless re-proved in the
text, in which case counted under PROVED).

## 0. Standing and scope

- The campaign seed (`~/workspace/euclid_work/books/seed_double_angle.md`)
  is on disk and PROVED; it is cited where used. Sibling files
  `book0_proof.md` .. `book19_proof.md` were not present when this worker
  ran (sibling workers presumably in flight). Book 20's declared dependency
  is Book 0 (primitive calculus, one-generator reduction); since that proof
  file is unavailable, the one-generator obstruction enters here as an
  explicitly named ASSERTED premise (**B0** below), never as a proved fact.
- **Euclid contact:** no proposition of Euclid's *Elements* (Books 1–13, as
  inventoried in `~/workspace/euclid_work/ledger/`) is used in any derivation
  below. The contact with Euclid is stylistic (definitions first, dependency
  order) and methodological. This is the No-Euclid-wholesale boundary: R
  Theory extends a synthetic-constructive stratum on its declared substrate;
  wholesale inheritance of the Elements is not claimed. The mathematical
  substrate actually used is modern: special-relativistic kinematics, Dirac
  theory, the Bloch-sphere two-state geometry, the Standard Model weak
  sector, Coulomb/Dirac-Coulomb analysis, classical electromagnetism —
  imported as standard theorems (ST) and re-proved where load-bearing.
- Proof-over-sampling rule (Kit, 2026-09-21): where an analytic proof is
  complete, no numerical sample is run on top of it. This file therefore
  contains zero new numerical runs; every PROVED item below is proved
  analytically in the text. Claims the book's own audit verified symbolically
  or numerically are re-proved analytically here where the proof is complete;
  where it is not, they are labeled ASSERTED with the gap named.

## A. Definitions (in dependency order; all proofs use only these)

- **D-χ (declared coordinate contract).** For a massive particle on the
  positive-energy branch, in units c = 1, define the kinematic angle χ by
  `sin χ = β` and `cos χ = m/E`, where `β = p/E` is the velocity,
  `E = √(p² + m²)` the energy, m > 0 the mass. The contract is invertible on
  the branch χ ∈ [0, π/2). This is a *contract*, not a derived fact; special-
  relativistic kinematics is the import (**I-SR**).
- **D-sxp/cxp (Book 0 convention, imported via B0).** `sxp(χ) = tan(χ/2)`,
  `srx(χ) = cot(χ/2)`, `cxp(χ) = e^η`, `crx(χ) = e^{-η}`, where η is the
  rapidity defined by `tanh η = β`.
- **D-q/u.** `q = sxp(χ) = tan(χ/2)` (kinematic half-angle coordinate);
  `u = sxp(a) = tan(a/2)` where a is the Coulomb structural angle of §4
  (`sin a = Zα`, `cos a = √(1-(Zα)²)`, **I-Coulomb**).
- **D-φ (independent phase, declared).** An independent real relative phase
  φ, adjoined to the one-generator coordinate q to complete a two-state
  spinor (**I-Bloch**).
- **D-Δ_op (operational prediction-difference set).** For a fully specified
  Projection-augmented model M_P against its accepted reference M_0:
  `Δ_op(M_P, M_0) = { c ∈ C_exp : P_P(·|c) ≠ P_0(·|c) }`, the experimental
  configurations where the predictions actually differ. Terminal statuses:
  **Class A** (fully specified, Δ_op = ∅), **Class B** (incomplete —
  Δ_op *undefined*; an open ansatz is not a nonempty prediction set),
  **Class C** (fully specified, Δ_op ≠ ∅).
- **D-C0.** The null hypothesis: Projection Craft changes representation
  but not physics.

## B. Claim inventory (load-bearing items of rewrite Book 20)

| # | Claim | Book tag | This file's scope |
|---|-------|----------|-------------------|
| 1 | 20.1.K1: kinematic dictionary — `sxp(χ) = pc/(E+mc²) = tan(χ/2)`, `cxp = e^η`, `cxp·crx = 1` as mass shell; invertible on branch | CONDITIONAL | PROVED (conditional on I-SR + I-Dirac) |
| 2 | 20.1.N1: rank is not created by notation — many functions of one χ give one angle's worth of content | OBSTRUCTION | ASSERTED (retained meta-claim) |
| 3 | 20.2.S1: spinor completion with independent phase φ; exact Bloch vector `(cos χ cos 2φ, cos χ sin 2φ, sin χ)`; reciprocal pair as component-amplitude odds | CONDITIONAL | PROVED (conditional on I-Bloch) |
| 4 | 20.2.N2: native carrier `Ψ = H + iV` exactly `(i/8)(e^{2ix} + 3e^{-2ix})` (1:3 counter-rotating decomposition); bare embedding Class B | exact internal / Class B | PROVED (algebra); Class B embedding ASSERTED |
| 5 | 20.3.V1: V−A helicity correspondence — after importing left-chiral orientation, `√(P_fav/P_wrong) = cxp` exactly | CONDITIONAL | PROVED (conditional on I-VA + K1) |
| 6 | 20.3.N2: chirality-orientation obstruction — the left-chiral orientation is imported, not derived | OBSTRUCTION | ASSERTED (retained) |
| 7 | 20.4.T1: two-angle necessity — a and χ generically independent; `a = χ` would force `β = Zα` | CONDITIONAL | PROVED (conditional on I-Coulomb) |
| 8 | 20.4.T2: `ξ = Zα/β = sin a / sin χ = u(1+q²)/(q(1+u²))` exactly | CONDITIONAL | PROVED |
| 9 | 20.4.T3: allowed beta phase space fully rational in (q, q₀) | CONDITIONAL | PROVED (conditional on the stated allowed-approximation integrand, ST) |
| 10 | 20.4.N3: complex-Gamma factor `exp(πξ)\|Γ(λ+iξ)\|²` lies outside finite rational primitive closure; Fermi function, matrix elements, radiative/finite-size corrections, endpoint energy, R imported | IMPORT / OBSTRUCTION | ASSERTED (retained; imports named) |
| 11 | 20.5.W1–W9: nine electromagnetic witnesses — exact correspondences, each stripped by projective/gauge/tetrad/duality/conformal redundancy; no Projection-specific invariant survives | OBSTRUCTION | correspondence identities PROVED (conditional); stripping verdict ASSERTED |
| 12 | 20.6.F1: firewall theorem — invertible representation change cannot create nonempty Δ_op | exact | PROVED (from D-Δ_op) |
| 13 | 20.6.F2: incompleteness is not novelty | exact | PROVED (from D-Δ_op) |
| 14 | 20.6.A1: every fully specified construction of §§1–5 lands Class A, Δ_op = ∅ | Class A assignments | PROVED (conditional on the correspondence proofs 1,3,5,7–9,11) |
| 15 | 20.6.A2: bare-carrier embedding, Projection-only chirality selection, scalar-only local duality dynamics land Class B | Class B assignments | ASSERTED (status declarations) |
| 16 | 20.6.C0: book closure — `Δ_op = ∅` for every fully specified construction in Book 20; C0 retained as undefeated null hypothesis | EXACT (book tag) | PROVED (conditional theorem about the book's content) |

## C. Proofs in dependency order

**Lemma L1 (half-angle rational identities, PROVED).** For t = tan(x/2):
`sin x = 2t/(1+t²)` and `tan(x/2) = sin x/(1+cos x)`. Proof: `sin x =
2 sin(x/2)cos(x/2) = 2t cos²(x/2) = 2t/(1+t²)` since `cos²(x/2) =
1/(1+tan²(x/2))`. Also `sin x/(1+cos x) = 2 sin(x/2)cos(x/2)/(2cos²(x/2)) =
tan(x/2)`. ∎

**20.1.K1 (PROVED, conditional on I-SR + I-Dirac).** From D-χ (c = 1):
`sin χ = β = p/E`, `cos χ = m/E`; `sin²χ + cos²χ = (p²+m²)/E² = 1` by the
imported mass shell (**I-SR**). By L1, `sxp(χ) = tan(χ/2) = sin χ/(1+cos χ)
= (p/E)/((E+m)/E) = p/(E+m)`. Restoring c: `pc/(E+mc²)`; this is the
imported free-Dirac lower/upper component ratio (**I-Dirac**), hence the
first equality. Rapidity: `tanh η = β`, so `e^η = √((1+β)/(1−β)) =
√((E+p)/(E−p))`. Now `cxp = (E+p)/m` (c = 1) and `(E+p)²/m² =
(E+p)²/(E²−p²) = (E+p)/(E−p)` by the mass shell, so `cxp = e^η`; similarly
`crx = (E−p)/m = e^{−η}`. Product: `cxp·crx = (E²−p²)/m² = 1`, exactly the
normalized mass shell. On χ ∈ [0, π/2), sin χ is strictly increasing, so the
χ ↔ β chart is invertible on the declared branch. ∎

*Scope note:* every physical identity in K1 (mass shell, Dirac ratio) is a
declared import; what is proved here is that *under those imports* the
half-angle/reciprocal calculus coincides with them exactly. The book's
IMPORT tags are therefore retained on the premises, and the theorem is
correctly CONDITIONAL.

**20.1.N1 (ASSERTED, retained).** "Rank is not created by notation": the book
states this as an obstruction, not as a derived theorem. Taken as stated:
all functions in K1 are functions of the single real coordinate χ, so the
dictionary carries one angle's worth of content. No proof of the general
meta-claim is attempted; it is retained as a declared obstruction. (The
one-generator obstruction itself belongs to Book 0 via **B0**, unavailable
here.)

**20.2.S1 (PROVED, conditional on I-Bloch).** The imported two-state
geometry (**I-Bloch**) identifies a normalized two-component spinor with a
Bloch vector. Complete the coordinate: choose the branch-normalized
amplitudes `c₀ = cos(π/4 − χ/2)`, `c₁ = sin(π/4 − χ/2)·e^{2iφ}` with φ the
independent phase **D-φ**. Bloch components: `r_z = |c₁|² − |c₀|² =
−cos(π/2 − χ) = sin χ`; `r_x = 2 Re(c₀*c̄₁) = sin(π/2 − χ)cos 2φ =
cos χ cos 2φ`; `r_y = 2 Im(c₀*c̄₁) = cos χ sin 2φ`. Hence the exact Bloch
vector `(cos χ cos 2φ, cos χ sin 2φ, sin χ)`. The component-amplitude odds
`|c₁/c₀|² = tan²(π/4 − χ/2)` carry the reciprocal structure of §1 as the
ratio of the two amplitudes; the phase φ is independent data, which is the
one-generator obstruction surviving completion (via **B0**). ∎

**20.2.N2 (PROVED; Class B embedding ASSERTED).** From §5's normalization
(also used here): `H = sin 2x/4`, `V = cos 2x/2`, `Ψ = H + iV`. Then
`(i/8)(e^{2ix} + 3e^{−2ix}) = (i/8)[(cos 2x + i sin 2x) + 3(cos 2x − i sin 2x)]
= (i/8)(4 cos 2x − 2i sin 2x) = i cos 2x/2 + sin 2x/4 = Ψ`. The 1:3
counter-rotating decomposition is exact algebra. The anisotropic squeeze is
descriptive of this form. That Ψ *as an unspecified physical embedding*
determines no unique observable (Class B) is the book's verdict, retained
here as ASSERTED: no complete contract or dynamics is supplied for the bare
carrier. ∎

**20.3.V1 (PROVED, conditional on I-VA + K1).** Import the Standard Model
left-chiral projector `P_L = (1−γ⁵)/2` and the standard massive-helicity
weights `P_fav = (1+β)/2`, `P_wrong = (1−β)/2` (**I-VA**, imported not
derived). Then `√(P_fav/P_wrong) = √((1+β)/(1−β)) = e^η = cxp` by the K1
rapidity identity, and `√(P_wrong/P_fav) = crx`. Exact under the §1
contract. ∎

**20.3.N2 (ASSERTED, retained).** The chirality-orientation obstruction:
the calculus is left–right symmetric until the SM orientation is imported,
so projection reconstructs the helicity-weight geometry but does not derive
why the interaction is left-chiral. The book retains this as an
obstruction, not a theorem; a Projection-only derivation of chirality
selection is declared Class B (unspecified). Retained as stated.

**20.4.T1 (PROVED, conditional on I-Coulomb).** The Coulomb structural
angle a satisfies `sin a = Zα` and the kinematic angle χ satisfies
`sin χ = β`, with a encoding the daughter-nucleus Coulomb coupling and χ
the electron's mass-shell kinematics — two independently imported data
(**I-Coulomb**). If a = χ on the common branch, then `Zα = sin a = sin χ =
β`, forcing the emitted electron's velocity to equal Zα at every emission
energy, i.e. collapsing the imported continuous beta spectrum to a
charge-selected velocity — contradiction with the imported continuous
spectrum. Hence a and χ are generically independent; the identification is
refuted. ∎

**20.4.T2 (PROVED).** `ξ = Zα/β = sin a/sin χ` by T1's definitions. With
`u = tan(a/2)`, `q = tan(χ/2)`, L1 gives `sin a = 2u/(1+u²)`,
`sin χ = 2q/(1+q²)`, so `ξ = [2u/(1+u²)]/[2q/(1+q²)] = u(1+q²)/(q(1+u²))`.
Exact. ∎

**20.4.T3 (PROVED, conditional on the stated allowed-approximation
integrand, ST).** The allowed beta phase-space weight is the standard
`∝ pE(E₀−E)²` form (ST, imported; E₀ the endpoint energy, **I-Coulomb**).
Under the §1 chart: `β = sin χ = 2q/(1+q²)`, `E = m sec χ = m(1+q²)/(1−q²)`,
`p = Eβ = 2mq/(1−q²)`, all rational in q; the endpoint maps to
`q₀ = tan(χ₀/2)` with `E₀ = m sec χ₀`, rational in q₀. Substituting gives a
phase-space measure rational in (q, q₀) on the branch. ∎

**20.4.N3 (ASSERTED, retained).** The relativistic Fermi function keeps its
non-elementary core `exp(πξ)|Γ(λ+iξ)|²`: the half-angle substitution
rationalizes the kinematic and projective layers but the complex-Gamma
Coulomb scattering dynamics is not generated by the finite rational
primitive closure. The book states this as a retained obstruction; the
Fermi function, nuclear matrix elements, radiative and finite-size
corrections, endpoint energy, and nuclear radius R are named imports. No
proof of the non-elementarity is given here; retained as ASSERTED with the
imports named.

**20.5.W1–W9 (correspondence identities PROVED conditional; stripping
verdict ASSERTED).** Each witness's exact correspondence is a short
analytic check, proved here; each stripping argument is the book's
redundancy analysis, retained as ASSERTED; the terminal verdict
(no Projection-specific invariant survives) is the book's audit
conclusion, retained as ASSERTED.

- *W1 Jones:* the standard Jones vector `(cos(α/2), sin(α/2)e^{iφ})`
  (ST, **I-EM**) has component ratio `e^{iφ} tan(α/2) = e^{iφ} sxp(α)`;
  exact by definition of sxp. Phase φ and intensity scale A² are
  independent imported coherency/Stokes data (ST). PROVED conditional.
- *W2 Duality:* with `2V = cos 2x`, `4H = sin 2x`, the pair (2V, 4H) is a
  unit vector at angle 2x; the shift x ↦ x+δ acts as the SO(2) rotation by
  2δ on it. Exact SO(2) duality-rotation action. PROVED. That constant
  duality is an accepted symmetry, not a new prediction, is the book's
  retained assessment (ASSERTED).
- *W3 Native carrier:* N2 above (PROVED). Direct H↔E, V↔B assignment fails
  an ordinary traveling wave, and the potential-first contract A ∝ H
  reproduces the standard wave after differentiation — the book's repair
  analysis, which reproduces Maxwell rather than a new law; retained as
  ASSERTED (the full differentiation check against the Maxwell system is
  the book's, **I-EM**).
- *W4 Local duality:* making the duality angle spacetime-dependent
  introduces an SO(2) connection; the standard gauge argument gives zero
  curvature for a scalar-only promotion with no kinetic term (ST,
  **I-EM**); the book's conclusion "pure gauge; does not defeat C0" is
  retained as ASSERTED.
- *W5 Newman–Penrose:* NP boost weights are reciprocal tetrad-gauge
  weights (ST, **I-EM**); they match cxp/crx by the K1 identity. PROVED
  conditional; "tetrad-gauge weights, not new observables" retained as
  ASSERTED.
- *W6 Null Maxwell spinor:* `[1:w:w²]` is the degree-two Veronese map
  CP¹ → CP² by definition; it covers the null rank-one sector only, the
  restriction to that sector being the book's imported specification
  (**I-EM**). PROVED (map form) conditional.
- *W7 Two CP¹ factors:* polarization CP¹ and propagation-direction CP¹ are
  independent state spaces (ST, **I-EM**); a CP¹ has 2 real degrees of
  freedom, two independent factors have 4, and one real scalar carries 1 —
  so one real scalar cannot supply both. PROVED (dimension count).
- *W8 Conformal dressing:* in four dimensions the vacuum Maxwell equations
  are conformally invariant on 2-forms (ST, **I-EM**); a scalar conformal
  factor therefore changes nothing in source-free propagation. Stated as
  imported standard theorem (ASSERTED here).
- *W9 Helicity coincidence:* at β = 1/2 the weak odds (1+β)/(1−β) = 3:1
  exactly (arithmetic from V1); the electromagnetic sector's q = 1/2
  coincidence is numerical. Arithmetic PROVED; "promotes no cross-sector
  law" retained as ASSERTED.

**20.6.F1 (PROVED, from D-Δ_op).** Let M_P be related to M_0 by an
invertible representation change R: a bijection on the representation
labels such that every operational configuration c receives the same
outcome probabilities, `P_P(·|c) = P_0(·|c)` — invertibility means no
operational content is added or lost by R. Then for every c ∈ C_exp the
predictions coincide, so `Δ_op(M_P, M_0) = ∅`. An invertible
representation change cannot create a nonempty Δ_op. ∎

**20.6.F2 (PROVED, from D-Δ_op).** Class B is defined by Δ_op
*undefined*. An open ansatz has no prediction set; it therefore cannot
exhibit a nonempty prediction-difference set and cannot falsify C0.
Incompleteness is not novelty. ∎

**20.6.A1 (PROVED, conditional on the correspondence proofs).** Each fully
specified construction of §§1–5 — the kinematic dictionary (K1), the
completed spinor (S1), the V−A odds (V1), the two-angle beta rewrite
(T1–T3), every EM witness (W1–W9) — is, by the proofs above, an exact
invertible coordinate/parametrization correspondence on its declared
branch, conditional on the named imports. By F1 each has Δ_op = ∅, i.e.
Class A. ∎

**20.6.A2 (ASSERTED, status declarations).** The book assigns Class B to:
bare native-carrier embedding (no complete contract/dynamics — cf. N2),
Projection-only chirality selection (orientation not derived — cf. N2 of
§3), scalar-only local duality dynamics (unfinished proposal — cf. W4).
These are the book's correctly scoped status declarations; retained as
ASSERTED.

**20.6.C0 closure (PROVED, conditional theorem about the book's
content).** By A1, every fully specified construction of Book 20 has
Δ_op = ∅; by A2/F2, the unfinished proposals are Class B and do not
constitute Class-C counterexamples. Hence no construction of Book 20
alters the invariant predictions of its accepted reference theory: C0 —
Projection Craft changes representation but not physics — is retained as
the undefeated null hypothesis *for the content of this book*. The book
tags this EXACT; the exact part is the audit logic over the book's own
inventory, which is what is proved here. Falsifiability is preserved: a
future fully specified Class-C model with a stated measurement contract
would defeat C0, and nothing here is a universal no-go. ∎

## D. New axioms/assumptions beyond Euclid + seed + earlier books

1. **B0** — Book 0 primitive calculus and one-generator reduction
   (rewrite Book 0): `book0_proof.md` was not on disk; enters as an
   ASSERTED premise pending that audit.
2. **D-χ** — the kinematic angle contract `sin χ = β`, `cos χ = m/E` on
   the positive-energy branch: declared coordinate contract, not derived.
3. **I-SR** — special-relativistic kinematics import: mass shell
   `E² − p²c² = m²c⁴`, β, γ, rapidity η with `e^η = (E+pc)/mc²`.
4. **I-Dirac** — free-Dirac lower/upper spinor component ratio
   `pc/(E+mc²)` (standard representation): imported, not derived.
5. **I-Bloch** — two-state geometry (Bloch sphere) for spinor completion;
   the independent relative phase φ is declared independent data.
6. **I-VA** — Standard Model left-chiral projector `P_L = (1−γ⁵)/2` and
   massive helicity weights `(1±β)/2`: imported, not derived.
7. **I-Coulomb** — Coulomb structural angle (`sin a = Zα`,
   `cos a = √(1−(Zα)²)`), relativistic Fermi function
   `exp(πξ)|Γ(λ+iξ)|²`, nuclear matrix elements, radiative and finite-size
   corrections, endpoint energy, nuclear radius R, and the radial
   Dirac–Coulomb paper's Coulomb circle: imports, not derived.
8. **I-EM** — standard electromagnetic imports: vacuum Maxwell system and
   traveling waves, Jones vector/coherency/Stokes data, SO(2) duality
   covariance, Newman–Penrose tetrad formalism, CP¹ state spaces, and the
   conformal invariance of 4D vacuum Maxwell on 2-forms: stated, not
   proved here.

No new Euclidean postulate or common notion is introduced; no Elements
proposition is used or extended.

## E. Scope notes

- The book's own status discipline (EXACT / CONDITIONAL / IMPORT /
  OBSTRUCTION) is preserved: every CONDITIONAL item above keeps its
  imports named; every IMPORT stays an import; every OBSTRUCTION is
  retained, not repaired.
- The strongest positive results retained (book's §6 verdict): the
  one-contract kinematic dictionary (sxp ↔ Dirac ratio, cxp ↔ e^η,
  cxp·crx = 1 as mass shell); the independent-phase spinor completion;
  V−A odds as cxp/crx after chiral import; the two-angle beta/Coulomb
  structure with ξ = sin a/sin χ; rational beta phase space; the exact
  native-carrier characterization.
- The strongest negative results retained: one scalar gains no rank from
  many evaluations; chirality orientation not derived; a ≠ χ necessarily;
  no complex-Gamma from rational closure; direct E/B assignment fails;
  local scalar duality is pure gauge; NP weights are tetrad-gauge;
  conformal dressing invisible to source-free Maxwell; helicity sectors
  not identified by coincidence.
- No INCOMPLETE items: nothing timed out or failed; all gaps are named
  ASSERTED premises, per the standing rule to report incomplete work
  plainly.

## F. Counts

- PROVED: 17 — K1, S1, N2 (algebra), V1, T1, T2, T3, W1, W2, W3-carrier
  (same proof as N2), W5-match, W6-map, W7-dimension-count, W9-arithmetic,
  F1, F2, A1, C0-closure — all analytic, complete in the text; zero
  numerical runs (proof-over-sampling rule). Note: N2 serves both §2 and
  W3, counted once.
- CHECKED: 0 — no numeric runs were needed or performed.
- ASSERTED: 11 — N1 (rank obstruction), §3 orientation obstruction, N3
  (complex-Gamma obstruction + named imports), bare-carrier Class B, W3
  potential-first repair, W4 pure-gauge conclusion, W8 conformal
  invariance (ST), §5 no-invariant audit verdict, A2 Class B declarations,
  no-Class-C declaration, B0 pending premise. (D-χ is a declared contract
  in §D, not a claim.)
- INCOMPLETE: 0 — nothing timed out or failed; all gaps are named ASSERTED
  premises.
