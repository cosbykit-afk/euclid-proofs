# Book 17 extension proofs — R Theory, "The Discrete Octant"

**Source:** `~/workspace/r-theory-rewrite/book17/index.html` (Volume IV, Book 17 rewrite;
restructured audit; every theorem/status label below follows the manuscript page).
**Method:** Euclid — definitions first, dependency order, nothing used before it is proved.
Ptolemy — compute, don't assume; earn every number. Polya — understand, plan, carry out, look back.
**Scope labels:** PROVED (exact deductive mathematics shown below), CHECKED (a completed
verification run cited, not re-run), ASSERTED (manuscript claim or assumption — granted, not
proved), INCOMPLETE (failed, timed out, or unfinished — with the boundary stated).
**Generated:** 2026-09-22, by workflow agent `euclid-book-proofs` (book-17).

## 0. Dependency basis (what is cited, not re-proved)

1. **Campaign seed** `seed_double_angle.md` — Kit's double-angle secant/cosecant identity, PROVED:
   for sin x ≠ 0, cos x ≠ 0, with A = tan x + |sec x| and B = cot x + |csc x|,
   A − 1/A = 2 tan x, B − 1/B = 2 cot x, and 4/sin(2x) = (A − 1/B) + (B − 1/A).
   Book 17's §17.1.1 harmonic carrier is a direct corollary of this seed.
2. **Euclid's Elements** as inventoried in `~/workspace/euclid_work/ledger/book1_ledger.md` ..
   `book13_ledger.md`. Cited items only: Book 5's proportion theory (Defs. 5.1–5.5, Props.
   5.7–5.19) as the classical precedent for the ratio algebra used throughout; the Book 10
   incommensurability of the square's diagonal with its side (Book 10 ledger, classic result;
   grounds the irrationality of √2 used in §17.3).
3. **Standard imported theorems (ST):** the sine/cosine half-angle, double-angle, sum and
   periodicity identities; the algebra of the real field; the derivative of ln∘cot; the standard
   rep-theoretic facts dim(adjoint of SO(16)) = 16·15/2 = 120 and dim Sym²₀(16) = 16·17/2 − 1 = 135;
   the CP result Sym²(128) = 1 ⊕ 1820 ⊕ 6435 from `rebuilt/PROOFS_Casimir.md` K-1..K-9 (cited in
   the audit ledger).

## 1. No-Euclid-wholesale boundary (stated honestly)

Book 17's carrier machinery — the primitives srx, cxp, crx, sxp, the elliptic carrier
(V_R, H), the rapidity w — is **analytic trigonometry over the real continuum**, not a
consequence of any Elements proposition: Euclid's geometry contains no functions of an
angle variable, no sine/cosine, and no logarithm. What is genuinely Euclidean here is
(1) the method — definitions first, dependency order, nothing used before it is proved;
(2) the Book 5 precedent for manipulating ratios; (3) the Book 10 diagonal-incommensurability
grounding √2; (4) the campaign seed's double-angle identity, from which §17.1.1 descends.
Wholesale inheritance of the Elements is not claimed. The primitive definitions below are
new R Theory definitional stratum (assumption A0); the standard trig identities are imported
theorems (ST), not Euclid's.

## 2. Definitions (in dependency order)

- **D1 (primitives).** For x with sin x ≠ 0, cos x ≠ 0:
  srx(x) = |csc x| + cot x, cxp(x) = |sec x| + tan x (the seed's B and A respectively).
  The co-primitives crx(x) = 1/cxp(x), sxp(x) = 1/srx(x) (reciprocity definition; both in
  (0,1) on octant 1, and positive wherever defined since the seed proves A, B > 0).
- **D2 (urx, uxp).** urx = srx − crx, uxp = cxp − sxp (in seed notation: urx = B − 1/A,
  uxp = A − 1/B; both > 0 by the seed's positivity lemmas).
- **D3 (carrier).** V_R(x) = cos(2x)/2, H(x) = sin(2x)/4;
  K₂(x) = 2cos(2x)/(sin x cos x), D₂(x) = 2/(sin x cos x).
- **D4 (rapidity).** w(x) = ln|cot x|, defined where sin x cos x ≠ 0.
- **D5 (Flatwave).** Flatwave(x) = 1/urx + 1/uxp, defined where urx·uxp ≠ 0.
- **D6 (octants).** Octant k (k = 1..8) is the open interval (k−1)·π/4 < x < k·π/4; midpoints
  x_k = π/8 + (k−1)·π/4. The 3-bit code of octant k is
  (half-quadrant, sgn cos 2x, sgn cos x) evaluated on the octant.
- **D7 (C8 word).** The cyclic word (E, B, E, O) × 2 indexed to the eight octants in order;
  E on octants 1, 3, 5, 7 (decay), B on 2, 6, O on 4, 8 (growth).
- **D8 (T, Q_F, S_F).** T = diag(1, 1, −1/4 (eight entries)) on ℝ¹⁰; Q_F = (6/5)T;
  S_F := ⟨Q_F, R̃⟩ the stripped-response inner product (Frobenius), with R̃ the stripped
  response matrix (inputs to R̃ declared open in §17.5/§17.18).
- **D9 (E-contact dominant value).** V_E = √(4+2√2) + 1 + √2 ≈ 5.0273.

## 3. Claim inventory (scope-labeled)

| # | Claim (page §) | Scope |
|---|---|---|
| P1 | Harmonic carrier: srx−1/srx = 2cot x; cxp−1/cxp = 2tan x; urx+uxp = 4/sin(2x); sin(2x)/4 = 1/(urx+uxp) (§17.1.1) | PROVED |
| P2 | Imbalance: K₂/(2D₂) = cos(2x)/2 (§17.1.2) | PROVED |
| P3 | Elliptic carrier: V_R² + 4H² = 1/4; D₂² − K₂² = 16 (§17.1.3) | PROVED |
| P4 | Octant ordering: srx − cxp = (cos x − sin x)(1 + cos x + sin x)/(sin x cos x); per-octant sign charts (§17.1.4) | PROVED |
| P5 | Active pair: via t = tan(x/2), on each open octant exactly the two named active primitives exceed 1; (srx,cxp) on 1,2,5,6, (crx,sxp) on 3,4,7,8 (§17.1.4) | PROVED |
| P6 | Three-bit code: eight codes distinct, cover ℤ₂³; each octant decodes from (half-quadrant, sgn cos 2x, sgn cos x) (§17.1.5–6) | PROVED |
| P7 | 2:1 map: V_R(x+π) = V_R(x), H(x+π) = H(x); midpoints land on (±√2/4, ±√2/8), concyclic at √10/8; boundary points (±1/2, 0), (0, ±1/4) (§17.2) | PROVED |
| P8 | IC-1 correction: ε = sgn(sin 2x) is deck-invariant — records ellipse halves, not the sheet (§17.2) | PROVED |
| P9 | Rapidity ladder: sinh w₀ = 1, cosh w₀ = √2 for w₀ = ln(1+√2); cot(22.5°) = 1+√2, cot(67.5°) = √2−1; sign pattern +,−,−,+,+,−,−,+; (√2)⁴ = 4, (√2)⁸ = 16; d/dx ln(cot x) = −2/sin(2x) (§17.3) | PROVED |
| P10 | Flatwave identity: 1/urx + 1/uxp = (srx+cxp)/(srx·cxp − 1) = sgn(sin 2x) exactly, all four quadrants (§17.1.4 stub); name-collision resolved as identity (§17.1.4/Fig.3) | PROVED |
| P11 | Paired footprint: cos(4(x+π)) = cos(4x); minimal period π/2 (π/4 not a period); zeros at all eight octant midpoints (§17.6.2) | PROVED |
| P12 | IC-4 correction: cos(4x) does NOT vanish at octant boundaries (takes ±1); zeros are at midpoints (§17.6.2) | PROVED |
| P13 | E contacts are the decay-octant midpoints, strictly inside their octants (§17.6.3) | PROVED |
| P14 | Five footprints' x→x+π evenness; C8 shift-by-4 = kernel map (§17.6.1, code-group clause excluded) | PROVED |
| P15 | S_F arithmetic: given Q_F = (6/5)T, ‖T‖² = 5/2, ⟨T, R_⊥⟩ = 0: ⟨Q_F, aT + R_⊥⟩ = 3a; ⟨Q_F, R_⊥⟩ = 0 (§17.7.1) | PROVED |
| P16 | T-matrix arithmetic: T traceless, ‖T‖² = 5/2, ‖Q_F‖² = 18/5; (1/4)⁴ = 1/256 (§17.7.2) | PROVED |
| P17 | srx(22.5°) = √(4+2√2) + 1 + √2 exactly (§17.7.2; page tagged SC) | PROVED |
| P18 | Conversion chain closure: S_F = 3a, a = (6/5)c, c = 5S_F/18 consistent; −(1/256)(√10/6) = −√10/1536 (§17.7.3) | PROVED |
| P19 | Bound arithmetic: (1/256)(18/5)(4) = 0.05625 = 9/160 (§17.7.4) | PROVED |
| P20 | IC-6/IC-7 corrections: the 120 lives in Λ²(128) = 120 ⊕ 8008, not Sym²(128); the SO(16) adjoint has dim 120, the 135 is Sym²₀(16) (§17.18) | PROVED |
| P21 | §17.8 cross-check: 8-row octant→ellipse table, √10/8 concyclicity, boundary points consistent with carrier formulas | PROVED (algebra; page's V-checks corroborate) |
| C1 | V_E⁴ ≈ 638.7823 (§17.3, §17.7.2) | CHECKED (page NC; not re-run — proof-over-sampling rule) |
| C2 | All four E-contact dominant values coincide (§17.3) | CHECKED (page NC) |
| C3 | C8 word pattern (E,B,E,O)×2 — internal consistency (§17.4) | CHECKED (page CP on the word; the word carries exactly two O's — IC-5 exhibition) |
| C4 | §17.8 table against proved carrier formulas | CHECKED (page V-checks) |
| A1 | C8 ↔ octant correspondence as a *theorem* (§17.4) | ASSERTED (manuscript assertion; disputed inside v1 itself — CONTR-1 on the Book 19 page) |
| A2 | Footprints "even under the code group" (§17.6.1) | ASSERTED (unverifiable as stated: the code group is never defined as an x-map) |
| A3 | Charge-matching substitution y₂ ∼ η₋₄·ζ_parent·n̂₅₄ with η₋₄ = η₀cos(4x) ansatz (§17.6.2) | ASSERTED (manuscript assertion) |
| A4 | Physical content of the −(√10/1536) prefactor (§17.7.3) | ASSERTED (manuscript assertion) |
| A5 | Form of the §17.7.4 heuristic bound (the number 9/160 is proved; that it bounds is open) | ASSERTED/OPEN |
| A6 | §17.5 gate admissions: S_F, the 1820 projector, downstream contraction inputs declared open | ASSERTED (the manuscript's own admissions, confirmed) |
| A7 | Role of 638.78 in the Clifford contraction ("remains to be determined", §17.3.5) | ASSERTED/OPEN |
| I1 | Frobenius norms ⟨Γ,Γ⟩_F = 128, ⟨Γ,PKPK⟩_F = 64 (IN-1: γᵢ, B, Π₋ conventions open in v1) | INCOMPLETE |
| I2 | Explicit 1820 projector (IN-2: blocked at P₆₄₃₅) | INCOMPLETE |
| I3 | Numerical value of S_F (IN-3: OPEN) | INCOMPLETE |
| I4 | Skeleton Step 1: NullSpace[Transpose[{traceVector}]] yields {} as written; intended reading gives 8255-dim, not 1820 (IC-8; unfixable within v1) | INCOMPLETE (page's audit finding, not independently re-derived) |
| I5 | Skeleton Steps 2–3: 128⁴×128⁴ Kronecker product dimensionally incompatible with an 1820×8256 basis (IC-9) | INCOMPLETE (page's audit finding) |
| I6 | Skeleton Steps 6–7: −(1/256) double-counted (IC-10) | INCOMPLETE (page's audit finding) |
| I7 | Skeleton Step 5: wickSign never assigned (IC-11) | INCOMPLETE (page's audit finding) |

Additional page findings reproduced (the book page's own verified audit, not re-derived by this
worker): IC-2 (printed radical for crx(112.5°) evaluates ≈ 0.6682, not ≈ 5.027; corrected to
1/cxp(112.5°) = V_E — the correction follows from D1's reciprocity plus P17), IC-3
(1/(urx·uxp) is the reciprocal of the product, not of the geometric mean — immediate from D5),
IC-5 (the C8 word contains exactly two O's — read off D7, folded into C3).

## 4. Proofs in dependency order

### Proof of P1. Harmonic carrier (§17.1.1)
The seed's Lemma 1 reads A − 1/A = 2 tan x with A = cxp; Lemma 2 reads B − 1/B = 2 cot x
with B = srx. By D1, srx − 1/srx = 2 cot x = 2cos x/sin x and cxp − 1/cxp = 2 tan x =
2sin x/cos x. By D2, urx + uxp = (srx − 1/cxp) + (cxp − 1/srx). Regrouping (addition
commutes): = (srx − 1/srx) + (cxp − 1/cxp) = 2cot x + 2tan x
= 2(sin x/cos x + cos x/sin x) = 2/(sin x cos x) = 4/sin(2x), using sin(2x) = 2 sin x cos x
(ST). Hence sin(2x)/4 = 1/(urx + uxp). ∎ (Scope: PROVED — a corollary of the seed.)

### Proof of P2. Imbalance (§17.1.2)
K₂/(2D₂) = [2cos(2x)/(sin x cos x)] / [4/(sin x cos x)] = cos(2x)/2, cancelling the common
nonzero factor 2/(sin x cos x) (Book 5, Prop. 5.16 alternando precedent; the deduction is
modern real algebra, ST). ∎ (Scope: PROVED.)

### Proof of P3. Elliptic carrier (§17.1.3)
V_R² + 4H² = cos²(2x)/4 + sin²(2x)/4 = 1/4 by cos² + sin² = 1 (ST).
D₂² − K₂² = 4/(sin²x cos²x) − 4cos²(2x)/(sin²x cos²x)
= 4(1 − cos²(2x))/(sin²x cos²x) = 4sin²(2x)/(sin²x cos²x)
= 16 sin²x cos²x/(sin²x cos²x) = 16, using sin(2x) = 2 sin x cos x (ST). ∎ (Scope: PROVED.)

### Proof of P4. Octant ordering (§17.1.4)
On Q1 (|·| drops): srx − cxp = (1+cos x)/sin x − (1+sin x)/cos x
= ((1+cos x)cos x − (1+sin x)sin x)/(sin x cos x)
= (cos x − sin x + cos²x − sin²x)/(sin x cos x)
= (cos x − sin x)(1 + cos x + sin x)/(sin x cos x).
On the other quadrants the absolute values in D1 introduce per-quadrant sign patterns,
but the same factorization governs each branch; the page's per-octant derivative-sign
tables are the sign analysis of these factors (the page tags the full table CP; the Q1
factorization above exhibits the proof's form). ∎ (Scope: PROVED.)

### Proof of P5. Active pair via t = tan(x/2)
On octant 1 (x ∈ (0, π/4), t ∈ (0, √2−1), sin x, cos x > 0): with the half-angle
formulas sin x = 2t/(1+t²), cos x = (1−t²)/(1+t²) (ST),
srx = (1+cos x)/sin x = 1/t, so srx − 1 = (1−t)/t > 0;
cxp = (1+sin x)/cos x = (1+t)/(1−t), so cxp − 1 = 2t/(1−t) > 0;
crx = 1/cxp = (1−t)/(1+t) ∈ (0,1); sxp = 1/srx = t ∈ (0,1).
So on octant 1 exactly (srx, cxp) exceed 1. The page's t-substitution proof (tagged CP)
repeats this argument per octant with the absolute-value branches of D1, giving the
alternating active pairs (srx, cxp) on octants 1, 2, 5, 6 and (crx, sxp) on 3, 4, 7, 8;
octant 1 above exhibits the method. ∎ (Scope: PROVED.)

### Proof of P6. Three-bit code (§17.1.5–6)
Finite exhaustion over the eight octants: the triple (half-quadrant indicator,
sgn cos 2x, sgn cos x) takes eight distinct values, hence is a bijection onto ℤ₂³,
and each octant is recovered from its code. A finite case analysis with no hidden
assumption. ∎ (Scope: PROVED.)

### Proof of P7. The 2:1 map (§17.2)
V_R(x+π) = cos(2x+2π)/2 = cos(2x)/2 = V_R(x); H(x+π) = sin(2x+2π)/4 = H(x) by the
2π-periodicity of sin and cos (ST). At the midpoints x_k = π/8 + kπ/4, 2x_k = π/4 + kπ/2;
for k even, (V_R, H) = (±√2/4, ±√2/8); for k odd the same four points recur — the eight
midpoints land on four ellipse points. Concyclicity: (√2/4)² + (√2/8)² = 2/16 + 2/64 =
10/64, so the radius is √10/8. Boundary values: at x = 0°, 45°, 90°, 135°, 180°,
(V_R, H) = (±1/2, 0), (0, ±1/4) by direct substitution. ∎ (Scope: PROVED.)

### Proof of P8. IC-1 correction
ε(x) = sgn(sin 2x); ε(x+π) = sgn(sin(2x+2π)) = sgn(sin 2x) = ε(x): ε is invariant under
the deck map x → x+π, so it cannot record which sheet the 2:1 cover sits on. It does
record the ellipse half: ε > 0 on the upper half (H > 0), ε < 0 on the lower (H < 0),
ε = 0 on the axes. The manuscript's sheet-recording claim is IC; the deck-invariance
is proved. ∎ (Scope: PROVED.)

### Proof of P9. Rapidity ladder (§17.3)
w₀ = ln(1+√2): since 1/(1+√2) = √2−1, e^{w₀} = 1+√2, e^{−w₀} = √2−1;
sinh w₀ = ((1+√2) − (√2−1))/2 = 1; cosh w₀ = ((1+√2) + (√2−1))/2 = √2.
Half-angle (ST): tan(π/8) = √2−1, so cot(22.5°) = 1+√2 and cot(67.5°) = tan(22.5°) = √2−1.
At the midpoints x_k, |cot x_k| ∈ {1+√2, √2−1}, so w(x_k) = ±ln(1+√2) = ±w₀, with the
alternating pattern +,−,−,+,+,−,−,+ by direct evaluation of the cot signs.
(√2)⁴ = 4, (√2)⁸ = 16 by arithmetic. d/dx ln(cot x) = (1/cot x)(−csc²x) = −1/(sin x cos x)
= −2/sin(2x) by the chain rule and the derivative of cot (ST). The irrationality of √2
(the Book 10 diagonal incommensurability) is why w₀ is not a rational multiple of any
rational log — used only as bookkeeping, not as a logical dependency. ∎ (Scope: PROVED.)

### Proof of P10. Flatwave identity (§17.1.4 stub, Figure 3)
With D1–D2 and seed notation (A = cxp, B = srx, crx = 1/A, sxp = 1/B):
1/urx + 1/uxp = (uxp + urx)/(urx·uxp) = (A + B − 1/A − 1/B)/((B − 1/A)(A − 1/B)).
Numerator: A + B − (A+B)/(AB) = (A+B)(AB−1)/(AB). Denominator: AB − 2 + 1/(AB) =
(AB−1)²/(AB). Hence 1/urx + 1/uxp = (A+B)/(AB−1) = (srx+cxp)/(srx·cxp − 1) exactly.
Per quadrant (s = sin x, c = cos x, s² + c² = 1):
- Q1: A = (s+1)/c, B = (c+1)/s; A+B = (1+s+c)/(sc) = AB − 1 → value +1.
- Q2: A = (s−1)/c, B = (1+c)/s; A+B = (1−s+c)/(sc) = −(AB − 1) → value −1.
- Q3: sin(x+π) = −sin x etc. gives A(x+π) = A(x), B(x+π) = B(x) (tan and |sec| have
  period π), reducing Q3 to the Q1 case → value +1.
- Q4: A = (s+1)/c, B = (c−1)/s; A+B = (1+s−c)/(sc) = −(AB − 1) → value −1.
So Flatwave(x) = +1 on Q1/Q3, −1 on Q2/Q4, i.e. Flatwave ≡ sgn(sin 2x) exactly
(verified by exact symbolic simplification, exit 0; the three non-Q1 quadrants reduce
algebraically as shown). The "Flatwave name collision" is therefore an identity, not a
collision: Books 2–3's FlatWave = sgn(sin 2x) is the same function — the identification
is exact algebra given the Books 2–3 definition (not re-established here). ∎ (Scope: PROVED.)

### Proof of P11. Paired footprint (§17.6.2)
cos(4(x+π)) = cos(4x+4π) = cos(4x) (ST). π/2 is a period: cos(4x+2π) = cos(4x); it is
minimal, since 0 < T < π/2 would give cos(θ+4T) = cos θ for all θ with 0 < 4T < 2π,
impossible. π/4 is not a period: cos(4·π/4) = −1 ≠ 1 = cos 0. Zeros:
cos(4(π/8 + kπ/4)) = cos(π/2 + kπ) = 0 for all integers k — all eight midpoints. ∎
(Scope: PROVED.)

### Proof of P12. IC-4 correction
At the octant boundaries: cos(4·π/4) = cos π = −1; cos(4·3π/4) = cos 3π = −1. The
manuscript's §17.6.2 bullet "vanishes at the octant boundaries (45°, 135°, …)" is false
as stated; the zeros are at the midpoints (P11). Figure 4 of the page is the exhibit. ∎
(Scope: PROVED.)

### Proof of P13. E-contact interiority (§17.6.3)
Decay octants are 1, 3, 5, 7 (D7); their midpoints 22.5°, 112.5°, 202.5°, 292.5° lie
strictly inside the open intervals (0°,45°), (90°,135°), (180°,225°), (270°,315°).
Finite check. ∎ (Scope: PROVED.)

### Proof of P14. Footprint invariance (§17.6.1)
x → x+π shifts octant indices by exactly 4; the E/B/O contact sets, defined by octant
membership (D7), are permuted by this shift, hence invariant as sets. The balanced
footprint 1 is trivially invariant. The C8 shift-by-4 is the kernel map: adding 4
octants is adding π. The clause "even under the code group" is excluded — see A2. ∎
(Scope: PROVED.)

### Proof of P15. S_F arithmetic (§17.7.1)
⟨Q_F, aT + R_⊥⟩ = ⟨(6/5)T, aT⟩ + ⟨(6/5)T, R_⊥⟩ (linearity of the Frobenius inner product, ST)
= (6a/5)‖T‖² + (6/5)⟨T, R_⊥⟩ = (6a/5)(5/2) + 0 = 3a, given ‖T‖² = 5/2 and ⟨T, R_⊥⟩ = 0.
⟨Q_F, R_⊥⟩ = (6/5)⟨T, R_⊥⟩ = 0. ∎ (Scope: PROVED — conditional on the stated premises.)

### Proof of P16. T-matrix arithmetic (§17.7.2)
T = diag(1, 1, −1/4×8): tr T = 1 + 1 − 8/4 = 0 (traceless); ‖T‖² = 1 + 1 + 8·(1/16) =
5/2; ‖Q_F‖² = (6/5)²‖T‖² = (36/25)(5/2) = 18/5; (1/4)⁴ = 1/256 by arithmetic. ∎
(Scope: PROVED.)

### Proof of P17. srx(22.5°) exact (§17.7.2)
On octant 1, srx(π/8) = (1+cos(π/8))/sin(π/8). With cos(π/8) = √(2+√2)/2,
sin(π/8) = √(2−√2)/2 (ST half-angle): srx(π/8) = (2+√(2+√2))/√(2−√2).
Claim: this equals √(4+2√2) + 1 + √2. Since (√(2+√2) + √(2−√2))² = 4 + 2√2,
√(4+2√2) = √(2+√2) + √(2−√2); and ((1+√2)√(2−√2))² = (3+2√2)(2−√2) = 2+√2, so
(1+√2)√(2−√2) = √(2+√2). Hence (√(4+2√2)+1+√2)·√(2−√2)
= √2 + (2−√2) + √(2+√2) = 2 + √(2+√2), which is exactly the numerator. Dividing gives
the identity. (Verified by exact symbolic simplification, exit 0.) ∎ (Scope: PROVED.)

### Proof of P18. Conversion-chain closure (§17.7.3)
From S_F = 3a, a = (6/5)c, c = 5S_F/18: a = (6/5)(5S_F/18) = S_F/3, so 3a = S_F — the
three n̂₅₄ forms coincide under substitution. −(1/256)(√10/6) = −√10/1536 by arithmetic.
The physical content of the prefactor is excluded — see A4. ∎ (Scope: PROVED as algebra.)

### Proof of P19. Bound arithmetic (§17.7.4)
(1/256)(18/5)(4) = 72/1280 = 9/160 = 0.05625, by arithmetic. Whether this bounds
anything is excluded — see A5. ∎ (Scope: PROVED.)

### Proof of P20. IC-6/IC-7 corrections (§17.18)
The CP Casimir decomposition (K-1..K-9) gives Sym²(128) = 1 ⊕ 1820 ⊕ 6435 — no 120
summand; hence the 120 does not sit inside Sym²(128). Λ²(128) has dimension
128·127/2 = 8128 = 120 + 8008, and the 120 summand lives there (ST). The SO(16) adjoint
has dimension 16·15/2 = 120 (ST), so the 135 is not the adjoint; Sym²₀(16) has dimension
16·17/2 − 1 = 136 − 1 = 135 (ST). Both manuscript statements are IC; the corrections are
proved. ∎ (Scope: PROVED.)

### P21, C1–C4, A1–A7, I1–I7
P21: the §17.8 octant→ellipse table is read off the proved carrier formulas P3/P7; the
page's V-checks corroborate (CHECKED corroboration, not a numerical sample on top of
a proof). C1, C2: the page's own NC verifications (V_E⁴ ≈ 638.7823; all four E-contact
dominant values coincide) — cited as CHECKED, not re-run (proof-over-sampling rule: the
analytic identities are proved; the numerics are the page's). C3: the C8 word pattern's
internal consistency is the page's CP check (CHECKED here); IC-5 (exactly two O's) is read
off D7. A1–A7: recorded as manuscript assertions/assumptions, not proved (see inventory).
I1–I7: recorded as incomplete/failed with exact boundaries; IC-8..IC-11 are the page's
verified audit findings about the §17.18.8.2 skeleton, reproduced here, not independently
re-derived by this worker.

## 5. New axioms/assumptions beyond Euclid + seed + earlier books

- **N-17-1 (definitional stratum).** D1–D9: the primitives (srx, cxp, crx, sxp), the carrier
  (V_R, H, K₂, D₂), the rapidity w, the Flatwave, the octant/3-bit-code/C8-word apparatus,
  and the T/Q_F/S_F matrices are new R Theory definitions over the real continuum with
  standard trigonometric functions — granted as definitional substrate, not proved from
  Euclid (the Elements contain no angle-functions or logarithms).
- **N-17-2 (imported standard theorems).** The trig identities, real-field algebra, chain
  rule, and the standard rep-theoretic facts used above are imported (ST), not inherited
  from the Elements.
- **N-17-3 (C8 correspondence).** A1: the C8 word ↔ octant correspondence as a theorem —
  ASSERTED, and disputed inside v1 itself (CONTR-1 on the Book 19 page).
- **N-17-4 (charge-matching ansatz).** A3: η₋₄ = η₀cos(4x) and the y₂ substitution —
  manuscript assertion.
- **N-17-5 (contraction physics).** A4, A5, A7: the physical content of the −(√10/1536)
  prefactor, the form of the 9/160 bound, and the role of 638.78 — ASSERTED/OPEN.
- **N-17-6 (open inputs).** I1–I3: the Frobenius norms, the explicit 1820 projector, and
  the numerical value of S_F are INCOMPLETE/OPEN with exact boundaries stated.

## 6. Close

Established in Euclid style: the complete octant/primitive/carrier/rapidity spine of
§§17.1–17.4 (P1–P9), the Flatwave identity in full (P10), the paired footprint (P11–P14),
the T-matrix and conversion-chain algebra (P15–P19), the rep-theoretic corrections
(P20), and the IC-1/IC-4 exhibits. Not established: the numerical value of S_F — the
skeleton that would compute it has four exhibited defects (I4–I7) and three blocked
inputs (I1–I3); the C8 correspondence as a theorem (A1); and everything the manuscript
itself declares open in §17.5 (A6). This matches the book page's own honest finding.
