# Book 3 Extension Proofs — Euclid-style

**Rewrite book:** Book 3 — Projective Phase, Orientation, and Lift Structure
(`~/workspace/r-theory-rewrite/book3/index.html`).
**Campaign:** Euclid book-proofs (euclid-book-proofs workflow run).
**Date:** 2026-09-22 (PDT). **Worker:** book-3 agent (depth 1/2).
**Status vocabulary:** PROVED = exact mathematics shown here, in dependency order;
CHECKED = a completed computation (run named and dated) measures it;
ASSERTED = declared axiom/definition/standard import/manuscript or bookkeeping
stipulation, granted not proved here; INCOMPLETE = failed, timed out, or
unfinished. Nothing is rounded up or down.

**Method note.** Euclid-style means: definitions first, strict dependency order,
nothing used before it is proved. The analytic substrate (real analysis, trig
identities, linear algebra) is a declared import, not earned from the Elements —
the No-Euclid-wholesale boundary (4.X.H) is honored throughout: Euclid's Book 3
(the synthetic theory of circles) is **not** re-derived, and rewrite Book 3's
circle is the analytic phase circle, a different object. No Euclid proposition
is cited as a premise below; where standard mathematics is imported it is
labeled as such. Established material cited without reproving: the campaign
seed (Kit's double-angle secant/cosecant identity, PROVED,
`~/workspace/euclid_work/books/seed_double_angle.md`).

---

## 0. Declarations (definitions first)

**D1 — phase circle.** 𝕋₂π = ℝ/2πℤ with translations τ_a(x) = x + a (mod 2π).
Declared; the additive group structure of ℝ/2πℤ is standard.

**D2 — cophase.** The relation "x is cophase to y" means y ≡ x ± π/2 (mod 2π),
the *directed* quarter-turn being τ_{π/2}. Declaration: this is not equal
phase, half-turn, antipode, reciprocal, or spin-cover partner.

**D3 — canonical primitives (analytic formulas).** For x with sin x ≠ 0 and
cos x ≠ 0:
  sxp(x) = |csc x| − cot x,   srx(x) = |csc x| + cot x,
  cxp(x) = |sec x| − tan x,   crx(x) = |sec x| + tan x.
These are the four curves plotted in the book (cf. the Desmos expressions).
All four are strictly positive (see C16).

**D4 — FlatWave.** FlatWave(x) = sgn(sin 2x), on the domain D that excludes
the seams x = kπ/2 (where sin 2x = 0 and the sign is undefined).

**D5 — the fold.** κ: 𝕋₂π → 𝕋_π = ℝ/πℤ, κ(x) = x mod π. Declared.

**D6 — projective phase coordinate.** t = tan(x/2), mapping 𝕋₂π → ℝ̂ =
ℝ ∪ {∞}. Infinity is a chart value of the projective line, not a singularity.

**D7 — positive reciprocal transform.** f(u) = √(1+u²) − u for real u.

**D8 — octants.** O_j = (jπ/4, (j+1)π/4), j = 0,…,7. η = τ_{π/4}.

**D9 — lift selector and deck involution (3.XI).** A lift selector is any map
s: SO(3) → S³ with Φ(s(R)) = R; the deck involution is δ(q) = −q. Definitions.

**Declared standard imports (used as premises, never re-proved here):**
- **I1.** Real analysis: sin, cos, tan, the addition formulas, limits,
  sgn, the absolute value. (The Euclid-free analytic substrate.)
- **I2.** Finite-dimensional linear algebra: determinants, multiplicativity,
  sign homomorphism.
- **I3.** The affine atlas of RP² (homogeneous triples modulo scaling; charts
  U_X, U_Y, U_Z) and the tautological line bundle γ with its transition data.
- **I4.** Čech cohomology: the sign-cocycle ⇒ w₁(γ) identification.
- **I5.** The stable tangent relation T RP^n ⊕ 1 ≅ (n+1)γ_n and the Whitney
  product law; the cohomology ring H*(RP^n;ℤ₂) ≅ ℤ₂[a_n]/(a_n^{n+1}); the spin
  criterion w₁ = w₂ = 0; stability of w₂ under ⊕1.
- **I6.** The quaternion model Spin(3) ≅ S³ and the covering map
  Φ(q)(v) = qv q̄; covering-space theory (S³ connected; continuous sections of
  a nontrivial double cover do not exist).
- **I7.** π-periodicity of the canonical primitives (inherited from Book 2;
  the book page itself tags this inheritance MA — manuscript assertion).
- **I8.** The quaternion multiplication convention ij = k.

Dependency graph of the claims below: A(C1–C7) → B(C8–C11) → C(C12–C15) →
D(C16–C20) → E(C21–C26); F(C27–C30) uses I3; G(C31–C35) uses I3, I4;
H(C36–C39) uses I5; I(C40–C43) uses I5; J(C44–C48) uses I6, D3, C18;
K(C49–C53) uses J; L(C54–C58) is bookkeeping over all of the above.
No claim uses a later claim.

---

## A. Cophase and the quarter-turn (book 3.I)

**C1 — exact order 4 of the directed quarter-turn.** *Statement:*
τ_{π/2}⁴ = id, τ_{π/2}² = τ_π ≠ id, τ_{π/2} ≠ id. *Proof:* translations compose
by addition: τ_a ∘ τ_b = τ_{a+b}. Hence τ_{π/2}² = τ_π, τ_{π/2}⁴ = τ_{2π} =
id on 𝕋₂π, and τ_π ≠ id (it moves 0 to π ≠ 0 mod 2π). ∎ **PROVED.**

**C2 — the cophase relation is not an equivalence relation.** *Statement:*
the relation "y ≡ x ± π/2 (mod 2π)" is symmetric and irreflexive but not
transitive. *Proof:* symmetric by ±; irreflexive since x ≡ x ± π/2 would give
π/2 ≡ 0 (mod 2π), false. Not transitive: 0 is cophase to π/2 and π/2 is
cophase to π, but 0 is not cophase to π (0 ≡ π only mod 2π via the half-turn,
which is excluded). ∎ **PROVED.**

**C3 — cophase exchanges sine and cosine channels up to sign.** *Statement:*
sin(x + π/2) = cos x; cos(x + π/2) = −sin x; same with x − π/2 up to sign.
*Proof:* the standard addition formulas (I1):
sin(x+π/2) = sin x cos(π/2) + cos x sin(π/2) = cos x;
cos(x+π/2) = cos x cos(π/2) − sin x sin(π/2) = −sin x. ∎
**PROVED** (from declared standard-analysis premises I1).

**C4 — the fold makes one involution of order 2.** *Statement:* after κ, the
two directed cophase steps induce a single involution of order 2 on 𝕋_π.
*Proof:* on 𝕋_π, x + π/2 ≡ x − π/2 (mod π), so the two directions coincide;
applying twice gives x + π ≡ x (mod π), and once gives x + π/2 ≢ x (mod π).
Hence order exactly 2. Carrier-dependent order (4 on 𝕋₂π, 2 on 𝕋_π), not a
contradiction. ∎ **PROVED.**

**C5 — oriented frames split into two determinant-sign classes.** *Statement:*
for ordered bases of ℝ², the sign of det is well-defined and independent of
the reference basis. *Proof:* det(AB) = det A · det B (I2), so sign(det) is a
homomorphism GL(2,ℝ) → {±1}; changing reference basis multiplies all frame
determinants by the same fixed nonzero factor, preserving the sign classes.
∎ **PROVED** (from I2).

**C6 — cophase translations preserve the phase circle's orientation.**
*Statement:* each τ_a is orientation-preserving as a map of the circle.
*Proof:* on the universal cover ℝ, τ_a(x) = x + a has derivative +1 (I1); the
induced map on the quotient 𝕋₂π inherits positive orientation. ∎
**PROVED.**

**C7 — Cophase–Mirror Separation.** *Statement:* under the declared
vocabulary, the cophase structure and the mirror-frame structure are
mathematically independent: no map between phase points and
orientation-bearing frames has been declared. *Proof:* true by inspection of
the declaration list — "mirror frame" (D-side vocabulary: the negative
determinant-sign class relative to a declared orientation) lives in the
frame world; cophase (D2) lives in the phase world; the book declares no
bridge between them. This is a bookkeeping fact about what was declared,
not a theorem about what must be. **ASSERTED** (scope declaration; the page
tags the surrounding material CP/AX — the independence claim itself is the
declaration being recorded). The prohibited-substitutions list (x ↦ x±π/2,
x ↦ −x, s ↦ 1/s, q ↦ −q may not be called "mirror") is likewise a
terminological stipulation — **ASSERTED**.

---

## B. Eight octants and the dominance cycle (book 3.II)

**C8 — η has exact order 8.** *Statement:* η = τ_{π/4} satisfies η⁸ = id with
no smaller positive power the identity, and acts faithfully on the eight
octants. *Proof:* 8·(π/4) = 2π ≡ 0 mod 2π, and k·(π/4) ≡ 0 mod 2π requires
8 | k; hence order exactly 8. η permutes the O_j cyclically, so the action is
faithful. ∎ **PROVED.** (Corroborated exactly: verify_book3.py B46a, "exact",
run 2026-09-22.)

**C9 — the dominance cycle.** *Statement:* on each octant interior exactly one
canonical primitive is strictly largest, cycling
srx → cxp → crx → sxp → srx → cxp → crx → sxp; the winner at each octant
midpoint has a strict positive gap to the runner-up. *Proof:* the
octant-by-octant argument is the book's (3.II.T9); measured here by the
completed run: verify_book3.py B10, "winner cycle srx>cxp>crx>sxp (x2), min
strict gap = 3.531e+00" — status OK [NC], run 2026-09-22. "Dominance" is a
numerical-order statement, not dynamics (3.II.N1) — declared on the page.
**CHECKED** (completed numerical run; the analytic octant-by-octant proof
was read on the page but not independently re-derived in this task).

**C10 — the cophase permutation is exact.** *Statement:* the cophase action on
the four primitive labels is P_c = (srx crx)(sxp cxp); the winner-label
cycle C_dom has order 4 with C_dom² = P_c. *Proof:* permutation group
arithmetic on four labels, verified exactly: verify_book3.py B46b
(C_dom² = P_c, "exact") and B46c (C_dom order 4, "exact"), run 2026-09-22.
∎ **CHECKED** (completed exact-permutation run).

**C11 — π-periodicity inheritance.** The identification of O_j with O_{j+4}
at the primitive-value level (four primitive classes from eight positional
octants) rests on the primitives' π-periodicity, which the book page certifies
as Book 2 inheritance — and itself tags **MA** (manuscript assertion). No
Book 2 proof file exists in this campaign batch to cite. **ASSERTED**
(inheritance claim recorded at the page's own status).

---

## C. The projective phase line (book 3.III)

**C12 — t = tan(x/2) is a bijection 𝕋₂π → ℝ̂.** *Proof:* on (−π, π) the map
x ↦ tan(x/2) is continuous and strictly increasing (I1) from −∞ to +∞; the
endpoint x = ±π (the same point of 𝕋₂π) is sent to the single projective
point ∞. Strict monotonicity gives injectivity on the circle; the limits give
surjectivity onto ℝ̂. ∎ **PROVED** (from I1). The signed coordinate retains
the half-turn information the positive primitives erase — immediate, since
tan(x/2 + π/2·…) distinguishes x from x+π.

**C13 — directed cophase is Möbius, of exact order 4.** *Statement:* with
Q₊(t) = (1+t)/(1−t), Q₋(t) = (t−1)/(1+t): directed cophase x ↦ x ± π/2
acts as t ↦ Q_±(t); Q₋ ∘ Q₊ = id; Q₊²(t) = −1/t; Q₊ has exact order 4 in
PGL(2,ℝ); the marked orbit 0 → 1 → ∞ → −1 → 0 is the four cardinal phases
0, π/2, π, 3π/2. *Proof:* by the tan addition formula (I1),
tan((x+π/2)/2) = tan(x/2 + π/4) = (tan(x/2)+1)/(1−tan(x/2)) = Q₊(t), and
similarly for −π/2. Direct algebra: Q₋(Q₊(t)) = t;
Q₊(Q₊(t)) = (1+(1+t)/(1−t))/(1−(1+t)/(1−t)) = −1/t; iterating,
Q₊⁴(t) = t with Q₊²(t) = −1/t ≠ t (e.g. at t = 0: ∞ ≠ 0), so order exactly 4
in PGL(2,ℝ). Orbit: Q₊(0) = 1, Q₊(1) = ∞ (projective), Q₊(∞) = −1,
Q₊(−1) = 0; via C12 these are x = 0, π/2, π, 3π/2. ∎ **PROVED.**
(Measured as well: B1–B4 NC all OK; B6a/b/c exact; B7 NC; run 2026-09-22 —
CHECKED corroboration of the proved algebra.)

**C14 — the harmonic cross-ratio.** *Statement:* the ordered quadruple
(0, ∞; 1, −1) has cross-ratio −1 (ordering matters). *Proof:* with
λ(z₁,z₂;z₃,z₄) = (z₃−z₁)(z₄−z₂)/((z₃−z₂)(z₄−z₁)), substituting
(0,∞;1,−1) and taking the projective limit at ∞ gives
λ = (1−0)(−1−∞)/((1−∞)(−1−0)) → −1. ∎ **PROVED** (exact algebra;
B8 "exact" in the run). Infinity is a chart value; the harmonic −1 selects
no chirality — immediate from the computation. **PROVED.**

**C15 — determinant separates cophase from reflection.** *Statement:* with
A₊ = [[1,1],[−1,1]] (so Q₊(t) = (t+1)/(−t+1)) and R(t) = −t:
det A₊ = +2 > 0 (orientation-preserving on RP¹) while det R = −1
(orientation-reversing); scalar reflection conjugates Q₊ to Q₋,
R∘Q₊∘R = Q₋. *Proof:* det [[1,1],[−1,1]] = 1+1 = 2; the reflection matrix
diag(−1,1) has det −1 (I2). Conjugation: −Q₊(−t) = −(1−t)/(1+t) = (t−1)/(1+t)
= Q₋(t). ∎ **PROVED** (B9 "exact", B5 NC OK in the run). That reflection is
still not automatically a mirror frame is the page's clarification —
**ASSERTED** (terminological).

---

## D. The universal positive reciprocal transform (book 3.IV)

**C16 — f is a strictly decreasing bijection ℝ → (0,∞) with exact inverse.**
*Statement:* f(u) = √(1+u²) − u is strictly positive, strictly decreasing, a
bijection ℝ → (0,∞) with inverse u = (1−s²)/(2s); f(−u)·f(u) = 1; and
f(u) = e^{−arsinh u}. *Proof:* √(1+u²) > |u| ≥ u gives f(u) > 0 (I1).
Derivative f′(u) = u/√(1+u²) − 1 < 0 since u < √(1+u²); strictly decreasing,
continuous, limits +∞ at −∞ and 0⁺ at +∞ — hence a bijection ℝ → (0,∞).
Inverse: s = √(1+u²) − u ⇒ √(1+u²) = s + u ⇒ 1 + u² = s² + 2su + u² ⇒
u = (1 − s²)/(2s), valid for s > 0. Reciprocal:
f(−u)·f(u) = (√(1+u²)+u)(√(1+u²)−u) = (1+u²) − u² = 1. Exponential form:
arsinh u = ln(u + √(1+u²)); then
e^{−arsinh u} = 1/(u + √(1+u²)) = (√(1+u²) − u)/((1+u²) − u²) = f(u). ∎
**PROVED** (B20 "exact", B22 "exact" corroborate).

**C17 — the unit threshold recovers the sign.** *Statement:*
sgn(u) = sgn(1 − s²) where s = f(u). *Proof:* s = 1 ⟺ u = 0 by C16's inverse
((1−s²)/(2s) = 0 ⟺ s = 1); f strictly decreasing (C16) gives u > 0 ⟺ s < 1
⟺ 1 − s² > 0. ∎ **PROVED.**

**C18 — one map generates all four primitives.** *Statement:*
sxp(x) = f(cot x), srx(x) = f(−cot x), crx(x) = f(tan x), cxp(x) = f(−tan x),
with logarithmic coordinates arsinh(cot x) = ln srx = −ln sxp. *Proof:*
from D3, sxp(x) = |csc x| − cot x; with u = cot x,
f(u) = √(1+cot²x) − cot x = √((sin²x+cos²x)/sin²x) − cot x
     = |1/sin x| − cot x = |csc x| − cot x = sxp(x) (I1). The other three
are identical with tan/cot and signs. Logarithms: from C16's exponential
form, ln f(u) = −arsinh u; hence ln srx = ln f(−cot x) = arsinh(cot x) and
ln sxp = ln f(cot x) = −arsinh(cot x) = −ln srx, using f(−u) = 1/f(u).
∎ **PROVED.** (Suite B21a–d NC all OK, max residual 1.136e-13; B41a/b NC OK
with B41b's 2.391e-10 noted on the page as float cancellation in
ln srx + ln sxp — the identity itself is the exact algebra just shown.)
Consistency note: the campaign seed's Lemma 1 (A − 1/A = 2 tan x with
A = tan x + |sec x| = crx) is the same reciprocal-pair algebra: with
cxp = |sec x| − tan x = 1/A (since A·cxp = sec²x − tan²x = 1), the seed
gives crx − cxp = 2 tan x — the PROVED seed and C18 agree. Cited, not
re-proved.

**C19 — threshold formulas.** *Statement:* sgn(1 − sxp²) = sgn(srx² − 1)
(and the cxp/crx analogue). *Proof:* from C18, srx = 1/sxp; so
srx² − 1 = (1 − sxp²)/sxp², and sxp² > 0 gives equal signs. ∎ **PROVED**
(B42a/b NC OK, max residual 0, run 2026-09-22).

**C20 — no single-valued global RP¹ coordinate.** *Statement:* the unequal
limits f(u) → 0⁺ (u → +∞) and f(u) → +∞ (u → −∞) bar a single-valued global
RP¹ coordinate. *Proof:* limits from C16 (I1); a global RP¹ coordinate would
have to identify the two ends compatibly, but the reciprocal pair takes
distinct unequal limit values 0 and ∞ — no single-valued continuous
extension assigns one value to both ends. ∎ **PROVED** (B22 "exact" in the
run).

---

## E. The cophase–FlatWave character (book 3.V)

**C21 — Γ_c preserves the domain.** *Statement:* Γ_c = ⟨τ_{π/2}⟩ ≅ C4
preserves D. *Proof:* the seams are x = kπ/2; τ_{π/2} permutes them
(k ↦ k+1), so D is invariant; C1 gives Γ_c ≅ C4. ∎ **PROVED.**

**C22 — reversal and invariance.** *Statement:* FlatWave(x ± π/2) =
−FlatWave(x); FlatWave(x + π) = FlatWave(x); the cophase orbit is
ε → −ε → ε → −ε → ε. *Proof:* sin(2(x+π/2)) = sin(2x+π) = −sin(2x) (I1);
sgn flips. sin(2(x+π)) = sin(2x + 2π) = sin(2x); invariant. Iterating the
reversal gives the orbit. ∎ **PROVED** (B23, B24, B25, B26, B27b all NC OK
in the run, residuals 0).

**C23 — the character and its kernel.** *Statement:*
χ_c(τ_{kπ/2}) = (−1)^k is a homomorphism Γ_c → {±1} with
FlatWave(g·x) = χ_c(g)·FlatWave(x); ker χ_c = {id, τ_π}; it factors through
C4/{0,2} ≅ C2. *Proof:* (−1)^{k+l} = (−1)^k(−1)^l gives the homomorphism;
C22 is the equivariance; kernel = {τ_{kπ/2} : k even} = {id, τ_π}; the
quotient by the kernel is C2. ∎ **PROVED.**

**C24 — the octant sign law.** *Statement:* FlatWave|_{O_j} = (−1)^{⌊j/2⌋}.
*Proof:* on O_j, jπ/4 < x < (j+1)π/4, so jπ/2 < 2x < (j+1)π/2. The sign of
sin on successive half-π intervals alternates every two intervals:
j = 0,1 → 2x ∈ (0,π), sin > 0 = (−1)^0; j = 2,3 → 2x ∈ (π,2π), sin < 0 =
(−1)^1; j = 4,5 → (−1)^2 = +1; j = 6,7 → (−1)^3 = −1. ∎ **PROVED**
(B27 NC OK at all 8 midpoints, run 2026-09-22). Dominance and FlatWave are
different quotients — immediate: C9's quotient has four classes, C24's has
two. **PROVED.**

**C25 — the projective sign polynomial.** *Statement:*
FlatWave(x) = sgn[t(1 − t²)] with t = tan(x/2); cophase reverses and the
half-turn preserves this sign polynomial. *Proof:* with t = tan(x/2) (I1),
tan x = 2t/(1−t²) and sin 2x = 2 tan x/(1+tan²x) = 4t(1−t²)/(1+t²)²; the
prefactor 4/(1+t²)² > 0, so sgn(sin 2x) = sgn(t(1−t²)). Cophase sends
t ↦ Q_±(t); a direct sign check gives sgn(Q₊(t)(1−Q₊(t)²)) = −sgn(t(1−t²))
(reversal), while the half-turn t ↦ −1/t preserves it. ∎ **PROVED**
(B34, B36 NC OK with residual 0, run 2026-09-22).

**C26 — the character is binary but lossy.** The page's 3.V.CL1: χ_c detects
cophase parity, not the four orbit positions. This is an interpretive gloss
on C23 (a {±1}-valued map cannot separate four points) — **ASSERTED**
(interpretive; the page itself tags it MA).

Scope declaration (page 3.V): no bundle, orientation, mirror, spin, or
chirality inference is drawn here — recorded as **ASSERTED** (the page's
own MA scope declaration).

---

## F. The RP² atlas and reciprocal charts (book 3.VI)

**C27 — cyclic ratio identity.** *Statement:* on P° = {XYZ ≠ 0}, the cyclic
ratios u_{XY} = Y/X etc. satisfy u_{XY}·u_{YZ}·u_{ZX} = 1; two ratios are
complete, with inverse (a,b) ↦ [1:a:ab]. *Proof:* the product is
(Y/X)(Z/Y)(X/Z) = 1 by field arithmetic — the atlas itself (homogeneous
triples modulo scaling, affine cover U_X,U_Y,U_Z) is the declared import I3.
Completeness: given a = Y/X, b = Z/Y on U_X, X is fixed to 1 by scaling,
so [1:a:ab] recovers the point; the inverse is continuous. ∎ **PROVED**
(from I3; B43 NC OK, residual 3.331e-16).

**C28 — reciprocal compatibility surface.** *Statement:* with σ_{IJ} =
f(u_{IJ}), (1−σ_{XY}²)(1−σ_{YZ}²)(1−σ_{ZX}²) = 8σ_{XY}σ_{YZ}σ_{ZX} on P° —
a reparameterization of the projective identity, not new content. *Proof:*
substitute σ = f(u) with inverse u = (1−σ²)/(2σ) (C16) into C27's identity
u_{XY}u_{YZ}u_{ZX} = 1 and clear denominators; the computation is exact
algebra. ∎ **CHECKED** as a completed float evaluation (B44, residual
5.684e-12, OK, run 2026-09-22); the underlying identity is the exact
substitution just shown. (The page tags the theorem CP; the run I can
independently witness is the NC evaluation, so CHECKED is the honest label
for my citation.)

**C29 — methodological rules.** Compatibility lives only on P°; the threshold
σ = 1 records a signed-ratio zero, not automatically mirror/orientation;
u ↦ −u ≠ u ↦ 1/u. The first is immediate from C27's domain; the third is
algebra; the middle clause is the page's methodological rule — recorded as
**ASSERTED**.

**C30 — seam taxonomy.** The deeper overlap computations (e.g. the overlap
Jacobian J_{XY} = −u^{−3}) were, by the page's own admission, "read at
section level, not independently re-derived." **ASSERTED** (the page's MA;
not re-derived in this task).

---

## G. The tautological bundle and the FlatWave comparison (book 3.VII)

**C31 — the transition-sign cocycle.** *Statement:* with the standard
tautological line bundle γ over RP² (import I3), local frames satisfying
e_Y = (X/Y)e_X, the transition signs ζ_{YX} = sgn(X/Y) satisfy the Čech
cocycle identity ζ_{ZY}·ζ_{YX} = ζ_{ZX}. *Proof:* sgn is multiplicative and
(Z/Y)(Y/X) = Z/X; hence sgn(Z/Y)·sgn(Y/X) = sgn(Z/X). ∎ **CHECKED**
(B45 "exact" in the run, 2026-09-22). That this sign cocycle represents
a = w₁(γ) is the standard import I4 — **ASSERTED** as imported (the page
itself tags the identification SI).

**C32 — the tautological lift flips.** *Statement:* the half-angle map
ρ: 𝕋₂π → L_Z ≅ RP¹ is bijective; the tautological lift satisfies
v(x + 2π) = −v(x), so the pulled-back bundle is nontrivial; the pulled-back
transition sign is ρ*ζ_{YX} = sgn(t). *Proof:* bijectivity is the analytic
half-angle identification (I1, I3); the flip v(x+2π) = −v(x) is **CHECKED**
(B48, residual 5.829e-16, run 2026-09-22); nontriviality follows from the
flip (a trivial bundle would admit a nowhere-zero section with no sign
change — standard covering theory, I6-flavored); ρ*ζ_{YX} = sgn(t) is the
page's computed pullback, consistent with C12's coordinate. **CHECKED**
for the flip; the bijectivity/nontriviality reasoning is PROVED modulo the
declared imports.

**C33 — FlatWave versus the tautological sign.** *Statement:*
FlatWave = (ρ*ζ_{YX})·sgn(1 − t²), agreeing with the tautological sign only
on |t| < 1; they are pointwise different functions (agree on |t|<1,
disagree on |t|>1). *Proof:* C25 gives FlatWave = sgn(t(1−t²)) =
sgn(t)·sgn(1−t²) (B34 NC OK, residual 0); C32 gives ρ*ζ_{YX} = sgn(t).
The factorization is exact sign algebra; the agreement/disagreement regions
are immediate (B35a/b "exact" in the run). ∎ **PROVED** (exact sign
algebra; B36 NC cross-check vs sgn(sin 2x), residual 0, corroborates).

**C34 — type separation and the monodromy test.** *Statement:* χ_c ∈
Hom(C4,{±1}) and a ∈ H¹(RP²;ℤ₂) admit no canonical equality (different
mathematical objects); the monodromy test gives tautological −1 against a
FlatWave-multiplier product of +1 around one 2π circuit. *Proof:* the type
claim is immediate — a group character and a cohomology class are different
kinds of object (no canonical identification declared). The monodromy
product: the four cophase FlatWave multipliers are −1,−1,−1,−1 with product
+1 — **CHECKED** (B37 "exact", run 2026-09-22) — against the tautological
lift's single −1 (C32). ∎ Type separation **PROVED**; monodromy product
**CHECKED**.

**C35 — the ratio-transition signs, not FlatWave, realize w₁(γ).**
*Proof:* C31 (+ I4) identifies the transition-sign cocycle with w₁(γ);
C33–C34 show the FlatWave character differs from that cocycle by the factor
sgn(1−t²) and fails the monodromy test. ∎ **PROVED** (conditional on the
declared import I4 — the w₁-from-signs identification; the page tags the
conclusion CP). The prior-paper audit ("FlatWave = projective orientation
invariant" corrected) is the page's historical note — **ASSERTED**.

---

## H. Tangent orientation of RP^n (book 3.VIII)

**C36 — the Stiefel–Whitney premises.** The stable tangent relation
T RP^n ⊕ 1 ≅ (n+1)γ_n and the Whitney product law are the declared standard
imports I5. **ASSERTED** (SI; the page tags them SI).

**C37 — the tangent formula and orientability.** *Statement:*
w(T RP^n) = (1 + a_n)^{n+1}, hence w₁(T RP^n) = (n+1)a_n; RP^n is orientable
iff n is odd. *Proof:* from C36 by the Whitney law (I5),
w(T RP^n ⊕ 1) = w((n+1)γ_n) = (1 + a_n)^{n+1} (I5, binomial expansion over
ℤ₂); stability of w under ⊕1 (I5) gives w(T RP^n) = (1+a_n)^{n+1}; the
degree-1 term is (n+1)a_n, which vanishes iff n+1 is even. ∎ **PROVED**
(modulo declared I5).

**C38 — diagnostics.** *Statement:* RP¹ is orientable while γ₁ is
nonorientable (a line-bundle obstruction is not a manifold obstruction);
RP² is nonorientable with w₁(T RP²) = a₂ (the ratio-transition class, not
FlatWave — C35); RP³ is orientable, essential for RP³ ≅ SO(3) (see J).
*Proof:* immediate from C37: n = 1 gives w₁ = 0 (orientable) while w₁(γ₁) =
a₁ ≠ 0 (I5); n = 2 gives w₁ = 3a₂ = a₂ ≠ 0; n = 3 gives w₁ = 4a₃ = 0. ∎
**PROVED** (modulo I5).

**C39 — the minus sign is convention.** The fixed minus sign in
sgn J_{XY} = −ε_{XY} is a coboundary-level chart-order convention, not new
topology. The overlap computation was not independently re-derived in this
task (cf. C30) — recorded at the page's status: **ASSERTED** (the page tags
it CP; I record the computation as not re-derived here).

**C40 — global frame classification.** A global positive-vs-mirror
tangent-frame classification exists exactly for odd n (orientability, C37) —
and even then the positive label is not canonically selected. *Proof:*
orientability is exactly the existence of a global frame orientation (I5);
non-canonicity: two global orientations differ by the deck of the
orientation double cover, with no distinguished choice declared. ∎
**PROVED** (modulo I5). Cophase parity is not tangent orientation;
FlatWave reversal does not imply mirror reversal; nonorientability does not
choose chirality — immediate from C7, C23, C37. **PROVED.**

---

## I. Spin-lift conditions (book 3.IX)

**C41 — spin criterion premises.** The spin criterion (w₁ = w₂ = 0),
stability of w₂ under ⊕1, and H*(RP^n;ℤ₂) ≅ ℤ₂[a_n]/(a_n^{n+1}) are the
declared imports I5. **ASSERTED** (SI).

**C42 — w₂ of the tangent bundle.** *Statement:*
w₂(T RP^n) = C(n+1,2)·a_n²; for n = 1 the degree-two group vanishes so
w₂ = 0. *Proof:* from w(T RP^n) = (1+a_n)^{n+1} (C37), the degree-2 term is
the binomial coefficient C(n+1,2)a_n² (I5). For n = 1, H²(RP¹;ℤ₂) = 0 by I5,
so w₂ = 0. ∎ **PROVED** (modulo I5).

**C43 — spin existence theorem.** *Statement:* RP^n is spin iff n = 1 or
n ≡ 3 (mod 4). *Proof:* spin ⟺ w₁ = w₂ = 0 (C41). w₁ = 0 ⟺ n odd (C37).
For odd n ≥ 3, w₂ = 0 ⟺ C(n+1,2) even (C42, I5 with a_n² ≠ 0 for n ≥ 2).
C(n+1,2) = (n+1)n/2; for odd n = 2m+1 this is (m+1)(2m+1), even ⟺ m odd ⟺
n ≡ 3 (mod 4). n = 1 is spin by C42. Hence: spin ⟺ n = 1 or n ≡ 3 mod 4. ∎
**PROVED** (elementary parity; exact-integer corroboration B38 for n = 1…7,
"exact", run 2026-09-22 — CHECKED corroboration of the proved arithmetic).
Orientability strictly weaker than spin: RP⁵ orientable (C37) with w₂ =
C(6,2)a₅² = 15a₅² = a₅² ≠ 0 — **PROVED**. Every spin RP^n has exactly two
spin structures — standard spin theory, import — **ASSERTED** (SI; the page
tags CP). The mod-8 refinement adds no new obstruction — the page's
interpretive note, **ASSERTED** (MA).

**C44 — explicit stable Clifford-lift audit.** The page records a checked
audit with the corrected (tautological, not FlatWave) sign cocycle. The
audit computation is not reproduced in this task — recorded at the page's
status: **ASSERTED** (page CP; not independently re-run here).

---

## J. RP³, SO(3), Rodrigues coordinates, the double cover (book 3.X)

**C45 — the quaternion model premises.** Spin(3) ≅ S³ as the unit quaternions
is the declared import I6. **ASSERTED** (SI).

**C46 — the covering map.** *Statement:* Φ(q)(v) = qv q̄ lands in SO(3);
Φ: S³ → SO(3) is a homomorphism whose kernel contains {±1}; each rotation's
fiber contains {q, −q}; axis-angle lifts satisfy q(θ+2π, n) = −q(θ, n).
*Proof of the measured parts:* **CHECKED** — B47a (|qvq̄| = |v|,
residual 1.332e-15), B47b (scalar part 0, 3.331e-16), B47c (Φ(−q) = Φ(q),
residual 0), B47d (R(q)ᵀR(q) = I, 8.882e-16), B47e (det R(q) = +1,
1.221e-15): all OK, run 2026-09-22. The half-angle flip: with
q(θ,n) = cos(θ/2) + sin(θ/2)n (I6), q(θ+2π,n) = cos(θ/2+π) + sin(θ/2+π)n =
−q(θ,n) — **PROVED** (modulo I6). Surjectivity of Φ and exactness of the
kernel {±1} (beyond containment, B47c) are the standard import —
**ASSERTED** (SI; the page tags the covering theorem CP).

**C47 — the Rodrigues chart.** *Statement:* r = q_V/q₀ is lift-blind
(r(−q) = r(q)); the inverse lift pair is q_±(r) = ±(1+r)/√(1+‖r‖²);
composition is a⊕b = (a+b+a×b)/(1−a·b) under the ij = k convention (I8),
reducing to tangent addition collinearly. *Proof of the measured parts:*
**CHECKED** — B39 (‖q₊(r)‖ = 1, residual 4.441e-16), B40 (composition =
tangent addition collinearly, residual 6.079e-16), run 2026-09-22.
Lift-blindness r(−q) = r(q) is immediate from the formula (both numerator
and denominator change sign). The convention ij = k is a declaration —
**ASSERTED**. ∎

**C48 — the certified bridge.** *Statement:* on 0 < θ < π, ‖r‖ = tan(θ/2) =
sxp(θ) — an exact, chart-qualified coordinate identification; the FlatWave
seam θ = π/2 (ρ = 1) is regular in the Rodrigues chart (q₀ = 1/√2 ≠ 0); the
chart boundary is q₀ = 0 (θ → π, ρ → ∞). *Proof:* from the axis-angle lift
(I6), q₀ = cos(θ/2), q_V = sin(θ/2)n, so ‖r‖ = tan(θ/2) for θ ∈ (0,π).
From C18, sxp(θ) = f(cot θ); for θ ∈ (0,π), |csc θ| = csc θ, so
sxp(θ) = csc θ − cot θ = (1 − cos θ)/sin θ = tan(θ/2) (I1). Hence
‖r‖ = tan(θ/2) = sxp(θ). At θ = π/2: ρ = tan(π/4) = 1, q₀ = cos(π/4) =
1/√2 ≠ 0 — seam regular. At θ → π: q₀ → 0, ρ → ∞ — chart boundary. ∎
**PROVED** (modulo I6; B28 NC OK residual 1.317e-14; B29, B30, B31 "exact"
in the run). The projective state [q] reconstructs the rotation but not the
lift sign — immediate from r(−q) = r(q) (C47). **PROVED.**

---

## K. Lift, mirror, and chirality nonselection (book 3.XI)

**C49 — no global continuous lift selector.** *Statement:* no continuous map
s: SO(3) → S³ with Φ∘s = id exists. *Proof:* such an s would be a continuous
section of the double cover Φ; a double cover admitting a continuous section
is trivial (I6, standard covering theory); but S³ is connected (I6) while a
trivial double cover of the connected base SO(3) has disconnected total
space S³ ⊔ S³ — contradiction. Local branches exist: the Rodrigues
q₀ > 0 hemisphere gives an explicit smooth local section (C47). Bare
discontinuous selectors need added branch/cut conventions — declared.
∎ **PROVED** (modulo declared covering-theory imports I6; the page tags
3.XI.T1 CP).

**C50 — deck-blind data cannot see the fiber sign.** *Statement:* nothing
factoring through SO(3) distinguishes q from −q; the deck involution δ is
not mirror (both lifts sit in the det +1 component, C46/B47e); cophase,
half-turn, and deck shift have distinct quotient effects (cophase changes
the rotation and reverses FlatWave — C22; half-turn changes the rotation
and preserves FlatWave — C22; deck shift fixes the rotation, flips q → −q,
preserves FlatWave — B26 NC OK). *Proof:* the first clause is definitional
(factoring through SO(3) means constant on {q,−q}); the rest is C22, C46,
B47e, B26. ∎ **PROVED.** The further clause "every certified Book 2
operator, including FlatWave, is invariant under the 2π deck shift" is a
bookkeeping survey over the Book 2 corpus, not re-audited here —
**ASSERTED** (the page tags it CP).

**C51 — the nonselection theorem.** *Statement:* none of (i) cophase,
(ii) half-turn, (iii) FlatWave, (iv) reciprocal/UNA operators,
(v) projective/Rodrigues coordinates, (vi) tautological/tangent classes,
(vii) spin-structure existence, (viii) the fiber sign q vs −q, (ix) the O(3)
mirror component selects a preferred lift sign or a physical chirality.
*Proof sketch (as recorded):* (i)–(iii) are deck-blind or character-valued
(C50, C23); (iv) is built from deck-invariant data (C50's bookkeeping
clause); (v) is lift-blind (C47–C48); (vi) are bundle classes independent
of any lift choice (C31, C37); (vii) is an existence statement (C43) with
exactly two structures and no distinguished one; (viii) is the fiber itself
with no canonical selector (C49); (ix) the O(3) mirror component is
disjoint from SO(3) and its lifts. The "no canonical selector even allowing
discontinuity, by the Book 0 naturality obstruction" step invokes Book 0
machinery not re-derived in this task. **ASSERTED** as the page's certified
theorem (page CP): the component arguments are proved above, but the global
negative claim rests in part on bookkeeping and the un-re-derived
naturality obstruction, so it is not upgraded to PROVED here.

**C52 — necessary conditions for any future mechanism.** Deck sensitivity,
global consistency, orientation sensitivity, empirical bridge (3.XI.NC1–NC4):
forward-looking requirements, not theorems — **ASSERTED** (the page's own
MA).

---

## L. Vocabulary freeze and closure (book 3.XII)

**C53 — definitions frozen.** Twelve canonical definitions (phase point,
cophase, half-turn, phase fold, FlatWave sign, projective antipode,
transition sign, tangent orientation, spin structure, lift sign, mirror
frame, physical chirality) — declarations. **ASSERTED** (definitions).

**C54 — vocabulary separation.** The twelve items are kept distinct absent
an explicit identifying theorem. True by inspection of the declaration list
— **PROVED** as bookkeeping (the separation is the absence of any declared
identification; C7, C33–C35, C40, C50 are the proved non-identifications).

**C55 — dependency audit.** The dependency graph is certified acyclic with no
retroactive use of later results — the page itself notes "acyclicity was not
machine-checked" (MA). The claim-dependency order exhibited in §§A–K above
is acyclic by construction. The book's own graph audit is recorded as
**ASSERTED** (bookkeeping audit at the page's MA status).

**C56 — binary noncollapse.** The book's binary/two-sheeted objects do not
reduce to one universal ℤ₂ — survey claim over the proved separations
(C4 vs C23 vs C46 vs C49: different groups, different structures).
Recorded as **ASSERTED** (bookkeeping synthesis; the page tags CP).

**C57 — provenance discipline and the inheritance lock.** Standard
mathematics and Projection-specific deductions kept provenance-distinct;
every certified theorem survives removal of physical interpretation; no
physical chirality follows from the mathematics alone; the three climaxes
are mutually compatible (different structures/scales); a later book may not
strengthen a Book 3 theorem merely by changing vocabulary (3.XII.T6,
constitutional rule). The compatibility and no-physics-consequence claims
follow from the proved separations — **PROVED** as bookkeeping; the
inheritance lock is a constitutional rule — **ASSERTED**.

**Zero counts (page 3.XII / Part IV):** new axioms 0, external physics
imports 0, projection contracts 0, preferred-orientation/lift/chirality
axioms 0, empirical calibrations 0, claims of a new physical interaction 0.
These are counts over the declaration list — **PROVED** as bookkeeping.

---

## New axioms / assumptions beyond Euclid + seed

Beyond Euclid's Elements (which is *not* used as a premise — see boundary
note) and the campaign seed, the extension rests on:

- **N1.** The analytic substrate as declared background: real analysis with
  sin/cos/tan/sgn/absolute value (I1), linear algebra (I2). Not earned from
  Euclid; declared.
- **N2.** The vocabulary declarations D1–D9 (phase circle, cophase, the four
  primitive formulas, FlatWave with seam-excluding domain, the fold,
  projective coordinate, f(u), octants, lift selector/deck involution).
- **N3.** π-periodicity of the canonical primitives (I7) — the page's own
  MA-tagged Book 2 inheritance; no Book 2 proof file exists in this batch.
- **N4.** Standard-import premises used without proof: the RP² affine atlas
  and tautological bundle (I3); the sign-cocycle ⇒ w₁ identification (I4);
  the stable tangent relation, Whitney law, cohomology ring, spin criterion
  (I5); the quaternion model of Spin(3) and covering-space theory (I6);
  the ij = k convention (I8).
- **N5.** Bookkeeping inheritances not re-audited here: Book-2-operator deck
  invariance (C50's second clause); the explicit stable Clifford-lift audit
  (C44); the overlap/seam-taxonomy computations (C30, C39); the Book 0
  naturality obstruction behind C51's strongest clause; the dependency-graph
  acyclicity audit (C55).
- **N6.** Terminological/methodological stipulations: the
  prohibited-substitutions list and "mirror frame" definition (C7); the
  "dominance is not dynamics" note (C9); the four necessary conditions for
  future chirality mechanisms (C52); the inheritance lock (C57).
- **Explicitly zero:** no new physical axiom, no preferred-orientation,
  preferred-lift, or preferred-chirality axiom, no empirical calibration
  (matches the page's zero counts).

**No-Euclid-wholesale boundary (honest statement).** Rewrite Book 3 is not
an extension of Euclid's *Book 3* (the synthetic theory of circles): the
Elements' 37 circle propositions are neither cited as premises nor
re-derived — the book-3 Euclid ledger finds the extension program
INCOMPLETE across all 37. What is extended here is a synthetic-constructive
*stratum* (definitions first, dependency order, nothing used before it is
proved) on a declared analytic substrate, together with standard imported
topology (I3–I6). No wholesale inheritance of the Elements is claimed.

---

## Claim inventory and counts

| # | Claim (one line) | Scope |
|---|---|---|
| C1 | τ_{π/2} exact order 4; τ_{π/2}² = τ_π | PROVED |
| C2 | cophase symmetric, irreflexive, not transitive | PROVED |
| C3 | cophase exchanges sin/cos up to sign | PROVED (from I1) |
| C4 | fold gives one involution of order 2 on 𝕋_π | PROVED |
| C5 | det-sign orientation classes, basis-independent | PROVED (from I2) |
| C6 | τ_a preserves phase-circle orientation | PROVED (from I1) |
| C7 | cophase–mirror separation + prohibited substitutions | ASSERTED (declaration) |
| C8 | η exact order 8, faithful octant action | PROVED (+B46a exact) |
| C9 | dominance cycle, strict gaps at midpoints | CHECKED (B10 NC) |
| C10 | P_c = (srx crx)(sxp cxp); C_dom² = P_c; C_dom order 4 | CHECKED (B46b/c exact) |
| C11 | π-periodicity inheritance (Book 2) | ASSERTED (page MA) |
| C12 | t = tan(x/2) bijection 𝕋₂π → ℝ̂ | PROVED (from I1) |
| C13 | cophase = Q_±; order 4; marked orbit = cardinal phases | PROVED (+B1–B7 corroboration) |
| C14 | harmonic cross-ratio (0,∞;1,−1) = −1 | PROVED (+B8 exact) |
| C15 | det A₊ = +2 vs det R = −1; conjugation | PROVED (+B9 exact, B5) |
| C16 | f bijection ℝ → (0,∞), inverse, reciprocal, exp form | PROVED (+B20/B22 exact) |
| C17 | threshold rule sgn(u) = sgn(1−s²) | PROVED |
| C18 | one map generates four primitives; log coordinates | PROVED (+B21/B41 corroboration; seed-consistent) |
| C19 | threshold formulas sgn(1−sxp²) = sgn(srx²−1) | PROVED (+B42, residual 0) |
| C20 | unequal limits bar global RP¹ coordinate | PROVED (+B22 exact) |
| C21 | Γ_c ≅ C4 preserves D | PROVED |
| C22 | FlatWave reversal/invariance; ε-orbit | PROVED (+B23–B27b) |
| C23 | character χ_c, equivariance, kernel {id,τ_π} | PROVED |
| C24 | octant sign law (−1)^{⌊j/2⌋}; dominance ≠ FlatWave quotient | PROVED (+B27) |
| C25 | FlatWave = sgn[t(1−t²)]; cophase reverses, half-turn preserves | PROVED (+B34/B36, residual 0) |
| C26 | character binary but lossy | ASSERTED (interpretive) |
| C27 | cyclic ratio identity; two ratios complete | PROVED (from I3; +B43) |
| C28 | reciprocal compatibility surface | CHECKED (B44; exact substitution shown) |
| C29 | methodological rules (P° domain; σ=1; −u ≠ 1/u) | ASSERTED |
| C30 | seam-taxonomy overlap computations | ASSERTED (page MA; not re-derived) |
| C31 | transition-sign Čech cocycle | CHECKED (B45 exact); w₁-identification ASSERTED (I4) |
| C32 | half-angle map bijective; lift flip v(x+2π) = −v(x) | CHECKED (B48); reasoning PROVED (from I1/I3/I6) |
| C33 | FlatWave = (ρ*ζ)·sgn(1−t²); agree only on |t|<1 | PROVED (+B34–B36) |
| C34 | type separation; monodromy +1 vs −1 | PROVED / CHECKED (B37 exact) |
| C35 | ratio signs realize w₁(γ); FlatWave does not | PROVED (conditional on I4) |
| C36 | stable tangent relation + Whitney law | ASSERTED (I5, page SI) |
| C37 | w(T RP^n) = (1+a_n)^{n+1}; orientable iff n odd | PROVED (from I5) |
| C38 | RP¹/RP²/RP³ diagnostics | PROVED (from I5) |
| C39 | sgn J_{XY} minus sign is chart convention | ASSERTED (not re-derived) |
| C40 | positive-vs-mirror frame classification, non-canonical | PROVED (from I5) |
| C41 | spin criterion, cohomology ring, w₂ stability | ASSERTED (I5, page SI) |
| C42 | w₂(T RP^n) = C(n+1,2)a_n²; n=1 case | PROVED (from I5) |
| C43 | spin iff n=1 or n≡3 mod 4; RP⁵ gap; two spin structures | PROVED (+B38 exact); two-structures ASSERTED (SI) |
| C44 | explicit Clifford-lift audit | ASSERTED (page CP; not re-run) |
| C45 | quaternion model of Spin(3) | ASSERTED (I6, page SI) |
| C46 | Φ lands in SO(3), homomorphism, kernel ∋ {±1}; lift flip | CHECKED (B47a–e); flip PROVED (from I6); surjectivity/exact kernel ASSERTED (SI) |
| C47 | Rodrigues chart lift-blind; inverse lifts; composition | CHECKED (B39/B40); convention ASSERTED (I8) |
| C48 | certified bridge ‖r‖ = tan(θ/2) = sxp(θ); seam regular; boundary q₀=0 | PROVED (from I6; +B28–B31) |
| C49 | no global continuous lift selector; local branches exist | PROVED (from I6) |
| C50 | deck-blind data can't see fiber sign; quotient effects distinct | PROVED; Book-2-operator clause ASSERTED |
| C51 | nonselection theorem (nine structures) | ASSERTED (page CP; components proved, global claim bookkeeping) |
| C52 | four necessary conditions for future mechanisms | ASSERTED (forward-looking) |
| C53 | twelve definitions frozen | ASSERTED (definitions) |
| C54 | vocabulary separation | PROVED (bookkeeping) |
| C55 | dependency-graph acyclicity audit | ASSERTED (page MA) |
| C56 | binary noncollapse | ASSERTED (bookkeeping synthesis) |
| C57 | provenance discipline; inheritance lock | PROVED (bookkeeping) / ASSERTED (rule) |
| zero counts | 0 new axioms, 0 physics imports, 0 contracts, 0 preferred-orientation/lift/chirality axioms, 0 calibrations | PROVED (bookkeeping count) |

**Counts:** PROVED 34 · CHECKED 8 · ASSERTED 15 · INCOMPLETE 0.

(Recount audit: PROVED rows — C1, C2, C3, C4, C5, C6, C8, C12, C13, C14, C15,
C16, C17, C18, C19, C20, C21, C22, C23, C24, C25, C27, C33, C35, C37, C38, C40,
C42, C43, C48, C49, C54, C57, plus the zero-counts bookkeeping row = 34.
CHECKED rows — C9, C10, C28, C31, C32, C34, C46, C47 = 8.
ASSERTED rows — C7, C11, C26, C29, C30, C36, C39, C41, C44, C45, C51, C52, C53,
C55, C56 = 15. Total 57 claim rows + 1 bookkeeping row = 58. INCOMPLETE: none.)

**Verification runs cited:** `~/workspace/r-theory-rewrite/validation/book3/verify_book3.py`
— 67 checks, all passed, no timeouts, no failures (re-run 2026-09-22,
exit 0; worst numerical residual 2.4e-10 on B41b, noted as float
cancellation; plotted-identity worst 3.7e-13). Exact (non-float) checks
cited: B6a/b/c, B8, B9, B20, B22, B29, B30, B31, B35a/b, B37, B38, B45,
B46a/b/c.

**What was not done (disclosed):** the overlap/seam-taxonomy computations
(C30, C39), the explicit Clifford-lift audit (C44), and the Book 0
naturality obstruction behind C51 were read on the page but not
independently re-derived — all recorded ASSERTED at the page's own status,
never upgraded. The "Wolfram independently verified" notes on the page are
manuscript assertions I did not witness — excluded from the inventory.
No command timed out; nothing is INCOMPLETE.
