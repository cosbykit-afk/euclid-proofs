# Book 9 — Euclid-style extension proofs (R Theory, rewrite book 9)

**Rewrite book:** `~/workspace/r-theory-rewrite/book9/index.html` — *Book 9 — Relativity
and Gravitation: Conditional Reconstruction* (Volume II, Book 9; source lines 2094–2264
of the volume text; read in full).
**Worker:** Euclid book-proofs campaign, item "book 9" · **Date:** 2026-09-22 (PDT).
**Scope discipline (Kit's, non-negotiable):** PROVED = exact mathematics shown here, in
dependency order, definitions first, nothing used before it is proved. CHECKED = a completed
computation (run named and dated). ASSERTED = declared contract, standard import, or
manuscript claim — never presented as established. INCOMPLETE = failed, timed out, unfinished.
"PROVED (conditional)" means the proof is exact *given the stated declared contracts* — the
book's whole program is conditional reconstruction, and every conditionality is named.

**Method note.** The book's own audit verified most identities numerically (nc) or symbolically
(sc) and kept them at those statuses. Where an analytic proof is complete it is given here,
and per Kit's 2026-09-21 rule no numerical sampling is run on top of it. The two symbolic
computations the book rests on for §9.5 were re-run here (V9-11, V9-12) and pass exactly.

## 0. Citation availability and the No-Euclid-wholesale boundary

- The campaign seed (`~/workspace/euclid_work/books/seed_double_angle.md`, Kit's double-angle
  secant/cosecant identity, PROVED) is on disk. It is **not invoked** by any proof below: the
  identities here use `csc²−cot² = 1`, `sec²−tan² = 1`, and elementary algebra directly.
  Dependency honesty requires saying so rather than manufacturing a citation.
- Sibling files `book0_proof.md`, `book2_proof.md`, `book4_proof.md` were **not present** when
  this worker ran (sibling workers presumably in flight); `book1/3/5/6/7/8` exist. Volume I
  premises are therefore proved directly where needed (the reciprocal-product identities in
  §9.1a), and everything else enters through explicitly declared contracts/imports below —
  never as assumed proved facts.
- **Euclid contact:** no proposition of Euclid's *Elements* (Books 1–13, as inventoried in
  `~/workspace/euclid_work/ledger/`) is used deductively anywhere below. The contact with
  Euclid is stylistic (definitions first, dependency order) and methodological. The Euclid
  Book 9 ledger (`~/workspace/euclid_work/ledger/book9_ledger.md`) establishes that R Theory
  makes no extension claim on any of the Elements' 36 number-theoretic propositions — that
  null mapping is a scope finding, not a premise used here. This respects the
  No-Euclid-wholesale theorem (4.X.H, Book 4 §4.X): R Theory extends a
  synthetic-constructive stratum on its declared substrate; wholesale inheritance of the
  Elements is not claimed.

## 1. Definitions and declared contracts (definitions first)

- **D0 — standard substrate (ST, ASSERTED standard import):** the complete ordered field ℝ,
  real analysis, trigonometry, finite-dimensional linear algebra, and differential forms
  (exterior derivative nilpotency `d² = 0`, wedge antisymmetry `α∧α = 0`). Used, never
  derived here.
- **D-PRIM — canonical primitives (declaration):**
  `s_xp = |csc x| − cot x`, `s_rx = |csc x| + cot x`,
  `c_xp = |sec x| + tan x`, `c_rx = |sec x| − tan x`
  (global conventions, Volume II front matter), wherever sin/cos are nonzero.
- **D-RP — relativistic projection contract (ASSERTED declared contract):** on the declared
  positive-energy timelike chart,
  `sin χ = β = p_phys·c / E`, `cos χ = m·c² / E`, with `β ∈ [0, 1)`,
  hence `sin χ, cos χ ≥ 0` on the chart; the mass shell `E² − p²c² = m²c⁴` is part of the
  contract, not derived. (The book, lines 12–15, does not state the `β ≥ 0` branch
  restriction explicitly; it is made explicit here because the identities below drop the
  absolute values in D-PRIM. This is the book's stated "projection contract," honestly
  labeled as such in the book itself, lines 35–37.)
- **D-HR — hyperbola readouts (ASSERTED declared contract):** `q = s_xp > 0`,
  `u = q^{−1/2}`, `v = q^{1/2}`, `E_r = u+v`, `O_r = u−v`; lapse readout `N = O_r / E_r`;
  areal-radius readout `r = a·E_r²` with parameter `a > 0`. The identification of `r` as
  physical areal radius and `N` as gravitational lapse is a projection contract (book
  line 78), declared here as such.
- **D-CAL — external calibration (ASSERTED):** `a = GM / (2c²)`. External; not derived.
- **D-CH — chart declarations:** `q = (1−N)/(1+N)`, `σ = ln(AN)` (vacuum locus `σ = 0`).
- **D-GR — general-relativity imports (ASSERTED standard imports):**
  (i) the static reciprocal spherical metric `ds² = −f·c²dt² + f^{−1}dr² + r²dΩ²`;
  (ii) its vacuum Einstein reduction `r·f′ + f − 1 = 0`;
  (iii) the independent-N,A metric `ds² = −N(r)²c²dt² + A(r)²dr² + r²dΩ²` and its vacuum
  field equations; (iv) the minimal first-order Palatini action and the facts that
  metric-compatibility does not imply zero torsion, and that independent connection
  variation gives `T^a = 0` when the coframe is nondegenerate and matter carries no
  intrinsic spin current. All imported, none derived here.
- **D-BRANCH — coordinate branches (declaration):** `r > 0`, `θ ∈ (0,π)` for the
  §9.5 density resolution; `N ≠ −1` for the chart inversion; `q > 0` for `u,v`.

## 2. Claim inventory and proofs in dependency order

### §9.1 — Local Lorentz witness

**B9.1a — Reciprocal-product identities.** `s_rx·s_xp = c_xp·c_rx = 1`. **PROVED.**
`s_rx·s_xp = |csc x|² − cot²x = csc²x − cot²x = 1` and
`c_xp·c_rx = |sec x|² − tan²x = sec²x − tan²x = 1` by D0 trigonometry. (The book notes
these as earned in the Volume I Book 2 algebraic spine; they are proved directly here.)

**B9.1b — Lorentz-weight identities.** On D-RP:
`s_xp(χ) = pc/(E+mc²)`, `s_rx(χ) = (E+mc²)/(pc)`,
`c_xp(χ) = (E+pc)/(mc²)`, `c_rx(χ) = (E−pc)/(mc²)`. **PROVED (conditional on D-RP).**
With `sin χ, cos χ ≥ 0`: `|csc χ| = E/(pc)`, `cot χ = mc²/(pc)`,
`|sec χ| = E/(mc²)`, `tan χ = pc/(mc²)`. Hence
`s_xp = (E−mc²)/(pc)` and
`(E−mc²)/(pc) = (E²−m²c⁴)/(pc(E+mc²)) = p²c²/(pc(E+mc²)) = pc/(E+mc²)`
using the mass shell from D-RP. The other three are direct substitution.
(The book kept these as numerical checks, max error 5.7e−14; the analytic proof here
stands alone, per Kit's rule — no sampling on top of it.)

**B9.1c — Boost weights.** With `β = tanh η`: `c_xp = e^η`, `c_rx = e^{−η}`.
**PROVED (conditional on D-RP).** `e^η = cosh η + sinh η = (1+β)/√(1−β²)`.
From D-RP, `E = mc²γ`, `pc = βmc²γ` with `γ = 1/√(1−β²)`, so
`(E+pc)/(mc²) = (1+β)/√(1−β²) = e^η` and `(E−pc)/(mc²) = (1−β)/√(1−β²) = e^{−η}`.

**B9.1d — Mass-shell factorization.** `c_xp·c_rx = 1` reproduces the mass shell.
**PROVED (conditional on D-RP).** From B9.1b,
`c_xp·c_rx = (E²−p²c²)/m²c⁴`, which equals 1 exactly by the D-RP mass shell
(and equals 1 independently by B9.1a — consistency check).

**Dependency flag (not a premise).** The book's provenance sentence (lines 5–8) cites
"T4, T6, Towards Unification, Reverse Engineering Einstein" and a "Lorentz witness,"
none of which are Books 0–6 or earned in the Volume I ledger; under the volume's own
dependency rule these are not valid upstream dependencies. The identities above are
self-contained, so this is a dependency-labeling defect, not a mathematical error.
**Minor gap (book §9.1):** the `β ≥ 0` branch restriction needed to drop the absolute
values is unstated in the book (lines 12–15); made explicit in D-RP here.

### §9.2 — Rank and curvature firewall

**B9.2a — Coframe-rank obstruction.** If every coframe one-form is
`e^a = f^a(x)·dx` for a single variable `x`, then the coframe spans at most one
dimension at each point: rank ≤ 1. **PROVED.** Every `e^a` is a scalar multiple of
`dx`, so `span{e^a} ⊆ span{dx}`, a one-dimensional space (D0 linear algebra).

**B9.2b — Fixed-generator pure gauge.** For `ω = K·dη` with `K` a fixed algebra
element, `R = dω + ω∧ω = 0` on smooth regions. **PROVED.** `dω = dK∧dη + K·d²η`;
`K` fixed ⇒ `dK = 0`; `d²η = 0` (D0); `ω∧ω = K²·dη∧dη = 0` (D0 wedge antisymmetry).
Hence "scalar rapidity variation by itself is pure gauge."

**B9.2c — Nonzero curvature requires additional structure.** **PROVED** as the logical
contrapositive of B9.2a/B9.2b: nonzero curvature forces either additional independent
connection directions, singular/global structure, or an imported geometric field law.

### §9.3 — Reciprocal half-weight theorem

**B9.3a — Half-weight hyperbola.** With D-HR, `uv = 1` and
`E_r² − O_r² = 4uv = 4`. **PROVED.** `(u+v)² − (u−v)² = 4uv`; `uv = q^{−1/2}·q^{1/2} = 1`.

**B9.3b — Defect identities.** `N = (1−q)/(1+q)`, `r(1−N²) = 4a`, `N² = 1 − 4a/r`.
**PROVED (conditional on D-HR).** `N = O_r/E_r = (u−v)/(u+v) = (1−v/u)/(1+v/u) = (1−q)/(1+q)`
since `v/u = q`. Then `1−N² = 4q/(1+q)²`, and
`r = a(u+v)² = a·u²(1+v/u)² = a(1+q)²/q`, so `r(1−N²) = a·(1+q)²/q·4q/(1+q)² = 4a`,
i.e. `N² = 1 − 4a/r` for `r > 0`.

**B9.3c — Reciprocal-defect identity on the first exterior chart.**
`(1−q)/(1+q) = c_rx` where `q = s_xp(χ)`. **PROVED (conditional on D-RP branch +
D-HR).** On the chart, `q = |csc χ| − cot χ = (1−cos χ)/sin χ`, so
`(1−q)/(1+q) = (sin χ + cos χ − 1)/(sin χ − cos χ + 1)` and
`c_rx = (1−sin χ)/cos χ`. Cross-multiplication is exact:
`(sin χ + cos χ − 1)·cos χ = sin χcos χ + cos²χ − cos χ`, and
`(1−sin χ)(sin χ − cos χ + 1) = (1−sin²χ) − cos χ(1−sin χ) = cos²χ − cos χ + sin χcos χ`. ∎

### §9.4 — Vacuum Einstein first-integral theorem

**B9.4a — Metric.** The static reciprocal spherical metric is **imported** (book line 90).
**ASSERTED** (D-GR(i) standard import).

**B9.4b — Vacuum reduction.** `r·f′ + f − 1 = 0` for this metric.
**ASSERTED** (D-GR(ii) standard imported theorem: temporal/radial Einstein equations).

**B9.4c — First-integral equivalence.** `d[r(1−f)]/dr = 0 ⟺ r·f′ + f − 1 = 0`.
**PROVED.** `d[r(1−f)]/dr = (1−f) − r·f′`, which vanishes exactly when `r·f′ + f = 1`.

**B9.4d — Schwarzschild form.** With the external calibration D-CAL (`a = GM/(2c²)`),
`f = N² = 1 − 4a/r = 1 − 2GM/(rc²)`. **PROVED (conditional on D-CAL):**
`4a/r = 4GM/(2c²r) = 2GM/(c²r)`. The calibration itself is ASSERTED (external, not
derived). The book's status sentence (lines 104–105: "a conditional theorem inside
imported general relativity, not a derivation of Einstein's equations") is accurate;
no scope violation.

### §9.5 — Reciprocity is selected on shell, not before variation

**B9.5a — On-shell selection of AN = 1.** For the independent-N,A metric, vacuum
Einstein equations imply `(NA)′ = 0`, hence `NA = const`, and `= 1` after asymptotic
normalization. **CHECKED + ASSERTED import.** The engine identity
`G^r_r − G^t_t = 2(NA)′/(r·N·A³)` (mixed components) was re-derived here by a completed
SymPy run (2026-09-22 PDT; SymPy 1.12; units `c = 1`; script
`work/book9_sympy_95.py`, log `work/sympy_95.log`; residual exactly 0; Schwarzschild-vacuum
tripwire `[0,0,0,0]` passed). The vacuum field equations `G^t_t = G^r_r = 0` are the
D-GR(iii) import (ASSERTED); the deduction `(NA)′ = 0` then follows from the checked
identity; asymptotic normalization `NA → 1` is declared. The covariant form
`G_rr/A² + G_tt/N² = 2(NA)′/(rNA³)` is the same identity (equivalent at `c = 1`; the
book's 2026-09-19 correction of the mixed-component quotation is respected — the
identity is stated with mixed components correctly). The AN = 1 conclusion is also a
standard imported GR result (D-GR).

**B9.5b — Boundary-term collapse.** Imposing `A = N^{−1}` *before* variation makes the
bulk density `√(−g)·R` a total derivative: `√(−g)R = sinθ·dB/dr` with
`B = −r²f′ − 2r(f−1)`, `f = N²`. **CHECKED.** Completed SymPy run 2026-09-22 PDT
(same script; residual exactly 0; physical branch `θ ∈ (0,π)` declared to resolve
`√(r⁴sin²θ) = r²sinθ`; factored forms of both sides agree). The methodological
consequence — pre-variation imposition discards an independent field equation — is the
D-GR standard variational-principle import (ASSERTED). The book's rule (lines 122–124:
reciprocity must be selected on shell, not imposed before variation) is sound.

### §9.6 — Sourced transfer and the one-scalar matter obstruction

**B9.6a — Chart inversion.** `q = (1−N)/(1+N)` inverts `N = (1−q)/(1+q)` exactly.
**PROVED** (D-CH): substitution gives `(2q/2) = q`, valid for `N ≠ −1`.

**B9.6b — Radial-strain variable.** `σ = ln(AN)`; `σ = 0 ⟺ AN = 1`; `σ′ = 0` in
vacuum. **PROVED (conditional on B9.5a).** Follows from D-CH and B9.5a.

**B9.6c — Newtonian Poisson recovery.** "The sourced transfer variable q reproduces the
correctly normalized Newtonian Poisson equation in the weak-field, nonrelativistic limit
after the exterior mass calibration is fixed" (book lines 130–132).
**ASSERTED — manuscript assertion, not independently verified.** No derivation is shown
in this book and it was not computed here. Must not be treated as earned upstream.

**B9.6d — Static-dust obstruction.** "The static-dust test collapses to the vacuum
branch" and "a second coframe variable is therefore necessary for general matter" (book
lines 134–136). **ASSERTED — manuscript assertion, not independently verified.** No
computation is shown in this book and it was not checked here.

### §9.7 — Torsion and spin boundary

**B9.7a — Compatibility does not kill torsion.** "Metric-compatible Lorentz transport
does not itself imply zero torsion." **ASSERTED** (D-GR(iv) standard import:
metric compatibility constrains the symmetric part of the connection; torsion is the
antisymmetric part).

**B9.7b — Palatini torsion statement.** "Under the imported minimal first-order Palatini
action, independent connection variation gives `T^a = 0` only when the coframe is
nondegenerate and matter carries no intrinsic spin current."
**ASSERTED** (D-GR(iv), explicitly labeled imported by the book, lines 146–148).
**Dependency flag:** the book's "T6 Einstein–Cartan witness" (lines 148–149) cites T6,
which is not a Books 0–6 result and does not appear as earned in the Volume I ledger —
not a valid upstream dependency, and not used as a premise above.

### §9.8 — Book 9 closure ledger

**B9.8 — Closure consistency.** The book's certified-list / conditional-list / not-derived
list (lines 152–165) is **consistent with the audit above**: the nine-item "not derived"
list (physical time; Lorentzian signature as fact about nature; Einstein/Palatini dynamics;
Newton's constant; a unique areal-radius contract; nonspherical gravity; gravitational
waves; fermionic matter; any invariant observable differing from accepted relativity) is
honored — nothing here derives any of them — and the conclusion (lines 166–168:
representation and conditional reconstruction, not replacement of GR; operational
prediction-difference set empty) accurately summarizes what the proofs above establish.
**ASSERTED** (audit bookkeeping). The Poisson-recovery and static-dust claims remain
ASSERTED per B9.6c/B9.6d and should not be inherited as earned.

## 3. New axioms / assumptions beyond Euclid + seed + earlier books

**None as axioms.** In the book's own zero-counts discipline, new axioms: 0 — projection
contracts and calibrations are declared, not smuggled as axioms. The declared conditional
content is exactly:

1. **D-RP** — relativistic projection contract (`sin χ = β`, `cos χ = mc²/E`, mass shell);
   the book's honestly-labeled conditional correspondence, not a derivation of relativity.
2. **D-HR** — hyperbola readouts (`N = O_r/E_r`, `r = a·E_r²`) and the lapse/areal-radius
   identification as projection contract.
3. **D-CAL** — external calibration `a = GM/(2c²)`; Newton's constant enters only here.
4. **D-GR** — the declared general-relativity physics imports (static metric, vacuum
   Einstein equations, Palatini action, variational principle); explicitly imported, not
   derived.
5. **D0/D-PRIM/D-CH/D-BRANCH** — the stipulated mathematical substrate, primitive
   definitions, chart definitions, and branch choices.

No Elements proposition is inherited (No-Euclid-wholesale boundary, §0). The campaign
seed (Kit's double-angle identity) is established but not invoked by this book.
`book0/2/4_proof.md` were absent at run time; no claim above depends on them.

## 4. Status tally

- **PROVED:** 14 — B9.1a, B9.1b, B9.1c, B9.1d, B9.2a, B9.2b, B9.2c, B9.3a, B9.3b, B9.3c,
  B9.4c, B9.4d, B9.6a, B9.6b (several conditional on the declared contracts D-RP/D-HR/D-CAL).
- **CHECKED:** 2 — B9.5a (`G^r_r − G^t_t = 2(NA)′/(rNA³)`, SymPy, residual exactly 0),
  B9.5b (`√(−g)R = sinθ·dB/dr` under `A = N^{−1}`, SymPy, residual exactly 0);
  both runs 2026-09-22 PDT, script `work/book9_sympy_95.py`, log `work/sympy_95.log`,
  Schwarzschild-vacuum tripwire passed.
- **ASSERTED:** 8 — B9.4a (metric import), B9.4b (vacuum reduction `rf′+f−1=0`),
  B9.4d-calibration (D-CAL `a = GM/(2c²)`), B9.6c (Poisson recovery),
  B9.6d (static-dust obstruction), B9.7a (compatibility ⇏ zero torsion),
  B9.7b (Palatini torsion statement), B9.8 (closure bookkeeping).
- **INCOMPLETE:** 0.

## 5. Notes for the campaign

- The book's §9.1 identities were kept as numerical checks in the book's own audit; the
  analytic proofs given here (B9.1b–B9.1d) supersede those as proof, per the
  proof-over-sampling rule — no numerical run was made on top of them.
- The book's §9.5 symbolic checks were independently re-derived here (not taken on trust);
  an earlier script draft had a Christoffel sign error (wrong contraction
  `∂_l g_ij + ∂_j g_il − ∂_i g_lj`), caught by the Schwarzschild-vacuum tripwire and
  corrected before the passing run. Disclosed per the standing rule.
- Two dependency-labeling defects in the book (T4/T6/Towards-Unification/
  Reverse-Engineering-Einstein provenance; T6 Einstein–Cartan witness) are flagged, not
  errors: the mathematics cited is self-contained or imported explicitly.
- One minor gap: the book's §9.1 chart leaves the `β ≥ 0` (equivalently
  `sin χ, cos χ ≥ 0`) branch restriction unstated; the identities hold on that branch.
- The Euclid Book 9 ledger's null mapping (no R Theory extension of the Elements'
  number-theoretic Book 9) is a scope finding, consistent with this file: rewrite Book 9
  is a conditional reconstruction on the modern substrate, not a continuation of Euclid's
  arithmetic program. The "extension of Euclid" here is methodological — definitions
  first, dependency order, nothing used before it is proved.
