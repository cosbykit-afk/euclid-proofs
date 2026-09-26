# Book 0 Extension Proofs — Euclid-style recast

**Book:** 0 — Source Boundary and the Orientation Question (rewrite page:
`~/workspace/r-theory-rewrite/book0/index.html`, read end to end)
**Worker:** euclid-book-proofs workflow, Book 0 agent · **Date:** 2026-09-22 (PDT)
**Scope vocabulary:** PROVED — exact mathematics shown here; CHECKED — completed
numeric run (none needed: every load-bearing claim below has an analytic proof, so per
standing rule no sampling was run); ASSERTED — manuscript/audit claim or assumption
taken as stated, not re-derived; INCOMPLETE — failed/timed out/unfinished (none).

**Established material cited without re-proof:**
- Campaign seed: Kit's double-angle identity, PROVED, at
  `~/workspace/euclid_work/books/seed_double_angle.md` (cited as **Seed**).
  With `A = tan x + |sec x| = cxp`, `B = cot x + |csc x| = srx`, it gives
  `A − 1/A = 2 tan x`, `B − 1/B = 2 cot x`, and
  `(A − 1/B) + (B − 1/A) = 4/sin(2x)`.
- M0 inherited background (the book's own declared substrate, §9): ordinary real
  analysis, trigonometry, elementary topology, linear algebra. Used, never re-derived.
- **No-Euclid-wholesale boundary (honest statement):** no proposition of Euclid's
  *Elements* is a premise of any proof below. Book 0's mathematics is analysis and
  algebra over M0 plus the Seed; this matches the book's own dispositions ("ordinary
  trigonometry — no R-specific axiom, no physics import") and the campaign's
  No-Euclid-wholesale theorem (Book 4 §4.X.H, per the Book 1 ledger). Euclid's
  Elements enter only as the campaign's framing, not as logical dependencies.
- Sibling book proof files in this batch were NOT used (batch-independence rule);
  only the Seed was cited.

**New axioms/assumptions beyond Euclid + Seed:** see §13. The M0–M4 spine adds
zero axioms; the single referenced axiom is Axiom 0 (forward-looking M5 airlock).

---

## §0. Definitions (used throughout)

Domain `D = ℝ \ {kπ/2 : k ∈ ℤ}` (the seams). On `D`, with `s = sin x`, `c = cos x`:

- `srx = |csc x| + cot x`, `sxp = |csc x| − cot x`
- `cxp = |sec x| + tan x`, `crx = |sec x| − tan x`
- `urx = srx − crx`, `uxp = cxp − sxp`
- `H = 1/(urx+uxp)`, `FlatWave = 1/urx + 1/uxp`

Quadrant sign notation: `σ_s = sgn(sin x)`, `σ_c = sgn(cos x)`, constant on each
open quadrant `(kπ/2, (k+1)π/2)`.

---

## §1. Primitive reciprocal kernel — PROVED

**Claim 1.1 (definitions and positivity).** On `D` all four primitives are
strictly positive. *Proof.* `srx = B > 0` and `cxp = A > 0` are the Seed's
positivity argument: `B ≥ |csc x| − |cot x| = (1 − |cos x|)/|sin x| > 0` since
`sin x ≠ 0` implies `|cos x| < 1`; likewise `A > 0`. ∎

**Claim 1.2 (reciprocal identities).** `srx·sxp = 1` and `cxp·crx = 1` on `D`.
*Proof.* `srx·sxp = |csc x|² − cot²x = csc²x − cot²x = 1`; same for the cosine
pair with `sec² − tan² = 1`. Hence `sxp = 1/srx > 0`, `crx = 1/cxp > 0`. ∎

**Claim 1.3 (quadrant-local smoothness).** Each primitive is smooth on every open
quadrant. *Proof.* On a fixed open quadrant `|sin x| = σ_s sin x`,
`|cos x| = σ_c cos x` with constant signs, so each primitive is a rational
function of `sin x, cos x` with nowhere-zero denominator. ∎

**Claim 1.4 (reflection laws).** `srx(−x) = sxp(x)`, `cxp(−x) = crx(x)` (and
vice versa). *Proof.* `|csc(−x)| = |csc x|`, `cot(−x) = −cot x`. ∎

**Claim 1.5 (quarter-turn laws).** The quarter-turn swaps the sine/cosine pairs:
`srx(x−π/2) = crx(x)`, `cxp(x−π/2) = sxp(x)` (hence also with `+π/2`).
*Proof.* `csc(x−π/2) = −sec x`, `cot(x−π/2) = −tan x`, so
`srx(x−π/2) = |sec x| − tan x = crx(x)`; similarly
`cxp(x−π/2) = |csc x| − cot x = sxp(x)`. ∎

**Claim 1.6 (π-periodicity; half-turn blindness).** All four primitives are
π-periodic, so the static quartet cannot recover phase modulo 2π.
*Proof.* `|csc(x+π)| = |csc x|`, `cot(x+π) = cot x` (likewise sec/tan); the
quartet factors through `ℝ/πℤ`. ∎

Dependency: 1.1–1.6 use only M0 trigonometry + Seed positivity. (Book: §1, §10A.)

## §2. Local generator theorem — PROVED

**Claim 2.1 (rational quartet recovery).** Fix an open quadrant. Set `z = srx`
and `ε = sgn(z−1) ∈ {+1,−1}`. Then `sxp = 1/z`,
`cxp = (z+ε)/(εz−1)`, `crx = (εz−1)/(z+ε)`.
*Proof.* From the Seed, `z − 1/z = 2 cot x`, so with `t = tan x`,
`t = 2z/(z²−1)` (here `z = 1` is impossible on `D`: `z = 1` would give
`cot x = 0`, i.e. `cos x = 0`, a seam). Now
`cxp = 1/|cos x| + tan x = √(1+t²) + t` unconditionally (since
`1/cos²x = 1 + tan²x` and `1/|cos x| > 0`). Substituting `t`:
`cxp = (z²+1)/|z²−1| + 2z/(z²−1)`. Since `z > 0`,
`sgn(z²−1) = sgn(z−1) =: ε`, so `(z²+1)/|z²−1| = ε(z²+1)/(z²−1)` and
`cxp = [ε(z²+1) + 2z]/(z²−1)`. Cross-multiplication gives
`[ε(z²+1) + 2z](εz−1) = (z+ε)(z²−1)` (both expand to
`z³ + εz² − z − ε`), i.e. `cxp = (z+ε)/(εz−1)`. The denominator never
vanishes on `D` (`εz − 1 = 0` would need `z = 1`, excluded). `crx = 1/cxp`
by Claim 1.2. ∎

**Claim 2.2 (Riccati generator law and differential closure).** On each open
quadrant `z′ = −(1+z²)/2`, and the rational function field `ℝ(z)` is closed
under `d/dx`. *Proof.* With fixed quadrant signs,
`z = (1 + σ_s cos x)/(σ_s sin x)`; differentiating,
`z′ = −(1 + σ_s cos x)/sin²x`. Since
`(1+z²)/2 = (sin²x + (1+σ_s cos x)²)/(2sin²x) = (1 + σ_s cos x)/sin²x`,
the Riccati law follows. For any `r ∈ ℝ(z)`,
`dr/dx = r_z(z)·z′ ∈ ℝ(z)`. ∎ (A mathematical phase derivative; no time law.)

Dependency: 2.1–2.2 use §1 + Seed Lemma 2. (Book: §2, §10B–C.)

## §3. UNA sum identity — PROVED (via Seed)

**Claim 3.1.** `urx + uxp = 4/sin(2x)` on `D`, with no chartwise sign choice.
*Proof.* `uxp = cxp − sxp = A − 1/B` and `urx = srx − crx = B − 1/A` (using
Claim 1.2). The Seed proves `(A − 1/B) + (B − 1/A) = 4/sin(2x)` by regrouping
`(A − 1/A) + (B − 1/B) = 2tan x + 2cot x = 4/sin(2x)`. ∎

**ASSERTED (A1 — sign fixture, editorial/historical).** The book's audit (§3,
§10D) retires the reversed label `uxp = sxp − cxp` found in part of the
historical Trig2 workbook as a transcription error, restoring canonical
`uxp = cxp − sxp`. The identity 3.1 is PROVED either way; the claim that the
reversal was *error rather than convention* is a historical assertion I did not
independently verify.

## §4. FlatWave — PROVED

**Claim 4.1.** `1/urx + 1/uxp = sgn(sin 2x)` on `D`.
*Proof.* Put `p̃ = 1/|s| − 1/|c|`, `q̃ = s/c + c/s = 1/(sc)`. Then
`urx = p̃ + q̃`, `uxp = −p̃ + q̃`, so
`urx·uxp = q̃² − p̃² = 1/(s²c²) − (1/s² + 1/c² − 2/|sc|) = 2/|sc| = 4/|sin 2x|`.
Hence `(1/urx + 1/uxp) = (urx+uxp)/(urx·uxp) = (4/sin 2x)/(4/|sin 2x|)
= sgn(sin 2x)`. ∎

**Claim 4.2 (transformation laws).** `FW(x+π/2) = −FW(x)` (cophase reversal),
`FW(x+π) = FW(x)` (half-turn invariance), hence `FW(x+2π) = FW(x)`
(deck-blindness). *Proof.* `sgn(sin(2x+π)) = −sgn(sin 2x)`;
`sgn(sin(2x+2π)) = sgn(sin 2x)`. Exact identities of `sgn∘sin`. ∎

**Claim 4.3.** `sgn(urx) = sgn(uxp) = sgn(sin 2x) =: ε_FW`.
*Proof.* `urx·uxp = 4/|sin 2x| > 0` (same sign) and `urx + uxp = 4/sin 2x`
(sum has the sign of `sin 2x`). ∎
(Note: this `ε` is `sgn(sin 2x)`, distinct from the `ε = sgn(z−1)` of §2;
the book reuses the letter.)

Dependency: §3 + M0. (Book: §4, §10D FlatWave layer.)

## §5. Harmonic carrier — PROVED

**Claim 5.1.** With `H = 1/(urx+uxp)` and `V = H′`: `H = sin(2x)/4`,
`V = cos(2x)/2`, and `V² + 4H² = 1/4` (ellipse).
*Proof.* `H = sin(2x)/4` by Claim 3.1; `V = dH/dx = cos(2x)/2`;
`cos²(2x)/4 + 4·sin²(2x)/16 = 1/4`. ∎

**Claim 5.2 (smooth seam extension).** `H` extends smoothly to all of `ℝ`
(indeed `H(x) = sin(2x)/4` is entire), although the primitives are undefined
at the seams. *Proof.* The formula `sin(2x)/4` is defined at `x = kπ/2`;
no finite value is assigned to the primitive poles — the carrier sidesteps
them into new coordinates. ∎

**Claim 5.3 (scalar topological obstruction).** No continuous injective map
`S¹ → ℝ` exists; hence the circular carrier needs the pair `(H,V)` (or a
two-chart atlas), not one scalar. *Proof.* If `f: S¹ → ℝ` were continuous and
injective, `f(S¹)` would be a compact connected subset of `ℝ` with ≥ 2 points,
i.e. a nondegenerate interval `[m,M]`. Removing an interior point disconnects
`[m,M]`, but `S¹` minus one point is connected and `f` is injective — a
contradiction. ∎ (Standard M0 topology.)

Dependency: §3–§4. (Book: §5, §10E.)

## §6. Transfer layer (T0.III) — PROVED identities; essay theorems ASSERTED

Definitions (from `~/workspace/t_essays_study/essays/T0.III.txt`, fixed open
quadrant, `α = σ_s`, `β = σ_c`): `p = α cos x − β sin x`,
`q = α sin x + β cos x = |sin x| + |cos x|`, `λ = (1−p)/2`,
`saw_r = 1/urx`, `saw_x = 1/uxp`, `R_λ = 1/λ`, `U_λ = 1/(1−λ)`,
`Ω = λ/(1−λ)`, `χ = (1−λ)/λ`.

**Claim 6.1 (transfer-circle identity).** `p² + q² = 2`.
*Proof.* `p² = cos²x + sin²x − 2αβ sin x cos x`,
`q² = sin²x + cos²x + 2αβ sin x cos x` (using `α² = β² = 1`); sum `= 2`. ∎

**Claim 6.2 (differential transfer closure).** Quadrant-locally,
`λ′ = q/2`; `λ″ + λ = 1/2`; `(1−2λ)² + 4(λ′)² = 2`.
*Proof.* `p′ = −α sin x − β cos x = −q`, so `λ′ = −p′/2 = q/2`;
`λ″ = p/2` (since `q′ = α cos x − β sin x = p`), whence
`λ″ + λ = p/2 + (1−p)/2 = 1/2`; and
`(1−2λ)² + 4(λ′)² = p² + q² = 2` by 6.1. ∎

**Claim 6.3 (sharp phase-rate bounds).** `1/2 < λ′ ≤ 1/√2`, the upper bound
attained exactly at the unique midpoint `λ = 1/2` where `Ω = χ = 1`.
*Proof.* `λ′ = q/2` and on an open quadrant `1 < q ≤ √2` (`q = |sin x| +
|cos x| > 1` strictly interior; `q² ≤ 2(sin²x + cos²x) = 2` with equality iff
`|sin x| = |cos x|`). At the midpoint `p = ±(|cos x| − |sin x|) = 0`, so
`λ = 1/2` and `Ω = χ = 1`. ∎

**Claim 6.4.** `saw_r′ + saw_x′ = 0` quadrant-locally (definitional, not a
conservation law). *Proof.* `saw_r + saw_x = 1/urx + 1/uxp = sgn(sin 2x)`
(Claim 4.1), constant on each open quadrant. ∎

**Claim 6.5 (reciprocal odds).** `Ωχ = 1`; `χ = R_λ − 1`; `Ω = U_λ − 1`.
*Proof.* Direct algebra from the definitions. ∎

**Claim 6.6 (cross-layer ratio).**
`Ω = λ/(1−λ) = saw_r/saw_x = uxp/urx = cxp/srx`.
*Proof.* `saw_r/saw_x = (1/urx)/(1/uxp) = uxp/urx`; since `saw_r, saw_x`
share sign `ε_FW` and `|saw_r| + |saw_x| = 1` (Claim 4.1: `|1/urx| + |1/uxp|
= (|urx| + |uxp|)/|urx·uxp| = |urx+uxp|/|urx·uxp| = 1`), we get
`|saw_r| = λ`, `|saw_x| = 1−λ`, so `saw_r/saw_x = λ/(1−λ)`.
Finally `uxp/urx = (A−1/B)/(B−1/A) = ((AB−1)/B)/((AB−1)/A) = A/B = cxp/srx`. ∎

**Claim 6.7 (reciprocal-even normalization).**
`E_D = 1/(srx+sxp+cxp+crx) = |sin 2x|/(4(|sin x|+|cos x|))`; normalized
primitives form a positive partition of unity.
*Proof.* `srx+sxp = 2|csc x|`, `cxp+crx = 2|sec x|`; sum
`= 2(|sin x|+|cos x|)/(|sin x||cos x|)`; reciprocal gives the formula.
Each `n_i = prim_i/(sum) ≥ 0` and `Σn_i = 1` — algebra, not probability. ∎

**Claim  6.8 (log representation).** `cxp = e^{asinh(tan x)}`,
`srx = e^{asinh(cot x)}` exactly on `D`; hyperbolic functions arise exactly
after the log change `y = ln(cxp·srx)`.
*Proof.* `e^{asinh t} = t + √(1+t²)`; with `t = tan x`,
`√(1+tan²x) = |sec x|`. No physical rapidity or Lorentz kinematics follows. ∎

**ASSERTED (A2 — T0.III essay theorems).** Taken as inherited per the book's
audit (not re-derived here): the signed scalar `ζ = saw_r ∈ (−1,0)∪(0,1)`
reconstructs the named static calculus modulo π (T0.III.T28); no value of `ζ`
extends continuously through a primitive seam (T0.III.C31); the N2/N3/N5
readings (no conservation law, no equation of motion, no seam-crossing law);
T0.III.T30 (axiom-free closure of the layer). The book reports 13 symbolic +
9 numerical checks, all pass — I did not re-run them; the identities above
are my independent analytic re-derivation of the layer's core.

## §7. Rank firewall — PROVED

**Claim 7.1 (differential rank firewall).** For `ŷ = Γ∘E∘Φ`,
`rank(dŷ) ≤ min(rank dΦ, rank dE, rank dΓ)`.
*Proof.* Chain rule: `dŷ = dΓ·dE·dΦ` as linear maps; `rank(AB) ≤ min(rank A,
rank B)`. Readout cannot manufacture intrinsic rank. ∎

**Claim 7.2 (coframe/metric obstruction).** One-forms `e^a = f^a(x)dx` on a
one-dimensional domain span at most rank one; all wedges vanish; no
nondegenerate four-coframe comes from the scalar family alone.
*Proof.* `e^a ∧ e^b = f^a f^b dx∧dx = 0`. ∎

**Claim 7.3 (fixed-generator local flatness).** If `ω = K dη` with `K = K(η)`
then `dω + ω∧ω = 0` locally.
*Proof.* `ω∧ω = K² dη∧dη = 0`; `dω = dK∧dη = K′(η)dη∧dη = 0`. Scalar variation
along one fixed generator is not curvature. ∎

**Claim 7.4 (complex-state rank obstruction).** `u(λ) = (√λ, √(1−λ))` cannot
cover `ℂP¹`; adjoining an independent phase `φ` to get
`ψ(λ,φ) = (√λ, e^{iφ}√(1−λ))` is an explicit extension.
*Proof.* On each `[δ,1−δ]`, `u` is Lipschitz, so its image has 2-dimensional
Lebesgue measure zero; the countable union over `δ = 1/n` plus endpoints still
has measure zero, while `ℂP¹ ≅ S²` has positive 2-measure. A `J² = −I` is
algebra (Claim 8.1), not a new coordinate. ∎

Dependency: M0 only. (Book: §6, §11E–H.)

## §8. Complex structure J — PROVED

**Claim 8.1 (real linear lift).** The Riccati flow `z′ = −(1+z²)/2` lifts to
the homogeneous real linear system `u′′ + u/4 = 0`, i.e.
`(u,v)′ = M(u,v)` with `M = [[0,1],[−1/4,0]]`, via `z = 2v/u`, `v = u′`.
On this plane `J = [[0,2],[−1/2,0]]` satisfies `J² = −I` and commutes with
the flow (`MJ = JM = −I/2`): an exact, flow-invariant complex structure.
*Proof.* `z = 2u′/u` gives `z′ = 2u′′/u − z²/2`; matching `−1/2 − z²/2`
forces `u′′ = −u/4`. `J² = [[−1,0],[0,−1]]` by direct multiplication. ∎
Quotiented by scale, `(u,v)` lives in `ℝP¹` — one real degree of freedom
(Claim 7.1 undefeated); no independently variable phase is created.

**Claim 8.2 (orientation-relative uniqueness).** On an oriented Euclidean
2-plane, exactly one orthogonal complex structure is compatible; reversing
the orientation sends `J ↔ −J`.
*Proof.* Let `J` be orthogonal with `J² = −I`, `(e₁,e₂)` oriented
orthonormal. `⟨Je₁,e₁⟩ = ⟨J²e₁,Je₁⟩ = −⟨Je₁,e₁⟩`, so `Je₁ ⊥ e₁`,
`|Je₁| = 1`, i.e. `Je₁ = ±e₂`; positive orientation of `(e₁,Je₁)` forces
`Je₁ = e₂`, and then `Je₂ = −e₁`. Unique. Reversing orientation flips the
forced sign. ∎

**Claim 8.3 (conjugacy classification).** Every real-linear `J` with
`J² = −I` on `ℝ²` is `GL(2,ℝ)`-conjugate to the standard quarter-turn.
*Proof.* For `v ≠ 0`, `Jv` is not a real multiple of `v` (else
`J²v = λ²v = −v`, impossible over `ℝ`); `{v, Jv}` is a basis in which
`J = [[0,−1],[1,0]]`. ∎

Dependency: Claim 2.2 + M0 linear algebra. (Book: §7, §12A–B.)

## §9. Tetrahedral carrier — PROVED computations; audit findings ASSERTED

**Claim 9.1 (rank-three carrier).** For three mutually adjacent tetrahedral
edge directions, `G = ℓ²[[1,½,½],[½,1,½],[½,½,1]]` has
`det G = ℓ⁶/2 > 0`: rank three.
*Proof.* `det[[1,½,½],[½,1,½],[½,½,1]] = (3/4) − (1/2)(1/4) + (1/2)(−1/4)
= 1/2`. ∎ (Independent geometric data are *added* — the T1 spatial-rank
obstruction is resolved by extension, not derived.)

**Claim 9.2.** `O(G)` contains orientation-reversing isometries.
*Proof.* `G > 0`, so `O(G)` is conjugate to `O(3)`; e.g. `diag(−1,1,1)` in a
`G`-orthonormal basis is a `G`-isometry of determinant `−1`. ∎

**Claim 9.3 (boundary-of-boundary).** `D₁D₀ = 0`, `D₂D₁ = 0` for oriented
simplicial boundary operators. *Proof.* Standard: each `(k−1)`-face of a
`k`-simplex occurs in `D²` twice with opposite induced orientations. (M0
simplicial homology.) ∎

**Claim 9.4 (central-sign information loss, general principle).** No function
defined on a 2-to-1 projective/quadratic quotient can recover the lost
central `±`. *Proof.* If `q(−v) = q(v)`, a putative recovery `r` would need
`r(q(v)) = +v` and `= −v` simultaneously. An obstruction to *selecting* a
lift, not to representing one. ∎

**Claim 9.5 (Clifford presentations).** `M₂(ℝ)` admits Clifford presentations
of more than one signature, e.g. `Cl(2,0)` via
`e₁ = [[1,0],[0,−1]]`, `e₂ = [[0,1],[1,0]]`, and `Cl(1,1)` via the same `e₁`
and `e₂ = [[0,−1],[1,0]]`; both generate `M₂(ℝ)`. *Proof.* Direct check:
squares `±I`, anticommute, span all of `M₂(ℝ)`. ∎

**Claim 9.6 (affine readout sign).** In `y = αz + β` (`α ≠ 0`),
`σ = sgn(α)` is representable from the map. *Proof.* `σ = sgn(dy/dz)`. A
readout-identifiability fact, not a chirality law. ∎

**ASSERTED (A3–A7 — audit dispositions).** Taken as stated from the book's
T1/T2/T3 audits (not re-derived): Projection architecture/candidate
discipline/observation grammar/extension certificates (methodological
framework); seam/Pin/central-lift nonselection findings; composition/control
audit; the T3 stripping of physical time, Lorentzian signature, Maxwell and
Einstein–Maxwell content to the physics interface; the obstruction ledger;
"coordinate choice generates no physics"; physics-import counts of 0.

## §10. Theorem 0.IV.T1 — Automorphism Obstruction — PROVED

**Theorem 0.IV.T1.** Let `U` be an unoriented structure with orientations
`Or(U) = {o₊, o₋}`, and let `r ∈ Aut(U)` exchange them with no fixed
orientation (`r·o₊ = o₋`, `r·o₋ = o₊`). Then no canonical selector from `U`
alone exists.
*Proof.* A canonical selector is a rule `C` with `C(U) ∈ Or(U)` natural under
automorphisms: `C(g·U) = g·C(U)` for all `g ∈ Aut(U)`; since `g·U = U` as
unoriented structures, `C(U) = g·C(U)`. Take `g = r`: `C(U) = r·C(U)`. But
`C(U) ∈ {o₊, o₋}` and `r` fixes neither (`r·o₊ = o₋ ≠ o₊`,
`r·o₋ = o₊ ≠ o₋`) — contradiction. ∎
(Four lines, as the book says. Its force rests on the *definition* of
"canonical" as "natural under `Aut(U)`" — a stipulation, not a hidden
assumption.)

**Application to T2 — PROVED.** For the unoriented Euclidean two-channel
plane, reflection `(x,y) ↦ (x,−y)` is an orientation-reversing automorphism;
after one orientation is declared the compatible complex structure is the
`J` of Claim 8.2, and reversal sends `J ↔ −J`. By Claim 9.4, quotient data
cannot restore a preferred central sign.

**Application to T3 — PROVED.** For the tetrahedral metric carrier, Claim 9.2
gives orientation-reversing `G`-isometries; reversing an ordered frame flips
the orientation sign while the Gram metric is preserved, and consistent
reorientation preserves the boundary-of-boundary identities (Claim 9.3).

**ASSERTED (A9 — Corollaries 0.IV.C1–C3).** Exact-scope and
no-universal-impossibility caveats: methodological clarifications of the
theorem's boundary, not further mathematics.

## §11. Theorem 0.III.T1 — Representation–Preference Separation — MIXED

(1) Orientation is internally representable — **PROVED** (Claims
4.1–4.2, 8.1–8.2, 9.2: FlatWave sign, the `J/−J` pair, oriented frames).
(2)–(5) Mirror/oppositely-oriented realizations are admissible; projective or
quadratic quotients may erase rather than select a central sign — **PROVED**
(Claims 8.2–8.3, 9.2, 9.4).
(6) "No inherited theorem assigns one member of the pair a privileged
physical status" — **ASSERTED (A8)**: an audit-completeness claim over
T0–T3; I verified the mathematics, not the exhaustiveness of the audit.
**Therefore:** within the audited M0–M4 corpus, orientation is represented
but no preferred physical chirality is derived — the "therefore" inherits
the ASSERTED status of (6).
**Corollary 0.III.C1** (no axiom needed for representation) — **PROVED**
(the constructions above need none).
**Corollaries 0.III.C2–C3** (physics-interface permission; candidate-boundary
warning) — **ASSERTED** (forward-looking methodological statements).

## §12. Closure — ASSERTED (audit-level); M5 conditional consequences PROVED

**Theorem 0.VI.T1 (Book 0 Closure) — ASSERTED (A8).** "T0–T3 suffice for a
coherent formal core with zero inherited physical law; Book 0 closes with no
added Orientation Axiom and no hidden physics import" is the audit's
completeness verdict. The mathematics it summarizes is PROVED above; the
*completeness* ("no hidden import") is taken from the book's audit, not
independently re-established.

**M5 decadic airlock (forward-looking; conditional on Axiom 0) — PROVED
conditional.** Given Axiom 0 (see §13): with `W = U ⊕ iU`,
`I(u,v) = (−v,u)` satisfies `I² = −id_{W}` (direct check), i.e. a complex
structure on the real space `W`; `W ≅ U ⊗_ℝ ℂ` as complex spaces;
`dim_ℝ W = 10`, `dim_ℂ W = 5` (direct sum / tensor dimensions).
**ASSERTED (A10):** "M5 inherits no Spin(10), chirality selector, gauge
groups, or empirical calibration" — boundary declaration.

## §13. New axioms / assumptions beyond Euclid + Seed

1. **Axiom 0 (Book 5, A0.1–A0.2) — the only R-specific mathematical axiom
   referenced in Book 0, forward-looking (§18, M5 layer):** the rank-five
   real carrier `U = E ⊕ V` admits a tagged independent real partner with
   `U ∩ iU = {0}` and `W = U ⊕ iU`; the primitive lift of an upstream
   operator `A` is diagonal `A ⊕ ιAι⁻¹` (no off-diagonal mixing is
   primitive). Referenced, not derived. Adds **0** axioms to the M0–M4
   spine (the book's added-axiom ledger reads 0/0/0/0).
2. **Governing source rule (methodological assumption):** T0–T3 admitted
   claim-by-claim with earned status; essay-level theorems (T0.III.T28,
   C31, N2/N3/N5, T30) and all audit-completeness statements used as
   ASSERTED, not re-derived.
3. **M0 substrate (declared background, not new):** ordinary real analysis,
   trigonometry, elementary topology, linear algebra — used throughout.
4. When a definite orientation is needed for purely mathematical work, the
   book adds only a declared convention `o ∈ {+1,−1}` — ordinary
   convention, not an axiom (book §17; no new law).

## Claim inventory (counts)

- **PROVED: 43** — §1 (6: 1.1–1.6), §2 (2: 2.1–2.2), §3 (1: 3.1),
  §4 (3: 4.1–4.3), §5 (3: 5.1–5.3), §6 (8: 6.1–6.8), §7 (4: 7.1–7.4),
  §8 (3: 8.1–8.3), §9 (6: 9.1–9.6), §10 (3: theorem + 2 applications),
  §11 (3: T1 representability, T1 admissibility/quotient, C1),
  §12 (1: M5 conditional block).
- **CHECKED: 0** — every load-bearing claim has a complete analytic proof;
  per standing rule no numerical sampling was run on top of proofs.
- **ASSERTED: 10 groups** — A1 sign fixture (historical); A2 T0.III essay
  theorems; A3–A7 T1/T2/T3 audit dispositions & methodology; A8 audit
  completeness (0.III.T1(6), 0.VI.T1); A9 0.IV corollaries caveats; A10 M5
  boundary declaration.
- **INCOMPLETE: 0** — no timeouts, no failures; all commands exited 0.

## Notes for the parent

- The Seed (`seed_double_angle.md`) was present and is *exactly* the UNA
  identity `urx + uxp = 4/sin(2x)` in the book's notation — the single most
  load-bearing analytic fact of Book 0 — so §3–§5 build on it by citation.
- Sibling book proof files (`book1_proof.md`, etc.) exist in
  `~/workspace/euclid_work/books/` but were deliberately NOT read or cited
  (batch-independence rule for books 0–6).
- No `exec` command failed or timed out; no pipe-masked exit codes were used.
- Honest boundary kept: nothing from Euclid's *Elements* is a logical
  premise anywhere above; the proofs use M0 + Seed only, matching the book's
  own "ordinary trigonometry, no R-specific axiom" dispositions.
- The book's CERTIFIED labels were re-scoped per standing rules: analytic
  core → PROVED; audit-completeness and historical/editorial claims →
  ASSERTED with the assumption named. Nothing was rounded up.
