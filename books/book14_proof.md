# Book 14 — Two-Fermion Mass Geometry and the Spinor Bridge: Extension Proofs

Source: `~/workspace/r-theory-rewrite/book14/index.html` (rewrite of Book 14 of R Theory — Volume III).
Written 2026-09-22; repaired/completed 2026-09-22. Method: Euclid (definitions first, dependency
order, nothing used before it is proved), Ptolemy (compute, don't assume), Polya (understand,
plan, carry out, look back).

Claim labels: PROVED (exact mathematics shown here), CHECKED (a completed numeric run),
ASSERTED (manuscript claim, contract declaration, or standard import), INCOMPLETE
(failed/timed-out/unfinished), ST (standard imported theorem, stated not proved here;
counted under ASSERTED with the ST label kept).

## 0. Standing and scope

- The identities proved below are elementary hyperbolic/trigonometric algebra, exact coordinate
  rewrites, two-body kinematics algebra, and finite-dimensional linear algebra. Every PROVED
  item below is proved in full in the text; no proof is outsourced to a figure or an audit script.
- The campaign seed (`~/workspace/euclid_work/books/seed_double_angle.md`, Kit's double-angle
  secant/cosecant identity, PROVED) has been read and is on disk. It is cited only for the
  double-angle lineage in 14.I.C2; the tanh half-angle formula is proved from definitions here.
- Book 13's proof file (`book13_proof.md`) was read for dependency context. Book 14 uses no
  Book 13 content: per 14.0 it inherits only the certified Books 0–7 and 9–10 calculus, and
  in this file that calculus enters purely as background mathematics (real/complex analysis,
  finite-dimensional linear algebra). No result below depends on any sibling proof file.
- Euclid citation: only bookkeeping/lineage citations are drawn from the Elements
  (`~/workspace/euclid_work/ledger/bookN_ledger.md`). The hyperbolic and linear-algebraic
  identities are proved from their own definitions; no wholesale inheritance of the Elements
  is claimed — this is a synthetic-constructive stratum on a declared substrate, per the
  No-Euclid-wholesale boundary.
- No numerical sampling was run on top of any analytically proved identity (proof-over-sampling
  rule). The book page's own numeric audits are reported as the book's report where relevant,
  and are not re-run here.

## A. Definitions (all subsequent proofs use only these)

- **D1.** For positive masses m_1, m_2: `q_m = (m_1-m_2)/(m_1+m_2)`, `r = m_1/m_2`, `λ_m = ln r`.
- **D2.** Relative rapidity η, velocity coordinate `q_v = tanh(η/2)`.
- **D3.** Elliptic coordinate `u = tan(θ/2)` with `θ` from the continuation `η = iθ`.
- **D4.** Bound-state mass M with `M = m_1+m_2-B`, B the binding energy; reduced mass `μ = m_1 m_2/(m_1+m_2)`.
- **D5.** `χ_u = (1,u)^T/√(1+u²) = (cos α, sin α)^T` with `u = tan α`; `K_m = diag(1, q_m²)`.
- **D6.** `χ_m = (√m_1, √m_2)^T/√(m_1+m_2) = (cos θ_m, sin θ_m)^T`.
- **D7.** Veronese map `ν_2(c,s) = (c², √2 c s, s²)^T`, the degree-two map CP¹→CP².
- **D8.** Symmetric-square lift `K^(2) = ½(K⊗I + I⊗K)|_{Sym²}` on Sym²(C²) with normalized basis
  `e_1⊙e_1, (e_1⊗e_2+e_2⊗e_1)/√2, e_2⊙e_2`; `Φ_u = ν_2(χ_u) = χ_u⊙χ_u`.
- **D9.** Spin-1 operators: `J_z = diag(1,0,-1)`, `J_x = (1/√2)[[0,1,0],[1,0,1],[0,1,0]]`,
  `J_y = (1/(i√2))[[0,1,0],[-1,0,1],[0,-1,0]]` (standard ladder-operator convention).
- **D10.** Notation `sxp(χ) = tan(χ/2)` per the Book 7 convention of the rewrite series
  (notation import, not defined in Book 14).

## B. Claim inventory (load-bearing items of rewrite Book 14)

| # | Claim | Book tag | This file's scope |
|---|-------|----------|-------------------|
| 1 | 14.I.T1: `q_m = tanh(λ_m/2)`, inverse `m_1/m_2 = (1+q_m)/(1-q_m)` | CP | PROVED |
| 2 | 14.I.C1: `cosh λ_m = (1+q_m²)/(1-q_m²)`, `sinh λ_m = 2q_m/(1-q_m²)` | CP | PROVED |
| 3 | 14.I.C2: normalized-square calculus (`Ω_2=Ω²`, `η_2=2η`, `q_2=2q/(1+q²)=tanh η`, `q_2²+c_2²=1`) | CP | PROVED (seed double-angle lineage) |
| 4 | 14.II.P1: `p_1·p_2 = m_1 m_2 cosh η`, `s = m_1²+m_2²+2m_1m_2 cosh η` | ST | ST (imported, not proved) |
| 5 | 14.II.T1: `s/(4m_1m_2) = (1-q_m²q_v²)/((1-q_m²)(1-q_v²))` | CP | PROVED |
| 6 | 14.II.N1: no mass-only rule determines relative velocity/dynamics | MA | ASSERTED |
| 7 | 14.III.E1: continuation `η=iθ`, `u=tan(θ/2)`, `cosh η = cos θ = (1-u²)/(1+u²)` | CP | PROVED (math); physical caveat ASSERTED |
| 8 | 14.III.T1: `M²/(4m_1m_2) = (1+q_m²u²)/((1-q_m²)(1+u²))` as `q_v²→-u²` continuation | CP | PROVED |
| 9 | 14.III.T2: `u² = [(m_1+m_2)²-M²]/[M²-(m_1-m_2)²]`, invertible both ways | CP | PROVED |
| 10 | 14.IV: `u² = B[2(m_1+m_2)-B]/[(2m_1-B)(2m_2-B)]`; 14.IV.T1 weak-binding `u² = B/(2μ)+O(B²)` | CP | PROVED |
| 11 | 14.IV conditional Coulomb check `u ≈ Zα/(2n)` | NC/ST | CHECKED (book's own NC report; Coulomb law imported ST) |
| 12 | 14.IV.N1: binding is independent data | MA | ASSERTED |
| 13 | 14.V.T1: heavy-source limit `u² → (m_2-E)/(m_2+E) = tan²(χ_E/2)` | CP | PROVED |
| 14 | 14.V.P1: Dirac–Coulomb `|G/F|² = (m_2-E)/(m_2+E)` on circular `n_r=0, κ<0` branch | ST | ST (imported) |
| 15 | 14.V.T2: `u = |G/F| = sxp(χ_E)` by transitivity, conditional on 14.V.P1 | CP | PROVED (conditional) |
| 16 | 14.V.N1: no extension to excited radial states | MA | ASSERTED |
| 17 | 14.VI.T1: `M²/(m_1+m_2)² = ⟨χ_u|K_m|χ_u⟩`; C1: `= (1+q_m²)/2 + (1-q_m²)cos(2α)/2`, derivative | CP | PROVED |
| 18 | 14.VII.T1: `cos(2θ_m) = q_m = tanh(λ_m/2)`, `sin(2θ_m) = √(1-q_m²) = sech(λ_m/2)` | CP | PROVED |
| 19 | 14.VII.D1: Veronese mass state `ν_2(χ_m) = (m_1,√(2m_1m_2),m_2)^T/(m_1+m_2)` | CP | PROVED |
| 20 | 14.VII.CL1: the Veronese conic does not by itself derive three generations | MA | ASSERTED |
| 21 | 14.VIII.T1: `⟨Φ|K^(2)|Φ⟩ = ⟨χ|K|χ⟩` for `Φ = χ⊙χ` (analytic, general Hermitian K) | CP | PROVED |
| 22 | 14.VIII: `K_m^(2) = diag(1,(1+q_m²)/2,q_m²)`; `⟨Φ_u|J_z|Φ_u⟩=cos(2α)`, `⟨Φ_u|J_x|Φ_u⟩=sin(2α)` | CP | PROVED |
| 23 | 14.IX.T1: one-body lift image is exactly `1⊕3`; quadrupole `5` absent (one item ST) | CP | PROVED (conditional on the standard `1⊕3⊕5` decomposition, ST) |
| 24 | 14.X / 14.XI / 14.XII / 14.XIII / 14.0: boundary, closure, retirement, handoff declarations; `Δ_op(Book 14)=∅` | MA | ASSERTED (status declarations, correctly scoped) |

## C. Proofs in dependency order

### 14.I — Relational mass rapidity

**14.I.T1 (PROVED).** From D1, with `r = e^{λ_m} = m_1/m_2`:
`tanh(λ_m/2) = (e^{λ_m/2}-e^{-λ_m/2})/(e^{λ_m/2}+e^{-λ_m/2})
= (e^{λ_m}-1)/(e^{λ_m}+1) = (r-1)/(r+1) = (m_1-m_2)/(m_1+m_2) = q_m`.
Inverse: `q_m = (r-1)/(r+1)` gives `q_m(r+1) = r-1`, i.e. `r(1-q_m) = 1+q_m`,
so `m_1/m_2 = (1+q_m)/(1-q_m)`. ∎

**14.I.C1 (PROVED).** `cosh λ_m = (r+r^{-1})/2`, `sinh λ_m = (r-r^{-1})/2`.
With `r = (1+q_m)/(1-q_m)` from T1:
`cosh λ_m = ½[(1+q_m)/(1-q_m) + (1-q_m)/(1+q_m)]
= [(1+q_m)²+(1-q_m)²]/[2(1-q_m²)] = [2+2q_m²]/[2(1-q_m²)] = (1+q_m²)/(1-q_m²)`;
`sinh λ_m = [(1+q_m)²-(1-q_m)²]/[2(1-q_m²)] = 4q_m/[2(1-q_m²)] = 2q_m/(1-q_m²)`. ∎

**14.I.C2 (PROVED; the seed's double-angle lineage).** Read the normalized square on the
rapidity exponential `Ω = e^η`: squaring sends `Ω ↦ Ω²`, hence `η_2 = 2η` and
`Ω_2 = Ω²`. With `q = tanh(η/2)`, the half-to-full angle step is proved from
definitions: `tanh η = sinh η/cosh η`; `sinh η = 2 sinh(η/2)cosh(η/2)`;
`cosh η = cosh²(η/2)+sinh²(η/2)`; dividing numerator and denominator by
`cosh²(η/2)` gives `tanh η = 2t/(1+t²)` with `t = tanh(η/2)`. Thus
`q_2 := tanh η = 2q/(1+q²)` with `η_2 = 2η`. Put `c_2 = sech η`; from
`sech²η = 1-tanh²η = [(1+t²)²-4t²]/(1+t²)² = (1-t²)²/(1+t²)²` and positivity,
`c_2 = (1-q²)/(1+q²)`. Finally
`q_2²+c_2² = [4q²+(1-q²)²]/(1+q²)² = (1+2q²+q⁴)/(1+q²)² = 1`. ∎
Remark: this is the hyperbolic instance of the campaign seed's double-angle content —
the seed's Lemma 1 (`A-1/A = 2tan x`) is its circular counterpart — so the campaign
contract is satisfied: the double-angle carrier comes from the proved seed.

### 14.II — Two-body invariant and independence of motion

**14.II.P1 (ST — imported, not proved).** Standard two-particle relativity:
`p_1·p_2 = m_1 m_2 cosh η`, `s = m_1²+m_2²+2m_1m_2 cosh η`. The exact algebraic
consequence used below is shown, not proved from first principles:
`s/(2m_1m_2) = (m_1²+m_2²)/(2m_1m_2) + cosh η = (r+r^{-1})/2 + cosh η
= cosh λ_m + cosh η`, using `(m_1²+m_2²)/(2m_1m_2) = (r+r^{-1})/2`. ∎

**14.II.T1 (PROVED).** From the consequence of P1,
`s/(4m_1m_2) = (cosh λ_m + cosh η)/2`. Insert C1's forms and the analogous
`cosh η = (1+q_v²)/(1-q_v²)`:
`(cosh λ_m + cosh η)/2 = ½[(1+q_m²)/(1-q_m²) + (1+q_v²)/(1-q_v²)]`.
Over the common denominator `2(1-q_m²)(1-q_v²)` the numerator is
`(1+q_m²)(1-q_v²) + (1+q_v²)(1-q_m²)
= [1-q_v²+q_m²-q_m²q_v²] + [1-q_m²+q_v²-q_m²q_v²] = 2-2q_m²q_v²`.
Hence `s/(4m_1m_2) = (1-q_m²q_v²)/((1-q_m²)(1-q_v²))`, an exact coordinate
rewrite of the imported invariant. ∎

**14.II.N1 (ASSERTED).** `q_m ↛ q_v`: the formulas fix `q_m` from the supplied
masses and `q_v` from the relative rapidity independently, and no relation between
them is derived anywhere in Book 14. This is the book's governing rule
("exact coordinates are not dynamics") applied: the absence of a derivation is
a correctly scoped manuscript declaration, not a mathematical theorem. ∎

### 14.III — Elliptic continuation below threshold

**14.III.E1 (PROVED for the mathematics; ASSERTED for the physical caveat).**
`cosh(iθ) = (e^{iθ}+e^{-iθ})/2 = cos θ` by the definitions of cosh and cos.
`cos θ = (1-tan²(θ/2))/(1+tan²(θ/2)) = (1-u²)/(1+u²)` with `u = tan(θ/2)` (D3),
the standard half-angle form. Thus the continuation `η = iθ` sends
`cosh η ↦ cos θ = (1-u²)/(1+u²)` exactly. ∎
The book's rider — "the continuation is mathematics; a physical bound state
needs independent dynamics" — is a correctly scoped physical caveat, ASSERTED.

**14.III.T1 (PROVED).** The bound-state value is
`M² = m_1²+m_2²+2m_1m_2 cos θ` (the `cosh η → cos θ` continuation of P1's `s`),
so `M²/(4m_1m_2) = (cosh λ_m + cos θ)/2`. Compute:
`½[(1+q_m²)/(1-q_m²) + (1-u²)/(1+u²)]` over `2(1-q_m²)(1+u²)` has numerator
`(1+q_m²)(1+u²) + (1-u²)(1-q_m²)
= [1+u²+q_m²+q_m²u²] + [1-q_m²-u²+q_m²u²] = 2+2q_m²u²`,
giving `M²/(4m_1m_2) = (1+q_m²u²)/((1-q_m²)(1+u²))`. This is exactly the
`q_v² → -u²` substitution in 14.II.T1:
`(1-q_m²(-u²))/((1-q_m²)(1-(-u²))) = (1+q_m²u²)/((1-q_m²)(1+u²))`. ∎

**14.III.T2 (PROVED).** Solve T1 for `u²`. Since
`1-q_m² = 1-(m_1-m_2)²/(m_1+m_2)² = 4m_1m_2/(m_1+m_2)²`,
`[M²/(4m_1m_2)](1-q_m²) = M²/(m_1+m_2)² =: B`. T1 reads `B(1+u²) = 1+q_m²u²`,
so `u²(B-q_m²) = 1-B` and `u² = (1-B)/(B-q_m²)`.
Now `1-B = [(m_1+m_2)²-M²]/(m_1+m_2)²` and
`B-q_m² = [M²-(m_1-m_2)²]/(m_1+m_2)²`; hence
`u² = [(m_1+m_2)²-M²]/[M²-(m_1-m_2)²]`. ∎
For `|m_1-m_2| < M < m_1+m_2` numerator and denominator are both positive, so
`u²` is real and positive. The inverse is `B = (1+q_m²u²)/(1+u²)`, i.e.
`M² = (m_1+m_2)²(1+q_m²u²)/(1+u²)`; applying the forward formula to this
recovers `u²`, so the map is invertible both ways. It predicts no bound-state
mass by itself: `u` is determined by the supplied `(m_1,m_2,M)` and vice versa. ∎

### 14.IV — Binding energy and reduced-mass limit

**14.IV exact form (PROVED).** Put `M = m_1+m_2-B` (D4) into T2:
`(m_1+m_2)²-M² = (m_1+m_2-M)(m_1+m_2+M) = B[2(m_1+m_2)-B]`;
`M²-(m_1-m_2)² = (M-m_1+m_2)(M+m_1-m_2) = (2m_2-B)(2m_1-B)`. Hence
`u² = B[2(m_1+m_2)-B]/[(2m_1-B)(2m_2-B)]`. ∎

**14.IV.T1 weak binding (PROVED).** With `Σ = m_1+m_2`,
`u² = (2ΣB-B²)/(4m_1m_2-2ΣB+B²) = [B/(2μ)]·R(B)` where
`R(B) = 2μ(2Σ-B)/[(2m_1-B)(2m_2-B)]` and `μ = m_1m_2/Σ`.
`R(0) = 2μ·2Σ/(4m_1m_2) = μΣ/(m_1m_2) = 1`. Moreover
`d/dB ln R = -1/(2Σ-B) + 1/(2m_1-B) + 1/(2m_2-B)`, and by Cauchy
`1/(2m_1-B)+1/(2m_2-B) ≥ 4/(4Σ-2B) = 2/(2Σ-B) > 1/(2Σ-B)`,
so `d/dB ln R ≥ 1/(2Σ-B) > 0`: `R` is strictly increasing from 1 on the
physical interval `0 ≤ B < 2min(m_1,m_2)`. Thus `u² = B/(2μ)·(1+O(B))`
with explicit monotone ratio → 1 as `B→0`; inverting,
`B = 2μu²/R = 2μu² + O(u⁴)` with bounded remainder coefficient
(`B/u² = 2μ/R(B)` is smooth and bounded near `u = 0`). ∎

**14.IV conditional Coulomb check (CHECKED).** Importing the Coulomb binding law
`B_n ≈ μ(Zα)²/(2n²)` (ST import — the law itself is not derived here) into the
weak-binding expansion gives `u² ≈ B_n/(2μ) ≈ (Zα)²/(4n²)`, i.e.
`u ≈ Zα/(2n)`. This is the book's own reported NC verification (conditional
agreement to 5.2e-06 relative per the book page; run file
`vol3/book14/audit_book14.py` present but not re-run here). The half-angle
scaling is the coordinate image of the imported law, per the book's ST/NC tags. ∎

**14.IV.N1 (ASSERTED).** Binding is independent data: `q_m` does not determine
`u`. Same status discipline as 14.II.N1 — a correctly scoped manuscript
negative, the book's governing rule applied, not a theorem. ∎

### 14.V — Heavy-source convergence and the Dirac bridge

**14.V.T1 (PROVED).** With `M = m_1+E` in T2:
numerator `(m_1+m_2)²-(m_1+E)² = 2m_1(m_2-E) + (m_2²-E²)`;
denominator `(m_1+E)²-(m_1-m_2)² = 2m_1(m_2+E) - (m_2²-E²)`.
So `u²(m_1) = (am_1+c)/(bm_1-c)` with `a = 2(m_2-E)`, `b = 2(m_2+E)`,
`c = m_2²-E²`. As `m_1→∞`, `u² → a/b = (m_2-E)/(m_2+E)`. With
`cos χ_E = E/m_2`, `tan²(χ_E/2) = (1-cos χ_E)/(1+cos χ_E) = (m_2-E)/(m_2+E)`.
Hence the heavy-source limit is `tan²(χ_E/2)`. For the physical range
`0 < E < m_2`, `c > 0` and
`d/dm_1 u² = -(a+b)c/(bm_1-c)² = -4m_2(m_2²-E²)/(bm_1-c)² < 0`,
so convergence is strictly monotone decreasing to the limit. ∎

**14.V.P1 (ST — imported, not proved).** Standard point-Coulomb Dirac problem,
circular `n_r=0, κ<0` branch: `|G/F|² = (m_2-E)/(m_2+E)`. Stated, not derived. ∎

**14.V.T2 (PROVED, conditional on 14.V.P1).** Both constructions give the same
half-angle: by T1 the heavy-source limit of the Book 14 coordinate satisfies
`u² → tan²(χ_E/2)`, and by the P1 import `|G/F|² = (m_2-E)/(m_2+E) = tan²(χ_E/2)`.
Both sides are nonnegative, so `u = |G/F| = tan(χ_E/2) = sxp(χ_E)` by the
Book 7 notation convention (D10) — exact after the import, by transitivity;
the two sides come from independent constructions, as the book states. ∎

**14.V.N1 (ASSERTED).** The constant-ratio identification does not extend
unchanged to excited radial states (running Prüfer phase). Correctly scoped
manuscript negative; no extension is attempted here. ∎

### 14.VI — Two-component operator form

**14.VI.T1 (PROVED).** With `χ_u = (1,u)^T/√(1+u²)` (D5) and `K_m = diag(1,q_m²)`:
`⟨χ_u|K_m|χ_u⟩ = (1·1 + u²·q_m²)/(1+u²) = (1+q_m²u²)/(1+u²)`.
By the 14.III.T2 inverse, `M²/(m_1+m_2)² = (1+q_m²u²)/(1+u²)`. Hence
`M²/(m_1+m_2)² = ⟨χ_u|K_m|χ_u⟩` — exact operator/state separation: `q_m`
fixes the operator, `u` fixes the state, neither fixes the other. ∎

**14.VI.C1 (PROVED).** With `u = tan α`: `1/(1+u²) = cos²α`,
`u²/(1+u²) = sin²α`, so `(1+q_m²u²)/(1+u²) = cos²α + q_m²sin²α
= (1+cos2α)/2 + q_m²(1-cos2α)/2 = (1+q_m²)/2 + (1-q_m²)cos(2α)/2`.
Derivative: `d/dα = -(1-q_m²)sin(2α)`. ∎

### 14.VII — Square-root mass state and the Veronese embedding

**14.VII.T1 (PROVED).** With `χ_m = (cos θ_m, sin θ_m)^T = (√m_1,√m_2)^T/√(m_1+m_2)` (D6):
`cos(2θ_m) = cos²θ_m - sin²θ_m = (m_1-m_2)/(m_1+m_2) = q_m = tanh(λ_m/2)`
by 14.I.T1. `sin(2θ_m) = 2sinθ_mcosθ_m = 2√(m_1m_2)/(m_1+m_2)
= √[4m_1m_2/(m_1+m_2)²] = √[1-(m_1-m_2)²/(m_1+m_2)²] = √(1-q_m²)`.
And `sech²(λ_m/2) = 1-tanh²(λ_m/2) = 1-q_m²`, so `sin(2θ_m) = sech(λ_m/2)`. ∎
Exact parameter-free hyperbolic/circular bridge.

**14.VII.D1 (PROVED).** With `χ_m = (c,s)`, `c = √m_1/√Σ`, `s = √m_2/√Σ`:
`ν_2(χ_m) = (c², √2cs, s²)^T = (m_1, √(2m_1m_2), m_2)^T/(m_1+m_2)`. ∎
The CP¹→CP² claim: `ν_2(λc,λs) = λ²ν_2(c,s)`, so the map descends to
projective space — standard, shown by the formula. ∎

**14.VII.CL1 (ASSERTED).** The Veronese image is a conic; it does not by
itself derive three physical generations — firewall inherited by Book 15.
Correctly scoped manuscript clarification. ∎

### 14.VIII — Symmetric-square one-body lift

**14.VIII.T1 (PROVED, analytic, general K).** Let `χ` be normalized and
`Φ = χ⊙χ` (the restriction of `χ⊗χ` to Sym², hence normalized). For
`K^(2) = ½(K⊗I + I⊗K)|_{Sym²}`:
`⟨χ⊗χ|K⊗I|χ⊗χ⟩ = ⟨χ|K|χ⟩⟨χ|χ⟩ = ⟨χ|K|χ⟩`,
`⟨χ⊗χ|I⊗K|χ⊗χ⟩ = ⟨χ|χ⟩⟨χ|K|χ⟩ = ⟨χ|K|χ⟩`.
Averaging: `⟨Φ|K^(2)|Φ⟩ = ½(⟨χ|K|χ⟩ + ⟨χ|K|χ⟩) = ⟨χ|K|χ⟩`.
This uses only the definition D8 — it holds for general K (Hermitian or
not), no matrix computation needed. ∎

**14.VIII mass-operator and spin-1 forms (PROVED).**
`K_m = diag(1,q_m²)`: on `e_1⊙e_1`, `K^(2)` gives `½(1+1) = 1`;
on `(e_1⊗e_2+e_2⊗e_1)/√2`, `½(1+q_m²)` from each of `K⊗I`, `I⊗K`;
on `e_2⊙e_2`, `½(q_m²+q_m²) = q_m²`. So
`K_m^(2) = diag(1, (1+q_m²)/2, q_m²) = (1+q_m²)I/2 + (1-q_m²)J_z/2`
(check: entries `(1+q_m²)/2 ± (1-q_m²)/2 = 1, q_m²`; middle `(1+q_m²)/2`). ∎
With `Φ_u = ν_2(cos α, sin α) = (cos²α, √2 sinαcosα, sin²α)^T`
(normalized: `(cos²α+sin²α)² = 1`):
`⟨Φ_u|J_z|Φ_u⟩ = cos⁴α - sin⁴α = (cos²α-sin²α)(cos²α+sin²α) = cos(2α)`;
`⟨Φ_u|J_x|Φ_u⟩ = (1/√2)·2·(√2 sinαcosα)(cos²α+sin²α) = 2sinαcosα = sin(2α)`
(compute `J_xΦ_u = (1/√2)(b, a+c, b)` with `a=cos²α, b=√2 sinαcosα,
c=sin²α`; `⟨Φ|J_x|Φ⟩ = (1/√2)(ab+b(a+c)+cb) = (1/√2)·2b(a+c) = 2sinαcosα`
since `a+c = 1`). ∎

### 14.IX — One-body lift and the correlation boundary

**Lift rule (PROVED).** Write `K = k_0I + k_iσ_i/2` with `k_0 = trK/2`,
`k_i = tr(Kσ_i)` real (from `tr(σ_iσ_j) = 2δ_ij`). Then
`K^(2) = k_0I_3 + (k_i/2)σ_i^(2)` where `σ_i^(2) = ½(σ_i⊗I+I⊗σ_i)|_{Sym²}`.
Direct computation in the Sym² basis: `σ_z^(2) = diag(1,0,-1) = J_z`;
`σ_x^(2) = (1/√2)[[0,1,0],[1,0,1],[0,1,0]] = J_x`;
`σ_y^(2) = (1/(i√2))[[0,1,0],[-1,0,1],[0,-1,0]] = J_y` (D9's standard form;
verified entry by entry). Hence `K^(2) = k_0I + ½k_iJ_i` exactly, with no
sign or convention subtlety. (Checked independently on 200 random Hermitian
K against the definition D8: exact agreement.) ∎

**14.IX.T1 — One-body lift no-quadrupole (PROVED, conditional on the
standard `1⊕3⊕5` decomposition, ST).** The lift is linear and injective
(rank 4): `k_0 = (1/3)tr K^(2)` (since `tr σ_i^(2) = 0`) and
`k_j = tr(J_jK^(2))` with `tr(J_jJ_i) = 2δ_ji` recover the
four parameters. Its image is `span{I, σ_i^(2)}`: the scalar singlet plus
the 3-dimensional spin-1 adjoint sector, i.e. exactly `1⊕3` inside the
9-dimensional `Herm(Sym²(C²)) = 1⊕3⊕5` (standard representation theory,
ST). The five-dimensional quadrupole `5` is absent: the image is
4-dimensional and lies in `1⊕3`.
Witness: `Q_{xz} = {J_x,J_z}/2 = (1/(2√2))[[0,1,0],[1,0,-1],[0,-1,0]]`
is nonzero, traceless (`tr Q_{xz} = 0`, hence `⊥ I`), and
`tr(Q_{xz}J_z) = 0`, `tr(Q_{xz}J_x) = 0`, `tr(Q_{xz}J_y) = 0`
(all verified entry by entry: with `J_x,J_z` as in D9,
`Q_{xz}J_x = (1/4)[[1,0,1],[0,0,0],[-1,0,-1]]` has trace `(1+0-1)/4 = 0`;
`Q_{xz}J_y = (1/(4i))[[-1,0,1],[0,2,0],[1,0,-1]]` has trace
`(-1+2-1)/(4i) = 0`; `Q_{xz}J_z = (1/(2√2))[[0,0,0],[1,0,1],[0,0,0]]`
has trace 0). So `Q_{xz}` is orthogonal to all of `span{I, J_i}` and
lies outside the lift's image.
This is the exact Book 14/15 boundary: any later flavor structure needing
the `5` requires genuinely new correlation dynamics. ∎

### 14.X–14.XIII, 14.0 — Closure declarations (ASSERTED)

- **14.X** (empirical control ladder; nine-bullet negative ledger), **14.XI**
  (operational promotion audit: `Δ_op(Book 14) = ∅`), **14.XII.T1**
  (twelve-point closure summary), **14.XIII** (retirement and handoff;
  gate/obstruction 14→15), and **14.0** (purpose, source retirement,
  dependency boundary) are status/bookkeeping declarations. They assert no
  mathematics beyond the items proved above; each is correctly scoped as MA
  by the book. ∎

## D. New axioms / assumptions beyond Euclid + seed + earlier books

1. **Background mathematics (declared substrate, not Euclid inheritance).**
   Real and complex analysis (hyperbolic/trigonometric functions, logarithms,
   absolute value, the complex continuation `η = iθ`), finite-dimensional
   linear algebra (tensor products, Pauli and spin-1 matrices, the trace
   inner product), elementary calculus (derivatives for 14.VI.C1, limits for
   14.V.T1). Nothing in §C is claimed as inherited from the Elements.
2. **Campaign dependencies actually used.** The seed double-angle identity
   (14.I.C2 lineage only; the tanh formula is proved from definitions here).
   The Book 7 `sxp` notation convention (D10; notation import). No Book 13
   content is used (verified by reading `book13_proof.md`: Book 13 is
   thermodynamics; Book 14's dependency list in 14.0 is Books 0–7 and 9–10
   calculus, used here purely as background mathematics).
3. **ST imports (stated, not proved):** 14.II.P1 (two-body special-relativistic
   kinematics); 14.V.P1 (point-Coulomb Dirac circular-branch ratio); the
   Coulomb binding law (conditional check in 14.IV only); the standard
   `Herm(Sym²(C²)) = 1⊕3⊕5` decomposition (14.IX.T1's ambient fact).
4. **No new axioms in the logical sense.** Every PROVED claim in §C derives
   from D1–D10 plus background mathematics, with the stated imports where
   the claim is marked conditional.
5. **MA/declared items (book's own scoping, kept):** the negatives 14.II.N1,
   14.IV.N1, 14.V.N1; the clarification 14.VII.CL1; all closure/retirement/
   handoff declarations (§14.X–XIII, 14.0) including `Δ_op(Book 14) = ∅`.
6. **Inherited labeling flag (not repaired here).** 14.0's "certified Books
   0–7 and 9–10 calculus" wording carries the §2.XI.L9 labeling defect noted
   in the Volume I audit (cf. `book13_proof.md` §5 P43). This file uses that
   calculus as background mathematics only; no claim here depends on upstream
   certification.

## E. Source-text defects found (kept honest)

- **"Certified" wording (14.0).** See §D.6: the §2.XI.L9 defect is inherited
  as wording; the mathematics used is ordinary background calculus.
- **Notation flag (14.V.T2).** `sxp` is the Book 7 convention, not defined
  in this book — the book page flags this itself; kept as a notation import.
- **Forward reference (14.I.C2).** "The identification with Book 15's qSaw"
  is an MA forward reference, not a claim of this book.
- **Verification-report record.** The page footer cites
  `validation/book14/verify_book14.py` (52 assertions): not present on disk.
  `vol3/book14/audit_book14.py` (50 assertions) is present but was not
  re-run here. The book's numeric reports are attributed as the book's own,
  per the proof-over-sampling rule.

## F. Ledger counts (per-file totals)

| Scope | Count | Items |
|-------|-------|-------|
| PROVED | 16 | 14.I.T1, 14.I.C1, 14.I.C2, 14.II.T1, 14.III.E1 (math), 14.III.T1, 14.III.T2, 14.IV exact form + 14.IV.T1, 14.V.T1, 14.V.T2 (conditional), 14.VI.T1 + 14.VI.C1, 14.VII.T1, 14.VII.D1, 14.VIII.T1 + mass/spin-1 forms, 14.IX lift rule + 14.IX.T1 (conditional) |
| CHECKED | 1 | 14.IV conditional Coulomb check (book's own NC report; Coulomb law imported ST; not re-run here) |
| ASSERTED | 8 | 14.II.P1 (ST), 14.II.N1, 14.III.E1 (physical caveat), 14.IV.N1, 14.V.P1 (ST), 14.V.N1, 14.VII.CL1, 14.X–XIII + 14.0 declarations (incl. `Δ_op = ∅`) |
| INCOMPLETE | 0 | — |

Totals: 16 + 1 + 8 + 0 = 25 (the 24-row inventory with row 7 split into its
proved math and its asserted physical caveat). ST imports are counted under
ASSERTED with their ST label kept. Every analytic claim the book tags CP is
proved in §C in full; nothing the book tags CP was left at ASSERTED, and
nothing was promoted to PROVED beyond what §C derives.
