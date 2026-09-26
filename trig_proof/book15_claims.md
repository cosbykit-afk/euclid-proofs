# Book 15 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book15_proof.md` (claim inventory
1–44 plus firewalls M15-A…M15-H) checked against the rewrite page
`~/workspace/r-theory-rewrite/book15/index.html` (*Book 15 — Saw
Interchanges, Double-Angle Decomposition, Bridge to E8*; the page's CP/SC/
NC/ST/MA tags are the book's own and are cited, not re-derived). Evaluated
2026-09-22.

**Verification method.** All 44 claim proofs read in full and re-derived
independently. The load-bearing algebra was recomputed step by step and
checks out exactly: claim 1 (complement interchange via
cot θ = tan(π/2−θ)); claim 4 (A = 2cot x via common denominator and
double-angle, B = 2tan x via tan P − tan Q and product-to-sum); claim 6
(D₂ = 4/sin 2x, K₂ = 4cot 2x); claim 7 (Z₂ = e^{2ix}); claim 8
(H_R = sin 2x/4, V_R = cos 2x/2, differential ladder); claim 9
(Z₂(Cx) = −conj Z₂); claim 12 (transfer-angle parametrization, incl. the
θ = π − 2θ_λ consistency); claim 13 (Weierstrass sum-of-squares = 1, tanh
double-angle); claim 14 (Bloch off-diagonal match e^{−iφ} = −is_Ω for both
signs; ⟨Y⟩ = 2s_Ω√H_Saw); claim 18 (the [H,ρ] = ih₁(2λ−1)X computation and
the meridian tangent (s_Ω/2)(1−2λ)Y + √H_Saw Z, verified from
[X,Z] = −2iY, [X,Y] = 2iZ); claim 21 (Q_t² = ¼I, Q_t″ = −4Q_t); claim 26
(commuting-involution bigrading, modulo the stated multiplicative
hypothesis); claim 27 (K² = I); claim 32-lemma (−cosθ = 0 ⟺ θ = π/2 + kπ);
claims 34–37 (binomial/exterior dimensions, reciprocal covariance,
parent identity P_δ, cosh minimum at r = 1 value 2). Analysis steps
(domains, nonvanishing on the standing domain x ∈ (0,π/2)) were checked by
reading for domain errors and circularity — none found.

The book page's reported verification suites (`vol3/book15/audit_book15.py`,
`validation/book15/verify_book15.py`, `validation/book15/test_embeds.py`,
the sympy Saw core reduction, the exact 4×4/2×2 bigrading witnesses, and
the E8 computations in `~/workspace/e8/`) are **cited, not re-run**, per
the proof-over-sampling rule. Where a claim rests on them it is labeled
CHECKED with the source named and the non-rerun stated.

Because this audit assigns **exactly one label per claim** (per the task),
the two split verdicts of the source file are placed conservatively:
claim 15 (proved balance half / cited R_Y-mapping half) → CHECKED;
claim 32 (proved stationary-point lemma / asserted conditional theorem) →
ASSERTED. Both splits are documented in the notes; the underlying content
verdicts agree with the source file and with the chapter.

**Scope labels:** PROVED (exact mathematics, complete proof verified here),
CHECKED (completed computation, reported run cited, not re-run),
ASSERTED (manuscript claim/assumption/interpretation/definition-substrate/
status declaration), INCOMPLETE (failed, timed out, or unfinished — none).

**Euclid boundary:** no proposition of the *Elements* is used as a logical
premise of any proof in the source file (analytic trigonometry is declared
ST substrate, consistent with the 13 ledgers). Nothing is cited by title.

## PROVED claims (25)

"Folded in?" uses the chapter's principle names; the chapter body numbers
its nine principles 1–9 while the chapter register table lists rows
1–6, 10, 11, 12 "(Book 15)" — the mapping is given in the notes for
principles 7–9 (see "Chapter discrepancies" below).

| Claim | Restatement | Verdict | Scope | Folded in? | Notes |
|---|---|---|---|---|---|
| 1 | 15.I.T1: srx ↔ cxp, sxp ↔ crx under Cx = π/2 − x; urx/uxp swap | proof verified (re-derived: srx(Cx) = cot(π/4−x/2) = tan(π/4+x/2) = cxp(x); involution for the reverse) | PROVED | yes — Principle 1 (Book 15) | — |
| 2 | 15.I.D1: Ψ_U(Cx) = i·conj(Ψ_U(x)) | proof verified (re-derived: i(urx − i·uxp) = uxp + i·urx) | PROVED | yes — Principle 1 (corollary) | — |
| 3 | 15.I.C1: C is an involution, C(Cx) = x | proof verified (substitution law) | PROVED | yes — Principle 1 (premise) | — |
| 4 | 15.II.T1: A = cot(x/2) − tan(x/2) = 2cot x; B = tan(π/4+x/2) − tan(π/4−x/2) = 2tan x; AB = 4 | proof verified (re-derived both, incl. cos(π/4+x/2)cos(π/4−x/2) = cos x/2) | PROVED | yes — Principle 2 (Book 15) | — |
| 5 | 15.II.T2: D₂² − K₂² = 16; D₂(Cx) = D₂, K₂(Cx) = −K₂ | proof verified (4AB; A(Cx) = B(x), B(Cx) = A(x)) | PROVED | partial — parity half in Principle 5 (Book 15) | hyperbola relation D₂²−K₂² = 16 is algebra from Principle 2, not a new identity |
| 6 | 15.III.T1: D₂ = 4/sin 2x, K₂ = 4cot 2x | proof verified (re-derived; sum is the Seed regrouping line, cited) | PROVED | yes — Principle 3 (Book 15) | cites seed_double_angle.md for the sum regrouping |
| 7 | 15.III.T2: Z₂ = (K₂+4i)/D₂ = e^{2ix} | proof verified (re-derived: sin 2x·(cot 2x + i) = cos 2x + i sin 2x) | PROVED | yes — Principle 4 (Book 15) | — |
| 8 | 15.III.D1: H_R = sin 2x/4, V_R = cos 2x/2; H_R′ = V_R, V_R′ = −4H_R, Z₂′ = 2iZ₂ | proof verified (re-derived all three derivatives) | PROVED | yes — Principle 4 (Book 15) | — |
| 9 | 15.III.C1: H_R even, V_R odd, Z₂(Cx) = −conj Z₂ | proof verified (re-derived: e^{i(π−2x)} = −e^{−2ix}) | PROVED | yes — Principle 5 (Book 15) | — |
| 11 | 15.IV.T1 parities: Ω ↦ Ω⁻¹, ln Ω odd about λ = 1/2, ε even under λ ↔ 1−λ | proof verified given the reduction (exact algebra on saw_up = ελ, saw_down = ε(1−λ)) | PROVED | no — chart-share/logarithm parities, not a trig identity | premise (claim 10) is CHECKED; the parity derivation itself is exact |
| 12 | 15.IV.C1: λ = sin²(θ/2) ⇒ Ω = tan²(θ/2), 2√H_Saw = sin θ, θ = π − 2θ_λ | proof verified (re-derived; sin θ ≥ 0 on (0,π) used legitimately) | PROVED | yes — Principle 6 (Book 15) | — |
| 13 | 15.IV.D1: qSaw² + c_q² = 1; q₂ = 2q/(1+q²) = tanh η₂, η₂ = 2η | proof verified (re-derived: numerator 1+2q²+q⁴ = (1+q²)²; standard tanh double-angle) | PROVED | partial — Weierstrass half in Principle 7 (Book 15) | tanh companion is hyperbolic, not folded; already in the top register as row 2 (Book 15) from Book 16's 16.I.59(a) |
| 14 | 15.V.T1: Saw–Hodge meridian projection ρ = ½[I + (2λ−1)Z + 2s_Ω√H_Saw Y]; sign s_Ω visible in ⟨Y⟩ | proof verified given the lift definition (off-diagonal match checked for both signs; ⟨Y⟩ = 2s_Ω√H_Saw) | PROVED | no — Bloch-state algebra, not a trig identity | "given the quarter-phase lift definition" — exact given the premise |
| 16 | 15.V.T2: sign visibility; joint (ε, s_Ω) recovery from (ρ, Q_C) | proof verified given the manuscript definitions (λ = ρ₀₀, sign(⟨Y⟩) = s_Ω for H_Saw > 0, ε = sign of Q_C's first component) | PROVED | no — definition bookkeeping, no trig content | "given the manuscript definitions" |
| 18 | 15.V.T3: protected-traversal obstruction — no R_Y-even H in the I/Y algebra traverses the meridian | proof verified given the premise (recomputed [H,ρ] and the Y/Z-type tangent) | PROVED | no — operator obstruction, not a trig identity | exact given the R_Y-even premise; negative result retained |
| 20 | 15.VI.T1: order-two Saw complement vs order-four quarter-turn are distinct maps | proof verified (C_J²t = −t ≠ t, C_J⁴ = id) | PROVED | no — order-of-maps group theory | negative result retained |
| 21 | 15.VI.T2 (differential/square part): Q_t² = ¼I; Q_t″ + 4Q_t = 0 | proof verified (re-derived: {Z,X} = 0 used correctly) | PROVED | partial — harmonic part in Principle 8 (Book 15) | Q_t² = ¼I is operator algebra, not folded |
| 24 | 15.VI.C2: one harmonic structure (sin 2x, cos 2x), two routes (Q_t coefficients; H_R/V_R; phasor Z₂) | proof verified (the pair (sin 2x, cos 2x) appears in claims 21, 8, 7 exactly) | PROVED | no — correspondence observation, no new identity | minor presentational slip in the source: "(2H_R, V_R)·(2,1)" should be "(2H_R, V_R)·(2,2)" to yield (sin 2x, cos 2x); the claim itself is exact |
| 26 | 15.VII.T1: commuting involutions give a four-way bigrading with multiplicative parity rules | proof verified given the stated multiplicative hypothesis | PROVED | no — linear-algebra lemma, not trig | caveat: multiplicativity σ(ST) = σ(S)σ(T) is an explicit hypothesis of the lemma, not a consequence of linearity + σ² = id; the manuscript's σ_ext, σ_int are supplied as substrate |
| 27 | 15.VII.C1: K = σ₁σ₂ ⇒ K² = I | proof verified (uses commutativity exactly) | PROVED | no — linear algebra, not trig | — |
| 33 | 15.VII.3: hyperbolic double-angle compatibility v = 2u (from v = −2ln r, u = −ln r) | proof verified (exact log algebra) | PROVED | no — logarithmic, not trig | — |
| 34 | 15.VIII.T1: even-exterior polynomial of a real 4-manifold is Q_M(χ) = 1 + 6χ + χ² | proof verified (binomial dimensions C(4,0), C(4,2), C(4,4)) | PROVED | no — combinatorics, not trig | — |
| 35 | 15.VIII.C1: χ²Q_M(χ⁻¹) = Q_M(χ); Q_M/χ = 2cosh v + 6 for χ = e^{−v} | proof verified (re-derived both) | PROVED | no — hyperbolic identity, deliberately not folded | chapter's documented scope choice; circular measure not involved |
| 36 | 15.VIII.D2: P_0 = Q_M(r²), P_{±1} = (1±r)⁴ | proof verified (binomial expansion) | PROVED | no — binomial identities | tagged "(def)" in the source; the endpoint identities are exact |
| 37 | 15.VIII.T2: parent identity A_δ² + (1−δ²)(1+r²)² = P_δ; unique minimum of (cosh v + 3)/2 at r = 1, value 2 | proof verified (re-derived the expansion and the cosh monotonicity argument) | PROVED | no — hyperbolic/AM-GM, not circular trig | minimum argument uses cosh strictly decreasing/increasing on the two half-lines — correct |

## CHECKED claims (11)

Reported completed computations, cited from the book's suites or
established workspace computations; none re-run here (proof-over-sampling
rule). None is a trigonometric identity, so none is folded in.

| Claim | Restatement | Scope | Folded in? | Notes |
|---|---|---|---|---|
| 10 | 15.IV.T1 core reduction: Saw = (ελ, ε(1−λ)) on the positive bounded chart, by the book's sympy core | CHECKED | no | premise of claim 11; cited from the page's reported provenance (audit + verify_book15.py) |
| 15 | 15.V.C1: balance states ρ = ½(I±Y) at λ = 1/2; R_Y maps ρ(λ) → ρ(1−λ) preserving the sign choice | CHECKED (split: balance identity independently proved here; R_Y-mapping cited from the book's symbolic proof) | no — Bloch-state algebra | single-label rule: cannot be PROVED while the R_Y half is only cited |
| 22 | 15.VI.T2 commutator form: Q_t′ = [J, Q_t] | CHECKED | no | manuscript J-convention; cited from the book's suite, not reconstructed |
| 23 | 15.VI.C1: JQ_tJᵀ = −Q_t | CHECKED | no | cited from the book's suite (manuscript J-convention) |
| 29 | 15.VII.Witness 1: real 4×4 bigrading witness, four 4-dim parity spaces | CHECKED | no | cited: the book's exact finite-dimensional computation |
| 30 | 15.VII.Witness 2: 2×2 bridge polarization, {K,B} = {H,B} = 0, ⟨B,H(θ)⟩ = −sinθ | CHECKED | no | cited: the book's exact symbolic computation |
| 31 | 15.VII.C3: ⟨B_δ,H(θ)⟩ = cos(δ+θ) | CHECKED | no | cited: the book's exact computation (manuscript B_δ convention) |
| 40 | 15.IX.T3: canonical round-trip normalization c = 1 | CHECKED | no | cited: the page's two-line proof via the book's suite |
| 41 | E8 30380 weight table (Freudenthal, exact integer; 9121 weights, total 30380) | CHECKED | no | cited: established SC computation in ~/workspace/e8/ (files present: table_30380_full.csv, summary JSON, freudenthal_30380.py) |
| 42 | 248-adjoint Jacobi/Fierz check (exactly 0.0 over 341,376 triples; 240 roots, E8 Cartan) | CHECKED | no | cited: reported numerical run per the page |
| 43 | 30380-rep generators (Casimir deviation 4.0e-10, Serre 1.7e-14, Cartan diagonals match SC table) | CHECKED | no | cited: reported numerical run per the page |

## ASSERTED claims (8) + firewalls (8)

Manuscript interpretations, imported substrate definitions, conditional
bridges, and status declarations — correctly labeled in the source, not
folded in.

| Claim | Restatement | Scope | Notes |
|---|---|---|---|
| 17 | 15.V.C2: the minus sign as mandatory π/2-phase residue | ASSERTED (interpretive reading) | no independent mathematical content beyond claim 14 |
| 19 | 15.VI.D1–D2: transfer doublet (p,q), p²+q² = 2, and native quarter-turn generator J, J² = −I | ASSERTED (manuscript substrate, NA-15-4) | imported as data |
| 25 | 15.VI.B1: product-duality bridge (conditional) | ASSERTED (explicitly conditional, MA) | nothing derived about it |
| 28 | 15.VII.C2: relative complex-structure orientation on K sectors | ASSERTED (manuscript) | no reconstructible content on the page |
| 32 | 15.VII.CT1: conditional quarter-phase selection θ_* = ±π/2 by sign of s_Ωκ_y | ASSERTED (split: stationary-point lemma independently proved here and folded as Principle 9 (Book 15); the full conditional theorem is conditional on the B-purity contract and the manuscript stationarity equation, not derived) | single-label rule: the theorem as named is conditional, hence ASSERTED |
| 38 | 15.IX.T1: E8(−24) threshold admission | ASSERTED (admission, not derived; MA) | scope declaration |
| 39 | 15.IX.T2: threshold closure meta-summary | ASSERTED (MA) | status accounting |
| 44 | 15.X: Δ_op(Book 15) = ∅ | ASSERTED (status declaration, MA) | negative-results retained (claims 18, 20, M15-F) |

**Firewalls M15-A…M15-H** (all ASSERTED scope contracts, evaluated, not
folded in): M15-A substitution-law boundary (no time/transport/Hamiltonian
from the complement swap); M15-B1 (D₂,K₂) is algebraic state geometry;
M15-B2 Z₂ is a mathematical phase coordinate; M15-C ε factored before
squaring, Saw complement is involutive chart swap; M15-D "Hodge" stays a
conditional bridge; M15-E Saw complement ≠ product duality, native J not
automatically Hodge/E8; M15-F bigrading awaits representation realization;
M15-G the §15.VIII 4-manifold is not a spacetime tangent space;
M15-H constrains Book-16 ordering, no backward strengthening.

## Candidate principles — independent verification

All nine principles from the chapter were restated, their proofs
re-verified, and their domains/scope confirmed:

1. **Complement interchange of the canonical primitives** — CONFIRMED,
   PROVED. x ∈ (0,π/2); srx ↔ cxp, sxp ↔ crx; Ψ_U(Cx) = i·conj(Ψ_U(x)).
   Proof re-derived exactly (substrate complement laws + definitions).
2. **Primitive-difference identities** — CONFIRMED, PROVED. x ∈ (0,π/2);
   cot(x/2) − tan(x/2) = 2cot x, tan(π/4+x/2) − tan(π/4−x/2) = 2tan x.
   Proof re-derived exactly (half/double-angle, tan-difference,
   product-to-sum).
3. **Double-angle difference identity** — CONFIRMED, PROVED. x ∈ (0,π/2);
   D₂ = 4/sin 2x (sum cited from Principle 0, not re-proved), K₂ = 4cot 2x
   re-derived exactly from Principle 2 + substrate.
4. **Double-angle phasor and differential ladder** — CONFIRMED, PROVED.
   x ∈ (0,π/2); Z₂ = e^{2ix}, H_R = sin 2x/4, V_R = cos 2x/2,
   H_R′ = V_R, V_R′ = −4H_R, Z₂′ = 2iZ₂ — all re-derived exactly.
5. **Complement parity of the double-angle pair** — CONFIRMED, PROVED.
   x ∈ (0,π/2); D₂, H_R even; K₂, V_R odd; Z₂(Cx) = −conj(Z₂(x))
   re-derived exactly from Principles 1, 2, 4 + complement laws.
6. **Transfer-angle parametrization** — CONFIRMED, PROVED. θ ∈ (0,π);
   λ = sin²(θ/2) ⇒ Ω = tan²(θ/2), 2√(λ(1−λ)) = sin θ (sin θ ≥ 0 used
   legitimately); θ = π − 2θ_λ consistency exact on the chart.
7. **Rational (Weierstrass) parametrization of the circle** — CONFIRMED,
   PROVED. θ ∈ (0,π), q = tan(θ/2) > 0;
   (2q/(1+q²), (1−q²)/(1+q²)) = (sin θ, cos θ), sum of squares = 1 —
   re-derived exactly (half-angle + Pythagorean).
8. **Harmonic-oscillator relation of the double-angle pair** — CONFIRMED,
   PROVED. All real x; (sin 2x)″ + 4sin 2x = 0, (cos 2x)″ + 4cos 2x = 0 —
   re-derived exactly from substrate differentiation.
9. **Stationary points of the sine** — CONFIRMED, PROVED. Real θ;
   −sinθ stationary ⟺ cosθ = 0 ⟺ θ = π/2 + kπ; on the quarter-phase
   domain, θ = ±π/2. The chapter's generalized statement (π/2 + kπ) is a
   correct strengthening of the source file's domain-restricted ±π/2.

**Missed principles:** none. The chapter's exclusions are all justified:
claim 4's AB = 4 and claim 5's D₂² − K₂² = 16 are algebraic corollaries of
Principle 2, not new identities; claim 24 is a correspondence observation
with no new identity; claims 11, 16, 18, 20, 26, 27, 33, 34, 36 are
proved-but-not-trigonometric (chart parities, Bloch algebra, operator
obstruction, group theory, linear algebra, log algebra, binomial
combinatorics). The hyperbolic items — claim 13's tanh double-angle and
claims 35, 37's cosh identities — are deliberately excluded from this
chapter's circular-trig fold set; the tanh double-angle is already
registered in the top table as row 2 (Book 15) via Book 16's 16.I.59(a),
and the cosh content is subsumed by row 3 (Book 15), the hyperbolic
Pythagorean identity. No genuine trigonometric principle of Book 15 was
left out.

## Chapter discrepancies found

1. **Principle numbering inconsistency (editorial, math unaffected).** The
   chapter body names its principles 1–9; the chapter's own register-table
   preamble says rows "1 (Book 15)" through "9 (Book 15)", but the actual
   table lists rows 1–6, 10, 11, 12 "(Book 15)" (the top-of-document
   register has rows 1–12 "(Book 15)", where rows 1–3 are Book-16-sourced
   and rows 7–9 plain-numbered were already taken). Three different
   numbering statements for the same nine principles. Content, proofs,
   and proved-from chains are unaffected.
2. **Claim 24 presentational slip (minor, math unaffected).** The source
   writes "(2H_R, V_R)·(2, 1) = (sin 2x/2·2, cos 2x)"; the scaling vector
   should be (2, 2), since V_R = cos 2x/2 and V_R·1 = cos 2x/2 ≠ cos 2x.
   The claim itself — one harmonic pair (sin 2x, cos 2x) via the three
   routes (claims 21, 8, 7) — is exact as verified.
3. **Lemma hypothesis caveat (claim 26).** The bigrading lemma's
   multiplicative parity rule σ(ST) = σ(S)σ(T) is an explicit hypothesis
   of the lemma, not a consequence of "commuting linear involutions"
   alone; the proof is exact given the hypothesis, and the manuscript
   supplies the specific σ_ext, σ_int as substrate. The chapter records
   this correctly ("general lemma" + substrate supplied), so this is a
   scope note, not a correction.
4. **Single-label bookkeeping (not a content discrepancy).** The chapter
   reports 25 PROVED / 10 CHECKED / 7 ASSERTED / 0 INCOMPLETE + 2 split
   verdicts (claims 15, 32). Under this audit's exactly-one-label rule,
   claim 15 → CHECKED (balance half proved here, R_Y half only cited) and
   claim 32 → ASSERTED (lemma proved here, conditional theorem not
   derived), giving 25 / 11 / 8 / 0. The underlying content verdicts are
   identical — no claim's substance was upgraded or downgraded.

## Counts

- Evaluated: **44** (25 PROVED, 11 CHECKED, 8 ASSERTED, 0 INCOMPLETE)
  plus 8 firewalls M15-A…M15-H (all ASSERTED scope contracts).
- Content-verdict match with the chapter: exact (25 full-PROVED, 10
  full-CHECKED, 7 ASSERTED, 2 split, 0 INCOMPLETE); the only difference is
  the forced single-label placement of the two splits (15 → CHECKED,
  32 → ASSERTED).
- Folded into the cumulative proof: **9** principles (all PROVED):
  Principles 1–9 (Book 15) = register rows 1–6, 10, 11, 12 "(Book 15)".
- Not folded: **35** — 16 proved-but-not-trigonometric (11, 14, 15-balance,
  16, 18, 20, 21-square-part, 24, 26, 27, 33, 34, 35, 36, 37, 32-lemma is
  folded), 11 cited computations (10, 15-R_Y, 22, 23, 29, 30, 31, 40, 41,
  42, 43), 8 asserted (17, 19, 25, 28, 32-full, 38, 39, 44), 8 firewalls.
- No Euclid proposition is a logical premise of any claim (campaign
  boundary honored).

status: complete
