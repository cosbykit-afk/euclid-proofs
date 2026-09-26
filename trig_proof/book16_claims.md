# Book 16 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book16_proof.md` (claim inventory
#1–#34 with proofs; rewrite page `~/workspace/r-theory-rewrite/book16/index.html`
— *Book 16 — The Microscopic R Theory*, Part III:
Established / Conditional / Not established). Evaluated 2026-09-22.

**Verification method.** Independent re-derivation, not a copy of the chapter.
All 34 proofs were read in full. The load-bearing analytic identities were
re-derived by hand and check out exactly: the exp-series split
(#1); the tanh double-angle and cosh²−sinh² (#2); projector idempotence from
D4 (#3); the (Π,Ξ) inverse (#12); the selector derivative
R′/R = −3(2y⁴+9y²+2)/[y(y²+2)(2y²+1)] (#13); radial minima (#14); dihedral
relations R²=K, R⁸=I, PRP⁻¹=R⁻¹ (#16); R⁴ centrality (#18); the
Clifford-algebra gamma contraction γ_{μν}γ^ν = 3γ_μ (#30); the Fujikawa
closure e^{−2πik}=1 ∀k∈ℤ (#23); the artanh+sinh cubic coefficient (#27);
the pitchfork V′/V″ ladder, threshold a_c=1/2, spinodal, and δ∗² (#29).
Exact integer arithmetic was re-run computationally (comb(16,4)=1820,
comb(16,6)=8008, the 30380 sums, Alt²(248), Sym²(128), 30380²,
Sym²(30380), the 4/3 ratio, 8128−8008=120, (−1)⁶⁴=+1, the claim-8
determinant −3·2¹⁶k¹⁶) — all exact, exit 0. Items whose evidence is the
book audit's own computation (audit_16a–e.py) or a standard import are
accepted as CHECKED/conditional at the book's scope and labeled honestly;
they were not re-run (proof-over-sampling rule does not apply to them,
but no new run was needed for the audit verdicts).

**Scope labels:** PROVED (exact mathematics shown, complete — conditional
premises named), CHECKED (completed computation, no analytic proof here),
ASSERTED (manuscript claim/assumption/declaration), INCOMPLETE
(unfinished or, here, documented incorrect as proved).

**Euclid boundary:** no proposition of Euclid's *Elements* is a logical
premise of any proof below. The proof file declares the same boundary
(§0, §E: the only Euclid contact is thematic lineage — the §16.I.112
completing-the-square as algebraic descendant of Elements 2.4–2.5, with
no deductive inheritance claimed). No *Elements* citation appears in this
file. Nothing below was folded into the cumulative proof except the
three named principles; reasons are given for the rest.

## PROVED claims (29)

| Claim | Restatement | Scope | Folded in? | Notes |
|---|---|---|---|---|
| 1 | 16.I.49: exp(2xJ)=cos(2x)I+sin(2x)J for J²=−I; ordinary derivative −2I at x=π/4; covariant stationarity ∇ₓB_Z=H′·calZ₂=0 since H′(π/4)=0 | PROVED | **yes — P1 (bridge identity only)** | exp-series split re-derived; derivative checked: 2J·calZ₂=d calZ₂/dx exactly; H′(x)=cos(2x)/2 vanishes at π/4. The stationarity corollary (uses cos(π/2)=0) not folded — reason below |
| 2 | 16.I.59(a): qSaw(tanh w)=tanh 2w; Σ²−Δ²=μ² invariant; lift uniqueness from the ratio argument | PROVED | **yes — P2 (tanh double-angle) and P3 (hyperbolic Pythagorean + radius invariance)** | both identities re-derived exactly; uniqueness is descent algebra, not trig — not folded |
| 3 | 16.I.58: transported projector P(w)²=P(w); coefficient identification | PROVED (conditional on D4's 2×2 Clifford premises) | no | (cosh w·X−sinh w·J)²=cosh²w−sinh²w=1 re-derived; the anticommutator kills the cross term. Clifford algebra, no trig content |
| 5 | 16.I.61/60(b): C(16,4)=1820, C(16,6)=8008; 120+1920+7020+8008+13312=30380; Alt²(248)=30628=248+30380; Sym²(128)=8256=1+1820+6435 | PROVED | no | exact integer arithmetic re-run; the 1⊕1820⊕6435 decomposition itself cited as the proved PROOFS_Casimir theorem (K-1..K-9), not re-proved here |
| 6 | 16.I.71.1: two symmetric copies of 27000 in 30380⊗30380 | PROVED (arithmetic) + ST (LieART 2.1.1 multiplicities, imported) | no | dimension sums verify consistency; the multiplicity statement is a standard import, not derived here |
| 7 | 16.I.71.2: projection ratio (P₂₇₀₀Q⁽²⁾)D=(4/3)(P₃₈₇₅Q⁽²⁾)D | PROVED (conditional on the book's two eigenspace premises) | no | ratio arithmetic 4/3=(4/7)/(3/7) re-run exactly |
| 8 | 16.I.64.E: ambient rank-four witness H(E)=2k[(tr E)I−Eᵀ], spectrum 6k:1,−2k:9,+2k:6, det=−3·2¹⁶k¹⁶ | PROVED (conditional on the manuscript's explicit 16×16 matrix; diagonalization is the book audit's computation) | no | determinant identity 6·(−512)·64=−3·65536 re-run exactly |
| 9 | 16.I.66.4: F=θ⁰∧θ¹, G=θ²∧θ³ ⇒ F∧G≠0, both Pfaffians zero | PROVED | no | Pf(F)=F₀₁F₂₃−F₀₂F₁₃+F₀₃F₁₂=0 re-derived; exterior algebra, no trig content |
| 10 | 16.I.66.1: homogeneous degree-k (k>0) function vanishes at the origin — origin seed impossible | PROVED | no | one-line from homogeneity F(0)=0^kF(v)=0; general algebra |
| 11 | 16.I.64.D: H_C(XF)=(H_C X)F on the branch where the source factors as the same exterior form | PROVED (conditional on the stated branch factorization) | no | not trig |
| 12 | 16.I.76.6: (Π_C I−Ξ_C ∗_L)⁻¹=(Π_C I+Ξ_C ∗_L)/(Π_C²+Ξ_C²) | PROVED (conditional on D8, ∗_L²=−I i.e. AX-16.4) | no | product expands to (Π_C²+Ξ_C²)I re-derived; not trig |
| 13 | 16.I.81: selector ratio strictly monotone each side of y=0; exactly one finite stationary point per nonzero v/u; H_ww^Schur>0 for B₄>0 | PROVED (conditional on the declared fixed shared-form/co-moving reduction) | no | R′ factorization re-derived independently via the logarithmic derivative (matches the stated form exactly); limits and uniqueness argument verified; the Hessian formula is the audit's symbolic check, cited |
| 14 | 16.I.75.11: min of Aq²+Bq⁴ at q*²=−A/(2B), A<0<B | PROVED | no | V″=−4A>0 at the nonzero critical point re-derived; calculus, not a trig identity |
| 15 | 16.I.95.T1: candidate q_Y=exp[iπ(ad D)/4]·𝒳 falsified (eigenspace-exchange vs eigenspace-preservation) | PROVED (conditional on the stated premises) | no | one-line logical obstruction; the anticommutation check is the audit's explicit-matrix computation, cited |
| 16 | 16.I.96.T1: R²=K, R⁸=I, PRP⁻¹=R⁻¹, q_ℓ²=I | PROVED | no | exact 2×2 identities re-derived from D5. **Classification note:** the rotation interpretation is the book's reading; the proof is Clifford/matrix algebra, not a trigonometric identity |
| 17 | 16.I.96.T2: Q_Y-orthogonality ⇒ no ordinary Ward parity forces c_contact=0 | PROVED (conditional on the orthogonality premise) | no | elementary from the premise |
| 18 | 16.I.98.T1/T2: order-16 dihedral presentation; R⁴=−I central; quotient D₄ order 8 | PROVED | no | centrality R⁴=(PRP⁻¹)⁴ re-derived; quotient presentation verified. Same classification note as #16 (group theory, not trig) |
| 19 | 16.I.97.T2: finite-mode Jacobian trivial from det q=(−1)⁶⁴=+1; global anomaly open | PROVED (finite part) + ASSERTED (global anomaly remains open, carried in #33) | no | (−1)⁶⁴=+1 exact; the open part is an assertion, not a result |
| 20 | 16.I.100.T1: quarter dressing not in the Spin(12,4) normalizer (120≠1820) | PROVED (conditional on standard Hodge duality, ST) | no | dimension contradiction verified; not trig |
| 21 | 16.I.101.T2: no full-E8 lift induces the Grassmannian Hodge-complement action | PROVED (conditional on the stated premises) | no | ∩_{A∋v}A^⊥={0} argument is elementary linear algebra; not trig |
| 22 | 16.I.102.T2: Z⁺=Z⁻ the unique positive q-fixed kinetic surface | PROVED (conditional on the manuscript's kinetic-surface premises) | no | uniqueness argument accepted at the book's scope |
| 23 | 16.I.104.T2: oriented Fujikawa closure J(R_D)=1 ∀k∈ℤ | PROVED (conditional on the asserted index divisibility AX-16.2) | no | e^{−iπ·4k/2}=e^{−2πik}=1 re-derived; the trig kernel is elementary but the claim's substance is conditional on an asserted axiom — correctly not promoted |
| 24 | 16.I.109: λ_Xq consistency Re(ab̄)=0 ⇒ φ_a−φ_b=±π/2 mod π, phase lattice φ_a∈(π/4)ℤ | PROVED (at the book's level) | **no — deliberate exclusion, see note** | has genuine angle content, but (a) the needed trig lemma (cos θ=0 ⟺ θ an odd quarter-turn) rests on the zero-structure of cosine, established by no earlier principle and no Euclid proposition (trig is excluded from the Euclid substrate); (b) the cos(φ_a−φ_b)=0 step needs |a||b|≠0, a non-degeneracy the proof file takes from the book's premises. Not forced |
| 25 | 16.I.110.T2: degree four is the first lawful phase-sensitive degree | PROVED (conditional on the Spin(10) invariant-theory premises) | no | not trig — invariant theory |
| 26 | 16.I.112: Schur complement g⁴_eff=−λ₂²/2m_S²; induced-quartic minima at the odd-quarter lattice φ_a=π/4 mod π/2 | PROVED (conditional on the healthy heavy-54 block AX-16.1) | **no — deliberate exclusion, see note** | completing-the-square re-derived; stationary lattice φ_a=nπ/4 and minima at cos 4φ_a=−1 verified. (a) conditional on the asserted AX-16.1 — assertions cannot found principles; (b) its trig kernel (sin 4φ/cos 4φ zero-structure) is not yet established. **Wording slip noted:** the proof file's "d²V/dφ_a² ∝ −16cos 4φ_a is negative exactly at odd quarters" is misstated — at cos 4φ_a=−1 the second derivative is +16C>0 (a minimum); the conclusion (minima at φ_a=π/4 mod π/2) is correct |
| 27 | 16.I.124: kinetic-rapidity cubic (η_N/6+η_N³/3)ω³ vanishes for real η_N only at η_N=0 | PROVED | no | series expansion re-derived term by term; an impossibility result, not a trig identity |
| 28 | 16.I.127: Υ_B=y_B+2δ_Z invariant; instability iff 2λ_B>1 | PROVED (conditional on the stated transformation laws) | no | not trig |
| 29 | 16.I.130: pitchfork V′=δ−a·tanh 2δ−h, V″=1−2a·sech²2δ, threshold a_c=1/2, spinodal δ_s=½arcosh√(2a) | PROVED | no | full derivative ladder re-derived; uses P2's identity (tanh 2δ) as machinery but is bifurcation calculus, not a trig principle |
| 30 | 16.I.88: γ_{μν}γ^ν=3γ_μ in the stated convention | PROVED | no | contraction re-derived from {γ_μ,γ_ν}=2η_{μν}I exactly; Clifford algebra, not trig |

## CHECKED claims (1)

| Claim | Restatement | Scope | Folded in? | Notes |
|---|---|---|---|---|
| 4 | 16.I.59(b): quartic-135 witness — 4-form Q₄ symmetric, traceless, SO(16)-equivariant, nonzero (Q₀₀=9/2) | CHECKED | no | the book audit's explicit computation (audit_16a.py), not re-derived here; exterior algebra/representation, no trig content |

## ASSERTED claims (3)

| Claim | Restatement | Scope | Folded in? | Notes |
|---|---|---|---|---|
| 32 | Sept 15, 2026 synchronization correction: c_ord=1, N_1820=2, K_parent=1 not established; absolute normalization open | ASSERTED | no | the manuscript's own verdict, correctly scoped and recorded |
| 33 | Activation/open gates: λ₂≠0 not forced by E8/T_w/D4 covariance, reduced q parity, or common fermion-pair ancestry (§16.I.114); radius stabilization open; action-level gates (BRST survival, healthy spin-2, mirror selection) open | ASSERTED | no | open physical gates; the global-anomaly open item from #19 is carried here |
| 34 | Δ_op(Book 16)=∅; Volume III closure declarations (Three-Volume Boundary, Master-Retirement Condition antecedent unmet) | ASSERTED | no | status declarations, correctly scoped |

## INCOMPLETE claims (1)

| Claim | Restatement | Scope | Notes |
|---|---|---|---|
| 31 | IC defects: (i) 16.I.80 sign error — boxed h_R(v_a,C)=0 derivation gives 0=0, not the claimed identity (explicit skew counterexample h_R(HC,C)=−1≠0 in audit_16c.py); dependent boxed P_F C=0 and N_scalar,radial=0 incorrect as proved; (ii) line-1614 Schur formula wrong under the ordinary real adjoint (correct form (R_B²/R_D)e^{−θ_D J}); (iii) line-1925 rank biconditional omits the zero-coupling case g_A=g_P=0 (rank 0); (iv) 16.I.106.T2/C1 sign error, retracted by the manuscript itself at 16.I.107 | INCOMPLETE (documented incorrect as proved) | the defects are precisely located and none is papered over |

## Candidate-principle verification (independent)

**P1 — Double-angle bridge identity: exp(2xJ)=cos(2x)I+sin(2x)J for J²=−I.**
CONFIRMED as PROVED: re-derived from the power-series definitions (even/odd
split of the exponential series; absolute convergence justifies regrouping).
Domain: all real x; any real-linear J with J²=−I (book's D3 is the 2×2 model).
Source claim #1 (16.I.49). Scope note: **this is the Book 6 operator Euler
formula (exp(χJ)=cos χ·id+sin χ·J, Principle 1 of the Book 6 chapter) under
the reparametrization χ=2x — identical mathematical content.** It already
appears in the register both as bare "1" (Book 6) and as "1 (Book 15)"
(Double-angle bridge identity). Dedup is handled later per the campaign
plan; recorded here so nothing is double-counted as novel.

**P2 — Hyperbolic double-angle: tanh(2w)=2·tanh(w)/(1+tanh²(w)).**
CONFIRMED as PROVED: re-derived from D1 exponential definitions (the
numerator/denominator ratio reduces exactly to (e^{2w}−e^{−2w})/(e^{2w}+e^{−2w})).
Domain: all real w (cosh w ≥ 1 > 0 everywhere, denominator never zero).
Source claim #2 (16.I.59(a)). Dedup note: the same identity is the Book 14
chapter's tanh double-angle (register row 17); verified on its own merits
here.

**P3 — Hyperbolic Pythagorean identity cosh²(ζ)−sinh²(ζ)=1; radius invariance.**
CONFIRMED as PROVED: re-derived — [(e^ζ+e^{−ζ})²−(e^ζ−e^{−ζ})²]/4 = 1 exactly;
then Σ²−Δ²=μ²(cosh²ζ−sinh²ζ)=μ², and Π_C=Δ/Σ=tanh ζ. Domain: all real ζ,
μ>0. Source claim #2 (16.I.59(a)). No double-counting issue found in the
register for this one.

## Missed-principle scan

No foldable trig principle was missed. The three genuine, independently
established trig/hyperbolic identities are exactly P1–P3. The exclusions are
all documented with reasons:
- #1's 45°-stationarity corollary (needs cos(π/2)=0, a zero-structure fact
  established nowhere yet).
- #2's lift-uniqueness descent algebra (not trig).
- #16/#18 dihedral relations (rotation is the book's reading; the proofs are
  matrix/group theory).
- #23's e^{−2πik}=1 kernel (conditional on the asserted AX-16.2; not promoted).
- #24 phase lattice and #26 odd-quarter selection (judgment calls, excluded
  with stated reasons — see table notes; not errors).
- #29 pitchfork (bifurcation calculus; tanh 2δ is machinery, not the claim).
None of these would be honest principles under the dependency discipline.

## Discrepancies found (chapter vs this audit)

1. **None in the counts.** This independent evaluation yields exactly
   29 PROVED / 1 CHECKED / 3 ASSERTED / 1 INCOMPLETE — matching the chapter's
   29/1/3/1 and the proof file's own inventory.
2. **P1 is not novel content** (see above): it is the Book 6 operator Euler
   formula with χ=2x. The chapter presents it as new ("the circular sibling
   of the seed's (P0) double-angle theorem"); the statement and proof are
   correct, but the register already holds the same identity twice (bare "1"
   and "1 (Book 15)"). This is the reevaluation stage's deduplication work;
   not an error in the math, but the "new" framing overstates.
3. **#26 wording slip in the proof file** (the chapter flagged it too, and
   this audit confirms the flag): "d²V/dφ_a² ∝ −16cos 4φ_a is negative
   exactly at odd quarters" — at the odd-quarter lattice cos 4φ_a=−1, so
   d²V ∝ +16C > 0, a minimum. The conclusion (minima at φ_a=π/4 mod π/2) is
   correct; only the one sentence misdescribes the sign.
4. **#24 non-degeneracy caveat (new, chapter did not state it):** the step
   Re(ab̄)=|a||b|cos(φ_a−φ_b)=0 ⇒ cos(φ_a−φ_b)=0 requires |a||b|≠0; if either
   vanishes the condition holds vacuously. The proof file's lattice
   conclusion inherits this from the book's premises — fine as a conditional
   claim, but the caveat should be on the record.
5. No genuine *Elements* proposition is used anywhere (the proof file's §0
   and §E say so; verified). The §E lineage note to Elements 2.4–2.5 is
   thematic, not deductive, and the per-book2_ledger condition is met.

## Counts

- Evaluated: **34** (29 PROVED, 1 CHECKED, 3 ASSERTED, 1 INCOMPLETE) —
  matches the chapter's 29/1/3/1
- Of the 29 PROVED, 18 carry explicit conditional premises (named in the
  table: 3, 5, 6, 7, 8, 11, 12, 13, 15, 17, 19, 20, 21, 22, 23, 25, 26, 28 —
  for 5 the cited Casimir theorem, for 6 the LieART import, for 19 the
  asserted global-anomaly part); 10 are unconditional (1, 2, 9, 10, 14, 16,
  18, 27, 29, 30); #24 is PROVED at the book's level, conditional on the
  book's non-degeneracy/lattice premises as noted
- Folded into the cumulative proof from this book: **3** (P1, P2, P3), all PROVED

status: complete
