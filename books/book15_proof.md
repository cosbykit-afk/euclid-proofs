# Book 15 extension proofs — Saw interchanges, double-angle decomposition, bridge to E8

Source: `~/workspace/r-theory-rewrite/book15/index.html`
(rewrite of Book 15 of R Theory — Volume III; source volume_iii.txt lines 795–1320).
Date of this proof file: 2026-09-22.

## 0. Basis, boundary, and method

Citable without reproof (per campaign contract):
- Euclid's Elements as inventoried in `~/workspace/euclid_work/ledger/book1_ledger.md`
  … `book13_ledger.md`. **Boundary:** the ledgers record that analytic trigonometry on a
  declared coordinate is a *standard imported* substrate (ST), not derived from the
  Elements. This file therefore does **not** claim wholesale inheritance of the Elements;
  R Theory extends a synthetic-constructive stratum on its declared substrate, and the
  trigonometric substrate below is listed explicitly as new axioms NA-15-1…NA-15-7.
- The campaign seed: Kit's double-angle secant/cosecant identity, PROVED, at
  `~/workspace/euclid_work/books/seed_double_angle.md`. Its final regrouping step
  (2·tan x + 2·cot x = 2/(sin x·cos x) = 4/sin 2x) is cited in §15.III.
- `book0_proof.md` … `book13_proof.md` are **not present** in this environment
  (only `seed_double_angle.md` exists under `books/`), so no citations to earlier
  book proof files are made here.

Provenance cited but **not re-run** here: the upstream audit
`vol3/book15/audit_book15.py` (240 assertions, all passed per the page),
`validation/book15/verify_book15.py` (220 assertions, all passing, worst measured
error 2.5e-8 on cancellation-prone reciprocal forms near seams — pure floating-point
cancellation, the identities being exact algebra), and
`validation/book15/test_embeds.py` (13 embed-consistency assertions). Where a claim
below rests on those suites rather than on a proof written here, it is labeled
CHECKED with the suite named, and the non-rerun is stated.

Scope labels used in this file (campaign contract):
PROVED = exact mathematics proved here; CHECKED = a completed computation
(reported run, cited; not re-run here unless stated); ASSERTED = manuscript claim,
admission, definition-substrate, or scope contract; INCOMPLETE = failed/timed-out/
unfinished. No claim is presented above its established status.

Standing domain for the trigonometric work: x ∈ (0, π/2), so all sines, cosines,
tangents, and cotangents below are strictly positive and every division is legitimate.
λ ∈ (0,1), r > 0, ε = ±1, s_Ω = ±1.

---

## 1. Claim inventory

| # | Claim (page ref) | Page tag | This file's label |
|---|---|---|---|
| 1 | 15.I.T1 primitive complementary interchange (+ urx/uxp swap) | CP | PROVED |
| 2 | 15.I.D1 complex package Ψ_U closure | (def) | PROVED |
| 3 | 15.I.C1 complement is an involution | CP | PROVED |
| 4 | 15.II.T1 AB = 4 | CP | PROVED |
| 5 | 15.II.T2 hyperbola D₂²−K₂² = 16; complement fixes D₂, negates K₂ | CP | PROVED |
| 6 | 15.III.T1 D₂ = 4/sin 2x, K₂ = 4cot 2x | CP | PROVED |
| 7 | 15.III.T2 Z₂ = (K₂+4i)/D₂ = e^{2ix} | CP | PROVED |
| 8 | 15.III.D1 H_R, V_R definitions and derivatives | (def) | PROVED |
| 9 | 15.III.C1 complement parity (H_R even, V_R odd, Z₂(Cx) = −conj Z₂) | CP | PROVED |
| 10 | 15.IV.T1 signed Saw complement: reduction (symbolic core) | SC | CHECKED (cited: book's sympy core reduction) |
| 11 | 15.IV.T1 parities: Ω ↔ Ω⁻¹, ln Ω odd, ε even under λ ↔ 1−λ | SC | PROVED (given the reduction) |
| 12 | 15.IV.C1 square-root transfer angle reparametrization | CP | PROVED |
| 13 | 15.IV.D1 qSaw normalized square identities | CP | PROVED |
| 14 | 15.V.T1 Saw–Hodge meridian projection | CP | PROVED (given the quarter-phase lift definition) |
| 15 | 15.V.C1 balance states ρ = ½(I±Y); R_Y maps ρ(λ) → ρ(1−λ) preserving sign | CP | PROVED (balance part); CHECKED (R_Y-mapping, cited) |
| 16 | 15.V.T2 sign visibility; joint (ε, s_Ω) recovery | CP | PROVED (given manuscript definitions) |
| 17 | 15.V.C2 minus sign as mandatory π/2-phase residue | CP | ASSERTED (interpretive reading) |
| 18 | 15.V.T3 protected-traversal obstruction | CP | PROVED (given the R_Y-even premise) |
| 19 | 15.VI.D1–D2 transfer doublet, native quarter-turn J | (def) | ASSERTED (manuscript substrate) |
| 20 | 15.VI.T1 order-two Saw complement vs order-four quarter-turn are distinct | CP | PROVED |
| 21 | 15.VI.T2 symmetric-square readout: Q_t″+4Q_t = 0, Q_t² = ¼I | CP | PROVED |
| 22 | 15.VI.T2 commutator form Q_t′ = [J, Q_t] | CP | CHECKED (cited: manuscript J, book's suite) |
| 23 | 15.VI.C1 JQ_tJᵀ = −Q_t | CP | CHECKED (cited) |
| 24 | 15.VI.C2 one harmonic structure, two routes | CP | PROVED |
| 25 | 15.VI.B1 product-duality bridge (conditional) | MA | ASSERTED (explicitly conditional) |
| 26 | 15.VII.T1 dual-mode bigrading (commuting involutions) | CP | PROVED (general lemma) |
| 27 | 15.VII.C1 K = I_ext J_int, K² = I | CP | PROVED |
| 28 | 15.VII.C2 relative complex-structure orientation | CP | ASSERTED (manuscript) |
| 29 | 15.VII.Witness 1 (real 4×4 witness, exact) | CP | CHECKED (cited: book's exact computation) |
| 30 | 15.VII.Witness 2 (2×2 bridge polarization, exact symbolic) | CP | CHECKED (cited) |
| 31 | 15.VII.C3 generic bridge polarization shifts phase | CP | CHECKED (cited: book's exact computation) |
| 32 | 15.VII.CT1 conditional quarter-phase selection θ_* = ±π/2 | CP (conditional) | PROVED (stationary-point lemma); ASSERTED (full conditional theorem) |
| 33 | 15.VII.3 hyperbolic double-angle compatibility v = 2u | CP | PROVED |
| 34 | 15.VIII.T1 even-exterior polynomial Q_M(χ) = 1+6χ+χ² | CP | PROVED |
| 35 | 15.VIII.C1 reciprocal covariance | CP | PROVED |
| 36 | 15.VIII.D2 mirror-weighted family endpoints | (def) | PROVED |
| 37 | 15.VIII.T2 parent identity; unique minimum at r = 1 | CP | PROVED |
| 38 | 15.IX.T1 E8(−24) threshold admission | MA | ASSERTED (admission, not derived) |
| 39 | 15.IX.T2 threshold closure meta-summary | MA | ASSERTED |
| 40 | 15.IX.T3 canonical round-trip normalization c = 1 | CP | CHECKED (cited: book's two-line proof / suite) |
| 41 | 15.IX E8 30380 weight table (Freudenthal, exact integer) | SC | CHECKED (cited: established SC computation in ~/workspace/e8/) |
| 42 | 15.IX 248-adjoint Jacobi/Fierz check (exactly 0.0 over 341,376 triples) | NC | CHECKED (cited: reported numerical run) |
| 43 | 15.IX 30380-rep generators (Casimir dev. 4.0e-10, Serre 1.7e-14) | NC | CHECKED (cited: reported numerical run) |
| 44 | 15.X Δ_op(Book 15) = ∅ | MA | ASSERTED (status declaration) |
| — | Firewalls M15-A … M15-H | MA | ASSERTED (scope contracts, §6) |

INCOMPLETE: none. No claim was found timed-out, failed, or unfinished.

---

## 2. Definitions (dependency order)

**D-1 (substrate, NA-15-1).** Real sin, cos on (0, π/2) with sin²+cos² = 1,
tan = sin/cos, cot = cos/sin, sin 2x = 2 sin x cos x, cos 2x = cos²x − sin²x,
and the complement laws sin(π/2−x) = cos x, cos(π/2−x) = sin x. Complex
exponentials and complex differentiation are standard imported mathematics (ST).

**D-2 (15.I).** The four canonical primitives on (0, π/2):
srx = cot(x/2), sxp = tan(x/2), cxp = tan(π/4+x/2), crx = tan(π/4−x/2).
Complement Cx = π/2 − x.

**D-3 (15.I).** The manuscript's sum/difference packaging
urx = srx − crx, uxp = cxp − sxp
(the identification consistent with the two stated relations
urx(Cx) = uxp(x), uxp(Cx) = urx(x), and D₂ = urx+uxp; see proof of claim 1).
The complex package Ψ_U = urx + i·uxp.

**D-4 (15.II).** A = srx − sxp, B = cxp − crx; D₂ = A+B, K₂ = A−B.

**D-5 (15.III).** Z₂ = (K₂+4i)/D₂; H_R = 1/D₂, V_R = K₂/(2D₂).

**D-6 (15.IV; NA-15-2).** Saw chart substrate (manuscript): chart sign ε = ±1,
share λ ∈ (0,1), Ω = λ/(1−λ), H_Saw = λ(1−λ). The book's symbolic core reduction
states that on the positive bounded chart the Saw is exactly
saw_up = ελ, saw_down = ε(1−λ) — CHECKED (claim 10), taken as given for the
parity proofs.

**D-7 (15.IV).** Transfer-angle reparametrization: θ = π − 2θ_λ with λ = cos²θ_λ;
equivalently λ = sin²(θ/2). q = −cos θ. qSaw(q) = 2q/(1+q²) with companion
c_q = (1−q²)/(1+q²); Ω₂ = Ω², η₂ = 2η, q₂ = 2q/(1+q²) = tanh η (with q = tanh η).

**D-8 (15.V; NA-15-3).** Pauli matrices X, Y, Z with [X,Y] = 2iZ, [Y,Z] = 2iX,
[Z,X] = 2iY, X² = Y² = Z² = I (ST). The quarter-phase lift
ψ = (√λ, e^{iφ}√(1−λ)) with φ pinned to the quarter phase,
φ = s_Ω·π/2 (s_Ω = ±1); ρ = ψψ†. An "R_Y-even Hamiltonian" means a Hamiltonian
confined to the I/Y operator algebra, H = h₀I + h₁Y (manuscript premise).
The componentwise symmetric square Q_C(ξ) = (ελ, −ε(1−λ)) (manuscript definition).

**D-9 (15.VI; NA-15-4).** Native transfer doublet (p,q) with p²+q² = 2,
p′ = −q, q′ = p; native quarter-turn generator J with J² = −I, t′ = Jt
(manuscript substrate). Symmetric-square readout
Q_t = (ε/2)[sin 2x·Z + cos 2x·X].

**D-10 (15.VII; NA-15-5).** Two commuting involutions σ_ext, σ_int acting on
End(V) (manuscript substrate; specific matrices and the witnesses are imported
data, verified exactly in the book's suite — claims 29–31). K = σ_extσ_int
(the page's I_extJ_int), B = −σ_y.

**D-11 (15.VIII).** Amplitude dictionary χ = r², λ = 1/(1+r²),
v = ln[λ/(1−λ)] = −2ln r, u = −ln r; reciprocal exchange r ↔ r⁻¹.
Q_M(χ) = 1+6χ+χ²; P_δ = 1+4δr+6r²+4δr³+r⁴; A_δ = δ(1+r²)+2r.

---

## 3. Proofs in dependency order

### §15.I — Canonical complementary-swap closure

**Claim 1 (15.I.T1), PROVED.** Complement exchanges the primitive pairs.
Compute, for x ∈ (0, π/2):
srx(Cx) = cot((π/2−x)/2) = cot(π/4 − x/2).
Since cot(π/4 − x/2) = tan(π/2 − (π/4 − x/2)) = tan(π/4 + x/2) = cxp(x),
we have srx(Cx) = cxp(x). By involution (claim 3, proved independently below),
cxp(Cx) = srx(x). Similarly sxp(Cx) = tan((π/2−x)/2) = tan(π/4 − x/2) = crx(x),
and crx(Cx) = sxp(x). Hence srx ↔ cxp and sxp ↔ crx under C. ∎

With the packaging D-3: urx(Cx) = srx(Cx) − crx(Cx) = cxp(x) − sxp(x) = uxp(x),
and uxp(Cx) = cxp(Cx) − sxp(Cx) = srx(x) − crx(x) = urx(x). ∎

**Claim 2 (15.I.D1), PROVED.** Ψ_U(Cx) = urx(Cx) + i·uxp(Cx) = uxp(x) + i·urx(x)
by claim 1, while i·conj(Ψ_U(x)) = i(urx(x) − i·uxp(x)) = uxp(x) + i·urx(x). ∎

**Claim 3 (15.I.C1), PROVED.** C(Cx) = π/2 − (π/2 − x) = x, so C² = id; C is an
involution (a substitution law), not a propagation equation — the latter phrase
is the M15-A scope contract (§6), not a theorem. ∎

### §15.II — Aligned primitive-difference hyperbola

**Claim 4 (15.II.T1), PROVED.** A = cot(x/2) − tan(x/2)
= (cos²(x/2) − sin²(x/2))/(sin(x/2)cos(x/2)) = cos x/(sin x/2) = 2cot x,
using cos²−sin² = cos x and 2 sin(x/2)cos(x/2) = sin x.
B = tan(π/4+x/2) − tan(π/4−x/2). With tan P − tan Q = sin(P−Q)/(cos P cos Q):
P−Q = x, and cos(π/4+x/2)cos(π/4−x/2) = (cos(π/2) + cos x)/2 = (cos x)/2,
so B = sin x/((cos x)/2) = 2tan x. Therefore AB = 4cot x·tan x = 4. ∎

**Claim 5 (15.II.T2), PROVED.** D₂² − K₂² = (A+B)² − (A−B)² = 4AB = 16 by claim 4.
Complement: A(Cx) = 2cot(π/2−x) = 2tan x = B(x); B(Cx) = 2tan(π/2−x) = 2cot x
= A(x). Hence D₂(Cx) = A(Cx)+B(Cx) = B(x)+A(x) = D₂(x) (fixed) and
K₂(Cx) = A(Cx)−B(Cx) = B(x)−A(x) = −K₂(x) (negated). ∎

### §15.III — Double-angle decomposition and phasor

**Claim 6 (15.III.T1), PROVED.** D₂ = A+B = 2cot x + 2tan x = 2(sin x/cos x +
cos x/sin x) = 2/(sin x cos x) = 4/sin 2x — the seed's final regrouping step,
cited from `seed_double_angle.md`. K₂ = A−B = 2cot x − 2tan x
= 2(cos²x − sin²x)/(sin x cos x) = 2cos 2x/(sin 2x/2) = 4cot 2x. ∎

**Claim 7 (15.III.T2), PROVED.** Z₂ = (K₂+4i)/D₂ = (4cot 2x + 4i)/(4/sin 2x)
= sin 2x·(cot 2x + i) = cos 2x + i sin 2x = e^{2ix}. ∎

**Claim 8 (15.III.D1), PROVED.** H_R = 1/D₂ = sin 2x/4 and
V_R = K₂/(2D₂) = (4cot 2x)/(8/sin 2x) = (cos 2x/sin 2x)(sin 2x/2) = cos 2x/2
by claim 6. Derivatives: H_R′ = 2cos 2x/4 = cos 2x/2 = V_R;
V_R′ = −2sin 2x/2 = −sin 2x = −4H_R; Z₂′ = 2i·e^{2ix} = 2iZ₂ (claim 7). ∎

**Claim 9 (15.III.C1), PROVED.** Complement parity:
H_R(Cx) = sin 2(π/2−x)/4 = sin(π−2x)/4 = sin 2x/4 = H_R(x) (even);
V_R(Cx) = cos(π−2x)/2 = −cos 2x/2 = −V_R(x) (odd);
Z₂(Cx) = e^{2i(π/2−x)} = e^{i(π−2x)} = cos(π−2x) + i sin(π−2x)
= −cos 2x + i sin 2x = −(cos 2x − i sin 2x) = −conj(Z₂(x)). ∎

### §15.IV — Signed Saw complement and transfer

**Claim 10 (15.IV.T1 core reduction), CHECKED.** The exact reduction of the Saw
to saw_up = ελ, saw_down = ε(1−λ) on the positive bounded chart is the book's
symbolic core, proved in sympy per the page (SC tag). Not re-derived here;
cited from the page's reported provenance (upstream audit + verify_book15.py,
all passing). The complement parities verified numerically in the book's suite.

**Claim 11 (15.IV.T1 parities), PROVED given the reduction.** Under λ ↔ 1−λ:
the shares exchange (ελ ↔ ε(1−λ)) by definition; Ω = λ/(1−λ) maps to
(1−λ)/λ = Ω⁻¹; ln Ω(1−λ) = ln(Ω(λ)⁻¹) = −ln Ω(λ), i.e. ln Ω is odd about the
midpoint λ = 1/2; the chart sign ε is untouched by the λ-swap (even). ∎

**Claim 12 (15.IV.C1), PROVED.** With λ = sin²(θ/2): 1−λ = cos²(θ/2), so
Ω = λ/(1−λ) = tan²(θ/2); H_Saw = λ(1−λ) = sin²(θ/2)cos²(θ/2) = (sin θ/2)²,
hence 2√H_Saw = sin θ on the chart (sin θ ≥ 0 for θ ∈ (0,π)).
Consistency: λ = cos²θ_λ = sin²(θ/2) gives θ/2 = π/2 − θ_λ, i.e. θ = π − 2θ_λ. ∎

**Claim 13 (15.IV.D1), PROVED.** With qSaw = 2q/(1+q²) and c_q = (1−q²)/(1+q²):
qSaw² + c_q² = (4q² + (1−q²)²)/(1+q²)² = (1+2q²+q⁴)/(1+q²)² = 1.
With q = tanh η, q₂ = 2q/(1+q²) is the standard tanh double-angle formula, so
q₂ = tanh 2η = tanh η₂ with η₂ = 2η; Ω₂ = Ω² is definitional. ∎

### §15.V — Quarter-phase Saw–Hodge lift

**Claim 14 (15.V.T1), PROVED given the lift definition D-8.** With
ψ = (√λ, e^{iφ}√(1−λ)) and φ = s_Ωπ/2:
ρ = ψψ† = [[λ, √λ√(1−λ)e^{−iφ}],[√λ√(1−λ)e^{iφ}, 1−λ]].
The page's form: ½[I + (2λ−1)Z] = diag(λ, 1−λ) ✓, and
½·2s_Ω√H_Saw·Y = s_Ω√H_Saw·[[0,−i],[i,0]] with √H_Saw = √(λ(1−λ)).
Off-diagonal match requires e^{−iφ} = −is_Ω: for s_Ω = +1, φ = π/2 gives
e^{−iπ/2} = −i ✓; for s_Ω = −1, φ = −π/2 gives e^{iπ/2} = i = −i·(−1) ✓.
Hence ρ = ½[I + (2λ−1)Z + 2s_Ω√H_Saw·Y], a Bloch meridian in the Y–Z plane
(⟨X⟩ = 0), with ⟨Y⟩ = tr(ρY) = 2s_Ω√H_Saw — the sign choice s_Ω is visible in
⟨Y⟩. ∎

**Claim 15 (15.V.C1), split.** Balance states, PROVED: at λ = 1/2,
2λ−1 = 0 and √H_Saw = 1/2, so ρ = ½[I ± Y] by claim 14. The R_Y reflection
mapping ρ(λ) → ρ(1−λ) with the sign choice preserved is CHECKED — cited from
the book's symbolic proof computation (manuscript R_Y convention, not
reconstructed here).

**Claim 16 (15.V.T2), PROVED given the manuscript definitions D-8.**
ξ is the unsigned lift, carrying no ε, so ξξ† = ρ is blind to ε; Q_C(ξ) =
(ελ, −ε(1−λ)) carries ε but no s_Ω, so is blind to s_Ω. Joint recovery:
from ρ, λ = ρ₀₀ and sign(⟨Y⟩) = s_Ω (for H_Saw > 0, claim 14); from Q_C,
ε = sign of the first component (λ > 0). Neither alone suffices. ∎

**Claim 17 (15.V.C2), ASSERTED.** "The minus sign is the mandatory π/2-phase
residue" is the manuscript's interpretive reading of the quarter-phase pinning
in claim 14; no independent mathematical content beyond it is established here.

**Claim 18 (15.V.T3), PROVED given the R_Y-even premise D-8.**
Let H = h₀I + h₁Y (R_Y-even, confined to the I/Y algebra) and
ρ = ½[I + (2λ−1)Z + 2s_Ω√H_Saw·Y]. Then
[H, ρ] = h₁(2λ−1)/2·[Y,Z] = ih₁(2λ−1)X (using [Y,Z] = 2iX, [Y,Y] = 0),
so −i[H,ρ] = h₁(2λ−1)X is pure X-type. Hence
d⟨Y⟩/dt = tr(Y·(−i[H,ρ])) = 0 and d⟨Z⟩/dt = 0: the flow is stationary in the
meridian coordinates (⟨Y⟩,⟨Z⟩). The meridian (claim 14) lies in the Y–Z plane
with non-degenerate tangent dρ/dθ = −i[(s_Ω/2)X,ρ] = (s_Ω/2)(1−2λ)Y + √H_Saw·Z
(pure Y/Z-type, computed from [X,Z] = −2iY, [X,Y] = 2iZ); an X-type generator
cannot produce this tangent, so no R_Y-even Hamiltonian in the I/Y algebra
traverses the meridian. The obstruction is proved, not assumed. ∎

### §15.VI — Saw complement vs native quarter-turn

**Claim 19 (15.VI.D1–D2), ASSERTED.** The transfer doublet (p,q), p²+q² = 2,
p′ = −q, q′ = p, and the generator J with J² = −I, t′ = Jt, are manuscript
substrate definitions (NA-15-4), imported as data.

**Claim 20 (15.VI.T1), PROVED.** The Saw complement acts on the share by
λ ↦ 1−λ, an involution (order two; claim 3 applied to the λ-chart). The native
quarter-turn acts by t ↦ Jt with J² = −I, so C_J²: t ↦ J²t = −t ≠ t for t ≠ 0
and C_J⁴ = id: order four. An order-two map and an order-four map are distinct
transformations; conflating them is an error. ∎

**Claim 21 (15.VI.T2 partial), PROVED.** For Q_t = (ε/2)[sin 2x·Z + cos 2x·X]:
Q_t² = (ε²/4)(sin²2x·Z² + cos²2x·X² + sin2x cos2x·{Z,X})
= (1/4)(sin²2x + cos²2x)I = ¼I, since Z² = X² = I and {Z,X} = 0.
Q_t′ = ε[cos 2x·Z − sin 2x·X],
Q_t″ = ε[−2sin 2x·Z − 2cos 2x·X] = −4Q_t, i.e. Q_t″ + 4Q_t = 0. ∎

**Claim 22 (15.VI.T2 commutator form), CHECKED.** Q_t′ = [J, Q_t] is the
manuscript's relation in its own J-convention; cited from the book's CP tag
and verification suite, not independently reconstructed here.

**Claim 23 (15.VI.C1), CHECKED.** JQ_tJᵀ = −Q_t, cited from the book's suite
(manuscript J-convention).

**Claim 24 (15.VI.C2), PROVED.** The pair (sin 2x, cos 2x) appearing as the
Z/X coefficients in Q_t (claim 21) is the same harmonic pair as
(2H_R, V_R)·(2, 1) = (sin 2x/2·2, cos 2x) from claim 8 and the phasor Z₂ =
cos 2x + i sin 2x (claim 7): one harmonic structure, two routes. ∎

**Claim 25 (15.VI.B1), ASSERTED.** The product-duality bridge — that a later
physical normal-plane quotient *may* realize product duality with the same
J² = −I algebra — is explicitly conditional per the page (MA tag); nothing is
derived about it here.

### §15.VII — Dual-mode operator bigrading

**Claim 26 (15.VII.T1), PROVED (general lemma).** Let σ₁, σ₂ be commuting linear
involutions on End(V). Each involution splits End(V) into ±1 eigenspaces;
commuting operators preserve each other's eigenspaces, giving the four-way
decomposition End(V) = ⊕_{a,b∈{±1}} E_{a,b} with
E_{a,b} = {T : σ₁T = aT, σ₂T = bT}. If S ∈ E_{a,b}, T ∈ E_{c,d} then
σ₁(ST) = (σ₁S)(σ₁T) = ac·ST (involution acting multiplicatively), so
ST ∈ E_{ac,bd}: multiplicative parity rules. The manuscript supplies the
specific commuting involutions σ_ext, σ_int as substrate (NA-15-5). ∎

**Claim 27 (15.VII.C1), PROVED.** With K = σ₁σ₂ for commuting involutions,
K² = σ₁σ₂σ₁σ₂ = σ₁²σ₂² = I. ∎

**Claim 28 (15.VII.C2), ASSERTED.** "Relative complex-structure orientation on
K sectors" — manuscript-internal; no reconstructible content on the page.

**Claims 29–30 (15.VII witnesses), CHECKED.** The minimal real 4×4 witness
(four 4-dimensional parity spaces) and the 2×2 orthogonal bridge-polarization
witness (B = −σ_y, {K,B} = {H,B} = 0, ⟨B,H(θ)⟩ = −sinθ) were verified exactly
(finite-dimensional exact / exact symbolic computation) per the page; cited
from the book's suite, not re-run here.

**Claim 31 (15.VII.C3), CHECKED.** ⟨B_δ,H(θ)⟩ = cos(δ+θ) — the book's exact
computation; cited, not re-derived (manuscript B_δ convention).

**Claim 32 (15.VII.CT1), split.** Lemma, PROVED: the stationary points of
θ ↦ −sinθ satisfy d/dθ(−sinθ) = −cosθ = 0, i.e. θ = ±π/2. Full conditional
theorem, ASSERTED: quarter-phase selection θ_* = ±π/2 "by sign of s_Ωκ_y" is
conditional on the enforced B-purity contract (κ_x = 0) and the manuscript's
stationarity equation — explicitly not derived, per the page.

**Claim 33 (15.VII.3), PROVED.** From the dictionary D-11, v = −2ln r and with
u = −ln r, v = 2u exactly. ∎

### §15.VIII — Four-dimensional even-exterior

**Claim 34 (15.VIII.T1), PROVED.** For a 4-dimensional real manifold,
dim Λ^0 = C(4,0) = 1, dim Λ^2 = C(4,2) = 6, dim Λ^4 = C(4,4) = 1, so the
even-exterior generating polynomial is Q_M(χ) = 1 + 6χ + χ². ∎

**Claim 35 (15.VIII.C1), PROVED.** χ²Q_M(χ⁻¹) = χ²(1 + 6χ⁻¹ + χ⁻²)
= χ² + 6χ + 1 = Q_M(χ). With χ = e^{−v} (from v = −2ln r, χ = r²):
Q_M/χ = χ + 6 + χ⁻¹ = 2cosh v + 6. ∎

**Claim 36 (15.VIII.D2), PROVED.** P_0 = 1 + 6r² + r⁴ = Q_M(r²) ✓.
P_{+1} = 1+4r+6r²+4r³+r⁴ = (1+r)⁴ ✓; P_{−1} = (1−r)⁴ ✓ (binomial expansion).

**Claim 37 (15.VIII.T2), PROVED.** Parent identity: with A_δ = δ(1+r²) + 2r,
A_δ² = δ²(1+r²)² + 4δr(1+r²) + 4r²; adding (1−δ²)(1+r²)² gives
(1+r²)² + 4δr(1+r²) + 4r² = 1 + 4δr + 6r² + 4δr³ + r⁴ = P_δ. ∎
At δ = 0: Q_M(r²)/(4r²) = (1+6r²+r⁴)/(4r²); with χ = r² = e^{−v},
= (χ⁻¹ + 6 + χ)/4 = (2cosh v + 6)/4 = (cosh v + 3)/2 by claim 35.
Minimum: cosh v ≥ 1 with equality iff v = 0; cosh is strictly decreasing on
(−∞,0] and strictly increasing on [0,∞), so the minimum is unique at v = 0,
i.e. r = 1 (χ = 1, λ = 1/2, v = 0), value 2. ∎

### §15.IX — Representation bridge to the E8 threshold

**Claim 38 (15.IX.T1), ASSERTED.** Threshold admission: Books 14–15 structures
may be carried into the E8(−24) gateway analysis without status change. This is
a dependency/scope declaration admitting the host — explicitly not a derivation,
correctly labeled MA on the page.

**Claim 39 (15.IX.T2), ASSERTED.** Threshold closure: the pre-E8 chain status
accounting is a meta-summary, asserted not proved (page's MA tag).

**Claim 40 (15.IX.T3), CHECKED.** Canonical round-trip normalization (common
scalar factor c = 1): the page's two-line proof, cited from the book's
verification suite; not reconstructed here.

**Claim 41 (E8 30380 weight table), CHECKED.** Exact integer (Freudenthal)
computation — Weyl dimension 30380, 4 dominant weights, exact multiplicity sum
30380 — established as SC in `~/workspace/e8/` and cited from the book's tables
page; not re-run here.

**Claims 42–43 (E8 generator numerics), CHECKED.** Reported completed numerical
runs per the page: the 248 adjoint matrices (so(16)⊕S⁺ spinor construction)
satisfy the Jacobi identity with the 3-spinor Fierz check exactly 0.0 over
341,376 triples and yield 240 roots with the E8 Cartan matrix (NC); the 30380
representation's 248 sparse generators (44.4M nonzeros) give Casimir eigenvalue
120 (measured deviation 4.0e-10), Serre relations 1.7e-14, Cartan diagonals
reproducing the SC weight table (NC). Both constructions are complexified (no
real-form reality condition imposed). Cited from the page; not re-run here.

### §15.X — Operational status

**Claim 44 (15.X), ASSERTED.** Δ_op(Book 15) = ∅ — the bridges predict no new
independently measured observable. A status declaration (page's MA tag), not a
theorem; the local negative results (claims 18, 20, and the M15-F firewall) are
retained in the stack.

---

## 4. New axioms and assumptions beyond Euclid + seed + earlier books

(Analytic trigonometry itself is the largest one: the Elements contain no
sine/cosine/tangent functions. The ledgers confirm analytic trig is treated as
ST imported substrate across the campaign.)

- **NA-15-1.** Analytic trigonometric substrate: real sin/cos/tan/cot on
  (0, π/2) with the standard identities (Pythagorean, half/double-angle,
  complement laws), complex exponentials, and complex differentiation.
  Used by claims 1–9, 11–14, 21, 24, 32–37.
- **NA-15-2.** The canonical UNA primitive substrate and Saw chart data:
  the four primitives as declared objects; the chart sign ε, share λ,
  Ω = λ/(1−λ), H_Saw = λ(1−λ), and the positive bounded chart on which the
  exact reduction saw_up = ελ, saw_down = ε(1−λ) holds (the reduction itself
  is the book's symbolic computation, claim 10).
- **NA-15-3.** Complex/Hermitian linear-algebra substrate: the Pauli algebra,
  the Bloch representation, the quarter-phase lift ψ with its sign data
  (ε, s_Ω), the componentwise symmetric square Q_C, and the notion of an
  R_Y-even Hamiltonian (confinement to the I/Y operator algebra) used as the
  premise of the obstruction theorem (claim 18).
- **NA-15-4.** Native quarter-turn substrate: the transfer doublet (p,q) with
  p²+q² = 2, p′ = −q, q′ = p; the generator J with J² = −I; the symmetric-square
  readout Q_t (claim 19; commutator form claim 22 cited from the book's suite).
- **NA-15-5.** Operator-bigrading substrate: the specific commuting involutions
  σ_ext, σ_int (and K, B = −σ_y) with their witness matrices — imported data,
  verified exactly in the book's suite (claims 29–31).
- **NA-15-6.** The E8(−24) representation host as admitted input (M15-H):
  explicitly not derived in Book 15 (claim 38).
- **NA-15-7.** The firewall scope contracts M15-A…M15-H as declared boundary
  conditions (§6): not mathematical axioms, but load-bearing assumptions about
  what the mathematics is *not* allowed to imply downstream.

## 5. Firewalls (scope contracts, all ASSERTED)

- **M15-A:** the complementary swap is a substitution law usable downstream; it
  generates no time, transport, Hamiltonian, chirality, Hodge structure, or
  product duality.
- **M15-B1:** the (D₂, K₂) geometry is algebraic state geometry — not energy,
  momentum, or a boost.
- **M15-B2:** Z₂ is a mathematical phase coordinate — not yet a quantum, gauge,
  clock, Hodge, or E8 phase.
- **M15-C:** ε is factored out before squaring; Saw complement is an involutive
  chart swap, not a Hodge or product duality.
- **M15-D:** "Hodge" remains a conditional bridge interpretation until the
  gateway supplies operator matching.
- **M15-E:** Saw complement (order 2) is not product duality; the native J is
  not automatically Hodge or E8.
- **M15-F:** the bigrading is an operator bridge awaiting representation
  realization — no unconditional E8 theorem.
- **M15-G:** the 4-manifold of §15.VIII is not yet identified with a spacetime
  tangent space; no cosmology follows.
- **M15-H:** constrains Book-16 ordering; no backward strengthening of Book 15.

## 6. Status summary

- PROVED: 28 (claims 1–9, 11–14, 15-balance, 16, 18, 20, 21, 24, 26, 27,
  32-lemma, 33–37)
- CHECKED: 11 (claims 10, 15-R_Y, 22, 23, 29, 30, 31, 40, 41, 42, 43)
  — all cited from the book's reported verification suites / established
  workspace computations; none re-run here (stated at each claim).
- ASSERTED: 18 (claims 17, 19, 25, 28, 32-full, 38, 39, 44; firewalls M15-A…H;
  substrate definitions D-6/D-8/D-9/D-10 as imported data)
- INCOMPLETE: 0

No-Euclid-wholesale boundary honored: no proposition of the Elements is invoked
as the source of any trigonometric, complex, operator-algebraic, or E8 content.
Everything analytic rests on the declared substrate axioms NA-15-1…NA-15-7 plus
the campaign seed; the firewalls M15-A…M15-H are the explicit record of what the
book refuses to let the mathematics imply.
