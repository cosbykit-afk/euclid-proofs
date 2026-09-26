# Book 12 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book12_proof.md` (claim inventory
P1–P13, A1–A13, C1–C2) and rewrite page
`~/workspace/r-theory-rewrite/book12/index.html` (*Book 12 — Mass,
Frequency, and Harmonic Calibration*, Volume II). Evaluated 2026-09-22.

**Verification method.** All 13 proofs read in full and every algebraic step
re-derived independently, by hand, with no step taken on trust:
P1 (coordinate bijection); P2 (two-body ratio); P3 (exact inversion and the
u → 0 Taylor expansion to O(u⁴), including the reduction
(m₁+m₂)²−(m₁−m₂)² = 4m₁m₂ = 4μ(m₁+m₂)); P4–P6 (transfer identities, checked
by expanding both sides and reducing the difference to the Pythagorean
identity — P5 re-verified by direct cross-multiplication rather than the
file's two-step form, same result); P7 (centering constant c = 2/5 forced by
Tr(Q) = 0, spectrum and (1/5)Tr(Q²) = 6/25 recomputed); P8 (strict
monotonicity of λ on (0, π/2), a−b = 1/5 solved with (a−b)² = 1−2ab and
(a+b)² = 49/25, all four reciprocal-spine values recomputed); P9
(2λ = N(1−λ) algebra); P10 (r²+s²−1 = 2rs ⟺ (r−s)² = 1, both sectors = 12
for 2+3, 4H = 24/25 = dim su(5)/dim End(ℂ⁵)); P11 (D(N) reduced to
N²(N²−9)/[4(N²−1)], zero iff integer N = 3; C_A = 3 = cxp, C_F = 4/3 =
(cxp−crx)/2, C_A/C_F = 9/4 = Ω² rechecked); P12 (V = cos(2x)/2 and
H = sin(2x)/4 under the D6 carrier map, dV/dx = −4H, the n_f = 3 solution
of 3n_f/(16+3n_f) = 9/25 solved uniquely); P13 (equality reduced to the
quadratic 10λ²−11λ+3 = 0 with roots {3/5, 1/2}, counterexample values
at λ = 0.7, 0.3 rechecked, signed gap = ε verified for all λ ∈ (0,1)).
The two numeric claims C1–C2 were re-run independently in Python (values
reported below). No Euclid proposition is cited as a logical premise by
the proofs; the substrate is the declared trigonometric substrate
(sin/cos on ℝ, the Pythagorean identity, the double-angle formula) plus
definitions D1–D6, consistent with the chapter's Euclid-citation boundary.
Per the proof-over-sampling rule, no numerical sampling was run on top of
any proved identity.

**Scope labels:** PROVED (exact mathematics, complete), CHECKED
(completed numeric run), ASSERTED (manuscript claim/assumption/convention),
INCOMPLETE (failed, timed out, or unfinished — none here).

## PROVED claims (13)

| Claim | Restatement | Verdict | Scope | Folded in? | Notes |
|---|---|---|---|---|---|
| P1 | M ↔ ν_M = Mc²/h invertible for M > 0 (12.II.T1) | proof verified (re-derived: multiplication by nonzero constant c²/h is a bijection of (0,∞)) | PROVED | no | coordinate relabeling; no trig content |
| P2 | (1+q_m)/(1−q_m) = m₁/m₂ (§12.III) | proof verified (re-derived) | PROVED | no | two-body algebra; no trig content |
| P3 | binding coordinate inverts exactly; B = 2μu² + O(u⁴) (§12.III) | proof verified (re-derived: exact M² inversion and the u → 0 expansion through μ) | PROVED | no | Taylor bookkeeping; no trig content |
| P4 | H = λ(1−λ) = sin(2x)/4 from λ = (1+sin x−cos x)/2 (§12.V) | proof verified (re-derived: λ(1−λ) = (1−(a−b)²)/4 = ab/2) | PROVED | **yes — Principle 26** | genuine trig identity; holds for all real x (no branch restriction) |
| P5 | Ω = λ/(1−λ) = cxp/srx on the principal branch (§12.V) | proof verified (re-derived by direct cross-multiplication; difference reduces to (b−a)(1−a²−b²) = 0) | PROVED | no — already registered as 14 (Book 0) | re-folding would duplicate a registered principle |
| P6 | λ = 1/urx with urx = srx − crx (§12.V) | proof verified (re-derived: 1/urx = a(1+a)/(1+a+b); equivalence ⟺ 2a(1+a) = (1+a)²−b² ⟺ a²+b² = 1) | PROVED | **yes — Principle 27** (the explicit reciprocal-spine computation; bare saw_r = 1/urx is already 13 (Book 0)) | all denominators nonzero on (0,π/2); urx = 1/λ ≠ 0 since λ ∈ (0,1) |
| P7 | centered projector spectrum: 3/5 (×2), −2/5 (×3), gap 1, (1/5)Tr(Q²) = 6/25 (12.VI.T1) | proof verified (re-derived: Tr(Q) = 2−5c = 0 forces c = 2/5 uniquely) | PROVED | no | spectral linear algebra on ℂ²⊕ℂ³; trig enters only via the later λ = 3/5 identification |
| P8 | λ = 3/5 selects the unique principal-branch preimage; (srx,sxp,cxp,crx) = (2,1/2,3,1/3), Ω = 3/2, H = 6/25 (§12.VI) | proof verified (re-derived: dλ/dx > 0 gives uniqueness; a−b = 1/5, a+b = 7/5 solve to (a,b) = (4/5,3/5); all four spine values recomputed) | PROVED | **yes — Principle 28** | exact (3,4,5) trig values; uniqueness on (0,π/2) uses a+b > 0 to fix the positive root |
| P9 | Tr(Q_λ) = 0 ⇒ λ = N/(N+2), Ω = N/2 on the 2+N family (12.VII.T1) | proof verified (re-derived) | PROVED | no | rational algebra in N, not about trig functions |
| P10 | H = rs/m² normalized cross-block capacity; (r−s)² = 1 ⟺ both sectors 12 for 2+3 (12.VIII.T1) | proof verified (re-derived: r²+s²−1 = 2rs ⟺ (r−s)² = 1; 4H = 24/25 = dim su(5)/dim End(ℂ⁵)) | PROVED | no | dimension counting + Principle 26's content; no new trig identity |
| P11 | Ω² − C_A/C_F = N²(N²−9)/[4(N²−1)], zero iff integer N ≥ 2 equals 3 (12.IX.T1) | proof verified (re-derived, conditional on ASSERTED A5) | PROVED | no | rational-function algebra in N; cross-invariant theorem on the carrier family, fenced from physical QCD identification |
| P12 | (a_q,a_g) = (9/25,16/25) meets the LO fixed point uniquely at n_f = 3; dV/dx = −4H (§12.XI) | proof verified (re-derived, conditional on ASSERTED import A6) | PROVED | no | conditional cross-check; derivative part is a one-step corollary of registered 9 (Book 0) |
| P13 | (1/5)Tr(Q_ε²) = |H| only at λ ∈ {1/2, 3/5}; signed gap = ε always (§10 correction) | proof verified (re-derived: equality ⟺ 10λ²−11λ+3 = 0; counterexamples at λ = 0.7, 0.3 rechecked) | PROVED | no | partly a correction: the manuscript's stated general identity is INCORRECT as stated, true at the native state (λ = 3/5) |

## ASSERTED claims (13)

| Claim | Restatement | Scope | Folded in? | Notes |
|---|---|---|---|---|
| A1 | 128/220 Hz anchors are calibrations, not kernel derivations (12.II.N1) | ASSERTED (methodological) | no | — |
| A2 | s = 2m₁m₂(cosh λ_m + cosh η) — imported SR kinematics (§12.III) | ASSERTED (import) | no | — |
| A3 | the 2+3 carrier W = ℂ²⊕ℂ³ itself — inherited, axiom-based (§12.VI) | ASSERTED (inherited stipulation) | no | all of §3.4–3.6 conditional on it |
| A4 | canonical notation bridge (λ, saw, H, Ω, FlatWave, reciprocal spine) — inherited definitions (§8) | ASSERTED (inherited definitions) | no | supplies D2 used by Principles 26–28 |
| A5 | SU(N) Casimir normalizations C_A = N, C_F = (N²−1)/(2N) — standard import (§12.IX) | ASSERTED (import) | no | used by P11 |
| A6 | LO singlet fixed point a_q^* = 3n_f/(16+3n_f) — imported QCD (§12.XI) | ASSERTED (import) | no | used by P12 |
| A7 | QCD import + projection contract (12.X.P1/PC1) — declared, not derived | ASSERTED (declared contract) | no | — |
| A8 | jet-multiplicity witness 2.29 ± 0.06 ± 0.14 — empirical input (§12.X) | ASSERTED (data) | no | witness, not derivation |
| A9 | dim Hom(ℂ^r,ℂ^s) = rs, dim End(ℂ^m) = m² — standard linear algebra (§12.VIII) | ASSERTED (standard import) | no | used by P10 |
| A10 | rational-lattice density is a methodological negative (§12.IV) | ASSERTED (methodological) | no | correctly applied against the manuscript's own near-matches |
| A11 | no mass law / no new RG traversal follow — properly fenced negatives (§12.III/12.XI/12.XII) | ASSERTED (fenced negatives) | no | negative closure |
| A12 | "selection firewall" (output, not input) — methodological claim (§12.VI) | ASSERTED (methodological) | no | sound given the forced centering, not a computation |
| A13 | empirical inputs: PDG masses, 1420.405751768 MHz, pitch anchors — data | ASSERTED (data) | no | — |

## CHECKED claims (2)

Both re-run independently in Python (this evaluation), not merely cited;
all values confirmed.

| Claim | What it checks | Scope | Folded in? |
|---|---|---|---|
| C1 | ν_H = 2.2687318183…×10²³ Hz (independent run: 2.2687318183860646e+23); ratio to the 1420.405751768 MHz hyperfine line = 1.5972420666152194e14 ≈ 10¹⁴ (12.II.N2) | CHECKED | no — numeric; no trig content |
| C2 | ρ = (m_n−m_p)/m_e = 2.5309882926374354 ≈ 2.53098829; 81/32 = 2.53125; discrepancy = −0.0002617073625645894 ≈ −2.617×10⁻⁴, nonzero far beyond parts-per-10⁷ precision (§12.IV) | CHECKED | no — numeric; the historical match cannot be promoted to a law |

## Counts

- Evaluated: **28** (13 PROVED, 2 CHECKED, 13 ASSERTED, 0 INCOMPLETE)
- Folded into the cumulative proof: **3** (P4 → Principle 26, P6 → Principle 27, P8 → Principle 28), all PROVED
- Not folded: **25** — 10 PROVED with no new trigonometric content
  (P1–P3 coordinate/two-body bookkeeping, P7–P13 spectral/rational
  algebra — P5, P6's bare saw_r = 1/urx, and P12's derivative part already
  registered as 14, 13, 9 (Book 0) respectively, register rows verified to
  exist), 2 completed numeric checks, 13 asserted imports/negatives/data
- New axioms beyond Euclid + seed + earlier books: **none** — rests on
  the inherited notation bridge (A4), the axiom-based 2+3 carrier (A3),
  standard imports (A2, A5, A9), declared physics imports/contracts
  (A6, A7), and empirical inputs (A8, A13, A1)

## Principle verification (independent)

- **Principle 26** (P4): λ(1−λ) = sin(2x)/4, λ = (1+sin x−cos x)/2 —
  **confirmed**. Proof re-derived: λ(1−λ) = (1−(a−b)²)/4 = ab/2 = sin(2x)/4.
  Domain: all real x — confirmed correct, no branch restriction needed
  (no absolute values in λ). No discrepancy with the chapter.
- **Principle 27** (P6): 1/(srx−crx) = (1+sin x−cos x)/2 —
  **confirmed**. Proof re-derived: 1/urx = a(1+a)/(1+a+b); the claim is
  equivalent, by legitimate cross-multiplication (all denominators nonzero
  on the branch), to a²+b² = 1. Domain: principal branch (0,π/2) —
  confirmed correct; urx = 1/λ with λ ∈ (0,1) is nonzero throughout.
  No discrepancy with the chapter.
- **Principle 28** (P8): λ = 3/5 on (0,π/2) ⟹ (sin x, cos x) = (4/5,3/5),
  (srx,sxp,cxp,crx) = (2,1/2,3,1/3), Ω = 3/2, H = 6/25 —
  **confirmed**. Proof re-derived including the uniqueness argument
  (dλ/dx = (cos x + sin x)/2 > 0; the linear system a−b = 1/5, a+b = 7/5
  with a,b > 0 has the single solution (4/5,3/5)). No discrepancy.

No discrepancies found with the chapter's statements, proofs, domains,
scopes, or folding decisions.

status: complete
