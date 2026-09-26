# Book 11 — Particle Architecture and Standard Model Comparison: Euclid-style extension proofs

**Rewrite source:** `~/workspace/r-theory-rewrite/book11/index.html` ("Book 11 — Particle
Architecture and Standard Model Comparison (Restructured)"; rewrite of Volume II Book 11,
source lines 2497–4810). The page states every theorem and status label comes from the
original manuscript and no mathematics was added.

**Scope vocabulary (Kit's, non-negotiable):** PROVED = exact mathematics shown here.
CHECKED = a completed computation, cited with its run. ASSERTED = manuscript claim,
declared contract, or adopted assumption — never presented as established. INCOMPLETE =
failed, timed out, unfinished, or deliberately not done. ST = standard imported theorem
(used, not re-proved; listed, not counted).

**Honesty preamble (read before the proofs).**
- The campaign seed (Kit's double-angle identity) is PROVED
  (`euclid_work/books/seed_double_angle.md`). It is **not** needed by Book 11's
  load-bearing chain (the helicity reciprocal identity of §11.PG.IX is a different
  identity, proved independently in T11 below). No false dependency is claimed.
- `euclid_work/books/book6_proof.md` exists and is cited per the task's permission
  (claims P10, P12, P13, P14, each PROVED there conditional on its declared data
  AX-6.1–AX-6.5). I read the cited claims; I did not independently re-verify Book 6's
  proofs. Where Book 11's page labels the same inheritance "MANUSCRIPT ASSERTION not
  independently verified as an inheritance," the citation below supersedes that label
  for the *mathematical* content (the physical non-identification firewalls stand).
- The Volume II manuscript text (source lines 2497–4810) was not available in this
  task; the load-bearing claims are re-derived here from the definitions stated on the
  rewrite page. Where the page's argument depends on manuscript text not reproduced on
  the page, the item stays ASSERTED with the assumption named.
- `validation/book11/verify_book11.py` was re-run by the author of this file on
  2026-09-22: exit 0, all 33 assertions passed (19 CP + 8 NC + 6 SC), no timeouts;
  worst measured numerical error 5.403e-15 (the script's own summary line). CHECKED
  citations below refer to that run.
- Nothing here inherits Euclid's Elements wholesale (see §H). Equational steps use
  only Euclid I Common Notions (equality substitution), as inventoried in
  `euclid_work/ledger/book1_ledger.md`.

---

## A. Claim inventory

| ID | Statement | Scope | Depends on |
|---|---|---|---|
| T1 | UᵀJU = (det U)J for U ∈ GL(2,ℂ); J-preserving ⟺ det U = 1; + Hermitian form ⟺ SU(2); J alone gives SL(2,ℂ) (11.PG.T1) | PROVED | D5 |
| T2 | XᵀJ + JX = (tr X)J; infinitesimal algebra = {X†=−X, tr X=0} = su(2), real dim 3 (11.PG.III) | PROVED | D5 |
| T3 | Pure-gauge A = −dUU⁻¹ gives F = dA + A∧A = 0; local basis variation alone produces no force (11.PG.N1) | PROVED | T1 (U invertible) |
| T4 | JŪJ⁻¹ = U for U ∈ SU(2) (mirror-automorphism lemma, 11.PG.XII) | PROVED | D5 |
| T5 | Unique traceless block phase: 2a+3b=0 forces (a,b) ∝ (1/2,−1/3); normalization conventional (11.III.C) | PROVED (cited) | book6 P12 (cond. AX-6.2) |
| T6 | Φ(A,B,z) = (z³A, z⁻²B): S(U(2)×U(3)) ≅ [SU(2)×SU(3)×U(1)]/ℤ₆; kernel = six roots z⁶=1 (11.III.B) | PROVED | D2 |
| T7 | Primitive integral cocharacter X = i(3I₂⊕−2I₃); weights 0,6,1,−4,2,−3; Y₀ = X/6; primitivity from gcd(3,2)=1 (11.IX.T1, C1) | PROVED | D2, D3 |
| T8 | S₊ = Λ^even W: six blocks, dims 1⊕1⊕6⊕3⊕3⊕2 = 16, Y₀-weights 0,+1,+1/6,−2/3,+1/3,−1/2 (11.IV.T1, T2) | PROVED | D1–D4; ST(Λ²V≅V̄) |
| T9 | A_SU(3)³ = A_SU(3)²Y = A_SU(2)²Y = A_Y³ = A_grav²Y = 0, exact (11.VI.T2–T4) | PROVED (conditional) | T8; AX-C4 (rules) |
| T10 | Vacuum neutrality forces c = 1/6, Q = T₃ + Y₀; full 16-charge pattern exact (11.IX.T2, T3) | PROVED (conditional) | T8; AX-C1, AX-C2 |
| T11 | cxp(χ) = e^η = √[(1+β)/(1−β)], crx = e^{−η}, cxp·crx = 1; P_L↔P_R swaps favored/suppressed (11.PG.IX) | PROVED | D6; ST(Dirac formula) |
| T12 | 10_ℂ dims 2+3+2+3 = 10 with conjugate pairing; 3+1 = 4 doublets, even; g-blindness (11.VIII.T1, 11.VI.T5, 11.VII.T2–T3) | PROVED | T8; D8 |
| T13 | No-go forms: chirality nonselection; singlet-algebra firewall; generation-number blindness; T7 vs Axiom Zero (11.PG.N3, 11.I.B, 11.II.F1, 11.VII.N1, 11.VI.T7) | PROVED (conditional) | T4, T9, T12; A7 |
| K1 | Helicity-odds plotted-curve agreement: max err 1.12e-10 < 1e-9 (V1) | CHECKED | run 2026-09-22 |
| K2 | Λ²V ≅ V* character check: 300 random SU(3), max err 1.3e-15 (V14) | CHECKED | run 2026-09-22 |
| K3 | 10_ℂ branching dims + Sym²(16)=136=10+126, Asym=120, 3⊗3̄, 3⊗3⊗3 decompositions (V18) | CHECKED | run 2026-09-22 |
| K4 | U(2) ≅ (SU(2)×U(1))/ℤ₂ surjectivity/kernel (V10; 6.9e-16) | CHECKED | run 2026-09-22 |
| K5 | ℤ₆ kernel acts trivially on all six blocks; quotient descent (V20) | CHECKED | run 2026-09-22 |
| K6 | Six-block table = one SM generation + neutral singlet under the comparison contract (V25) | CHECKED | run 2026-09-22 |
| A1 | Physical comparison contract 11.V.A (SU(3)↔color, SU(2)↔weak, Y₀↔hypercharge) | ASSERTED | AX-C1 |
| A2 | Doublet scalar + nonzero vacuum 11.IX.P1 | ASSERTED | AX-C2 |
| A3 | Imported standard physics: Dirac+P_L, 4D Lorentzian spin base (Book 9 conditional), Weyl anomaly rules (11.VI.P1), YM candidate-class uniqueness (11.PG.VI), color projection (11.II.E), Dai–Freed/bordism (11.VI.H) | ASSERTED | AX-C4 |
| A4 | Closure theorem 11.X.T1 (summary) + Δ_op(Book 11) = ∅ | ASSERTED | page's own label |
| A5 | Fermionic-ontology firewall 11.IV.G (exterior/Fock realization ≠ fields/statistics/dynamics) | ASSERTED | page's own label |
| A6 | No-go theorems' mirror-symmetric premise data | ASSERTED | AX-C5 |
| A7 | Physical debts ledger: scalar ontology, potential, VEV, masses, doublet–triplet splitting, couplings, θ_W, EW scale, replication, flavor, RG flow | ASSERTED (as open) | page's own ledger |
| I1 | Forward book map Books 12–19: no per-book entries, roadmap only | INCOMPLETE | — |
| I2 | Book 12 "later Casimir correspondence" forward reference | INCOMPLETE | — |
| I3 | Unresolved physical debts (see A7): not derived here | INCOMPLETE | — |
| I4 | Euclid XI 11.1–11.39: no counterpart by the No-Euclid-wholesale boundary | INCOMPLETE (boundary) | §H |

Standard imported theorems used but not proved (ST, not counted): Dirac helicity-weight
formula (§11.PG.IX); 2⊗2 = 3⊕1 with weights ±1/2, 0, ±1; Λ²V ≅ V̄ and Λ³V ≅ 1 (A₂);
16⊗16 = (10⊕126)_s ⊕ 120_a with 1 ∉ Sym²(16); Weyl anomaly rules (11.VI.P1);
L_T,eff = −(β²/4α)K² sign erasure (11.I.E); Euclid I Common Notions.

---

## B. Definitions

**D1 (carrier).** W ≅ ℂ² ⊕ ℂ³, the 2+3 complex block decomposition. Cited PROVED from
`book6_proof.md` P14 (unique faithful complex completion; conditional on declared
premise AX-6.4) and P10 (maximal envelope U(2)×U(3)). Write E = ℂ², V = ℂ³.

**D2 (block groups).** U(2)×U(3) acting blockwise; S(U(2)×U(3)) = {(A,B) : det A·det B = 1};
Lie algebra su(2)⊕su(3)⊕u(1). Cited PROVED from `book6_proof.md` P10, P12
(conditional on AX-6.2, the fixed complex volume form).

**D3 (central generators).** Y₀ = i[(1/2)I₂ ⊕ (−1/3)I₃]; X = i(3I₂ ⊕ −2I₃). Hence
Y₀ = X/6 by inspection. The normalization (1/2, −1/3) is conventional (page, §2:
"normalization and sign remain conventional until a physical U(1) contract is supplied").

**D4 (half-spin module).** S₊ = Λ^even W = ⊕_{p+q even} Λ^pE ⊗ Λ^qV, p ∈ {0,1,2},
q ∈ {0,1,2,3}. The scalar generator (D3) acts additively on exterior products, so its
weight on Λ^pE ⊗ Λ^qV is y(p,q) = p·(1/2) + q·(−1/3) = p/2 − q/3.

**D5 (symplectic unit).** J = [[0,1],[−1,0]] ∈ M₂(ℂ); J² = −I₂, J⁻¹ = −J.

**D6 (helicity coordinates).** sin χ = β; cxp(χ) = e^η, crx(χ) = e^{−η}, where β = tanh η
(rapidity). The helicity-weight formula itself is imported Dirac spinor algebra (ST).

**D7 (conditional reading).** AX-C1 (11.V.A): the comparison contract identifying the
SU(3) block with color, the SU(2) block with weak isospin, the Y₀ weight with
hypercharge. AX-C2 (11.IX.P1): a doublet scalar with nonzero vacuum. Both are
ASSUMPTION OR AXIOM on the page; conclusions using them are conditional.

**D8 (mirror map).** M: weight-sign reversal y ↦ −y, interchanging the six-block pattern
with its mirror (and S_L ↔ S_R candidates). Used only in T13.

---

## C. Proofs in dependency order

### T1 — The J-identity and SU(2) (11.PG.T1). PROVED.

For U = [[a,b],[c,d]] ∈ GL(2,ℂ):
UᵀJ = [[a,c],[b,d]]·[[0,1],[−1,0]] = [[−c,a],[−d,b]];
(UᵀJ)U = [[−c,a],[−d,b]]·[[a,b],[c,d]] = [[0, ad−bc],[bc−ad, 0]] = (ad−bc)J.
Hence **UᵀJU = (det U)J** exactly. Corollary: UᵀJU = J ⟺ (det U − 1)J = 0 ⟺
det U = 1 (J ≠ 0). So the J-preserving subgroup of GL(2,ℂ) is SL(2,ℂ); intersecting
with the Hermitian-form preservers gives U(2) ∩ SL(2,ℂ) = SU(2). Warning, exact:
diag(2,1/2) has det 1 (in SL(2,ℂ)) but is not unitary — preserving J alone does not
give SU(2). This keeps the page's status warning. (The V7 sympy/numeric checks in the
run are consistent with, and unnecessary beside, this proof.)

### T2 — Infinitesimal form (11.PG.III). PROVED.

For X = [[a,b],[c,d]]: XᵀJ = [[−c,a],[−d,b]] (as above); JX = [[c,d],[−a,−b]];
sum = [[0, a+d],[−(a+d), 0]] = (tr X)J. Hence **XᵀJ + JX = (tr X)J** exactly.
The infinitesimal J-preservers with X† = −X and tr X = 0 form su(2): anti-Hermitian
traceless 2×2 matrices, real dimension 3 (basis iσ_k), pseudoreal fundamental. This
is a Lie-algebra fact, not a count of physical particles (page's note kept).

### T3 — Maurer–Cartan negative lemma (11.PG.N1). PROVED.

Let A = −dUU⁻¹ (matrix-valued 1-form). Then dA = −d(dU·U⁻¹) = dU∧d(U⁻¹) (d² = 0,
graded Leibniz). From UU⁻¹ = I, d(U⁻¹) = −U⁻¹(dU)U⁻¹. So
dA = −(dU U⁻¹)∧(dU U⁻¹) = −A∧A, and F = dA + A∧A = 0 exactly. Pure-gauge local basis
variation produces no force. (V15's 40-surface numeric check is consistent.)

### T4 — Mirror-automorphism lemma (11.PG.XII). PROVED.

Let U = [[a,b],[−b̄,ā]] ∈ SU(2). Then Ū = [[ā,b̄],[−b,a]] and
JŪ = [[−b,a],[−ā,−b̄]]; (JŪ)J⁻¹ = [[−b,a],[−ā,−b̄]]·[[0,−1],[1,0]] = [[a,b],[−b̄,ā]] = U.
Hence **JŪJ⁻¹ = U** exactly for U ∈ SU(2). (V9's 2000-matrix check, max err 0.0, agrees.)

### T5 — Unique traceless block phase (11.III.C). PROVED (by citation).

Cited from `book6_proof.md` P12 (PROVED there, conditional on declared AX-6.2): the
u(1) summand is (iaI₂, ibI₃) with 2a+3b = 0; the map (a,b) ↦ 2a+3b has one-dimensional
kernel, so the traceless direction is unique up to scale and sign. Inline check:
2(1/2) + 3(−1/3) = 1 − 1 = 0, so (1/2, −1/3) spans it. Normalization and sign are
conventional (D3; page §2).

### T6 — The ℤ₆ kernel (11.III.B, Figure 6). PROVED.

Define Φ(A,B,z) = (z³A, z⁻²B) for (A,B,z) ∈ SU(2)×SU(3)×U(1).
Image: det(z³A) = z⁶·1 (2×2), det(z⁻²B) = z⁻⁶·1 (3×3); product = 1, so
Φ lands in S(U(2)×U(3)). Surjective: given (A,B) with det A·det B = 1, pick
z ∈ U(1) with z⁶ = det A; set A′ = z⁻³A, B′ = z²B; then det A′ = z⁻⁶det A = 1,
det B′ = z⁶det B = 1, |z| = 1 keeps unitarity, and Φ(A′,B′,z) = (A,B).
Kernel: Φ(A,B,z) = (I,I) ⟺ A = z⁻³I₂, B = z²I₃ with det A = z⁻⁶ = 1,
det B = z⁶ = 1 ⟺ z⁶ = 1 — exactly the six roots. Hence
**S(U(2)×U(3)) ≅ [SU(2)×SU(3)×U(1)]/ℤ₆**. (V11/V20 checks consistent.)

### T7 — Primitive integral cocharacter (11.IX.T1, C1; Figure 4). PROVED.

X(z) = diag(z³,z³, z⁻²,z⁻²,z⁻²) on W = ℂ²⊕ℂ³. If X factored through a d-fold cover
(d ≥ 2), every exponent would be divisible by d; gcd(3,3,−2,−2,−2) = gcd(3,2) = 1,
so no such d exists — X is primitive. On Λ^pE⊗Λ^qV the weight is x(p,q) = 3p−2q:
(0,0)→0, (2,0)→6, (1,1)→1, (0,2)→−4, (2,2)→2, (1,3)→−3 — integers, and
y(p,q) = x(p,q)/6, i.e. **Y₀ = X/6** exactly. The fractions are the lattice divided
by six; the denominator six is tied to the 2+3 block structure (T6's ℤ₆).

### T8 — Six-block weighted branching (11.IV.T1, T2; Figure 2). PROVED.

Even p+q with p ∈ {0,1,2}, q ∈ {0,1,2,3} gives six blocks:
(p,q): (0,0) dim 1·1 = 1; (2,0) dim 1·1 = 1; (1,1) dim 2·3 = 6;
(0,2) dim 1·3 = 3; (2,2) dim 1·3 = 3; (1,3) dim 2·1 = 2.
Sum: 1+1+6+3+3+2 = 16. As representations, using ST Λ²E ≅ 1, Λ³V ≅ 1,
Λ²V ≅ V̄ = 3̄ (A₂; K2 consistent):
(1,1)₀ ⊕ (1,1)_{+1} ⊕ (2,3)_{+1/6} ⊕ (1,3̄)_{−2/3} ⊕ (1,3̄)_{+1/3} ⊕ (2,1)_{−1/2},
with y(p,q) = p/2 − q/3 giving 0, +1, +1/6, −2/3, +1/3, −1/2 exactly
(independently rechecked with exact fractions: all six match the page's table).
Check: Λ⁴W = (Λ¹E⊗Λ³V) ⊕ (Λ²E⊗Λ²V), dims 2+3 = 5 (page's V13). No weight was fitted.

### T9 — Anomaly cancellation (11.VI.T2–T4; Figure 5). PROVED, conditional on AX-C4.

Using T8's table (block: dim, Y): (1,1)₀:1,0; (1,1)₁:1,1; (2,3):6,1/6;
(1,3̄):3,−2/3; (1,3̄):3,1/3; (2,1):2,−1/2. Exact fraction arithmetic:
- A_Y³ = Σ dim·Y³ = 0 + 1 + 6(1/216) + 3(−8/27) + 3(1/27) + 2(−1/8)
  = 1 + 1/36 − 8/9 + 1/9 − 1/4 = (36+1−32+4−9)/36 = 0.
- A_grav²Y = Σ dim·Y = 0 + 1 + 1 − 2 + 1 − 1 = 0.
- A_SU(3)³ ∝ (#3 − #3̄) = 2 − 2 = 0.
- A_SU(3)²Y ∝ ½(2·(1/6) + 1·(−2/3) + 1·(1/3)) = 0.
- A_SU(2)²Y ∝ 3·(1/6) + 1·(−1/2) = 0.
All five vanish exactly. This proves the *arithmetic*; the conclusion "the anomalies
cancel" additionally requires the imported 4D left-handed Weyl anomaly rules
(11.VI.P1) and the chiral interpretation contract — hence conditional (AX-C4, §G).
The representation was not chosen by solving these equations. Chirality-sign
blindness: negating all Y leaves every sum zero (11.VI.N1).

### T10 — Conditional charge pattern (11.IX.T2, T3; Figure 3). PROVED, conditional on AX-C1, AX-C2.

The scalar doublet's neutral component has (T₃, X)-weights (−1/2, +3) (T7's
x(1,0) = 3). Vacuum neutrality for Q = T₃ + cX: −1/2 + 3c = 0 forces **c = 1/6**,
so Q = T₃ + X/6 = T₃ + Y₀. Then Q on T8's blocks (T₃ = ±1/2 on doublets, 0 else):
(2,3)_{1/6} → +2/3 (×3), −1/3 (×3); (1,3̄)_{−2/3} → −2/3 (×3);
(1,3̄)_{+1/3} → +1/3 (×3); (2,1)_{−1/2} → 0, −1; (1,1)₀ → 0; (1,1)₁ → +1.
Sixteen charges {±1, ±2/3, ±1/3, 0}, the one-generation pattern — exact, with no
charge inserted by hand. Conditional throughout on the comparison contract (AX-C1)
and the scalar vacuum (AX-C2); physical identification remains conditional, as the
page states.

### T11 — Helicity reciprocal pair (11.PG.IX; Figure 1). PROVED (identity); formula ST.

With β = tanh η: (1+β)/(1−β) = (coshη+sinhη)/(coshη−sinhη) = e^{2η}, so
**√[(1+β)/(1−β)] = e^η = cxp(χ)** exactly; crx(χ) = e^{−η}; **cxp·crx = 1**.
The helicity-weight formula itself is standard Dirac spinor algebra (ST, imported);
the identity is bookkeeping, exact. Replacing P_L by P_R interchanges the two
projectors, exchanging favored/suppressed with the same reciprocal magnitude — the
correspondence selects no handedness. (K1: the plotted curve agreement, max err
1.12e-10 < 1e-9, is consistent; the seed double-angle identity is not used.)

### T12 — Ten-dimensional branching, doublet parity, multiplicity blindness. PROVED.

- 10_ℂ ≅ (2,1)_{+1/2} ⊕ (1,3)_{−1/3} ⊕ (2,1)_{−1/2} ⊕ (1,3̄)_{+1/3}: dims
  2+3+2+3 = 10 exactly, with conjugate pairing (second pair = mirror of first, D8).
  The full branching isomorphism is CHECKED (K3/V18).
- Doublet–triplet companion (11.VIII.T2): the (1,3)_{−1/3} sits in the same five as
  the (2,1)_{+1/2}; it cannot be silently discarded — immediate from the stated
  decomposition.
- Witten parity (11.VI.T5): SU(2) doublets are 3 (from (2,3)) + 1 (from (2,1)) = 4,
  even — pass, exact.
- Multiplicity blindness (11.VII.T2–T3): with g generations every anomaly coefficient
  and the doublet count scales by g; zeros stay zero and parity stays even — no
  theorem here distinguishes g = 1, 2, 3, … (11.VII.N1). (V21 checked g = 1..6.)

### T13 — Negative theorems (no-go forms). PROVED, conditional on A6.

- **Chirality nonselection** (11.PG.N3, 11.I.B, 11.VI.N1): let D be the data the book's
  rules may use (T8 dims/weights, T9 zeros, T12 parity) — all invariant under the
  mirror map M (D8), and M swaps the S_L/S_R candidates. A selector built only from
  D, applied after M, would select the mirror image equally: no D-built rule prefers
  one. Orientation correlation ≠ orientation selection. Proved from the premise that
  D is mirror-symmetric (ASSERTED, A6 — the page: premises include manuscript data).
- **Singlet-algebra firewall** (11.II.F1): the premises (3⊗3̄ = 1⊕8, 3⊗3⊗3
  decompositions — ST) contain no dynamical law; confinement is dynamical; separation
  of claims gives non-derivability.
- **Generation blindness**: T12. **T7 vs Axiom Zero** (11.VI.T7): anomaly zeros are
  consequences; a true consequence cannot retroactively prove its premise (A⇒B, B
  true ⊬ A) — elementary logic.
- Certificate 11.I.G / 11.VII.F–H (what a future derivation must supply) are
  requirements, not derivations — recorded, not proved.

---

## D. CHECKED items (run: `validation/book11/verify_book11.py`, re-run 2026-09-22, exit 0, 33/33, no timeouts)

- **K1.** V1: helicity-odds curve agreement, max err 1.12e-10 < 1e-9 (supports the ST
  formula's application in T11; the identity itself is proved in T11).
- **K2.** V14: Λ²V ≅ V* SU(3) character check, 300 random, max err 1.3e-15 (supports
  T8's use of the ST isomorphism).
- **K3.** V18: 10_ℂ dims 2+3+2+3 = 10 with conjugate pairing; Sym²(16) = 136 = 10+126,
  Asym = 120; 3⊗3̄ = 1⊕8; 3⊗3⊗3 = 1⊕8⊕8⊕10 (supports T12/T13; Yukawa admissibility
  11.VIII.T3 after a 10-valued field is introduced — the field is a further extension).
- **K4.** V10: U(2) ≅ (SU(2)×U(1))/ℤ₂ surjectivity and kernel, max err 6.9e-16
  (11.PG.VIII, ST).
- **K5.** V20: ℤ₆ kernel acts trivially on all six T8 blocks; quotient descent
  (supports T6's application to the weight table; 11.VI.T1).
- **K6.** V25: six-block table = one SM generation + neutral singlet **under the
  comparison contract** (11.V.T1; the identification is contract-conditional, A1).

Per proof-over-sampling: no numeric sampling was run for any T-item with a complete
analytic proof above; the K-items cite the already-completed validation run.

## E. ASSERTED items (assumption named)

- **A1 (AX-C1).** 11.V.A physical comparison contract — explicitly a physics
  identification, not a premise of T8.
- **A2 (AX-C2).** 11.IX.P1 doublet scalar with nonzero vacuum — field extension.
- **A3 (AX-C4).** Imported standard physics bundle: Dirac structure + P_L (11.PG.IX);
  4D Lorentzian spin base (Book 9's conditional reconstruction); chiral-QFT Weyl
  anomaly rules (11.VI.P1); Yang–Mills candidate S_YM = −(1/2g²)∫tr(F∧∗F) with
  candidate-class uniqueness asserted not proved (11.PG.VI); color projection
  contract (11.II.E); Dai–Freed/bordism witness with restricted background (11.VI.H).
- **A4.** 11.X.T1 closure theorem (a scope-labeled summary, not a derivation) and
  Δ_op(Book 11) = ∅ — the page's own MANUSCRIPT ASSERTION labels kept.
- **A5.** 11.IV.G fermionic-ontology firewall: exterior/Fock realization does not
  establish fields, statistics, or dynamics.
- **A6 (AX-C5).** Mirror-symmetric premise data for the T13 no-go arguments
  (manuscript-supplied).
- **A7.** Physical-debts ledger kept open: scalar ontology, potential, VEV, masses,
  doublet–triplet splitting, couplings g, g′, e, θ_W, EW scale, replication, flavor
  texture, RG flow — explicitly unresolved on the page.

## F. INCOMPLETE items

- **I1.** Forward book map Books 12–19: the section contains no per-book entries
  ("roadmap records, not completed theorem stacks") — nothing to prove.
- **I2.** Book 12 "later Casimir correspondence" forward reference — a claim about a
  book not in this corpus; recorded without endorsement.
- **I3.** The A7 physical debts — not derived here, by the page's own accounting.
- **I4.** Euclid XI 11.1–11.39 — no counterpart (see §H).

## G. New axioms / assumptions beyond Euclid + seed + earlier books

- **AX-C1** (11.V.A): physical comparison contract (A1).
- **AX-C2** (11.IX.P1): doublet scalar + nonzero vacuum (A2).
- **AX-C3**: *none new* — the carrier W ≅ ℂ²⊕ℂ³, envelope U(2)×U(3), S(U(2)×U(3))
  reduction, and su(2)⊕su(3)⊕u(1) with unique traceless direction are cited PROVED
  from `book6_proof.md` P10/P12/P14, conditional on that file's declared data
  AX-6.2 (volume form) and AX-6.4 (common complex carrier), here inherited, not new.
- **AX-C4**: imported standard-physics bundle (A3).
- **AX-C5**: mirror-symmetry premise data for no-go theorems (A6).
- The campaign seed is inherited PROVED and unused by this book's chain (preamble).

## H. No-Euclid-wholesale boundary

Per the book11 Euclid ledger and the No-Euclid-wholesale theorem (4.X.P10): R Theory
does not cite, reprove, or build on any of Euclid XI 11.1–11.39 (I4). The extension
proved here is a synthetic-constructive stratum on the declared substrate (D1–D8 +
AX-C1/C2/C4/C5 + inherited AX-6.2/AX-6.4): exact algebra and representation
combinatorics over the 2+3 carrier, with standard theorems imported by name and
physics identifications admitted as explicit contracts. No wholesale inheritance of
the Elements is claimed; Euclid enters only through the Common Notions used in
equational steps.

**Counts:** PROVED 13 (T1–T13; T5 by citation; T9/T10/T13 conditional as stated) ·
CHECKED 6 (K1–K6) · ASSERTED 7 (A1–A7) · INCOMPLETE 4 (I1–I4) · ST imports listed, uncounted.
