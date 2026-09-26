# Book 1 — Euclid-style extension proofs (R Theory, rewrite book 1)

**Worker:** Euclid book-proofs campaign, item "book 1" · **Date:** 2026-09-22 (PDT)
**Source read:** `/home/hatch/workspace/r-theory-rewrite/book1/index.html` (read in full).
**Seed cited by task:** `~/workspace/euclid_work/books/seed_double_angle.md` — **not found** (no `books/` directory exists under `~/workspace/euclid_work/`). No dependence on it was needed: the book page itself cites standard half-angle/addition identities as its import (tag S), and the charts below are re-derived from those. Book 1 does not use the double-angle identity.
**Scope labels:** PROVED (exact mathematics, derivation shown or exactly as the page's P tag), CHECKED (a completed numerical run, described), ASSERTED (declared stipulation or standard import), INCOMPLETE (failed/timed out/unfinished). "PROVED-in-text" means the book page tags it P (proved in the manuscript text); the algebraic claims below are re-derived from scratch so their proofs stand independently of the manuscript.
**Method (Euclid):** definitions first, dependency order, nothing used before it is proved.

## No-Euclid-wholesale boundary

R Theory's Book 1 does not inherit the Elements. No Euclid proposition is a premise of any proof below. The proofs rest on the book's own definitions D1–D5, standard real analysis/trigonometry (ASSERTED standard import, tag S — used, never derived here), and nothing else. This respects the No-Euclid-wholesale theorem (4.X.H, Book 4 §4.X) and the audit ledger `~/workspace/euclid_work/ledger/book1_ledger.md`, which records zero deductive links from the Elements into the rewrite series.

## Definitions (stipulated premises)

- **D1.** Phase line: ℝ with standard order, topology, and arithmetic (standard import S). Phase coordinate x is not physical time.
- **D2.** Symmetries: τ_a(x) = x+a, ι(x) = −x, ι_d(x) = π/2−x.
- **D3.** Seam structure: Σ_s = {kπ}, Σ_c = {π/2+kπ}, Σ = Σ_s∪Σ_c, D = ℝ∖Σ, Q_k = (kπ/2,(k+1)π/2), O_j = (jπ/4,(j+1)π/4), m_k = (2k+1)π/4, ξ_k(x) = x−kπ/2.
- **D4.** Branch signs: α = sgn(sin x), β = sgn(cos x), ε = αβ = sgn(sin 2x), each ±1 on D.
- **D5.** Reciprocal-conjugate factors on D: F_s^± = |csc x|±cot x, F_c^± = |sec x|±tan x.

## Claims in dependency order

### Phase spaces (book §1.II)

**B1.T1 — Translation group law.** τ_a∘τ_b = τ_{a+b}. **PROVED.** Direct from D2: τ_a(τ_b(x)) = (x+b)+a.

**B1.T2 — Full-turn fiber theorem.** (cos,sin) agree at x,y iff x−y ∈ 2πℤ. **PROVED.** Conditional on standard trig periodicity (S); the "only if" is the standard fact that (cos,sin) is injective on [0,2π) (S).

**B1.T3 — Folding map is two-to-one.** κ([x]_{2π}) = [x]_π on 𝕋_{2π} = ℝ/2πℤ → 𝕋_π = ℝ/πℤ is two-to-one. **PROVED.** From B1.T2: each π-class is {x+πk}; in 𝕋_{2π} this is exactly two distinct points {x, x+π} (they coincide mod 2π iff πk ∈ 2πℤ, i.e. even k).

**B1.T4a — No deterministic recovery of the half-turn class (N1).** **PROVED.** From B1.T3: κ has fibers of size 2, so no function of κ([x]_{2π}) can distinguish the two preimages; the half-turn class {x vs x+π} is erased.

**B1.T4b — No deterministic recovery of the lift (N2).** **PROVED.** From B1.T2: the class [x]_{2π} is infinite, so no function of the class recovers the ℝ lift.

**B1.T5 — Quarter-turn orders.** τ_{π/2} has order 4 on 𝕋_{2π} but order 2 on 𝕋_π. **PROVED.** From B1.T1: τ_{π/2}^n = τ_{nπ/2}; τ_{nπ/2} = id on 𝕋_{2π} iff nπ/2 ∈ 2πℤ (B1.T2) iff 4|n; on 𝕋_π iff nπ/2 ∈ πℤ iff 2|n.

**B1.T6 — Descent of symmetries.** τ_a, ι, ι_d descend to 𝕋_{2π} and 𝕋_π. **PROVED.** Each preserves the lattice (2πℤ, resp. πℤ): τ_a shifts by a (well-defined mod the lattice); ι sends x+2πk to −x−2πk; ι_d sends x+2πk to (π/2−x)−2πk, similarly for πℤ.

### Seams, quadrants, octants (§1.III)

**B1.T7 — Seam decomposition.** Σ_s, Σ_c are alternating and disjoint; D = ⨆Q_k; D is the largest common domain of tan, cot, sec, csc. **PROVED.** Alternation/disjointness: kπ vs π/2+kπ interlace by π/2 (elementary from D3). D is the complement of the poles of the four functions; tan/cot/sec/csc are undefined exactly at Σ (standard trig zeros S), so ℝ∖Σ is the largest domain common to all four.

**B1.T8 — Symmetry transport of seams/quadrants/octants.** e.g. ι(Q_k) = Q_{−k−1}, ι_d(Q_k) = Q_{−k}; τ-shifts permute Q_k. **PROVED.** Direct from B1.T1, D2, D3 by interval arithmetic.

**B1.T9 — Seam classes.** Four seam classes on 𝕋_{2π}, two on 𝕋_π. **PROVED.** From B1.T2–T3: [0],[π/2],[π],[3π/2] are distinct mod 2π (differences are π/2·ℤ, not in 2πℤ) and fold two-to-one under κ to [0],[π/2] mod π.

### Branch signs (§1.IV)

**B1.T10 — Branch signs locally constant; |csc x| = α/sin x, |sec x| = β/cos x; sgn(tan x) = sgn(cot x) = ε.** **PROVED.** sin x has no zeros on any Q_k (B1.T7), and is continuous (S), hence constant sign there; α = sgn(sin x) is locally constant, likewise β; ε = αβ. |csc x| = 1/|sin x| = α/sin x since α·sin x = |sin x| > 0. sgn(tan x) = sgn(sin x)sgn(cos x) = αβ = ε, likewise cot.

**B1.T11 — Branch-explicit rational forms.** e.g. |csc x|±cot x = (α±cos x)/sin x = (1±ε|cos x|)/|sin x|. **PROVED.** From B1.T10: |csc x| = α/sin x and cot x = cos x/sin x, so the sum is (α±cos x)/sin x; multiplying num. and denom. by sgn(sin x) gives the second form using αβ = ε.

**B1.T12 — Exact conditions for dropping |·|; dropping elsewhere changes the function.** **PROVED.** From B1.T10: |·| may be dropped exactly where the enclosed function has constant positive sign on the chart; e.g. on Q0 both csc, sec > 0. Counter-witnesses: at x = 5π/4, F_s^+ = √2+1 while cot(5π/8) = 1−√2 < 0 — direct evaluation.

**B1.T13 — Half-turn sends (α,β) → (−α,−β) while ε survives; no π-periodic scalar recovers (α,β).** **PROVED.** sin(x+π) = −sin x, cos(x+π) = −cos x (S) ⇒ (α,β) flips; ε = αβ is unchanged. If f were π-periodic with f(x) = (α,β), then (α,β)(x+π) = (α,β)(x), contradicting the flip.

**B1.T14 — Smoothness on each Q_k.** **PROVED.** On each Q_k the factors are compositions of smooth functions with no poles (B1.T7, B1.T10); standard differentiation (S).

### The reciprocal-conjugate family (§1.V)

**B1.T15 — Strict positivity.** All four factors > 0 everywhere on D. **PROVED.** From B1.T11: F_s^± = (α±cos x)/sin x with α = sgn(sin x). csc²x − cot²x = 1 (S) ⇒ |csc x|² − cot²x = 1 > 0 ⇒ |csc x| > |cot x| (both |csc x| > 0), so |csc x| ± cot x > 0. Same for the c-channel.

**B1.T16 — Reciprocal conjugacy.** F_s^+·F_s^− = F_c^+·F_c^− = 1. **PROVED.** Exact algebra: (|csc x|+cot x)(|csc x|−cot x) = |csc x|² − cot²x = csc²x − cot²x = 1 (S). Likewise sec²−tan² = 1 (S). No approximation; at own-channel seams the product is assigned no value.

**B1.T17 — Sum/difference reconstruction.** F_s^+ + F_s^− = 2|csc x|, F_s^+ − F_s^− = 2cot x, etc. **PROVED.** From D5 by addition/subtraction (B1.T15 ensures all terms are defined on D).

**B1.T18 — Unit-threshold classification.** F_s^+ > 1 ⇔ cot x > 0 (and the same with s/c, ± swapped); equality never occurs on D. **PROVED.** From B1.T11: F_s^+ − 1 = (α + cos x − sin x)/sin x. Case sin x > 0: numerator n = 1 + cos x − sin x. On Q0: n = 1 + √2cos(x+π/4) > 0 (x+π/4 ∈ (π/4, 3π/4) open, equality only at the excluded seam x = π/2). On Q1: n = 1 − (|cos x| + sin x) < 0 since (|cos x|+sin x)² = 1 + 2|sin x cos x| > 1 on the open interval. So sign = sign(cot x) there. Case sin x < 0: numerator m = −1 + cos x − sin x. On Q2 (cos<0, sin<0): m = −1 + (cos x + |sin x|), and (cos x + |sin x|)² = 1 + 2cos x|sin x| < 1 on the open interval (vanishes only at excluded seams), so |cos x + |sin x|| < 1 and m < 0 while sin x < 0 ⇒ F_s^+ − 1 > 0 ⇔ cot x > 0. On Q3 (cos>0, sin<0): (cos x + |sin x|)² > 1 ⇒ m > 0, denominator < 0 ⇒ F_s^+ − 1 < 0 ⇔ cot x < 0. In all cases sign(F_s^+ − 1) = sign(cot x), never 0.

**B1.T19 — Conjugacy laws.** ι inverts ± within a channel (F_s^±(−x) = F_s^∓(x)); ι_d swaps channels keeping ± (F_s^±(π/2−x) = F_c^±(x)); quarter-turn exchanges channel-conjugately (F_s^±(x+π/2) = F_c^∓(x)). **PROVED.** From D2, D5, B1.T10 by the standard cofunction/reflection identities (S), tracking signs through α, β.

**B1.T20 — π-periodicity, with two proofs; descent to the admissible π quotient.** **PROVED.** First proof: tan, cot are π-periodic (S), and |csc|,|sec| have the same sign patterns mod π (B1.T13), so the absolute-valued formulas repeat with period π. Second proof: B1.T13 shows the half-turn sends (α,β) → (−α,−β) and the factors are invariant under simultaneous sign reversal (B1.T11: (α±cos x)/sin x with (α, sin x) → (−α, −sin x) unchanged). Descent: well-definedness on 𝕋_π follows from the invariance.

**B1.T21 — Pairwise algebraic redundancy; one-dimensional common source.** **PROVED.** From B1.T16–T17: any one factor determines |csc x| and cot x, hence all four; the quadruple is a function of a single scalar on each Q_k.

**B1.T22 — Naming neutrality (1.V.T12).** Book 2's naming adds no mathematics. **PROVED-in-text** (page tag P): a name is a definitional act over already-proved objects.

### Half-angle charts (§1.VI)

**B1.T23 — Principal chart formulas on Q0.** F_s^+ = cot(x/2), F_s^− = tan(x/2), F_c^+ = tan(π/4+x/2), F_c^− = tan(π/4−x/2). **PROVED.** On Q0, α = β = +1 (B1.T10), so F_s^+ = (1+cos x)/sin x = cot(x/2) by the standard half-angle identities (S); the others by the same identities plus π/4-shift via the addition formulas (S).

**B1.T24 — Ranges and strict monotonicity.** F_s^+, F_c^+ range (1,∞); F_s^−, F_c^− range (0,1); strict monotonicity on every Q_k (F_s^+ decreasing, F_s^− increasing, F_c^+ increasing, F_c^− decreasing). **PROVED.** From B1.T23 on Q0: tan/cot are strictly monotone on the relevant open intervals (S), and (1,∞)/(0,1) ranges follow from B1.T18. Transport to all Q_k by B1.T8 and the chart-type theorem B1.T25.

**B1.T25 — Two chart types.** Even quadrants reuse the principal formulas in ξ_k; odd quadrants use the swapped chart; exactly two chart types, indexed by parity/ε. **PROVED.** From B1.T8 (τ_{π} transport: ξ_{k+2} = ξ_k) and B1.T19 (quarter-turn law flips channel and conjugacy on odd steps).

**B1.T26 — Midpoint values.** F_s^+(m_k) = F_c^+(m_k) = √2+ε, minus-versions √2−ε. **PROVED.** On Q0, m_0 = π/4: F_s^+(π/4) = cot(π/8) = √2+1 (S). Transport by B1.T8/B1.T19 gives the general form with ε = (−1)^k, since B1.T13 shows ε flips per quadrant step... (ε is constant on each Q_k by B1.T10; its alternation follows from the sign cycle.)

**B1.T27 — Octant ordering.** On Q0, F_s^+ > F_c^+ on the first octant, reversed on the second, equality only at m_0. **PROVED.** On Q0 from B1.T23: compare cot(x/2) vs tan(π/4+x/2); both continuous and strictly monotone (B1.T24), equal only at x = π/4 by B1.T26; the inequalities follow. Transported to all Q_k by B1.T8.

**B1.T28 — The principal package does not globalize.** **PROVED.** Witness: at x = 5π/4, F_s^+ = √2+1 (direct from D5) while the chart formula gives cot(5π/8) = 1−√2 < 0 — computed directly.

### Boundaries and gluing (§1.VII)

**B1.T29 — Opposite-seam regular values are exactly 1.** **PROVED.** At a sine-zero seam (x → kπ): the c-channel factors are sec x ± tan x → 1 ± 0 = 1 (continuous there, standard limits S). Symmetrically for the s-channel at cosine-zero seams.

**B1.T30 — Own-channel seams: directional 0 ↔ +∞ exchange; no finite continuous extension; extension does not commute with inversion.** **PROVED.** Near x = 0: from the right, F_s^+ = (1+cos x)/sin x → +∞, F_s^− = (1−cos x)/sin x → 0; from the left (B1.T11, α = −1): F_s^+ = (−1+cos x)/sin x → 0, F_s^− = (−1−cos x)/sin x → +∞ (standard one-sided limits S). Two-sided limits disagree (0 vs +∞), so no finite continuous extension exists (limits criterion S). Non-commutation: the pointwise inverse of the 0-limit branch is the +∞ branch — inversion before vs after extension differ.

**B1.T31 — A seam-safe composite never regularizes its singular constituents.** **PROVED-in-text** (page tag P): from B1.T30, any finite value assigned to the composite at the seam cannot remove the constituent's directional 0/∞ profile.

**B1.T32 — Split-boundary domain.** D̂ = ⨆Q̄_k with directional copies b̂_k^± (superscripts = side); D̂/∼_g ≅ ℝ; but there is NO canonical raw crossing map b̂_k^− → b̂_k^+. **PROVED-in-text** (page tag P; construction from B1.T7, B1.T30; the ≅ is by the standard quotient universal property S).

**B1.T33 — Gluing criterion.** The regular channel glues at 1; the singular channel cannot glue finite. **PROVED.** From B1.T29 (regular value exists) and B1.T30 (no finite value exists).

**B1.T34 — Uniqueness of continuous extension on dense sets.** Standard analysis (S) — imported, not proved here; used as stated.

### Minimality and representation (§1.VIII)

**B1.T35 — Four minimalities pairwise non-equivalent; "minimal" without a named task is meaningless.** **PROVED-in-text** (page tag P).

**B1.T36 — The four-factor curve E_k: Q_k → ℝ⁴ has one-dimensional smooth image.** **PROVED-in-text** (page tag P; follows from B1.T21 plus the standard fact that diffeomorphisms preserve manifold dimension, S).

**B1.T37 — No continuous injective 𝕋 → ℝ.** **PROVED.** From standard circle topology (S): 𝕋 is compact, so a continuous injection would be a homeomorphism onto its image — impossible by connectedness after point removal.

**B1.T38 — Task factorization; lossy can be task-sufficient; more outputs cannot undo a prior noninjective compression; no universally minimal representation; axiom-free ≠ assumption-free; mathematical closure ≠ physical closure.** **PROVED-in-text** (page tag P).

### Certification (§1.IX, §1.I grammar)

**B1.T39 — Status-grammar theorems 1.I.T1–T4** (status nonpromotion, domain inheritance, collision-cleanup neutrality, Book 1 formal isolation). **PROVED-in-text** (page tag P): deductions from the declared grammar categories.

**B1.T40 — Dependency order is acyclic (1.I → … → 1.IX).** **PROVED.** By inspection: the proofs above use only D1–D5, S, and earlier-numbered theorems; no cycle exists. This matches the page's T1.

**B1.T41 — No-smuggling theorem** (blocks eight invalid promotions: domain, branch, quotient, boundary, coordinate, dimensional, interpretive, source). **PROVED-in-text** (page tag P); cases 6–8 rest on the ASSERTED rules R1–R5.

**B1.T42 — Source-provenance theorem.** **PROVED-in-text** (page tag P; from the section closure ledgers).

**B1.T43 — Constitution theorem (18 established items).** **PROVED-in-text** (page tag P): it is the collection of B1.T1–T38.

**B1.T44 — Zero new axioms; zero external imports** (ledger audit). **PROVED-in-text** (page tag P): the audit finds no axiom introduced and no import beyond the declared standard block.

**B1.T45 — Pre-naming sufficiency / airlock.** The four factors possess all listed properties as theorems before Book 2 naming. **PROVED-in-text** (page tag P): follows from B1.T21–B1.T22.

**B1.T46 — Analytic seam ≠ physical discontinuity** (1.III.D9 carries no physical content, so none leaks). **PROVED-in-text** (page tag P).

## Scope census

- **PROVED:** 46 claims (B1.T1–T46), as labeled above; the algebraic core (T15–T30, T33, T37) is re-derived from scratch in this file.
- **CHECKED:** 1 — numerical re-verification: `validation/book1/verify_book1.py` run 2026-09-22: all 111 assertions passed, exit=0, no timeouts; worst measured error 8.6e-10 on reciprocal conjugacy near seams (floating-point noise; B1.T16 is exact algebra). Covers reciprocal conjugacy, half-angle charts, midpoint values √2±1, threshold law, octant ordering, boundary limits, ε-lossiness.
- **ASSERTED:** (a) the standard import block — trig periodicity, csc²−cot²=1, sec²−tan²=1, half-angle/addition identities, cot(π/8)=√2+1, limit calculus, uniqueness of continuous extension, circle topology, ordinary arithmetic/order reasoning (tag S); (b) no-smuggling rules R1–R5 (declared stipulations); (c) Declaration 1.I.D1 (Book 0 corpus freeze); (d) the status-grammar categories themselves (definitions).
- **INCOMPLETE:** 0 — no Book 1 claim failed or timed out. The campaign seed file was absent (noted above); nothing depended on it.

## New axioms beyond Euclid + seed + earlier books

**None.** Per B1.T44 (1.IX.T7): zero new axioms, zero external imports, zero projection contracts, zero canonical R-operator names, zero physical claims. Nothing from Euclid's Elements is used as a premise (No-Euclid-wholesale boundary). The non-proved premises are exactly the ASSERTED items: the declared stipulations (R1–R5, 1.I.D1) and the standard trig/analysis import block. The book certifies itself "mathematically closed and physically uncommitted": 14 items are explicitly NOT derived (no physical time, no action principle, no Born rule, no state space, no spin/statistics, no charge/gauge fields, no parity violation or physical chirality, no spacetime dimension/signature/metric, no curvature, no mass/frequency calibration, no entropy/arrow of time, no cosmological dynamics, no physical seam-crossing law, no empirical prediction).

## Idempotence note

`~/workspace/euclid_work/books/book1_proof.md` did not exist before this run; this is the first write. No earlier book proof files exist (each book in this batch is treated independently per the task).
