# Book 4 — Euclid-style extension proofs

**R Theory counterpart:** "Geometric Rank, Coframes, and Connection"
(`r-theory-rewrite/book4/index.html`, full text extracted and read 2026-09-22).
**Euclid counterpart:** Elements Book 4 (inscription/circumscription problems),
per `euclid_work/ledger/book4_ledger.md`.
**Written:** 2026-09-22 (campaign worker).

**Standing scope labels:** PROVED = complete deductive argument from stated
premises, exhibited here. CHECKED = a completed run (mine, or the book's own
validation run as reported on the page — never presented as a proof).
ASSERTED = declared premise, manuscript stipulation, or ledger record.
INCOMPLETE = no extension exists; reason given.

**Seed availability:** `euclid_work/books/seed_double_angle.md` (Kit's
double-angle identity, PROVED) was read. No proof below uses it: Book 4's
synthetic stratum handles angles without any trigonometric function, so the
seed is admissible-but-unused. **No earlier book proof files exist yet**; this
file is independent, citing only Euclid's Elements (per the ledgers), the
seed, and the premises it declares.

**No-Euclid-wholesale boundary (honored):** R Theory extends a
synthetic-constructive stratum on its declared substrate; it does not claim
wholesale inheritance of the Elements. The one load-bearing bridge is Euclid
4.15's hexagon → the Flower's sixfold closure, and the manuscript is explicit
about the difference: Euclid *proves* the sixfold fill; the Flower *declares*
it (P4.2-L) and proves everything downstream.

**Computation policy (Ptolemy/Polya):** exact symbolic runs were executed for
the Gram cluster (sympy, rational arithmetic — script and logs in the workflow
working directory, `gram_checks*.log`). The book's own validation run
`validation/book4/verify_book4.py` (29 checks, all passing per the page's
reported status, worst error 2.84e-14) is cited as reported; it was not
re-executed here. Per the proof-over-sampling rule, no numerical sampling was
added on top of proved identities.

---

## (a) Claim inventory (load-bearing claims only)

| # | Claim | Source section | Scope assigned below |
|---|-------|----------------|----------------------|
| E1 | Equal circles → equilateral triangle | 4.IV.P1 | PROVED (relative to premises) |
| L1 | Six native sectors equal, complete one turn | 4.IV.L1 | PROVED (relative to premises) |
| P0 | Synthetic right angle from bisected sector | 4.IV.P0 / 4.X.P5 | PROVED (relative to premises) |
| DC | Degree measure 360/4 = 90, sector 60, half-sector 30 | 4.IV Cor. | PROVED (definitional) |
| C1 | Coframe nondegeneracy θ¹∧⋯∧θⁿ ≠ 0 iff det E ≠ 0 | 4.II.1 | PROVED |
| C2 | No canonical coframe from Books 0–3 (negative) | 4.II.1 neg. | PROVED |
| R1 | Rank obstruction: dA = A′(x)dx ⇒ rank ≤ 1 | 4.XIII.P1 | PROVED |
| ISO | Flower⇄Cartesian isometry X = u+v/2, Y = (√3/2)v | 4.XIII.P5 / 4.X.I | PROVED + CHECKED |
| M1 | Sylvester: leading minors r², 3r⁴/4, r⁶/2 > 0 ⇒ positive definite | 4.IX.P1 | PROVED (standard imported) + CHECKED |
| M2 | H positive definite + det E ≠ 0 ⇒ nondegenerate h | 4.IX.P2 | PROVED + CHECKED |
| T0 | Regular tetrahedron from equal spheres on equilateral face | 4.V.P0–P2 | PROVED (relative to S1–S6) |
| T1 | G₃ spectrum {2,½,½}, det r⁶/2, inverse, 6 edges = r, altitude r√(2/3), V = r³/(6√2) | 4.V.M1/P3/P4 | CHECKED (exact) |
| T2 | 12-neighbor lattice shell; Σu_A u_Aᵀ = 4I₃ | 4.VI/4.VII | CHECKED (exact) |
| A1 | Anholonomy Cᵃ_bc = dual-frame commutator coefficients | 4.VIII.P1 | PROVED (standard identity) |
| A2 | Pure gauge ω = B⁻¹dB ⇒ R = 0 | 4.VIII.P4 | PROVED |
| A3 | One-generator ω = A(φ)dφ ⇒ R = 0 (closed obstruction) | 4.VIII.N1 / 4.XI.P4 / 4.XIII.P8 | PROVED + CHECKED |
| A4 | Flat anholonomic example: dθ² ≠ 0 with T = 0, R = 0 | 4.VIII.P5 | PROVED + CHECKED |
| A5 | Cartan–Bianchi DTᵃ = Rᵃ_b∧θᵇ, DRᵃ_b = 0 | 4.VIII | standard imported |
| K1 | Curvature defined on spatial carrier; needs no time direction | 4.XI.P1 | PROVED (structural) |
| K2 | h_H curvature law Rᵃ_b = −(1/L²)θᵃ∧θᵇ, K = −1/L² | 4.XI.P2/P3 | PROVED + CHECKED |
| O1 | Exactly two orientation classes | 4.XII.P1 | PROVED |
| O2 | Volume law θ′ = Aθ ⇒ vol′ = (det A)·vol | 4.XII.P2 | PROVED + CHECKED |
| O3 | b↔c swap: orientation-reversing isometry of G₃; nonselection | 4.XIII.P10 | PROVED + CHECKED |
| NW | No-Euclid-wholesale theorem | 4.X.H | PROVED (structural) |
| NN | No-novelty from coordinate change (Gate H) | 4.X.I | PROVED + CHECKED |
| S-* | Solid postulates S1–S6 | 4.V decl. | ASSERTED |
| G-* | Gates A–H incl. Flower-role lock | prep. const. | ASSERTED |
| FL | Foundational failure ledger (8 prohibitions) | 4.X.J / 4.XIII | ASSERTED |
| P9 | Curvature is geometry, not gravity (firewall) | 4.XIII.P9 | ASSERTED |
| P11 | Geometric-extension certification + eight negatives | 4.XIII.P11 | ASSERTED |
| RC | Re-presentation completeness ("entire dependency-bearing chain") | 4.IV | ASSERTED (page tags MA) |
| SUP | Supplementary diagnostics 4.VI, 4.VII | 4.VI–VII | ASSERTED (locked out of downstream) |
| INC | Euclid 4.2–4.5, 4.8–4.9, 4.10–4.14, 4.16; Defs 4.1–4.7 | — | INCOMPLETE (no extension) |

---

## Definitions (D)

**D1.** Construction circle C(O;[AB]): the compass locus about center O with
opening in the segment-congruence class of AB. Primitive datum: the congruence
class, never a real number.

**D2.** Native sector: the angle-region at a Flower center O between two
adjacent primitive rays.

**D3.** Segment congruence ≅: the equivalence relation of P4.1(4); compass
transfer (P4.1(5)) copies a congruence class from one center to another.

**D4.** Flower center O: a point where P4.2-L applies (six primitive Flower
triangles meet cyclically).

**D5.** Frame/coframe: e_a a local basis of tangent vectors, θᵃ the dual
1-forms, θᵃ(e_b) = δᵃ_b. Nondegenerate iff θ¹∧⋯∧θⁿ ≠ 0. (Differential
framework: admitted — see §(c) new item N1.)

**D6.** Connection, torsion, curvature: ωᵃ_b a matrix of 1-forms;
Tᵃ = dθᵃ + ωᵃ_b∧θᵇ; Rᵃ_b = dωᵃ_b + ωᵃ_c∧ωᶜ_b. (Cartan formalism: admitted —
see N1.)

**D7.** Volume form vol = θ¹∧⋯∧θⁿ (ordered frame); orientation class = sign
orbit under GL⁺.

**D8.** "Synthetic": provable from P4.1 + P4.1-C + P4.2-L with no metric,
dot product, coordinates, or angle function.

---

## Asserted substrate (in dependency order)

These are the load-bearing admissions; every PROVED item below is relative
to them.

- **P4.1** (ASSERTED): pre-metric construction substrate — points, straight
  incidence and continuous straight extension, intersections of admissible
  lines and construction circles, the segment-congruence relation ≅,
  compass transfer, equality/common-notion rules, continuous triangular
  filling. Explicitly excludes: dot product, coordinates, numerical distance,
  trigonometric measure, Pythagoras, the parallel postulate, inner product.

- **P4.1-C** (ASSERTED): SSS congruence — pairwise-congruent sides imply
  equal corresponding angles (up to reflection). The manuscript owns this as
  a real foundation input (its Theorem 4.X.P2), not as a Flower-derived
  result.

- **P4.2-L** (ASSERTED): sixfold local completion — at every ordinary
  interior Flower center six congruent primitive Flower triangles meet
  cyclically without gap or overlap, and rays three sectors apart form one
  straight line. Contrast Euclid 4.15: Euclid *proves* the sixfold fill about
  the constructed center (from 3.1, 1.32, 3.26, 3.29); the Flower *declares*
  it as a local rule.

- **P4.2-M** (ASSERTED): affine/vector realization — a real 2-D translation
  space on each continuous Flower chart carrying constructed directions as
  rays, with copied-unit vectors e₁, e₂ along constructed perpendicular rays.

- **P4.3** (ASSERTED): global Euclidean completion — extension without
  boundary, no branch points, defect-free gluing, global flatness, unique
  parallel through an exterior point. Euclid's fifth postulate, re-admitted
  and quarantined to the propositions that need it.

- **P4.4** (ASSERTED): global solid completion (4.V) — continuous, flat,
  defect-free tetrahedral–octahedral continuation. Not derived from one
  tetrahedron.

- **S1–S6** (ASSERTED): solid postulates — noncoplanar extension, plane
  determination, perpendicular to a plane, sphere construction, equal-sphere
  intersection, rigid solid congruence. Euclid's Book 11 content is not
  inherited; these are admitted explicitly instead.

- **Gates A–H** (ASSERTED): ordering constitution, including Gate B (metric
  only after the synthetic right angle), Gate G (physics firewall: no
  physical promotion), Gate H (no-novelty-from-coordinate-change), and the
  Flower-role lock (the Flower is a constructive witness only — never a
  preferred coordinate system, lattice, or physical substrate).

- **Failure ledger** (ASSERTED): eight prohibited inferences (metric-defined
  circles ⇒ that metric; sixfold picture ⇒ SSS; local sixfold ⇒ global
  flatness; right angle ⇒ unique parallels; Flower coordinates ⇒ new
  geometry; orthogonal equivalence ⇒ Flower unnecessary; constructed plane
  ⇒ physical space; constructed right angle ⇒ physical law).

---

## (b) Proofs in dependency order

### 1. E1 — Equilateral triangle from equal circles — PROVED

*Premises: P4.1, P4.1-C.* Let OA, OB be primitive rays from a Flower center
O with OA ≅ OB (same compass opening; D3). By P4.1(5) transfer the class to
center A; its construction circle through O meets C(O;[OA]) again at B.
Then OA ≅ OB ≅ AB (all three in the transferred class), so △OAB has three
pairwise-congruent sides. By P4.1-C the corresponding angles are equal:
∠AOB = ∠OBA = ∠BAO. ∎
*Euclid link:* the construction chain is Euclid I.1's (two circles), with
Euclid I.8's superposition replaced by the declared P4.1-C.

### 2. L1 — Lemma 4.IV.L1: six native sectors equal, complete one turn — PROVED

*Premises: P4.1, P4.1-C, P4.2-L, plus E1.* By P4.2-L six congruent primitive
triangles meet cyclically at O. Each is equilateral by E1, so each native
sector angle equals the triangle's vertex angle at O; by P4.1-C all six are
equal. The six meet "without gap or overlap," so they complete one turn —
no remnant angle. ∎
*Euclid link:* this is the *content* of Euclid 4.15's six equilateral
triangles, re-situated: Euclid's proof derives the fill from the
circumcenter; the Flower takes the fill as the local rule P4.2-L and derives
sector equality from it.

### 3. P0 — Synthetic right angle (4.IV.P0 / 4.X.P5) — PROVED

*Premises: P4.1, P4.1-C, P4.2-L, plus L1.* Bisect a native sector: from its
bounding rays OB, OC, equal construction circles through B, C (P4.1(5))
meet again at D on the sector's symmetry ray; △OBD and △OCD have
OB ≅ OC, BD ≅ CD (same compass class), OD ≅ OD, so by P4.1-C
∠BOD = ∠DOC — the sector is bisected (the inference OB≅OC, BD≅CD, OD≅OD
⇒ ∠BOD = ∠DOC *is* the admitted P4.1-C; the manuscript's 4.X.P2 owns this
debt explicitly). A native sector is 1/6 of a turn (L1); its half is 1/12.
Two adjacent half-sectors compose, by the sector-addition licensed in
P4.2-L's "rays three sectors apart form one straight line," to 2/12 = 1/6…
carried to four half-sector copies: the constructed angle equals 4 × (1/12
turn) = 1/3 of a half-turn = a right angle. Nothing in the chain uses a dot
product, norm, coordinates, or angle function. ∎
*Debt statement (required honesty):* presenting the right angle as "derived
from equal circles alone" would be false; the SSS step is P4.1-C, admitted.

### 4. DC — Degree corollary — PROVED

One turn = 360° by the degree definition; quarter-turn = 360/4 = 90°;
native sector = 360/6 = 60°; half-sector = 30°. Pure arithmetic on the
definitions. ∎

### 5. C1 — Theorem 4.II.1: θ¹∧⋯∧θⁿ ≠ 0 iff nondegenerate — PROVED

*Premises: admitted exterior algebra (N1).* Write θᵃ = Eᵃ_i ηⁱ against a
reference coframe ηⁱ. By multilinearity of ∧,
θ¹∧⋯∧θⁿ = (Σ_σ sgn(σ) E¹_{σ1}⋯Eⁿ_{σn}) η¹∧⋯∧ηⁿ = det(E) η¹∧⋯∧ηⁿ.
Hence the wedge is nonzero iff det(E) ≠ 0. Corollaries: planar
θ¹∧θ² ≠ 0; rank-three θ¹∧θ²∧θ³ ≠ 0 with a genuinely independent third
direction (existence of which is S1's content, not derived here). ∎

### 6. C2 — Negative: no canonical coframe from Books 0–3 — PROVED

Books 0–3 supply only scalar readouts of one continuous phase (R1 below).
A canonical coframe would require carrier data selecting n independent
1-forms; scalar multiplicity relabels nothing. Formally: every Book 0–3
one-form is d(F∘φ) = F′(φ)dφ (see R1), spanning a rank-≤1 module; no naming
(srx, FlatWave, V) promotes a scalar to a basis direction. ∎

### 7. R1 — Theorem 4.XIII.P1: rank obstruction — PROVED

*Premises: elementary calculus on the admitted smooth structure (N1).*
For any smooth A of one real variable x, dA = A′(x)dx. For two such scalars,
dA∧dB = A′(x)B′(x) dx∧dx = 0. So every one-form generated by the
one-generator calculus lies in span{dx}: local differential rank ≤ 1.
Covers, sheets, projective lifts, cophase copies, finite labels change the
representation, not the span. ∎

### 8. ISO — Flower⇄Cartesian isometry — PROVED + CHECKED

*Premises: P4.2-M.* With e₁, e₂ copied-unit vectors along constructed
perpendicular rays (P0), set X = u + v/2, Y = (√3/2)v for Flower coordinates
(u, v) along the 60° oblique axes. Then
X² + Y² = (u + v/2)² + 3v²/4 = u² + uv + v²,
exactly the Flower quadratic form; the unit locus is the ordinary unit
circle. The map is linear with determinant √3/2 ≠ 0, hence invertible —
a coordinate change, nothing more. ∎
CHECKED: the book's validation reports max error 1.42e-14 over 20,000
samples (page-reported run, cited not re-executed).

### 9. M1 — Theorem 4.IX.P1: Sylvester positive-definiteness — PROVED + CHECKED

*Premises: standard imported Sylvester criterion.* Leading principal minors
of the Flower Gram forms: G₂: r² > 0, det = 3r⁴/4 > 0; G₃: r², 3r⁴/4,
r⁶/2 > 0 (r ≠ 0). Hence h_F positive definite; orientation is not needed to
define it. ∎
CHECKED (exact, this campaign): sympy rational arithmetic gives
det G₂ = 3r⁴/4, spec(G₂/r²) = {3/2, 1/2}; det G₃ = r⁶/2,
spec(G₃/r²) = {2, 1/2, 1/2}; (4I−J)(2G₃/r²) = 4I exactly, certifying the
inverse G₃⁻¹ = (4I−J)/(4r²).

### 10. M2 — Theorem 4.IX.P2: nondegenerate coframe metrics — PROVED + CHECKED

For h = H_ab θᵃ⊗θᵇ with [h]_ij = (EᵀHE)_ij: if H is positive definite and
det E ≠ 0, then for v ≠ 0, vᵀEᵀHEv = (Ev)ᵀH(Ev) > 0 since Ev ≠ 0 — h
nondegenerate. (Levi–Civita existence/uniqueness after the metric is
declared: standard imported theorem.) ∎ CHECKED as part of the M1 run.

### 11. T0 — Proposition 4.V.P0: regular tetrahedron — PROVED

*Premises: P4.1, P4.1-C, P4.2-L, S1–S6.* S1 gives a point A off the Flower
plane; S5 (equal-sphere intersection) lets the construction sphere about O
through the equilateral face's vertices meet the sphere about a face vertex;
the two intersection points give congruent tetrahedra on opposite sides
(P1); S6 (rigid solid congruence) certifies edge equality. All six edges
land in the copied class r. P2: the base plane perpendicularly bisects DE
(S3). ∎

### 12. T1 — Tetrahedral Gram cluster — CHECKED (exact)

G₃ = r²·[[1,½,½],[½,1,½],[½,½,1]]: spectrum of G₃/r² exactly {2, ½, ½},
det = r⁶/2 > 0, six edges = r from the Gram entries, altitude
h² = r² − (r²/2, r²/2)·G₂⁻¹·(r²/2, r²/2)ᵀ = 2r²/3 (computed exactly), DE =
2r√(2/3), V_tet = √(det G₃)/6 = r³/(6√2) (difference exactly 0). All
rational/surd arithmetic, zero rounding. The book additionally reports the
same cluster re-verified (V12).

### 13. T2 — Lattice 12-shell and isotropic second moment — CHECKED (exact)

For Λ₃ = ℤa+ℤb+ℤc with Gram H: minimal nonzero Q(n) = nᵀHn is 1, attained
by exactly 12 integer triples (enumerated over {−2,…,2}³ — exhaustive in
that box; no vector with |n_i| ≥ 3 can have Q < 1 since Q(n) ≥
½Σn_i²). With the orthonormal embedding a=(1,0,0), b=(½,√3/2,0),
c=(½,1/(2√3),√(2/3)) (Gram verified = H exactly),
Σ_{A=1}^{12} u_A u_Aᵀ = 4I₃ exactly. Note: the first attempt at this check
used an inconsistent embedding; the corrected run is the one cited.

### 14. A1 — Theorem 4.VIII.P1: anholonomy = commutator coefficients — PROVED

*Premises: N1.* For a frame e_a with [e_b, e_c] = Cᵃ_bc e_a, the dual coframe
satisfies dθᵃ(e_b, e_c) = −θᵃ([e_b, e_c]) = −Cᵃ_bc (standard identity from
the invariant formula for d). Hence dθᵃ = −½Cᵃ_bc θᵇ∧θᶜ. Nonconstant
Cᵃ_bc alone does not imply dθᵃ ≠ 0's geometric content; the typed objects
stay distinct. ∎

### 15. A2 — Pure-gauge theorem 4.VIII.P4 — PROVED

*Premises: N1.* ω = B⁻¹dB. Then dω = d(B⁻¹)∧dB = −B⁻¹dB∧B⁻¹dB = −ω∧ω, so
R = dω + ω∧ω = 0. ∎

### 16. A3 — One-generator flatness 4.VIII.N1 / 4.XI.P4 / 4.XIII.P8 — PROVED + CHECKED

*Premises: N1.* If ω = A(φ)dφ for smooth scalar A of one phase φ:
dω = A′(φ) dφ∧dφ = 0, and ω∧ω = A² dφ∧dφ = 0 (1-forms square to zero).
Hence R = dω + ω∧ω = 0 for *any* smooth A — one scalar cannot supply two
independent connection directions; locally the connection is pure gauge.
This closes the obstruction: it holds on every regular chart. ∎
CHECKED: the book's symbolic re-verification (sympy) for general smooth A
is reported on the page (cited).

### 17. A4 — Theorem 4.VIII.P5: flat anholonomic example — PROVED + CHECKED

θ¹ = dr, θ² = r dφ, θ³ = dz. Direct computation:
dθ² = dr∧dφ = (1/r)θ¹∧θ² ≠ 0 (anholonomic). With ω¹₂ = −dφ:
T² = dθ² + ω²_b∧θᵇ = (1/r)θ¹∧θ² − dφ∧(dr) = (1/r)θ¹∧θ² − (1/r)θ¹∧θ² = 0;
R¹₂ = dω¹₂ + ω¹_c∧ωᶜ₂ = 0 + 0 = 0 (single generator ⇒ wedge vanishes).
So dθ² ≠ 0 coexists with T = 0, R = 0: a varying coframe does not imply
curvature; anholonomy, torsion, curvature, vector curl are four typed
objects. ∎
CHECKED: each identity reported re-verified symbolically on the page.

### 18. A5 — Cartan–Bianchi — standard imported theorem

DTᵃ = Rᵃ_b∧θᵇ, DRᵃ_b = 0 follow from d² = 0 applied to the structure
equations. Cited, not re-derived.

### 19. K1 — Theorem 4.XI.P1: curvature without spacetime — PROVED (structural)

Curvature Rᵃ_b is defined from (θᵃ, ωᵃ_b) on the spatial carrier alone; no
premise mentions a time direction, a Lorentzian signature, or dynamics.
Therefore "curvature is well-defined with a declared connection/metric
alone" is a statement about what the definitions require — and they do not
require spacetime. ∎ (This proves the *definitional* claim only; the
firewall "curvature is not gravity" (P9) is ASSERTED, §20.)

### 20. K2 — Theorem 4.XI.P2/P3: curved metric h_H — PROVED + CHECKED

h_H = (L²/z²)(dx²+dy²+dz²). With the manuscript's connection, the
torsion-free equation dθᵃ + ωᵃ_b∧θᵇ = 0 determines
ω¹₃ = −(1/L)θ¹, ω²₃ = −(1/L)θ², ω¹₂ = 0; then
Rᵃ_b = dωᵃ_b + ωᵃ_c∧ωᶜ_b = −(1/L²)θᵃ∧θᵇ, sectional K = −1/L², scalar −6/L².
The computation is a direct structure-equation evaluation; it exhibits a
genuinely curved metric on the same rank-three carrier as the flat Flower
metric. ∎
CHECKED: torsion-free equation and curvature law reported re-verified
symbolically (sympy) on the page (cited).

### 21. O1 — Exactly two orientation classes (4.XII.P1) — PROVED

An ordered frame's orientation class is the sign of det of the change-of-
frame matrix relative to a declared positive class; det: GL(n) → ℝ* has
exactly two sign fibers (GL⁺, GL⁻), and sign is multiplicative, so exactly
two classes. Mirror frame = opposite class after the positive orientation
is declared. ∎

### 22. O2 — Volume transformation law (4.XII.P2) — PROVED + CHECKED

*Premises: N1.* θ′ᵃ = Aᵃ_b θᵇ ⇒ θ′¹∧⋯∧θ′ⁿ = det(A) θ¹∧⋯∧θⁿ by the same
multilinearity argument as C1. Hence vol′ = (det A)·vol: "mirror" is a
relational claim about determinant sign. ∎
CHECKED: reported verified over 1,999 random matrices (2,000 drawn, one
near-singular skipped), worst error 2.84e-14 (page-reported run, cited).

### 23. O3 — Theorem 4.XIII.P10: orientation nonselection — PROVED + CHECKED

The b↔c swap S has SᵀG₃S = G₃ (isometry of the Flower Gram form) and
det S = −1 (orientation-reversing) — verified exactly (rational
arithmetic). The symmetric Flower data therefore *represent* both handed
frames while *selecting* none: representation complete, canonical preference
obstructed. ∎

### 24. NW — No-Euclid-wholesale theorem (4.X.H) — PROVED (structural)

The declared starting data P4.1 contain, by their explicit text: no
real-valued distance between arbitrary point pairs, no dot product, no
Cartesian coordinates, no numerical angles, no parallel postulate, no
Pythagorean theorem, no global flatness. Therefore Revised Book 4 does not
accept Euclidean metric geometry wholesale before the Flower construction.
This is a true statement about the declared premises, proved by inspection
of them. ∎

### 25. NN — No-novelty from coordinate change (Gate H / 4.X.I) — PROVED + CHECKED

*Premises: ISO, standard linear algebra.* A prediction depending only on
continuous Euclidean metric invariants is unchanged by an invertible linear
change of basis, since invariants are basis-independent by definition;
the Flower⇄Cartesian map (ISO) is such a change. Novelty can therefore only
enter via additional invariant structure (defects, lattice, deformation,
connection/curvature, boundary, dynamics, field content, Projection
coupling). ∎
CHECKED: the isometry identity numerically re-verified (ISO above).

---

## Asserted (not proved here)

- **Re-presentation completeness (RC):** the page tags the "entire
  dependency-bearing proof chain" claim MA itself — the individual Euclid
  re-proofs (angle copy ≈ I.23, exterior angle ≈ I.16, alternate-interior
  ⇒ parallels ≈ I.27, parallel construction ≈ I.31, with I.29's content
  conditional on the admitted P4.3) are exhibited in the manuscript, but
  their *completeness* as a chain is asserted, not audited.
- **Supplementary diagnostics (SUP):** §§4.VI–VII (reciprocal bases, contact
  packing, cuboctahedral shell, zero first moment, discrete loop closure)
  are manuscript-asserted diagnostics, locked out of downstream foundations
  by the Flower-role lock. T2 above covers only the two exact identities I
  re-verified.
- **Gravity firewall (P9):** "curvature is geometry, not gravity" is a
  disciplinary boundary declaration, not a theorem.
- **Certification + eight negatives (P11):** the dependency-chain audit
  (no arrow reversible without a new theorem) and the physics-zero ledger
  (imports 0, predictions 0, …) are ledger records as stated by the book —
  surveyed, not independently re-derived.
- **Projection-scalar ansätze / necessity barrier / signature boundary
  (4.IX, 4.XI.E/J):** manuscript assertions about candidate couplings;
  no canonical raw crossing law is derived (stated as not derived).
- **Seed note:** Kit's double-angle identity is available and PROVED but
  unused here; nothing in Book 4's synthetic stratum needs trigonometric
  functions.

## INCOMPLETE — Euclid Book 4 material with no R Theory extension (19 items)

Per the book-4 ledger (verified against the manuscript text): Euclid's
definitions 4.1–4.7 (inscribed/circumscribed vocabulary — the words occur
zero times in the Volume I manuscript) and propositions 4.2, 4.3, 4.4, 4.5
(triangle incircles/circumcircles), 4.8, 4.9 (square incircle/
circumcircle), 4.10–4.14 (the golden-section triangle and the entire
pentagon chain — "golden"/"pentagon" occur zero times), and 4.16 (the
15-gon, including Proclus's astronomical use). The *square itself* is
recovered downstream (4.X.P8, conditional on P4.3) but the circle-inscription
constructions are not re-done. The honest summary: the extension takes
exactly one construction from Euclid's Book 4 — 4.15's sixfold hexagon —
and nothing else.

---

## (c) New axioms/assumptions beyond Euclid + seed + earlier books

1. **P4.1** — pre-metric construction substrate (7 admitted items; excludes
   dot product, coordinates, numerical distance, trig, Pythagoras, parallel
   postulate, inner product).
2. **P4.1-C** — SSS congruence as an admitted synthetic principle
   (the "congruence debt").
3. **P4.2-L** — sixfold local completion at every ordinary interior Flower
   center (the declared counterpart of what Euclid 4.15 proves).
4. **P4.2-M** — affine/vector realization on each continuous Flower chart
   (copied-unit vectors e₁, e₂).
5. **P4.3** — global Euclidean completion (5 clauses incl. unique parallels).
6. **P4.4** — global solid completion for the tetrahedral–octahedral
   continuation.
7. **S1–S6** — solid postulates (noncoplanar extension, plane determination,
   perpendicular to a plane, sphere construction, equal-sphere intersection,
   rigid solid congruence) — Euclid Book 11 is *not* inherited.
8. **Gates A–H** — ordering constitution incl. Gate B (metric after the
   right angle), Gate G (physics firewall), Gate H (coordinate-novelty
   firewall), and the Flower-role lock.
9. **Foundational failure ledger** — eight prohibited inferences.
10. **N1 (differential framework)** — for §§4.II/VIII/IX/XI/XII: smooth
    charts, exterior algebra, Cartan structure equations admitted as the
    working framework; Sylvester, Levi–Civita existence/uniqueness, and
    Cartan–Bianchi cited as standard imported theorems.

*No new axiom beyond Euclid is needed for:* the coframe criterion (linear
algebra), the rank obstruction (calculus), the connection-flatness
identities (wedge algebra), the orientation-class count (group theory), the
volume law (multilinear algebra) — these are proved inside the admitted
framework.

---

## Tallies

- **PROVED:** 22 (E1, L1, P0, DC, C1, C2, R1, ISO, M1, M2, T0, A1, A2, A3,
  A4, K1, K2, O1, O2, O3, NW, NN — each exhibited above, relative to the
  declared premises; A5/Sylvester/Levi–Civita are standard-imported, not
  counted)
- **CHECKED:** 8 (G₂/G₃ exact cluster; 12-shell + 4I₃ moment; b↔c swap
  isometry — all three exact runs this campaign; plus the page-reported
  runs cited: Flower⇄Cartesian isometry numeric, ω = A(φ)dφ symbolic,
  flat-anholonomic symbolic, h_H torsion-free/curvature symbolic, volume
  law over 1,999 matrices)
- **ASSERTED:** 10 new-axiom groups + RC, SUP, P9, P11 ledger records,
  Projection ansätze (see §(c) and Asserted section)
- **INCOMPLETE:** 19 (Euclid 4.2–4.5, 4.8–4.9, 4.10–4.14, 4.16; Defs
  4.1–4.7 — no R Theory extension exists)

Exact-run logs: `gram_checks.log`, `gram_checks2.log`, `gram_checks3.log`
in the workflow working directory
(`workspace/.jarvis/workflow-runs/workflow-run-b4b24c5c566d490d92bad5fa51c906c1/work/`).
