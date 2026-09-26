# Book 6 — Local Symmetry and Carrier Mathematics: extension proofs

**R Theory rewrite book:** `~/workspace/r-theory-rewrite/book6/index.html` (Book 6 of Volume I + Volume I closure; 17 sections §§6.0–6.16, Part V closure).
**Worker:** Euclid book-proofs campaign, workflow run `workflow-run-b4b24c5c566d490d92bad5fa51c906c1`.
**Date:** 2026-09-22 (PDT).
**Scope discipline (Kit's, non-negotiable):** PROVED = exact mathematics shown here. CHECKED = a completed numerical run, cited with its result. ASSERTED = manuscript claim, declared framing, or adopted assumption — never presented as established. INCOMPLETE = failed, timed out, unfinished, or deliberately not done.

## 0. Method and the No-Euclid-wholesale boundary

This book is proved in Euclid's *manner* — definitions first, strict dependency order,
nothing used before it is proved — but **not** from Euclid's *Elements* content.
Theorem 4.X.P10 (the no-Euclid-wholesale theorem, Book 4 §§4.X.H) is the governing
boundary: R Theory does not accept Euclidean metric geometry wholesale before the Flower
construction. The Euclid Book 6 ledger (`~/workspace/euclid_work/ledger/book6_ledger.md`)
establishes, proposition by proposition (6.1–6.33), that **Euclid's Book 6 (similar figures)
is not inherited, not re-derived, and not used**: zero occurrences of "similar"/"similarity"
in rewrite Books 0–6; ratio-of-area content is carried by modern admitted machinery
(Gram forms, exterior algebra, the determinant law), never deduced from Euclid's 6.1–6.33.
That negative result is INCOMPLETE-as-extension (deliberate, not failed) and is recorded
honestly in §8 below.

Consequence for citations: no Elements proposition is used deductively anywhere in this
file. The established material cited without reproof is:

- **(S1) The declared modern substrate (ST):** real Euclidean vector spaces, orthogonal
  and unitary groups, Lie algebras, exterior algebra, complexification, Hermitian forms,
  representation theory of compact Lie groups (Schur's lemma, commutant structure,
  irreps of SO(3)/O(2)). These are standard imported theorems, not Euclid deductions.
- **(S2) The campaign seed:** Kit's double-angle secant/cosecant identity, PROVED, at
  `~/workspace/euclid_work/books/seed_double_angle.md`. Established; **not directly
  needed** by any proof below (the trig steps here use cos²+sin²=1 directly). Dependency
  honesty requires saying so rather than manufacturing a citation.
- **(S3) The M5 structure from rewrite Book 5:** the split U = E⊕V (dim_ℝE=2, dim_ℝV=3),
  the doubled carrier W = U⊕U♯ (dim_ℝW=10) under primitive diagonal noncoupling, Axiom
  Zero (forbids primitive U↔U♯ mixing), and the Axiom-Zero pairing ι: U→U♯. These are
  *inherited premises*, proved/declared in Book 5's own campaign file, not re-proved here.
- **(S4) The book's own verification run:** `verify_book6.py` (V1–V32) was **re-run by
  this worker 2026-09-22**: `ALL 214 CHECKS PASSED (32 numbered V-checks: 66 CP, 148 NC)
  — 0 failed, 0 errors, 0 timeouts; worst CP max_err = 8.327e-16, worst NC max_err =
  9.070e-11`. Run log: `/tmp/b6_run.log` (ephemeral; the script is deterministic and
  re-runnable). CHECKED claims below cite this run. Where an analytic proof exists, the
  proof is given and the numerical check is noted only as corroboration (proof over
  sampling: no numerical samples on top of a complete proof).

## 1. Claim inventory

| # | Section | Claim (one line) | Scope |
|---|---|---|---|
| C1 | 6.1 | Aut_blk(U,g;E,V) = O(2)×O(3); Lie algebra so(2)⊕so(3), dim 1+3=4 | PROVED |
| C2 | 6.2 | Λ²U = Λ²E ⊕ (E⊗V) ⊕ Λ²V, dims 1+6+3=10; outer sectors = block Lie algebra | PROVED |
| C3 | 6.2 | Adjoining one nonzero simple cross generator closes brackets to so(5): rank 4→10 | CHECKED |
| C4 | 6.3 | I_ι(u,v) = (−ι⁻¹v, ιu): I_ι²=−1; commutes with diagonal lifts; W complex rank 5 | PROVED |
| C5 | 6.3A | Π isometric datum; J_CHI²=−1; J_CHI conjugate to I_ι via Π | PROVED (Π is AX) |
| C6 | 6.3A | exp(χJ_CHI) = cosχ·1 + sinχ·J_CHI | PROVED (CHECKED vs independent Taylor series) |
| C7 | 6.3A | Orbit weights cos²χ/sin²χ: sum 1, diff cos2χ, 2√(w_Uw_U♯)=\|sin2χ\|; norm preserved | PROVED |
| C8 | 6.4 | Single real-type M3/SO(3) module has no scalar complex structure in its commutant; multiplicity two minimal | ST (imported) |
| C9 | 6.5 | Hermitian transport through ι compatible with I_ι; block maps act unitarily | PROVED |
| C10 | 6.6 | Maximal complex-linear block envelope U(2)×U(3); real form O(2)×O(3) | PROVED |
| C11 | 6.7 | Z(U(2)×U(3)) = U(1)_E × U(1)_V; diagonal vs relative phase | PROVED |
| C12 | 6.8 | Volume datum; reduction to S(U(2)×U(3)), su(2)⊕su(3)⊕u(1); traceless line 2a+3b=0 unique up to norm; (1/2,−1/3) | PROVED (volume form is AX) |
| C13 | 6.9 | Hodge-return criterion; C(n,4)=n ⟺ n=5 (n≥4); grade pattern 0:1,2:10,4:5; Λ⁴U dual to U | PROVED (criterion is AX) |
| C14 | 6.10 | Complexification: 2m=10−k; faithful ⟺ k=0; unique faithful equivariant completion ℂ⁵ | PROVED (mod ST) |
| C15 | 6.10 | k=4 real-rank-5 embedding into ℂ³ | CHECKED |
| C16 | 6.11 | ω|_U=0 ⟺ U⊥IU ⟺ IU=U^⊥; graph(A): Lagrangian ⟺ A symmetric; totally real ⟺ I+A² invertible | PROVED |
| C17 | 6.11 | Nonsymmetric nilpotent witness: totally real, not Lagrangian | PROVED |
| C18 | 6.12 | dim_ℂW ≥ 5 with equality at ℂ³_geom⊕ℂ²_orient (common-completion premise) | PROVED (mod ST; premise is AX) |
| C19 | 6.13 | 2n=n(n−1)/2 ⟺ n=5 (n>0); C(n,r)=2n ⟺ (n,r)=(5,2),(5,3) | PROVED |
| C20 | 6.13 | Exterior dims 1,5,10,10,5,1; even/odd sectors 16 each | PROVED |
| C21 | 6.14 | Möbius identities; p′du′=pdu, dp′∧du′=dp∧du; reciprocal-coordinate momentum law | PROVED |
| C22 | 6.14 | J_G²=−1 cotangent completion compatible with canonical symplectic form | PROVED |
| C23 | 6.15 | Simplex: \|v_A\|²=(N−1)/N, dots −1/N, edge²=2 | PROVED |
| C24 | 6.15 | Gram spectrum {(d+1)/2, ½×(d−1)}, det=(d+1)/2^d | PROVED |
| C25 | 6.15 | det(T\|_{V(N−1)}) = sgn(T); odd permutations exchange orientation classes | PROVED |
| — | 6.0/6.16/closure | Status grammar, terminal firewall, Volume-I inheritance boundary | ASSERTED (declared) |

## 2. Definitions (nothing used before it is defined)

- **D1.** E, V: real Euclidean vector spaces, dim_ℝE=2 (oriented), dim_ℝV=3.
- **D2.** U = E ⊕ V, orthogonal direct sum; dim_ℝU = 5.
- **D3.** W = U ⊕ U♯ with U♯ a second copy; U ∩ U♯ = {0}; dim_ℝW = 10.
- **D4.** ι: U → U♯ the Axiom-Zero pairing (linear isometry; inherited premise from Book 5).
- **D5.** O(n): real orthogonal group; so(n): skew-adjoint matrices; dim so(n) = n(n−1)/2
  (free entries above the diagonal).
- **D6.** Aut_blk(U,g;E,V) = {T ∈ O(U) : T(E)=E, T(V)=V}.
- **D7.** Λ²U: second exterior power; for U = E⊕V, Λ²U = Λ²E ⊕ (E⊗V) ⊕ Λ²V
  (basis: e_i∧e_j, e_i∧f_k, f_k∧f_l).
- **D8.** I_ι(u,v) = (−ι⁻¹v, ιu) on W = U⊕U♯.
- **D9.** Π: U → U♯ an isometric identification — **AX-6.1**, additional datum, not axiom.
- **D10.** J_CHI(u,v) = (−Π⁻¹v, Πu).
- **D11.** h: Hermitian form on (W, I_ι) obtained by transporting ⟨·,·⟩_U through ι;
  ω = Im h the associated real symplectic form.
- **D12.** U(n): complex-linear isometries of ℂⁿ; S(U(2)×U(3)) = {(A,B) : detA·detB = 1}.
- **D13.** Fixed complex volume form — **AX-6.2**, additional datum.
- **D14.** Hodge-return criterion — **AX-6.3**, declared selector premise: the first new
  grade generated by composing orientation bivectors returns to coframe/vector type.
- **D15.** Common-complex-carrier premise — **AX-6.4**: a common complex space must carry
  faithful commuting complex-linear actions of internal O(2) and geometric SO(3) with no
  preferred plane identification.
- **D16.** Metric/duality choice identifying U♯ with U* — **AX-6.5**, additional datum.

## 3. Proofs in dependency order

**P1 (6.1, uses D1,D2,D5,D6) — PROVED.** T ∈ Aut_blk preserves the orthogonal split,
so T = T_E ⊕ T_V with T_E ∈ O(E) ≅ O(2), T_V ∈ O(V) ≅ O(3); every such pair gives a
block map. Hence Aut_blk = O(2)×O(3). Identity component: SO(2)×SO(3); Lie algebra
so(2)⊕so(3) with dim 1+3 = 4 by D5 (so(2): one free entry; so(3): three). ∎
*A1 (ASSERTED):* "No larger mixing group is primitive at this stage" is a boundary
declaration resting on the inherited M3/M4 seam — not a computation. The absence of
primitive E↔V maps is inherited from the independent M3/M4 seam; Axiom Zero separately
forbids primitive U↔U♯ mixing. These are two distinct non-mixings and must not be
conflated (declared, MA).

**P2 (6.2, uses D7, P1) — PROVED.** dim Λ²E = C(2,2) = 1, dim(E⊗V) = 2·3 = 6,
dim Λ²V = C(3,2) = 3; sum 10 = C(5,2) = dim so(5). The identification
v∧w ↦ (x ↦ ⟨v,x⟩w − ⟨w,x⟩v) sends Λ²E onto so(2) and Λ²V onto so(3) — exact, so the
outer sectors reproduce the inherited block Lie algebra of P1. ∎

**P3 (6.2 extension, uses P2) — CHECKED.** Adjoining one nonzero simple cross generator
e∧f ∈ E⊗V to the four block generators and closing under iterated Lie brackets reaches
rank 10 (so(5)): completed iterated-commutator rank computation in the V-run
(verify_book6.py, scope NC — this run: all pass). This is an *extension* theorem: the
cross-block datum is available, not primitive. ∎
*A2 (ASSERTED):* Book 6 does not promote the cross-block datum to a primitive axiom
(explicit non-promotion declaration, MA).

**P4 (6.3, uses D3,D4,D8) — PROVED.** I_ι²(u,v) = I_ι(−ι⁻¹v, ιu)
= (−ι⁻¹(ιu), ι(−ι⁻¹v)) = (−u,−v), so I_ι² = −1. For the diagonal lift
L_A = A ⊕ ιAι⁻¹: I_ιL_A(u,v) = I_ι(Au, ιAι⁻¹v) = (−Aι⁻¹v, ιAu) = L_A(−ι⁻¹v, ιu)
= L_AI_ι(u,v); hence every primitive paired lift commutes with I_ι. W with complex
structure I_ι has complex dimension 10/2 = 5. ∎
*A3 (ASSERTED):* I_ι is not the internal M3 operator J; conflating them would erase the
independence Axiom Zero introduced, and the ι-dependent construction is not canonical
from an unpaired abstract isomorphism class alone (firewall framing, MA).

**P5 (6.3A, uses D9,D10, P4) — PROVED.** J_CHI²(u,v) = J_CHI(−Π⁻¹v, Πu)
= (−Π⁻¹Πu, Π(−Π⁻¹v)) = (−u,−v); J_CHI² = −1 by the same computation as P4. With
Φ(u,v) = (u, Πι⁻¹v), invertible with Φ⁻¹(u,w) = (u, ιΠ⁻¹w):
ΦI_ιΦ⁻¹(u,w) = ΦI_ι(u, ιΠ⁻¹w) = Φ(−Π⁻¹w, ιu) = (−Π⁻¹w, Πu) = J_CHI(u,w).
So J_CHI is conjugate to I_ι relative to Π — no second primitive complex structure, no
new ambient dimension. ∎ (Π itself is AX-6.1, declared datum.)

**P6 (6.3A exponential, uses P5) — PROVED.** For any real operator with J² = −1,
exp(χJ) = Σ χⁿJⁿ/n! splits into even/odd series = cosχ·1 + sinχ·J (standard power
series; termwise grouping is exact). Hence exp(χ_CHI J_CHI) = cosχ_CHI·1 + sinχ_CHI·J_CHI.
*CHECKED corroboration:* independent Taylor-series matrix exponential agrees (this run,
worst disagreement 2.3e-16, NC) — corroboration only; the series argument is the proof. ∎

**P7 (6.3A weights, uses P5,P6, D9) — PROVED.** The orbit of (u,0):
exp(χJ_CHI)(u,0) = cosχ·(u,0) + sinχ·J_CHI(u,0) = cosχ u ⊕ sinχ Πu.
‖cosχ u ⊕ sinχ Πu‖² = cos²χ‖u‖² + sin²χ‖Πu‖² = ‖u‖², since Π is isometric (D9) and
U ⊥ U♯. Weights w_U = cos²χ, w_U♯ = sin²χ: w_U + w_U♯ = cos²χ+sin²χ = 1;
w_U − w_U♯ = cos²χ − sin²χ = cos2χ; 2√(w_Uw_U♯) = 2|sinχcosχ| = |sin2χ|.
χ = 0, π/4, π/2 give one-copy occupancy, equal weight, complete transfer, directly.
The orbit leaves U∩U♯ = {0}, W = U⊕U♯, dim_ℝW = 10 untouched. ∎
*A4 (ASSERTED):* Firewalls — J_CHI is off-diagonal mathematics, not a primitive active
coupling (A0.2); Book 6 does not assert χ_CHI evolves, transfers physical energy or
matter, or is observable; no physical mirror-universe/parity/time/spacetime/phase
interpretation is derived (MA).

**P8 (6.4) — ST (imported) + ASSERTED framing.** Real representation theory: a single
M3 real-type module admits no independent scalar complex structure in its commutant;
multiplicity two is minimal; the same holds for the standard SO(3) module. Imported as
standard theorems (ST), not re-derived.
*A5 (ASSERTED):* the reading "the Axiom-Zero doubling therefore supplies exactly the
multiplicity needed for a global central complex structure on W" is application framing
(MA).

**P9 (6.5, uses D4,D8,D11, P4) — PROVED.** Transport the Euclidean metric of U to U♯
through ι: h((u₁,w₁),(u₂,w₂)) = ⟨u₁,u₂⟩_U + ⟨ι⁻¹w₁,ι⁻¹w₂⟩_U extended sesquilinearly over
I_ι. Direct check: h(I_ιξ, I_ιη) = h(ξ,η) (the two summands swap), so the direct-sum
metric is compatible with I_ι — a Hermitian form. Primitive orthogonal block maps
L_A = A⊕ιAι⁻¹ preserve h, hence act unitarily once the complex pairing is installed. ∎
*A6 (ASSERTED):* "canonical relative to the declared pairing" — canonicality is proved
*conditional* on the declared ι; the declaration itself is premise, not theorem (MA).

**P10 (6.6, uses D1,D2, P1, P9) — PROVED.** Complex-linear isometries preserving the
Hermitian metric and the 2+3 complex block decomposition: on each block they are
unitary; the two blocks have different complex dimensions, hence are inequivalent as
Hermitian spaces, so no block-mixing isometry is possible. Maximal envelope:
U(2)×U(3). The fixed locus of complex conjugation (real-form preservation) is
O(2)×O(3). ∎
*A7 (ASSERTED):* this enlargement is a mathematical automorphism envelope — not yet a
physical gauge postulate (MA).

**P11 (6.7, uses P10) — PROVED.** Z(U(n)) = {e^{iθ}I_n}: an element commuting with all
unitaries is scalar by Schur's lemma (standard, ST), and a scalar unitary is a phase.
Hence Z(U(2)×U(3)) = Z(U(2))×Z(U(3)) = U(1)_E × U(1)_V. The diagonal U(1) is the common
scalar phase generated by I; the relative phase exists because the 2+3 decomposition
is preserved. ∎
*A8 (ASSERTED):* neither U(1) is identified with electromagnetism or hypercharge (MA).

**P12 (6.8, uses D12,D13, P10) — PROVED.** Requiring preservation of the fixed complex
volume form (AX-6.2) imposes detA·detB = 1, reducing the envelope to S(U(2)×U(3)).
Its Lie algebra: {(X,Y) skew-Hermitian : trX + trY = 0} = su(2)⊕su(3)⊕u(1) — the u(1)
summand is (iaI₂, ibI₃) with 2a+3b = 0. The map (a,b) ↦ 2a+3b = tr diag(aI₂,bI₃) has
one-dimensional kernel: the traceless block-scalar direction is unique up to
normalization; 2(1/2)+3(−1/3) = 1−1 = 0, so (1/2,−1/3) is the convenient normalization. ∎
*A9 (ASSERTED):* conditional carrier theorem only; the su(2)/su(3)/u(1) notation is not
permission to identify these factors with weak isospin, color, hypercharge, or any
physical force (MA).

**P13 (6.9, uses D14) — PROVED (criterion AX-6.3).** The criterion forces
Λ^{(n−4)}U* = Λ¹U*, i.e. C(n,4) = n. For n ≥ 4:
C(n,4) = n(n−1)(n−2)(n−3)/24 = n ⟺ (n−1)(n−2)(n−3) = 24.
f(n) = (n−1)(n−2)(n−3) is strictly increasing for n ≥ 1; f(5) = 4·3·2 = 24, f(4) = 6 < 24;
hence n = 5 is the unique integer solution for n ≥ 4. At n = 5: C(5,2) = 10 bivectors;
exterior grades C(5,k) = 1,5,10,10,5,1 — even grades sum 1+10+5 = 16, odd grades
5+10+1 = 16; the grade pattern 0:1, 2:10, 4:5 closes the scalar-plus-bivector sector;
Λ⁴U is Hodge-dual to U via interior product with the orientation (exact construction).
∎
*A10 (ASSERTED):* this is an independent rank-five structural certificate — not a
derivation of Axiom Zero (MA).

**P14 (6.10 complexification, uses D15-premise for the strong form) — PROVED.**
Let S = f(U) ⊂ ℂ⁵, f real-injective, m = dim_ℂ span_ℂS, k = dim_ℝ(S ∩ iS).
S+iS is the real span of a complex m-space ⇒ dim_ℝ(S+iS) = 2m; by the sum formula,
2m = dim S + dim iS − dim(S∩iS) = 10 − k. S∩iS is a complex subspace, so k is even;
k ≤ 2m and 2m ≤ 10 give m ≤ 5 and 2m = 10−k ≥ 10−2m ⇒ m ≥ 3; m ∈ {3,4,5}.
dim_ℂ ker f_ℂ = 5−m and k = 2·dim_ℂ ker f_ℂ, consistent with 2m = 10−k. Faithful
complexification (f_ℂ injective) ⟺ m = 5 ⟺ k = 0. Stronger conditional theorem: with the
2+3 block structure, the complexified blocks are inequivalent irreducibles (ST,
imported), so any symmetry-equivariant faithful complex completion must keep them
apart — the unique such completion is ℂ²⊕ℂ³ ≅ ℂ⁵. ∎
*A11 (ASSERTED):* the M2 rank firewall does not forbid lower-dimensional complex
completions; the stronger theorem does not prove M0–M4 require complex completion in
the first place (nonselection, MA).

**P15 (6.10 k=4 example) — CHECKED.** Explicit real-rank-five embedding into ℂ³ with
k = 4, verified by SVD intersection-rank computation (this run, NC). The ℂ⁴ case
(k = 2) is asserted in the manuscript, not recomputed.
*A12 (ASSERTED):* the k=2 ℂ⁴ example (MA — explicitly flagged as asserted).

**P16 (6.11 Lagrangian/totally-real, uses D11) — PROVED.** For half-dimensional real U
in Hermitian (W,h,I), ω = Im h: ω(u,v) = ⟨Iu,v⟩_ℝ. ω|_U = 0 ⟺ ⟨Iu,v⟩ = 0 ∀u,v ∈ U ⟺
U ⊥ IU. dim IU = dim U = n = (dim W)/2, so U ⊥ IU ⟺ IU = U^⊥ (dimension count).
If x ∈ U∩IU, x = Iv, then ⟨x,x⟩ = ⟨u,Iv⟩ = 0 ⇒ x = 0; then W = U⊕IU by dimension.
For U_A = graph(A) in standard ℂ⁵ = ℝ⁵⊕iℝ⁵ with ω((x₁,y₁),(x₂,y₂)) = x₁·y₂ − x₂·y₁:
ω((x,Ax),(z,Az)) = x·Az − z·Ax = xᵀ(A−Aᵀ)z — exact. Lagrangian ⟺ this vanishes
∀x,z ⟺ A = Aᵀ (symmetric). Totally real: (x,Ax) = i(z,Az) ⟺ x = −Az, Ax = z ⟺
(I+A²)z = 0; nontrivial intersection ⟺ I+A² singular; hence totally real ⟺ I+A²
invertible. ∎

**P17 (6.11 witness) — PROVED.** Let A be nonsymmetric with A² = 0 (exists in M₅(ℝ),
exact matrix algebra). Then I+A² = I is invertible ⇒ graph(A) is totally real, while
A ≠ Aᵀ ⇒ it is not Lagrangian — exact, no sampling. (The book's script corroborates
numerically, NC; the algebra above is the proof.)
*A13 (ASSERTED):* positive-overlap Hermitian examples with k = 2, 4 exist — asserted,
not recomputed (MA). Consequence: Hermitian compatibility alone does not select k = 0;
Lagrangianity would be a sufficient additional axiom, not a discharge of Axiom Zero
(declared, MA).

**P18 (6.12 minimal carrier, uses D15/AX-6.4) — PROVED (mod ST).** O(2) is nonabelian
(rotation by π/2 and reflection across the x-axis do not commute — exact matrix check);
GL(1,ℂ) ≅ ℂ* is abelian ⇒ no faithful complex representation of O(2) in dimension 1.
Faithful 2-dimensional complex realization exists (rotations as SO(2) matrices,
reflection as diag(1,−1) — relations checked exactly). Smallest faithful complex SO(3)
representation is 3-dimensional (ST: SO(3) irreps have odd dimension; the 1-dim is
trivial, not faithful). In complex dimension 4, a faithful SO(3) representation is
3⊕1 (odd dims, ST); its commutant is ℂ⊕ℂ, abelian (Schur, ST) — it cannot contain a
commuting faithful (nonabelian) O(2) image; impossible. In dimension 5, 3⊕2 has
commutant containing M₂(ℂ) (ST), and the required O(2) block exists by the 2-dim
construction. Hence, inside the stated class (AX-6.4), dim_ℂW ≥ 5 with equality at
W ≅ ℂ³_geom ⊕ ℂ²_orient (real dimension 10). ∎
*A14 (ASSERTED):* exact minimality inside the stated class; not a pre-Axiom selector
(MA).

**P19 (6.13 balance) — PROVED.** dim_ℝ(U⊗_ℝℂ) = 2n, dim_ℝΛ²U = n(n−1)/2. Equality:
4n = n²−n ⟺ n(n−5) = 0 ⟺ n = 5 (n > 0) — exact. For 2 ≤ r ≤ n−2, C(n,r) = 2n:
by symmetry assume r ≤ n/2. r = 2: n(n−1)/2 = 2n ⟺ n = 5. r = 3:
n(n−1)(n−2)/6 = 2n ⟺ n²−3n−10 = 0 ⟺ n = 5 or n = −2; n > 0 gives n = 5. r ≥ 4:
then n ≥ 2r ≥ 8 and C(n,r) ≥ C(n,4) (C(n,r) increases in r for r < n/2); C(n,4) > 2n
⟺ (n−1)(n−2)(n−3) > 48, true at n = 8 (7·6·5 = 210) and increasing — no solutions.
By r ↔ n−r symmetry: (n,r) ∈ {(5,2),(5,3)} exactly, the Hodge-dual middle pair. ∎
(The book's exact integer scan corroborates; the argument above is the proof.)

**P20 (6.13 exterior pattern) — PROVED.** At n = 5: C(5,k) = 1,5,10,10,5,1; even
1+10+5 = 16, odd 5+10+1 = 16 — exact binomial arithmetic.
*A15 (ASSERTED):* nonselection — equal dimensions do not imply a natural or equivariant
identification (U_ℂ and Λ²U have different SO(5) characters, ST); no inherited principle
requires these ranks to match; the balance is an exact fingerprint of the already-earned
rank five, not a selector for it (MA).

**P21 (6.14 Möbius/cotangent) — PROVED.** For u′ = (au+b)/(cu+d), ad−bc = 1:
du′/du = ((cu+d)a − (au+b)c)/(cu+d)² = (ad−bc)/(cu+d)² = (cu+d)^{−2} (quotient rule,
exact). Preserving p du: p′ = p(cu+d)² gives p′du′ = p du, hence dp′∧du′ = d(pdu) = dp∧du
(exactness ⇒ closed). Reciprocal coordinate s = √(1+u²)−u: 1/s = √(1+u²)+u
(rationalizing: s(√(1+u²)+u) = 1), so u = (1/s−s)/2 = (1−s²)/(2s) — exact inverse;
p_s = p_u·du/ds with du/ds = −(1+s²)/(2s²) (exact differentiation), i.e.
p_s = −(1+s²)p_u/(2s²). The book's finite-difference spot checks (NC) corroborate;
the computations above are the proofs. ∎

**P22 (6.14 cotangent lift) — PROVED.** J_G(q,p) = (−G⁻¹p, Gq):
J_G²(q,p) = J_G(−G⁻¹p, Gq) = (−G⁻¹Gq, −GG⁻¹p) = (−q,−p); J_G² = −1 — exact. Compatibility
with the canonical symplectic form ω((q₁,p₁),(q₂,p₂)) = ⟨q₁,p₂⟩−⟨q₂,p₁⟩ is a direct
exact check (standard). At n = 5 this is a ten-real-dimensional cotangent completion. ∎
*A16 (ASSERTED):* the no-go is load-bearing — the functorial cotangent lift exists for
every smooth carrier and does not make cotangent covectors primitive state variables;
identifying U♯ with U* needs the explicit metric/duality choice (AX-6.5); nothing here
is physical momentum before a later action or dynamics is supplied; this route
corroborates the M5 doubling but does not derive it (MA).

**P23 (6.15 simplex vertices, N ≥ 2) — PROVED.** v_A = e_A − (1/N)·1 (centered):
|v_A|² = 1 − 2/N + N·(1/N²) = 1 − 1/N = (N−1)/N — exact. For A ≠ B:
v_A·v_B = −1/N − 1/N + N·(1/N²) = −1/N — exact. |v_A−v_B|² = 2(N−1)/N + 2/N = 2 —
exact (regular simplex, squared side 2). ∎
(The book's N = 2…8 sampling, NC, is corroboration; the algebra is the proof.)

**P24 (6.15 Gram spectrum) — PROVED.** Normalized edge Gram G_d = ½(I_d + J_d), J_d the
all-ones matrix: J_d has eigenvalues d (once) and 0 (d−1 times) — exact; hence G_d has
eigenvalues (d+1)/2 (once) and 1/2 (d−1 times), and
det G_d = ((d+1)/2)·(1/2)^{d−1} = (d+1)/2^d — exact. ∎

**P25 (6.15 orientation classes) — PROVED.** Permutations act orthogonally on ℝ^N,
fixing span(1); for T ∈ S_N, det(T|_{V(N−1)}) = det(T)/det(T|_{span 1}) = sgn(T)/1.
Hence A_N preserves orientation while every odd permutation exchanges the two
orientation classes: symmetric simplex data contain both orientations but canonically
select neither. ∎
*A17 (ASSERTED):* the simplex theorem is universal in N; d = 3 and d = 10 are examples
only — it does not select ten, and cannot select N = 11 or d = 10 (nonselection, MA).

**P26 (§6.0 status grammar, §6.16 firewall, Volume I closure) — ASSERTED (declared).**
M0–M4 frozen; the A/B/C/D classification grammar (direct M5 consequences / maximal
mathematical automorphism envelopes / conditional extensions with declared data /
obstruction–nonselection theorems) is a declared grammar, not a derived one. "Local"
means pointwise or frame symmetry only — not gauge symmetry localized over spacetime.
The terminal firewall (§6.16): no passage from a pointwise carrier automorphism group
to a spacetime-dependent gauge group without additional structure (base/bundle, local
sections, connection, curvature, dynamics/action) — a declared boundary, not a derived
theorem. Volume II may inherit only the mathematical structures and explicit assumptions
certified in Books 0–6. The master-retirement note (obsolete "HANDOFF TO BOOK 5" line
dropped) is provenance/editorial; the earlier split copy was not inspected in this audit.

## 4. New axioms / assumptions beyond Euclid + seed + earlier books

New in Book 6 (all are *declared mathematical data*, explicitly never promoted to
primitive axioms — Book 6's Part IV "Zero counts" records 0 new primitive axioms):

- **AX-6.1** §6.3A: isometric identification Π: U → U♯ (conditional CHI orbit datum).
- **AX-6.2** §6.8: fixed complex volume form (S(U(2)×U(3)) reduction datum).
- **AX-6.3** §6.9: Hodge-return selector criterion (rank-five certificate premise).
- **AX-6.4** §§6.10/6.12: common-complex-carrier premise (faithful commuting O(2)/SO(3)
  actions, no preferred plane identification).
- **AX-6.5** §6.14: metric/duality choice identifying U♯ with U* (cotangent datum).

Inherited (not new): Axiom Zero and the pairing ι (Book 5 / M5); the M3/M4 carriers E, V;
the modern substrate (S1); standard imported theorems (ST); the campaign seed (S2).

## 5. Boundary ledger — what is NOT extended

- **Euclid's Book 6 (similar figures, 6.1–6.33): INCOMPLETE — deliberately not extended.**
  Per theorem 4.X.P10 (no-Euclid-wholesale) and the book6 Euclid ledger rows 6.1–6.33:
  no similarity definition is adopted, no similarity criterion is re-derived, and the
  application of areas (6.27–6.29) and golden section (6.30) have no R Theory counterpart.
  This is a boundary, not a failure.
- **χ_CHI dynamics/observability: INCOMPLETE** — firewalled; the orbit is conditional
  carrier geometry, not a physical process (§6.3A, A4).
- **Physical selectors: INCOMPLETE** — no physical gauge group, spacetime localization,
  action/dynamics, particle ontology, chirality, hypercharge, couplings, masses, mixings,
  anomalies, generations, or force identification is derived (§6.16, A-list above).
