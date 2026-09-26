# Cumulative Trigonometric Proof — R Theory as an Extension of Euclid

**Campaign:** claim-by-claim evaluation, Books 0–22, building one trigonometric
proof from the seed principle and the evaluated books.
**Status:** deterministic rebuild 2026-09-22 (second pass; the first parallel
pass raced and was discarded); extended 2026-09-26 with Books 21–22.
**Scope:** Books 0–22. The Books 21–22 stop was lifted by Kit's directive on
2026-09-26.

## Standing rules

Every claim is scoped with exactly one label:

- **PROVED** — complete analytic mathematics, verified step by step.
- **CHECKED** — a completed computation (numerical or symbolic); no analytic proof.
- **ASSERTED** — manuscript claim, assumption, import, convention, or status
  declaration; not proved or computed.
- **INCOMPLETE** — unfinished, failed, timed-out, or missing.

Nothing is presented as established unless the mathematics proves it or a
completed computation measured it. A complete analytic proof is not followed
by numerical sampling (proof over sampling). If a computation fails or times
out, it is reported INCOMPLETE plainly.

**Background substrate (M0).** Ordinary real analysis, trigonometry, and
calculus (derivatives of sin/cos/tan/cot, the Pythagorean identity,
half-angle and double-angle formulas, the exponential/logarithm laws) are
background mathematics, not principles. A "principle" is a proved
identity/lemma about trigonometric functions, angles, or circular/hyperbolic
measure that is not immediate background and not a duplicate of an earlier
principle.

**Euclid boundary.** A proposition of Euclid's *Elements* is cited as a
logical premise only when it is genuinely used and was verified in the
ledgers at `~/workspace/euclid_work/ledger/book1_ledger.md` through
`book13_ledger.md`. Most trigonometric principles cite no Euclid proposition;
the honest boundary is stated per principle. The campaign's established
finding stands: R Theory is not proved to be a deductive extension of all of
Euclid's *Elements*; it extends a synthetic-constructive stratum on an
explicitly admitted substrate (see the No-Euclid-wholesale record).

**Dependency discipline.** Principles are numbered P0, P1, P2, … sequentially
in book order (Seed, then Books 0–20). Each principle cites only earlier
principles, definitions, M0, or explicitly named asserted imports
(PROVED-conditional). Nothing is used before it is established. Duplicate
identities are folded once, at their first book-order occurrence; later
books note the earlier registration instead of re-folding.

---

## Principle 0 (PROVED) — Kit's double-angle secant-cosecant identity (seed)

**Source:** `~/workspace/kit_theorems/secant-cosecant-identity/PROOF.md`,
`~/workspace/euclid_work/books/seed_double_angle.md`.

**Statement.** For sin x ≠ 0 and cos x ≠ 0:

    4/sin(2x) = (tan x + |sec x| − 1/(cot x + |csc x|))
              + (cot x + |csc x| − 1/(tan x + |sec x|)).

**Proof.** Set A = tan x + |sec x| and B = cot x + |csc x|.
Lemma 1: A − 1/A = 2 tan x. Indeed A − 1/A = (A² − 1)/A; with
A = tan x + |sec x|, A² = tan²x + 2|tan x sec x| + sec²x, and
|tan x sec x| = |tan x|·|sec x|; a direct computation using
sec²x − 1 = tan²x gives (A²−1)/A = 2 tan x.
Lemma 2: B − 1/B = 2 cot x, by the symmetric computation with
csc²x − 1 = cot²x.
Regrouping: (A − 1/B) + (B − 1/A) = (A − 1/A) + (B − 1/B)
= 2 tan x + 2 cot x = 2(sin x/cos x + cos x/sin x)
= 2/(sin x cos x) = 4/sin(2x). ∎

**Domain note.** sin(2x) = 2 sin x cos x, so sin(2x) ≠ 0 ⟺
sin x ≠ 0 ∧ cos x ≠ 0; no separate condition is needed. The absolute
values are absorbed by |sec x|² = sec²x; no quadrant case split is needed.

**Scope:** PROVED (analytic, complete). **Depends on:** definitions only.
No Euclid proposition is a premise.

---

## Book 0 — Source Boundary and the Orientation Question (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book0_proof.md` (claim inventory:
43 PROVED, 0 CHECKED, 10 ASSERTED groups, 0 INCOMPLETE); rewrite page
`~/workspace/r-theory-rewrite/book0/index.html`.

**Boundary:** No proposition of Euclid's *Elements* is a premise of any proof
below (the book's own honest boundary, kept). Every principle is proved from
P0, earlier principles of this chapter, or M0, in strict dependency order.

**Evaluated claims summary:** 53 evaluated — **43 PROVED**, **0 CHECKED**,
**10 ASSERTED**, **0 INCOMPLETE**. Of the 43 proved, 16 yield genuine
trigonometric principles (folded as P1–P16); Book 0's Claim 3.1 is P0 itself
in the book's notation (no new principle); 26 proved claims are established
non-trig mathematics (recorded in `book0_claims.md`, not forced in); 10
ASSERTED groups cannot found principles.

**Definitions (cumulative):** On D = ℝ ∖ {kπ/2 : k ∈ ℤ}: srx = |csc x| +
cot x, sxp = |csc x| − cot x, cxp = |sec x| + tan x, crx = |sec x| − tan x;
urx = srx − crx, uxp = cxp − sxp; saw_r = 1/urx, saw_x = 1/uxp.

### P1 — Folded Pythagorean identities (from Book 0, Claim 1.2)

**Statement.** On D: srx·sxp = 1 and cxp·crx = 1.

**Proof.** srx·sxp = |csc x|² − cot²x = csc²x − cot²x = 1 (M0: the
Pythagorean identity csc² − cot² = 1); likewise
cxp·crx = sec²x − tan²x = 1. Hence sxp = 1/srx, crx = 1/cxp. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P2 — Positivity of the folded primitives (from Book 0, Claim 1.1)

**Statement.** On D, srx, sxp, cxp, crx are all strictly positive.

**Proof.** The seed's positivity argument (P0): with A = cxp =
tan x + |sec x| and B = srx = cot x + |csc x|,
A ≥ |sec x| − |tan x| = (1 − |sin x|)/|cos x| > 0 (since cos x ≠ 0
implies |sin x| < 1), and
B ≥ |csc x| − |cot x| = (1 − |cos x|)/|sin x| > 0. By P1,
sxp = 1/srx > 0 and crx = 1/cxp > 0. ∎

**Scope:** PROVED. **Depends on:** P0, P1.

### P3 — Symmetry laws of the folded primitives (from Book 0, Claims 1.4–1.6)

**Statement.** On D:
(a) srx(−x) = sxp(x), cxp(−x) = crx(x) (and vice versa);
(b) srx(x−π/2) = crx(x), cxp(x−π/2) = sxp(x);
(c) all four primitives are π-periodic.

**Proof.** (a) |csc(−x)| = |csc x|, cot(−x) = −cot x (M0 parity).
(b) csc(x−π/2) = −sec x, cot(x−π/2) = −tan x, so
srx(x−π/2) = |−sec x| − tan x = crx(x); similarly
cxp(x−π/2) = |−csc x| − cot x = sxp(x).
(c) |csc(x+π)| = |csc x|, cot(x+π) = cot x (likewise sec/tan), so the
quartet factors through ℝ/πℤ — it cannot recover phase modulo 2π. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P4 — Local generator rational recovery (from Book 0, Claim 2.1)

**Statement.** Fix an open quadrant, set z = srx, ε = sgn(z−1). Then
sxp = 1/z, cxp = (z+ε)/(εz−1), crx = (εz−1)/(z+ε).

**Proof.** By P1, sxp = 1/z. From P0's Lemma 2 with B = z:
z − 1/z = 2 cot x, so with t = tan x, t = 2z/(z²−1) (z = 1 is
impossible on D: it would give cot x = 0, i.e. cos x = 0, a seam).
cxp = 1/|cos x| + tan x = √(1+t²) + t (M0: 1/cos²x = 1 + tan²x,
1/|cos x| > 0). Substituting t:
cxp = (z²+1)/|z²−1| + 2z/(z²−1); since z > 0 (P2),
sgn(z²−1) = sgn(z−1) = ε, giving cxp = [ε(z²+1)+2z]/(z²−1).
Cross-multiplication verifies [ε(z²+1)+2z](εz−1) = (z+ε)(z²−1)
(both expand to z³ + εz² − z − ε), i.e. cxp = (z+ε)/(εz−1).
The denominator is nonzero on D (εz − 1 = 0 would need z = 1).
crx = 1/cxp by P1. ∎

**Scope:** PROVED. **Depends on:** P0, P1, P2.

### P5 — Riccati generator law (from Book 0, Claim 2.2)

**Statement.** On each open quadrant, z = srx satisfies
z′ = −(1+z²)/2, and the rational function field ℝ(z) is closed under
d/dx.

**Proof.** With fixed quadrant signs σ_s = sgn(sin x),
z = (σ_s + cos x)/sin x = (1 + σ_s cos x)/(σ_s sin x) (definitions).
Differentiating: z′ = −(1 + σ_s cos x)/sin²x. Meanwhile
(1+z²)/2 = (sin²x + (1+σ_s cos x)²)/(2sin²x)
= (2 + 2σ_s cos x)/(2sin²x) = (1 + σ_s cos x)/sin²x,
so z′ = −(1+z²)/2. For any r ∈ ℝ(z),
dr/dx = r_z(z)·z′ ∈ ℝ(z). ∎

**Scope:** PROVED. **Depends on:** M0, P2 (positivity for the stated form).

### P6 — FlatWave identity (from Book 0, Claim 4.1)

**Statement.** On D, with urx = srx − crx, uxp = cxp − sxp:
1/urx + 1/uxp = sgn(sin 2x).

**Proof.** Put p̃ = 1/|s| − 1/|c|, q̃ = s/c + c/s = 1/(sc).
Then urx = p̃ + q̃, uxp = −p̃ + q̃ (definitions), so
urx·uxp = q̃² − p̃² = 1/(s²c²) − (1/s² + 1/c² − 2/|sc|) = 2/|sc|
= 4/|sin 2x|. By P1, uxp = cxp − sxp = A − 1/B and
urx = srx − crx = B − 1/A; hence P0 gives urx + uxp = 4/sin(2x).
Therefore (1/urx + 1/uxp) = (urx+uxp)/(urx·uxp)
= (4/sin 2x)/(4/|sin 2x|) = sgn(sin 2x). ∎

**Scope:** PROVED. **Depends on:** P0, P1.

### P7 — FlatWave transformation laws (from Book 0, Claim 4.2)

**Statement.** With FW(x) = 1/urx + 1/uxp:
FW(x+π/2) = −FW(x), FW(x+π) = FW(x), FW(x+2π) = FW(x).

**Proof.** By P6, FW(x) = sgn(sin 2x). M0:
sgn(sin(2x+π)) = −sgn(sin 2x) (cophase reversal),
sgn(sin(2x+2π)) = sgn(sin 2x) (half-turn invariance), and hence
FW(x+2π) = FW(x) (deck-blindness). ∎

**Scope:** PROVED. **Depends on:** P6, M0.

### P8 — Common-sign law (from Book 0, Claim 4.3)

**Statement.** On D: urx·uxp = 4/|sin 2x| > 0 and
sgn(urx) = sgn(uxp) = sgn(sin 2x) =: ε_FW.

**Proof.** From P6's computation, urx·uxp = 4/|sin 2x| > 0, so urx
and uxp share a sign; from P0, urx + uxp = 4/sin(2x), so that common
sign is the sign of sin(2x). ∎

**Scope:** PROVED. **Depends on:** P0, P6.

### P9 — Harmonic carrier ellipse (from Book 0, Claim 5.1)

**Statement.** With H = 1/(urx+uxp) and V = H′:
H = sin(2x)/4, V = cos(2x)/2, and V² + 4H² = 1/4.

**Proof.** H = sin(2x)/4 by P0 (inverting the sum); differentiating
(M0), V = dH/dx = cos(2x)/2. Then
cos²(2x)/4 + 4·sin²(2x)/16 = (cos²(2x) + sin²(2x))/4 = 1/4. ∎

**Scope:** PROVED. **Depends on:** P0, M0.

### P10 — Transfer-circle identity (from Book 0, Claim 6.1)

**Statement.** Fix an open quadrant; with α = σ_s, β = σ_c,
p = α cos x − β sin x and q = α sin x + β cos x = |sin x| + |cos x|:
p² + q² = 2.

**Proof.** p² = cos²x + sin²x − 2αβ sin x cos x,
q² = sin²x + cos²x + 2αβ sin x cos x (using α² = β² = 1); the sum is
2(sin²x + cos²x) = 2 (M0). ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P11 — Differential transfer closure (from Book 0, Claim 6.2)

**Statement.** Quadrant-locally, with λ = (1−p)/2:
λ′ = q/2; λ″ + λ = 1/2; (1−2λ)² + 4(λ′)² = 2.

**Proof.** p′ = −α sin x − β cos x = −q, so
λ′ = −p′/2 = q/2. q′ = α cos x − β sin x = p, so
λ″ = q′/2 = p/2 and λ″ + λ = p/2 + (1−p)/2 = 1/2.
Finally (1−2λ)² + 4(λ′)² = p² + q² = 2 by P10. ∎

**Scope:** PROVED. **Depends on:** P10, M0.

### P12 — Sharp phase-rate bounds (from Book 0, Claim 6.3)

**Statement.** On each open quadrant: 1/2 < λ′ ≤ 1/√2; the upper bound
is attained exactly at the unique midpoint λ = 1/2, where
Ω = λ/(1−λ) = 1 and χ = (1−λ)/λ = 1.

**Proof.** λ′ = q/2 (P11) with q = |sin x| + |cos x|.
q² = 1 + 2|sin x cos x| = 1 + |sin 2x|; on D,
0 < |sin x cos x| ≤ 1/2 (M0: AM–GM on sin²x, cos²x), with equality
iff |sin x| = |cos x|, i.e. p = ±(|cos x| − |sin x|) = 0, i.e.
λ = 1/2. Hence 1 < q ≤ √2 and 1/2 < λ′ ≤ 1/√2. At λ = 1/2,
Ω = (1/2)/(1/2) = 1, χ = 1. ∎

**Scope:** PROVED. **Depends on:** P11, M0.

### P13 — Equal-and-opposite saw derivatives (from Book 0, Claim 6.4)

**Statement.** Quadrant-locally, saw_r′ + saw_x′ = 0, where
saw_r = 1/urx, saw_x = 1/uxp.

**Proof.** saw_r + saw_x = 1/urx + 1/uxp = sgn(sin 2x) (P6), which is
constant on each open quadrant (the sign of sin 2x cannot change without
crossing a seam); the derivative of a locally constant function is 0.
(Definitional consequence, not a conservation law.) ∎

**Scope:** PROVED. **Depends on:** P6.

### P14 — Cross-layer ratio (from Book 0, Claim 6.6)

**Statement.** On D:
Ω = λ/(1−λ) = saw_r/saw_x = uxp/urx = cxp/srx.

**Proof.** saw_r/saw_x = (1/urx)/(1/uxp) = uxp/urx. By P8, saw_r and
saw_x share the sign ε_FW, and |saw_r| + |saw_x| = |sgn(sin 2x)| = 1
(P6); with |saw_r| = λ, |saw_x| = 1−λ this gives
saw_r/saw_x = λ/(1−λ). Finally
uxp/urx = (A − 1/B)/(B − 1/A) = ((AB−1)/B)/((AB−1)/A) = A/B = cxp/srx
(using P1), valid since urx·uxp = 4/|sin 2x| ≠ 0 (P8) implies
urx ≠ 0 and AB ≠ 1 on D. ∎

**Scope:** PROVED. **Depends on:** P1, P6, P8.

### P15 — Reciprocal-even normalization (from Book 0, Claim 6.7)

**Statement.** On D:
E_D = 1/(srx+sxp+cxp+crx) = |sin 2x|/(4(|sin x| + |cos x|)), and the
normalized primitives n_i = prim_i/(srx+sxp+cxp+crx) satisfy n_i ≥ 0,
Σ n_i = 1.

**Proof.** By P1, srx + sxp = 2|csc x| and cxp + crx = 2|sec x|;
their sum is 2(|sin x| + |cos x|)/(|sin x||cos x|). The reciprocal is
|sin x||cos x|/(2(|sin x|+|cos x|)), and |sin x||cos x| = |sin 2x|/2
(M0). Nonnegativity follows from P2. ∎

**Scope:** PROVED. **Depends on:** P1, P2, M0.

### P16 — Log representation (from Book 0, Claim 6.8)

**Statement.** On D: cxp = e^{asinh(tan x)} and
srx = e^{asinh(cot x)} exactly.

**Proof.** M0: e^{asinh t} = t + √(1+t²). With t = tan x,
√(1+tan²x) = |sec x|, so e^{asinh(tan x)} = tan x + |sec x| = cxp;
with t = cot x, √(1+cot²x) = |csc x|, giving srx. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### Book 0 claims not folded, and why

- Claim 3.1 (urx + uxp = 4/sin(2x)): not folded — it is P0 itself in
  the book's notation, already registered.
- Claims 1.3, 5.2 (quadrant-local smoothness; smooth seam extension of
  H): verified PROVED, but regularity/analysis facts, not identities
  about trig functions; the formulas they concern are already P3/P9.
- Claim 5.3 (no continuous injective S¹ → ℝ): verified PROVED, but
  general topology, not trigonometry.
- Claims 7.1–7.4 (rank firewall), 8.1–8.3 (real linear lift, J² = −I,
  orientation-relative uniqueness, conjugacy classification), 9.1–9.6
  (tetrahedral Gram rank, O(G) orientation-reversing isometries,
  D₁D₀ = D₂D₁ = 0, central-sign nonselection, Clifford presentations,
  affine readout sign): verified PROVED, but linear algebra, group/set
  theory, simplicial homology, and matrix-algebra facts — not trig
  identities.
- Theorem 0.IV.T1 (automorphism obstruction) and its T2/T3
  applications: verified PROVED, but an automorphism/naturality
  argument, not a trig identity.
- The M5 conditional block (Axiom-0-conditional complex structure on W,
  dimensions 10/5): verified PROVED-conditional, but conditional on the
  asserted Axiom 0 and not a trig relation.
- Claim 6.5 (Ωχ = 1, χ = R_λ − 1, Ω = U_λ − 1): verified PROVED, but
  pure algebra from the definitions — no trig content.
- ASSERTED groups A1–A10: historical/editorial, inherited essay
  theorems, audit methodology and dispositions, audit completeness,
  corollary caveats, boundary declaration — assertions cannot found
  trigonometric principles.

Claim-by-claim table with verdicts: `book0_claims.md` (status: complete).
Highest principle: **P16**.

---

## Book 1 — The Folded Factors (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book1_proof.md` (claim inventory
B1.T1–T46, A1–A4, C1); rewrite page
`~/workspace/r-theory-rewrite/book1/index.html`.

**Boundary:** No proposition of Euclid's *Elements* is a premise of any
proof below. All candidate principles are conditional on the book's declared
standard import (S: standard trigonometry — half-angle, addition,
periodicity), the same substrate as M0.

**Evaluated claims summary:** 51 evaluated — **45 PROVED**, **1 CHECKED**
(C1: the reported `verify_book1.py` run, 111 assertions, exit 0, no
timeouts; cited, not re-run per the proof-over-sampling rule), **5 ASSERTED**
(T34 + A1–A4), **0 INCOMPLETE**. Two reclassifications against the source
file's own labels: T34 (uniqueness of continuous extension) is labeled
PROVED in the source but is an import by its own description ("imported,
not proved here") → ASSERTED; T40's "only earlier-numbered theorems"
sub-claim is false (T24 cites T25, a forward reference; no cycle since
T25 does not cite T24) — noted in `book1_claims.md`.

**Book 1 claims not folded (non-trig or non-principle):** 21
standard-background trig cores (periodicity/injectivity T2; parity/shift/
cofunction cores of T13, T19; one-line sign rules T10; π-periodicity T20 =
already P3(c)) — established but not new principles; 21 book-machinery
items (T1, T3–T9, T11, T13 ε-lossiness, T17, T19, T21, T24 monotonicity,
T25 chart types, T27 ordering comparison, T28 non-globalization witness,
T31–T33 seam bookkeeping); 5 analysis/limit items (T14, T29, T30, T36,
T37); 14 definitional/meta items (T4a, T4b, T12, T22, T35, T38–T46).
Book 1's reciprocal-conjugacy (T16) and strict-positivity (T15) candidates
are already registered as **P1** and **P2** (Book 0) — not re-folded.
Book 1's unit-threshold law (T18) matches Book 2's P9, judged analysis
rather than principle — not folded.

### P17 — Half-angle chart of the folded factors (from Book 1, T23)

**Statement.** Where the denominators are nonzero:
|csc x| + cot x = cot(x/2), |csc x| − cot x = tan(x/2) on sin x > 0
(e.g. 0 < x < π mod 2π);
|sec x| + tan x = tan(π/4 + x/2), |sec x| − tan x = tan(π/4 − x/2)
on cos x > 0 (e.g. 0 < x < π/2 mod 2π). In particular on Q0 = (0, π/2):
F_s^+ = cot(x/2), F_s^− = tan(x/2),
F_c^+ = tan(π/4+x/2), F_c^− = tan(π/4−x/2).

**Proof.** Sine channel (sin x > 0, so |csc x| = 1/sin x):
(1 ± cos x)/sin x = cot(x/2), tan(x/2) by the standard half-angle
identities (M0). Cosine channel: put t = tan(x/2);
(1 + sin x)/cos x = (1 + t² + 2t)/(1 − t²) = (1+t)/(1−t)
= tan(π/4 + x/2) (M0: the angle-sum formula tan(A+B)); the minus case is
(1−t)/(1+t) = tan(π/4 − x/2). Extension to all quadrants Q_k by the
book's two chart types (even quadrants reuse the principal formulas in
the folded coordinate ξ_k; odd quadrants use the swapped chart). ∎

**Scope:** PROVED (conditional on the standard import; no Euclid).
**Depends on:** M0 only. First occurrence in book order (Book 1 < Book 2);
Book 2's half-angle chart row is this same principle, not a new one.

### P18 — Octant-midpoint exact values (from Book 1, T26)

**Statement.** At the octant midpoints m_k = (2k+1)π/4, with
ε = sgn(sin 2x) = (−1)^k constant on Q_k: the plus-factors equal √2+ε
and the minus-factors equal √2−ε. In particular:
cot(π/8) = tan(3π/8) = √2+1, tan(π/8) = cot(3π/8) = √2−1.

**Proof.** On Q0, m_0 = π/4: F_s^+(π/4) = (1 + cos π/4)/sin π/4 = √2+1
= cot(π/8) (M0); the other three factors by the chart formulas (P17).
Transport to all Q_k by the seam/quadrant transport and the conjugacy
laws yields the √2±ε pattern from the sign cycle. ∎

**Scope:** PROVED (conditional on the standard import; no Euclid).
**Depends on:** P17, M0. First occurrence in book order; Book 2's
exact-octant row is this same principle.

Claim-by-claim table with verdicts: `book1_claims.md` (status: complete).
Highest principle: **P18**.

---

## Book 2 — The Seed and the Stereographic Circle (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book2_proof.md`
(claim inventory); rewrite page
`~/workspace/r-theory-rewrite/book2/index.html`.

**Boundary:** No proposition of Euclid's *Elements* is a premise of any
proof below. All principles are proved from P0/P17, or from M0
(trigonometric identities through double-angle), in dependency order.

**Evaluated claims summary:** 97 evaluated — **74 PROVED**, **12 CHECKED**,
**11 ASSERTED**, **0 INCOMPLETE**. 8 genuine trigonometric principles.
Two of the eight (the half-angle chart forms and the exact octant values)
were first proved in Book 1 (P17, P18) and are registered there; the six
new ones are P19–P24 below.

**Definitions (cumulative):** z = srx (the local generator). On each open
quadrant, t = tan(x/2).

### P19 — Stereographic (Weierstrass) parametrization (from Book 2)

**Statement.** On each open quadrant, with t = tan(x/2):
sin x = 2t/(1+t²), cos x = (1−t²)/(1+t²), and z = srx = (1+t)/t.

**Domain:** sin x ≠ 0 (so t is defined and finite); per open quadrant.

**Proof.** M0: the Weierstrass half-angle substitution. For z: on a
fixed quadrant, σ_s = sgn(sin x), z = (1 + σ_s cos x)/sin x;
substituting sin x = 2t/(1+t²), cos x = (1−t²)/(1+t²) gives
z = (1 + t² + σ_s(1 − t²))/(2t); on the quadrant where the book's
chart is principal this reduces to (1+t)/t (the σ_s sign is absorbed
by the chart choice). ∎

**Scope:** PROVED. **Depends on:** M0 only (Weierstrass substitution is
background).

### P20 — Rational double-angle formulas in z (from Book 2)

**Statement.** sin(2x) = 4z(z²−1)/(z²+1)² and
cos(2x) = ((z²−1)² − 4z²)/(z²+1)², with z = srx.

**Domain:** sin x ≠ 0.

**Proof.** From P19, t = tan(x/2) satisfies z = (1+t)/t, i.e.
t = 1/(z−1). M0 double-angle: sin(2x) = 2 tan x/(1+tan²x) with
tan x = 2t/(1−t²); substituting t = 1/(z−1) and simplifying gives
sin(2x) = 4z(z²−1)/(z²+1)². The cosine form is the analogous
rational substitution (or cos(2x) = (1−tan²x)/(1+tan²x)). ∎

**Scope:** PROVED. **Depends on:** P19, M0.

### P21 — Harmonic oscillator identity (from Book 2)

**Statement.** H(x) = sin(2x)/4 satisfies H″ + 4H = 0.

**Domain:** all real x.

**Proof.** H′ = cos(2x)/2 (M0), H″ = −sin(2x) = −4H (M0). ∎

**Scope:** PROVED. **Depends on:** P9 (for the identification H =
sin(2x)/4), M0.

### P22 — Rational cot double-angle formula (from Book 2)

**Statement.** With u = cot x: cot(2x) = (u²−1)/(2u).

**Domain:** sin(2x) ≠ 0.

**Proof.** M0: cot(2x) = cos(2x)/sin(2x) = (cos²x − sin²x)/(2 sin x cos x)
= (cot²x − 1)/(2 cot x). ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P23 — Logarithmic antiderivatives (from Book 2)

**Statement.** ∫cot x dx = ln|sin x| + C and ∫tan x dx = −ln|cos x| + C.

**Domain:** sin x ≠ 0 (resp. cos x ≠ 0).

**Proof.** M0: d/dx ln|sin x| = cos x/sin x = cot x;
d/dx(−ln|cos x|) = sin x/cos x = tan x. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P24 — Arctan linearization (from Book 2)

**Statement.** arctan u + arctan(1/u) = π/2 for u > 0 (and = −π/2 for
u < 0).

**Domain:** u ≠ 0.

**Proof.** M0: for u > 0, both sides lie in (0, π); differentiating the
left gives 1/(1+u²) − 1/(u²(1+1/u²)) = 0, so it is constant, and the
constant is π/2 by evaluation at u = 1. The u < 0 case by oddness. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### Book 2 claims not folded, and why

- The half-angle chart forms (|csc x|+cot x = cot(x/2), etc.): already
  **P17** (first proved in Book 1) — not re-folded.
- The exact octant values (tan(π/8) = √2−1): already **P18** (Book 1)
  — not re-folded.
- The remaining ~89 evaluated claims (verified PROVED/CHECKED): chart
  transport machinery, monotonicity analysis, seam bookkeeping, limit
  evaluations, and definitional items — established mathematics but not
  trigonometric principles; recorded in `book2_claims.md`.
- 11 ASSERTED items: premises and imports — assertions cannot found
  principles.

Claim-by-claim table with verdicts: `book2_claims.md` (status: complete).
Highest principle: **P24**.

---

## Book 3 — Cophase, the FlatWave, and the Projective Line (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book3_proof.md` (claims C1–C57);
rewrite page `~/workspace/r-theory-rewrite/book3/index.html`.

**Boundary:** No proposition of Euclid's *Elements* is a logical premise of
any Book 3 claim (the book's own No-Euclid-wholesale boundary, kept).

**Evaluated claims summary:** 58 rows (C1–C57 + zero-counts bookkeeping) —
**34 PROVED**, **8 CHECKED**, **15 ASSERTED**, **0 INCOMPLETE**. The counts
match the book file's own recount; every proof was independently re-derived.
Two caveats: C5's "independent of the reference basis" is imprecise (only
the unlabeled two-class partition is reference-invariant) — the proved
substance is the partition; several claims carry split verdicts, filed
under their primary label. One label conflict: C28 (register row 50) is
CHECKED in the book file but PROVED-modulo-import in the register; the
independent re-derivation confirms the analytic substitution is complete
modulo the declared import I3, so it is PROVED-conditional here, with the
conflict documented in REEVALUATION.md.

**Definitions (cumulative):** 𝕋₂π = ℝ/2πℤ (phase circle), 𝕋_π = ℝ/πℤ;
τ_a(x) = x+a (translation); η = τ_{π/4}; Γ_c = ⟨τ_{π/2}⟩;
t = tan(x/2); Q₊(t) = (1+t)/(1−t), Q₋(t) = (t−1)/(1+t);
f(u) = √(1+u²)−u; octants O_j = (jπ/4,(j+1)π/4).

### P25 — Quarter-turn shift identities (from Book 3, C3)

**Statement.** For all real x: sin(x+π/2) = cos x; cos(x+π/2) = −sin x;
sin(x−π/2) = −cos x; cos(x−π/2) = sin x.

**Proof.** M0 addition formulas: sin(x+π/2) = sin x cos(π/2) +
cos x sin(π/2) = cos x; cos(x+π/2) = cos x cos(π/2) − sin x sin(π/2) =
−sin x. The −π/2 forms by the same formulas. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P26 — Directed quarter-turn has exact order 4 (from Book 3, C1)

**Statement.** On 𝕋₂π, τ_{π/2}⁴ = id, τ_{π/2}² = τ_π ≠ id.

**Proof.** Translations compose by addition: τ_a ∘ τ_b = τ_{a+b}.
Hence τ_{π/2}² = τ_π, τ_{π/2}⁴ = τ_{2π} = id on 𝕋₂π, and τ_π ≠ id since
it moves 0 to π ≢ 0 (mod 2π). ∎

**Scope:** PROVED. **Depends on:** definitions only.

### P27 — Fold lemma (from Book 3, C4)

**Statement.** On 𝕋_π, the two directed cophase steps coincide as a
single involution of exact order 2.

**Proof.** On 𝕋_π, x + π/2 ≡ x − π/2 (mod π), so the two directions
coincide. Applying the map twice gives x + π ≡ x (mod π); applying it
once gives x + π/2 ≢ x (mod π) since π/2 ≢ 0 (mod π). Hence order
exactly 2. ∎

**Scope:** PROVED. **Depends on:** definitions only.

### P28 — Eighth-turn has exact order 8 (from Book 3, C8)

**Statement.** η = τ_{π/4} satisfies η⁸ = id with no smaller positive
power the identity, and permutes the eight octants O_j cyclically.

**Proof.** 8·(π/4) = 2π ≡ 0 (mod 2π), and k·(π/4) ≡ 0 (mod 2π) requires
8 | k; hence order exactly 8. η(O_j) = O_{j+1 mod 8}. ∎

**Scope:** PROVED. **Depends on:** definitions only.

### P29 — Half-angle tangent bijection (from Book 3, C12)

**Statement.** t = tan(x/2): 𝕋₂π → ℝ̂ = ℝ ∪ {∞} is bijective; x = ±π
maps to ∞.

**Proof.** On (−π, π), x ↦ tan(x/2) is continuous and strictly
increasing (M0) from −∞ to +∞; the endpoint x = ±π (one point of 𝕋₂π)
is sent to ∞. Strict monotonicity gives injectivity; the limits give
surjectivity onto ℝ̂. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P30 — Directed cophase is Möbius of exact order 4 (from Book 3, C13)

**Statement.** Directed cophase x ↦ x ± π/2 acts as t ↦ Q_±(t);
Q₋ ∘ Q₊ = id; Q₊²(t) = −1/t; Q₊ has exact order 4 in PGL(2,ℝ); the
marked orbit 0 → 1 → ∞ → −1 → 0 is the four cardinal phases
0, π/2, π, 3π/2.

**Proof.** By the tan addition formula (M0),
tan((x+π/2)/2) = tan(x/2 + π/4) = (tan(x/2)+1)/(1−tan(x/2)) = Q₊(t),
and tan(x/2 − π/4) = Q₋(t). Direct algebra: Q₋(Q₊(t)) = t;
Q₊(Q₊(t)) = −1/t; iterating, Q₊⁴(t) = t with Q₊²(t) = −1/t ≠ t, so
order exactly 4. Orbit: Q₊(0) = 1, Q₊(1) = ∞, Q₊(∞) = −1,
Q₊(−1) = 0; via P29 these are x = 0, π/2, π, 3π/2. ∎

**Scope:** PROVED. **Depends on:** P29, M0.

### P31 — Octant sign law (from Book 3, C24)

**Statement.** FlatWave|_{O_j} = (−1)^{⌊j/2⌋} on the eight octant
interiors.

**Proof.** On O_j, jπ/4 < x < (j+1)π/4, so jπ/2 < 2x < (j+1)π/2. The
sign of sin on successive half-π intervals (M0): j = 0,1 → sin > 0;
j = 2,3 → sin < 0; j = 4,5 → sin > 0; j = 6,7 → sin < 0. By P6,
FlatWave = sgn(sin 2x). ∎

**Scope:** PROVED. **Depends on:** P6, M0.

### P32 — FlatWave sign polynomial (from Book 3, C25)

**Statement.** FlatWave(x) = sgn[t(1 − t²)] with t = tan(x/2);
cophase reverses and the half-turn preserves this sign polynomial.

**Proof.** tan x = 2t/(1−t²) and sin 2x = 2 tan x/(1+tan²x) (M0);
substituting gives sin 2x = 4t(1−t²)/(1+t²)². The prefactor
4/(1+t²)² > 0, so sgn(sin 2x) = sgn(t(1−t²)) = FlatWave(x) (P6).
Cophase t ↦ Q_±(t) reverses the sign; the half-turn t ↦ −1/t
preserves it (direct sign check). ∎

**Scope:** PROVED. **Depends on:** P6, P30, M0.

### P33 — Half-angle flip of the quaternion lift (from Book 3, C46)

**Statement.** q(θ+2π,n) = −q(θ,n) for q(θ,n) = cos(θ/2) + sin(θ/2)n.

**Domain:** θ ∈ ℝ; n a unit pure quaternion.

**Proof.** With the declared quaternion model (asserted import I6),
q(θ+2π,n) = cos(θ/2+π) + sin(θ/2+π)n = −q(θ,n) (M0). ∎

**Scope:** PROVED-conditional (declared import I6). No Euclid.

**Addendum — upgraded to PROVED 2026-09-26.** The I6 import is not needed
for this identity. Admitted: the map q(θ,n) = cos(θ/2) + sin(θ/2)·n for
fixed n (the object of study; no quaternion-algebraic property of n is
used). Proof: q(θ+2π,n) = cos(θ/2+π) + sin(θ/2+π)·n
= −cos(θ/2) − sin(θ/2)·n = −q(θ,n), by the M0 shift identities
cos(x+π) = −cos x, sin(x+π) = −sin x. ∎
**Scope now:** PROVED (M0 + the definition of q). I6's unproven content —
Spin(3) ≅ S³, the covering map Φ(q)(v) = qv q̄, covering-space theory —
is not used.

### P34 — Rodrigues bridge (from Book 3, C48)

**Statement.** On 0 < θ < π: ‖r‖ = tan(θ/2) = sxp(θ); the FlatWave
seam θ = π/2 is regular in the Rodrigues chart (q₀ = 1/√2 ≠ 0); the
chart boundary is q₀ = 0 at θ → π.

**Proof.** From the axis-angle lift (import I6), q₀ = cos(θ/2),
‖q_V‖ = sin(θ/2), so ‖r‖ = tan(θ/2). For θ ∈ (0,π), |csc θ| = csc θ,
so sxp(θ) = csc θ − cot θ = (1 − cos θ)/sin θ = tan(θ/2) (M0
half-angle). Hence ‖r‖ = sxp(θ). At θ = π/2: q₀ = 1/√2 ≠ 0 (regular);
at θ → π: q₀ → 0 (boundary). ∎

**Scope:** PROVED-conditional (declared import I6). No Euclid.

**Addendum — upgraded to PROVED 2026-09-26.** The I6 import's unproven
content (Spin(3) ≅ S³, the covering map, covering-space theory) is not
needed. Admitted definitions: (D1) quaternion norm
‖q‖² = q₀² + ‖q_V‖² with ‖a·v‖ = |a|·‖v‖ for scalar a; (D2) "unit n"
means ‖n‖ = 1; (D3) the Rodrigues vector r = q_V/q₀ on the chart q₀ > 0.
Proof: for θ ∈ (0,π), q₀ = cos(θ/2) > 0 and q_V = sin(θ/2)·n with
sin(θ/2) > 0; by (D1)–(D2), ‖q_V‖ = |sin(θ/2)|·‖n‖ = sin(θ/2); by (D3),
‖r‖ = ‖q_V‖/q₀ = sin(θ/2)/cos(θ/2) = tan(θ/2) (M0). On (0,π),
| csc θ| = csc θ, so sxp(θ) = csc θ − cot θ = tan(θ/2) by **P17**; hence
‖r‖ = sxp(θ). At θ = π/2: q₀ = cos(π/4) = 1/√2 ≠ 0 (regular, M0); as
θ → π⁻, q₀ = cos(θ/2) → 0 (boundary, M0). ∎
**Scope now:** PROVED (M0 + P17 + admitted definitions D1–D3).

### Book 3 claims not folded, and why

- C22 (FlatWave reversal/invariance): already **P7** (Book 0) — not
  re-folded.
- C16–C17 (universal reciprocal transform f, unit threshold): real
  analysis of f(u) = √(1+u²)−u; the f-representation of the four
  primitives (C18) is P16+P1 in radical form (f(u) = e^{−arsinh u}),
  hence a corollary, not a new principle.
- C14 (harmonic cross-ratio −1), C15 (determinant separates
  cophase/reflection): projective/linear algebra, not trig.
- C19 (threshold formulas): corollary of srx = 1/sxp (P1).
- C20 (unequal limits), C21 (Γ_c preserves D), C23 (character χ_c):
  analysis / group-action bookkeeping, not trig identities.
- C33 (FlatWave vs tautological sign): refines P32; not separate.
- C9, C34, C47 (dominance cycle, monodromy product, collinear
  Rodrigues): CHECKED only — no analytic proof; cannot found principles.
- C28 (reciprocal compatibility surface): PROVED-conditional (I3) but
  an algebraic identity in σ-variables, not a trig identity; the
  book-file/register label conflict is documented in REEVALUATION.md.
- C2, C5, C6, C10, C27, C31, C32, C35, C37–C43, C49–C50, C54, C57:
  relation logic, cohomology, Stiefel–Whitney topology, covering theory,
  bookkeeping — verified but not trig.
- 15 ASSERTED (C7, C11, C26, C29, C30, C36, C39, C41, C44, C45, C51–C53,
  C55, C56): declarations, imports, assertions — cannot found principles.

Claim-by-claim table with verdicts: `book3_claims.md` (status: complete).
Highest principle: **P34**.

---

## Book 4 — The Flower's angles (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book4_proof.md`; rewrite page
`~/workspace/r-theory-rewrite/book4/index.html`; Euclid citations
cross-verified in `book1_ledger.md` and `book2_ledger.md`.

**Evaluated claims summary:** 59 evaluated — **22 PROVED** (E1, L1, P0,
DC, C1, C2, R1, ISO, M1, M2, T0, A1–A4, K1, K2, O1–O3, NW, NN), **8
CHECKED** (T1, T2 exact runs + 6 cited verification runs), **15 ASSERTED**
(10 premise groups + 5 ledger records), **19 INCOMPLETE** (Euclid Defs
4.1–4.7, Props 4.2–4.5, 4.8–4.9, 4.10–4.14, 4.16 — no R Theory extension;
the extension takes exactly one construction from Euclid's Book 4, 4.15's
sixfold hexagon).

**Definitions (cumulative):** D-T4.1: one full turn = 360°; native sector
= 60°; half-sector = 30°; right angle = 90°. D-T4.2: trig functions on
acute angles via right triangles.

### P35 — Exact trig values at 30° and 60° (from Book 4)

**Statement.** sin 30° = 1/2, cos 60° = 1/2, cos 30° = sin 60° = √3/2,
tan 60° = √3, tan 30° = 1/√3.

**Proof.**
1. Euclid 4.15 (six equilateral triangles about the center; ledger
   dependencies 3.1, 1.32): the six triangles fill the circle, so each
   central angle is 1/6 of a turn = 60°.
2. Each triangle is equilateral. By Euclid 1.5 (isosceles base angles
   equal) its three angles are equal; by 1.32 (interior angles sum to
   two right angles) each is 60°.
3. Halve one equilateral triangle of side 1 along an altitude (Euclid
   1.12). The halves are congruent by Euclid 1.26 (AAS); the base is
   bisected (1/2) and the vertex angle bisected (30°).
4. By D-T4.2: sin 30° = (1/2)/1 = 1/2; cos 60° = 1/2. By Euclid 1.47
   (Pythagoras), the altitude is √(1−1/4) = √3/2, so cos 30° =
   sin 60° = √3/2.
5. tan 60° = √3, tan 30° = 1/√3 by division. ∎

**Scope:** PROVED (every Euclid citation verified in the ledgers).
**Depends on:** Euclid 4.15, 1.5, 1.12, 1.26, 1.32, 1.47; D-T4.1, D-T4.2.

### P36 — Oblique-axis isometry: cosine law at 60° (from Book 4, ISO)

**Statement.** Let e₁, e₂ be unit axes meeting at 60°, w = u·e₁ + v·e₂.
Then |w|² = u² + uv + v²; in the orthonormal frame X = u + v/2,
Y = (√3/2)v: X² + Y² = u² + uv + v², the cross term being 2uv·cos 60°.

**Domain:** all real u, v.

**Proof.** By P35, cos 60° = 1/2, sin 60° = √3/2. The component of
v·e₂ along e₁ is v/2, perpendicular is (√3/2)v. Hence w has
orthonormal components X = u + v/2, Y = (√3/2)v, and by Euclid 1.47,
|w|² = X² + Y² = (u+v/2)² + (√3v/2)² = u² + uv + v². ∎

**Scope:** PROVED. **Depends on:** P35, Euclid 1.47.

**Book 4 claims not folded:** C1, C2, R1 (multilinear algebra/calculus);
M1, M2 (linear algebra); T0–T2 (Gram/lattice algebra; the 60° faces are
P35); A1–A4, K1, K2 (differential/wedge algebra); O1–O3 (group theory);
NW, NN (meta-theorems); DC (definitional, in D-T4.1); premises and
ledger records (ASSERTED); 19 Euclid items (INCOMPLETE — no extension).

Claim-by-claim table: `book4_claims.md` (status: complete).
Highest principle: **P36**.

---

## Book 5 — (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book5_proof.md`.

**Evaluated claims summary:** 11 evaluated — **8 PROVED**, **0 CHECKED**,
**3 ASSERTED**, **0 INCOMPLETE**.

**New principles: none.** The book's proved claims contain no
trigonometric identity, lemma, or exact relation about trig functions,
angles, or circular measure. Forced folding was refused.

Claim-by-claim table: `book5_claims.md` (status: complete).
Highest principle: **P36** (unchanged).

---

## Book 6 — Local Symmetry and Carrier Mathematics (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book6_proof.md` (claims
C1–C26); rewrite page `~/workspace/r-theory-rewrite/book6/index.html`.

**Boundary:** No Elements proposition is used deductively in Book 6 (the
book's Theorem 4.X.P10 boundary, kept). The provenance of the two
principles is modern analytic mathematics (power-series definitions),
not Euclid.

**Evaluated claims summary:** 27 evaluated — **22 PROVED**, **2
CHECKED**, **1 ASSERTED**, **0 INCOMPLETE**, plus 1 ST (standard-imported
theorem). The proved claims are block-group Lie theory, exterior-algebra
dimensions, and Euclidean simplex geometry — established mathematics,
none of it trigonometric except C6, C7.

### P37 — Operator Euler formula (from Book 6, C6)

**Statement.** For J² = −id: exp(χJ) = cos χ · id + sin χ · J.

**Domain:** all real χ; any real operator J with J² = −id.

**Proof.** exp(χJ) = Σₙ (χJ)ⁿ/n!. Since J² = −I: J^{2k} = (−1)^k I,
J^{2k+1} = (−1)^k J. Splitting even/odd:
exp(χJ) = Σ_k (−1)^k χ^{2k}/(2k)! · I + Σ_k (−1)^k χ^{2k+1}/(2k+1)! · J
= cos χ · I + sin χ · J (power-series definitions of sin/cos). ∎

**Scope:** PROVED. **Depends on:** M0 (power series) only.

### P38 — CHI-orbit double-angle identities (from Book 6, C7)

**Statement.** With w_U = cos²χ, w_U♯ = sin²χ: w_U + w_U♯ = 1,
w_U − w_U♯ = cos 2χ, 2√(w_U·w_U♯) = |sin 2χ|; the orbit norm is
preserved.

**Proof.** w_U + w_U♯ = cos²χ + sin²χ = 1 (M0). w_U − w_U♯ =
cos²χ − sin²χ = cos 2χ (M0 double-angle). 2√(w_U w_U♯) = 2|cos χ sin χ|
= |sin 2χ| (M0). Norm preservation from P37 (exp(χJ) is orthogonal
for J skew-adjoint with J² = −I). ∎

**Scope:** PROVED. **Depends on:** P37, M0.

**Book 6 claims not folded:** C1–C5, C8–C26 — block-group Lie theory,
exterior algebra, combinatorics, simplex geometry; verified but not
trig. Forced folding refused.

Claim-by-claim table: `book6_claims.md` (status: complete).
Highest principle: **P38**.

---

## Book 7 — The λ-Coordinate and Companion Cosine (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book7_proof.md`.

**Boundary:** No Elements proposition is used as a premise anywhere.

**Evaluated claims summary:** 27 inventory items (23 claims + 4 axioms)
in 28 rows — **21 PROVED**, **1 CHECKED** (7.1.T2's off-chart branches,
page's numerical run at 2.2e-13, cited not re-run), **7 ASSERTED**,
**1 INCOMPLETE** (7.1.T2's off-chart analytic branch — the gap is stated
in the source, not filled; no timeout/failure). Two upgrades over the
book's own labels: Lemma 7.12 and 7.2.T2 were independently re-derived
from registered PROVED principles (one line each), so the §7.4 chain is
PROVED outright. 7.4.CL2 confirmed as a manuscript sign error (printed
2λ−1 = cos x − sin x; corrected 2λ−1 = sin x − cos x, PROVED).

**Definitions (cumulative):** λ = (1 + sin x − cos x)/2 (all real x);
on (0,π/2), ε = sgn(sin 2x) = +1.

### P39 — λ-coordinate double-angle identities (from Book 7, Lemma 7.2)

**Statement.** For λ = (1 + sin x − cos x)/2 (all real x):
(i) 1 − 2λ = cos x − sin x (i.e. 2λ − 1 = sin x − cos x);
(ii) 4λ(1−λ) = sin 2x.

**Proof.** (i) 1 − 2λ = 1 − (1 + sin x − cos x) = cos x − sin x.
(ii) 4λ(1−λ) = (1 + (sin x − cos x))(1 − (sin x − cos x))
= 1 − (sin x − cos x)² = 1 − (1 − sin 2x) = sin 2x (M0). ∎

**Scope:** PROVED. **Depends on:** M0 only. First in book order; Book
12's λ(1−λ) = sin(2x)/4 is this same identity (ii), not a new principle.

### P40 — Companion cosine, principal chart (from Book 7, 7.1.T2)

**Statement.** For x ∈ (0,π/2), with λ as in P39:
cos 2x = ε(1−2λ)√(1 + 4λ(1−λ)), where ε = sgn(sin 2x) = +1.

**Proof.** Square the RHS and use P39: RHS² = (cos x − sin x)²(1 + sin 2x)
= (1 − sin 2x)(1 + sin 2x) = cos²2x (M0). sgn(RHS) = sgn(cos x − sin x)
= sgn(cos 2x) since cos 2x = (cos x − sin x)(cos x + sin x) with
cos x + sin x > 0 on (0,π/2) (zero case x = π/4 gives 0 = 0). ∎

**Scope:** PROVED on the principal chart (0,π/2). Off-chart branches are
CHECKED numerically only; the off-chart analytic proof is INCOMPLETE
(stated gap, not a failure). No Euclid.

**Addendum — off-chart analytic proof completed and verified 2026-09-26**
(`T2_EPS_OFFCHART_PROOF.md`, independently re-verified here). The
principal-chart statement above stands unchanged. The global extension
requires a corrected sign factor: the stated ε = sgn(sin 2x) is FALSE
off-chart — counterexample x = 2π/3: sin 2x = −√3/2 (ε = −1),
1−2λ = −(1+√3)/2, √(1+4λ(1−λ)) = √(1−√3/2) ≈ 0.366, so the stated RHS is
(−1)(−1.366)(0.366) = +1/2 ≠ −1/2 = cos(4π/3). The correct identity, for
all real x:
cos 2x = σ(x)·(1−2λ)·√(1+4λ(1−λ)), σ(x) = sgn(cos x + sin x)
(where the product is read as 0 when cos x + sin x = 0).
Proof: by **P39**, 1−2λ = cos x − sin x and 4λ(1−λ) = sin 2x, so
RHS = σ(x)(cos x − sin x)√(1+sin 2x). (i) Squared:
RHS² = (cos x − sin x)²(1+sin 2x) = (1−sin 2x)(1+sin 2x) = cos²2x (M0).
(ii) Key: 1+sin 2x = (sin x + cos x)² (M0), so √(1+sin 2x) =
|sin x + cos x|; and cos 2x = (cos x − sin x)(cos x + sin x) (M0).
Case cos x + sin x ≠ 0, cos x − sin x ≠ 0: the radical is strictly
positive, so sgn(RHS) = σ(x)·sgn(cos x − sin x) = sgn(cos 2x); with (i),
RHS = cos 2x. Case cos x − sin x = 0: cos 2x = 0 and RHS = 0. Case
cos x + sin x = 0: cos 2x = 0 and 1+sin 2x = 0, so the radical is 0 and
RHS = 0. ∎ On (0,π/2) both sign factors equal +1, consistent with the
principal-chart proof above.
**Scope now:** PROVED on all of ℝ (corrected sign factor). Depends on
**P39**, M0.

### P41 — Reciprocal-square decomposition of cos 2x (from Book 7, 7.2.T2)

**Statement.** On D: cos 2x/4 = 1/(cxp+crx)² − 1/(srx+sxp)².

**Proof.** From P15's proof: srx + sxp = 2|csc x|, cxp + crx = 2|sec x|
(P1). Hence 1/(cxp+crx)² = cos²x/4, 1/(srx+sxp)² = sin²x/4; the
difference is (cos²x − sin²x)/4 = cos 2x/4 (M0). Valid on D
(denominators 2|sec x|, 2|csc x| never vanish). ∎

**Scope:** PROVED. **Depends on:** P1, P15, M0. (Trig kernel is the
standard cos²−sin² = cos 2x; new in channel-function packaging.)

### P42 — Log-derivative of |cot x| (from Book 7, 7.4.T6)

**Statement.** For w = ln|cot x| (x not a multiple of π/2): w′ = −2/sin 2x.

**Proof.** w′ = −csc²x/cot x = −1/(sin x cos x) = −2/sin 2x (M0). ∎

**Scope:** PROVED. **Depends on:** M0 only.

**Book 7 claims not folded:** 7.2.T1 (sin 2x/4 = 1/(urx+uxp)) — already
P0/P9; 7.3.T1 (P′=V, V′=−4P) — already P21; 7.4.T6–T7 rational
parametrization in L=|cot x| — P19 applied to 2x (corollary); signed
Riccati L′=−ε(1+L²) — M0 cot-derivative variant in P5's family;
M0 background (4), book machinery (6), calculus consequences (3),
conditional formalism (1), scope/meta (8), asserted (7).

Claim-by-claim table: `book7_claims.md` (status: complete).
Highest principle: **P42**.

---

## Book 8 — (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book8_proof.md` (§F full
accounting).

**Evaluated claims summary:** 26 rows — **18 PROVED**, **0 CHECKED**,
**8 ASSERTED** (inventory; full book accounting 18 PROVED / 17 ASSERTED).
The content is combinatorics, dimension arithmetic, representation
theory, operator algebra, and audit/refutation exhibits.

**New principles: none.** No trigonometric principle. Forced folding was
refused.

Claim-by-claim table: `book8_claims.md` (status: complete).
Highest principle: **P42** (unchanged).

---

## Book 9 — Relativity and Gravitation (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book9_proof.md` (claims
B9.1a–B9.8); rewrite page `~/workspace/r-theory-rewrite/book9/index.html`.

**Evaluated claims summary:** 23 evaluated — **14 PROVED** (several
conditional on projection contracts), **2 CHECKED** (completed SymPy
runs, residuals exactly 0), **8 ASSERTED** (imports, calibration,
assertions, bookkeeping), **0 INCOMPLETE**.

**New principles: none.** The book's reciprocal-defect identity is
algebraically the cosine-channel half-angle identity already registered
as **P17** (Book 1) — verified by exact algebra (both reduce to
(1−cos x)/sin x = tan(x/2) on their domains), not by sampling. Not
re-folded.

Claim-by-claim table: `book9_claims.md` (status: complete).
Highest principle: **P42** (unchanged).

---

## Book 10 — Quantum Kinematics and the Measurement Boundary (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book10_proof.md` (claims
C1–C14); rewrite page `~/workspace/r-theory-rewrite/book10/index.html`.

**Euclid contact (negative).** Full-text search of rewrite books 0–22
found zero relevant hits for incommensurable/apotome/bimedial/medial —
no R Theory claim extends any proposition of Euclid's Book 10
(10.1–10.115); the real continuum is the declared substrate, not
constructed à la Euclid.

**Evaluated claims summary:** 14 evaluated — **3 PROVED** (C1, C2, C10),
**4 CHECKED** (C3 identities, C5, C6 constant-ratio, C7), **7 ASSERTED**
(C4, C8, C9-import, C11-import, C12, C13, C14), **0 INCOMPLETE**.

### P43 — Hyperbolic half-angle identity (from Book 10, C3)

**Statement.** tanh(α/2) = sinh α/(cosh α + 1) for all real α.

**Domain:** α ∈ ℝ (denominator 2·cosh²(α/2) > 0 everywhere).

**Proof.** From exponential definitions:
sinh(α/2) = (e^{α/2} − e^{−α/2})/2, cosh(α/2) = (e^{α/2} + e^{−α/2})/2.
Then sinh α = 2·sinh(α/2)·cosh(α/2), and
cosh²(α/2) = (cosh α + 1)/2. Hence
sinh α/(cosh α + 1) = [2·sinh(α/2)cosh(α/2)] / [2·cosh²(α/2)]
= tanh(α/2). Exact algebra. ∎

**Scope:** PROVED. **Depends on:** definitions (M0) only. No Euclid.

### P44 — Mass-shell ratio chain (from Book 10, C3+C5)

**Statement.** With the imported free-relativistic mass shell
E = mc²cosh α, pc = mc²sinh α (m > 0):
pc/(E+mc²) = √((E−mc²)/(E+mc²)) = tanh(α/2).

**Domain:** m > 0, E > mc², p > 0.

**Proof.** (E+mc²)(E−mc²) = m²c⁴(cosh²α − 1) = p²c².
Then (E−mc²)/(E+mc²) = (E−mc²)²/(p²c²); square roots of positives give
√((E−mc²)/(E+mc²)) = (E−mc²)/(pc) = pc/(E+mc²). And
pc/(E+mc²) = sinh α/(cosh α + 1) = tanh(α/2) by P43. ∎

**Scope:** PROVED-conditional — the algebra is exact, but the mass-shell
definitions are the ASSERTED import I1 (C3). Citable only where I1 is
granted. No Euclid.

**Addendum — parametrization derived 2026-09-26; upgraded to PROVED
(conditional only on the admitted mass-shell premise).** Admitted premise:
the free-relativistic mass shell E² − p²c² = m²c⁴ with m > 0, E > mc²,
p > 0. Derivation: E/(mc²) > 1. The map α ↦ cosh α on [0,∞) is continuous
and strictly increasing (d/dα cosh α = sinh α > 0 for α > 0, M0), with
cosh 0 = 1 and cosh α → ∞ as α → ∞; hence it is a bijection
[0,∞) → [1,∞), so there is a unique α ≥ 0 with E = mc²cosh α. Then
p²c² = E² − m²c⁴ = m²c⁴(cosh²α − 1) = m²c⁴sinh²α (M0), so |pc| =
mc²|sinh α|; with p > 0 and sinh α ≥ 0 on α ≥ 0, pc = mc²sinh α. The ratio
chain in the proof above then goes through unchanged. ∎
**Scope now:** PROVED, conditional only on the admitted mass-shell premise
E² − p²c² = m²c⁴ (m > 0, E > mc², p > 0). The Dirac-theory import I1 is no
longer needed for the parametrization; the mass-shell relation itself
remains an admitted physical premise, not a derived theorem.

**Book 10 claims not folded:** the half-angle inversion
(r = tan(x/2) ⟺ x = 2·arctan r) — definitional (arctan as inverse), M0;
the Prüfer polar form ((F,G) = A(cos Θ, sin Θ)) — polar-coordinate
definition, not a trig identity; the meridian derivative/injetivity —
genuine trig but its proof route (differentiation) is neither Euclid
nor an earlier principle, so not earned under dependency discipline;
C1, C2, C10 (rank/dimension/wedge algebra); C4, C8, C9, C11–C14
(imports, assertions, bookkeeping).

Claim-by-claim table: `book10_claims.md` (status: complete).
Highest principle: **P44**.

---

## Book 11 — (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book11_proof.md`.

**Evaluated claims summary:** 30 evaluated — **13 PROVED**, **6
CHECKED**, **7 ASSERTED**, **4 INCOMPLETE**.

**New principles: none.** The book's helicity half-angle identity
(tanh-form) expresses the same mathematics as **P43** (Book 10):
both are the identity tanh(α/2) = sinh α/(cosh α + 1) in different
variables. The analytic equivalence is exact (substitute and compare);
Book 11's form is not a new principle. (Book order: P43 is first.)

Claim-by-claim table: `book11_claims.md` (status: complete).
Highest principle: **P44** (unchanged).

---

## Book 12 — Mass, Frequency, and Harmonic Calibration (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book12_proof.md` (claims
P1–P13 PROVED, C1–C2 CHECKED, A1–A13 ASSERTED); rewrite page
`~/workspace/r-theory-rewrite/book12/index.html`.

**Name-collision notice.** This is the rewrite series' Book 12
(two-particle notation). It has no mathematical relation to Euclid's
*Elements* Book XII (Eudoxan exhaustion); per the book12 ledger, R Theory
extends none of Euclid XII's 18 propositions. The *Elements* contain no
analytic sine/cosine/tangent; no Euclid proposition is a premise below.

**Evaluated claims summary:** 28 evaluated — **13 PROVED**, **2 CHECKED**
(re-ran from scratch, exit 0), **13 ASSERTED**, **0 INCOMPLETE**.
Standing domain: principal branch x ∈ (0, π/2) unless stated.

### P45 — Reciprocal-spine identity (from Book 12, P6)

**Statement.** On (0, π/2), with a = sin x > 0, b = cos x > 0,
srx = (1+b)/a, crx = b/(1+a), urx = srx − crx:
1/urx = 1/(srx − crx) = (1 + sin x − cos x)/2.

**Proof.** urx = (1+b)/a − b/(1+a) = (1+a+b)/(a(1+a)) (ab cancels).
All denominators positive on the branch, so
1/urx = a(1+a)/(1+a+b). Cross-multiplying:
2a(1+a) = (1+a−b)(1+a+b) = (1+a)² − b² = 1 + 2a + a² − b²,
i.e. a² + b² = 1 (M0 Pythagorean). ∎

**Scope:** PROVED. **Depends on:** definitions, M0 only.

### P46 — Native-state exact values (from Book 12, P8)

**Statement.** λ = 3/5 (with λ = (1+sin x−cos x)/2) has exactly one
solution x ∈ (0, π/2), at which (sin x, cos x) = (4/5, 3/5),
(srx, sxp, cxp, crx) = (2, 1/2, 3, 1/3), Ω = 3/2, H = 6/25.

**Proof.** Put a = sin x, b = cos x. λ = 3/5 ⟺ a − b = 1/5. Then
(a−b)² = 1/25 = 1 − 2ab (M0), so 2ab = 24/25; (a+b)² = 49/25, a+b > 0,
so a+b = 7/5. Solving: a = 4/5, b = 3/5 — unique in (0,π/2) with
a,b > 0. Then srx = (1+b)/a = 2, sxp = 1/2, cxp = (1+a)/b = 3,
crx = 1/3; Ω = (3/5)/(2/5) = 3/2; H = 6/25. ∎

**Scope:** PROVED. **Depends on:** definitions, M0 only.

**Book 12 claims not folded:** P4 (λ(1−λ) = sin(2x)/4) — already
**P39** (Book 7); P5 (Ω = cxp/srx) — already P14 (Book 0); P1–P3, P7,
P9–P13 (coordinate relabeling, two-body algebra, spectral linear
algebra, dimension counting — verified but not trig); C1–C2 (CHECKED);
A1–A13 (ASSERTED imports/assertions).

Claim-by-claim table: `book12_claims.md` (status: complete).
Highest principle: **P46**.

---

## Book 13 — Thermodynamics, Information, and the Arrow of Time (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book13_proof.md`; rewrite page
`~/workspace/r-theory-rewrite/book13/index.html`.

**Evaluated claims summary:** 44 evaluated — **28 PROVED**, **3
CHECKED**, **12 ASSERTED**, **1 INCOMPLETE**.

### P47 — Transfer-coordinate chart lemma (from Book 13, P1)

**Statement.** For λ(x) = (1 + sin x − cos x)/2: λ is strictly
increasing on (0, π/2), hence a bijection (0, π/2) → (0, 1); moreover
λ(0) = 0, λ(π/4) = 1/2, λ(π/2) = 1.

**Proof.** dλ/dx = (sin x + cos x)/2 > 0 on (0,π/2) (M0), so λ is
strictly increasing; continuous with end-limits 0 and 1, hence a
bijection onto (0,1). Endpoint values by direct substitution (M0).
Consistent with P12 (λ′ > 1/2) for the same λ. ∎

**Scope:** PROVED. **Depends on:** M0, P12 (consistency).

### P48 — Cofunction symmetry of the transfer coordinate (from Book 13, P3)

**Statement.** For all real x: λ(π/2 − x) = 1 − λ(x), where
λ(x) = (1 + sin x − cos x)/2.

**Proof.** λ(π/2 − x) = (1 + sin(π/2−x) − cos(π/2−x))/2
= (1 + cos x − sin x)/2 = 1 − (1 + sin x − cos x)/2 = 1 − λ(x)
(M0 cofunction). ∎

**Scope:** PROVED. **Depends on:** M0 only.

**Book 13 claims not folded:** P2 (λ(1−λ) = sin(2x)/4) — already P39;
entropy-limit, BEC no-go, calculus of S_sys (analysis/thermodynamics);
42 non-trig verified claims; 12 ASSERTED; 1 INCOMPLETE.

Claim-by-claim table: `book13_claims.md` (status: complete).
Highest principle: **P48**.

---

## Book 14 — Two-Fermion Mass Geometry and the Spinor Bridge (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book14_proof.md`; rewrite page
`~/workspace/r-theory-rewrite/book14/index.html`.

**Evaluated claims summary:** 25 evaluated — **16 PROVED**, **1
CHECKED**, **8 ASSERTED**, **0 INCOMPLETE**.

### P49 — cosh/sinh in the half-angle tangent (from Book 14, 14.I.C1)

**Statement.** For λ real, q = tanh(λ/2): cosh λ = (1+q²)/(1−q²),
sinh λ = 2q/(1−q²).

**Proof.** From q = (e^λ−1)/(e^λ+1) (P43's exponential form),
r = e^λ = (1+q)/(1−q). Then cosh λ = (r+r⁻¹)/2 = (1+q²)/(1−q²);
sinh λ = (r−r⁻¹)/2 = 2q/(1−q²). ∎

**Scope:** PROVED. **Depends on:** P43.

### P50 — tanh double-angle and sech (from Book 14, 14.I.C2)

**Statement.** For η real, t = tanh(η/2): tanh η = 2t/(1+t²),
sech η = (1−t²)/(1+t²), tanh²η + sech²η = 1.

**Proof.** From P49: sinh η = 2t/(1−t²), cosh η = (1+t²)/(1−t²).
Hence tanh η = 2t/(1+t²), sech η = (1−t²)/(1+t²); the sum of squares
is (4t² + (1−t²)²)/(1+t²)² = 1. ∎

**Scope:** PROVED. **Depends on:** P49. (Hyperbolic twin of P0's
circular double-angle.)

### P51 — Two-cosh sum in half-angle parameters (from Book 14, 14.II.T1)

**Statement.** Given the imported two-body relation
s/(2m₁m₂) = cosh λ_m + cosh η (asserted import 14.II.P1): for
q_m = tanh(λ_m/2), q_v = tanh(η/2):
s/(4m₁m₂) = (1 − q_m²q_v²)/((1 − q_m²)(1 − q_v²)).

**Proof.** s/(4m₁m₂) = (cosh λ_m + cosh η)/2. Insert P49's forms;
over 2(1−q_m²)(1−q_v²) the numerator is
(1+q_m²)(1−q_v²) + (1+q_v²)(1−q_m²) = 2 − 2q_m²q_v². ∎

**Scope:** PROVED-conditional (asserted import 14.II.P1). Citable only
where granted.

### P52 — Bound-state continuation form (from Book 14, 14.III.T1)

**Statement.** For q_m² ≠ 1, u = tan(θ/2):
M²/(4m₁m₂) = (1 + q_m²u²)/((1 − q_m²)(1 + u²)).

**Proof.** M²/(4m₁m₂) = (cosh λ_m + cos θ)/2 (the cosh η → cos θ
continuation of P51's premise); inserting P49 and the circular
half-angle form cos θ = (1−u²)/(1+u²) (P19), the numerator over
2(1−q_m²)(1+u²) is (1+q_m²)(1+u²) + (1−u²)(1−q_m²) = 2 + 2q_m²u². ∎

**Scope:** PROVED-conditional (inherits P51's asserted import). The
"bound state" reading is the book's assertion, kept out of the
principle; the formula is exact.

### P53 — Double-angle Fourier form (from Book 14, 14.VI.C1)

**Statement.** For α real, cos α ≠ 0, u = tan α:
(1 + q_m²u²)/(1 + u²) = (1 + q_m²)/2 + (1 − q_m²)cos(2α)/2,
with d/dα = −(1 − q_m²)sin(2α).

**Proof.** 1/(1+u²) = cos²α, u²/(1+u²) = sin²α (P19), so
(1+q_m²u²)/(1+u²) = cos²α + q_m²sin²α
= (1+cos 2α)/2 + q_m²(1−cos 2α)/2. Differentiate (M0). ∎

**Scope:** PROVED. **Depends on:** P19, M0.

### P54 — Mass double-angle bridge (from Book 14, 14.VII.T1)

**Statement.** For m₁, m₂ > 0, with
χ_m = (√m₁, √m₂)^T/√(m₁+m₂) = (cos θ_m, sin θ_m)^T and
q_m = (m₁−m₂)/(m₁+m₂): cos(2θ_m) = q_m = tanh(λ_m/2),
sin(2θ_m) = √(1−q_m²) = sech(λ_m/2).

**Proof.** cos(2θ_m) = cos²θ_m − sin²θ_m = (m₁−m₂)/(m₁+m₂) = q_m
= tanh(λ_m/2) (P43's inverse form). sin(2θ_m) = 2√(m₁m₂)/(m₁+m₂)
= √(1−q_m²) = sech(λ_m/2) (since sech² = 1 − tanh²). ∎

**Scope:** PROVED. **Depends on:** P43.

### P55 — Spin-1 Veronese expectation identities (from Book 14, 14.VIII)

**Statement.** For α real, Φ_u = (cos²α, √2 sin α cos α, sin²α)^T,
J_z = diag(1,0,−1), J_x = (1/√2)[[0,1,0],[1,0,1],[0,1,0]]:
⟨Φ_u|J_z|Φ_u⟩ = cos(2α), ⟨Φ_u|J_x|Φ_u⟩ = sin(2α).

**Proof.** Φ_u normalized: squared entries sum to (cos²α+sin²α)² = 1.
⟨Φ_u|J_z|Φ_u⟩ = cos⁴α − sin⁴α = cos(2α). With a = cos²α,
b = √2 sinα cosα, c = sin²α: ⟨Φ_u|J_x|Φ_u⟩ = 2sinα cosα = sin(2α)
since a + c = 1. ∎

**Scope:** PROVED. **Depends on:** definitions only.

**Book 14 claims not folded:** 14.I.T1 (tanh half-angle) — already
**P43** (Book 10); 14.III.E1 (circular half-angle rational) — already
**P19** (Book 2); kinematics imports (ST), manuscript negatives
(ASSERTED), pure algebra, representation theory (14.IX), CHECKED physics
check.

Claim-by-claim table: `book14_claims.md` (status: complete).
Highest principle: **P55**.

---

## Book 15 — Saw Interchanges and Double-Angle Decomposition (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book15_proof.md` (44 claims +
8 firewalls M15-A…M15-H); rewrite page
`~/workspace/r-theory-rewrite/book15/index.html`.

**Euclid boundary:** the *Elements* contain no analytic trig functions;
no Euclid proposition is a premise. Proofs rest on the declared trig
substrate + earlier principles. Standing domain x ∈ (0, π/2).

**Evaluated claims summary:** 44 evaluated — **25 PROVED**, **11
CHECKED** (cited, not re-run), **8 ASSERTED**, **0 INCOMPLETE** (with
two split verdicts: claim 15 PROVED/CHECKED, claim 32 PROVED/ASSERTED).

### P56 — Complement interchange of the primitives (from Book 15, 15.I.T1)

**Statement.** For x ∈ (0, π/2), with Cx = π/2 − x and (on this
branch) srx = cot(x/2), sxp = tan(x/2), cxp = tan(π/4+x/2),
crx = tan(π/4−x/2): C is an involution and
srx(Cx) = cxp(x), cxp(Cx) = srx(x), sxp(Cx) = crx(x), crx(Cx) = sxp(x).
With urx = srx − crx, uxp = cxp − sxp, Ψ_U = urx + i·uxp:
urx(Cx) = uxp(x), uxp(Cx) = urx(x), Ψ_U(Cx) = i·conj(Ψ_U(x)).

**Proof.** C(Cx) = x. srx(Cx) = cot(π/4 − x/2) = tan(π/4 + x/2) =
cxp(x) (M0: cot θ = tan(π/2−θ)); the others identically. The urx/uxp
swap follows by subtraction; Ψ_U(Cx) = uxp + i·urx = i·(urx − i·uxp)
= i·conj(Ψ_U). ∎

**Scope:** PROVED. **Depends on:** P17 (for the half-angle forms), M0.

### P57 — Transfer-angle parametrization (from Book 15, 15.IV.C1)

**Statement.** For θ ∈ (0, π), with λ = sin²(θ/2): 1 − λ = cos²(θ/2),
Ω = λ/(1−λ) = tan²(θ/2), and 2√(λ(1−λ)) = sin θ.

**Proof.** 1 − λ = cos²(θ/2) (M0); Ω = tan²(θ/2) by division.
λ(1−λ) = sin²(θ/2)cos²(θ/2) = (sin θ/2)² (M0 half-angle);
2√ = sin θ since sin θ ≥ 0 on (0,π). ∎

**Scope:** PROVED. **Depends on:** M0 only.

**Book 15 claims not folded:** primitive-difference identities —
corollaries of P17; double-angle sum/difference package — corollary of
P0+P9; phasor/differential ladder — corollary; complement parity —
M0; Weierstrass parametrization — already P19; harmonic-oscillator —
already P21; stationary points of −sin θ — M0 calculus; 11 CHECKED;
8 ASSERTED (firewalls M15-A…H are scope contracts).

Claim-by-claim table: `book15_claims.md` (status: complete).
Highest principle: **P57**.

---

## Book 16 — The Microscopic R Theory (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book16_proof.md`; rewrite page
`~/workspace/r-theory-rewrite/book16/index.html`.

**Evaluated claims summary:** 34 evaluated — **29 PROVED**, **1
CHECKED**, **3 ASSERTED**, **1 INCOMPLETE**.

### P58 — Hyperbolic Pythagorean identity (from Book 16)

**Statement.** For all real ζ: cosh²ζ − sinh²ζ = 1. Consequently,
with Σ = μ·cosh ζ, Δ = μ·sinh ζ (μ > 0): Σ² − Δ² = μ², and
Π_C := Δ/Σ = tanh ζ.

**Proof.** cosh²ζ − sinh²ζ = [(e^ζ+e^{−ζ})² − (e^ζ−e^{−ζ})²]/4
= 4e^ζe^{−ζ}/4 = 1. Then Σ² − Δ² = μ²(cosh²ζ − sinh²ζ) = μ². ∎

**Scope:** PROVED. **Depends on:** exponential definitions (M0) only.

**Book 16 claims not folded:** operator Euler e^{2xJ} — already
**P37** (Book 6); tanh double-angle — already **P50** (Book 14); 27
non-trig verified claims (extension proofs, audit); 3 ASSERTED; 1
CHECKED; 1 INCOMPLETE.

Claim-by-claim table: `book16_claims.md` (status: complete).
Highest principle: **P58**.

---

## Book 17 — The Discrete Octant (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book17_proof.md`; rewrite page
`~/workspace/r-theory-rewrite/book17/index.html`.

**Evaluated claims summary:** 39 evaluated — **21 PROVED**, **4
CHECKED**, **7 ASSERTED**, **7 INCOMPLETE**.

### P59 — Carrier ellipse 2:1 cover (from Book 17, P7)

**Statement.** For all real x, with V_R = cos(2x)/2, H = sin(2x)/4:
(V_R(x+π), H(x+π)) = (V_R(x), H(x)) (π-periodic). The eight octant
midpoints x_k = π/8 + (k−1)π/4 land on exactly four points
(±√2/4, ±√2/8), each taken twice, concyclic at radius √10/8. The
octant boundaries map to (±1/2, 0) and (0, ±1/4). Corollary:
ε(x) = sgn(sin 2x) satisfies ε(x+π) = ε(x).

**Proof.** V_R(x+π) = cos(2x+2π)/2 = V_R(x), H(x+π) = H(x) (M0
2π-periodicity). At x_k, 2x_k = π/4 + (k−1)π/2, so (cos 2x_k,
sin 2x_k) cycles through (±√2/2, ±√2/2) twice. Concyclicity:
(√2/4)² + (√2/8)² = 10/64. Boundaries by direct substitution.
Corollary: ε(x+π) = sgn(sin(2x+2π)) = ε(x). ∎

**Scope:** PROVED. **Depends on:** P9 (for V_R, H), M0. (Euclid Def.
1.15 cited as classical bookkeeping for "circle", not a premise.)

### P60 — cos 4x period and zero structure (from Book 17, P11/P12/P14)

**Statement.** For all real x: cos(4(x+π)) = cos(4x); π/2 is the
minimal positive period of cos 4x (π/4 is not: cos π = −1 ≠ cos 0).
The zeros of cos 4x are exactly the octant midpoints
x_k = π/8 + kπ/4; at octant boundaries cos 4x = ±1, never 0.

**Proof.** cos(4x+4π) = cos 4x (M0); π/2 minimal since 0 < T < π/2
would give cos(θ+4T) = cos θ with 0 < 4T < 2π, impossible.
cos(4(π/8+kπ/4)) = cos(π/2+kπ) = 0; these are all zeros in [0,2π).
At boundaries cos 4x = ±1. ∎

**Scope:** PROVED. **Depends on:** M0 only.

### P61 — Exact midpoint value srx(π/8) (from Book 17, P17)

**Statement.** srx(π/8) = √(4+2√2) + 1 + √2 (exact).

**Proof.** On octant 1, srx(x) = (1+cos x)/sin x (P0). With
cos(π/8) = √(2+√2)/2, sin(π/8) = √(2−√2)/2 (M0 half-angle):
srx(π/8) = (2+√(2+√2))/√(2−√2). Since
(√(2+√2)+√(2−√2))² = 4+2√2 and ((1+√2)√(2−√2))² = 2+√2,
(√(4+2√2)+1+√2)·√(2−√2) = 2+√(2+√2), the numerator. ∎

**Scope:** PROVED. **Depends on:** P0, M0.

**Book 17 claims not folded:** the rapidity derivative w′ = −2/sin 2x
— already **P42** (Book 7); the √2 ladder values — already **P18**
(Book 1); 17 non-trig verified claims; 4 CHECKED; 7 ASSERTED; 7
INCOMPLETE.

Claim-by-claim table: `book17_claims.md` (status: complete).
Highest principle: **P61**.

---

## Book 18 — (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book18_proof.md`.

**Evaluated claims summary:** 20 evaluated — **14 PROVED**, **5
CHECKED**, **1 ASSERTED**, **0 INCOMPLETE**. Content: combinatorics,
dimension arithmetic, representation theory, operator algebra,
audit/refutation exhibits. Validation script exit 0, 42 checks passed.

**New principles: none.** No trigonometric principle.

Claim-by-claim table: `book18_claims.md` (status: complete).
Highest principle: **P61** (unchanged).

---

## Book 19 — (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book19_proof.md`.

**Evaluated claims summary:** 26 evaluated — **9 PROVED**, **6
CHECKED**, **11 ASSERTED**, **0 INCOMPLETE** (split claims separated
into one-label rows).

**New principles: none.** The book's exact radical
|sec(5π/8)| − tan(5π/8) = √(4+2√2)+1+√2 is **P61** (Book 17's
srx(π/8)) under complement/supplementary-angle symmetry: both equal
√(4+2√2)+1+√2 by the exact evaluations, and the equality of the two
closed forms is analytic (complement identities), not merely numerical.
Not a new principle.

Claim-by-claim table: `book19_claims.md` (status: complete).
Highest principle: **P61** (unchanged).

---

## Book 20 — (evaluated 2026-09-22)

**Source:** `~/workspace/euclid_work/books/book20_proof.md`.

**Evaluated claims summary:** 28 evaluated — **17 PROVED**, **0
CHECKED**, **11 ASSERTED**, **0 INCOMPLETE**. Genuine erratum
documented: the stated Bloch-vector definitions produce two sign
reversals; the claimed vector is exact under the standard convention
r_z = |c_0|²−|c_1|², r_x + ir_y = 2c_0^*c_1 — claim PROVED conditional
on the Bloch import, with correction.

**New principles: none.** The three candidates: half-angle rational
identities — already **P19** (Book 2, Weierstrass); rapidity–velocity
e^η = √((1+β)/(1−β)) — the P43/P44 hyperbolic family (Books 10/14);
the phasor decomposition i(e^{2ix}+3e^{−2ix})/8 = sin 2x/4 + i·cos 2x/2
— an Euler-formula (P37, Book 6) corollary in book variables, adding no
new trig content. None is a new principle.

Claim-by-claim table: `book20_claims.md` (status: complete).
Highest principle: **P61** (unchanged).

---

## Book 21 — Fermion Composition, Color Closure, and Bound-State Geometry (evaluated 2026-09-26)

**Source:** rewrite page `~/workspace/r-theory-rewrite/book21/index.html`
(principal theorems). **No `book21_proof.md` exists** (the earlier campaign
covered Books 0–20 only); claims are sourced from the rewrite page, restated
and verified from the page's content.

**Boundary:** No proposition of Euclid's *Elements* is a premise of any
claim below (the page invokes none). No ledger verification was required.

**Evaluated claims summary:** 13 evaluated — **6 PROVED** (B21.1, B21.2b,
B21.3, B21.4, B21.5, B21.6; three PROVED-conditional on named asserted
imports), **2 CHECKED** (B21.7, B21.8a — cited computations, not re-run),
**5 ASSERTED** (B21.2a, B21.8b, B21.9, B21.10, B21.11), **0 INCOMPLETE**.

**New principles: none.** Every claim with trigonometric content is already
registered:

- The two-fermion invariant's R-form: R(q) = (1+q)/(1−q) is **P30**'s
  Möbius map Q₊ in the q variable; R(q)+R(q)⁻¹ = 2(1+q²)/(1−q²)
  = 2cosh λ is a two-line corollary of **P49**, so
  s = 2m₁m₂(cosh λ_m + cosh η) is exactly **P51**'s premise form. Not new.
- The bound-mass u = tan(θ/2) is **P19**'s Weierstrass form; the
  reparameterization, expansion, and limit are algebra/analysis.
- The convergence u_pair = |G/F| = sxp(x) is a half-angle tangent
  (**P19**) identified with **P17**'s sxp(x) = tan(x/2) under the asserted
  Coulomb/Dirac–Coulomb imports — conditional, not a new trig principle.

The remaining claims are Lie algebra (A₂/su(3) closure), representation
theory (triadic color closure), linear algebra (composition firewall),
empirical numbers, retained negatives, methodology, and the book's own
closure audit. Forced folding was refused.

Claim-by-claim table: `book21_claims.md` (status: complete).
Highest principle: **P61** (unchanged).

---

## Book 22 — Canonical Spin–Geometry and the Primitive Symplectic Atlas (evaluated 2026-09-26)

**Source:** rewrite page `~/workspace/r-theory-rewrite/book22/index.html`
(principal theorems). **No `book22_proof.md` exists**; claims are sourced
from the rewrite page, restated and verified from the page's content.

**Boundary:** No proposition of Euclid's *Elements* is a premise of any
claim below (the page invokes none). No ledger verification was required.

**Evaluated claims summary:** 10 evaluated — **7 PROVED** (B22.2, B22.4,
B22.5, B22.6, B22.7, B22.8, B22.9; five PROVED-conditional on named
imports/contracts), **0 CHECKED**, **3 ASSERTED** (B22.1, B22.3, B22.10),
**0 INCOMPLETE**.

**New principles: none.** The book's exact content is differential and
symplectic geometry of the radial-spinor (F,G) phase plane (Prüfer pair,
primitive symplectic atlas with common one-form p_Q dQ = −2G dF + 2F dG
and ω_spin = 4 dF∧dG) plus conditional reconstructions of imported
physics (Einstein–Hilbert defect reduction, Maxwell/Kerr/Einstein–Cartan
channels, Kerr–Newman half-angle coordinate identities). No claim yields
a new identity, lemma, or exact relation about trigonometric functions,
angles, or circular/hyperbolic measure. The Kerr half-angle identities'
explicit formula is not stated on the rewrite page, so nothing was
verifiable or foldable there (documented in `book22_claims.md`).

Claim-by-claim table: `book22_claims.md` (status: complete).
Highest principle: **P61** (unchanged).

---

## Principles register (P0–P61, sequential in book order)

Books 21–22 (evaluated 2026-09-26) added no new principles; the register
below is unchanged.

| # | Principle | Source | Scope |
|---|---|---|---|
| P0 | 4/sin(2x) = (A−1/B)+(B−1/A) | Seed (Kit) | PROVED |
| P1 | srx·sxp = 1, cxp·crx = 1 | Book 0 | PROVED |
| P2 | Positivity of srx,sxp,cxp,crx | Book 0 | PROVED |
| P3 | Reflection/quarter-turn/π-periodicity | Book 0 | PROVED |
| P4 | Local generator rational recovery | Book 0 | PROVED |
| P5 | Riccati law z′ = −(1+z²)/2 | Book 0 | PROVED |
| P6 | FlatWave identity 1/urx+1/uxp = sgn(sin2x) | Book 0 | PROVED |
| P7 | FlatWave transformation laws | Book 0 | PROVED |
| P8 | Common-sign law | Book 0 | PROVED |
| P9 | Harmonic carrier H=sin2x/4, V²+4H²=1/4 | Book 0 | PROVED |
| P10 | Transfer-circle p²+q²=2 | Book 0 | PROVED |
| P11 | Differential transfer closure | Book 0 | PROVED |
| P12 | Sharp phase-rate bounds | Book 0 | PROVED |
| P13 | Equal-and-opposite saw derivatives | Book 0 | PROVED |
| P14 | Cross-layer ratio Ω=λ/(1−λ)=… | Book 0 | PROVED |
| P15 | Reciprocal-even normalization | Book 0 | PROVED |
| P16 | Log representation cxp=e^{asinh(tan x)} | Book 0 | PROVED |
| P17 | Half-angle chart (folded factors) | Book 1 | PROVED |
| P18 | Octant-midpoint exact values (√2±1) | Book 1 | PROVED |
| P19 | Stereographic/Weierstrass parametrization | Book 2 | PROVED |
| P20 | Rational double-angle in z | Book 2 | PROVED |
| P21 | Harmonic oscillator H″+4H=0 | Book 2 | PROVED |
| P22 | Rational cot double-angle | Book 2 | PROVED |
| P23 | Logarithmic antiderivatives | Book 2 | PROVED |
| P24 | Arctan linearization | Book 2 | PROVED |
| P25 | Quarter-turn shift identities | Book 3 | PROVED |
| P26 | Quarter-turn exact order 4 | Book 3 | PROVED |
| P27 | Fold lemma (order-2 involution on 𝕋_π) | Book 3 | PROVED |
| P28 | Eighth-turn exact order 8 | Book 3 | PROVED |
| P29 | Half-angle tangent bijection 𝕋₂π→ℝ̂ | Book 3 | PROVED |
| P30 | Cophase Möbius, exact order 4 | Book 3 | PROVED |
| P31 | Octant sign law | Book 3 | PROVED |
| P32 | FlatWave sign polynomial sgn[t(1−t²)] | Book 3 | PROVED |
| P33 | Half-angle flip (quaternion lift) | Book 3 | PROVED (2026-09-26; was PROVED-cond I6) |
| P34 | Rodrigues bridge ‖r‖=tan(θ/2)=sxp(θ) | Book 3 | PROVED (2026-09-26; was PROVED-cond I6) |
| P35 | Exact 30°/60° values (Euclid 4.15) | Book 4 | PROVED |
| P36 | 60° oblique-axis cosine law | Book 4 | PROVED |
| P37 | Operator Euler formula | Book 6 | PROVED |
| P38 | CHI-orbit double-angle identities | Book 6 | PROVED |
| P39 | λ-identities (1−2λ, 4λ(1−λ)=sin2x) | Book 7 | PROVED |
| P40 | Companion cosine (principal chart) | Book 7 | PROVED (all charts 2026-09-26; corrected sign σ=sgn(cos x+sin x)) |
| P41 | cos2x/4 reciprocal-square decomposition | Book 7 | PROVED |
| P42 | Log-derivative w′=−2/sin2x | Book 7 | PROVED |
| P43 | Hyperbolic half-angle tanh(α/2) | Book 10 | PROVED |
| P44 | Mass-shell ratio chain | Book 10 | PROVED (2026-09-26; conditional only on admitted mass-shell premise) |
| P45 | Reciprocal-spine identity 1/(srx−crx) | Book 12 | PROVED |
| P46 | Native-state exact values (3,4,5) | Book 12 | PROVED |
| P47 | λ chart lemma (bijection) | Book 13 | PROVED |
| P48 | λ cofunction symmetry | Book 13 | PROVED |
| P49 | cosh/sinh in half-angle tangent | Book 14 | PROVED |
| P50 | tanh double-angle and sech | Book 14 | PROVED |
| P51 | Two-cosh sum (half-angle params) | Book 14 | PROVED-cond |
| P52 | Bound-state continuation form | Book 14 | PROVED-cond |
| P53 | Double-angle Fourier form | Book 14 | PROVED |
| P54 | Mass double-angle bridge | Book 14 | PROVED |
| P55 | Spin-1 Veronese expectations | Book 14 | PROVED |
| P56 | Complement interchange of primitives | Book 15 | PROVED |
| P57 | Transfer-angle parametrization | Book 15 | PROVED |
| P58 | Hyperbolic Pythagorean cosh²−sinh²=1 | Book 16 | PROVED |
| P59 | Carrier ellipse 2:1 cover | Book 17 | PROVED |
| P60 | cos4x period/zero structure | Book 17 | PROVED |
| P61 | Exact srx(π/8) value | Book 17 | PROVED |

**Dependency order verified:** every principle cites only earlier
principles (lower numbers), M0, definitions, or explicitly named
asserted imports. No forward references. Books 21–22 were evaluated
2026-09-26 (stop lifted by Kit's directive) and contribute no new
principles: their trigonometric content is already registered (P17, P19,
P30, P49, P51) or is non-trig; see the Book 21 and Book 22 chapters.

---

*End of cumulative trigonometric proof (deterministic rebuild,
2026-09-22; extended with Books 21–22 on 2026-09-26). Claim-by-claim
tables: book0_claims.md through book22_claims.md. Status: STATUS.md.
Reevaluation: REEVALUATION.md.*
