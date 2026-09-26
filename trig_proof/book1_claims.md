# Book 1 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book1_proof.md` (claim inventory
B1.T1–B1.T46 plus the scope census: 1 numerical run, 4 asserted blocks) and
rewrite page `~/workspace/r-theory-rewrite/book1/index.html` (*Book 1 —
Foundations of the One-Generator Calculus*). Evaluated 2026-09-22.

**Verification method.** All 46 proofs read in full. The load-bearing
algebraic identities were independently re-derived and check out exactly
(T11 rational forms; T15 strict positivity; T16 reciprocal conjugacy;
T18 threshold law — quadrant-by-quadrant inequality argument rechecked,
equality cases verified to land exactly on excluded seams; T19 conjugacy
laws; T23 half-angle chart, including the c-channel cross-multiplication;
T26 midpoint values; T28/T12 counter-witness at 5π/4 recomputed). The
limit arguments (T29–T30, T33) were checked by reading for domain errors
and circularity — none found; one looseness noted at T29 (the absolute
value does the work). The dependency DAG was checked for forward
references: exactly one numbering inversion found (T24 cites T25), no
cycle — T25 does not cite T24. "PROVED-in-text" claims (manuscript page
tag P) were evaluated by reading the restated argument for soundness,
circularity, and correct dependence on earlier theorems. The book page's
reported numerical re-verification (111 assertions, all passing, no
timeouts) is cited as CHECKED, not re-run, per the proof-over-sampling
rule. The script exists at
`~/workspace/r-theory-rewrite/validation/book1/verify_book1.py`.

**Euclid.** No Elements proposition is a premise of any proof below. The
ledger `~/workspace/euclid_work/ledger/book1_ledger.md` records zero
deductive links from the Elements into the rewrite series (No-Euclid-wholesale
theorem, 4.X.H, Book 4 §4.X). All five candidate trig principles cite no
Euclid — stated plainly.

**Scope labels:** PROVED (exact mathematics, complete proof verified),
CHECKED (completed computation), ASSERTED (manuscript claim, assumption,
import, convention, or status declaration — not proved or computed),
INCOMPLETE (failed, timed out, or unfinished — none here).

## PROVED claims (45)

| Claim | Restatement | Verdict | Scope | Folded in? | Notes |
|---|---|---|---|---|---|
| T1 | τ_a∘τ_b = τ_{a+b} (translation group law) | proof verified (direct from D2) | PROVED | no — additive group law of the phase line, standard-background level | — |
| T2 | (cos,sin) agree at x,y iff x−y ∈ 2πℤ | proof verified; conditional on standard periodicity/injectivity-on-[0,2π) (S) | PROVED | no — standard trig background, imported as S | — |
| T3 | folding map κ: 𝕋_{2π}→𝕋_π is two-to-one | proof verified (each π-class is exactly {x, x+π} in 𝕋_{2π}) | PROVED | no — torus quotient group theory, not a trig identity | — |
| T4a | no deterministic recovery of the half-turn class (N1) | proof verified (fibers of size 2 from T3) | PROVED | no — negative information result | — |
| T4b | no deterministic recovery of the ℝ lift (N2) | proof verified (infinite class from T2) | PROVED | no — negative information result | — |
| T5 | τ_{π/2} has order 4 on 𝕋_{2π}, order 2 on 𝕋_π | proof verified (τ_{π/2}^n = τ_{nπ/2}; divisibility check) | PROVED | no — finite group orders on tori | — |
| T6 | τ_a, ι, ι_d descend to 𝕋_{2π} and 𝕋_π | proof verified (each preserves the lattices 2πℤ, πℤ) | PROVED | no — well-definedness of quotient maps | — |
| T7 | Σ_s, Σ_c alternating and disjoint; D = ⨆Q_k; D is the largest common domain of tan, cot, sec, csc | proof verified (interlacing by π/2; poles exactly Σ per S) | PROVED | no — domain bookkeeping | — |
| T8 | symmetry transport: ι(Q_k) = Q_{−k−1}, ι_d(Q_k) = Q_{−k}, τ-shifts permute Q_k | proof verified (interval arithmetic recomputed: both index formulas check) | PROVED | no — chart transport machinery | — |
| T9 | four seam classes on 𝕋_{2π}, two on 𝕋_π | proof verified (differences π/2·ℤ ∉ 2πℤ; κ folds two-to-one) | PROVED | no — quotient bookkeeping | — |
| T10 | branch signs locally constant; |csc x| = α/sin x, |sec x| = β/cos x; sgn(tan x) = sgn(cot x) = ε | proof verified (no zeros on Q_k + continuity; α·sin x = |sin x|) | PROVED | no — elementary sign rules at the level of the standard import; not a new principle | trig core is M0-level |
| T11 | branch-explicit rational forms: |csc x|±cot x = (α±cos x)/sin x = (1±ε|cos x|)/|sin x| | proof verified (re-derived both forms; α cos x = ε|cos x| checks) | PROVED | no — algebra from T10, book-operator forms | — |
| T12 | exact conditions for dropping |·|; dropping elsewhere changes the function | proof verified (counter-witness at 5π/4 recomputed: F_s^+ = √2+1 vs cot(5π/8) = 1−√2) | PROVED | no — definitional audit point | — |
| T13 | half-turn sends (α,β)→(−α,−β), ε survives; no π-periodic scalar recovers (α,β) | proof verified (sin(x+π) = −sin x (S); contradiction argument) | PROVED | no — sign bookkeeping + negative result | — |
| T14 | smoothness of the factors on each Q_k | proof verified (compositions of smooth functions, no poles per T7/T10) | PROVED | no — analysis, not an identity | relative to S |
| T15 | strict positivity of all four factors on D | proof verified (re-derived: csc²−cot² = 1 ⇒ |csc x| > |cot x|) | PROVED | **yes — candidate principle** (possible duplicate of Book 0 P2 / Book 2 P2) | trig inequality |
| T16 | reciprocal conjugacy: F_s^+·F_s^− = F_c^+·F_c^− = 1 | proof verified (re-derived: difference of squares = csc²−cot² = 1 (S)) | PROVED | **yes — candidate principle** (possible duplicate of Book 0 P1 / Book 2 P1) | genuine trig identity |
| T17 | sum/difference reconstruction: F_s^+±F_s^− = 2|csc x|, 2cot x | proof verified (addition/subtraction from D5; defined on D per T15) | PROVED | no — algebra from T16 | — |
| T18 | unit-threshold classification: F_s^+ > 1 ⇔ cot x > 0 (s/c, ± swapped); equality never on D | proof verified (re-derived quadrant-by-quadrant: numerator sign analysis + sum-of-squares estimates; equality cases verified to require |sin x cos x| = 0, i.e. excluded seams) | PROVED | **yes — candidate principle** (matches Book 2 P9, which the book-2 audit judged analysis rather than principle — flag for the dedup pass) | trig inequality lemma |
| T19 | conjugacy laws: ι inverts ± within a channel; ι_d swaps channels keeping ±; quarter-turn exchanges channel-conjugately | proof verified (re-derived all three: parity of |csc|/cot, cofunction identities (S)) | PROVED | no — operator-level actions; trig core (parity/cofunction) is M0 background | cf. book-2 P14–P16, not folded |
| T20 | π-periodicity of the factors; descent to 𝕋_π | proof verified (two proofs: tan/cot π-periodic (S) + sign patterns; simultaneous sign-reversal invariance via T11) | PROVED | no — already registered as Book 0 P3(c) | — |
| T21 | pairwise algebraic redundancy; one-dimensional common source | proof verified (T16–T17: one factor determines |csc x|, cot x, hence all four) | PROVED | no — book architecture (redundancy), not a trig identity | — |
| T22 | naming neutrality (Book 2's naming adds no mathematics) | proof verified by reading (definitional act over proved objects; manuscript page tag P) | PROVED | no — methodological, no mathematical content | in-text |
| T23 | principal chart formulas on Q0: F_s^+ = cot(x/2), F_s^− = tan(x/2), F_c^+ = tan(π/4+x/2), F_c^− = tan(π/4−x/2) | proof verified (re-derived; s-channel from standard half-angle (S); c-channel cross-multiplied: (1+t)/(1−t) = tan(π/4+x/2) checks) | PROVED | **yes — candidate principle** (possible duplicate of Book 2 P17) | genuine half-angle identities |
| T24 | ranges (1,∞)/(0,1) and strict monotonicity on every Q_k | proof verified by reading (Q0 from S; transport via T8); directions F_s^+ decreasing etc. check on Q0 | PROVED | no — monotonicity analysis, not an identity | numbering inversion: cites T25 (forward), but no cycle — T25 does not cite T24 |
| T25 | exactly two chart types (even quadrants reuse principal formulas in ξ_k; odd use swapped chart) | proof verified (τ_π transport via T20; quarter-turn law T19) | PROVED | no — chart-transport machinery | — |
| T26 | midpoint values: F^+(m_k) = √2+ε, F^−(m_k) = √2−ε, ε = (−1)^k | proof verified (m_0 = π/4: cot(π/8) = √2+1 (S); transport via T8/T19; Q1 check: F_s^+(3π/4) = √2−1 = √2+ε with ε = −1) | PROVED | **yes — candidate principle** (possible duplicate of Book 2 P20) | exact trig values |
| T27 | octant ordering on Q0: F_s^+ > F_c^+ on first octant, reversed on second, equality only at m_0 | proof verified by reading (difference strictly decreasing via T24; endpoint limits +∞ vs 1+ ⇒ exactly one zero, located at m_0 by T26; transported by T8) | PROVED | no — monotonicity comparison, not an identity | cf. book-2 P11, not folded |
| T28 | the principal package does not globalize (witness x = 5π/4) | proof verified (recomputed: F_s^+(5π/4) = √2+1 vs chart cot(5π/8) = 1−√2 < 0) | PROVED | no — negative check / computed counterexample | — |
| T29 | opposite-seam regular values are exactly 1 | proof verified by reading (c-channel at x→kπ: |sec x|→1, tan x→0; s-channel symmetric) | PROVED | no — limit evaluation / definitional audit point | note: the absolute value does the work (|sec x|, not sec x — sec(kπ) = ±1) |
| T30 | own-channel seams: directional 0↔+∞ exchange; no finite continuous extension; extension does not commute with inversion | proof verified (re-derived one-sided limits at 0±: F_s^+ → +∞/0, F_s^− → 0/+∞; two-sided disagreement ⇒ no finite extension per limits criterion S) | PROVED | no — limit analysis, not an identity | — |
| T31 | a seam-safe composite never regularizes its singular constituents | proof verified by reading (follows from T30; manuscript page tag P) | PROVED | no — boundary bookkeeping | in-text |
| T32 | split-boundary domain D̂ with directional copies; D̂/∼_g ≅ ℝ; no canonical raw crossing map | proof verified by reading (construction from T7/T30; quotient via universal property S; no-canonical-map from directional asymmetry in T30; manuscript page tag P) | PROVED | no — domain construction + negative claim | in-text |
| T33 | gluing criterion: regular channel glues at 1; singular channel cannot glue finite | proof verified (T29 gives the regular value; T30 the obstruction) | PROVED | no — boundary criterion | — |
| T35 | four minimalities pairwise non-equivalent; "minimal" without a named task is meaningless | proof verified by reading (manuscript page tag P) | PROVED | no — methodological/definitional | in-text |
| T36 | the four-factor curve E_k: Q_k→ℝ⁴ has one-dimensional smooth image | proof verified by reading (from T21 + diffeomorphisms preserve manifold dimension, S; manuscript page tag P) | PROVED | no — differential topology, not trig | in-text |
| T37 | no continuous injective 𝕋→ℝ | proof verified (standard circle topology S: compactness ⇒ homeomorphism onto image; connectedness after point removal) | PROVED | no — topology, no trig content | relative to S |
| T38 | task factorization; lossy can be task-sufficient; more outputs cannot undo prior noninjective compression; no universally minimal representation; axiom-free ≠ assumption-free; mathematical ≠ physical closure | proof verified by reading (manuscript page tag P) | PROVED | no — meta/methodological | in-text |
| T39 | status-grammar theorems 1.I.T1–T4 (nonpromotion, domain inheritance, collision-cleanup neutrality, formal isolation) | proof verified by reading (deductions from declared grammar; manuscript page tag P) | PROVED | no — meta (grammar) | in-text |
| T40 | dependency order is acyclic | proof verified (DAG check: only forward reference is T24→T25; T25 does not cite T24 ⇒ no cycle; otherwise each proof uses only D1–D5, S, earlier theorems) | PROVED | no — meta | one numbering inversion noted |
| T41 | no-smuggling theorem (blocks eight invalid promotions) | proof verified by reading (manuscript page tag P; cases 6–8 rest on ASSERTED rules R1–R5 — disclosed) | PROVED | no — meta (audit rule) | in-text |
| T42 | source-provenance theorem | proof verified by reading (from section closure ledgers; manuscript page tag P) | PROVED | no — meta (provenance) | in-text |
| T43 | constitution theorem (18 established items) | proof verified by reading (manuscript page tag P; from the section closure ledgers) | PROVED | no — meta (collection) | in-text; the "18 established items" count is the manuscript ledger's taxonomy, not independently re-verified here |
| T44 | zero new axioms; zero external imports (ledger audit) | proof verified by reading (manuscript page tag P) | PROVED | no — meta (audit verdict) | "zero external imports" means beyond the declared standard block S and declared stipulations |
| T45 | pre-naming sufficiency / airlock (factors possess all properties before Book 2 naming) | proof verified by reading (follows from T21–T22; manuscript page tag P) | PROVED | no — meta (closure) | in-text |
| T46 | analytic seam ≠ physical discontinuity | proof verified by reading (scope declaration; manuscript page tag P) | PROVED | no — non-scope declaration | in-text |

## ASSERTED claims (5)

| Claim | Restatement | Scope | Folded in? | Notes |
|---|---|---|---|---|
| T34 | uniqueness of continuous extension on dense sets | ASSERTED (imported standard analysis theorem; used as stated, not proved here) | no | the source file labels this PROVED, but by its own description ("imported, not proved here") it is an import — reclassified honestly |
| A1 | the standard import block S: trig periodicity, csc²−cot² = 1, sec²−tan² = 1, half-angle/addition identities, cot(π/8) = √2+1, limit calculus, uniqueness of continuous extension, circle topology, ordinary arithmetic/order reasoning | ASSERTED (declared standard import; used, never derived in the book) | no | every PROVED claim above is conditional on this block |
| A2 | no-smuggling rules R1–R5 (declared stipulations) | ASSERTED (stipulation) | no | T41 cases 6–8 rest on these |
| A3 | Declaration 1.I.D1 (Book 0 corpus freeze) | ASSERTED (declared stipulation) | no | — |
| A4 | the status-grammar categories themselves (P/C/A/I + tags) | ASSERTED (definitions) | no | — |

## CHECKED claims (1)

The book page reports its own completed validation run
(`validation/book1/verify_book1.py`: 111 assertions — reciprocal
conjugacy, half-angle charts, midpoint values √2±1, threshold law, octant
ordering, boundary limits, ε-lossiness — all passing, exit=0, no timeouts;
worst measured error 8.6e-10 on reciprocal conjugacy near seams,
floating-point noise on an exact-algebra identity). Per the
proof-over-sampling rule this was **not re-run here**; it is cited, not
folded as a principle (a numerical check of a proved identity is not a new
theorem).

| Claim | What it checks | Scope | Folded in? |
|---|---|---|---|
| C1 | numerical re-verification run described above | CHECKED | no — checks proved T15–T18, T23–T30 |

## Candidate trigonometric principles (5)

Full statements, domains, proofs, scope, and source claims. None cites
Euclid. All are conditional on the declared standard import S.

**1. Reciprocal conjugacy identity (source B1.T16).**
Statement: for all x ∈ D = ℝ ∖ {kπ/2 : k ∈ ℤ},
(|csc x| + cot x)(|csc x| − cot x) = 1 and
(|sec x| + tan x)(|sec x| − tan x) = 1.
Domain: D, where all four factors are defined and nonzero (strict
positivity, B1.T15).
Proof: (|csc x|+cot x)(|csc x|−cot x) = |csc x|² − cot²x =
csc²x − cot²x = 1 by the standard Pythagorean identity (S); likewise
sec²x − tan²x = 1 (S). Exact algebra; at own-channel seams the product is
assigned no value (domain restriction, not an approximation).
Scope: PROVED (conditional on S; no Euclid).
Note: already registered as Book 0 P1 / Book 2 P1 — dedup pass to decide.

**2. Strict positivity / |csc| > |cot| inequality (source B1.T15).**
Statement: for all x ∈ D, |csc x| > |cot x| and |sec x| > |tan x|; hence
|csc x| ± cot x > 0 and |sec x| ± tan x > 0 everywhere on D.
Domain: D.
Proof: csc²x − cot²x = 1 (S) gives |csc x|² = 1 + cot²x > cot²x =
|cot x|², so |csc x| > |cot x| ≥ 0; then
|csc x| ± cot x ≥ |csc x| − |cot x| > 0. Same argument for sec/tan.
Scope: PROVED (conditional on S; no Euclid).
Note: already registered as Book 0 P2 / Book 2 P2 — dedup pass to decide.

**3. Principal half-angle chart (source B1.T23).**
Statement: on Q0 = (0, π/2), where sgn(sin x) = sgn(cos x) = +1:
|csc x| + cot x = cot(x/2), |csc x| − cot x = tan(x/2),
|sec x| + tan x = tan(π/4 + x/2), |sec x| − tan x = tan(π/4 − x/2).
Domain: Q0 (extends to all Q_k by the two chart types, B1.T25).
Proof: on Q0, |csc x| = 1/sin x, so the s-factors are
(1 ± cos x)/sin x = cot(x/2), tan(x/2) by the standard half-angle
identities (S). For the c-channel, put t = tan(x/2):
(1 + sin x)/cos x = (1 + t² + 2t)/(1 − t²) = (1+t)/(1−t) =
tan(π/4 + x/2), and (1 − sin x)/cos x = (1−t)/(1+t) = tan(π/4 − x/2),
by the standard addition formulas (S).
Scope: PROVED (conditional on S; no Euclid).
Note: already registered as Book 2 P17 — dedup pass to decide.

**4. Octant midpoint exact values (source B1.T26).**
Statement: at the octant midpoints m_k = (2k+1)π/4, with
ε = sgn(sin 2x) = (−1)^k constant on Q_k, the plus-factors equal √2+ε
and the minus-factors equal √2−ε. In particular cot(π/8) = tan(3π/8) =
√2+1 and tan(π/8) = cot(3π/8) = √2−1.
Domain: the points m_k (k ∈ ℤ).
Proof: on Q0, m_0 = π/4: F_s^+(π/4) = (1 + cos π/4)/sin π/4 = √2+1 =
cot(π/8) (S); the other three factors by the chart formulas (B1.T23).
Transport to all Q_k by the seam/quadrant transport (B1.T8) and the
conjugacy laws (B1.T19) yields the √2±ε pattern from the sign cycle
(B1.T10).
Scope: PROVED (conditional on S; no Euclid).
Note: already registered as Book 2 P20 — dedup pass to decide.

**5. Unit-threshold law (source B1.T18).**
Statement: on D, F_s^+ > 1 ⇔ cot x > 0 (and F_s^+ < 1 ⇔ cot x < 0);
F_s^+ = 1 never occurs on D. Channel-swapped: F_c^+ > 1 ⇔ tan x > 0;
sign-swapped: F_s^− > 1 ⇔ cot x < 0, F_c^− > 1 ⇔ tan x < 0.
Domain: D.
Proof: from the rational forms (B1.T11),
F_s^+ − 1 = (α + cos x − sin x)/sin x. Quadrant by quadrant: on Q0,
numerator 1 + cos x − sin x = 1 + √2cos(x+π/4) > 0 on the open interval
(equality only at the excluded seam x = π/2); on Q1,
1 − (|cos x| + sin x) < 0 since (|cos x|+sin x)² = 1 + 2|sin x cos x| >
1 on the open interval; on Q2 and Q3 the analogous estimate with
(cos x + |sin x|)² = 1 ± 2cos x|sin x| gives the sign of the numerator
opposite to sin x exactly when cot x > 0. In all cases
sign(F_s^+ − 1) = sign(cot x), and equality would require
|sin x cos x| = 0, i.e. an excluded seam — so F_s^+ = 1 never occurs on
D. The c-channel and minus-factor versions follow by symmetry and by
F^− = 1/F^+ (B1.T16).
Scope: PROVED (conditional on S; no Euclid).
Note: matches Book 2 P9, which the book-2 audit evaluated as
monotonicity analysis rather than a principle — flag for the dedup pass.

## Claims not made into principles (46)

Grouped by category:

- **Standard-background trig, imported as S rather than proved (not new):**
  the periodicity/injectivity facts inside T2; the parity, shift, and
  cofunction identities underlying T13 and T19; the one-line sign rules at
  the core of T10; π-periodicity T20 (already registered as Book 0 P3(c)).
  Count: effectively the S-dependent cores of T2, T10, T13, T19, T20.
- **Book machinery — chart transport, operators, quotients, redundancy
  (no general trig identity):** T1, T3–T9, T11, T13 (ε-lossiness negative
  result), T17, T19, T21, T24 (ranges/monotonicity), T25 (chart types),
  T27 (octant ordering comparison), T28 (non-globalization witness),
  T31–T33 (boundary/seam bookkeeping). Count: 21.
- **Analysis / limits / topology (not identities):** T14 (smoothness),
  T29–T30 (seam limits), T36 (manifold dimension), T37 (circle topology).
  Count: 5.
- **Definitional / meta / methodological (no trig content):** T4a, T4b, T12,
  T22, T35, T38–T46. Count: 14.
- **ASSERTED, not proved:** T34 (imported extension-uniqueness theorem),
  A1–A4. Count: 5.
- **CHECKED, not a new theorem:** C1 (numerical check of proved T15–T18,
  T23–T30). Count: 1.

## Counts

- Evaluated: **51** (45 PROVED, 1 CHECKED, 5 ASSERTED, 0 INCOMPLETE)
- Candidate trig principles: **5** (T15, T16, T18, T23, T26), all PROVED
  (conditional on the declared standard import S; no Euclid cited)
- Not folded: **46** — 5 asserted, 1 numerical check, 40 evaluated with no
  new trigonometric content (standard background, book machinery,
  analysis/limits, meta)

status: complete
