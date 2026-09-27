# Book 0 claim-by-claim evaluation — Euclid trig-cumulative campaign

**Book:** 0 — Source Boundary and the Orientation Question.
**Sources:** `~/workspace/euclid_work/books/book0_proof.md` (claim inventory
§1–§13: 43 PROVED, 0 CHECKED, 10 ASSERTED groups, 0 INCOMPLETE);
`~/workspace/r-theory-rewrite/book0/index.html` (principal theorems).
**Date:** 2026-09-22.
**Trig criterion:** a claim is folded into the cumulative trigonometric proof
only if it yields a genuine trigonometric principle — an identity, lemma, or
exact relation about trigonometric functions, angles, or circular measure.

## Claim table

| Claim | Restatement | Verdict | Scope | Folded-in? | Notes |
|---|---|---|---|---|---|
| 1.1 | folded primitives srx, sxp, cxp, crx strictly positive on D | correct | PROVED | **P2** | srx, cxp via the Seed's positivity argument; sxp, crx via P1 |
| 1.2 | srx·sxp = 1 and cxp·crx = 1 (csc²−cot², sec²−tan²) | correct | PROVED | **P1** | folded Pythagorean identities |
| 1.3 | each primitive smooth on every open quadrant | correct | PROVED | no — regularity/analysis fact, not a trig identity | rational functions with nowhere-zero denominators on open quadrants |
| 1.4 | reflection laws: srx(−x)=sxp(x), cxp(−x)=crx(x) | correct | PROVED | **P3** | parity folded into the symmetry principle |
| 1.5 | quarter-turn laws: srx(x−π/2)=crx(x), cxp(x−π/2)=sxp(x) | correct | PROVED | **P3** | shift laws folded into the symmetry principle |
| 1.6 | all four primitives π-periodic (static quartet blind to 2π phase) | correct | PROVED | **P3** | periodicity folded into the symmetry principle |
| 2.1 | rational quartet recovery from z = srx with ε = sgn(z−1) | correct | PROVED | **P4** | z = 1 excluded on D (would need cos x = 0) |
| 2.2 | Riccati law z′ = −(1+z²)/2; ℝ(z) closed under d/dx | correct | PROVED | **P5** | mathematical phase derivative, no time law |
| 3.1 | urx + uxp = 4/sin(2x) in the book's notation | correct | PROVED | no new — already **P0** (the campaign Seed) | the Seed restated; folding again would duplicate P0 |
| A1 | sign fixture: reversed uxp = sxp − cxp retired as transcription error | recorded | ASSERTED | no — historical/editorial assertion | not independently verified; identity 3.1 holds either way |
| 4.1 | 1/urx + 1/uxp = sgn(sin 2x) on D | correct | PROVED | **P6** | FlatWave identity |
| 4.2 | FW(x+π/2) = −FW(x), FW(x+π) = FW(x), FW(x+2π) = FW(x) | correct | PROVED | **P7** | exact identities of sgn∘sin |
| 4.3 | sgn(urx) = sgn(uxp) = sgn(sin 2x); urx·uxp = 4/\|sin 2x\| | correct | PROVED | **P8** | common-sign law |
| 5.1 | H = sin(2x)/4, V = cos(2x)/2, V² + 4H² = 1/4 | correct | PROVED | **P9** | harmonic carrier ellipse |
| 5.2 | H extends smoothly to all of ℝ (seams sidestepped, not filled) | correct | PROVED | no — analysis fact; the formula is already P9 | smooth seam extension, no new trig identity |
| 5.3 | no continuous injective S¹ → ℝ exists | correct | PROVED | no — general topology, not trig | forces the (H,V) pair; standard M0 topology |
| 6.1 | transfer-circle identity p² + q² = 2 | correct | PROVED | **P10** | uses α² = β² = 1, sin²+cos² = 1 |
| 6.2 | λ′ = q/2; λ″ + λ = 1/2; (1−2λ)² + 4(λ′)² = 2 | correct | PROVED | **P11** | differential transfer closure |
| 6.3 | sharp bounds 1/2 < λ′ ≤ 1/√2; max exactly at λ = 1/2 where Ω = χ = 1 | correct | PROVED | **P12** | phase-rate bounds |
| 6.4 | saw_r′ + saw_x′ = 0 quadrant-locally | correct | PROVED | **P13** | definitional consequence of P6, not a conservation law |
| 6.5 | Ωχ = 1; χ = R_λ − 1; Ω = U_λ − 1 | correct | PROVED | no — pure algebra from the definitions | reciprocal odds; no trig content |
| 6.6 | Ω = λ/(1−λ) = saw_r/saw_x = uxp/urx = cxp/srx | correct | PROVED | **P14** | cross-layer ratio; AB ≠ 1 and urx ≠ 0 hold on D |
| 6.7 | E_D = \|sin 2x\|/(4(\|sin x\|+\|cos x\|)); normalized primitives give a positive partition of unity | correct | PROVED | **P15** | reciprocal-even normalization |
| 6.8 | cxp = e^{asinh(tan x)}, srx = e^{asinh(cot x)} exactly | correct | PROVED | **P16** | log representation; no physical rapidity follows |
| A2 | T0.III essay theorems (ζ reconstruction T28, seam obstruction C31, readings N2/N3/N5, closure T30) | inherited per the book's audit | ASSERTED | no — not re-derived | book reports 13 symbolic + 9 numerical checks pass; I did not re-run them |
| 7.1 | rank(dŷ) ≤ min(rank dΦ, rank dE, rank dΓ) | correct | PROVED | no — chain-rule linear algebra, not trig | differential rank firewall |
| 7.2 | one-forms f^a(x)dx span at most rank one; wedges vanish | correct | PROVED | no — exterior algebra on a 1D domain | coframe/metric obstruction |
| 7.3 | ω = K dη ⇒ dω + ω∧ω = 0 locally | correct | PROVED | no — differential-form computation, not trig | fixed-generator local flatness |
| 7.4 | u(λ) = (√λ, √(1−λ)) cannot cover ℂP¹; independent phase φ is an explicit extension | correct | PROVED | no — measure-theoretic rank obstruction, not trig | a J² = −I is algebra, not a new coordinate |
| 8.1 | Riccati flow lifts to u′′ + u/4 = 0; J² = −I commutes with the flow | correct | PROVED | no — algebraic complex structure on the lifted plane, not a trig identity (its differential content is P5) | flow-invariant complex structure; quotiented to ℝP¹, rank intact |
| 8.2 | on an oriented Euclidean 2-plane exactly one orthogonal complex structure is compatible; J ↔ −J under orientation reversal | correct | PROVED | no — classification of orthogonal complex structures, not trig | — |
| 8.3 | every real-linear J with J² = −I on ℝ² is GL(2,ℝ)-conjugate to the standard quarter-turn | correct | PROVED | no — conjugacy classification, not trig | — |
| 9.1 | tetrahedral Gram G has det G = ℓ⁶/2 > 0: rank three | correct | PROVED | no — determinant computation, not trig | T1 spatial-rank obstruction resolved by extension |
| 9.2 | O(G) contains orientation-reversing isometries | correct | PROVED | no — group-theoretic fact, not trig | — |
| 9.3 | D₁D₀ = 0, D₂D₁ = 0 for oriented simplicial boundary operators | correct | PROVED | no — simplicial homology, not trig | boundary-of-boundary |
| 9.4 | no function on a 2-to-1 projective/quadratic quotient recovers the lost central ± | correct | PROVED | no — general set-theoretic obstruction, not trig | central-sign nonselection |
| 9.5 | M₂(ℝ) admits Clifford presentations Cl(2,0) and Cl(1,1) | correct | PROVED | no — matrix-algebra presentations, not trig | — |
| 9.6 | in y = αz + β (α ≠ 0), σ = sgn(α) is representable from the map | correct | PROVED | no — readout-identifiability, not trig | not a chirality law |
| A3 | projection architecture / candidate discipline / observation grammar / extension certificates (T1 audit framework) | as stated | ASSERTED | no — methodological framework | taken from the book's T1 audit, not re-derived |
| A4 | seam/Pin/central-lift nonselection findings | as stated | ASSERTED | no — audit findings, not theorems | — |
| A5 | composition/control audit (tensor products, Hamiltonian expressibility, Lie closure, tomography relative to declared extensions) | as stated | ASSERTED | no — audit finding | exact only relative to declared extensions |
| A6 | T3 stripping of physical time, Lorentzian signature, Maxwell and Einstein–Maxwell content to the physics interface; obstruction ledger | as stated | ASSERTED | no — disposition declaration | — |
| A7 | "coordinate choice generates no physics"; physics-import counts of 0 | as stated | ASSERTED | no — methodological declarations | — |
| 0.IV.T1 | Automorphism Obstruction: unoriented U with orientation-exchanging r admits no canonical selector | correct | PROVED | no — automorphism/naturality argument, not trig | four-line proof; force rests on the definition of "canonical" |
| 0.IV.T1 app (T2) | reflection on the two-channel plane; J ↔ −J after declaration; quotient data cannot restore central sign | correct | PROVED | no — application of the theorem, no new trig identity | rests on 8.2, 9.4 |
| 0.IV.T1 app (T3) | orientation-reversing G-isometries; frame reversal preserves Gram; reorientation preserves D² = 0 | correct | PROVED | no — geometric application, no new trig identity | rests on 9.2, 9.3 |
| A9 | 0.IV corollaries C1–C3: exact scope, no universal impossibility | as stated | ASSERTED | no — methodological clarifications | boundary of the theorem |
| 0.III.T1 (1) | orientation internally representable | correct | PROVED | no — summarizes folded facts (P6, P7, 8.x), not a new principle | — |
| 0.III.T1 (2)–(5) | mirror/oppositely-oriented realizations admissible; quotients may erase central sign | correct | PROVED | no — classification summary, not a trig identity | rests on 8.2, 8.3, 9.2, 9.4 |
| 0.III.C1 | no axiom needed for representation | correct | PROVED | no — meta-theorem about the corpus | constructions need no new axiom |
| A8 | 0.III.T1 (6): no inherited theorem assigns privileged physical status; closure "therefore" | as stated | ASSERTED | no — audit-completeness claim | exhaustiveness of the T0–T3 audit not independently verified; 0.III.C2–C3 likewise ASSERTED. **Note 2026-09-27:** theorem statement, 6 conclusions, proof sketch, C1–C3, and the Book 0 checkpoint verified present in the manuscript (volume-i.txt ll.900–1010); T1 σκ readout verified (l.346). "Revised M0–M4" is the manuscript's candidate-universe term. Same passage verified VERBATIM in the ORIGINAL `R_Theory___Volume_I.docx` (Kit's 2026-09-27 upload). What remains ASSERTED is only the exhaustiveness of the underlying T0–T3 closure audit, not the theorem's presence or wording. |
| M5-conditional | given Axiom 0: I(u,v) = (−v,u), I² = −id_W; W ≅ U⊗_ℝℂ; dim_ℝW = 10, dim_ℂW = 5 | correct | PROVED (conditional on Axiom 0) | no — conditional complex-structure construction, not trig | forward-looking decadic airlock |
| A10 | M5 inherits no Spin(10), chirality selector, gauge groups, or empirical calibration | declared | ASSERTED | no — boundary declaration | — |

## Per-book counts

- Claims evaluated: **53** (43 PROVED + 10 ASSERTED)
- PROVED: **43** (1.1–1.6, 2.1–2.2, 3.1, 4.1–4.3, 5.1–5.3, 6.1–6.8,
  7.1–7.4, 8.1–8.3, 9.1–9.6, 0.IV.T1 + 2 applications,
  0.III.T1(1)/(2)–(5)/C1, M5-conditional)
- CHECKED (as verdict): **0** (every load-bearing claim has a complete
  analytic proof; per the proof-over-sampling rule no sampling was run)
- ASSERTED: **10** (A1, A2, A3, A4, A5, A6, A7, A8, A9, A10)
- INCOMPLETE: **0**
- Folded into the cumulative trigonometric proof as new Principles: **16**
  (P1–P16, all PROVED)
- Not folded: **37** (1 already P0; 26 proved claims with no trig content;
  10 asserted groups)

## Why 26 proved claims were not folded

Verified mathematics is not the same as trigonometric content. The 26
non-folded proved claims are rank inequalities (7.1–7.3), a
measure-theoretic rank obstruction (7.4), complex-structure classification
(8.1–8.3), linear-algebraic and geometric computations (9.1–9.6), an
automorphism/naturality theorem and its applications (0.IV.T1 × 3), the
separation theorem's representability summaries (0.III.T1(1), (2)–(5), C1),
a conditional complex-structure construction (M5), regularity facts
(1.3, 5.2), a topology theorem (5.3), and definitional algebra (6.5).
None is an identity, lemma, or exact relation about trigonometric
functions, angles, or circular measure. Forcing any of them into the
cumulative *trigonometric* proof would misrepresent the book and weaken
the document's dependency discipline. Claim 3.1 was not folded because it
is P0 itself in the book's notation.

## Honest Euclid boundary

No proposition of Euclid's *Elements* is a logical premise of any
principle folded from Book 0 — the book's own proof file states this
plainly, and the standing rule forbids invented citations. Each folded
principle cites only the Seed (P0), earlier principles in dependency
order, or ordinary background mathematics (M0). Euclid's Elements enter
this campaign as the method (definitions first, nothing used before it is
proved), not as deductive premises of Book 0's analytic trigonometry.

status: complete
