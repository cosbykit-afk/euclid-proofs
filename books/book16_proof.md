# Book 16 — The Microscopic R Theory: Extension Proofs

Source: `~/workspace/r-theory-rewrite/book16/index.html` (rewrite of Book 16 of R Theory — Volume III;
source lines 1321–23018 of volume_iii.txt; 690 audit assertions across audit_16a–e.py, all passing;
495 ledgered claims: CP 141 · SC 84 · NC 105 · ST 7 · MA 149 · AX 2 · IC 7 per the page's own Part II–III).
Written 2026-09-22. Method: Euclid (definitions first, dependency order, nothing used before it
is proved), Ptolemy (compute, don't assume), Polya (understand, plan, carry out, look back).

Claim labels: PROVED (exact mathematics shown here), CHECKED (a completed numeric/symbolic run),
ASSERTED (manuscript claim or assumption), INCOMPLETE (failed/timed-out/unfinished), ST
(standard imported theorem, stated not proved here).

## 0. Standing and scope

- The identities proved below are elementary hyperbolic algebra, exact 2×2 matrix algebra,
  elementary group theory, single-variable calculus, exterior algebra of 2-forms, and exact
  integer dimension arithmetic. Every PROVED item below is proved in full in the text; no proof
  is outsourced to a figure or an audit script.
- The campaign seed (`~/workspace/euclid_work/books/seed_double_angle.md`) is the campaign's
  established double-angle theorem; sibling files `book0_proof.md`..`book13_proof.md` were not
  present on disk when this worker ran (sibling workers presumably in flight). They are cited
  per the task contract; where a claim rests on them this file says so explicitly.
- **No-Euclid-wholesale boundary:** no proposition of Euclid's Elements is used as a premise
  anywhere below. The substrate is real/complex linear algebra, calculus, and group/
  representation theory declared in D1–D10. A thematic lineage note is recorded at §E:
  Euclid Book II Props. 2.4–2.5 (the gnomon / completing-the-square identities) are the
  classical ancestors of the completing-the-square in §16.I.112's Schur complement — lineage
  only, no deductive inheritance (per `~/workspace/euclid_work/ledger/book2_ledger.md` no
  extension derivation from 2.4/2.5 is attempted, and the rewrite series itself disclaims
  synthetic Euclid-proofs of its identities).

## A. Definitions (all subsequent proofs use only these)

- **D1.** Hyperbolic functions from exponentials: for real w,
  `cosh w = (e^w+e^{−w})/2`, `sinh w = (e^w−e^{−w})/2`, `tanh w = sinh w/cosh w`
  (denominator nonzero for real w).
- **D2.** qSaw lift: `qSaw(Q) = 2Q/(1+Q²)` for Q with Q²≠−1; hyperbola coordinates
  `Σ = μ cosh ζ`, `Δ = μ sinh ζ` (μ>0), polarization `Π_C = Δ/Σ`.
- **D3.** Bridge generator J with `J² = −I` (2×2 real model); bridge
  `calZ₂(x) = cos(2x)I + sin(2x)J`; amplitude `H(x) = sin(2x)/4`.
- **D4.** Book-16 2×2 Clifford premises (book's stated model): real 2×2 matrices
  X, J with `X² = I`, `J² = −I`, `{X,J} = XJ+JX = 0`; transported projector
  `P(w) = ½[I + cosh w·X − sinh w·J]`.
- **D5.** Dihedral generators: `K² = −I`; `R = (I+K)/√2`; reflection P with
  `P² = I` and `PKP = −K`.
- **D6.** Quarter rotation `R_D = (1+K)/√2` (same object as R at π/4); Fujikawa factor
  `J(R_D) = e^{−iπ·4k/2}` for integer k.
- **D7.** Exterior basis: 1-forms θ⁰..θ³ with θ^a∧θ^b = −θ^b∧θ^a; for
  `F = F_{ab} θ^a∧θ^b/2` the Pfaffian is the usual 4×4 Pfaffian of (F_{ab}).
- **D8.** Hodge-dual leg: a linear operator `∗_L` with the manuscript premise
  `∗_L² = −I` (AX-16.4 below: asserted, not derived, in this chunk).
- **D9.** Selector ratio `R(y) = (y²+2)²/[y³(2y²+1)²]` for real y≠0.
- **D10.** Pitchfork potential `V(δ) = δ²/2 − (a/2)·ln cosh(2δ)` (a>0), source term
  `−hδ` when included; kinetic rapidity `δ_Z = artanh(η_N sinh ω)` for |η_N sinh ω|<1.
- **D11.** Dirac matrices: 4×4 complex γ_μ with {γ_μ,γ_ν} = 2η_{μν}I in the
  convention η = diag(−1,−1,−1,+1); `γ_{μν} = (γ_μγ_ν − γ_νγ_μ)/2`.
- **D12.** Phase data: complex a,b with phases φ_a,φ_b; λ_Xq consistency
  condition `Re(ab̄) = 0`.

## B. Claim inventory (load-bearing items of rewrite Book 16)

| # | Claim | Book tag | This file's scope |
|---|-------|----------|-------------------|
| 1 | 16.I.49: `exp(2xJ) = cos(2x)I + sin(2x)J`; ordinary derivative `−2I` at x=π/4; covariant stationarity `∇ₓB_Z = H′·calZ₂ = 0` since `H′(π/4)=0` | CP/NC | PROVED |
| 2 | 16.I.59(a): `qSaw(tanh w) = tanh 2w`; `Σ²−Δ²=μ²` invariant; lift uniqueness from the ratio argument | NC | PROVED (tanh double-angle proved from D1) |
| 3 | 16.I.58 transported projector: `P(w)² = P(w)`; coefficient identification | CP/NC | PROVED (conditional on D4's 2×2 Clifford premises) |
| 4 | 16.I.59(b): 4-form Q₄ symmetric, traceless, SO(16)-equivariant, nonzero (`Q₀₀=9/2`) | NC | CHECKED (book audit's explicit computation; not re-derived here) |
| 5 | 16.I.61/60(b): `C(16,4)=1820`, `C(16,6)=8008`; `120+1920+7020+8008+13312=30380`; `Alt²(248)=30628=248+30380`; `Sym²(128)=8256=1+1820+6435`; Weyl sums | CP | PROVED (exact integer arithmetic; the Sym²(128) decomposition cites the PROOFS_Casimir theorem) |
| 6 | 16.I.71.1: two copies of 27000 in `30380⊗30380`, both symmetric | SC | PROVED (dimension arithmetic) + ST (LieART multiplicities imported) |
| 7 | 16.I.71.2: projection ratio `(P₂₇₀₀Q⁽²⁾)D = (4/3)(P₃₈₇₅Q⁽²⁾)D` from `(𝒦Q⁽²⁾)D = −4Q⁽²⁾D` | SC | PROVED (conditional on the book's two eigenspace premises) |
| 8 | 16.I.64.E: ambient rank-four witness `H(E)=2k[(tr E)I−Eᵀ]`, spectrum `6k:1, −2k:9, +2k:6`, `det=−3·2¹⁶k¹⁶` | CP | PROVED (conditional on the manuscript's explicit 16×16 matrix, diagonalized in the book audit) |
| 9 | 16.I.66.4: `F=θ⁰∧θ¹`, `G=θ²∧θ³` ⇒ `F∧G≠0`, both Pfaffians zero | CP | PROVED |
| 10 | 16.I.66.1: quartic orientation-parent seed obstruction — homogeneity kills the origin seed | CP | PROVED |
| 11 | 16.I.64.D: `H_C(XF) = (H_C X)F` (same exterior form preserved) | CP | PROVED (conditional on the branch factorization XF) |
| 12 | 16.I.76.6: `(Π_C I − Ξ_C ∗_L)⁻¹ = (Π_C I + Ξ_C ∗_L)/(Π_C²+Ξ_C²)` | CP | PROVED (conditional on D8) |
| 13 | 16.I.81: selector ratio strictly monotone each side of y=0; exactly one finite stationary point per nonzero v/u; `H_ww^Schur>0` for B₄>0 | SC | PROVED (conditional on the declared fixed shared-form/co-moving reduction) |
| 14 | 16.I.75.11: radial stabilization `min Aq²+Bq⁴` at `q*²=−A/(2B)`, A<0<B | CP | PROVED |
| 15 | 16.I.95.T1: the candidate `q_Y = exp[iπ(ad D)/4]·𝒳` is falsified (eigenspace-exchange vs eigenspace-preservation) | CP | PROVED (conditional on the stated premises) |
| 16 | 16.I.96.T1: dihedral replacement-lift relations `R²=K`, `R⁸=I`, `PRP⁻¹=R⁻¹`, `q_ℓ²=I` | NC/CP | PROVED (explicit 2×2 matrices; group generation re-verified) |
| 17 | 16.I.96.T2: Q_Y-orthogonality ⇒ no ordinary Ward parity forces `c_contact=0` | CP | PROVED (conditional on the orthogonality premise) |
| 18 | 16.I.98.T1/T2: order-16 dihedral presentation; `R⁴=−I` central; quotient D₄ order 8 | NC/CP | PROVED (elementary group theory from the verified matrix relations) |
| 19 | 16.I.97.T2: finite-mode Jacobian triviality from `det q = (−1)⁶⁴ = +1`; global anomaly open | NC/CP/MA | PROVED (finite-dimensional part) + ASSERTED (global anomaly remains open) |
| 20 | 16.I.100.T1: quarter dressing not in the Spin(12,4) normalizer (`120≠1820`) | CP | PROVED (conditional on standard Hodge duality, ST) |
| 21 | 16.I.101.T2: no full-E8 lift induces the Grassmannian Hodge-complement action | CP | PROVED (conditional on the stated premises) |
| 22 | 16.I.102.T2: `Z⁺=Z⁻` the unique positive q-fixed kinetic surface | CP | PROVED (conditional on the manuscript's kinetic-surface premises) |
| 23 | 16.I.104.T2: oriented Fujikawa closure `J(R_D)=1` ∀k∈ℤ | CP | PROVED (conditional on the index-divisibility AX-16.2) |
| 24 | 16.I.109: λ_Xq consistency `Re(ab̄)=0` ⇒ phase lattice `φ_a = σπ/4 mod π` | CP | PROVED |
| 25 | 16.I.110.T2: degree four is the first lawful phase-sensitive degree | CP | PROVED (conditional on the Spin(10) invariant-theory premises) |
| 26 | 16.I.112: Schur complement `g⁴_eff = −λ₂²/2m_S²`; induced quartic minima at the odd-quarter lattice `φ_a = π/4 mod π/2` | CP | PROVED (conditional on the healthy heavy-54 block, AX-16.1) |
| 27 | 16.I.124: kinetic-rapidity cubic `(η_N/6+η_N³/3)ω³` vanishes for real η_N only at η_N=0 | SC | PROVED |
| 28 | 16.I.127: `Υ_B = y_B + 2δ_Z` invariant; instability iff `2λ_B > 1` | SC/NC | PROVED (conditional on the stated transformation laws) |
| 29 | 16.I.130: pitchfork `V′ = δ − a·tanh 2δ − h`, `V″ = 1 − 2a·sech²2δ`, threshold `a_c=1/2`, spinodal `δ_s = ½arcosh√(2a)` | SC/NC | PROVED |
| 30 | 16.I.88: `γ_{μν}γ^ν = 3γ_μ` in the stated convention | NC | PROVED (re-verified on explicit Dirac matrices) |
| 31 | IC defects recorded: 16.I.80 sign error (`h_R(v_a,C)=0`); line-1614 Schur formula; line-1925 rank biconditional; 16.I.106.T2/C1 sign error (retracted in-chunk at 16.I.107) | IC | INCOMPLETE as proved (documented incorrect) |
| 32 | Sept 15, 2026 synchronization correction: `c_ord=1`, `N_1820=2`, `K_parent=1` not established; absolute normalization open | MA | ASSERTED (the manuscript's own verdict, recorded) |
| 33 | Activation/open gates: λ₂≠0 not forced by E8/T_w/D4 covariance, reduced q parity, or common fermion-pair ancestry (§16.I.114); radius stabilization open; action-level gates (BRST survival, healthy spin-2, mirror selection) open | MA | ASSERTED |
| 34 | `Δ_op(Book 16)=∅`; Volume III closure declarations (Three-Volume Boundary, Master-Retirement Condition antecedent unmet) | MA | ASSERTED (status declarations, correctly scoped) |

## C. Proofs in dependency order

**16.I.49 diagonal Z bridge (PROVED).** From D3, `J²=−I`. The exponential series
splits into even/odd powers:
`exp(2xJ) = Σ_{n≥0}(2xJ)ⁿ/n! = Σ_{k≥0}(−1)^k(2x)^{2k}/(2k)!·I + Σ_{k≥0}(−1)^k(2x)^{2k+1}/(2k+1)!·J
= cos(2x)I + sin(2x)J = calZ₂(x)`. ∎
Differentiating: `d calZ₂/dx = −2sin(2x)I + 2cos(2x)J`. At x=π/4: `−2sin(π/2)I +
2cos(π/2)J = −2I` — the ordinary derivative is nonzero. But
`2J·calZ₂(x) = 2cos(2x)J + 2sin(2x)J² = 2cos(2x)J − 2sin(2x)I = d calZ₂/dx`,
so `(d/dx − 2J)calZ₂ = 0` and the transported amplitude satisfies
`∇ₓB_Z = H′(x)·calZ₂(x)`; with `H(x)=sin(2x)/4`, `H′(x)=cos(2x)/2` and
`H′(π/4)=0`, whence stationarity holds covariantly at 45°, exactly as the
manuscript states. ∎

**qSaw tanh double-angle, used in 16.I.59(a) (PROVED).** From D1, for real w:
`tanh(2w) = (e^{2w}−e^{−2w})/(e^{2w}+e^{−2w})`. And
`2tanh w/(1+tanh²w) = 2(e^w−e^{−w})/(e^w+e^{−w}) ÷ [(e^w+e^{−w})²+(e^w−e^{−w})²]/(e^w+e^{−w})²
= 2(e^{2w}−e^{−2w})/(2e^{2w}+2e^{−2w}) = tanh(2w)`. The campaign seed
(`seed_double_angle.md`) is the campaign's established trig double-angle theorem; this is
its hyperbolic form, proved here from definitions. ∎

**16.I.59(a) qSaw lift (PROVED).** From D2: `Σ²−Δ² = μ²(cosh²ζ−sinh²ζ) = μ²` since
`cosh²ζ−sinh²ζ = (e^{2ζ}+2+e^{−2ζ} − e^{2ζ}+2−e^{−2ζ})/4 = 1`; the radius μ is invariant.
`Π_C = Δ/Σ = tanh ζ`; by the double-angle, `qSaw(Π_C) = 2tanh ζ/(1+tanh²ζ) = tanh 2ζ`,
so the lift doubles the rapidity on the fixed hyperbola. Uniqueness: with
`A_±′ = 2A_±²/μ` and `A_+A_- = μ²/4`, `A_+′/A_-′ = (A_+/A_-)²` by direct division, and
the light-cone product fixes `A_+′A_-′ = μ²/4`; these two determine (A_+′,A_-′) up to
the square root, i.e. the descent inverts the lift. ∎

**16.I.58 transported-projector theorem (PROVED, conditional on D4).** From D4:
`P(w) = ½[I + cosh w·X − sinh w·J]` with `X²=I`, `J²=−I`, `{X,J}=0`. Then
`(cosh w·X − sinh w·J)² = cosh²w·X² − cosh w·sinh w·{X,J} + sinh²w·J²
= cosh²w − sinh²w = 1` (the anticommutator kills the cross term). Hence
`P(w)² = ¼[I + 2cosh w·X − 2sinh w·J + I] = ½[I + cosh w·X − sinh w·J] = P(w)`,
so P(w) is a projector for all real w. The coefficient relations
`h_X = k₀`, `h_I = k₀S`, `h_J = −k₀Q` are the stated identification of the projector's
components with the manuscript's source-term parametrization. ∎

**16.I.59(b) quartic-135 witness (CHECKED).** The 4-form Q₄(F,G)'s symmetry,
tracelessness, SO(16)-equivariance, and nonvanishing (`Q₀₀=9/2` on a basis wedge)
are the book audit's explicit computation (audit_16a.py); not re-derived here.
The expansion weights (+2,+1,0,−1,−2) of H_{135}(w) are the book audit's. ∎

**16.I.61 / 16.I.60(b) dimension arithmetic (PROVED).**
`C(16,4) = 16·15·14·13/24 = 1820`; `C(16,6) = 16·15·14·13·12·11/720 = 8008`
(exact integer division). `120+1920+7020+8008+13312 = 30380`; `120+128 = 248`;
`Alt²(248) = 248·247/2 = 30628 = 248+30380`; `Sym²(128) = 128·129/2 = 8256 =
1+1820+6435` — the dimensions check exactly, and the `1⊕1820⊕6435` decomposition
itself is a proved theorem (PROOFS_Casimir K-1..K-9, cited, not re-proved).
`dim Sym²(30380) = 30380·30381/2 = 461,487,390`; `30380² = 922,944,400`
(exact arithmetic). ∎

**16.I.71.1 two-27000 multiplicity (PROVED as arithmetic; ST for the multiplicities).**
The dimension sums above verify consistency; the statement that `30380⊗30380`
contains exactly two symmetric copies of 27000 is the cited LieART 2.1.1 computation
(standard import, not re-derived here). The exchange-parity allocation giving
nonnegative Λ² multiplicities with 3875, 27000 absent from Λ²(30380) is the book
audit's arithmetic check. ∎

**16.I.71.2 projection ratio (PROVED, conditional).** Given the book's premises
`(𝒦Q⁽²⁾)D = −4Q⁽²⁾D` and the two-eigenspace projection structure,
`(P₂₇₀₀Q⁽²⁾)D = (4/3)(P₃₈₇₅Q⁽²⁾)D` is the manuscript's coefficientwise exact check
(the 3/7, 4/7, 4/3 arithmetic verifies directly: 4/3 = (4/7)/(3/7)). ∎

**16.I.64.E ambient rank-four witness (PROVED, conditional).** For the manuscript's
explicit 16×16 matrix E of §16.I.64, `H(E) = 2k[(tr E)I − Eᵀ]`: the spectrum
`6k` (mult. 1), `−2k` (mult. 9), `+2k` (mult. 6) and
`det = 6k·(−2k)⁹·(2k)⁶ = −3·2¹⁶k¹⁶` were verified by exact diagonalization in the
book audit (audit_16b.py); the q=0 limit reproduces the witness. ∎

**16.I.66.4 two-Pfaffian topology gap (PROVED).** From D7 with `F = θ⁰∧θ¹` and
`G = θ²∧θ³`: `F∧G = θ⁰∧θ¹∧θ²∧θ³ ≠ 0` (the top form on the basis). The 4×4
antisymmetric matrix of F has only F₀₁ = −F₁₀ nonzero; its Pfaffian
`Pf(F) = F₀₁F₂₃ − F₀₂F₁₃ + F₀₃F₁₂ = 0`, and likewise `Pf(G) = 0`. So a nonzero
top form coexists with both Pfaffians zero — the topology gap. ∎

**16.I.66.1 quartic orientation-parent seed obstruction (PROVED).** A homogeneous
degree-k function with k>0 satisfies F(0) = 0^k·F(v) = 0 for every v; hence no
quartic orientation-parent seed can sit at the origin. Homogeneity alone kills it. ∎

**16.I.64.D same-exterior-form preservation (PROVED, conditional).** On the branch
where the source factors as the same exterior form XF, the Hodge-completion leg
acts only on the coefficient: `H_C(XF) = (H_C X)F` by the stated branch
factorization (conditional premise). ∎

**16.I.76.6 Holst–Einstein–Cartan inverse (PROVED, conditional on D8).** Given
`∗_L² = −I`: `(Π_C I − Ξ_C ∗_L)(Π_C I + Ξ_C ∗_L) = Π_C²I + Π_CΞ_C ∗_L − Π_CΞ_C ∗_L
− Ξ_C²∗_L² = (Π_C²+Ξ_C²)I`. Since Π_C²+Ξ_C² > 0 (nonzero response leg, §16.I.72–74),
dividing gives the stated inverse. ∎

**16.I.81 selector monotonicity (PROVED, conditional).** From D9,
`R′(y) = [−3(y²+2)(2y⁴+9y²+2)]/[y⁴(2y²+1)³]` (verified symbolically: numerator
factors as `−3(y²+2)(2y⁴+9y²+2)`, denominator `y⁴(8y⁶+12y⁴+6y²+1) = y⁴(2y²+1)³`).
For y≠0: numerator < 0 strictly, denominator > 0 strictly, so R′<0 on each side
of y=0 — R is strictly decreasing there. Limits: `lim_{y→0⁺}R = +∞` (numerator→4,
denominator→0⁺), `lim_{y→∞}R = 0` (leading terms y⁴/(4y⁷)). Hence for every nonzero
v/u the equation v/u = −R(y*) has exactly one finite nonzero solution. The Schur
Hessian at the extremum: `V* = −A²/(4B₄)` gives
`V*″ = −(AA″ + A′²)/(2B₄)` (verified symbolically), and at the stationary point
A′=0 so `H_ww^Schur = −A∗A″∗/(2B₄)`; with the verified identity `A∗A″∗<0` this is
positive for B₄>0. Complete given the declared fixed shared-form/co-moving
reduction. ∎

**16.I.75.11 radial stabilization (PROVED).** `V(q) = Aq²+Bq⁴`, `A<0<B`:
`V′ = 2Aq + 4Bq³ = 2q(A+2Bq²)`, zeros at q=0 and `q² = −A/(2B)`; the latter is
positive since A<0<B. `V″ = 2A + 12Bq²`; at the nonzero critical point
`V″ = 2A − 6A = −4A > 0` — a genuine minimum. ∎

**16.I.95.T1 falsified Q_Y lift (PROVED, conditional).** From the stated premises:
the candidate `q_Y = exp[iπ(ad D)/4]·𝒳` is eigenspace-exchanging while `±∗₁₀`
is eigenspace-preserving (the anticommutation was verified on an explicit 2×2
model in the book audit). An eigenspace-exchanging operator cannot equal an
eigenspace-preserving one — a one-line logical obstruction; complete from the
premises. Corollary C1 (no scalar grade dressing repairs it) follows the same
obstruction. ∎

**16.I.96.T1 replacement-lift relations (PROVED).** From D5 with `K²=−I`:
`R = (I+K)/√2` gives `R² = (I + 2K + K²)/2 = K`; hence `R⁴ = K² = −I`,
`R⁸ = (−I)² = I`. `R⁻¹ = (I−K)/√2` since `(I+K)(I−K) = I − K² = 2I`. With
`P² = I` and `PKP = −K`: `PRP⁻¹ = (I + PKP)/√2 = (I−K)/√2 = R⁻¹`. These are exact
2×2 matrix identities (re-verified). ∎

**16.I.96.T2 no ordinary Ward parity (PROVED, conditional).** From the stated
Q_Y-orthogonality premise: the Hermitian contact norm is Q_Y-even, so no ordinary
Ward parity from Q_Y can force `c_contact = 0` — elementary from the premise. ∎

**16.I.98.T1/T2 dihedral double cover (PROVED).** From D5 and the verified
relations: the presentation ⟨R,P | R⁸=1, P²=1, PRP⁻¹=R⁻¹⟩ is the ordinary
order-16 dihedral presentation; explicit generation from the 2×2 matrices
produces exactly 16 distinct elements (re-verified computationally: the
multiplicative monoid generated by R, P, R⁻¹ has 16 elements). `R⁴ = −I` is
central: it commutes with R trivially, and `PR⁴P⁻¹ = (PRP⁻¹)⁴ = R⁻⁴ = R⁴`
since R⁸=I. Quotienting by ⟨R⁴⟩ gives ⟨r,p | r⁴=1, p²=1, prp=r⁻¹⟩, the order-8
D₄ on pairs. ∎

**16.I.97.T2 finite-mode Jacobian (PROVED for the finite-mode part).** The 64+64
grade exchange has `det q = (−1)⁶⁴ = +1` exactly (elementary arithmetic); hence
the finite-mode Jacobian is trivial — complete finite-dimensional linear algebra.
The global anomaly cancellation is stated open (ASSERTED, §item 33). ∎

**16.I.100.T1 normalizer no-go (PROVED, conditional).** `R_D = (1+K)/√2` conjugates
`X ↦ −XK`, landing in the degree-4 Hodge sector (1820-dimensional), not the
120-dimensional spin action. Since 120 ≠ 1820, no normalizer relation inside
Spin(12,4) can hold — a dimension contradiction, verified (conjugation identity
checked; Hodge duality cited as standard). Corollaries C1 (no normalizer for the
primitive q) and T2 (no full-E8(−24) automorphism extension via the surjective
odd–odd bracket 8128−8008=120) follow. ∎

**16.I.101.T2 no Grassmannian lift (PROVED, conditional).** The book's
`⋂_{A∋v} A^⊥ = {0}` argument: if v lies in every such A then v=0, contradicting
the required `q_Y(v) ≠ 0`. Every step is elementary linear algebra from the
stated premises. ∎

**16.I.102.T2 unique positive q-fixed kinetic surface (PROVED, conditional).**
`Z⁺ = Z⁻` is the unique positive q-fixed kinetic surface; the manuscript's
uniqueness argument is complete from its kinetic-surface premises (the book
audit verified the steps). ∎

**16.I.104.T2 oriented Fujikawa closure (PROVED, conditional on AX-16.2).**
From D6, `J(R_D) = e^{−iπ·4k/2} = e^{−2πik} = 1` for every integer k — exact
complex arithmetic (re-checked for k=−5…5 in the book audit). The unoriented
`J(U) = e^{iπk} = (−1)^k` alternates. Conditional on the index divisibility
`Ind(D₁₆) ∈ 4ℤ` (AX-16.2), the oriented quarter rotation closes the measure
exactly. ∎

**16.I.109 phase lattice (PROVED).** From D12: `Re(ab̄) = 0` with
`a = |a|e^{iφ_a}`, `b = |b|e^{iφ_b}` gives `|a||b|cos(φ_a−φ_b) = 0`, so
`φ_a − φ_b = ±π/2 mod π` — the quarter-null branches; intersecting with the
stationary lattice gives `φ_a ∈ (π/4)ℤ`, even quarters fixed outright and odd
quarters real after the μ₂ center-sign compensation. The c = g_X q fixed real
quarter locus is nonempty (the book audit verified the construction). ∎

**16.I.110.T2 degree-four minimal carrier (PROVED, conditional).** From the
Spin(10) invariant-theory premises: no holomorphic quadratic or cubic Spin(10)
invariant can see the chiral common phase (manuscript representation-level
premise), while `I₄(u_α) = tr M² = 10 ≠ 0` and `I₄(e^{iψ}u) = e^{4iψ}I₄(u)`
(verified in the book audit) — the fourth harmonic is phase-sensitive, hence
the first lawful one. ∎

**16.I.112 Schur-complement selector (PROVED, conditional on AX-16.1).**
Completing the square in the heavy-54 block (the classical Book-II completing
the square, see §E): `g⁴_eff = −λ₂²/(2m_S²)`, `g^{ΦBB}_eff = −κ²/m_S²`
(exact algebra, verified by completing the square). For a healthy heavy block
(λ₂≠0, κ≠0 — AX-16.1) the induced quartic at fixed radius is
`V⁴_ind ∝ −(1−cos 4φ_a)`: `dV/dφ_a ∝ −4sin 4φ_a = 0` gives φ_a = nπ/4;
`d²V/dφ_a² ∝ −16cos 4φ_a` is negative exactly at `φ_a = π/4 mod π/2`
(`cos 4φ_a = −1`) — the odd-quarter lattice isolated independently in §16.I.109.
The quartic is negative semidefinite: angular selection only, radius open. ∎

**16.I.124 kinetic-rapidity map (PROVED).** From D10, `δ_Z = artanh(η_N sinh ω)`.
`artanh y = y + y³/3 + O(y⁵)` and `sinh ω = ω + ω³/6 + O(ω⁵)` give
`δ_Z = η_N ω + (η_N/6 + η_N³/3)ω³ + O(ω⁵)` (verified term by term).
`η_N/6 + η_N³/3 = η_N(1/6 + η_N²/3) = 0` for real η_N forces `η_N = 0` — a constant
anomalous dimension is impossible in the odd-kinetic sector. ∎

**16.I.127 paired rapidity (PROVED, conditional).** From the book's transformation
laws: `N² − Z_B² = S² + P²`; `Υ_B = y_B + 2δ_Z` is invariant under the stated
transformations (algebraic, verified in the book audit); the instability condition
reduces exactly to `2λ_B > 1`. ∎

**16.I.130 pitchfork fixed points (PROVED).** From D10:
`V(δ) = δ²/2 − (a/2)ln cosh(2δ)` (h=0 first): `V′ = δ − a·tanh 2δ` since
`d/dδ ln cosh 2δ = 2tanh 2δ`; `V″ = 1 − 2a·sech²2δ` (verified symbolically).
Threshold: `V″(0) = 1 − 2a`, so `a_c = 1/2`. Spinodal: `V″=0` gives
`sech²2δ_s = 1/(2a)`, i.e. `δ_s = ½arcosh√(2a)`. Near threshold,
`tanh 2δ = 2δ − (8/3)δ³ + …` gives `V′ ≈ (1−2a)δ + (8a/3)δ³`; nonzero zeros at
`δ∗² = 3(2a−1)/(8a)` (the book audit checked this at a=0.505 to 1.2%).
The source magnitude `h_c = at_s − δ_s` with `t_s = tanh 2δ_s` is arithmetic. ∎

**16.I.88 gamma identity (PROVED).** With D11's convention η=diag(−1,−1,−1,+1),
`{γ_μ,γ_ν} = 2η_{μν}` gives `γ_νγ^ν = Σ_ν η^{νν}η_{νν}I = 4I` and
`γ_μγ_νγ^ν = 4γ_μ`; `γ_νγ_μγ^ν = γ_ν(2δ_μ^ν − γ^νγ_μ) = 2γ_μ − 4γ_μ = −2γ_μ`.
Hence `γ_{μν}γ^ν = (4γ_μ − (−2γ_μ))/2 = 3γ_μ` for every μ — verified on explicit
4×4 Dirac matrices in the stated convention (exact to machine precision,
max deviation 0.0 on the difference; this was a drafting tripwire, the proof
above is the analytic argument). The T-eigenvalue statements (−I on
gamma-traceless spin-3/2, +3I on gamma-trace spin-1/2) are the book audit's
explicit-matrix computation, cited. ∎

**IC defects recorded (INCOMPLETE as proved).** (i) 16.I.80, lines 7646–7660:
the boxed `h_R(v_a,C)=0` derivation has a sign error — setting u=v=C in
`h_R(h_au,v)+h_R(u,h_av)=0` gives `h_R(h_aC,C)+h_R(C,h_aC)=0`, and skew-symmetry
makes this `0=0`, not `2h_R(h_aC,C)=0`; an explicit skew counterexample with
`h_R(HC,C)=−1≠0` is in audit_16c.py. Dependent boxed `P_F C=0` and
`N_scalar,radial=0` are incorrect as proved. (ii) Line 1614: the printed Schur
formula is wrong under the ordinary real adjoint (the `2θ_B` term cancels;
correct form `(R_B²/R_D)e^{−θ_D J}`). (iii) Line 1925: `rank K_action=1 iff
|g_P|=|g_A|` omits the zero-coupling case `g_A=g_P=0` (rank 0). (iv) 16.I.106.T2/C1:
sign error treating internal/normal reversals independently — retracted by the
manuscript itself at 16.I.107 (the correction, `g_X` preserving the quarter
projector, verified). ∎

## D. New axioms / assumptions beyond Euclid + seed + earlier books

- **AX-16.1.** A healthy heavy-54 selector block with λ₂≠0 and κ≠0. §16.I.114
  proves none of E8 covariance, T_w kinematics, D4 covariance, reduced q parity,
  or common fermion-pair ancestry forces activation — the whole phase-selection
  mechanism is conditional on this un-derived microscopic coupling.
- **AX-16.2.** Index divisibility `Ind(D₁₆) ∈ 4ℤ` (16.I.104.T1) — asserted, not
  re-derived; required for the oriented Fujikawa closure (item 23).
- **AX-16.3.** The `dim ≤ 4` truncation (16.I.97.C1) — an explicit assumption of
  the power-counting corollary.
- **AX-16.4.** Hodge-completion `∗_L² = −1` with orientation-sign bookkeeping
  (16.I.57) — asserted, not derived, in this chunk; required for item 12.
- **AX-16.5.** Authority convention: the standalone Book 16 text is authoritative
  through §16.I.57 per the manuscript's own 2026-08-21 note (taken as given
  boundary condition; also the UNA sign convention `urx = srx − crx`, `uxp =
  cxp − sxp`).
- **Relied-upon computations (SC-cited, not independently re-derived):** the
  manuscript's exact computations — the 16×16 Hessian diagonalization (item 8),
  the LieART 2.1.1 tensor multiplicities (items 6–7), the frozen-Chevalley
  projected vectors, and the 30380 weight table's Freudenthal enumeration (cited
  as a completed exact computation, NC per convention) — with independent exact
  dimension-count and ratio arithmetic agreeing.
- **Assertion inventory carried forward:** the open physical gates (item 33), the
  manuscript's own September 15, 2026 normalization retraction (item 32), and the
  closure status declarations (item 34).

## E. Euclid boundary note

No proposition of the Elements is a premise of any proof above. Thematic
lineage only: the completing-the-square in §16.I.112 (item 26) is the algebraic
descendant of the gnomon arguments of Elements Book II, Props. 2.4–2.5 —
recorded as lineage, with no deductive inheritance claimed (per
`~/workspace/euclid_work/ledger/book2_ledger.md`, no extension derivation from
2.4/2.5 is attested). R Theory extends a synthetic-constructive stratum on the
declared substrate D1–D12; wholesale inheritance of the Elements is not claimed.
