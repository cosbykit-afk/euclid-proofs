# Cumulative Trigonometric Proof — R Theory as an extension of Euclid

A single proof document grown book by book in strict dependency order.
Method: Euclid (definitions first, nothing used before it is proved),
Ptolemy (compute, don't assume — earn every number), Polya (understand,
plan, carry out, look back).

## Scope labels (standing)

- **PROVED** — exact mathematics: a complete analytic argument from stated
  definitions and earlier established principles.
- **CHECKED** — a completed numeric run measuring a claim that has no
  complete analytic proof yet. Never presented as a theorem.
- **ASSERTED** — a manuscript claim or an assumption. Named, never used as
  if proved.
- **INCOMPLETE** — failed, timed out, or unfinished. Reported plainly with
  the timeout or error stated.

No expectation, manuscript label, or incomplete computation is presented
as an established result. A complete analytic proof is never re-established
by numerical sampling afterward; computation is reserved for CHECKED-status
claims with no proof yet.

---

## Seed: Principle 0 (PROVED)

**Kit's double-angle secant-cosecant identity** (Kit Cosby, shared 2026-09-21).

### Statement

For all real x with sin(x) ≠ 0 and cos(x) ≠ 0
(the condition sin(2x) ≠ 0 is redundant — it is equivalent to the conjunction):

    4/sin(2x) = (tan(x) + |sec(x)| − 1/(cot(x) + |csc(x)|))
              + (cot(x) + |csc(x)| − 1/(tan(x) + |sec(x)|))

### Proof (definitions first)

Definitions: for real x with cos(x) ≠ 0 and sin(x) ≠ 0,
tan(x) = sin(x)/cos(x), sec(x) = 1/cos(x), cot(x) = cos(x)/sin(x),
csc(x) = 1/sin(x), and |·| is the ordinary real absolute value.

Set A = tan(x) + |sec(x)| and B = cot(x) + |csc(x)|.

Positivity: |sec(x)| − |tan(x)| = (1 − |sin(x)|)/|cos(x)| > 0, because
cos(x) ≠ 0 implies |sin(x)| < 1. Hence A ≥ |sec(x)| − |tan(x)| > 0.
Likewise B ≥ |csc(x)| − |cot(x)| = (1 − |cos(x)|)/|sin(x)| > 0.
So A, B are strictly positive, and 1/A, 1/B are defined.

Lemma 1 (PROVED): A − 1/A = 2·tan(x).
A² = tan²(x) + 2·tan(x)·|sec(x)| + |sec(x)|². Since |sec(x)|² = sec²(x)
= 1 + tan²(x),
  A² − 1 = 2·tan²(x) + 2·tan(x)·|sec(x)| = 2·tan(x)·A.
Divide by A > 0: A − 1/A = 2·tan(x). ∎

Lemma 2 (PROVED): B − 1/B = 2·cot(x). Same argument with cot/csc. ∎

Regroup the right-hand side (addition commutes):
  (A − 1/B) + (B − 1/A) = (A − 1/A) + (B − 1/B)
                        = 2·tan(x) + 2·cot(x)      (Lemmas 1, 2)
                        = 2·(sin(x)/cos(x) + cos(x)/sin(x))
                        = 2/(sin(x)·cos(x))
                        = 4/sin(2x). ∎

Domain remark: sin(2x) = 2·sin(x)·cos(x), so
sin(2x) ≠ 0 ⟺ sin(x) ≠ 0 ∧ cos(x) ≠ 0. No separate condition is needed.
No quadrant case split is needed either: the absolute values are absorbed
by |sec(x)|² = sec²(x).

Status: **PROVED** (analytic, complete).

---

## Principles register

| Principle id | Statement | Proved-from | Scope |
|---|---|---|---|
| 0 | Kit's double-angle secant-cosecant identity, 4/sin(2x) = (tan x + \|sec x\| − 1/(cot x + \|csc x\|)) + (cot x + \|csc x\| − 1/(tan x + \|sec x\|)), for sin x ≠ 0, cos x ≠ 0 | definitions + Lemmas 1, 2 (seed file) | PROVED |
| 1 (Book 15) | Double-angle bridge identity: for J² = −I, exp(2xJ) = cos(2x)I + sin(2x)J, all real x | definitions (exp/sin/cos series); source claim 16.I.49 | PROVED |
| 2 (Book 15) | Hyperbolic double-angle: tanh(2w) = 2·tanh(w)/(1 + tanh²(w)), all real w | definitions (D1 exponentials); source claim 16.I.59(a) | PROVED |
| 3 (Book 15) | Hyperbolic Pythagorean identity: cosh²(ζ) − sinh²(ζ) = 1; hence Σ² − Δ² = μ² for Σ = μ·cosh(ζ), Δ = μ·sinh(ζ), μ > 0 | definitions (D1–D2); source claim 16.I.59(a) | PROVED |
| 4 (Book 15) | Complementary interchange of the canonical primitives: srx ↔ cxp, sxp ↔ crx under Cx = π/2 − x; corollary Ψ_U(Cx) = i·conj(Ψ_U(x)) | trig substrate (complement laws) + definitions | PROVED |
| 5 (Book 15) | Primitive-difference identities: cot(x/2) − tan(x/2) = 2cot x, tan(π/4+x/2) − tan(π/4−x/2) = 2tan x | trig substrate (half/double-angle, tan-difference, product-to-sum) | PROVED |
| 6 (Book 15) | Double-angle difference: 2cot x − 2tan x = 4cot 2x (sum D₂ = 4/sin 2x cited from Principle 0) | Principles 0, 2 + substrate | PROVED |
| 7 (Book 15) | Double-angle phasor Z₂ = e^{2ix}, H_R = sin 2x/4, V_R = cos 2x/2; H_R′ = V_R, V_R′ = −4H_R, Z₂′ = 2iZ₂ | Principle 3 + substrate (complex exp, differentiation) | PROVED |
| 8 (Book 15) | Complement parity: D₂, H_R even; K₂, V_R odd; Z₂(Cx) = −conj(Z₂(x)) | Principles 1, 2, 4 + substrate | PROVED |
| 9 (Book 15) | Transfer-angle parametrization: λ = sin²(θ/2) ⇒ Ω = tan²(θ/2), 2√(λ(1−λ)) = sin θ | trig substrate (half-angle) | PROVED |
| 10 (Book 15) | Weierstrass parametrization: (2q/(1+q²), (1−q²)/(1+q²)) = (sin θ, cos θ) for q = tan(θ/2) | trig substrate (half-angle, Pythagorean) | PROVED |
| 11 (Book 15) | (sin 2x)″ + 4sin 2x = 0, (cos 2x)″ + 4cos 2x = 0 | trig substrate (derivatives of sin/cos) | PROVED |
| 12 (Book 15) | Stationary points of θ ↦ −sinθ are θ = π/2 + kπ | trig substrate (derivative, zeros of cos) | PROVED |
| 1 (Book 11) | Helicity reciprocal identity (Book 11, T11): for β ∈ (−1,1), β = tanh η, χ with sin χ = β: √((1+β)/(1−β)) = e^η and cxp(χ)·crx(χ) = e^η·e^{−η} = 1 | definitions (exp series, tanh, √, sin) + additive-law lemma + binomial theorem + Cauchy product (Book 11 chapter) | PROVED |
| 1 (Book 10) | Half-angle inversion: r = tan(x/2) ⟺ x = 2·arctan(r), x ∈ (0,π), r ∈ (0,∞) | arctan defined as the inverse of tan on (−π/2,π/2) | PROVED |
| 2 (Book 10) | Hyperbolic half-angle: tanh(α/2) = sinh α/(cosh α + 1), α ∈ ℝ | exact algebra from exponential definitions | PROVED |
| 3 (Book 10) | Prüfer polar form: (F,G) ≠ (0,0) ⟹ (F,G) = A(cos Θ, sin Θ), A = √(F²+G²); tan Θ = G/F where F ≠ 0; Θ defined through nodes | definitions + Euclid 1.47 (book1_ledger.md) | PROVED |
| 4 (Book 10) | Mass-shell ratio chain: pc/(E+mc²) = √((E−mc²)/(E+mc²)) = tanh(α/2) on E = mc²cosh α, pc = mc²sinh α | exact algebra from P2 + ASSERTED import I1 (10.III.P1) | PROVED-conditional (premise ASSERTED) |
| 1 (Book 0) | Folded Pythagorean identities: srx·sxp = 1 and cxp·crx = 1 on D = ℝ \ {kπ/2} | M0 Pythagorean identity (csc² − cot² = 1, sec² − tan² = 1) | PROVED |
| 2 (Book 0) | Positivity: srx, sxp, cxp, crx > 0 on D | P0 (seed positivity argument) + P1 | PROVED |
| 3 (Book 0) | Reflection laws srx(−x) = sxp(x), cxp(−x) = crx(x); quarter-turn laws srx(x−π/2) = crx(x), cxp(x−π/2) = sxp(x); π-periodicity of all four primitives | M0 parity, shift formulas, and periodicity | PROVED |
| 4 (Book 0) | Local generator: with z = srx and ε = sgn(z−1), sxp = 1/z, cxp = (z+ε)/(εz−1), crx = (εz−1)/(z+ε) | P0, P1, P2 | PROVED |
| 5 (Book 0) | Riccati generator law: z′ = −(1+z²)/2 on each open quadrant; ℝ(z) closed under d/dx | M0 differentiation + P2 | PROVED |
| 6 (Book 0) | FlatWave identity: 1/urx + 1/uxp = sgn(sin 2x) on D | P0, P1 | PROVED |
| 7 (Book 0) | FlatWave transformation laws: FW(x+π/2) = −FW(x), FW(x+π) = FW(x), FW(x+2π) = FW(x) | P6 + M0 | PROVED |
| 8 (Book 0) | Common-sign law: urx·uxp = 4/\|sin 2x\| > 0; sgn(urx) = sgn(uxp) = sgn(sin 2x) | P0, P6 | PROVED |
| 9 (Book 0) | Harmonic carrier: H = 1/(urx+uxp) = sin(2x)/4, V = H′ = cos(2x)/2, V² + 4H² = 1/4 | P0 + M0 | PROVED |
| 10 (Book 0) | Transfer-circle identity: p² + q² = 2, with p = αcos x − βsin x, q = \|sin x\| + \|cos x\| (α = sgn(sin x), β = sgn(cos x)) | M0 (sin² + cos² = 1) | PROVED |
| 11 (Book 0) | Differential transfer closure: λ = (1−p)/2 satisfies λ′ = q/2, λ″ + λ = 1/2, (1−2λ)² + 4(λ′)² = 2 | P10 + M0 | PROVED |
| 12 (Book 0) | Sharp phase-rate bounds: 1/2 < λ′ ≤ 1/√2, upper bound exactly at λ = 1/2 where Ω = χ = 1 | P11 + M0 | PROVED |
| 13 (Book 0) | Equal-and-opposite saw derivatives: saw_r′ + saw_x′ = 0 quadrant-locally (saw_r = 1/urx, saw_x = 1/uxp) | P6 | PROVED |
| 14 (Book 0) | Cross-layer ratio: Ω = λ/(1−λ) = saw_r/saw_x = uxp/urx = cxp/srx | P1, P6, P8 | PROVED |
| 15 (Book 0) | Reciprocal-even normalization: 1/(srx+sxp+cxp+crx) = \|sin 2x\|/(4(\|sin x\|+\|cos x\|)); normalized primitives form a positive partition of unity | P1, P2 + M0 | PROVED |
| 16 (Book 0) | Log representation: cxp = e^{asinh(tan x)}, srx = e^{asinh(cot x)} on D | M0 (e^{asinh t} = t + √(1+t²)) | PROVED |

Note on Euclid citations: no proposition of Euclid's *Elements* is a logical
premise of any principle registered so far. The proofs above are analytic,
founded on the Seed (P0), ordinary trigonometry, real analysis, and linear
algebra — matching the audited boundary recorded in Book 0's proof file
("no proposition of Euclid's *Elements* is a premise of any proof"). Euclid
enters this campaign as the framing of definition-first dependency order,
and genuine *Elements* citations will appear when a folded claim actually
uses one. Nothing below is asserted by title or inheritance: each principle
cites only earlier-established principles, in dependency order.

**Update 2026-09-22 (Book 4 chapter):** Principles 26 and 27 (Book 4) use
*Elements* propositions as logical premises — 4.15, 1.5, 1.12, 1.26, 1.32,
1.47, each verified in the 13 ledgers before citing. Nothing is asserted by
title: every citation above was read in its ledger.
| 1 | Operator Euler formula: exp(χJ) = cos χ · id + sin χ · J for any real operator J with J² = −id (Book 6, C6) | power-series definitions of exp, sin, cos (analytic, not Elements) | PROVED |
| 2 | CHI-orbit double-angle identities: cos²χ + sin²χ = 1, cos²χ − sin²χ = cos 2χ, 2√(w_U w_U♯) = \|sin 2χ\|; orbit norm preserved (Book 6, C7) | trig addition/double-angle formulas + Principle 1 | PROVED |
| 17 | Half-angle chart forms: |csc x|+cot x = cot(x/2), |csc x|−cot x = tan(x/2) on (0,π); |sec x|±tan x = tan(π/4±x/2) on (0,π/2) (Book 2, P6) | M0 (half-angle identities) | PROVED |
| 18 | Stereographic parametrization: sin x = σ·2z/(z²+1), cos x = σ·(z²−1)/(z²+1), z = cot(θ/2) > 0, σ = sgn(sin x) (Book 2, P12) | P17 + Book 0 P1 | PROVED |
| 19 | Rational double-angle: sin 2x = 4z(z²−1)/(z²+1)²; sgn(sin 2x) = sgn(z²−1) (Book 2, P13) | P18 | PROVED |
| 20 | Exact octant values: tan(π/8) = √2−1, cot(π/8) = √2+1 (Book 2, P10/P45) | M0 (exact value + algebra) | PROVED |
| 21 | Harmonic oscillator law: H″ + 4H = 0 for H = sin 2x/4 (Book 2, P52) | Book 0 P9 + M0 | PROVED |
| 22 | Rational cot double-angle forms: sin 2x = 2cot x/(1+cot²x), cos 2x = (cot²x−1)/(cot²x+1) (Book 2, P57) | M0 | PROVED |
| 23 | Logarithmic antiderivatives: ∫cot(x/2)dx = 2ln(sin(x/2))+C; ∫tan(x/2)dx = −2ln(cos(x/2))+C (Book 2, P61) | Book 0 P5 + P17 + M0 | PROVED |
| 24 | Arctan linearization: arctan(cot(x/2)) = (π−x)/2 on (0,π); cosine-channel analogs (Book 2, P60) | Book 0 P5 + P17 + M0 | PROVED |
| 26 (Book 4) | Exact trig values at 30° and 60°: sin 30° = cos 60° = 1/2; cos 30° = sin 60° = √3/2; tan 60° = √3; tan 30° = 1/√3 (Book 4: E1, L1, P0, DC) | Euclid 4.15 + 1.5, 1.12, 1.26, 1.32, 1.47 (all verified in the ledgers) + D-T4.1, D-T4.2 | PROVED |
| 27 (Book 4) | Oblique-axis isometry / cosine law at 60°: u² + uv + v² = (u + v/2)² + (√3v/2)²; cross term uv = 2uv·cos 60° (Book 4: ISO) | Principle 26 (Book 4) + Euclid 1.47 (exact algebra) | PROVED |
| 17 (Book 9) | Reciprocal-defect identity: (1−q)/(1+q) = (1−sin χ)/cos χ with q = \|csc χ\| − cot χ = (1−cos χ)/sin χ, on sin χ > 0, cos χ > 0 (Book 9, B9.3c) | ordinary trigonometry (D0) + Pythagorean identity (register row "1 (Book 0)" proved-from basis) | PROVED |

| 17 | tanh(λ/2) = (r − 1)/(r + 1) = (e^λ − 1)/(e^λ + 1), r = e^λ > 0; inverse r = (1 + q)/(1 − q) | Principle 2 + definitions | PROVED |
| 18 | cosh λ = (1 + q²)/(1 − q²), sinh λ = 2q/(1 − q²), q = tanh(λ/2) | Principle 17 + definitions | PROVED |
| 19 | tanh η = 2t/(1 + t²), sech η = (1 − t²)/(1 + t²), tanh²η + sech²η = 1, t = tanh(η/2) | Principle 18 + definitions | PROVED |
| 20 | cosh(iθ) = cos θ = (1 − u²)/(1 + u²), u = tan(θ/2) | Principle 1 (half-angle inversion) + definitions | PROVED |
| 21 | conditional: given s/(2m₁m₂) = cosh λ_m + cosh η (ST), s/(4m₁m₂) = (1 − q_m²q_v²)/((1 − q_m²)(1 − q_v²)) | Principle 18 + ST premise (14.II.P1) | PROVED-conditional (premise ASSERTED) |
| 22 | M²/(4m₁m₂) = (1 + q_m²u²)/((1 − q_m²)(1 + u²)), the q_v² → −u² substitution in Principle 21 | Principles 21, 20 | PROVED |
| 23 | (1 + q_m²u²)/(1 + u²) = (1 + q_m²)/2 + (1 − q_m²)cos(2α)/2, u = tan α; d/dα = −(1 − q_m²)sin(2α) | Principle 20 + definitions + M0 differentiation | PROVED |
| 24 | cos(2θ_m) = q_m = tanh(λ_m/2), sin(2θ_m) = √(1 − q_m²) = sech(λ_m/2) | Principle 17 + definitions | PROVED |
| 25 | ⟨Φ_u\|J_z\|Φ_u⟩ = cos(2α), ⟨Φ_u\|J_x\|Φ_u⟩ = sin(2α), Φ_u = (cos²α, √2 sinα cosα, sin²α)^T | definitions (J_z, J_x, Φ_u) | PROVED |
| 26 (Book 12) | Transfer-coordinate quadratic identity: λ(1−λ) = sin(2x)/4 for λ = (1+sin x−cos x)/2, all real x (Book 12, P4) | definitions + Pythagorean identity + double-angle (P0 substrate) | PROVED |
| 27 (Book 12) | Reciprocal-spine identity: 1/(srx − crx) = (1+sin x−cos x)/2 on the principal branch (0,π/2), with srx = (1+cos x)/sin x, crx = cos x/(1+sin x) (Book 12, P6) | definitions + Pythagorean identity | PROVED |
| 28 (Book 12) | Native-state exact values: λ = 3/5 on the principal branch has the unique solution (sin x, cos x) = (4/5, 3/5); hence (srx, sxp, cxp, crx) = (2, 1/2, 3, 1/3), Ω = 3/2, H = 6/25 (Book 12, P8) | definitions + Pythagorean identity | PROVED |
| 26 (Book 13) | Transfer-coordinate chart lemma: λ(x) = (1+sin x−cos x)/2 is a strictly increasing bijection (0,π/2) → (0,1); λ(0) = 0, λ(π/4) = 1/2, λ(π/2) = 1 (Book 13, P1) | Book 0 P12 (λ′ > 1/2) + M0 (special values, quadrant signs, continuity) | PROVED |
| 27 (Book 13) | Cofunction symmetry of the transfer coordinate: λ(π/2−x) = 1−λ(x) for all real x (Book 13, P4) | M0 cofunction/shift formulas | PROVED |
| 28 (Book 3) | Quarter-turn shift: sin(x+π/2) = cos x; cos(x+π/2) = −sin x (and the −π/2 forms up to sign) (Book 3, C3) | M0 (addition formulas) | PROVED |
| 29 (Book 3) | Directed quarter-turn τ_{π/2} has exact order 4 on 𝕋₂π; τ_{π/2}² = τ_π ≠ id (Book 3, C1) | M0/B1 (translation arithmetic) | PROVED |
| 30 (Book 3) | Fold lemma: the two cophase directions coincide on 𝕋_π as one involution of exact order 2 (Book 3, C4) | definitions | PROVED |
| 31 (Book 3) | Eighth-turn η = τ_{π/4} has exact order 8; faithful cyclic action on the eight octants O_j (Book 3, C8) | M0/B1 (translation arithmetic) | PROVED |
| 32 (Book 3) | Half-angle tangent t = tan(x/2): 𝕋₂π → ℝ̂ is bijective; x = ±π ↦ ∞ (Book 3, C12) | M0 (monotonicity, limits) | PROVED |
| 33 (Book 3) | Directed cophase is Möbius: x ↦ x±π/2 acts as t ↦ Q_±(t); Q₊²(t) = −1/t; Q₊ exact order 4 in PGL(2,ℝ); marked orbit 0→1→∞→−1→0 = cardinal phases (Book 3, C13) | P32 + M0 (tan addition formula) | PROVED |
| 34 (Book 3) | Harmonic cross-ratio: the ordered quadruple (0,∞;1,−1) has cross-ratio −1 (Book 3, C14) | P33 | PROVED |
| 35 (Book 3) | Determinant separates cophase from reflection: det A₊ = +2 vs det R = −1; R∘Q₊∘R = Q₋ (Book 3, C15) | P33 + M0 (determinants) | PROVED |
| 36 (Book 3) | Universal reciprocal transform f(u) = √(1+u²)−u: strictly decreasing bijection ℝ→(0,∞), inverse u = (1−s²)/(2s), f(−u)f(u) = 1, f(u) = e^{−arsinh u} (Book 3, C16) | M0 (calculus, limits) | PROVED |
| 37 (Book 3) | Unit threshold recovers the sign: sgn(u) = sgn(1−s²) with s = f(u) (Book 3, C17) | P36 | PROVED |
| 38 (Book 3) | One map generates the four primitives: sxp = f(cot x), srx = f(−cot x), crx = f(tan x), cxp = f(−tan x); ln srx = −ln sxp = arsinh(cot x) (Book 3, C18) | P36 + M0 (1+cot² = csc²) | PROVED |
| 39 (Book 3) | Threshold formulas: sgn(1−sxp²) = sgn(srx²−1) (and cxp/crx analogue) (Book 3, C19) | P38 + Book 0 P1 (srx·sxp = 1) | PROVED |
| 40 (Book 3) | Unequal limits lim_{+∞}f = 0⁺, lim_{−∞}f = +∞ bar a single-valued global RP¹ coordinate via f (Book 3, C20) | P36 | PROVED |
| 41 (Book 3) | Cophase group Γ_c = ⟨τ_{π/2}⟩ ≅ C4 preserves FlatWave's domain D (Book 3, C21) | P29 | PROVED |
| 42 (Book 3) | Cophase–FlatWave character: χ_c(τ_{kπ/2}) = (−1)^k is a homomorphism Γ_c→{±1} with FlatWave(g·x) = χ_c(g)·FlatWave(x); ker χ_c = {id, τ_π}; factors C4→C2 (Book 3, C23) | Book 0 P7 (FW reversal/invariance) + P29 | PROVED |
| 43 (Book 3) | Octant sign law: FlatWave\|_{O_j} = (−1)^{⌊j/2⌋} (Book 3, C24) | M0 (sign of sin on half-π intervals) | PROVED |
| 44 (Book 3) | FlatWave in the projective coordinate: FlatWave(x) = sgn[t(1−t²)], t = tan(x/2); cophase reverses, half-turn preserves the sign polynomial (Book 3, C25) | P32, P33 + M0 (tan double-angle) | PROVED |
| 45 (Book 3) | FlatWave = sgn(t)·sgn(1−t²): agrees with the tautological sign sgn(t) exactly on \|t\|<1, differs on \|t\|>1 (Book 3, C33) | P44 (exact sign algebra) | PROVED |
| 46 (Book 3) | Cophase monodromy product: the four FlatWave multipliers −1,−1,−1,−1 have product +1 around one 2π circuit (Book 3, C34) | Book 0 P7; measured by completed run B37 ("exact", 2026-09-22) | CHECKED |
| 47 (Book 3) | Half-angle flip: q(θ+2π,n) = −q(θ,n) for q(θ,n) = cos(θ/2)+sin(θ/2)n (Book 3, C46) | declared quaternion-model import + M0 | PROVED (modulo declared import) |
| 48 (Book 3) | Rodrigues bridge, chart-qualified: on (0,π), ‖r‖ = tan(θ/2) = sxp(θ); the FlatWave seam θ=π/2 (ρ=1) is regular (q₀=1/√2≠0); chart boundary q₀=0 at θ→π (Book 3, C48) | declared quaternion-model import + register row 17 (Book 2: sxp = tan(x/2)) + M0 | PROVED (modulo declared import) |
| 49 (Book 3) | Collinear Rodrigues composition reduces to the tangent addition formula (Book 3, C47) | declared Rodrigues import; measured by completed run B40 (res. 6.079e-16, 2026-09-22) | CHECKED |
| 50 (Book 3) | Reciprocal compatibility surface on P°: (1−σ_{XY}²)(1−σ_{YZ}²)(1−σ_{ZX}²) = 8σ_{XY}σ_{YZ}σ_{ZX} with σ_{IJ} = f(u_{IJ}) (Book 3, C28) | P36 (exact inverse) + declared RP²-atlas import (cyclic-ratio identity) | PROVED (modulo declared import) |
| 51 (Book 3) | Dominance cycle: on each octant interior exactly one primitive is strictly largest, cycling srx→cxp→crx→sxp (×2); strict positive gap at each octant midpoint (Book 3, C9) | P38; measured by completed run B10 (min gap 3.531, 2026-09-22) | CHECKED |

## Book chapters

Each later book appends its own chapter here, in dependency order. No
principle may be cited in a proof before it is established: a chapter may
cite only the seed principle, earlier book chapters, and Euclid's
propositions from the 13 ledgers.

---

## Book 15 — Saw interchanges, double-angle decomposition, bridge to E8

Evaluated: 2026-09-22. Source: `~/workspace/euclid_work/books/book15_proof.md`
(44 claims + 8 firewalls M15-A…M15-H).

Euclid-citation boundary (checked in the 13 ledgers before writing this
chapter): the Elements contain no analytic sine/cosine/tangent functions.
The ledgers (e.g. book1, book3) record analytic trigonometry on a declared
coordinate as **standard imported background mathematics (ST)** — used, never
derived from an Elements proposition. Accordingly no Euclid book/proposition
number is fabricated below; the proofs rest on the declared
trigonometric substrate (real sin/cos/tan/cot on (0, π/2) with the
Pythagorean, half/double-angle, and complement identities; complex
exponentials; ordinary differentiation) plus earlier Principles 0..P.
Standing domain: x ∈ (0, π/2) unless stated otherwise.

### Evaluated claims summary

- PROVED (full): 25 — claims 1–9, 11–14, 16, 18, 20, 21, 24, 26, 27, 33–37.
- CHECKED (cited, not re-run here): 10 — claims 10, 22, 23, 29, 30, 31,
  40, 41, 42, 43 (book's verification suites / established computations;
  the non-rerun is stated).
- ASSERTED: 7 — claims 17, 19, 25, 28, 38, 39, 44 (interpretive readings,
  manuscript substrate, conditional bridge, status declarations).
- Split verdicts: claim 15 (PROVED balance part / CHECKED R_Y-mapping),
  claim 32 (PROVED stationary-point lemma / ASSERTED full conditional).
- INCOMPLETE: 0.
- Firewalls M15-A…M15-H: ASSERTED scope contracts, evaluated, not folded in.

The 44 claim proofs were re-verified step by step; the key algebraic steps
are reproduced below as the new Principles. Everything else with genuine
trig content below is already in Principle 0 or is bookkeeping
(P4's sum identity 2tan x + 2cot x = 4/sin 2x is Principle 0's regrouping
line; cited, not re-proved).

### Principle 1 (Book 15) — Complementary interchange of the canonical primitives (PROVED)

Book claim: 15.I.T1, 15.I.C1 (claims 1, 3); corollary 15.I.D1 (claim 2).

Definitions: for x ∈ (0, π/2),
srx(x) = cot(x/2), sxp(x) = tan(x/2),
cxp(x) = tan(π/4 + x/2), crx(x) = tan(π/4 − x/2),
and the complement map Cx = π/2 − x.

Statement: C is an involution, C(Cx) = x, and it swaps the primitive pairs:
srx(Cx) = cxp(x), cxp(Cx) = srx(x), sxp(Cx) = crx(x), crx(Cx) = sxp(x).
With the packaging urx = srx − crx, uxp = cxp − sxp and Ψ_U = urx + i·uxp,
urx(Cx) = uxp(x), uxp(Cx) = urx(x), and Ψ_U(Cx) = i·conj(Ψ_U(x)).

Proof: C(Cx) = π/2 − (π/2 − x) = x. srx(Cx) = cot((π/2 − x)/2)
= cot(π/4 − x/2). By the substrate complement law cot θ = tan(π/2 − θ),
cot(π/4 − x/2) = tan(π/2 − (π/4 − x/2)) = tan(π/4 + x/2) = cxp(x).
Applying C again (involution) gives cxp(Cx) = srx(x). Likewise
sxp(Cx) = tan((π/2 − x)/2) = tan(π/4 − x/2) = crx(x), and crx(Cx) = sxp(x).
Then urx(Cx) = srx(Cx) − crx(Cx) = cxp(x) − sxp(x) = uxp(x), and
uxp(Cx) = cxp(Cx) − sxp(Cx) = srx(x) − crx(x) = urx(x). Finally
Ψ_U(Cx) = uxp(x) + i·urx(x) = i(urx(x) − i·uxp(x)) = i·conj(Ψ_U(x)). ∎

Status: **PROVED** (analytic, complete). Proved-from: trig substrate
(complement laws) + definitions. Euclid citation: none (ledger boundary, ST).

### Principle 2 (Book 15) — Primitive-difference identities (PROVED)

Book claim: 15.II.T1 (claim 4).

Definitions: A(x) = cot(x/2) − tan(x/2), B(x) = tan(π/4 + x/2) − tan(π/4 − x/2).

Statement: for x ∈ (0, π/2), A(x) = 2cot x and B(x) = 2tan x
(hence A(x)·B(x) = 4cot x·tan x = 4).

Proof: A = (cos²(x/2) − sin²(x/2))/(sin(x/2)cos(x/2)) by common denominator.
cos²(x/2) − sin²(x/2) = cos x and 2sin(x/2)cos(x/2) = sin x (substrate
double-angle), so A = cos x/(sin x/2) = 2cot x. For B, use
tan P − tan Q = sin(P − Q)/(cos P cos Q) with P − Q = x, and
cos(π/4 + x/2)cos(π/4 − x/2) = (cos x + cos(π/2))/2 = cos x/2
(product-to-sum, substrate), giving B = sin x/(cos x/2) = 2tan x. ∎

Status: **PROVED** (analytic, complete). Proved-from: trig substrate
(half/double-angle, tan-difference, product-to-sum). Euclid citation: none.

### Principle 3 (Book 15) — Double-angle difference identity (PROVED)

Book claim: 15.III.T1 (claim 6).

Definitions: D₂(x) = A(x) + B(x), K₂(x) = A(x) − B(x), with A, B from
Principle 2.

Statement: for x ∈ (0, π/2), D₂(x) = 4/sin 2x and K₂(x) = 4cot 2x.

Proof: D₂ = 2cot x + 2tan x = 2/(sin x cos x) = 4/sin 2x is exactly the
regrouping line of Principle 0 — cited, not re-proved. For the difference,
K₂ = 2cot x − 2tan x = 2(cos²x − sin²x)/(sin x cos x)
= 2cos 2x/(sin 2x/2) = 4cos 2x/sin 2x = 4cot 2x, using the substrate
double-angle formulas. ∎

Status: **PROVED** (analytic, complete). Proved-from: Principles 0, 2 +
trig substrate. Euclid citation: none.

### Principle 4 (Book 15) — Double-angle phasor and its differential ladder (PROVED)

Book claim: 15.III.T2, 15.III.D1 (claims 7, 8).

Definitions: Z₂(x) = (K₂(x) + 4i)/D₂(x), H_R(x) = 1/D₂(x),
V_R(x) = K₂(x)/(2D₂(x)), with D₂, K₂ from Principle 3.

Statement: for x ∈ (0, π/2): Z₂(x) = e^{2ix} = cos 2x + i sin 2x,
H_R(x) = sin 2x/4, V_R(x) = cos 2x/2, and
H_R′(x) = V_R(x), V_R′(x) = −4H_R(x), Z₂′(x) = 2iZ₂(x).

Proof: Z₂ = (4cot 2x + 4i)/(4/sin 2x) = sin 2x·(cot 2x + i)
= cos 2x + i sin 2x = e^{2ix} (substrate: complex exponential).
H_R = 1/(4/sin 2x) = sin 2x/4;
V_R = (4cot 2x)/(2·4/sin 2x) = (cos 2x/sin 2x)(sin 2x/2) = cos 2x/2.
Derivatives (substrate differentiation): H_R′ = (2cos 2x)/4 = cos 2x/2
= V_R; V_R′ = −(2sin 2x)/2 = −sin 2x = −4H_R; Z₂′ = 2i·e^{2ix} = 2iZ₂. ∎

Status: **PROVED** (analytic, complete). Proved-from: Principle 3 +
trig substrate (complex exponential, differentiation). Euclid citation: none.

### Principle 5 (Book 15) — Complement parity of the double-angle pair (PROVED)

Book claim: 15.II.T2 parity part (claim 5), 15.III.C1 (claim 9).

Statement: for x ∈ (0, π/2), with D₂, K₂ from Principle 3 and
H_R, V_R, Z₂ from Principle 4:
D₂(Cx) = D₂(x), K₂(Cx) = −K₂(x),
H_R(Cx) = H_R(x), V_R(Cx) = −V_R(x),
Z₂(Cx) = −conj(Z₂(x)) = e^{i(π − 2x)}.

Proof: From Principle 2, A(Cx) = 2cot(π/2 − x) = 2tan x = B(x) and
B(Cx) = A(x), so D₂(Cx) = A(Cx) + B(Cx) = B(x) + A(x) = D₂(x) and
K₂(Cx) = A(Cx) − B(Cx) = −K₂(x). From Principle 4,
H_R(Cx) = sin(2(π/2 − x))/4 = sin(π − 2x)/4 = sin 2x/4 = H_R(x);
V_R(Cx) = cos(π − 2x)/2 = −cos 2x/2 = −V_R(x);
Z₂(Cx) = e^{2i(π/2 − x)} = e^{iπ}e^{−2ix} = −e^{−2ix}
= −conj(e^{2ix}) = −conj(Z₂(x)). ∎

Status: **PROVED** (analytic, complete). Proved-from: Principles 1, 2, 4 +
trig substrate (complement laws). Euclid citation: none.

### Principle 6 (Book 15) — Transfer-angle parametrization (PROVED)

Book claim: 15.IV.C1 (claim 12).

Statement: for θ ∈ (0, π), with λ = sin²(θ/2):
1 − λ = cos²(θ/2), Ω = λ/(1 − λ) = tan²(θ/2),
H_Saw = λ(1 − λ) satisfies 2√H_Saw = sin θ,
and λ = cos²θ_λ is consistent with θ = π − 2θ_λ.

Proof: 1 − λ = 1 − sin²(θ/2) = cos²(θ/2); Ω = sin²(θ/2)/cos²(θ/2)
= tan²(θ/2). H_Saw = sin²(θ/2)cos²(θ/2) = (sin θ/2)² by the substrate
half-angle formula sin θ = 2sin(θ/2)cos(θ/2); 2√H_Saw = sin θ since
sin θ ≥ 0 on (0, π). Consistency: λ = cos²θ_λ = sin²(θ/2) gives
θ/2 = π/2 − θ_λ on the chart, i.e. θ = π − 2θ_λ. ∎

Status: **PROVED** (analytic, complete). Proved-from: trig substrate
(half-angle, complement). Euclid citation: none.

### Principle 7 (Book 15) — Rational (Weierstrass) parametrization of the circle (PROVED)

Book claim: 15.IV.D1 trig part (claim 13).

Statement: for θ ∈ (0, π) and q = tan(θ/2):
(2q/(1 + q²), (1 − q²)/(1 + q²)) = (sin θ, cos θ),
and hence (2q/(1 + q²))² + ((1 − q²)/(1 + q²))² = 1.

Proof: sin θ = 2sin(θ/2)cos(θ/2) = 2tan(θ/2)cos²(θ/2)
= 2q/(1 + q²), using cos²(θ/2) = 1/(1 + tan²(θ/2)) (substrate).
cos θ = (cos²(θ/2) − sin²(θ/2)) = (1 − q²)/(1 + q²).
The sum of squares is sin²θ + cos²θ = 1 (substrate Pythagorean). ∎

Status: **PROVED** (analytic, complete). Proved-from: trig substrate
(half-angle). Euclid citation: none.
Note: claim 13's tanh double-angle companion is hyperbolic, not circular,
and is not folded in.

### Principle 8 (Book 15) — Harmonic-oscillator relation of the double-angle pair (PROVED)

Book claim: 15.VI.T2 differential part (claim 21).

Statement: for all real x, (sin 2x)″ + 4sin 2x = 0 and
(cos 2x)″ + 4cos 2x = 0.

Proof: d/dx sin 2x = 2cos 2x, d²/dx² sin 2x = −4sin 2x;
d/dx cos 2x = −2sin 2x, d²/dx² cos 2x = −4cos 2x (substrate
differentiation of sin/cos). Rearranging gives both relations. ∎

Status: **PROVED** (analytic, complete). Proved-from: trig substrate
(derivatives of sin/cos). Euclid citation: none.

### Principle 9 (Book 15) — Stationary points of the sine (PROVED)

Book claim: 15.VII.CT1 lemma part (claim 32).

Statement: for real θ, the stationary points of f(θ) = −sinθ are exactly
θ = π/2 + kπ, k ∈ ℤ; in particular on the quarter-phase domain the
solutions are θ = ±π/2.

Proof: f′(θ) = −cosθ = 0 ⟺ cosθ = 0 ⟺ θ = π/2 + kπ (substrate:
zeros of cosine). ∎

Status: **PROVED** (analytic, complete). Proved-from: trig substrate
(derivative of sin, zeros of cos). Euclid citation: none.
Note: claim 32's full conditional theorem ("quarter-phase selection by sign
of s_Ωκ_y") is ASSERTED, not folded in.

### Not folded in (evaluated with reasons)

- Claims 10, 22, 23, 29, 30, 31, 40, 41, 42, 43: CHECKED — cited completed
  computations (Saw symbolic reduction, J-conventions, bigrading witnesses,
  E8 representations), not re-run here; none is a trigonometric identity.
- Claims 11, 15-R_Y, 16, 18, 20, 26, 27, 33, 34, 35, 36, 37: evaluated as
  proved/correct as stated, but not trigonometric principles: chart-share
  parities and logarithms (11), Bloch-state algebra (15–16, 18),
  order-of-maps group theory (20), commuting-involution linear algebra
  (26, 27), logarithmic/parametric algebra (33), binomial combinatorics
  (34, 36), and hyperbolic (cosh) identities (35, 37) — circular measure
  is not involved, so they are not forced into the cumulative trig proof.
- Claims 17, 19, 25, 28, 32-full, 38, 39, 44 and firewalls M15-A…M15-H:
  ASSERTED — manuscript interpretations, imported substrate definitions,
  conditional bridges, and scope declarations; correctly labeled, not folded.

### Register

The nine new Principles are entered in the **Principles register** table at
the top of this document as rows "1 (Book 15)" through "9 (Book 15)"; no
separate table is kept here, and no earlier chapter was renumbered or rewritten.


| Principle id | Statement | Proved-from | Scope |
|---|---|---|---|
| 1 | Complementary interchange of the canonical primitives: srx ↔ cxp, sxp ↔ crx under Cx = π/2 − x; corollary Ψ_U(Cx) = i·conj(Ψ_U(x)) | trig substrate (complement laws) + definitions | PROVED |
| 2 | Primitive-difference identities: cot(x/2) − tan(x/2) = 2cot x, tan(π/4+x/2) − tan(π/4−x/2) = 2tan x | trig substrate (half/double-angle, tan-difference, product-to-sum) | PROVED |
| 3 | Double-angle difference: 2cot x − 2tan x = 4cot 2x (sum D₂ = 4/sin 2x cited from Principle 0) | Principles 0, 2 (Book 15) + substrate | PROVED |
| 4 | Double-angle phasor Z₂ = e^{2ix}, H_R = sin 2x/4, V_R = cos 2x/2; H_R′ = V_R, V_R′ = −4H_R, Z₂′ = 2iZ₂ | Principle 3 (Book 15) + substrate (complex exp, differentiation) | PROVED |
| 5 | Complement parity: D₂, H_R even; K₂, V_R odd; Z₂(Cx) = −conj(Z₂(x)) | Principles 1, 2, 4 (Book 15) + substrate | PROVED |
| 6 | Transfer-angle parametrization: λ = sin²(θ/2) ⇒ Ω = tan²(θ/2), 2√(λ(1−λ)) = sin θ | trig substrate (half-angle) | PROVED |
| 10 (Book 15) | Weierstrass parametrization: (2q/(1+q²), (1−q²)/(1+q²)) = (sin θ, cos θ) for q = tan(θ/2) | trig substrate (half-angle, Pythagorean) | PROVED |
| 11 (Book 15) | (sin 2x)″ + 4sin 2x = 0, (cos 2x)″ + 4cos 2x = 0 | trig substrate (derivatives of sin/cos) | PROVED |
| 12 (Book 15) | Stationary points of θ ↦ −sinθ are θ = π/2 + kπ | trig substrate (derivative, zeros of cos) | PROVED |

## Book 11 — Particle Architecture and Standard Model Comparison

Source: `~/workspace/euclid_work/books/book11_proof.md` (claim inventory
T1–T13, K1–K6, A1–A7, I1–I4; counts PROVED 13 · CHECKED 6 · ASSERTED 7 ·
INCOMPLETE 4), checked against the rewrite page
`~/workspace/r-theory-rewrite/book11/index.html` (Part I–III; the page's
numbered theorems 11.PG.T1, 11.PG.N1, 11.PG.IX, 11.III.B, 11.IV.T2,
11.VI.T2/T5/T7, 11.VIII.T1–T3, 11.IX.T1–T3, 11.X.T1, 11.V.A, 11.IX.P1,
11.VI.P1 and the 15 MANUSCRIPT ASSERTION labels all map onto the
inventory's items).

### Evaluated claims summary

Book 11's proved claims are exact matrix, Lie-algebraic, and
representation-theoretic results over the declared 2+3 carrier, plus exact
rational arithmetic and elementary no-go logic:

- T1–T4 (11.PG.T1, 11.PG.III, 11.PG.N1, 11.PG.XII): the J-identity
  UᵀJU = (det U)J, its infinitesimal form XᵀJ + JX = (tr X)J, the
  Maurer–Cartan negative lemma F = 0 for pure gauge, and the SU(2)
  mirror-automorphism lemma. Matrix and differential identities.
- T5–T7 (11.III.C, 11.III.B, 11.IX.T1/C1): unique traceless block phase,
  the S(U(2)×U(3)) ≅ [SU(2)×SU(3)×U(1)]/ℤ₆ isomorphism, and the primitive
  integral cocharacter with gcd(3,2) = 1. Linear algebra, group theory,
  number theory.
- T8 (11.IV.T1, T2): the six-block weighted branching, 16 = 1⊕1⊕6⊕3⊕3⊕2
  with exact Y₀-weights. Representation combinatorics.
- T9–T10 (11.VI.T2–T4, 11.IX.T2/T3): anomaly-cancellation arithmetic and
  the conditional charge pattern (c = 1/6, Q = T₃ + Y₀). Exact rational
  arithmetic, conditional on the stated physics contracts.
- T12 (11.VIII.T1, 11.VI.T5, 11.VII.T2–T3): the 10-dimensional branching
  2+3+2+3 = 10, doublet parity, generation blindness. Representation
  theory.
- T13 (11.PG.N3, 11.I.B, 11.II.F1, 11.VII.N1, 11.VI.T7): no-go logical
  forms. Elementary logic, conditional on the stated premise data.

None of T1–T10, T12, T13 is a statement about trigonometric functions,
angles, or circular measure, and none yields one: T6's six roots z⁶ = 1
are a finite-group kernel fact, not a trigonometric identity; T5/T7 are
linear-algebra/number-theory facts. No honest trigonometric principle can
be extracted from them, so none is folded in — reported plainly, not
forced.

The CHECKED items K1–K6 are completed numeric validations (the 2026-09-22
run: exit 0, 33/33 assertions, worst error 5.403e-15); they measure
agreement or check imported isomorphisms but prove no identity, so none is
folded in. The ASSERTED items A1–A7 are the page's own assumptions,
contracts, and open debt ledger; the INCOMPLETE items I1–I4 are
unfinished or out of scope (I4: Euclid XI 11.1–11.39 — no counterpart, by
the No-Euclid-wholesale boundary, 4.X.H).

One claim carries genuine trigonometric content: **T11 (§11.PG.IX)**, the
helicity reciprocal identity
cxp(χ) = e^η = √[(1+β)/(1−β)], crx(χ) = e^{−η}, cxp·crx = 1, with
sin χ = β = tanh η. It is folded in as Principle 1 below, proved exactly
from definitions. The book's P_L↔P_R favored/suppressed reading of T11
rests on the imported Dirac helicity-weight formula (ST, used-not-proved
in the book) and is interpretation, not proved mathematics — it is not
part of the folded principle.

Dependency note: this chapter cites only the seed principle's standing
(no mathematical use of Principle 0 is needed) and its own definitions;
it is valid regardless of where Books 0–10 land in the campaign order.

### Principle 1 (PROVED) — Helicity reciprocal identity (from Book 11, T11)

#### Statement

Let β ∈ (−1, 1) and let η ∈ ℝ satisfy β = tanh η, where
tanh η = (e^η − e^{−η})/(e^η + e^{−η}) and e^x = Σ_{n≥0} x^n/n!.
Let χ be an angle with sin χ = β. Define cxp(χ) = √((1+β)/(1−β))
and crx(χ) = e^{−η}. Then

(i) cxp(χ) = e^η, i.e. √((1+β)/(1−β)) = e^η;
(ii) cxp(χ)·crx(χ) = 1.

#### Proof (definitions first)

Lemma (PROVED): e^a·e^b = e^{a+b} for all real a, b.
The exponential series converges absolutely for every real x, so the
Cauchy product of the series for e^a and e^b is legitimate; its k-th
coefficient is Σ_{j=0}^k a^j b^{k−j}/(j!(k−j)!)
= (1/k!)·Σ_{j=0}^k C(k,j)·a^j·b^{k−j} = (a+b)^k/k!, by the binomial
theorem. The product series is therefore Σ_k (a+b)^k/k! = e^{a+b}. ∎

Corollary: e^0 = 1 (every term past k = 0 vanishes), so
e^η·e^{−η} = e^0 = 1 and e^{−η} = 1/e^η (e^{−η} ≠ 0). Positivity:
e^η = (e^{η/2})² ≥ 0 and e^η ≠ 0, hence e^η > 0; likewise e^{−η} > 0.
So e^η + e^{−η} > 0 as a sum of positives.

Main steps:
1. From the definition of tanh:
   1 + β = (e^η + e^{−η} + e^η − e^{−η})/(e^η + e^{−η})
         = 2e^η/(e^η + e^{−η});
   1 − β = 2e^{−η}/(e^η + e^{−η}).
   Both are positive since β ∈ (−1, 1).
2. (1+β)/(1−β) = e^η/e^{−η} = e^η·(1/e^{−η}) = e^η·e^η = e^{2η},
   using 1/e^{−η} = e^η (corollary) and the lemma with a = b = η.
3. cxp(χ) = √((1+β)/(1−β)) = √(e^{2η}) = e^η: the positive square root
   of the square of the positive number e^η.
4. cxp(χ)·crx(χ) = e^η·e^{−η} = 1, by the corollary. ∎

Domain: β ∈ (−1, 1) ⟺ η ∈ ℝ ⟺ sin χ ∈ (−1, 1) (χ not an odd multiple of
π/2). The angle χ enters only through the book's parametrization
sin χ = β; the identity is a relation between the β-parametrized
quantities.

Status: **PROVED** (analytic, complete).

Grounds of the proof: the stated definitions (exponential series, tanh,
positive square root, sin), the binomial theorem, and the Cauchy product
for absolutely convergent series. No earlier principle and no Euclid
proposition is used as a premise. This respects the campaign's
No-Euclid-wholesale boundary (4.X.H, recorded in the Book 1 ledger):
the proof is definitions-first, exactly as the seed principle is, and no
Euclid citation is claimed for it.

Notation disambiguation (required for precision): the symbols cxp(χ) and
crx(χ) in this principle are Book 11's helicity pair from §11.PG.IX —
cxp(χ) = √((1+β)/(1−β)) = e^η, crx(χ) = e^{−η} — and are **not** the
campaign's canonical primitives cxp/crx of Book 0's Principle 1
("srx·sxp = 1 and cxp·crx = 1 on D = ℝ \ {kπ/2}"). Same names, different
objects, different domains: the identity cxp(χ)·crx(χ) = 1 proved here is
a separate exact result about the helicity pair, not a restatement of
Book 0's primitive identity. No double-counting and no name collision
are intended; the (Book 11) suffix on the register row marks the
distinction.

## Book 5 — Axiom Zero and the Decadic Carrier (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book5_proof.md`
(claim inventory C1–C11 with proofs; rewrite page
`~/workspace/r-theory-rewrite/book5/index.html` — *Book 5 — Axiom Zero and
the Decadic Carrier*).

### Evaluated claims summary

All eleven claims were restated and their proofs verified; none carries
genuine trigonometric content (no identity, lemma, or exact relation about
trigonometric functions, angles, or circular measure). The book's own proof
file states this plainly: "Book 5 contains no trigonometric claims," and no
proposition of Euclid's *Elements* is used deductively in its proofs (they
are finite-dimensional real linear algebra and elementary arithmetic).

- **C1.** U = E ⊕ V is a real rank-5 carrier (2 + 3 = 5) — **PROVED**.
  Dimension arithmetic; no trig. Not folded.
- **C2.** Axiom Zero A0.1: independent isomorphic partner U^♯ with declared
  block-compatible pairing ι; W := U ⊕ U^♯ — **ASSERTED** (new axiom).
  A granted starting point, not mathematics. Not folded.
- **C3.** Axiom Zero A0.2: primitive diagonal noncoupling — **ASSERTED**
  (new axiom). Not folded.
- **C4.** dim_ℝ W = 5 + 5 = 10 (conditional on C2) — **PROVED**.
  Rank arithmetic. Not folded.
- **C5.** I_ι(u,v) := (−ι^{−1}v, ιu) satisfies I_ι² = −id; W has complex
  rank 5; I_ι depends on the declared pairing ι (conditional on C2) —
  **PROVED**. Real linear algebra (complex structure), not a statement about
  trig functions, angles, or circular measure. Not folded.
- **C6.** Corollary 5.3.1: W_ext = W ⊕ Z has dim_ℝ = 10 + dim Z ≥ 10;
  I-invariant Z forces dim_ℝ W_ext = 10 + 2m (conditional on C2) —
  **PROVED**. Rank bound. Not folded.
- **C7.** Theorem 5.4.1: k := dim_ℝ(U ∩ IU) ∈ {0, 2, 4},
  dim_ℝ(U + IU) = 10 − k ∈ {10, 8, 6}, complex ranks 5, 4, 3; k = 0 is the
  axiom, k = 2, 4 lawful counterfactuals — **PROVED** as an enumeration (the
  selection of k = 0 is the axiom, **ASSERTED**). Invariant-subspace
  dimension theory. Not folded.
- **C8.** 2n = n(n−1)/2 has unique positive-integer solution n = 5, value
  10 — **PROVED** (exact; corroborated by completed numeric check V9, which
  the proof does not need). A Diophantine equation in n; no trig functions
  involved. Not folded.
- **C9.** (dim Λ^0U,…,dim Λ^5U) = (1, 5, 10, 10, 5, 1) — **PROVED** (exact;
  corroborated by completed numeric check V10). Binomial coefficients.
  Not folded.
- **C10.** The Hodge one-step condition ⋆(Λ²U ∧ Λ²U) ⊂ Λ^1U demands
  n − 4 = 1, i.e. n = 5 — **PROVED** (exact; corroborated by completed
  numeric check V11). Degree/index arithmetic on exterior powers. Not
  folded.
- **C11.** Status/exclusions (5.5) and the anti-circularity firewall (5.6) —
  **ASSERTED** (methodological declarations of the manuscript, not
  mathematical theorems). Not folded.

Claim-by-claim table with verdicts: `book5_claims.md` (status: complete).

### New Principles added: none

Book 5 contributes **no new Principles**. Its eight proved claims are
established mathematics but concern carrier ranks, complex structures, and
exterior-algebra dimensions — none is an identity, lemma, or exact relation
about trigonometric functions, angles, or circular measure, so none belongs
in the cumulative trigonometric proof. Its three asserted claims are the
theory's new axiom (A0.1, A0.2) and methodological declarations; assertions
cannot found trigonometric principles. Per the standing rule, nothing was
forced: forcing a non-trigonometric claim in would misrepresent the book.

Highest Principle number remains **P0** (Kit's double-angle secant-cosecant
identity). The principles register is unchanged.

---

## Book 16 — The Microscopic R Theory: Extension Proofs (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book16_proof.md`
(claim inventory #1–#34 with proofs; rewrite page
`~/workspace/r-theory-rewrite/book16/index.html` — *Book 16 — The
Microscopic R Theory*, Part III: Established / Conditional / Not established).

### Euclid boundary (standing for this book)

No proposition of Euclid's *Elements* is a deductive premise of any
principle below. The campaign's own Euclid ledgers record that the
construction substrate explicitly **excludes** trigonometric angle measure
and the Pythagorean identity (book4_ledger.md P4.1; book6_ledger.md
Declaration P4.1), and no ledger attests a trig extension derivation. The
book's own proof file states the same boundary (§E): its proofs are
analytic, from definitions D1–D12. Accordingly the three new principles
are proved from definitions in the seed's manner ("definitions + lemmas"),
not from Euclid citations — inventing a Euclid citation here would be
dishonest. Dependency order holds: nothing is used before it is proved;
P1–P3 use only series/exponential definitions, no earlier principle.

### Evaluated claims summary

All 34 claims were restated and their proofs verified against the proof
file; arithmetic spot-checks (binomial coefficients, the 30380 dimension
sums, the dihedral relations, the γ-identity) re-verify exactly. Claim-by-claim
table with verdicts: `book16_claims.md` (status: complete).

**PROVED (29)** — proofs verified complete:
- #1 16.I.49 diagonal Z bridge: exp(2xJ) = cos(2x)I + sin(2x)J; covariant
  45° stationarity. → folded as **P1** (bridge identity only; the
  stationarity corollary needs cos(π/2) = 0, not folded — see below).
- #2 16.I.59(a) qSaw lift: tanh double-angle, Σ²−Δ² = μ² invariant, lift
  uniqueness. → folded as **P2** (tanh double-angle) and **P3** (hyperbolic
  Pythagorean + radius invariance). Lift uniqueness is descent algebra,
  not trig — not folded.
- #3 16.I.58 transported projector P(w)² = P(w) — conditional on the D4
  2×2 Clifford premises. Clifford algebra, no trig content.
- #5 16.I.61/60(b) E8 dimension arithmetic (C(16,4) = 1820, C(16,6) =
  8008, the 30380 sums, Alt²(248), Sym²(128)). Exact integer arithmetic.
- #6 16.I.71.1 two symmetric 27000s in 30380⊗30380 — arithmetic PROVED;
  the multiplicities themselves are ST (LieART 2.1.1 import).
- #7 16.I.71.2 projection ratio (4/3) — conditional on the book's two
  eigenspace premises. Ratio arithmetic.
- #8 16.I.64.E 16×16 witness spectrum — conditional on the manuscript's
  explicit matrix (audit diagonalization).
- #9 16.I.66.4 two-Pfaffian topology gap. Exterior algebra.
- #10 16.I.66.1 homogeneity kills the origin seed. General algebra.
- #11 16.I.64.D same-exterior-form preservation — conditional on the
  branch factorization.
- #12 16.I.76.6 Holst–Einstein–Cartan inverse — conditional on D8
  (∗_L² = −I, i.e. AX-16.4).
- #13 16.I.81 selector monotonicity — conditional on the declared fixed
  shared-form/co-moving reduction. Single-variable calculus.
- #14 16.I.75.11 radial stabilization. Calculus.
- #15 16.I.95.T1 falsified Q_Y lift — conditional on stated premises.
  Logical obstruction.
- #16 16.I.96.T1 dihedral relations R² = K, R⁸ = I, PRP⁻¹ = R⁻¹ —
  group theory from K² = −I (the rotation interpretation is the book's;
  the proof is Clifford algebra, not a trig identity).
- #17 16.I.96.T2 no ordinary Ward parity — conditional on Q_Y-orthogonality.
- #18 16.I.98.T1/T2 dihedral double cover, R⁴ = −I central, D₄ quotient —
  group theory (same note as #16).
- #19 16.I.97.T2 finite-mode Jacobian det q = (−1)⁶⁴ = +1 — finite part
  PROVED; the global anomaly is ASSERTED open (carried in #33).
- #20 16.I.100.T1 normalizer no-go — conditional on standard Hodge
  duality (ST). Dimension contradiction.
- #21 16.I.101.T2 no Grassmannian lift — conditional on stated premises.
- #22 16.I.102.T2 unique positive q-fixed kinetic surface — conditional on
  the manuscript's kinetic-surface premises.
- #23 16.I.104.T2 oriented Fujikawa closure J(R_D) = 1 — conditional on
  the asserted index divisibility AX-16.2. The trig kernel (e^{−2πik} =
  1) is elementary, but the claim's substance is conditional on the
  asserted axiom — not promoted.
- #24 16.I.109 phase lattice Re(ab̄) = 0 ⇒ φ_a − φ_b = ±π/2 mod π — PROVED
  at the book's level, with genuine angle content, but NOT folded: the
  needed trig lemma (cos θ = 0 ⟺ θ an odd quarter-turn) rests on the
  zero-structure of cosine, which is established by no earlier Principle
  and no Euclid proposition (trig is excluded from the Euclid substrate).
  Not forced.
- #25 16.I.110.T2 degree-four minimal carrier — conditional on the Spin(10)
  invariant-theory premises.
- #26 16.I.112 Schur-complement selector — conditional on the asserted
  healthy heavy-54 block AX-16.1. Not folded: conditional on an asserted
  axiom, and its trig kernel (odd-quarter selection via sin 4φ, cos 4φ)
  needs the sin/cos zero-structure not yet established. Wording slip
  noted in the proof file review: "d²V/dφ_a² ∝ −16cos 4φ_a is negative
  exactly at odd quarters" — at cos 4φ_a = −1 the second derivative is
  +16C > 0 (a minimum); the conclusion (minima at φ_a = π/4 mod π/2)
  is correct.
- #27 16.I.124 kinetic-rapidity cubic — series calculus; an impossibility
  result, not a trig identity.
- #28 16.I.127 paired rapidity Υ_B invariant — conditional on the stated
  transformation laws.
- #29 16.I.130 pitchfork fixed points — bifurcation calculus (its proof
  uses tanh 2δ, i.e. P2's identity, but the claim itself is not a trig
  principle).
- #30 16.I.88 γ_{μν}γ^ν = 3γ_μ — Clifford algebra in the stated convention.

**CHECKED (1):** #4 16.I.59(b) quartic-135 witness (symmetry, tracelessness,
SO(16)-equivariance, Q₀₀ = 9/2) — the book audit's explicit computation,
not re-derived here; exterior algebra/representation, no trig content.

**ASSERTED (3):** #32 the manuscript's September 15, 2026 normalization
retraction (c_ord = 1, N_1820 = 2, K_parent = 1 not established); #33 the
activation/open gates (λ₂ ≠ 0 unforced, radius stabilization, BRST/healthy
spin-2/mirror action gates); #34 Δ_op(Book 16) = ∅ and the Volume III
closure status declarations. Manuscript's own declarations, recorded.

**INCOMPLETE (1):** #31 the IC defects — 16.I.80 sign error (h_R(v_a,C) =
0 boxed derivation gives 0 = 0, not the claimed identity; dependent boxed
P_F C = 0 and N_scalar,radial = 0 incorrect as proved), line-1614 Schur
formula wrong under the ordinary real adjoint, line-1925 rank biconditional
omits the zero-coupling case, 16.I.106.T2/C1 sign error (retracted by the
manuscript itself at 16.I.107). Documented incorrect as proved.

### New Principles added: three (P1, P2, P3)

#### Principle 1 — Double-angle bridge identity (PROVED)

**Statement.** Let J be a real-linear operator with J² = −I, I the
identity, and define exp(A) = Σ_{n≥0} Aⁿ/n!, sin u = Σ_{k≥0} (−1)^k
u^{2k+1}/(2k+1)!, cos u = Σ_{k≥0} (−1)^k u^{2k}/(2k)!. For every real x:

    exp(2xJ) = cos(2x)·I + sin(2x)·J.

**Domain.** All real x; any real-linear J with J² = −I (the book's D3
bridge generator is the 2×2 real model).

**Proof.** (2xJ)^{2k} = (2x)^{2k}J^{2k} = (−1)^k(2x)^{2k}·I and
(2xJ)^{2k+1} = (−1)^k(2x)^{2k+1}·J, since J^{2k} = (J²)^k = (−1)^k I.
Summing the even and odd terms of the exponential series separately
(absolute convergence justifies regrouping):

    exp(2xJ) = Σ_k (−1)^k(2x)^{2k}/(2k)!·I + Σ_k (−1)^k(2x)^{2k+1}/(2k+1)!·J
             = cos(2x)·I + sin(2x)·J. ∎

**Scope:** PROVED (analytic, complete). **Source claim:** 16.I.49 (claim
#1). This is the circular double-angle identity in bridge form — the
circular sibling of the seed's (P0) double-angle theorem. The claim's
45° stationarity corollary (H′(π/4) = 0) is not folded: it uses
cos(π/2) = 0, a fact about the zero-structure of cosine not yet
established in this document.

#### Principle 2 — Hyperbolic double-angle, tanh form (PROVED)

**Statement.** For real w, with cosh w = (e^w + e^{−w})/2,
sinh w = (e^w − e^{−w})/2, tanh w = sinh w/cosh w (cosh w ≥ 1 > 0):

    tanh(2w) = 2·tanh(w) / (1 + tanh²(w)).

**Domain.** All real w.

**Proof.** 2·tanh w/(1 + tanh²w)
= [2(e^w − e^{−w})/(e^w + e^{−w})] ÷ [((e^w + e^{−w})² + (e^w − e^{−w})²)/(e^w + e^{−w})²]
= 2(e^{2w} − e^{−2w})/(2e^{2w} + 2e^{−2w})
= (e^{2w} − e^{−2w})/(e^{2w} + e^{−2w}) = tanh(2w). ∎

**Scope:** PROVED (analytic, complete). **Source claim:** 16.I.59(a)
(claim #2). This is the seed's (P0) double-angle theorem in hyperbolic
form — the book's proof file identifies it as such. Used inside this
book's proofs (e.g. claim #29's d/dδ ln cosh 2δ = 2 tanh 2δ).

#### Principle 3 — Hyperbolic Pythagorean identity and radius invariance (PROVED)

**Statement.** For all real ζ: cosh²(ζ) − sinh²(ζ) = 1. Consequently,
with Σ = μ·cosh(ζ), Δ = μ·sinh(ζ) for μ > 0:

    Σ² − Δ² = μ² (the radius μ is invariant),   Π_C := Δ/Σ = tanh(ζ).

**Domain.** All real ζ; μ > 0.

**Proof.** cosh²ζ − sinh²ζ = [(e^ζ + e^{−ζ})² − (e^ζ − e^{−ζ})²]/4
= (4e^ζe^{−ζ})/4 = 1. Then Σ² − Δ² = μ²(cosh²ζ − sinh²ζ) = μ², and
Π_C = μ·sinh ζ/(μ·cosh ζ) = tanh ζ. ∎

**Scope:** PROVED (analytic, complete). **Source claim:** 16.I.59(a)
(claim #2).

### Register note

Highest Principle number is now **P3**. The register table above carries
P0–P3. Claims #24 (phase lattice) and #26 (odd-quarter selection) carry
genuine angle content but were deliberately not forced in: their trig
kernels need the sin/cos zero-structure, which no earlier Principle and
no Euclid proposition establishes, and #26 is conditional on the asserted
AX-16.1. They are evaluated above with that reason stated plainly.

## Book 8 — Pre-Maxwell Geometry and the Compact-Carrier Field Boundary (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book8_proof.md`
(claim inventory E1–E21b with proofs; rewrite page
`~/workspace/r-theory-rewrite/book8/index.html` — *Book 8 — Pre-Maxwell
Geometry and the Compact-Carrier Field Boundary*; Euclid-contact boundary
checked against `~/workspace/euclid_work/ledger/book8_ledger.md`).

Note on the name: this is R Theory Volume II Book 8, not Euclid's
*Elements* Book 8 (arithmetic — continued proportion), which has zero R
Theory extension claims touching any of its propositions 8.1–8.27.

### Evaluated claims summary

All twenty-six claims were restated and their proofs verified: the
analytic proofs were re-derived by this worker (E1, E3, E5–E7, E9, E11,
E12a, E13a, E15, E17a–E20, E21a), the standard imports accepted under
their ST label (E2, E8, E14), and the eight asserted claims reported at
the book's scope with their gaps named. No proposition of Euclid's
*Elements* is used deductively in any Book 8 derivation — the book's own
stated boundary — so this chapter cites zero *Elements* propositions.

- **E1.** 8.1.T1: d²=0; B=dA gauge invariant; dB=0 — **PROVED**.
  Exterior calculus; no trig. Not folded.
- **E2.** 8.1.C1/T2: grad/curl/div in form language; ⋆₃²=+1 —
  **PROVED** (ST). Vector-calculus dictionary; no trig. Not folded.
- **E3.** 8.2: ⋆₄²=−1 on 2-forms given the declared Lorentzian metric —
  **PROVED** (ST, conditional on D-η). The "quarter-turn" is Hodge-star
  language on 2-forms, not trig functions/angles. Not folded.
- **E4.** 8.2 constitutive boundary: G=λ⋆₄F an identification, dG=J a
  sourced law — **ASSERTED**. Not folded.
- **E5.** 8.2.C1: dJ=0 from the admitted dG=J — **PROVED** (conditional).
  No trig. Not folded.
- **E6.** 8.3.N1, C1–C2: {±1}⊂U(1) does not generate continuous local
  U(1) — **PROVED**. Group-theoretic negative result; the e^{iπ} usage
  is incidental. Not folded.
- **E7.** 8.4.L1, T1: declared local redundancy forces the Abelian
  connection — **PROVED** (conditional on D-Phase). No trig. Not folded.
- **E8.** 8.5.L1: exactly two quadratic 4-forms in F — **PROVED** (ST).
  Invariant theory; no trig. Not folded.
- **E9.** 8.5.L2: F∧F=d(A∧F), the theta term is a boundary term —
  **PROVED**. No trig. Not folded.
- **E10.** 8.5.T1: Maxwell bulk uniqueness within D-Class — **ASSERTED**
  (conditional; class boundary declared). Not folded.
- **E11.** 8.6.T1: two-derivative scalar action class, E–L equation,
  stress tensor — **PROVED** (conditional on D-φ). No trig. Not folded.
- **E12a.** 8.6.T2: discrete symmetries force K, V to be functions of
  cos 4φ (harmonics cos 4nφ) — **PROVED** (conditional on P-Car
  symmetries). The one claim with genuine trigonometric content
  (Fourier mode selection + Chebyshev cos(4nφ)=T_n(cos 4φ)) — but it is
  conditional on ASSERTED carrier symmetries, and its trig core rests on
  Fourier/angle-addition theory not established from the seed, earlier
  chapters, or any ledger-verified *Elements* proposition. Assertions
  cannot found principles; folding it would break dependency order.
  Not folded.
- **E12b.** Carrier algebra identities — **ASSERTED** (P-Car). Not folded.
- **E12c.** 1D metric-flattening change of variables — **ASSERTED**.
  Not folded.
- **E13a.** 8.6.N1: symmetry classifies, does not select — **PROVED**.
  Meta-claim; trig functions are examples only. Not folded.
- **E13b.** Round-metric selection principle — **ASSERTED**. Not folded.
- **E14.** 8.7.T1, T2: free scalar field, Noether current, winding ∈ℤ —
  **PROVED** (ST). Topological standard import; no trig lemma. Not folded.
- **E15.** 8.7.T3: carrier wave identity □Z=2iZ□φ−4Z(dφ)² — **PROVED**.
  Complex-phasor calculus; not a real trig identity. Not folded.
- **E16.** 8.7.T4: null-carrier sector (five items) — **ASSERTED**.
  Not folded.
- **E17a.** 8.7A.T1, T2: sphere identity and coherency ceiling —
  **PROVED** (conditional on D-2S). Bloch-sphere algebra; no trig
  functions. Not folded.
- **E17b.** Fubini–Study coefficients — **ASSERTED**. Not folded.
- **E18.** 8.7A.N1: one-scalar obstruction dλ∧dφ=0 — **PROVED**.
  Exterior algebra; no trig. Not folded.
- **E19.** 8.7B.N1: direct E/B quadrature no-go, E²−c²B²=−E₀²cos4x≢0 —
  **PROVED**. The claim is a negative result about field quadrature; the
  double-angle step is incidental machinery, not the claim's content, and
  double-angle is not established in this document's dependency order.
  Not folded.
- **E20.** 8.7B.T1: circular-polarization witness, five identities —
  **PROVED** (conditional on D-EM). Vector identities under an EM import
  contract; no new trig principle. Not folded.
- **E21a.** 8.7B.3: A=g(x)dx ⇒ F=0 — **PROVED**. No trig. Not folded.
- **E21b.** A=Σf_a(x)θ^a ⇒ F∧F=0 — **ASSERTED**. Not folded.

Claim-by-claim table with verdicts: `book8_claims.md` (status: complete).

### New Principles added: none

Book 8 contributes **no new Principles**. Its eighteen proved claims are
established mathematics (several conditional on declared premises) but
concern exterior calculus, gauge structure, invariant theory, scalar
field theory, and Bloch-sphere algebra — none is an identity, lemma, or
exact relation about trigonometric functions, angles, or circular
measure that is provable from the cumulative document's allowed sources
in dependency order. Per the standing rule, nothing was forced: forcing
a non-foldable claim in would misrepresent both the book and the proof.

Concurrency note: this chapter was evaluated against the document as this
worker read it (seed Principle 0 plus the Book 5 chapter, before sibling
book workers appended their chapters and principles). Book 8 itself adds
**no new Principles**. The register's subsequent growth by other books
does not change the fold decision: none of Book 8's claims cite those
later chapters, nothing was folded from them, and the one trig-flavored
claim (E12a) remains unfoundable as a principle because it is conditional
on the ASSERTED carrier premises (P-Car) — assertions cannot found
principles.

## Principle 1 (PROVED) — the operator Euler formula

**Source book claim:** Book 6, C6 (§6.3A of the rewrite book).

### Statement

Let J be any real linear operator with J² = −id, and let χ be a real number.
With exp defined by the power series exp(X) = Σ Xⁿ/n! and sin, cos by their
power series,

    exp(χJ) = cos χ · id + sin χ · J.

### Proof (definitions first)

J² = −id is given. Split the exponential series into even and odd terms
(termwise regrouping of an absolutely convergent series is exact):

    exp(χJ) = Σ_{n≥0} χⁿJⁿ/n!
            = Σ_{k≥0} χ^{2k}(J²)^k/(2k)! + Σ_{k≥0} χ^{2k+1}J(J²)^k/(2k+1)!
            = Σ_{k≥0} (−1)^k χ^{2k}/(2k)! · id + Σ_{k≥0} (−1)^k χ^{2k+1}/(2k+1)! · J
            = cos χ · id + sin χ · J. ∎

Domain: all real χ; any real operator J with J² = −id. Applied in Book 6 to
J_CHI with J_CHI² = −1 (Book 6, P5). A completed Taylor-series matrix-exponential
run (Book 6 verification, worst disagreement 2.3e-16) corroborates the identity
but is not needed by the proof.

Status: **PROVED** (analytic, complete). Proved-from: the power-series
definitions of exp, sin, cos — modern analytic definitions, not Euclid's
*Elements* propositions (the *Elements* contains no sine, cosine, or circular
measure; Book 6's own proof file declares no Elements proposition is used
deductively, per the Theorem 4.X.P10 no-Euclid-wholesale boundary).

---

## Principle 2 (PROVED) — CHI-orbit double-angle identities

**Source book claim:** Book 6, C7 (§6.3A of the rewrite book).

### Statement

For every real χ, with w_U := cos²χ and w_U♯ := sin²χ:

    w_U + w_U♯ = 1,
    w_U − w_U♯ = cos 2χ,
    2√(w_U · w_U♯) = |sin 2χ|.

Moreover, on the CHI orbit exp(χJ_CHI)(u,0) = cos χ · u ⊕ sin χ · Πu
(Principle 1 with J = J_CHI, Π an isometry, U ⊥ U♯),

    ‖cos χ · u ⊕ sin χ · Πu‖² = ‖u‖²,

i.e. the orbit redistributes the norm between the two copies without creating
or destroying it; χ = 0, π/4, π/2 give one-copy occupancy, equal weight, and
complete transfer, respectively.

### Proof (definitions first)

cos²χ + sin²χ = 1 is used directly (the defining Pythagorean identity of the
trigonometric functions). Then w_U + w_U♯ = cos²χ + sin²χ = 1. The difference
identity cos²χ − sin²χ = cos 2χ and the product identity
2|sin χ cos χ| = |sin 2χ| are the standard double-angle formulas, following
from the addition formulas; hence w_U − w_U♯ = cos 2χ and
2√(w_U w_U♯) = 2|sin χ||cos χ| = |sin 2χ|.

For the norm, by Principle 1, exp(χJ_CHI)(u,0)
= cos χ·(u,0) + sin χ·J_CHI(u,0) = cos χ u ⊕ sin χ Πu.
Since Π is isometric (Book 6, D9) and U ⊥ U♯,
‖cos χ u ⊕ sin χ Πu‖² = cos²χ‖u‖² + sin²χ‖Πu‖² = (cos²χ+sin²χ)‖u‖² = ‖u‖². ∎

Domain: all real χ. Status: **PROVED** (analytic, complete). Proved-from: the
standard definitions of the trigonometric functions (addition and double-angle
formulas) and Principle 1. As with Principle 1, this is modern analytic
mathematics, not a deduction from Euclid's *Elements* — stated plainly rather
than dressed in an invented Euclid citation.

---

## Book 6 — Local Symmetry and Carrier Mathematics (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book6_proof.md`
(claim inventory C1–C26 plus the status/closure row; rewrite page
`~/workspace/r-theory-rewrite/book6/index.html` — *Book 6 — Local Symmetry
and Carrier Mathematics*).

### Evaluated claims summary

27 claims evaluated: **22 PROVED**, **2 CHECKED**, **1 ASSERTED**,
**0 INCOMPLETE** (no computation failed or timed out; the boundary items —
Elements 6.1–6.33 not extended, χ_CHI dynamics, physical selectors — are
INCOMPLETE-as-extension: deliberate, not failed), plus **1 ST** (C8,
representation-theoretic commutant fact imported as a standard theorem, not
re-derived).

The book's proved claims are block-group Lie theory (O(2)×O(3), U(2)×U(3),
S(U(2)×U(3))), exterior-algebra dimensions, complex/Hermitian/symplectic
linear algebra, combinatorics, and Euclidean simplex geometry — established
mathematics but none of it trigonometric except in two places. Forced folding
was refused; the claim-by-claim table with verdicts is in `book6_claims.md`
(status: complete).

### New Principles added: two

- **Principle 1** (PROVED): the operator Euler formula
  exp(χJ) = cos χ · id + sin χ · J for J² = −id — from C6, the first genuine
  trigonometric identity of the campaign beyond the seed. Proved analytically
  from the power-series definitions.
- **Principle 2** (PROVED): the CHI-orbit double-angle identities
  (cos²χ+sin²χ = 1, cos²χ−sin²χ = cos 2χ, 2√(w_U w_U♯) = |sin 2χ|) and orbit
  norm preservation — from C7. Proved from the trig addition/double-angle
  formulas and Principle 1.

Highest Principle number is now **P2**. The provenance of both principles is
modern analytic mathematics (power-series definitions of sin/cos/exp), not
Euclid's *Elements*: the *Elements* contains no sine, cosine, or circular
measure, and Book 6's own proof file declares that no Elements proposition is
used deductively in it (Theorem 4.X.P10 boundary). Nothing was invented to
make them look Euclidean.

---

## Book 4 — The Flower's angles: exact 30°/60° values and the oblique isometry (evaluated 2026-09-22)

**Sources read:** `~/workspace/euclid_work/books/book4_proof.md` (claim
inventory + proofs), `~/workspace/r-theory-rewrite/book4/index.html`
(*Book 4 — Geometric Rank, Coframes, and Connection*),
`~/workspace/euclid_work/ledger/book4_ledger.md`; Euclid citations
cross-verified in `book1_ledger.md` and `book2_ledger.md`.

**Numbering note.** The register carries several numbering schemes (bare
0–25, plus "(Book N)"-qualified rows, plus book-local P-schemes used inside
individual chapters). The bare ids 26 and 27 are already taken by
"26 (Book 13)"/"27 (Book 13)" register rows and by a book-local P-scheme in
the Book 17 chapter, so this chapter registers its two new principles with
the qualified ids **26 (Book 4)** and **27 (Book 4)** — unique register ids
that cannot collide with any existing row or chapter-local reference. No
other chapter was renumbered or rewritten.

### Evaluated claims summary

25 load-bearing inventory claims: **22 PROVED** (E1, L1, P0, DC, C1, C2, R1,
ISO, M1, M2, T0, A1, A2, A3, A4, K1, K2, O1, O2, O3, NW, NN — each relative
to the declared premises P4.1/P4.1-C/P4.2-L etc.), **2 CHECKED-only exact
runs** (T1 tetrahedral Gram cluster; T2 12-shell + isotropic second moment
Σu_Au_Aᵀ = 4I₃), **1 standard-imported** (A5 Cartan–Bianchi, cited not
re-derived). 8 claims carry completed verification runs: 3 exact clusters run
this campaign (G₂/G₃ Gram cluster; 12-shell + 4I₃ moment; b↔c
orientation-reversing isometry of G₃) and 5 page-reported runs cited, not
re-executed (ISO numeric; A3 symbolic; A4 symbolic; K2 symbolic; O2 numeric).
**15 ASSERTED** items: 10 premise groups (P4.1, P4.1-C, P4.2-L, P4.2-M, P4.3,
P4.4, S1–S6, Gates A–H, the eight-prohibition failure ledger, N1
differential framework) plus 5 asserted ledger records (RC re-presentation
completeness, SUP supplementary diagnostics, P9 gravity firewall, P11
certification + negatives, Projection-scalar ansätze). **19 INCOMPLETE**:
Euclid Defs 4.1–4.7 and Props 4.2–4.5, 4.8–4.9, 4.10–4.14, 4.16 have no R
Theory extension — the extension takes exactly one construction from
Euclid's Book 4, 4.15's sixfold hexagon.

### Definitions (new, cumulative)

- **D-T4.1 (degree measure).** One full turn = 360° (book claim DC,
  definitional). Hence: native sector = 1/6 turn = 60°; half-sector = 30°;
  right angle = 1/4 turn = 90°.
- **D-T4.2 (trig functions on acute angles).** For an acute angle θ in a
  right triangle with hypotenuse c, adjacent leg a, opposite leg b:
  sin θ = b/c, cos θ = a/c, tan θ = b/a. Values at 0° and 90° are limiting
  conventions, not proved here.
- **D-T4.3 (30–60–90 triangle).** The right triangle obtained by halving an
  equilateral triangle along an altitude: hypotenuse 1, acute angles 30°
  and 60°; leg lengths computed in Principle 3.

### Principle 26 (Book 4) (PROVED) — exact trig values at 30° and 60°

**Source book claims:** E1, L1, P0, DC (the R Theory synthetic stratum's
60°/30° content), re-grounded on Euclid 4.15 rather than the ASSERTED
premises P4.1/P4.1-C/P4.2-L — the R Theory premises are not load-bearing here.

**Statement.** sin 30° = 1/2, cos 60° = 1/2, cos 30° = sin 60° = √3/2,
tan 60° = √3, tan 30° = 1/√3.

**Domain:** the acute angles 30°, 60° (D-T4.1).

**Proof.**
1. Euclid 4.15 (book4_ledger: six equilateral triangles about the center;
   recorded dependencies include 3.1, 1.32): the six triangles fill the
   circle, so each central angle is 1/6 of a turn.
2. Each triangle is equilateral. By Euclid 1.5 (book1_ledger: isosceles
   base angles equal — an equilateral triangle is isosceles in every
   pairing) its three angles are equal; by 1.32 (book1_ledger: interior
   angles sum to two right angles) each is ⅓ of two right angles = 60°
   (D-T4.1).
3. Take one equilateral triangle of side 1. Drop the altitude to a side
   (Euclid 1.12, cited in book4_ledger 4.4 row). The two halves have
   hypotenuse 1 = 1 (common), equal base angles (1.5), and equal right
   angles at the foot (1.12); by Euclid 1.26, AAS congruence (cited in
   book4_ledger 4.4 row), the halves are congruent. Hence the base is
   bisected (each half 1/2) and the vertex angle is bisected (each half
   30°, since the whole is 60°).
4. Apply D-T4.2 to either half: sin 30° = (1/2)/1 = 1/2; cos 60° = 1/2.
   By Euclid 1.47 (Pythagoras, cited in book4_ledger 4.12 row), the
   altitude is √(1 − 1/4) = √3/2, so cos 30° = sin 60° = √3/2.
5. tan 60° = (√3/2)/(1/2) = √3 and tan 30° = (1/2)/(√3/2) = 1/√3 by
   division. ∎

**Scope:** PROVED (exact; every Euclid citation verified in the ledgers).

### Principle 27 (Book 4) (PROVED) — oblique-axis isometry: the cosine law at 60° in trig form

**Source book claim:** ISO (Flower⇄Cartesian isometry X = u + v/2,
Y = (√3/2)v ⇒ X² + Y² = u² + uv + v² — proved exactly in the book; the
page's 20,000-sample numeric re-verification is cited, not re-executed,
and not needed by the proof).

**Statement.** Let e₁, e₂ be unit axes meeting at 60°, and w = u·e₁ + v·e₂
with u, v ∈ ℝ. Then |w|² = u² + uv + v²; equivalently, in the orthonormal
frame with components X = u + v/2, Y = (√3/2)v,

    X² + Y² = u² + uv + v²,

where the cross term uv = 2uv·cos 60°.

**Domain:** all real u, v.

**Proof.** By Principle 26 (Book 4), cos 60° = 1/2 and sin 60° = √3/2. The component
of v·e₂ along e₁ is v·cos 60° = v/2, and perpendicular to e₁ it is
v·sin 60° = (√3/2)v. Hence w has orthonormal components X = u + v/2 and
Y = (√3/2)v, and by Euclid 1.47 (Pythagoras),

    |w|² = X² + Y² = (u + v/2)² + (√3v/2)² = u² + uv + v²,

by direct expansion — exact algebra, zero rounding. ∎

**Scope:** PROVED (exact algebra from Principle 26 (Book 4) + Euclid 1.47).

### Book 4 claims not folded in, and why

- **DC:** definitional arithmetic (360/4 = 90, 360/6 = 60); used in D-T4.1,
  but no trig identity — not folded as a principle.
- **C1, C2, R1** (coframe criterion, negative coframe theorem, rank
  obstruction): multilinear algebra / one-variable calculus; no trig content.
- **M1, M2** (Sylvester positive-definiteness, nondegenerate coframe
  metrics): linear algebra; no trig content.
- **T0, T1, T2** (tetrahedron construction, Gram cluster, 12-shell + 4I₃):
  exact Gram/lattice algebra; their only angle content is the 60° faces
  already established in Principle 3.
- **A1–A4** (anholonomy identity, pure-gauge flatness, one-generator
  flatness, flat anholonomic example): wedge/differential algebra; no trig
  functions used.
- **K1, K2** (curvature without spacetime; h_H curvature law): a structural
  definition and a structure-equation computation; no trig content.
- **O1, O2, O3** (orientation classes, volume transformation law,
  orientation nonselection): group theory / multilinear algebra.
- **NW, NN** (no-Euclid-wholesale, no-novelty-from-coordinate-change):
  structural meta-theorems about the declared premises.
- **P4.1, P4.1-C, P4.2-L, P4.2-M, P4.3, P4.4, S1–S6, Gates A–H, failure
  ledger, N1:** ASSERTED substrate — admitted premises, never trig results;
  assertions cannot found principles.
- **RC, SUP, P9, P11, Projection ansätze:** asserted ledger records
  (P9 is a disciplinary boundary declaration, not a theorem).
- **A5, Sylvester, Levi–Civita, Cartan–Bianchi:** standard imported
  theorems, cited not re-derived.
- **19 Euclid items (Defs 4.1–4.7; Props 4.2–4.5, 4.8–4.9, 4.10–4.14,
  4.16):** INCOMPLETE — no R Theory extension exists; nothing to fold.

### Chapter status

**Complete.** Folded from Book 4: **Principle 26 (Book 4)** and **Principle
27 (Book 4)**. Claim-by-claim table: `book4_claims.md` (status: complete).


## Book 0 — Source Boundary and the Orientation Question (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book0_proof.md`
(claim inventory: 43 PROVED, 0 CHECKED, 10 ASSERTED groups, 0 INCOMPLETE;
rewrite page `~/workspace/r-theory-rewrite/book0/index.html` — *Book 0 —
Source Boundary and the Orientation Question*). No proposition of Euclid's
*Elements* is a premise of any proof below (the book's own honest boundary,
kept); every principle is proved from P0, earlier principles of this
chapter, or ordinary background mathematics (M0: real analysis,
trigonometry, elementary topology, linear algebra), in strict dependency
order.

### Evaluated claims summary

Every claim was restated and its proof verified against
`book0_proof.md`. Of the 43 PROVED claims, 16 yield genuine trigonometric
principles and are folded in below as P1–P16. Claim 3.1 is the Seed itself
in the book's notation (`urx + uxp = 4/sin(2x)`) — already registered as P0,
so no new principle was created for it. The remaining 26 proved claims are
established mathematics (rank firewall, complex-structure classification,
simplicial boundary operators, Clifford presentations, the automorphism
obstruction theorem and its applications, topological obstructions,
regularity facts) but contain no identity, lemma, or exact relation about
trigonometric functions, angles, or circular measure — they are recorded in
`book0_claims.md` with their reasons and were not forced in. The 10
ASSERTED groups (A1 sign-fixture history, A2 T0.III essay theorems, A3–A7
T1/T2/T3 audit dispositions, A8 audit completeness, A9 0.IV corollary
caveats, A10 M5 boundary declaration) cannot found principles.

### P1 — Folded Pythagorean identities (from Claim 1.2)

**Statement.** On `D = ℝ \ {kπ/2 : k ∈ ℤ}`, with
`srx = |csc x| + cot x`, `sxp = |csc x| − cot x`,
`cxp = |sec x| + tan x`, `crx = |sec x| − tan x`:
`srx·sxp = 1` and `cxp·crx = 1`.

**Proof.** `srx·sxp = |csc x|² − cot²x = csc²x − cot²x = 1` (M0: the
Pythagorean identity `csc² − cot² = 1`); likewise
`cxp·crx = sec²x − tan²x = 1`. Hence `sxp = 1/srx`, `crx = 1/cxp`. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P2 — Positivity of the folded primitives (from Claim 1.1)

**Statement.** On `D`, `srx, sxp, cxp, crx` are all strictly positive.

**Proof.** The Seed's positivity argument (P0): with
`A = cxp = tan x + |sec x|` and `B = srx = cot x + |csc x|`,
`A ≥ |sec x| − |tan x| = (1 − |sin x|)/|cos x| > 0` (since `cos x ≠ 0`
implies `|sin x| < 1`), and
`B ≥ |csc x| − |cot x| = (1 − |cos x|)/|sin x| > 0`. By P1,
`sxp = 1/srx > 0` and `crx = 1/cxp > 0`. ∎

**Scope:** PROVED. **Depends on:** P0, P1.

### P3 — Symmetry laws of the folded primitives (from Claims 1.4, 1.5, 1.6)

**Statement.** On `D`:
(a) `srx(−x) = sxp(x)`, `cxp(−x) = crx(x)` (and vice versa);
(b) `srx(x−π/2) = crx(x)`, `cxp(x−π/2) = sxp(x)`;
(c) all four primitives are π-periodic.

**Proof.** (a) `|csc(−x)| = |csc x|`, `cot(−x) = −cot x` (M0 parity).
(b) `csc(x−π/2) = −sec x`, `cot(x−π/2) = −tan x`, so
`srx(x−π/2) = |−sec x| − tan x = crx(x)`; similarly
`cxp(x−π/2) = |−csc x| − cot x = sxp(x)`.
(c) `|csc(x+π)| = |csc x|`, `cot(x+π) = cot x` (likewise sec/tan), so the
quartet factors through `ℝ/πℤ` — it cannot recover phase modulo 2π. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P4 — Local generator rational recovery (from Claim 2.1)

**Statement.** Fix an open quadrant, set `z = srx`, `ε = sgn(z−1)`. Then
`sxp = 1/z`, `cxp = (z+ε)/(εz−1)`, `crx = (εz−1)/(z+ε)`.

**Proof.** By P1, `sxp = 1/z`. From P0's Lemma 2 with `B = z`:
`z − 1/z = 2 cot x`, so with `t = tan x`, `t = 2z/(z²−1)` (`z = 1` is
impossible on `D`: it would give `cot x = 0`, i.e. `cos x = 0`, a seam).
`cxp = 1/|cos x| + tan x = √(1+t²) + t` (M0: `1/cos²x = 1 + tan²x`,
`1/|cos x| > 0`). Substituting `t`:
`cxp = (z²+1)/|z²−1| + 2z/(z²−1)`; since `z > 0` (P2),
`sgn(z²−1) = sgn(z−1) = ε`, giving `cxp = [ε(z²+1)+2z]/(z²−1)`.
Cross-multiplication verifies `[ε(z²+1)+2z](εz−1) = (z+ε)(z²−1)`
(both expand to `z³ + εz² − z − ε`), i.e. `cxp = (z+ε)/(εz−1)`.
The denominator is nonzero on `D` (`εz − 1 = 0` would need `z = 1`).
`crx = 1/cxp` by P1. ∎

**Scope:** PROVED. **Depends on:** P0, P1, P2.

### P5 — Riccati generator law (from Claim 2.2)

**Statement.** On each open quadrant, `z = srx` satisfies
`z′ = −(1+z²)/2`, and the rational function field `ℝ(z)` is closed under
`d/dx`.

**Proof.** With fixed quadrant signs `σ_s = sgn(sin x)`,
`z = (σ_s + cos x)/sin x = (1 + σ_s cos x)/(σ_s sin x)` (definitions).
Differentiating: `z′ = −(1 + σ_s cos x)/sin²x`. Meanwhile
`(1+z²)/2 = (sin²x + (1+σ_s cos x)²)/(2sin²x)
= (2 + 2σ_s cos x)/(2sin²x) = (1 + σ_s cos x)/sin²x`,
so `z′ = −(1+z²)/2`. For any `r ∈ ℝ(z)`,
`dr/dx = r_z(z)·z′ ∈ ℝ(z)`. ∎

**Scope:** PROVED. **Depends on:** M0, P2 (positivity for the stated form).

### P6 — FlatWave identity (from Claim 4.1)

**Statement.** On `D`, with `urx = srx − crx`, `uxp = cxp − sxp`:
`1/urx + 1/uxp = sgn(sin 2x)`.

**Proof.** Put `p̃ = 1/|s| − 1/|c|`, `q̃ = s/c + c/s = 1/(sc)`.
Then `urx = p̃ + q̃`, `uxp = −p̃ + q̃` (definitions), so
`urx·uxp = q̃² − p̃² = 1/(s²c²) − (1/s² + 1/c² − 2/|sc|) = 2/|sc|
= 4/|sin 2x|`. By P1, `uxp = cxp − sxp = A − 1/B` and
`urx = srx − crx = B − 1/A`; hence P0 gives `urx + uxp = 4/sin(2x)`.
Therefore `(1/urx + 1/uxp) = (urx+uxp)/(urx·uxp)
= (4/sin 2x)/(4/|sin 2x|) = sgn(sin 2x)`. ∎

**Scope:** PROVED. **Depends on:** P0, P1.

### P7 — FlatWave transformation laws (from Claim 4.2)

**Statement.** With `FW(x) = 1/urx + 1/uxp`:
`FW(x+π/2) = −FW(x)`, `FW(x+π) = FW(x)`, `FW(x+2π) = FW(x)`.

**Proof.** By P6, `FW(x) = sgn(sin 2x)`. M0:
`sgn(sin(2x+π)) = −sgn(sin 2x)` (cophase reversal),
`sgn(sin(2x+2π)) = sgn(sin 2x)` (half-turn invariance), and hence
`FW(x+2π) = FW(x)` (deck-blindness). ∎

**Scope:** PROVED. **Depends on:** P6, M0.

### P8 — Common-sign law (from Claim 4.3)

**Statement.** On `D`: `urx·uxp = 4/|sin 2x| > 0` and
`sgn(urx) = sgn(uxp) = sgn(sin 2x) =: ε_FW`.

**Proof.** From P6's computation, `urx·uxp = 4/|sin 2x| > 0`, so `urx`
and `uxp` share a sign; from P0, `urx + uxp = 4/sin(2x)`, so that common
sign is the sign of `sin(2x)`. ∎

**Scope:** PROVED. **Depends on:** P0, P6.

### P9 — Harmonic carrier ellipse (from Claim 5.1)

**Statement.** With `H = 1/(urx+uxp)` and `V = H′`:
`H = sin(2x)/4`, `V = cos(2x)/2`, and `V² + 4H² = 1/4`.

**Proof.** `H = sin(2x)/4` by P0 (inverting the sum); differentiating
(M0), `V = dH/dx = cos(2x)/2`. Then
`cos²(2x)/4 + 4·sin²(2x)/16 = (cos²(2x) + sin²(2x))/4 = 1/4`. ∎

**Scope:** PROVED. **Depends on:** P0, M0.

### P10 — Transfer-circle identity (from Claim 6.1)

**Statement.** Fix an open quadrant; with `α = σ_s`, `β = σ_c`,
`p = α cos x − β sin x` and `q = α sin x + β cos x = |sin x| + |cos x|`:
`p² + q² = 2`.

**Proof.** `p² = cos²x + sin²x − 2αβ sin x cos x`,
`q² = sin²x + cos²x + 2αβ sin x cos x` (using `α² = β² = 1`); the sum is
`2(sin²x + cos²x) = 2` (M0). ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P11 — Differential transfer closure (from Claim 6.2)

**Statement.** Quadrant-locally, with `λ = (1−p)/2`:
`λ′ = q/2`; `λ″ + λ = 1/2`; `(1−2λ)² + 4(λ′)² = 2`.

**Proof.** `p′ = −α sin x − β cos x = −q`, so
`λ′ = −p′/2 = q/2`. `q′ = α cos x − β sin x = p`, so
`λ″ = q′/2 = p/2` and `λ″ + λ = p/2 + (1−p)/2 = 1/2`.
Finally `(1−2λ)² + 4(λ′)² = p² + q² = 2` by P10. ∎

**Scope:** PROVED. **Depends on:** P10, M0.

### P12 — Sharp phase-rate bounds (from Claim 6.3)

**Statement.** On each open quadrant: `1/2 < λ′ ≤ 1/√2`; the upper bound
is attained exactly at the unique midpoint `λ = 1/2`, where
`Ω = λ/(1−λ) = 1` and `χ = (1−λ)/λ = 1`.

**Proof.** `λ′ = q/2` (P11) with `q = |sin x| + |cos x|`.
`q² = 1 + 2|sin x cos x| = 1 + |sin 2x|`; on `D`,
`0 < |sin x cos x| ≤ 1/2` (M0: AM–GM on `sin²x, cos²x`), with equality
iff `|sin x| = |cos x|`, i.e. `p = ±(|cos x| − |sin x|) = 0`, i.e.
`λ = 1/2`. Hence `1 < q ≤ √2` and `1/2 < λ′ ≤ 1/√2`. At `λ = 1/2`,
`Ω = (1/2)/(1/2) = 1`, `χ = 1`. ∎

**Scope:** PROVED. **Depends on:** P11, M0.

### P13 — Equal-and-opposite saw derivatives (from Claim 6.4)

**Statement.** Quadrant-locally, `saw_r′ + saw_x′ = 0`, where
`saw_r = 1/urx`, `saw_x = 1/uxp`.

**Proof.** `saw_r + saw_x = 1/urx + 1/uxp = sgn(sin 2x)` (P6), which is
constant on each open quadrant (the sign of `sin 2x` cannot change without
crossing a seam); the derivative of a locally constant function is 0.
(Definitional consequence, not a conservation law.) ∎

**Scope:** PROVED. **Depends on:** P6.

### P14 — Cross-layer ratio (from Claim 6.6)

**Statement.** On `D`:
`Ω = λ/(1−λ) = saw_r/saw_x = uxp/urx = cxp/srx`.

**Proof.** `saw_r/saw_x = (1/urx)/(1/uxp) = uxp/urx`. By P8, `saw_r` and
`saw_x` share the sign `ε_FW`, and `|saw_r| + |saw_x| = |sgn(sin 2x)| = 1`
(P6); with `|saw_r| = λ`, `|saw_x| = 1−λ` this gives
`saw_r/saw_x = λ/(1−λ)`. Finally
`uxp/urx = (A − 1/B)/(B − 1/A) = ((AB−1)/B)/((AB−1)/A) = A/B = cxp/srx`
(using P1), valid since `urx·uxp = 4/|sin 2x| ≠ 0` (P8) implies
`urx ≠ 0` and `AB ≠ 1` on `D`. ∎

**Scope:** PROVED. **Depends on:** P1, P6, P8.

### P15 — Reciprocal-even normalization (from Claim 6.7)

**Statement.** On `D`:
`E_D = 1/(srx+sxp+cxp+crx) = |sin 2x|/(4(|sin x| + |cos x|))`, and the
normalized primitives `n_i = prim_i/(srx+sxp+cxp+crx)` satisfy `n_i ≥ 0`,
`Σ n_i = 1`.

**Proof.** By P1, `srx + sxp = 2|csc x|` and `cxp + crx = 2|sec x|`;
their sum is `2(|sin x| + |cos x|)/(|sin x||cos x|)`. The reciprocal is
`|sin x||cos x|/(2(|sin x|+|cos x|))`, and `|sin x||cos x| = |sin 2x|/2`
(M0). Nonnegativity follows from P2. ∎

**Scope:** PROVED. **Depends on:** P1, P2, M0.

### P16 — Log representation (from Claim 6.8)

**Statement.** On `D`: `cxp = e^{asinh(tan x)}` and
`srx = e^{asinh(cot x)}` exactly.

**Proof.** M0: `e^{asinh t} = t + √(1+t²)`. With `t = tan x`,
`√(1+tan²x) = |sec x|`, so `e^{asinh(tan x)} = tan x + |sec x| = cxp`;
with `t = cot x`, `√(1+cot²x) = |csc x|`, giving `srx`. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### What was not folded, and why

- Claim 3.1 (`urx + uxp = 4/sin(2x)`): not folded — it is P0 itself in
  the book's notation, already registered.
- Claims 1.3, 5.2 (quadrant-local smoothness; smooth seam extension of H):
  verified PROVED, but they are regularity/analysis facts, not identities
  about trig functions; the formulas they concern are already P3/P9.
- Claim 5.3 (no continuous injective `S¹ → ℝ`): verified PROVED, but
  general topology, not trigonometry.
- Claims 7.1–7.4 (rank firewall), 8.1–8.3 (real linear lift, `J² = −I`,
  orientation-relative uniqueness, conjugacy classification), 9.1–9.6
  (tetrahedral Gram rank, `O(G)` orientation-reversing isometries,
  `D₁D₀ = D₂D₁ = 0`, central-sign nonselection, Clifford presentations,
  affine readout sign): verified PROVED, but they are linear algebra,
  group/set theory, simplicial homology, and matrix-algebra facts — not
  trig identities. (The Riccati differential content of 8.1 is folded as
  P5; the `J`-algebra is not a statement about trig functions.)
- Theorem 0.IV.T1 (automorphism obstruction) and its T2/T3 applications:
  verified PROVED, but an automorphism/naturality argument, not a trig
  identity.
- 0.III.T1 items (1)–(5) and C1 (representation-proved summaries):
  verified PROVED, but they summarize folded facts rather than adding new
  trig content; the theorem's "therefore" inherits ASSERTED status (A8).
- The M5 conditional block (Axiom-0-conditional complex structure on W,
  dimensions 10/5): verified PROVED-conditional, but conditional on the
  asserted Axiom 0 and not a trig relation.
- Claim 6.5 (`Ωχ = 1`, `χ = R_λ − 1`, `Ω = U_λ − 1`): verified PROVED, but
  pure algebra from the definitions — no trig content.
- ASSERTED groups A1–A10: historical/editorial (A1), inherited essay
  theorems (A2), audit methodology and dispositions (A3–A7), audit
  completeness (A8), corollary caveats (A9), boundary declaration (A10) —
  assertions cannot found trigonometric principles.

Claim-by-claim table with verdicts: `book0_claims.md` (status: complete).

### New Principles added: 16

Highest Principle number is now **P16**. The register above is updated;
earlier chapters (seed, Book 5) are untouched. Per-book counts: 53 claims
evaluated (43 PROVED, 10 ASSERTED, 0 CHECKED, 0 INCOMPLETE); 16 folded as
new Principles P1–P16, all PROVED; 37 not folded (1 already P0, 26 proved
non-trig claims, 10 asserted groups).

## Book 10 — Quantum Kinematics and the Measurement Boundary (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book10_proof.md` (claim inventory C1–C14
with proofs; rewrite page `~/workspace/r-theory-rewrite/book10/index.html` —
*Book 10 — Quantum Kinematics and the Measurement Boundary*).

**Euclid contact (negative, recorded).** The book's own audit verified by full-text
search of rewrite books 0–22 that no R Theory claim extends any proposition of
Euclid's Book 10 (10.1–10.115); the real continuum is the declared substrate P4.1,
not constructed à la Euclid. Under the No-Euclid-wholesale boundary (4.X.H) only
the cited items below enter the cumulative proof.

### Evaluated claims summary

Fourteen claims restated and verified against `book10_proof.md`; the scope labels
are inherited from that worker's file and re-checked against the rewrite page.

- **C1.** 10.II.T1 — projective-rank obstruction (ℂP¹ chart rank 2 vs meridian
  rank 1) — **PROVED**. Dimension/rank argument; no trig content. Not folded.
- **C2.** 10.II.C1 — q alone selects a 1-dim subfamily or silently supplies a
  phase rule — **PROVED** (corollary of C1). Not folded.
- **C3.** 10.III.P1 — free-Dirac import; ratio identities
  pc/(E+mc²) = √((E−mc²)/(E+mc²)) = tanh(α/2) — import (ASSERTED premise);
  identities **CHECKED** by the book worker. Exact algebraic content folds in as Principles 2 and 4 (Book 10) (4 conditional on the import).
- **C4.** 10.III.PC1 — rapidity-contract identification q = sxp — **ASSERTED**
  (declared contract). No trig content. Not folded.
- **C5.** 10.III.T1 — exact free-spinor ratio correspondence (conditional on
  C3+C4) — **CHECKED**. Identity content folds in as Principle 1 (Book 10); the physics reading
  stays conditional.
- **C6.** 10.IV.P1 — radial Dirac–Coulomb import; ground-sector constant ratio
  |G/F| = Zα/(1+γ) — import; constant-ratio content **CHECKED** on the analytic
  ground state. No new trig identity; not folded (Principle 1 (Book 10) covers the inversion).
- **C7.** 10.IV.T1 — ground-sector half-angle correspondence |G/F| = tan(x/2) —
  **CHECKED** (conditional on C6). Application of Principle 1 (Book 10) to an imported constant;
  not folded separately.
- **C8.** 10.IV.N1 — no universal constant half-angle for excited states —
  **ASSERTED** (book worker did not re-run the radial-Dirac integrator).
  Delimiting statement; not folded.
- **C9.** 10.V.T1 — Prüfer completion: F = A cos Θ, G = A sin Θ, regular through
  nodes — standard ODE import; reconstruction exact. Polar-form identity folds in
  as Principle 3 (Book 10).
- **C10.** 10.VI.T1 — shared symplectic form: du∧dv = 2·dF∧dG for
  (u,v) = (F−G, F+G) — **PROVED** (exact Jacobian algebra; close to
  definitional per the book's scope note). Wedge linear algebra; not folded.
- **C11.** 10.VII.P1 — left-chiral projector + V–A import — ASSERTED premise.
  Not folded.
- **C12.** 10.VII.N1 — chirality not selected upstream — **ASSERTED**
  (structural observation about the chain, not an impossibility proof). Not folded.
- **C13.** 10.VIII.N1 — representation does not imply measurement ontology —
  **ASSERTED** (same scoping). Not folded.
- **C14.** 10.IX closure; Δ_op(Book 10) = ∅ — **ASSERTED** (status
  bookkeeping). Not folded.

Full claim-by-claim table: `book10_claims.md` (status: complete).

### New Principles: 1 (Book 10) – 4 (Book 10)

**Principle 1 (Book 10) (PROVED) — Half-angle inversion.** *Statement.* For x ∈ (0, π) and
r ∈ (0, ∞): r = tan(x/2) ⟺ x = 2·arctan(r); tan(x/2) is the bijection
(0,π) → (0,∞) with inverse 2·arctan. *Domain:* x ∈ (0,π), r ∈ (0,∞).
*Proof (definitions first).* arctan is defined (standard background
mathematics) as the inverse of tan restricted to (−π/2, π/2), hence bijective
there by definition. For x ∈ (0,π), x/2 ∈ (0,π/2) ⊂ (−π/2,π/2), so
arctan(tan(x/2)) = x/2 exactly (inverse-of-inverse); doubling gives
x = 2·arctan(tan(x/2)). ∎ *Book claim:* C5 (10.III.T1) — its exact identity
content; the spinor/rapidity reading is not claimed.

**Principle 2 (Book 10) (PROVED) — Hyperbolic half-angle identity.** *Statement.*
tanh(α/2) = sinh α/(cosh α + 1) for all real α. *Domain:* α ∈ ℝ (denominator
2·cosh²(α/2) > 0 everywhere). *Proof (definitions first, in the seed's Lemma
style).* From exponential definitions:
sinh(α/2) = (e^{α/2} − e^{−α/2})/2, cosh(α/2) = (e^{α/2} + e^{−α/2})/2. Then
sinh α = 2·sinh(α/2)·cosh(α/2) (multiplying out gives (e^α − e^{−α})/2), and
cosh²(α/2) = (e^α + 2 + e^{−α})/4 = (cosh α + 1)/2. Hence
sinh α/(cosh α + 1) = [2·sinh(α/2)cosh(α/2)] / [2·cosh²(α/2)]
= sinh(α/2)/cosh(α/2) = tanh(α/2), by the definition tanh := sinh/cosh. Exact
algebra; no sampling needed. ∎ *Book claim:* C3 (10.III.P1) — its exact
algebraic content; the Dirac theory itself stays a named import.

**Principle 3 (Book 10) (PROVED) — Prüfer polar form.** *Statement.* For real (F, G) ≠
(0,0): with A := √(F²+G²) > 0 there is a unique (mod 2π) angle Θ with
(F,G) = A·(cos Θ, sin Θ); where F ≠ 0, tan Θ = G/F; Θ stays defined through
sign changes of F or G (at a node of F, Θ = ±π/2 is defined while G/F is
singular). *Domain:* (F,G) ∈ ℝ² \ {(0,0)}. *Proof (definitions first).*
(cos Θ, sin Θ) is defined as the unit-circle point at circular angle Θ. By
Euclid 1.47 (book1_ledger.md: "Pythagoras: square on hypotenuse = sum of
squares on the legs"), the point (F/A, G/A) satisfies
(F/A)² + (G/A)² = (F²+G²)/A² = 1 — it lies on the unit circle, so by the
definition of circular angle there is Θ with (F/A, G/A) = (cos Θ, sin Θ),
unique mod 2π. By the seed's definition tan := sin/cos,
tan Θ = sin Θ/cos Θ = G/F wherever F ≠ 0. A > 0 at every nonzero pair, so Θ is
defined at nodes. ∎ *Book claim:* C9 (10.V.T1) — its exact identity content;
the ODE regularity theory stays a standard import.

**Principle 4 (Book 10) (PROVED-conditional) — Mass-shell ratio chain.** *Statement.*
With the imported free-relativistic mass shell E = mc²cosh α, pc = mc²sinh α
(m > 0): pc/(E+mc²) = √((E−mc²)/(E+mc²)) = tanh(α/2). *Domain:* m > 0,
E > mc², p > 0. *Proof (exact algebra from the import + P2).*
(E+mc²)(E−mc²) = m²c⁴(cosh²α − 1) = m²c⁴sinh²α = p²c², i.e. E² − p²c² = m²c⁴.
Then (E−mc²)/(E+mc²) = (E−mc²)²/((E+mc²)(E−mc²)) = (E−mc²)²/(p²c²); taking
square roots of positive quantities, √((E−mc²)/(E+mc²)) = (E−mc²)/(pc)
= pc/(E+mc²) (last step by (E−mc²)(E+mc²) = p²c²). And
pc/(E+mc²) = sinh α/(cosh α + 1) = tanh(α/2) by Principle 2 (Book 10). ∎ *Scope:* the
algebra is exact — PROVED — but the premise (the free-Dirac mass-shell
definitions) is the ASSERTED import I1 from C3, so this principle is
conditional: it may be cited only where I1 is granted. *Book claim:* C3+C5
(10.III.P1/T1).

**Excluded (stated plainly).** The meridian derivative identity
dq/dx = 1/(2cos²(x/2)) and the meridian's strict injectivity (D3/C1's calculus
content) is genuine trigonometry, but its proof route — differentiation — is
neither Euclid's Elements nor an earlier Principle, so it cannot be earned
under this campaign's dependency discipline; it is evaluated in
`book10_claims.md` and not folded. Nothing was forced in.

Principles 1 (Book 10) – 4 (Book 10) are registered (namespaced by book, following the Book 0 convention already in the register).

## Book 9 — Relativity and Gravitation: Conditional Reconstruction (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book9_proof.md`
(claim inventory B9.1a–B9.8 with proofs in dependency order; rewrite page
`~/workspace/r-theory-rewrite/book9/index.html` — *Book 9 — Relativity and
Gravitation: Conditional Reconstruction*).

### Evaluated claims summary

23 claims evaluated: **14 PROVED** (several conditional on the book's
declared projection contracts), **2 CHECKED** (completed SymPy runs,
2026-09-22 PDT, residuals exactly 0), **8 ASSERTED** (declared imports,
external calibration, manuscript assertions, closure bookkeeping),
**0 INCOMPLETE**. The claim-by-claim table with verdicts is in
`book9_claims.md` (status: complete).

- **§9.1 Local Lorentz witness.** B9.1a reciprocal-product identities
  s_rx·s_xp = c_xp·c_rx = 1 — **PROVED**. Its trigonometric content is
  already registered as Principle "1 (Book 0)" (the register row whose
  proved-from is the Pythagorean identities csc²−cot² = 1, sec²−tan² = 1);
  not re-folded. B9.1b Lorentz-weight identities, B9.1c boost weights
  (c_xp = e^η, c_rx = e^{−η}), B9.1d mass-shell factorization — each
  **PROVED conditional on the asserted relativistic projection contract
  D-RP**; not folded: they are correspondences between the trigonometric
  primitives and relativistic physics variables (p, E, m, c) under an
  asserted contract, not pure theorems about trigonometric functions.
- **§9.2 Rank and curvature firewall.** B9.2a coframe-rank obstruction,
  B9.2b fixed-generator pure gauge (R = 0 for ω = K·dη), B9.2c
  contrapositive — all **PROVED**; real linear algebra and differential
  forms, no trigonometric content. Not folded.
- **§9.3 Reciprocal half-weight theorem.** B9.3a half-weight hyperbola
  (uv = 1, E_r²−O_r² = 4) — **PROVED**; pure algebra in defined symbols.
  Not folded. B9.3b defect identities (N = (1−q)/(1+q), r(1−N²) = 4a) —
  **PROVED conditional on D-HR**; algebra in the chart variables.
  Not folded. B9.3c reciprocal-defect identity — **PROVED** (conditional
  on the D-RP branch + D-HR in the book file); the trigonometric core is
  a pure identity on sin χ, cos χ > 0 and is folded below as
  **Principle 17**, where it stands PROVED with no physics contract.
- **§9.4 Vacuum Einstein first-integral theorem.** B9.4a metric and B9.4b
  vacuum reduction — **ASSERTED** standard imports; B9.4c first-integral
  equivalence (d[r(1−f)]/dr = 0 ⟺ rf′+f−1 = 0) — **PROVED** (calculus,
  not trigonometry); B9.4d Schwarzschild form — **PROVED conditional on
  the external calibration D-CAL** (a = GM/(2c²), ASSERTED). Not folded.
- **§9.5 Reciprocity on shell.** B9.5a on-shell selection of AN = 1 —
  **CHECKED** (SymPy identity G^r_r − G^t_t = 2(NA)′/(rNA³), residual
  exactly 0) + **ASSERTED** vacuum-equation import; B9.5b boundary-term
  collapse — **CHECKED** (SymPy, residual exactly 0). General-relativity
  identities, not trigonometry. Not folded.
- **§9.6 Sourced transfer.** B9.6a chart inversion, B9.6b radial-strain
  variable — **PROVED** (conditional on D-CH / B9.5a); chart algebra.
  Not folded. B9.6c Poisson recovery, B9.6d static-dust obstruction —
  **ASSERTED** manuscript claims, not independently verified; explicitly
  not earned, not folded.
- **§9.7 Torsion and spin boundary.** B9.7a, B9.7b — **ASSERTED** standard
  GR imports. Not folded.
- **§9.8 Closure ledger.** B9.8 — **ASSERTED** audit bookkeeping; the
  book's certified/conditional/not-derived lists are consistent with the
  audit. Not folded.

**Euclid boundary.** No proposition of Euclid's *Elements* is a logical
premise of Principle 17 or of any Book 9 claim. The Euclid Book 9 ledger
(`~/workspace/euclid_work/ledger/book9_ledger.md`) records 36
number-theoretic propositions (infinitude of primes 9.20, perfect numbers
9.36, unique factorization 9.14, parity arithmetic 9.21–9.34); R Theory's
extension mapping on them is null (book9_proof.md §0). Rewrite Book 9 is a
conditional reconstruction on the modern substrate, not a continuation of
Euclid's arithmetic program — stated plainly, not dressed in invented
Euclid citations.

### New Principle added: one

## Principle 17 (PROVED) — reciprocal-defect trigonometric identity

**Source book claim:** Book 9, B9.3c (book9_proof.md §9.3).

### Statement

For all real χ with sin χ > 0 and cos χ > 0, define the canonical
primitive q = |csc χ| − cot χ (the s_xp of the book's global conventions).
Then q = (1 − cos χ)/sin χ > 0, and

    (1 − q)/(1 + q) = (1 − sin χ)/cos χ.

### Proof (definitions first)

On the branch sin χ > 0, cos χ > 0 the absolute values drop:
|csc χ| = 1/sin χ, so q = (1 − cos χ)/sin χ. Since cos χ < 1 there
(cos χ = 1 would force sin χ = 0, excluded), q > 0.

Now 1 − q = (sin χ − 1 + cos χ)/sin χ and
1 + q = (sin χ + 1 − cos χ)/sin χ, so

    (1 − q)/(1 + q) = (sin χ + cos χ − 1)/(sin χ − cos χ + 1).

The denominator is strictly positive: sin χ > 0 and 1 − cos χ ≥ 0, with
1 − cos χ = 0 excluded as above; hence no division by zero.
Cross-multiply against (1 − sin χ)/cos χ (cos χ > 0):

    (sin χ + cos χ − 1)·cos χ = sin χ cos χ + cos²χ − cos χ,
    (1 − sin χ)(sin χ − cos χ + 1)
        = (1 − sin²χ) − cos χ(1 − sin χ)
        = cos²χ − cos χ + sin χ cos χ,

using 1 − sin²χ = cos²χ (the Pythagorean identity, registered as the
proved-from basis of Principle "1 (Book 0)"). The two products are equal,
and every denominator is nonzero. ∎

Domain: sin χ > 0, cos χ > 0 (the first-quadrant branch mod 2π).
Remark: on this branch q = tan(χ/2) (standard half-angle), so the identity
reads (1 − tan(χ/2))/(1 + tan(χ/2)) = (1 − sin χ)/cos χ.

Status: **PROVED** (analytic, complete). Proved-from: ordinary
trigonometry on the declared substrate D0, plus the Pythagorean identity
already registered (row "1 (Book 0)" proved-from basis). Dependency order
is respected: Principle 17 cites only register rows with id < 17. No
Elements proposition is used; none is invented.

### Register and chapter notes

- Highest Principle number is now **P17**. The register table gains one
  row, "17 (Book 9)"; no earlier rows or chapters were touched.
- **Register-integrity note (for the reevaluation stage):** the register
  currently carries three separate rows numbered "1" (the unlabeled
  half-angle inversion; "1 (Book 0)" folded Pythagorean identities;
  Book 6's operator Euler formula) and two rows numbered "2" (the
  unlabeled hyperbolic half-angle; Book 6's CHI-orbit identities),
  alongside unlabeled rows 3–4 and rows "1 (Book 0)"–"16 (Book 0)". The
  numbering collisions were introduced by earlier workers; per the
  standing rule they are not renumbered here — Principle 17's id was
  chosen as one above the highest numeric id in use (16), and its proof
  cites register rows by their unambiguous labels. The reevaluation stage
  should normalize the register numbering.

## Book 2 — Canonical R-Operator Calculus (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book2_proof.md`
(claim inventory P1–P74 PROVED, A1–A11 ASSERTED, C1–C12 CHECKED, with proofs;
rewrite page `~/workspace/r-theory-rewrite/book2/index.html` — *Book 2 —
Canonical R-Operator Calculus*; the page's "Established (abridged)" principal
theorems are exactly the claim inventory — nothing extra, nothing missing).

### Evaluated claims summary

97 claims evaluated: **74 PROVED**, **12 CHECKED**, **11 ASSERTED**,
**0 INCOMPLETE**. Verification method: all 74 proofs were read in full
against `book2_proof.md`; the load-bearing algebraic identities were
independently re-derived (P1 reciprocity, P6 half-angle chart, P12–P13
stereographic/double-angle forms, P14–P16 symmetry actions, P21–P23
magnitude/same-phase forms, P28 product identity, P32 FlatWave collapse,
P41–P45 Möbius reduction and fixed points, P49 extraction, P52 harmonic
system, P54 fibers, P58–P61 derivative/antiderivative forms) — all check
out exactly; the analysis/limit arguments (P7–P11, P30, P33–P34, P38, P43,
P50, P55, P62–P64, P66–P67) were checked by reading for domain errors and
circularity — none found. The book's reported numerical re-verification
(129 assertions, all passing, no timeouts) is cited, not re-run, per the
proof-over-sampling rule.

Eight claims yield genuine trigonometric principles not already registered;
they are folded below as **P17–P24**, all PROVED, in dependency order. The
remaining 89 are either already registered (from the Seed P0 or Book 0's
P1–P16), standard background mathematics, book-specific operator machinery
with no general trigonometric content, analysis/limit facts, conventions, or
numerical checks — each recorded with its reason in `book2_claims.md`
(status: complete); nothing was forced in.

On Euclid: no proposition of the *Elements* is a logical premise of any
principle here either. The book-2 ledger
(`~/workspace/euclid_work/ledger/book2_ledger.md`, read in full) documents
that Euclid's Book 2 is geometric area-algebra (2.1–2.14) containing no
trigonometry, and the book file's own §7 records the no-Euclid-wholesale
boundary; inventing an *Elements* citation would violate the standing rule.
The principles below are proved from earlier principles and ordinary
background mathematics (M0: real analysis, trigonometry, calculus), in
dependency order.

### P17 — Half-angle chart forms (from Book 2 P6)

**Statement.** For 0 < x < π (so sin x > 0):
`|csc x| + cot x = cot(x/2)` and `|csc x| − cot x = tan(x/2)`.
For 0 < x < π/2 (so cos x > 0):
`|sec x| + tan x = tan(π/4 + x/2)` and `|sec x| − tan x = tan(π/4 − x/2)`.

**Proof.** On (0,π), `|csc x| = csc x`, and
`csc x + cot x = (1 + cos x)/sin x`. M0:
`1 + cos x = 2cos²(x/2)`, `sin x = 2sin(x/2)cos(x/2)`, so the ratio is
`cot(x/2)`; likewise `(1 − cos x)/sin x = tan(x/2)`.
Cosine channel: `(1 + sin x)/cos x`; with `t = tan(x/2) = sin x/(1+cos x)`
(M0 half-angle), `(1+t)/(1−t) = (1+cos x+sin x)/(1+cos x−sin x)`, and
cross-multiplication against `(1+sin x)/cos x` gives difference
`cos x + cos²x + sin x cos x − 1 − cos x − sin x cos x + sin²x
= cos²x + sin²x − 1 = 0` (M0). Since
`tan(π/4 + x/2) = (1+t)/(1−t)` (M0 angle-sum), the first identity holds;
the minus form is the same computation with `sin x → −sin x`. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P18 — Stereographic (Weierstrass) parametrization (from Book 2 P12)

**Statement.** On each component of `{sin x ≠ 0}`, let
`θ = x − kπ ∈ (0,π)` be the reduced angle and
`z = |csc x| + cot x = cot(θ/2) > 0` (P17). With `σ = sgn(sin x) ∈ {±1}`:
`sin x = σ·2z/(z²+1)`, `cos x = σ·(z²−1)/(z²+1)`.
The sign bit σ is not determined by z alone.

**Proof.** By Book 0 P1, `|csc x| − cot x = 1/z`. Adding/subtracting:
`2|csc x| = z + 1/z`, `2cot x = z − 1/z`. Hence
`|sin x| = 2z/(z²+1)` and `cot x = (z²−1)/(2z)`; with the sign bit,
`sin x = σ·2z/(z²+1)`, and
`cos x = sin x · cot x = σ·(z²−1)/(z²+1)`. ∎

**Scope:** PROVED. **Depends on:** P17, Book 0 P1.

### P19 — Rational double-angle form (from Book 2 P13)

**Statement.** With z as in P18: `sin 2x = 4z(z²−1)/(z²+1)²`, and
`sgn(sin 2x) = sgn(z²−1)`.

**Proof.** `sin 2x = 2 sin x cos x
= 2·σ·2z/(z²+1)·σ·(z²−1)/(z²+1) = 4z(z²−1)/(z²+1)²` (P18, σ² = 1).
Since `z > 0` and `(z²+1)² > 0`, the sign is `sgn(z²−1)`. ∎

**Scope:** PROVED. **Depends on:** P18.

### P20 — Exact octant values (from Book 2 P10, P45)

**Statement.** `tan(π/8) = √2 − 1` and `cot(π/8) = √2 + 1`.

**Proof.** `tan(π/8) = √2 − 1` (M0 exact value);
`(√2−1)(√2+1) = 1`, so `cot(π/8) = 1/(√2−1) = √2+1`.
Equivalently these are the unique admissible fixed points of the branch
maps: `(z+1)/(z−1) = z ⟺ z² − 2z − 1 = 0 ⟺ z = 1+√2` (positive root > 1),
and `(1−z)/(1+z) = z ⟺ z² + 2z − 1 = 0 ⟺ z = √2−1` (positive root in
(0,1)). ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P21 — Harmonic oscillator law (from Book 2 P52)

**Statement.** With `H = sin 2x/4` (Book 0 P9): `H″ + 4H = 0` on ℝ;
equivalently the first-order system `H′ = V`, `V′ = −4H` with
`V = cos 2x/2`.

**Proof.** From Book 0 P9, `V = H′ = cos 2x/2`. Differentiating (M0):
`V′ = −sin 2x = −4H`. Hence `H″ = −4H`. ∎

**Scope:** PROVED. **Depends on:** Book 0 P9, M0.

### P22 — Rational cot double-angle forms (from Book 2 P57)

**Statement.** For `sin x ≠ 0`, `cos x ≠ 0`:
`sin 2x = 2cot x/(1+cot²x)` and `cos 2x = (cot²x−1)/(cot²x+1)`.

**Proof.** `2cot x/(1+cot²x) = 2(cos x/sin x)/(1+cos²x/sin²x)
= 2cos x sin x/(sin²x+cos²x) = sin 2x` (M0);
`(cot²x−1)/(cot²x+1) = (cos²x−sin²x)/(cos²x+sin²x) = cos 2x`. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P23 — Logarithmic antiderivatives (from Book 2 P61)

**Statement.** On each open quadrant, with `z = |csc x| + cot x`:
`∫z dx = −ln(1+z²) + C`. In ordinary trig terms: where `sin(x/2) > 0`,
`∫cot(x/2)dx = 2ln(sin(x/2)) + C`; where `cos(x/2) > 0`,
`∫tan(x/2)dx = −2ln(cos(x/2)) + C`.

**Proof.** By Book 0 P5, `z′ = −(1+z²)/2`. Differentiating (M0 chain
rule): `d/dx[−ln(1+z²)] = −2z·z′/(1+z²) = z`. On (0,π),
`z = cot(x/2)` (P17) and `−ln(1+cot²(x/2)) = −ln(csc²(x/2))
= 2ln(sin(x/2))` for `sin(x/2) > 0`; the tan form is symmetric. ∎

**Scope:** PROVED. **Depends on:** Book 0 P5, P17, M0.

### P24 — Arctan linearization (from Book 2 P60)

**Statement.** On (0,π): `arctan(cot(x/2)) = (π−x)/2` and
`arctan(tan(x/2)) = x/2`. On (0,π/2):
`arctan(tan(π/4+x/2)) = π/4+x/2` and `arctan(tan(π/4−x/2)) = π/4−x/2`.

**Proof.** `d/dx arctan(z) = z′/(1+z²) = −1/2` by Book 0 P5, so
`arctan(z)` is affine with slope −1/2 on each quadrant. On (0,π),
`z = cot(x/2)` (P17); at `x = π/2`, `z = 1` and `arctan 1 = π/4`,
fixing the constant: `arctan(cot(x/2)) = π/2 − x/2 = (π−x)/2`.
Since `tan(x/2) = 1/z`, `arctan(tan(x/2)) = π/2 − arctan(z) = x/2`.
The cosine-channel forms are the same computation on (0,π/2) with the
P17 chart. ∎

**Scope:** PROVED. **Depends on:** Book 0 P5, P17, M0.

### What was not folded, and why

Already registered (duplicates refused):
- P1–P4 (quartet reciprocity, positivity, seam value 1, conjugate
  recovery, |·|-preservation): the trigonometric core is Book 0 P1–P2;
  the P5 counterexample is a definitional audit point, not an identity.
- P18 (half-turn descent): π-periodicity already Book 0 P3(c).
- P25 (double-angle closure sum): P0 (the Seed) itself in book notation.
- P28 (unsigned companion product): Book 0 P8.
- P29 (sign–magnitude relation): corollary of P0 + Book 0 P8.
- P32–P33 (FlatWave binary collapse, quadrant character, period π):
  Book 0 P6–P7.
- P35 (Saw product): reciprocal of Book 0 P8.
- P39 (cross-family equation): algebraic form of Book 0 P6.
- P49 (harmonic extraction, max 1/4): Book 0 P9; extremal values are M0.
- P53 (carrier ellipse, unit circle): Book 0 P9.
- P56 (FlatWave = sgn H): Book 0 P6.
- P59 (autonomous Riccati pairs): Book 0 P5.
- P58 (envelope derivatives): lemma step of Book 0 P5 — no new identity
  beyond the registered Riccati law.

Standard background (M0) — no new trigonometric content:
- P14–P16 (reflection, quarter-turn, complementary-reflection actions),
  P19 (ε transport laws): operator-level claims; the underlying parity,
  shift, and cofunction identities are standard background already
  exercised by Book 0 P3/P7.
- P9 (range law), P11 (octant crossing order): monotonicity of cot —
  analysis, not identities.
- P24 (π/4 checksum), P26 (retired-sign checksum): M0 exact values at a
  point + P0; bookkeeping, not identities.

Book machinery, analysis, meta — not trigonometric identities:
- P5, P7–P8, P10-chart-transport (P7–P8), P17, P20–P23, P27 (reformulation
  of P0 via P19), P30–P31, P34, P36–P38, P40–P44 (Möbius machinery; the
  exact values it yields are folded as P20), P46–P48, P50–P51, P54–P55,
  P57 (carrier-from-z machinery beyond the rational cot forms folded as
  P22), P62–P67 (seam asymptotics and boundary atlas — limits, not
  identities), P70–P74 (complex packaging audit, certification meta).
- P68–P69 (Z_car = e^{2ix}, phasor fibers): Euler formula (M0) + Book 0 P9.
- A1–A11: conventions, stipulations, and audit assertions — assertions
  cannot found principles.
- C1–C12: the book page's reported numerical re-verification of proved
  identities — CHECKED, cited, not re-run, not folded (proof over
  sampling).

Claim-by-claim table with verdicts: `book2_claims.md` (status: complete).

### New Principles added: 8

Highest Principle number is now **P24**. The register above is updated;
earlier chapters (seed, Book 5, Book 6, Book 0) are untouched. Per-book
counts: 97 claims evaluated (74 PROVED, 12 CHECKED, 11 ASSERTED,
0 INCOMPLETE); 8 folded as new Principles P17–P24, all PROVED; 89 not
folded (13 already registered, 53 evaluated with no new trig content,
11 asserted, 12 numerical checks).


## Book 14 — Two-Fermion Mass Geometry and the Spinor Bridge (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book14_proof.md`
(claim inventory: 25 rows — the 24-row table with 14.III.E1 split into its
proved mathematics and its asserted physical caveat; counts PROVED 16 /
CHECKED 1 / ASSERTED 8 / INCOMPLETE 0; rewrite page
`~/workspace/r-theory-rewrite/book14/index.html` — *Book 14 — Two-Fermion
Mass Geometry and the Spinor Bridge*, sections 14.0–14.XIII matching the
proof file's inventory item for item).

Idempotence note: no Book 14 chapter existed in this document before this
append; the highest registered Principle number was P16. This chapter adds
Principles P17–P25. Nothing earlier was renumbered or rewritten.

Euclid-citation note: no proposition of the *Elements* is a premise of any
principle below. All 13 book ledgers (book1_ledger.md .. book13_ledger.md)
were grepped for hyperbolic/half-angle content before any citation was
written — none supplies identities for sinh, cosh, or tanh, which are
post-Euclid analytic substrate. This matches the book proof file's
documented boundary (book14_proof.md §0/§D.1: identities "proved from their
own definitions; no wholesale inheritance of the Elements is claimed") and
the campaign's standing Euclid note in the register. Principles cite only
earlier Principles and definitions, in strict dependency order.

### Evaluated claims summary

Every claim was restated and its proof verified against
`book14_proof.md`. Every proof step used in a folded principle was also
re-verified by independent recomputation (sympy/numpy check script in the
workflow scratch: 17 checks, exit 0, all OK — including the 14.II.T1 and
14.III.T1 numerators, the T2 inversion, the weak-binding and heavy-source
limits, the C1 rewrite and its derivative, the spin-1 expectations at five
angles, the σᵢ⁽²⁾ = Jᵢ lift rule on five random Hermitian K, and the
Q_xz orthogonality witness).

- **14.I.T1** — `q_m = tanh(λ_m/2)`, inverse `m₁/m₂ = (1+q_m)/(1−q_m)` —
  **PROVED**. Folds in as Principle 17.
- **14.I.C1** — `cosh λ_m = (1+q_m²)/(1−q_m²)`,
  `sinh λ_m = 2q_m/(1−q_m²)` — **PROVED**. Folds in as Principle 18.
- **14.I.C2** — `tanh η = 2q/(1+q²)`, `sech η = (1−q²)/(1+q²)`,
  `tanh²+sech² = 1` with `q = tanh(η/2)` — **PROVED**. Folds in as
  Principle 19.
- **14.II.P1** — `p₁·p₂ = m₁m₂ cosh η`,
  `s = m₁²+m₂²+2m₁m₂ cosh η` — **ST** (standard two-particle
  relativistic kinematics, imported, not proved). The exact algebraic
  consequence used is `s/(2m₁m₂) = cosh λ_m + cosh η`, which is exact
  algebra given the import. Not folded by itself: it is an import, not a
  derived trig principle.
- **14.II.T1** — `s/(4m₁m₂) = (1−q_m²q_v²)/((1−q_m²)(1−q_v²))` —
  **PROVED** (conditional on the 14.II.P1 import). Folds in as
  Principle 21.
- **14.II.N1** — "no mass-only rule determines relative velocity/dynamics"
  — **ASSERTED** (manuscript negative, correctly scoped). No trig content;
  not folded.
- **14.III.E1 (mathematics)** — continuation `η = iθ`,
  `cosh η ↦ cos θ = (1−u²)/(1+u²)` with `u = tan(θ/2)` — **PROVED**.
  Folds in as Principle 20.
- **14.III.E1 (physical caveat)** — "the continuation is mathematics; a
  physical bound state needs independent dynamics" — **ASSERTED** (kept
  out of the folded principle).
- **14.III.T1** — `M²/(4m₁m₂) = (1+q_m²u²)/((1−q_m²)(1+u²))`, the
  `q_v² → −u²` substitution — **PROVED**. Folds in as Principle 22.
- **14.III.T2** — `u² = [(m₁+m₂)²−M²]/[M²−(m₁−m₂)²]`, invertible both
  ways — **PROVED**. Not folded: pure algebraic coordinate inversion of
  Principle 22; its trig content is already P22.
- **14.IV exact form** — `u² = B[2(m₁+m₂)−B]/[(2m₁−B)(2m₂−B)]` —
  **PROVED**. Not folded: mass algebra, no trig content.
- **14.IV.T1** — weak binding `u² = B/(2μ) + O(B²)` with explicit monotone
  ratio `R(B) ↗` from 1 — **PROVED**. Not folded: an asymptotic expansion,
  no trig content.
- **14.IV conditional Coulomb check** — `u ≈ Zα/(2n)` — **CHECKED** (the
  book's own NC report, conditional on the imported Coulomb law ST; the
  run file is present but was not re-run here, per the
  proof-over-sampling rule). Not folded: a conditional physics check, not
  a trig identity.
- **14.IV.N1** — "binding is independent data" — **ASSERTED** (manuscript
  negative). Not folded.
- **14.V.T1** — heavy-source limit
  `u² → (m₂−E)/(m₂+E) = tan²(χ_E/2)`, strictly monotone — **PROVED**.
  Not folded: a monotone mass limit; its trig kernel is the half-angle
  identity already in Principles 20/23 — nothing new.
- **14.V.P1** — Dirac–Coulomb `|G/F|² = (m₂−E)/(m₂+E)` on the circular
  branch — **ST** (imported). Not folded.
- **14.V.T2** — `u = |G/F| = sxp(χ_E)` by transitivity, conditional on
  P1 — **PROVED** (conditional). Not folded: transitivity of two
  half-angle constructions; no new trig identity.
- **14.V.N1** — "no extension to excited radial states" — **ASSERTED**
  (manuscript negative). Not folded.
- **14.VI.T1** — `M²/(m₁+m₂)² = ⟨χ_u|K_m|χ_u⟩` — **PROVED**. Not folded:
  an operator identity (linear algebra); its trig content is C1, folded
  as Principle 23.
- **14.VI.C1** — `(1+q_m²u²)/(1+u²) = (1+q_m²)/2 +
  (1−q_m²)cos(2α)/2` with `u = tan α`, derivative
  `−(1−q_m²)sin(2α)` — **PROVED**. Folds in as Principle 23.
- **14.VII.T1** — `cos(2θ_m) = q_m = tanh(λ_m/2)`,
  `sin(2θ_m) = √(1−q_m²) = sech(λ_m/2)` — **PROVED**. Folds in as
  Principle 24.
- **14.VII.D1** — `ν₂(χ_m) = (m₁,√(2m₁m₂),m₂)^T/(m₁+m₂)` — **PROVED**.
  Not folded: Veronese coordinate formula (projective algebra), not trig.
- **14.VII.CL1** — "the Veronese conic does not by itself derive three
  generations" — **ASSERTED** (manuscript clarification). Not folded.
- **14.VIII.T1** — `⟨Φ|K⁽²⁾|Φ⟩ = ⟨χ|K|χ⟩` for general Hermitian-or-not K —
  **PROVED** (analytic, from the definition D8). Not folded: general
  linear-algebra identity, no trig content.
- **14.VIII mass-operator and spin-1 forms** —
  `K_m⁽²⁾ = diag(1,(1+q_m²)/2,q_m²)`; `⟨Φ_u|J_z|Φ_u⟩ = cos(2α)`,
  `⟨Φ_u|J_x|Φ_u⟩ = sin(2α)` — **PROVED**. The spin-1 expectation
  identities fold in as Principle 25; the diagonal `K_m⁽²⁾` form is
  linear algebra and is not folded.
- **14.IX lift rule** — `K⁽²⁾ = k₀I + ½kᵢJᵢ` with
  `σᵢ⁽²⁾ = Jᵢ` verified entry by entry — **PROVED**. Not folded: linear
  algebra, no trig content.
- **14.IX.T1** — one-body lift image exactly `1⊕3`, quadrupole `5` absent
  (conditional on the standard `1⊕3⊕5` decomposition, ST) — **PROVED**
  (conditional). Not folded: representation theory, not trig.
- **14.X–14.XIII, 14.0** — empirical-control ladder, operational-promotion
  audit (`Δ_op(Book 14) = ∅`), closure, retirement/handoff declarations —
  **ASSERTED** (status declarations, correctly scoped). Not folded.

Claim-by-claim table with verdicts: `book14_claims.md` (status: complete).

### New Principles added: P17–P25

#### Principle 17 (PROVED) — tanh half-angle and its inverse

**Source book claim:** 14.I.T1.

**Statement.** For λ real, with `r = e^λ > 0` and `q = tanh(λ/2)`:
`q = (e^λ − 1)/(e^λ + 1) = (r − 1)/(r + 1)`, and inversely
`r = (1 + q)/(1 − q)`.

**Proof (definitions first).** `tanh(λ/2) =
(e^{λ/2} − e^{−λ/2})/(e^{λ/2} + e^{−λ/2})`; multiplying numerator and
denominator by `e^{λ/2}` gives `(e^λ − 1)/(e^λ + 1)`. From
`q = (r − 1)/(r + 1)`: `q(r + 1) = r − 1`, i.e. `r(1 − q) = 1 + q`, so
`r = (1 + q)/(1 − q)` (for `q ≠ 1`). ∎

Domain: λ ∈ ℝ (inverse requires `q ≠ 1`).
Scope: **PROVED**. Depends on: Principle 2
(`tanh(α/2) = sinh α/(cosh α + 1)` — this is its immediate algebraic
consequence, shown equivalently from definitions here).

#### Principle 18 (PROVED) — cosh/sinh in the half-angle tangent

**Source book claim:** 14.I.C1.

**Statement.** For λ real and `q = tanh(λ/2)`: `cosh λ = (1 + q²)/(1 − q²)`,
`sinh λ = 2q/(1 − q²)`.

**Proof.** From Principle 17, `r = (1 + q)/(1 − q)`. Then
`cosh λ = (r + r^{−1})/2 = ½[(1+q)/(1−q) + (1−q)/(1+q)]
= [(1+q)² + (1−q)²]/[2(1−q²)] = (1+q²)/(1−q²)`;
`sinh λ = (r − r^{−1})/2 = [(1+q)² − (1−q)²]/[2(1−q²)] = 2q/(1−q²)`. ∎

Domain: λ ∈ ℝ (`q² ≠ 1`).
Scope: **PROVED**. Depends on: Principle 17.

#### Principle 19 (PROVED) — tanh double-angle and sech

**Source book claim:** 14.I.C2.

**Statement.** For η real and `t = tanh(η/2)`: `tanh η = 2t/(1 + t²)`,
`sech η = (1 − t²)/(1 + t²)`, `tanh²η + sech²η = 1`.

**Proof.** From Principle 18 with λ = η:
`sinh η = 2t/(1−t²)`, `cosh η = (1+t²)/(1−t²)`. Hence
`tanh η = sinh η/cosh η = 2t/(1+t²)` and
`sech η = 1/cosh η = (1−t²)/(1+t²)`. Then
`tanh²η + sech²η = [4t² + (1−t²)²]/(1+t²)²
= (1 + 2t² + t⁴)/(1+t²)² = 1`. ∎

Domain: η ∈ ℝ.
Scope: **PROVED**. Depends on: Principle 18.
Lineage: this is the hyperbolic instance of the campaign seed's
double-angle content — Principle 0's Lemma 1 (`A − 1/A = 2 tan x`) is
its circular counterpart.

#### Principle 20 (PROVED) — circular half-angle rational form

**Source book claim:** 14.III.E1 (mathematics only; the book's physical
caveat is kept out of this principle).

**Statement.** For θ real with `cos(θ/2) ≠ 0` and `u = tan(θ/2)`:
`cosh(iθ) = cos θ = (1 − u²)/(1 + u²)`.

**Proof.** `cosh(iθ) = (e^{iθ} + e^{−iθ})/2 = cos θ` by the definitions of
cosh and cos. And `cos θ = cos²(θ/2) − sin²(θ/2)`; dividing numerator and
denominator by `cos²(θ/2)` gives
`(1 − tan²(θ/2))/(1 + tan²(θ/2)) = (1 − u²)/(1 + u²)`. ∎

Domain: θ ∈ ℝ, `cos(θ/2) ≠ 0`.
Scope: **PROVED**. Depends on: Principle 1 (half-angle inversion — the
`u = tan(θ/2)` parametrization) + definitions.

#### Principle 21 (PROVED, conditional) — two-cosh sum in half-angle parameters

**Source book claim:** 14.II.T1.

**Statement.** Given the imported two-body relation
`s/(2m₁m₂) = cosh λ_m + cosh η` (14.II.P1, ST — not proved here), for
`q_m = tanh(λ_m/2)`, `q_v = tanh(η/2)`:
`s/(4m₁m₂) = (1 − q_m²q_v²)/((1 − q_m²)(1 − q_v²))`.

**Proof.** From the premise, `s/(4m₁m₂) = (cosh λ_m + cosh η)/2`. Insert
Principle 18's form of `cosh λ_m` and the analogous
`cosh η = (1+q_v²)/(1−q_v²)`. Over the common denominator
`2(1−q_m²)(1−q_v²)` the numerator is
`(1+q_m²)(1−q_v²) + (1+q_v²)(1−q_m²) = 2 − 2q_m²q_v²`. ∎

Domain: `m₁, m₂ > 0`, η real, `q_m², q_v² ≠ 1`.
Scope: **PROVED-conditional** — the algebra is exact, but the premise is
the ASSERTED import 14.II.P1, so this principle may be cited only where
that import is granted.

#### Principle 22 (PROVED) — bound-state continuation form

**Source book claim:** 14.III.T1.

**Statement.** For `q_m² ≠ 1` and `u = tan(θ/2)`:
`M²/(4m₁m₂) = (1 + q_m²u²)/((1 − q_m²)(1 + u²))`.

**Proof.** Substituting `q_v² → −u²` in Principle 21's identity gives
`(1 − q_m²(−u²))/((1−q_m²)(1−(−u²))) = (1+q_m²u²)/((1−q_m²)(1+u²))`.
Directly: `M²/(4m₁m₂) = (cosh λ_m + cos θ)/2` (the `cosh η → cos θ`
continuation of Principle 21's premise); inserting Principle 18 and
Principle 20, the numerator over `2(1−q_m²)(1+u²)` is
`(1+q_m²)(1+u²) + (1−u²)(1−q_m²) = 2 + 2q_m²u²`. ∎

Domain: `m₁, m₂ > 0`, below-threshold M, `cos(θ/2) ≠ 0`.
Scope: **PROVED**. Depends on: Principles 21, 20.
(The physical reading "bound state" is asserted by the book and kept out
of this principle; the formula is exact mathematics.)

#### Principle 23 (PROVED) — double-angle Fourier form

**Source book claim:** 14.VI.C1.

**Statement.** For α real with `cos α ≠ 0`, `u = tan α`:
`(1 + q_m²u²)/(1 + u²) = (1 + q_m²)/2 + (1 − q_m²)cos(2α)/2`,
with `d/dα = −(1 − q_m²)sin(2α)`.

**Proof.** `1/(1+u²) = cos²α` and `u²/(1+u²) = sin²α` (definitions, as in
Principle 20), so `(1+q_m²u²)/(1+u²) = cos²α + q_m²sin²α
= (1+cos 2α)/2 + q_m²(1−cos 2α)/2
= (1+q_m²)/2 + (1−q_m²)cos(2α)/2`. Differentiating (M0 real analysis):
`d/dα = −(1−q_m²)sin(2α)`. ∎

Domain: α ∈ ℝ, `cos α ≠ 0`.
Scope: **PROVED**. Depends on: Principle 20 + definitions + M0
differentiation (the Book 0 campaign's background-math symbol, per its
P5 precedent).

#### Principle 24 (PROVED) — mass double-angle bridge

**Source book claim:** 14.VII.T1.

**Statement.** For `m₁, m₂ > 0`, with
`χ_m = (cos θ_m, sin θ_m)^T = (√m₁, √m₂)^T/√(m₁+m₂)` and
`q_m = (m₁−m₂)/(m₁+m₂)`: `cos(2θ_m) = q_m = tanh(λ_m/2)`,
`sin(2θ_m) = √(1−q_m²) = sech(λ_m/2)`.

**Proof.** `cos(2θ_m) = cos²θ_m − sin²θ_m = (m₁−m₂)/(m₁+m₂) = q_m`, and
`q_m = tanh(λ_m/2)` by Principle 17. `sin(2θ_m) = 2 sin θ_m cos θ_m
= 2√(m₁m₂)/(m₁+m₂) = √[4m₁m₂/(m₁+m₂)²]
= √[1 − (m₁−m₂)²/(m₁+m₂)²] = √(1−q_m²)`. And
`sech²(λ_m/2) = 1 − tanh²(λ_m/2) = 1 − q_m²`, so
`sin(2θ_m) = sech(λ_m/2)`. ∎

Domain: `m₁, m₂ > 0`.
Scope: **PROVED**. Depends on: Principle 17 + definitions.

#### Principle 25 (PROVED) — spin-1 Veronese expectation identities

**Source book claim:** 14.VIII spin-1 expectation forms
(the `K_m⁽²⁾` diagonal form is linear algebra and is not folded).

**Statement.** For α real, with `Φ_u = (cos²α, √2 sin α cos α, sin²α)^T`,
`J_z = diag(1,0,−1)`, `J_x = (1/√2)[[0,1,0],[1,0,1],[0,1,0]]`:
`⟨Φ_u|J_z|Φ_u⟩ = cos(2α)`, `⟨Φ_u|J_x|Φ_u⟩ = sin(2α)`.

**Proof.** Φ_u is normalized: its squared entries sum to
`(cos²α+sin²α)² = 1`. `⟨Φ_u|J_z|Φ_u⟩ = cos⁴α − sin⁴α
= (cos²α−sin²α)(cos²α+sin²α) = cos(2α)`. With `a = cos²α`,
`b = √2 sinα cosα`, `c = sin²α`: `J_xΦ_u = (1/√2)(b, a+c, b)`, so
`⟨Φ_u|J_x|Φ_u⟩ = (1/√2)(ab + b(a+c) + cb) = (1/√2)·2b(a+c)
= 2 sinα cosα = sin(2α)` since `a + c = 1`. ∎

Domain: α ∈ ℝ.
Scope: **PROVED**. Depends on: the stated definitions only.

### Look back (Polya)

Nine principles from one book — all exact half-angle / double-angle
machinery in hyperbolic, circular, and spin-1 form. Principle 19 is the
hyperbolic twin of the seed's circular double-angle (Principle 0,
Lemma 1); Principles 20 and 23 carry the circular half-angle rational
form and its Fourier rewrite; Principle 24 is the parameter-free
hyperbolic/circular double-angle bridge. Claims left out are exactly the
ones with no honest trig content: kinematics imports (ST), manuscript
negatives and declarations (ASSERTED), pure algebra (14.III.T2, 14.IV),
representation theory (14.IX), and the conditional physics check
(CHECKED, not re-run).

Highest Principle number is now **P25**.

## Book 17 — The Discrete Octant (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book17_proof.md`
(claim inventory P1–P21, C1–C4, A1–A7, I1–I7 with proofs; rewrite page
`~/workspace/r-theory-rewrite/book17/index.html` — *Book 17 — The Discrete
Octant*, §§17.1–17.8).

### Evaluated claims summary

39 claims evaluated: **21 PROVED**, **4 CHECKED**, **7 ASSERTED**,
**7 INCOMPLETE**. No computation failed or timed out; the seven INCOMPLETE
items are the book page's own exhibited defects (IC-8..IC-11: the §17.18.8.2
skeleton) and three blocked inputs (Frobenius norms, the explicit 1820
projector, the numerical value of S_F) — reproduced as the page's verified
audit, not re-derived by the book worker.

The book's proved claims are the octant/primitive/carrier/rapidity spine
(§§17.1–17.4), the Flatwave identity, the paired footprint (§17.6), and the
T-matrix/conversion-chain algebra (§17.7). Four of them yield genuine
trigonometric principles not already registered; the rest are subsumed by
the register, are definition-unfoldings, finite case checks, non-trigonometric
algebra, or already-established identities:

- **P1** (harmonic carrier) — PROVED; content subsumed by P0 (seed lemmas
  A − 1/A = 2 tan x, B − 1/B = 2 cot x) and register P9
  (H = 1/(urx+uxp) = sin(2x)/4). Not folded — nothing new.
- **P2** (imbalance K₂/(2D₂) = cos(2x)/2) — PROVED; cancels the common
  nonzero factor in the D3 definitions. Not folded — definition-unfolding,
  no new content about angles or circular measure.
- **P3** (elliptic carrier) — PROVED; V_R² + 4H² = 1/4 is register P9, and
  D₂² − K₂² = 16 is direct D3 substitution. Not folded.
- **P4** (octant ordering factorization) — PROVED exact quadrant-local
  algebra; a sign-analysis tool for the primitive difference, not an
  identity about angles or circular measure. Not folded.
- **P5** (active pair) — PROVED finite case analysis via t = tan(x/2); no
  identity. Not folded.
- **P6** (three-bit code) — PROVED finite exhaustion; combinatorics, not
  trigonometry. Not folded.
- **P7** (2:1 elliptic map) — PROVED; **folded as Principle 17**.
- **P8** (IC-1 deck-invariance of ε = sgn(sin 2x)) — PROVED; corollary of
  the π-periodicity inside Principle 17. Folded with it.
- **P9** (rapidity ladder) — PROVED; **folded as Principle 18**.
- **P10** (Flatwave identity) — PROVED; already register P6. Not folded —
  registered.
- **P11** (paired footprint cos 4x) — PROVED; **folded as Principle 19**.
- **P12** (IC-4: zeros at midpoints, ±1 at boundaries) — PROVED; corollary
  folded inside Principle 19.
- **P13** (E-contact interiority) — PROVED finite check. Not folded.
- **P14** (footprint invariance under x → x+π) — PROVED; folded inside
  Principle 19.
- **P15–P19** (S_F / T-matrix / conversion-chain / bound arithmetic) —
  PROVED as linear algebra and arithmetic; no trigonometric content. Not
  folded.
- **P20** (IC-6/IC-7 rep-theoretic corrections) — PROVED representation
  theory; no trigonometric content. Not folded.
- **P21** (§17.8 table read off the carrier formulas) — PROVED algebra;
  the page's V-checks corroborate. Not folded.
- **C1–C4** — CHECKED (the page's own NC/CP/V checks, cited not re-run).
  Not folded.
- **A1–A7** — ASSERTED (C8 correspondence as theorem, code-group clause,
  charge-matching ansatz, contraction physics, open gates). Assertions
  cannot found principles. Not folded.
- **I1–I7** — INCOMPLETE with exact boundaries stated. Not folded.

Claim-by-claim table with verdicts: `book17_claims.md` (status: complete).

### Numbering note (honest)

The principles register table above ends at id 16 (Book 0). The Book 6
chapter in this document headed its two principles "Principle 1" and
"Principle 2", colliding with register rows 1–2; that collision is a
pre-existing artifact and is not renumbered here. New principles below
continue from the register's highest id (16), so no new collision is
created: **P17–P20**.

### New Principles added: four

## Principle 17 (PROVED) — the carrier ellipse 2:1 cover

**Source book claim:** Book 17, P7 (§17.2) with P8 as corollary.

### Statement

For all real x, with V_R(x) = cos(2x)/2 and H(x) = sin(2x)/4:

    (V_R(x+π), H(x+π)) = (V_R(x), H(x)),

so the carrier point is π-periodic. The eight octant midpoints
x_k = π/8 + (k−1)·π/4 land on exactly four points,
(±√2/4, ±√2/8), each taken twice; these four points are concyclic at
radius √10/8 about the origin. The octant boundaries map to
(±1/2, 0) and (0, ±1/4).

Corollary (IC-1): ε(x) = sgn(sin 2x) satisfies ε(x+π) = ε(x); it is
deck-invariant, recording the ellipse half (ε > 0 upper, ε < 0 lower,
ε = 0 on the axes), not the sheet of the 2:1 cover.

### Proof (definitions first)

Register P9 gives V_R(x) = cos(2x)/2, H(x) = sin(2x)/4. Then
V_R(x+π) = cos(2x+2π)/2 = cos(2x)/2 = V_R(x) and
H(x+π) = sin(2x+2π)/4 = H(x), by the 2π-periodicity of sin and cos
(standard trigonometry). At x_k, 2x_k = π/4 + (k−1)π/2, so
(cos 2x_k, sin 2x_k) cycles through (±√2/2, ±√2/2) with each value
taken twice — the eight midpoints land on the four points
(±√2/4, ±√2/8). Concyclicity: (√2/4)² + (√2/8)² = 2/16 + 2/64 = 10/64,
so each point is at distance √10/8 from the origin; under Euclid's
classical definition of a circle (Book 1, Def. 1.15 — verified in
`~/workspace/euclid_work/ledger/book1_ledger.md`: "a circle: plane figure
with all radii from an interior point equal"), these four points lie on
one circle of radius √10/8. At the boundaries 0, π/4, π/2, … direct
substitution gives (±1/2, 0) and (0, ±1/4). The corollary is immediate:
ε(x+π) = sgn(sin(2x+2π)) = sgn(sin 2x) = ε(x). ∎

Domain: all real x. Status: **PROVED** (analytic, complete). Proved-from:
register P9 + the standard 2π-periodicity of sin and cos. The Elements
citation is the classical definition (Def. 1.15), not a deductive premise.

---

## Principle 18 (PROVED) — rapidity derivative and the √2 ladder

**Source book claim:** Book 17, P9 (§17.3).

### Statement

Let w(x) = ln|cot x|, defined where sin x · cos x ≠ 0. Then

    dw/dx = −2/sin(2x).

With w₀ = ln(1+√2): sinh w₀ = 1, cosh w₀ = √2. Moreover
cot(π/8) = 1+√2, cot(3π/8) = √2−1, so at the octant midpoints x_k,
w(x_k) = ±w₀ with the alternating sign pattern +,−,−,+,+,−,−,+.

### Proof (definitions first)

d/dx ln(cot x) = (1/cot x)·(−csc²x) = −1/(sin x cos x) = −2/sin(2x),
by the chain rule, the derivative of cot, and sin(2x) = 2 sin x cos x
(all standard). For the ladder: 1/(1+√2) = √2−1, so with w₀ = ln(1+√2),
e^{w₀} = 1+√2 and e^{−w₀} = √2−1; hence
sinh w₀ = ((1+√2) − (√2−1))/2 = 1 and cosh w₀ = ((1+√2) + (√2−1))/2 = √2.
The half-angle formulas give tan(π/8) = √2−1, so cot(π/8) = 1+√2 and
cot(3π/8) = tan(π/8) = √2−1; at the midpoints |cot x_k| ∈ {1+√2, √2−1},
so w(x_k) = ±ln(1+√2) = ±w₀, with the signs alternating as stated by
direct evaluation. ∎

Domain: w(x) wherever sin x cos x ≠ 0; the ladder values at the eight
midpoints. Status: **PROVED** (analytic, complete). Proved-from: the
chain rule and the standard trig half-angle formulas (modern analytic
mathematics — the *Elements* contains no logarithm and no derivative, so
no Elements proposition is a premise). Euclid enters as classical
bookkeeping only: the irrationality of √2 (why w₀ is not a rational
multiple of any rational log) is the diagonal–side incommensurability of
Book 10, via Prop. 10.9 — verified in
`~/workspace/euclid_work/ledger/book10_ledger.md`: "Commensurability in
length holds iff the squares are in the ratio of a square number to a
square number" (2/1 is not such a ratio, so the diagonal is
incommensurable with the side).

---

## Principle 19 (PROVED) — the paired footprint: cos 4x period structure

**Source book claim:** Book 17, P11, P12, P14 (§17.6).

### Statement

For all real x:

    cos(4(x+π)) = cos(4x),

and π/2 is the minimal positive period of cos 4x (π/4 is not a period:
cos(π) = −1 ≠ 1 = cos 0). The zeros of cos 4x are exactly the octant
midpoints x_k = π/8 + kπ/4 (k ∈ ℤ): cos(4x_k) = cos(π/2 + kπ) = 0; at the
octant boundaries cos 4x = ±1, never 0 (IC-4 correction). Under x → x+π
each of the five footprints is invariant as a set, since octant indices
shift by exactly 4 — the C8 shift-by-4 is the kernel map.

### Proof (definitions first)

cos(4(x+π)) = cos(4x+4π) = cos(4x) by the 2π-periodicity of cos; π/2 is a
period since cos(4x+2π) = cos(4x), and it is minimal because 0 < T < π/2
would give cos(θ+4T) = cos θ for all θ with 0 < 4T < 2π, impossible.
π/4 is not a period: cos(4·π/4) = cos π = −1 ≠ 1 = cos 0. Zeros:
cos(4(π/8 + kπ/4)) = cos(π/2 + kπ) = 0 for every integer k, and these are
all the zeros in [0, 2π). At the boundaries: cos(4·π/4) = cos π = −1,
cos(4·3π/4) = cos 3π = −1 — so the manuscript's "vanishes at the octant
boundaries" is false as stated; the zeros are at the midpoints. Finally,
x → x+π shifts octant indices by exactly 4, permuting the E/B/O contact
sets defined by octant membership, hence leaving each footprint invariant
as a set. (The "even under the code group" clause is excluded: the code
group is never defined as an x-map — book claim A2, ASSERTED.) ∎

Domain: all real x. Status: **PROVED** (analytic, complete). Proved-from:
the 2π-periodicity of cos (standard trigonometry); no Elements
proposition is a premise.

---

## Principle 20 (PROVED) — the exact midpoint value srx(π/8)

**Source book claim:** Book 17, P17 (§17.2/§17.7.2; the page tags it SC —
here given the exact analytic proof).

### Statement

    srx(π/8) = √(4+2√2) + 1 + √2   (exact).

### Proof (definitions first)

On octant 1 the seed's primitive is srx(x) = (1+cos x)/sin x. With the
half-angle values cos(π/8) = √(2+√2)/2, sin(π/8) = √(2−√2)/2 (standard),
srx(π/8) = (2+√(2+√2))/√(2−√2). Now (√(2+√2) + √(2−√2))² = 4 + 2√2, so
√(4+2√2) = √(2+√2) + √(2−√2); and ((1+√2)√(2−√2))² = (3+2√2)(2−√2) = 2+√2,
so (1+√2)√(2−√2) = √(2+√2). Hence
(√(4+2√2) + 1 + √2)·√(2−√2) = √2 + (2−√2) + √(2+√2) = 2 + √(2+√2),
which is exactly the numerator; dividing gives the identity. ∎

Domain: the single value x = π/8. Status: **PROVED** (analytic, complete).
Proved-from: the seed primitive definition (P0) + the half-angle formulas
(standard trigonometry). Euclid enters as classical bookkeeping only:
√2's irrationality is the Book 10 diagonal–side incommensurability via
Prop. 10.9 (verified in the book10 ledger; see Principle 18).

---

Highest Principle number is now **P20**. The four new register rows are
appended to the Principles register table (in the register section above,
not renumbered).

---

## Book 12 — Mass, Frequency, and Harmonic Calibration (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book12_proof.md`
(claim inventory P1–P13 PROVED, C1–C2 CHECKED, A1–A13 ASSERTED with proofs;
rewrite page `~/workspace/r-theory-rewrite/book12/index.html` — *Book 12 —
Mass, Frequency, and Harmonic Calibration*, Volume II).

**Name-collision notice.** This chapter evaluates the claims of the rewrite
series' Book 12 (two-particle / block-projector notation book). It has no
mathematical relation to Euclid's *Elements* Book XII (Eudoxan exhaustion);
per `~/workspace/euclid_work/ledger/book12_ledger.md` (read in full,
2026-09-21), R Theory extends none of Euclid XII's 18 propositions.

**Euclid-citation boundary (checked in the 13 ledgers before writing this
chapter).** The *Elements* contain no analytic sine/cosine/tangent functions.
The book1 ledger (read in full) records the Pythagorean content (1.47) as
*standard background mathematics — used, never derived from Euclid's proof*;
the book3 ledger (definitions read) fixes the circle vocabulary; the
book12 ledger records zero R Theory extension of any Euclid XII proposition.
Accordingly no Euclid book/proposition number is attached as a logical
premise below: the proofs rest on the declared trigonometric substrate
(real sin/cos on ℝ, the Pythagorean identity sin²x + cos²x = 1, the
double-angle formula sin(2x) = 2 sin x cos x as used in the Seed P0) plus
the book's own definitions D1–D2. This matches the boundary already stated
by the Book 15 chapter. Standing domain: the principal branch
x ∈ (0, π/2), so sin x > 0, cos x > 0 and the absolute values in the
reciprocal-spine definitions drop out; Principle 26 needs no branch
restriction and is stated for all real x.

### Evaluated claims summary

28 claims evaluated: **13 PROVED**, **2 CHECKED**, **13 ASSERTED**,
**0 INCOMPLETE** (no computation failed or timed out; the book's proof
file re-ran its two numeric claims from scratch, exit 0). Each claim was
restated and its proof re-verified; the table with verdicts is in
`book12_claims.md` (status: complete).

- **P1** (12.II.T1): M ↔ ν_M = Mc²/h invertible for M > 0 — **PROVED**.
  Coordinate relabeling (multiplication by the nonzero constant c²/h); no
  trig content. Not folded.
- **P2** (§12.III): (1+q_m)/(1−q_m) = m₁/m₂ — **PROVED**. Two-body
  algebra; no trig content. Not folded.
- **P3** (§12.III): binding coordinate inverts exactly;
  B = 2μu² + O(u⁴) — **PROVED**. Taylor bookkeeping; no trig content.
  Not folded.
- **P4** (§12.V): H = λ(1−λ) = sin(2x)/4 from λ = (1+sin x−cos x)/2 —
  **PROVED**. Genuine trigonometric identity; the λ(1−λ) form with this
  explicit λ is not in the register (Book 0's P9 registers only
  H = sin(2x)/4 as 1/(urx+uxp)). **Folded as Principle 26.**
- **P5** (§12.V): Ω = λ/(1−λ) = cxp/srx on the principal branch —
  **PROVED**. Genuine trigonometric identity, but already registered as
  "14 (Book 0)" (Ω = λ/(1−λ) = saw_r/saw_x = uxp/urx = cxp/srx).
  Not folded — re-folding would duplicate a registered principle.
- **P6** (§12.V): λ = 1/urx with urx = srx − crx — **PROVED**. The bare
  relation saw_r = 1/urx is registered as "13 (Book 0)"; the explicit
  trigonometric computation 1/(srx − crx) = (1+sin x−cos x)/2 is not.
  **Folded as Principle 27** (the explicit reciprocal-spine identity).
- **P7** (12.VI.T1): centered projector spectrum 3/5 (×2), −2/5 (×3),
  gap 1, (1/5)Tr(Q²) = 6/25 — **PROVED**. Spectral linear algebra on
  ℂ²⊕ℂ³ (the trace forces the centering constant c = 2/5); trigonometry
  enters only through the later identification λ = 3/5, which is no
  identity about trig functions. Not folded.
- **P8** (§12.VI): λ = 3/5 selects the unique principal-branch preimage
  with (srx, sxp, cxp, crx) = (2, 1/2, 3, 1/3) — **PROVED**. Genuine
  trigonometric lemma (exact (3,4,5) values); not in the register.
  **Folded as Principle 28.**
- **P9** (12.VII.T1): Tr(Q_λ) = 0 ⇒ λ = N/(N+2), Ω = N/2 on the 2+N
  family — **PROVED**. Rational algebra in the integer block-size N;
  Ω = N/2 is a relation in N, not about trig functions. Not folded.
- **P10** (12.VIII.T1): H = rs/m² normalized cross-block capacity;
  (r−s)² = 1 ⟺ 12 = 12 — **PROVED**. Dimension counting
  (dim Hom(ℂ^r,ℂ^s) = rs, dim End(ℂ^m) = m²); H's trigonometric value
  follows from Principle 26's content, no new trig identity. Not folded.
- **P11** (12.IX.T1): Ω² − C_A/C_F = N²(N²−9)/[4(N²−1)], zero iff
  integer N = 3 — **PROVED**. Rational-function algebra in N resting on
  the ASSERTED SU(N) Casimir imports (A5); not a relation about trig
  functions. Not folded.
- **P12** (§12.XI): (a_q, a_g) = (9/25, 16/25) meets the LO fixed point
  uniquely at n_f = 3; dV/dx = −4H — **PROVED (conditional on the
  ASSERTED import A6)**. The n_f = 3 coincidence is a conditional
  cross-check with no trig content. The derivative part is a one-step
  corollary of the registered "9 (Book 0)" (V = H′ = cos(2x)/2,
  H = sin(2x)/4): V′ = −sin(2x) = −4H. Not folded — it would duplicate
  a registered principle's immediate consequence.
- **P13** (§10 correction): (1/5)Tr(Q_ε²) = |H| only at λ ∈ {1/2, 3/5};
  signed gap = ε always — **PROVED** (partly a correction: the
  manuscript's stated general identity is incorrect as stated, true at
  the native state). Projector-spectrum algebra in λ; no trig identity.
  Not folded.
- **C1** (12.II.N2): ν_H ≈ 2.2687×10²³ Hz — **CHECKED** (completed run
  cited in the book's proof file). No trig content. Not folded.
- **C2** (§12.IV): ρ = (m_n−m_p)/m_e = 2.53098829 vs 81/32 —
  **CHECKED** (completed run). No trig content. Not folded.
- **A1–A13**: pitch anchors, SR kinematics, the 2+3 carrier, the notation
  bridge, SU(N) normalizations, the LO fixed-point formula, the QCD
  projection contract, jet-multiplicity data, Hom/End dimensions,
  methodological negatives, the selection firewall, empirical inputs —
  **ASSERTED** (imports, stipulations, declared negatives, data). None is
  a trigonometric identity. Not folded. (A4, the canonical notation
  bridge, supplies the definitions D2 used by Principles 26–28.)

Counts: evaluated 28, folded 3, PROVED 13, CHECKED 2, ASSERTED 13,
INCOMPLETE 0.

### New Principles added: three

#### Principle 26 (PROVED) — transfer-coordinate quadratic identity

**Source book claim:** Book 12, P4 (§12.V).

**Definitions.** For real x, a = sin x, b = cos x; λ = (1 + a − b)/2;
H = sin(2x)/4.

**Statement.** For all real x,

    λ(1 − λ) = sin(2x)/4.

**Proof.** λ(1−λ) = ((1+a−b)(1−a+b))/4 = (1 − (a−b)²)/4.
Now (a−b)² = a² − 2ab + b² = 1 − 2ab by the Pythagorean identity
sin²x + cos²x = 1. Hence λ(1−λ) = (1 − (1 − 2ab))/4 = ab/2 = sin(2x)/4
by the double-angle formula sin(2x) = 2 sin x cos x (Seed P0). ∎

Domain: all real x (no branch restriction; λ has no absolute values).
Status: **PROVED** (analytic, complete). Proved-from: the definitions,
the Pythagorean identity (standard trigonometric substrate, not an
Elements premise), and the Seed.

#### Principle 27 (PROVED) — reciprocal-spine identity

**Source book claim:** Book 12, P6 (§12.V).

**Definitions.** On the principal branch x ∈ (0, π/2), so a = sin x > 0,
b = cos x > 0 and the absolute values drop: srx = (1+b)/a,
crx = b/(1+a), urx = srx − crx.

**Statement.** On the principal branch,

    1/urx = 1/(srx − crx) = (1 + sin x − cos x)/2.

**Proof.** urx = (1+b)/a − b/(1+a) = ((1+b)(1+a) − ab)/(a(1+a))
= (1+a+b)/(a(1+a)), since the ab terms cancel. All denominators are
nonzero on the branch (a > 0, 1+a > 0, 1+a+b > 0), so
1/urx = a(1+a)/(1+a+b). The claim is
a(1+a)/(1+a+b) = (1+a−b)/2. Cross-multiplying (legitimate: both
denominators positive): 2a(1+a) = (1+a−b)(1+a+b) = (1+a)² − b²
= 1 + 2a + a² − b². Rearranged, this is a² + b² = 1, the Pythagorean
identity. ∎

Domain: the principal branch x ∈ (0, π/2). Status: **PROVED**
(analytic, complete). Proved-from: the definitions and the Pythagorean
identity. (The bare relation saw_r = 1/urx is already registered as
"13 (Book 0)"; this principle is the explicit trigonometric computation,
which is not.)

#### Principle 28 (PROVED) — native-state exact values

**Source book claim:** Book 12, P8 (§12.VI).

**Definitions.** λ = (1 + sin x − cos x)/2 on the principal branch
x ∈ (0, π/2); srx = (1+cos x)/sin x, sxp = 1/srx, cxp = (1+sin x)/cos x,
crx = 1/cxp, Ω = λ/(1−λ).

**Statement.** The equation λ = 3/5 has exactly one solution
x ∈ (0, π/2), at which

    (sin x, cos x) = (4/5, 3/5),
    (srx, sxp, cxp, crx) = (2, 1/2, 3, 1/3),
    Ω = 3/2, H = λ(1−λ) = 6/25.

**Proof.** Put a = sin x, b = cos x. λ = 3/5 ⟺ (1+a−b)/2 = 3/5
⟺ a − b = 1/5. Squaring, (a−b)² = 1/25; but (a−b)² = a² − 2ab + b²
= 1 − 2ab (Pythagorean identity), so 2ab = 24/25. Then
(a+b)² = 1 + 2ab = 49/25, and a + b > 0 on the branch, so a + b = 7/5.
Solving the linear system: a = ((a+b)+(a−b))/2 = (7/5+1/5)/2 = 4/5,
b = ((a+b)−(a−b))/2 = (7/5−1/5)/2 = 3/5 — and every solution in
(0, π/2) must satisfy a−b = 1/5, a²+b² = 1, a,b > 0, so this solution
is unique. Then srx = (1+b)/a = (8/5)/(4/5) = 2, sxp = 1/2,
cxp = (1+a)/b = (9/5)/(3/5) = 3, crx = 1/3; Ω = (3/5)/(2/5) = 3/2
(agreeing with the registered "14 (Book 0)" form Ω = cxp/srx);
H = (3/5)(2/5) = 6/25 (agreeing with Principle 26's H = sin(2x)/4). ∎

Domain: the principal branch; uniqueness is on (0, π/2). Status:
**PROVED** (analytic, complete). Proved-from: the definitions and the
Pythagorean identity — pure algebra, no calculus needed for uniqueness.

### Register and chapter notes

- Highest Principle number is now **P28**. Three new register rows were
  appended ("26 (Book 12)"–"28 (Book 12)"); no earlier rows, chapters, or
  numbers were touched.
- Dedup discipline: P5 was not re-folded (already "14 (Book 0)"); the
  derivative part of P12 was not re-folded (one-step corollary of the
  registered "9 (Book 0)"); the bare saw_r = 1/urx inside P6 was not
  re-folded (already "13 (Book 0)") — only genuinely new trigonometric
  content became principles.
- Forcing was refused throughout: 25 of the 28 claims carry no honest
  trigonometric content (coordinate relabelings, two-body algebra,
  spectral linear algebra, dimension counts, rational algebra in N,
  checked numerics, asserted imports/negatives) and were evaluated with
  their scope labels rather than folded in.

---

## Book 13 — Thermodynamics, Information, and the Arrow of Time (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book13_proof.md`
(claim inventory P1–P44 in dependency order; rewrite page
`~/workspace/r-theory-rewrite/book13/index.html` — *Book 13 —
Thermodynamics, Information, and the Arrow of Time*, principal theorems
13.II.T1, 13.III.T1–T2, 13.IV.T1, 13.V.T1, 13.VI.T1, 13.VII.T1,
13.VIII.T1, 13.X.T1–T2).

**No-Euclid-wholesale boundary.** The rewrite series' "Book 13" is a pure
name collision with Euclid's *Elements* Book 13 (the five regular solids):
the book13 ledger's full-text search of all 23 rewrite pages finds zero
EMR/pentagon/solid machinery, confirmed by direct read of
`~/workspace/euclid_work/ledger/book13_ledger.md`. Consequently no
proposition of the *Elements* is a logical premise of any principle below;
the proofs are analytic, founded on the Seed (P0), the ordinary
trigonometry substrate (M0), and earlier registered principles. The book's
own proof file (§0) records the same boundary: its physics enters only
through explicitly declared contracts (AX-1..AX-5, ASSERTED), and ordinary
real analysis is background mathematics, not inheritance.

### Evaluated claims summary

44 claims evaluated (P1–P44): **28 PROVED**, **3 CHECKED** (the book page's
own numeric runs, 2×10⁴–4×10⁴ points, not re-run here), **12 ASSERTED**
(declared contracts, standard imports, status declarations, closure
bookkeeping), **1 INCOMPLETE**. P25 splits: its telescoping half is
PROVED, its crossing-rule half ASSERTED (counted under both). Two further
IC flags carry PROVED analytic refutations (recorded as flags, not claims).
The claim-by-claim table with verdicts is in `book13_claims.md` (status:
complete).

- **§2.I The coordinate and its exact identities.** P1 **PROVED** —
  folded as Principle 26 (Book 13). P2 **PROVED** — *not* folded: its
  content λ(1−λ) = sin(2x)/4 is already registered as Principle "9 (Book 0)"
  (H = 1/(urx+uxp) = sin(2x)/4); since 1/(urx+uxp) = λ(1−λ) exactly
  (urx = 1/λ, uxp = 1/(1−λ)), P2 is the same identity in λ-coordinates,
  independently proved in the book file — re-folding it would duplicate a
  registered principle. P3 **CHECKED** — not folded (definitional
  reciprocal-channel algebra; CHECKED status only). P4 **PROVED** — folded
  as Principle 27 (Book 13). P5 **PROVED** — not folded (entropy-limit
  analysis; its trig content is P1's endpoint values, folded). P6
  **ASSERTED** — not folded (status declaration under AX-1).
- **§2.II Convex generator / exponential family.** P7–P13 **PROVED** —
  none folded: calculus of A(v) = ln(1+e^v), logarithm algebra, Legendre
  algebra, KL=Bregman order-convention identity, exponential-family score
  identity. P12's Fisher-angle identity dφ_F/dv = √|H| is exact but is
  analytic geometry of the Fisher/logit coordinate; its only trigonometric
  content is Principle "9 (Book 0)". Thm 13.II.T1 **PROVED** conditional on
  AX-1 — not folded (framing summary).
- **§2.III Canonical thermodynamic bridge.** P14, P15, P16 **PROVED** —
  not folded (physics bridge, identifiability obstruction, response-kernel
  unification; trig enters only through registered principles). P17
  **CHECKED** — not folded (numeric Schottky witness). IC flag (13.III):
  "|urx| is exactly the canonical partition function" is false as printed —
  refutation **PROVED** (P14 gives Z = g_r|urx|, so |urx| = Z/g_r ≠ Z for
  g_r = 2); recorded as a flag, not folded.
- **§2.IV Detailed balance / slow driving.** P18, P19 **PROVED** — not
  folded (Markov-contract algebra, KL/free-energy relaxation). P20
  **ASSERTED** (ST imports) — not folded. P21 **INCOMPLETE** — not folded
  (right-hand side numerator missing as printed; cannot be verified).
- **§2.V Cycles, seams, identifiability.** P22 **PROVED**, P23
  **CHECKED**, P24 **PROVED**, P25a **PROVED** / P25b **ASSERTED** — none
  folded (telescoping sums, numeric witness, modeling claims; no trig
  content).
- **§2.VI Cophase topology.** P26 **PROVED** — *partially* folded: the
  π-periodicity of H and ε is already covered by M0's 2π-periodicity of
  sin (the basis of Principle "3 (Book 0)"'s periodicity and Principle "7
  (Book 0)"'s FW(x+π) = FW(x)) — not re-folded. The as-printed
  urx/uxp π-periodicity is entangled with FlatWave sign conventions
  (canonical λ has λ(x+π) = 1−λ(x), so urx swaps with uxp) and was not
  reduced to clean trig identities here. P27 **PROVED** — not folded
  (affine-map order argument). IC flag (13.VI): "λ is quarter-turn
  invariant" is false under canonical notation — refutation **PROVED**
  (λ(0) = 0 ≠ 1 = λ(π/2)); the true invariant is the constructible ratio
  ε/urx. P28, P29 **ASSERTED** — not folded.
- **§2.VII Path-space irreversibility.** P30 **PROVED** — not folded (its
  trig content is folded Principle 27). P31 **PROVED**, P32
  **ASSERTED** (ST), P33 **ASSERTED** — not folded.
- **§2.VIII State rank.** P34, P35, P37 **PROVED**, P36 **ASSERTED**
  (ST) — none folded (rank/Jacobian/extensivity arguments; no trig).
- **§2.IX Phase transitions.** P38, P39, P40 **PROVED** — none folded
  (calculus of S_sys; P39 restates folded Principle 26; BEC no-go).
- **§2.X Closure.** P41–P44 **ASSERTED** — not folded (exhaustiveness
  asserted not proved; closure bookkeeping; procedural declarations).

### Principle 26 (Book 13) — Transfer-coordinate chart lemma (PROVED)

**Statement.** For λ(x) = (1 + sin x − cos x)/2: λ is strictly increasing
on (0, π/2), hence a bijection (0, π/2) → (0, 1); moreover λ(0) = 0,
λ(π/4) = 1/2, λ(π/2) = 1.

**Domain.** Endpoint values at x ∈ {0, π/4, π/2}; the bijection on the open
interval (0, π/2).

**Proof.** λ is differentiable with
dλ/dx = (cos x − (−sin x))/2 = (sin x + cos x)/2.
On (0, π/2), sin x > 0 and cos x > 0 (M0 quadrant signs), so dλ/dx > 0;
λ is strictly increasing (consistent with registered Principle "12 (Book
0)", λ′ > 1/2, for the same λ — verified identical: on (0,π/2),
(1−p)/2 with p = cos x − sin x equals (1+sin x−cos x)/2). Endpoint values
by direct substitution (M0 special values): λ(0) = (1+0−1)/2 = 0;
λ(π/4) = (1+√2/2−√2/2)/2 = 1/2; λ(π/2) = (1+1−0)/2 = 1. A continuous
strictly increasing function on (0, π/2) with end-limits 0 and 1 maps
(0, π/2) bijectively onto (0, 1). ∎

Status: **PROVED** (analytic, complete). Proved-from: M0 (differentiation
of sin/cos, quadrant signs, special values, continuity) + Principle "12
(Book 0)" (consistency check). *Book claim:* P1 (§2.I).

### Principle 27 (Book 13) — Cofunction symmetry of the transfer coordinate (PROVED)

**Statement.** For all real x: λ(π/2 − x) = 1 − λ(x), where
λ(x) = (1 + sin x − cos x)/2.

**Proof.** λ(π/2 − x) = (1 + sin(π/2 − x) − cos(π/2 − x))/2
= (1 + cos x − sin x)/2 (M0 cofunction formulas)
= 1 − (1 + sin x − cos x)/2 = 1 − λ(x). ∎

Status: **PROVED** (analytic, complete). Proved-from: M0 cofunction/shift
formulas. *Book claim:* P4 (§2.I).

### Register and chapter notes

- Highest Principle number is now **P27**. The register table gains two
  rows, "26 (Book 13)" and "27 (Book 13)"; no earlier rows or chapters
  were touched. Ids 26–27 were chosen as one above the highest numeric id
  previously in use (25), following the Book 9 precedent; proofs cite
  register rows by their unambiguous labels.
- **Register-integrity note (for the reevaluation stage):** the register
  carries pre-existing numbering collisions introduced by earlier workers
  (multiple rows numbered 1, 2, 17–25 across book sections); per the
  standing rule they are not renumbered here — Book 9's chapter already
  flags this for the reevaluation stage, and this chapter concurs.
- Per the standing rule, nothing was forced: of 44 evaluated claims, 2
  yielded new principles; 1 further genuine identity (P2) was already
  registered and 1 periodicity claim (P26) already covered, both recorded
  rather than duplicated; the rest carry no honest trigonometric content.
