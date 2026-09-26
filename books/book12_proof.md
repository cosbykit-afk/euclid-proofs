# Book 12 (rewrite) — Euclid-style extension proofs

Worker: euclid-book-proofs campaign, workflow run workflow-run-b4b24c5c566d490d92bad5fa51c906c1.
Written 2026-09-22 from a direct read of `~/workspace/r-theory-rewrite/book12/index.html`
(source span volume2_full.txt lines 4811–5228), the campaign verification script
`~/workspace/r-theory-rewrite/validation/book12/verify_book12.py` (87 assertions),
and the campaign's own verification run
`book12_verify.py` (sympy exact + 2 numeric checks, exit 0, log `book12_verify.log`
in the workflow working directory).

**Name-collision notice.** This file proves the claims of the *rewrite series*
Book 12 ("Mass, Frequency, and Harmonic Calibration", Volume II). It has no
mathematical relation to Euclid's *Elements* Book XII (Eudoxan exhaustion).
Per the campaign ledger `~/workspace/euclid_work/ledger/book12_ledger.md`
(2026-09-21, full-text search of the whole rewrite corpus): R Theory extends
**none** of Euclid XII's 18 propositions — no exhaustion argument, no 10.1 axiom,
no circle/pyramid/cone/sphere ratio theory occurs anywhere in the corpus. None
of Euclid XII is cited or used below.

**No-Euclid-wholesale boundary.** Nothing here claims wholesale inheritance of
the *Elements*. The proofs below extend a synthetic-constructive stratum on the
theory's declared substrate: definitions first, dependency order, nothing used
before it is proved. Euclid's own results are cited only where an inventoried
proposition is genuinely needed (none are, in this book); the standard imported
mathematics is fenced as ASSERTED imports, not re-derived.

**Availability caveat (honest).** The task cited
`~/workspace/euclid_work/books/seed_double_angle.md` and
`book0_proof.md`–`book6_proof.md` as established material. At run time those
files do not exist (only `ledger/` and `text/` exist under `~/workspace/euclid_work/`);
no other campaign worker had written them. Therefore nothing is cited from them
and nothing was assumed from them. The dependency order below starts from
explicit definitions plus fenced imports.

**Scope labels** (Kit's standard): PROVED = exact deductive proof shown in full;
CHECKED = a completed computation with its run cited; ASSERTED = manuscript
claim, assumption, import, or methodological stipulation; INCOMPLETE = failed,
timed out, or unfinished.

---

## 1. Claim inventory

| ID | Claim (one line) | Scope |
|---|---|---|
| P1 (12.II.T1) | M ↔ ν_M = Mc²/h invertible for M > 0 | PROVED |
| P2 (§12.III) | (1+q_m)/(1−q_m) = m₁/m₂ exactly | PROVED |
| P3 (§12.III) | binding coordinate inverts exactly; B = 2μu² + O(u⁴) | PROVED |
| P4 (§12.V) | H = λ(1−λ) = sin(2x)/4 from λ = (1+sin x−cos x)/2 | PROVED |
| P5 (§12.V) | Ω = λ/(1−λ) = cxp/srx on the principal branch | PROVED |
| P6 (§12.V) | λ = 1/urx with urx = srx − crx | PROVED |
| P7 (12.VI.T1) | centered projector spectrum: 3/5 (×2), −2/5 (×3), gap 1, (1/5)Tr(Q²) = 6/25 | PROVED |
| P8 (§12.VI) | λ = 3/5 selects unique principal-branch preimage q = sxp = 1/2, (srx,sxp,cxp,crx) = (2,1/2,3,1/3) | PROVED |
| P9 (12.VII.T1) | Tr(Q_λ) = 0 ⇒ λ = N/(N+2), Ω = N/2 on 2+N family | PROVED |
| P10 (12.VIII.T1) | H = rs/m² normalized cross-block capacity; (r−s)²=1 ⟺ 12=12 | PROVED |
| P11 (12.IX.T1) | Ω² − C_A/C_F = N²(N²−9)/[4(N²−1)], zero iff N = 3 (integer N ≥ 2) | PROVED |
| P12 (§12.XI) | (a_q,a_g) = (9/25,16/25) meets LO fixed point uniquely at n_f = 3; dV/dx = −4H | PROVED |
| P13 (§10 correction) | (1/5)Tr(Q_ε²) = |H| only at λ ∈ {1/2, 3/5}; signed gap = ε always | PROVED |
| C1 (12.II.N2) | ν_H ≈ 2.2687×10²³ Hz, ~1.6×10¹⁴ above the 21-cm line | CHECKED |
| C2 (§12.IV) | ρ = (m_n−m_p)/m_e = 2.53098829 vs 81/32: discrepancy −2.617×10⁻⁴ | CHECKED |
| A1 (12.II.N1) | 128/220 Hz anchors are calibrations, not kernel derivations | ASSERTED |
| A2 (§12.III) | s = 2m₁m₂(cosh λ_m + cosh η) — imported SR kinematics | ASSERTED |
| A3 (§12.VI) | the 2+3 carrier W = ℂ²⊕ℂ³ itself — inherited, axiom-based | ASSERTED |
| A4 (§8) | canonical notation bridge (λ, saw, H, Ω, FlatWave, reciprocal spine) — inherited definitions | ASSERTED |
| A5 (§12.IX) | SU(N) Casimir normalizations C_A = N, C_F = (N²−1)/(2N) — standard import | ASSERTED |
| A6 (§12.XI) | LO singlet fixed point a_q^* = 3n_f/(16+3n_f) — imported QCD | ASSERTED |
| A7 (12.X.P1/PC1) | QCD import + projection contract — declared, not derived | ASSERTED |
| A8 (§12.X) | jet-multiplicity witness 2.29 ± 0.06 ± 0.14 — empirical input | ASSERTED |
| A9 (§12.VIII) | dim Hom(ℂ^r,ℂ^s) = rs, dim End(ℂ^m) = m² — standard linear algebra | ASSERTED |
| A10 (§12.IV) | rational-lattice density is a methodological negative — ASSERTED |
| A11 (§12.III/12.XI/12.XII) | no mass law / no new RG traversal follow — properly fenced negatives | ASSERTED |
| A12 (§12.VI) | "selection firewall" (output, not input) — methodological claim | ASSERTED |
| A13 | empirical inputs: PDG masses, 1420.405751768 MHz, pitch anchors — data | ASSERTED |

Counts: PROVED 13, CHECKED 2, ASSERTED 13, INCOMPLETE 0. No timeouts, no failures.

---

## 2. Definitions (used before anything else)

**D1 (principal branch).** Work on x ∈ (0, π/2), so sin x > 0, cos x > 0;
the absolute values in the bridge below drop out there.

**D2 (canonical notation bridge — inherited, A4).** On the principal branch:
srx = |csc x| + cot x = (1+cos x)/sin x; sxp = 1/srx;
cxp = |sec x| + tan x = (1+sin x)/cos x; crx = 1/cxp;
urx = srx − crx; uxp = cxp − sxp;
λ = saw_r = (1 + sin x − cos x)/2; Ω = λ/(1−λ);
H = sin(2x)/4; V = cos(2x)/2; ε = FlatWave = sgn(sin 2x).

**D3 (mass-frequency coordinate).** For supplied invariant mass M > 0,
ν_M = Mc²/h.

**D4 (two-body coordinates).** For m₁, m₂ > 0: λ_m = ln(m₁/m₂),
q_m = (m₁−m₂)/(m₁+m₂); η the relative rapidity, q_v = tanh(η/2);
μ = m₁m₂/(m₁+m₂); M the total invariant mass of the pair;
u² = [(m₁+m₂)² − M²]/[M² − (m₁−m₂)²]; B = (m₁+m₂) − M.

**D5 (centered projector).** On W = ℂ²⊕ℂ³ (A3) with orthogonal block
projectors P₂, P₃: Q = P₂ − cI. For λ ∈ (0,1) on W_N = ℂ²⊕ℂ^N:
Q_λ = λP₂ − (1−λ)P_N; Q_ε = ε[λP₂ − (1−λ)P₃].

**D6 (carrier map, §12.XI).** Positive square-root carrier:
cos x = √a_q, sin x = √a_g (adapted coordinate, declared).

---

## 3. Proofs in dependency order

### 3.1 The coordinate relabeling (P1)

**P1 — PROVED (12.II.T1).** By D3, ν_M = Mc²/h with constants c, h nonzero,
M > 0. The map M ↦ ν_M is multiplication by the nonzero constant c²/h, hence
a bijection of (0, ∞) onto itself, inverse M = hν_M/c². Rest-energy frequency
carries exactly the information in mass. ∎

### 3.2 Two-body bookkeeping (P2, P3, A2)

**P2 — PROVED.** From D4,
(1+q_m)/(1−q_m) = ((m₁+m₂)+(m₁−m₂))/((m₁+m₂)−(m₁−m₂)) = 2m₁/2m₂ = m₁/m₂. ∎

**P3 — PROVED.** From D4, solve for M²:
u²[M² − (m₁−m₂)²] = (m₁+m₂)² − M²
⇒ M²(u²+1) = (m₁+m₂)² + u²(m₁−m₂)²
⇒ M² = [(m₁+m₂)² + u²(m₁−m₂)²]/(1+u²),
an exact inversion. For weak binding u → 0:
M² = (m₁+m₂)²[1 + u²((m₁−m₂)²/(m₁+m₂)² − 1)] + O(u⁴)
    = (m₁+m₂)²[1 − u²·4m₁m₂/(m₁+m₂)²] + O(u⁴)
    = (m₁+m₂)²[1 − 4μu²/(m₁+m₂)] + O(u⁴).
Hence M = (m₁+m₂)[1 − 2μu²/(m₁+m₂)] + O(u⁴) and
B = (m₁+m₂) − M = 2μu² + O(u⁴). ∎

**A2 — ASSERTED.** The invariant s = 2m₁m₂(cosh λ_m + cosh η) is imported
special-relativistic kinematics, properly fenced in the manuscript as an import;
it is not derived here. (The campaign verification grid confirmed the
s/(4m₁m₂) form to 4.5×10⁻¹⁶, but since no proof is given here it stays ASSERTED.)

**A11 (part) — ASSERTED.** "These are exact relational coordinates; they do
not determine the observed masses" — a properly fenced negative; a coordinate
cannot select a mass, so no mass law follows from P1–P3.

### 3.3 Transfer identities (P4, P5, P6)

**P4 — PROVED.** From D2, with a = sin x, b = cos x:
λ(1−λ) = ((1+a−b)(1−a+b))/4 = (1 − (a−b)²)/4 = (1 − (1 − 2ab))/4 = ab/2 = sin(2x)/4 = H. ∎

**P5 — PROVED.** On the principal branch a² + b² = 1, a, b > 0.
λ/(1−λ) = (1+a−b)/(1−a+b); cxp/srx = ((1+a)/b)·(a/(1+b)) = a(1+a)/(b(1+b)).
Since (1−a+b)(1+a) = b(1+a+b) (using 1−a² = b²):
(1+a−b)/(1−a+b) = (1+a−b)(1+a)/(b(1+a+b)).
And (1+a−b)(1+b) = 1+a+ab−b² while a(1+a+b) = a+a²+ab; these agree since
1−b² = a². Hence (1+a−b)(1+a)/(b(1+a+b)) = a(1+a)/(b(1+b)) = cxp/srx. ∎

**P6 — PROVED.** urx = srx − crx = (1+b)/a − b/(1+a) = ((1+b)(1+a) − ab)/(a(1+a))
= (1+a+b)/(a(1+a)). So 1/urx = a(1+a)/(1+a+b). Meanwhile
λ = (1+a−b)/2, and (1+a−b)/2 = a(1+a)/(1+a+b) ⟺ 2a(1+a) = (1+a−b)(1+a+b)
= (1+a)² − b² = 1+2a+a²−b², which holds since 1 − a² − b² = 0. ∎

### 3.4 The centered projector (P7, P8)

**P7 — PROVED (12.VI.T1).** By D5, Q = P₂ − cI = (1−c)P₂ − cP₃.
Tr(Q) = 2(1−c) − 3c = 2 − 5c; Tr(Q) = 0 forces c = 2/5 uniquely — the centering
constant is derived, not fitted. Thus Q = (3/5)P₂ − (2/5)P₃, diagonal in the
block decomposition (A3): eigenvalue 3/5 with multiplicity 2 on ℂ²,
eigenvalue −2/5 with multiplicity 3 on ℂ³. Spectral gap
3/5 − (−2/5) = 1. Tr(Q²) = 2·9/25 + 3·4/25 = 30/25 = 6/5, so
(1/5)Tr(Q²) = 6/25. The positive eigenvalue 3/5 selects λ = 3/5 in the
transfer coordinate (identification via the bridge D2). ∎

**P8 — PROVED.** λ = (1+a−b)/2 on the principal branch has
dλ/dx = (cos x + sin x)/2 > 0: continuous and strictly increasing,
λ(0⁺) = 0, λ(π/2⁻) = 1, hence a unique preimage of λ = 3/5.
That preimage satisfies a − b = 1/5; squaring, 2ab = 24/25, and with
(a+b)² = 1 + 2ab = 49/25, a+b = 7/5. Then a = (7/5+1/5)/2 = 4/5,
b = (7/5−1/5)/2 = 3/5. So srx = (1+b)/a = (8/5)/(4/5) = 2, sxp = 1/2,
cxp = (1+a)/b = (9/5)/(3/5) = 3, crx = 1/3, Ω = cxp/srx = 3/2,
H = λ(1−λ) = 6/25. ∎

**A12 — ASSERTED.** The "selection firewall" — W → projector → λ → q, the
distinguished state an output of the block geometry — is a methodological claim
about logical direction, sound given the forced centering but not a computation.

### 3.5 The 2+N family (P9, P10, P11)

**P9 — PROVED (12.VII.T1).** On W_N = ℂ²⊕ℂ^N,
Tr(Q_λ) = 2λ − N(1−λ). Setting to zero: 2λ = N(1−λ) ⇒ λ(N+2) = N
⇒ λ = N/(N+2), and Ω = λ/(1−λ) = [N/(N+2)]/[2/(N+2)] = N/2. For N = 3 this
reproduces λ = 3/5, Ω = 3/2, an independent consistency check of P7–P8. ∎

**P10 — PROVED (12.VIII.T1).** For an r+s split, m = r+s, λ = s/m:
H = λ(1−λ) = rs/m² by P4's algebra. By the standard facts A9,
dim_ℂ Hom(ℂ^r,ℂ^s) = rs and dim_ℂ End(ℂ^m) = m², so H is the normalized
complex dimension of one directed cross-block operator sector; the full
off-diagonal sector has normalized size 2H. The block-preserving traceless
sector has dimension r²+s²−1; r²+s²−1 = 2rs ⟺ r²−2rs+s² = 1
⟺ (r−s)² = 1. For 2+3: (2−3)² = 1, so both sectors have dimension 12;
H = 6/25, 2H = 12/25, 4H = 24/25 = dim su(5)/dim End(ℂ⁵) = 24/25. ∎

**P11 — PROVED (12.IX.T1).** Import the standard SU(N) normalizations A5:
C_A = N, C_F = (N²−1)/(2N), so C_A/C_F = 2N²/(N²−1). By P9, Ω² = N²/4.
Their difference:
D(N) = N²/4 − 2N²/(N²−1) = [N²(N²−1) − 8N²]/[4(N²−1)] = N²(N²−9)/[4(N²−1)].
For integer N ≥ 2 the denominator is nonzero, so D(N) = 0 ⟺ N²(N²−9) = 0
⟺ N² = 9 ⟺ N = 3. At N = 3: C_A = 3 = cxp (native, P8),
C_F = 8/6 = 4/3 = (cxp − crx)/2, and C_A/C_F = 9/4 = Ω². This is an exact
cross-invariant theorem on the mathematical carrier family; it does not by
itself identify the N = 3 block with physical QCD color (fenced negative). ∎

### 3.6 QCD cross-check (P12, A5–A8)

**P12 — PROVED (conditional on import A6).** Under the declared carrier map D6,
V = a_q − 1/2 = cos²x − 1/2 = cos(2x)/2 (D2) ✓, and
H = (1/2)√(a_q a_g) = (1/2)sin x cos x = sin(2x)/4 (D2) ✓ — consistent with
the Volume I carrier. Also dV/dx = −sin(2x) = −4H ✓.
At the native state (P8), (cos x, sin x) = (3/5, 4/5), so
(a_q, a_g) = (9/25, 16/25). Under the imported LO partition
a_q^* = 3n_f/(16+3n_f) (A6): 3n_f/(16+3n_f) = 9/25 ⟺ 75n_f = 144+27n_f
⟺ 48n_f = 144 ⟺ n_f = 3, uniquely. This coincidence is a conditional
cross-check, not a derivation of n_f, QCD, or DGLAP evolution. ∎

**A5, A6, A7, A8 — ASSERTED.** Standard imported theorems (SU(N) Casimirs,
LO DGLAP fixed-point formula) and declared contracts/imports (12.X.P1,
12.X.PC1); the jet-multiplicity agreement 2.29 ± 0.06 ± 0.14 vs 9/4 is an
empirical witness (ordinary QCD predicts the same value, so Δ_op = ∅).

### 3.7 The §10 correction (P13)

**P13 — PROVED.** With D5, ε² = 1:
Tr(Q_ε²) = 2λ² + 3(1−λ)², so (1/5)Tr(Q_ε²) = (2λ²+3(1−λ)²)/5,
whereas |H| = λ(1−λ) on (0,1). Equality ⟺ 2λ²+3(1−λ)² = 5λ(1−λ)
⟺ 10λ² − 11λ + 3 = 0 ⟺ λ = (11±1)/20 ∈ {3/5, 1/2}.
Counterexamples at λ = 0.7, 0.3, 0.9 (0.25 ≠ 0.21; 0.33 ≠ 0.21; 0.33 ≠ 0.09).
The manuscript's stated general identity is INCORRECT as stated; it is TRUE at
the native state (λ = 3/5: both sides 6/25), which is the context the
surrounding paragraph concerns. The adjacent claim — signed spectral gap = ε —
is exact for all λ ∈ (0,1): eigenvalues ελ and −ε(1−λ) differ by ε. ∎

### 3.8 Numeric claims (C1, C2)

**C1 — CHECKED (12.II.N2).** Completed run (this worker, `book12_verify.py`):
with m_p = 1.67262192595×10⁻²⁷ kg, c = 299792458 m/s, h = 6.62607015×10⁻³⁴ J·s,
ν_H = m_p c²/h ≈ 2.2687×10²³ Hz; against the 1420.405751768 MHz hyperfine
transition: ratio 1.5972×10¹⁴ ≈ 10¹⁴ — fourteen orders of magnitude below
hydrogen's rest-energy frequency, as the page states. Different observables. ✓

**C2 — CHECKED (§12.IV).** Completed run (this worker, PDG masses
m_e = 0.51099895, m_p = 938.27208816, m_n = 939.56542052 MeV):
ρ = (m_n−m_p)/m_e = 2.53098829; 81/32 = 2.53125; discrepancy −2.617×10⁻⁴,
relative 1.0×10⁻⁴, nonzero far beyond the parts-per-10⁷ experimental
precision. The historical match is close and not exact; it cannot be promoted
to a law. ✓

**A10 — ASSERTED.** The lattice-density argument (dense rational families
produce near-misses with hindsight) is a methodological assertion, correctly
applied against the manuscript's own historical matches.

**A11 (rest) — ASSERTED.** Negative Theorem 12.XII.N1 (projection phase is not
affine RG time): the premise — q = sxp strictly monotone on the principal
branch, hence no interior stationary point, while the imported singlet flow
has a genuine fixed point with H^* = 6/25 ≠ 0 — follows from D2; the negative
conclusion is properly fenced. "Projection does not derive DGLAP evolution"
and "no Projection-specific mass spectrum has been obtained" are honest
negative closures.

**A13 — ASSERTED.** PDG masses, 1420.405751768 MHz, the 128/220 Hz pitch
anchors: empirical/historical inputs used for negative results and witnesses,
never as derivations.

---

## 4. New axioms / assumptions beyond Euclid + seed + earlier books

None of the proof work above introduces a genuinely new axiom. What it rests
on, declared explicitly:

1. **Inherited Volume I notation bridge (A4)** — λ, saw_r/saw_x, H, V, Ω,
   FlatWave, the reciprocal spine (srx, sxp, cxp, crx, urx, uxp): taken as
   given definitions. Note the campaign audit's caveat: the Volume I ledger
   flags the word "certified" on the transfer coordinate as a
   dependency-labeling defect; the underlying algebra (proved here in §3.3)
   is correct.
2. **Axiom Zero and the 2+3 Hermitian carrier (A3)** — W = ℂ²⊕ℂ³ is inherited
   as an axiom-based stipulation; the ledger records the specific block
   decomposition as not independently verified. All of §3.4–3.6 is conditional
   on it.
3. **Standard mathematical imports (A2, A5, A9)** — SR two-particle invariant,
   SU(N) Casimir normalizations, Hom/End dimension counts: ordinary background
   mathematics, fenced as imported, not re-derived.
4. **Declared physics imports and contracts (A6, A7)** — LO DGLAP singlet
   fixed-point formula, 12.X.P1 (QCD SU(3)), 12.X.PC1 (ℂ³ block ↔ color
   fundamental *for this comparison*): assumptions by declaration; P12 is a
   conditional cross-check only.
5. **Empirical/historical inputs (A13, A8, A1)** — PDG masses, 21-cm line,
   pitch anchors, jet-multiplicity data: used as fenced inputs for negative
   results and witnesses.
6. **Not assumed and not needed:** no exhaustion/limit machinery (Euclid XII),
   no 10.1 axiom, no statistical or thermodynamic content (per the Book 12 →
   Book 13 dependency lock: probability, entropy, thermodynamic time,
   irreversibility, microscopic multiplicity, seam dynamics do not follow
   from these identities).

**Dependency verdict for Book 13 inheritance** (from the book's own lock,
§13): Book 13 may take λ, 1−λ, H, Ω, FlatWave, reciprocal access, and the
centered-projector spectral interpretation (P4–P11, conditional on 1–2 above);
everything else listed in the lock stays fenced.

---

## 5. Notes

- The campaign seed (`seed_double_angle.md`) and earlier book proofs
  (`book0_proof.md`–`book6_proof.md`) did not exist at run time, so nothing
  above cites them; the chain starts from definitions D1–D6 plus the fenced
  imports. If those files appear later, the only honest reconciliation needed
  is against the notation bridge D2.
- The book's page reports 87 real assertions in
  `~/workspace/r-theory-rewrite/validation/book12/verify_book12.py`; this
  worker did not re-run that script (its results are the rewrite pipeline's,
  read at face value only) and instead proved the identities analytically and
  re-ran the two numeric claims from scratch. Per the standing rule, the
  analytic proofs above establish the results; no post-proof sampling was run.
- One formula on the page is incorrect as stated in full generality (P13);
  true at the native state the paragraph concerns. Two upstream labels are
  overstated per the §9 audit ("certified" transfer map labeling defect; the
  2+3 carrier "independently earned"). Imports, contracts, witnesses, and
  negatives are properly fenced throughout — the book's own closure stands:
  Δ_op(Book 12) = ∅; a strong representation and spectral bridge, not a
  harmonic theory of particle masses.
- Verification run for this file: `book12_verify.py`, exit 0, log
  `book12_verify.log` (sympy exact simplifications-to-zero + 2 completed
  numeric checks), in the workflow working directory.
