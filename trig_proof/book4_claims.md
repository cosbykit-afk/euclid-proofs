# Book 4 — claim-by-claim evaluation (trig-cumulative campaign)

**Book:** Euclid's Elements Book 4 + R Theory Book 4 ("Geometric Rank,
Coframes, and Connection").
**Sources read 2026-09-22:** `~/workspace/euclid_work/books/book4_proof.md`
(claim inventory + proofs), `~/workspace/r-theory-rewrite/book4/index.html`,
`~/workspace/euclid_work/ledger/book4_ledger.md`; Euclid citations
cross-verified in `book1_ledger.md` / `book2_ledger.md`.
**Scope labels:** PROVED / CHECKED / ASSERTED / INCOMPLETE (+ ST = standard
imported theorem, cited not re-derived). Compound labels like
"PROVED+CHECKED" mean a proof exists AND a completed verification run
exists; the run is never the proof.

## 1. Load-bearing inventory claims (from book4_proof.md §(a))

| # | Claim (one line) | Verdict | Scope | Folded-in? | Notes |
|---|---|---|---|---|---|
| E1 | Equal circles → equilateral triangle | proved as stated | PROVED | no | R Theory synthetic counterpart of the Euclid 1.1 construction chain (relative to ASSERTED P4.1/P4.1-C). Its trig content (60° vertex angles) is proved from Euclid 4.15 in Principle 3, not from the R Theory premises. |
| L1 | Six native sectors equal, complete one turn | proved as stated | PROVED | yes → Principle 3 | The 60° sector grammar; Principle 3 re-grounds it on Euclid 4.15. |
| P0 | Synthetic right angle from bisected sector | proved as stated | PROVED | no | The 90° value enters definition D-T4.1; no trig identity beyond the right-angle definition. SSS debt (P4.1-C) disclosed in the source proof. |
| DC | Degree corollary: 360/4 = 90, sector 60, half-sector 30 | proved as stated | PROVED | no | Definitional arithmetic on the degree definition; used in D-T4.1. Not a trig identity. |
| C1 | Coframe criterion θ¹∧⋯∧θⁿ ≠ 0 iff det E ≠ 0 | proved as stated | PROVED | no | Multilinear algebra; no trig content. |
| C2 | No canonical coframe from Books 0–3 (negative) | proved as stated | PROVED | no | Rank argument; no trig content. |
| R1 | Rank obstruction: dA = A′(x)dx ⇒ rank ≤ 1 | proved as stated | PROVED | no | One-variable calculus; no trig content. |
| ISO | Flower⇄Cartesian isometry X = u+v/2, Y = (√3/2)v ⇒ X²+Y² = u²+uv+v² | proved as stated | PROVED+CHECKED | yes → Principle 4 | Exact algebra is the proof; page-reported 20,000-sample run (1.42e-14) cited, not re-executed. Principle 4 restates it as the 60° cosine law via Principle 3. |
| M1 | Sylvester: minors r², 3r⁴/4, r⁶/2 > 0 ⇒ positive definite | proved as stated | PROVED+CHECKED | no | Standard imported criterion applied; exact sympy run this campaign. Linear algebra; no trig content. |
| M2 | H positive definite + det E ≠ 0 ⇒ nondegenerate h | proved as stated | PROVED+CHECKED | no | Linear algebra (checked as part of the M1 exact run). |
| T0 | Regular tetrahedron from equal spheres on equilateral face | proved as stated | PROVED | no | Solid construction (relative to S1–S6); no trig content. |
| T1 | G₃ spectrum {2,½,½}, det r⁶/2, inverse, 6 edges = r, altitude r√(2/3), V = r³/(6√2) | verified exactly | CHECKED | no | Exact rational/surd arithmetic this campaign; only angle content is the 60° faces, already in Principle 3. |
| T2 | 12-neighbor lattice shell; Σu_A u_Aᵀ = 4I₃ | verified exactly | CHECKED | no | Exact enumeration + embedding this campaign (first attempt used an inconsistent embedding; corrected run is the one cited). Lattice combinatorics; no trig content. |
| A1 | Anholonomy Cᵃ_bc = dual-frame commutator coefficients | proved as stated | PROVED | no | Invariant formula for d; no trig content. |
| A2 | Pure gauge ω = B⁻¹dB ⇒ R = 0 | proved as stated | PROVED | no | Wedge algebra; no trig content. |
| A3 | One-generator ω = A(φ)dφ ⇒ R = 0 (closed obstruction) | proved as stated | PROVED+CHECKED | no | 1-forms square to zero; page-reported sympy run cited. No trig content. |
| A4 | Flat anholonomic example: dθ² ≠ 0 with T = 0, R = 0 | proved as stated | PROVED+CHECKED | no | Structure-equation computation; page-reported sympy run cited. No trig functions. |
| A5 | Cartan–Bianchi DTᵃ = Rᵃ_b∧θᵇ, DRᵃ_b = 0 | standard imported | ST | no | Cited, not re-derived; not counted in PROVED tally. |
| K1 | Curvature defined on spatial carrier; needs no time direction | proved as stated | PROVED | no | Structural: a statement about what the definitions require. |
| K2 | h_H curvature law Rᵃ_b = −(1/L²)θᵃ∧θᵇ, K = −1/L² | proved as stated | PROVED+CHECKED | no | Structure-equation computation; page-reported sympy run cited. No trig content. |
| O1 | Exactly two orientation classes | proved as stated | PROVED | no | Group theory (sign fibers of det); no trig content. |
| O2 | Volume law θ′ = Aθ ⇒ vol′ = (det A)·vol | proved as stated | PROVED+CHECKED | no | Multilinearity; page-reported 1,999-matrix run cited. |
| O3 | b↔c swap: orientation-reversing isometry of G₃; nonselection | proved as stated | PROVED+CHECKED | no | Exact rational arithmetic this campaign (SᵀG₃S = G₃, det S = −1). No trig content. |
| NW | No-Euclid-wholesale theorem | proved as stated | PROVED | no | Structural meta-statement about declared premises. |
| NN | No-novelty from coordinate change (Gate H) | proved as stated | PROVED+CHECKED | no | Basis-independence of metric invariants; isometry re-verified via ISO. |

## 2. Asserted premise groups (book4_proof.md §(c) — admitted, not proved)

| # | Premise group | Scope | Folded-in? | Notes |
|---|---|---|---|---|
| P4.1 | Pre-metric construction substrate (7 items) | ASSERTED | no | Admitted foundation; cannot found a principle. |
| P4.1-C | SSS congruence as admitted synthetic principle | ASSERTED | no | The "congruence debt"; owned explicitly by the manuscript (4.X.P2). |
| P4.2-L | Sixfold local completion at every interior Flower center | ASSERTED | no | Declared counterpart of what Euclid 4.15 proves; Principle 3 uses Euclid's proof, not this declaration. |
| P4.2-M | Affine/vector realization on each Flower chart | ASSERTED | no | Admitted. |
| P4.3 | Global Euclidean completion (5 clauses incl. unique parallels) | ASSERTED | no | Re-admitted fifth postulate, quarantined to propositions that need it. |
| P4.4 | Global solid completion | ASSERTED | no | Admitted; not derived from one tetrahedron. |
| S1–S6 | Solid postulates (noncoplanar extension, plane determination, perpendicular to a plane, sphere construction, equal-sphere intersection, rigid solid congruence) | ASSERTED | no | Euclid Book 11 not inherited; admitted explicitly. |
| Gates A–H | Ordering constitution incl. physics firewall (G) and coordinate-novelty firewall (H) | ASSERTED | no | Declared ordering rules, not theorems. |
| FL | Foundational failure ledger (8 prohibited inferences) | ASSERTED | no | Declared prohibition list. |
| N1 | Differential framework (smooth charts, exterior algebra, Cartan equations; Sylvester, Levi–Civita, Cartan–Bianchi imported) | ASSERTED | no | Working framework admitted at point of use. |

## 3. Asserted ledger records (manuscript stipulations, not theorems)

| # | Record | Scope | Folded-in? | Notes |
|---|---|---|---|---|
| RC | Re-presentation completeness ("entire dependency-bearing chain") | ASSERTED | no | The page tags this MA itself; surveyed, not audited. |
| SUP | Supplementary diagnostics §§4.VI–VII | ASSERTED | no | Locked out of downstream foundations by the Flower-role lock. |
| P9 | Curvature is geometry, not gravity (firewall) | ASSERTED | no | Disciplinary boundary declaration, not a theorem. |
| P11 | Geometric-extension certification + eight negatives | ASSERTED | no | Dependency-chain audit and physics-zero ledger as stated by the book; surveyed, not re-derived. |
| ANS | Projection-scalar ansätze / necessity barrier / signature boundary | ASSERTED | no | Manuscript assertions; no canonical raw crossing law derived (stated as not derived). |

## 4. INCOMPLETE — Euclid Book 4 material with no R Theory extension (19 items)

| Euclid item | Scope | Notes |
|---|---|---|
| Def 4.1 (inscribed figure) | INCOMPLETE | Inscribed/circumscribed vocabulary occurs zero times in the Volume I manuscript. |
| Def 4.2 (circumscribed figure) | INCOMPLETE | As Def 4.1. |
| Def 4.3 (figure inscribed in a circle) | INCOMPLETE | As Def 4.1. |
| Def 4.4 (figure circumscribed about a circle) | INCOMPLETE | As Def 4.1. |
| Def 4.5 (circle inscribed in a figure) | INCOMPLETE | As Def 4.1. |
| Def 4.6 (circle circumscribed about a figure) | INCOMPLETE | As Def 4.1. |
| Def 4.7 ("inserted" line) | INCOMPLETE | Absorbed implicitly into P4.1's compass transfer; not separately stated or proved. |
| Prop 4.2 (inscribe equiangular triangle) | INCOMPLETE | No R Theory extension. |
| Prop 4.3 (circumscribe equiangular triangle) | INCOMPLETE | No R Theory extension. |
| Prop 4.4 (incircle of a triangle) | INCOMPLETE | R Theory constructs no incircles. |
| Prop 4.5 (circumcircle of a triangle) | INCOMPLETE | R Theory constructs no circumcircles. |
| Prop 4.8 (circle in a square) | INCOMPLETE | No R Theory extension. |
| Prop 4.9 (circle about a square) | INCOMPLETE | No R Theory extension. |
| Prop 4.10 (golden-section triangle) | INCOMPLETE | "Golden" occurs zero times in the manuscript; 2.11 not re-presented. |
| Prop 4.11 (inscribed pentagon) | INCOMPLETE | "Pentagon" occurs zero times in the manuscript. |
| Prop 4.12 (circumscribed pentagon) | INCOMPLETE | As 4.11. |
| Prop 4.13 (circle in a pentagon) | INCOMPLETE | As 4.11. |
| Prop 4.14 (circle about a pentagon) | INCOMPLETE | As 4.11. |
| Prop 4.16 (15-gon) | INCOMPLETE | No R Theory counterpart (incl. Proclus's astronomical use). |

## Per-book counts

- Evaluated claims: **59** (25 inventory + 10 premise groups + 5 ledger records + 19 Euclid items)
- PROVED: **22** (inventory items with deductive proof exhibited, relative to declared premises)
- CHECKED: **8** verification runs — 3 exact this campaign (G₂/G₃ Gram cluster; 12-shell + 4I₃; b↔c swap isometry) + 5 page-reported runs cited, not re-executed (ISO numeric; A3 symbolic; A4 symbolic; K2 symbolic; O2 numeric). No failed or timed-out computations.
- ASSERTED: **15** (10 premise groups + 5 ledger records)
- INCOMPLETE: **19** (Euclid items with no extension; nothing failed — the absence is deliberate and disclosed)
- ST (standard imported, not counted above): **1** (A5 Cartan–Bianchi)
- Folded into the cumulative proof: **2** — Principle 3 (exact 30°/60° trig values; from E1, L1, P0, DC; proved via Euclid 4.15 + 1.5, 1.12, 1.26, 1.32, 1.47) and Principle 4 (oblique-axis isometry / 60° cosine law; from ISO; via Principle 3 + Euclid 1.47). Cumulative principle count: **5** (P0–P4).

## status: complete
