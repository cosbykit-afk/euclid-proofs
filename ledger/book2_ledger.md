# Euclid's Elements — Book 2: Extension Ledger (R Theory)

**Sources read for this ledger (not memory):**
- Euclid: `/home/hatch/workspace/euclid_work/text/book2.txt` (Fitzpatrick/Heiberg, Greek + English, 939 lines, read in full)
- R Theory rewrite: Books 0–6 pages at `/home/hatch/workspace/r-theory-rewrite/book{0..6}/index.html` (headings + full-text keyword contexts extracted)
- R Theory manuscript original: `/home/hatch/workspace/r-theory-rewrite/manuscript/R-Theory-Volume-I-original.txt` (Volume I, 26,734 lines; §4.IV.C, §4.X, §5.2 read in full where cited)
- History: `/home/hatch/workspace/user/files/euclid-encyclopedia-article.html` (Encyclopedia.com biography)
- Pedagogy: `/home/hatch/workspace/user/files/a3cd8c26d8eb63f6315ac09d5f1d1ef5071b2fe3.pdf` (TESS-India, *Developing creative thinking in mathematics: trigonometry* — "Trigonometry links concepts about shape and space with ratio, deduction and mathematical proof")

---

## Book summary

Book 2 is **geometric algebra**: 2 definitions + 14 propositions proving geometrically what are today
algebraic quadratic identities — a(b+c+…) = ab+ac+…, (a+b)² = a²+b²+2ab, and companions — by
dissecting and reassembling rectangles and squares. The encyclopedia source places it as follows:
Book II "develops the transformation of areas adumbrated in Book I" and is "a generalization of
Pythagoras' theorem, which was the penultimate proposition of book I" (1.47); in it "Euclid addressed
rectangles and squares" as Book III addresses circles and Book IV polygons. It is the book Apollonius'
*Conics* propositions 53–56 later build on (the three-line locus converse).

Internal dependencies of Book 2 on earlier material (from the proof texts): Postulate 5,
and propositions 1.3, 1.5, 1.6, 1.10, 1.11, 1.12, 1.15, 1.29, 1.31, 1.32, 1.34, 1.36, 1.43,
1.45, 1.46, 1.47 — plus intra-Book-2 dependencies 2.4 → 2.12, 2.5 → 2.14, 2.6 → 2.11, 2.7 → 2.13.

**The central extension finding (read the files, not the claim):** R Theory's audited Volume I
(rewrite Books 0–6) does **not** re-present, re-derive, or cite Euclid's 2.1–2.14. Its re-presented
Euclidean proof chain (§4.IV.C, "Global Euclidean Completion and Book II Proofs" — note: "Book II"
there means *Flower Space* Book II, not Euclid's Book 2) covers only Book-I-style constructions:
angle copying, exterior-angle inequality, parallel criteria (Q1–Q7), parallelograms (Q8–Q9), and the
square construction (Q10), ending with the status statement "The global Euclidean theory then enters
explicitly through P4.3, from which the source Book II proofs establish parallel-angle relations,
the triangle angle sum, parallelograms, and the square" (manuscript §4.IV.C, marked manuscript
assertion). No quadratic identity of Euclid's Book 2 is reproduced anywhere in the corpus or
manuscript — confirmed by full-text searches for "gnomon" (zero hits in all 23 book pages),
"golden" (zero hits everywhere), and "rectangle contained / twice the rectangle" (zero hits in the
Volume I manuscript).

What the extension does **instead** is replace the synthetic area-dissection method with admitted
symmetric-bilinear-metric machinery, and it says so explicitly:

- Theorem 4.X.P6 admits a symmetric bilinear form g (Declaration P4.2-M); **Corollary 4.X.P6.1**
  derives the analytic Pythagorean identity g(u+v,u+v) = g(u,u) + g(v,v) for perpendicular u, v
  from the admitted bilinearity — and then states verbatim: *"A separate synthetic Euclidean proof
  of the classical triangle proposition is not being claimed here."*
- Theorem 4.X.P7 proves the Flower quadratic identity X² + Y² = u² + uv + v² (the modern analytic
  successor of the "rectangles and squares" content), re-verified numerically for the rewrite
  (max error 1.42e-14 over 20,000 samples — completed numerical check).
- Theorem 4.X.P10 (No-Euclid-wholesale): the revised Book 4 "does not accept Euclidean metric
  geometry wholesale"; its starting data contain no inner product, Cartesian coordinates, parallel
  postulate, Pythagorean theorem, or global flatness — each is earned or explicitly declared.
- §4.IV.C: "the familiar Flower metric follows from the constructed unit, the constructed right
  angle, and the equilateral Flower edge relation. **No cosine formula is required as a premise.**"
  (The extension dispenses with 2.12–2.13 as premises rather than generalizing them.)

In TESS-India terms (shape/space ↔ ratio/deduction/proof, constructive rather than rote): Euclid's
Book 2 links shape (rectangles/squares) to algebraic ratio (2.11's golden section) by constructive
area dissection. The extension keeps the constructive half (the equal-circle Flower construction earns
the right angle *before* any metric — Theorem 4.X.P5, which invokes no parallel-line axiom) but moves
the deduction half into the admitted bilinear-form declaration. The load-bearing step is therefore an
**assumption**, and it is listed below with the other new axioms, exactly as Kit's standard requires.

---

## Full proposition inventory

Scope grammar (Kit's standard): **PROVED** = deductive proof from Euclid's definitions/postulates/
propositions shown; **CHECKED** = verified by a completed computation (described);
**ASSERTED** = manuscript stipulation or new axiom; **INCOMPLETE** = not established (with reason).

| # | Euclid statement (one line) | Euclid proof dependencies | R Theory extension (attested location) | Scope |
|---|---|---|---|---|
| Def 2.1 | A rectangular parallelogram is "contained by" its two sides forming the right angle. | — (definition) | **Not imported.** Book 4 replaces "rectangle contained by" language with the symmetric bilinear form g and Gram matrices G₂, G₃ (Book 4 §§4.IV–4.V). No attested formal derivation from Def 2.1. | **INCOMPLETE** — the conceptual replacement is real (quadratic forms succeed area language) but no extension claim is proved from this definition anywhere in the corpus. |
| Def 2.2 | The gnomon: a parallelogram about a diagonal plus its two complements. | — (definition) | **Absent.** The word "gnomon" occurs zero times in the entire rewrite series. The gnomon arguments of 2.5–2.8 have no counterpart. | **INCOMPLETE** — no extension claim exists. |
| 2.1 | a(b+c+d+…) = ab+ac+ad+… (distributive law, geometric) | 1.11, 1.3, 1.31, 1.34 | Successor: **bilinearity** of the admitted metric — Theorem 4.X.P6 proves a symmetric bilinear g is fixed by its values on basis pairs, i.e. g(v,w) is linear in each argument. But this is a property of the *declared* bilinear form, not a derivation from 2.1. | **ASSERTED** (conditional on P4.2-M): the algebraic content of 2.1 is absorbed into the admitted bilinearity; it is never proved from Euclid's axioms. |
| 2.2 | ab + ac = a² (for a = b+c) | 1.46, 1.31 | Same as 2.1: absorbed into admitted bilinearity (Thm 4.X.P6). Not re-derived. | **ASSERTED** (conditional on P4.2-M), same basis as 2.1. |
| 2.3 | (a+b)a = ab + a² | 1.46, 1.31 | Same as 2.1: absorbed into admitted bilinearity (Thm 4.X.P6). Not re-derived. | **ASSERTED** (conditional on P4.2-M), same basis as 2.1. |
| 2.4 | (a+b)² = a² + b² + 2ab (generalizes 1.47) | 1.46, 1.31, 1.29, 1.5, 1.6, 1.34, 1.43 | Closest attested successor: **Theorem 4.X.P7** — X²+Y² = u²+uv+v² (Flower quadratic form = ordinary unit-circle quadratic form), **numerically re-verified** (max error 1.42e-14 over 20,000 samples); plus **Cor. 4.X.P6.1** analytic Pythagorean g(u+v,u+v)=g(u,u)+g(v,v) from admitted bilinearity. The text explicitly disclaims a synthetic Euclid-proof: *"A separate synthetic Euclidean proof of the classical triangle proposition is not being claimed here."* | **CHECKED** (the Flower quadratic identity by completed numerical check; the algebra surveyed CP from admitted P4.2-M) — but **INCOMPLETE as a derivation from Euclid 2.4**: the corpus never attempts it, by its own statement. |
| 2.5 | ab + [(a+b)/2 − b]² = [(a+b)/2]² | 1.46, 1.31, 1.43, 1.36 | No counterpart re-presented. Algebraic content absorbed into the bilinear algebra imported with P4.2-M. | **INCOMPLETE** — no attested extension derivation. |
| 2.6 | (2a+b)b + a² = (a+b)² | 1.46, 1.31, 1.36, 1.43 | No counterpart re-presented. | **INCOMPLETE** — no attested extension derivation. |
| 2.7 | (a+b)² + a² = 2(a+b)a + b² | 1.46, 1.43 | No counterpart re-presented. | **INCOMPLETE** — no attested extension derivation. |
| 2.8 | 4(a+b)a + b² = [(a+b)+a]² | 1.3, 1.46, 1.34, 1.36, 1.43 | No counterpart re-presented. | **INCOMPLETE** — no attested extension derivation. |
| 2.9 | a² + b² = 2[((a+b)/2)² + ((a+b)/2 − b)²] | 1.11, 1.3, 1.31, 1.5, 1.32, 1.29, 1.6, 1.34, 1.47 | No counterpart re-presented. (Book 6's simplex Gram spectra are modern quadratic-form results, but no derivation chain to 2.9 is attested.) | **INCOMPLETE** — no attested extension derivation. |
| 2.10 | (2a+b)² + b² = 2[a² + (a+b)²] | 1.11, 1.3, 1.31, 1.29, Post 5, 1.5, 1.32, 1.15, 1.6, 1.34, 1.47 | No counterpart re-presented. | **INCOMPLETE** — no attested extension derivation. |
| 2.11 | Cut AB so that AB·BH = AH² (the "golden section" construction) | 1.46, 1.10, 1.3, 2.6, 1.47 | **Completely absent.** Zero mentions of "golden" in all 23 book pages and the Volume I manuscript. | **INCOMPLETE** — the extension makes no claim here at all. |
| 2.12 | Obtuse-angle cosine law: BC² = AB² + AC² + 2·CA·AD | 1.12, 2.4, 1.47 | Explicitly **dispensed with as a premise**: §4.IV.C — "No cosine formula is required as a premise" for the Flower metric (it follows from constructed unit + constructed right angle + equilateral edge relation). The Flower metric derivation is surveyed in the text (CP). | **CHECKED-proof-surveyed in text** that the cosine law is unnecessary as a premise (the metric derivation it surveys is CP from stated antecedents) — **INCOMPLETE as a re-derivation of 2.12**, which is not attempted. |
| 2.13 | Acute-angle cosine law: AC² = AB² + BC² − 2·CB·BD | 1.12, 2.7, 1.47 | Same as 2.12. | Same as 2.12. |
| 2.14 | Construct a square equal in area to a given rectilinear figure (quadrature) | 1.45, 1.3, 1.10, 2.5, 1.47 | **Not re-presented.** The re-presented chain covers only the square-on-a-segment construction Q10 (4.IV.C) and cites rectangle construction 1.45 as a step; 2.14's full quadrature argument is not reproduced, and the "square" claim in the 4.IV.C status sentence is a manuscript assertion (MA). | **INCOMPLETE** — not re-presented; the cited re-presentation claim is MA, not an independent verification. |

---

## New axioms/definitions the extension introduces beyond Euclid

These are the load-bearing assumptions. Euclid's Book 2 rests on his own definitions, postulates,
and common notions; R Theory's geometric layer rests on the following *additional* admitted premises
(all scope **ASSERTED** / **AA** = assumption or axiom, unless noted). Exact wording from the corpus:

1. **Axiom Zero** (Book 5, §5.2): real–imaginary independence and primitive noncoupling. A genuine
   new axiom with no Euclid antecedent; the Book 5 "Decadic Carrier Theorem" is conditional on it.
2. **P4.1** — pre-metric construction substrate (admitted import): points may be joined and straight
   segments continuously extended; one positive construction length r may be copied congruently;
   equal circles with that copied radius may be drawn and intersected; triangular faces produced by
   repeated flower operations may be continuously filled. Explicitly does *not* import: Euclidean
   affine plane, inner product, Cartesian coordinates, numerical angle measure, the Pythagorean
   theorem, a global distance function, the parallel postulate, global flatness, rank-three base,
   coframe, connection, curvature, time, or Lorentzian signature.
3. **P4.1-C** (Declaration) — SSS congruence principle: two triangles with three pairwise-congruent
   sides have equal corresponding angles, up to direct or reflected placement. The right-angle proof
   (Thm 4.X.P5) is *conditional* on it — "not presented as deriving all rigid congruence from equal
   circles alone" (Thm 4.X.P2).
4. **P4.2-L** (Declaration) — sixfold local completion: at every ordinary interior Flower center,
   six congruent primitive Flower triangles meet cyclically without gap or overlap; rays separated by
   three consecutive native sectors form one straight line.
5. **P4.2-M** (Declaration) — affine/vector realization: on each ordinary continuous Flower chart,
   admit a real two-dimensional translation space carrying the constructed directions as rays and
   respecting the synthetic line/incidence structure. **This is the premise that absorbs Euclid's
   Book 2**: bilinearity of the declared metric replaces the synthetic distributive/area identities
   2.1–2.10. It is admitted, not proved — Theorem 4.X.P6 exists *only* after this declaration.
6. **P4.3** (Declaration) — global Flower completion: (1) extension without boundary; (2) no branch
   points or topological twist; (3) defect-free metric gluing of neighboring charts; (4) global
   flatness (zero intrinsic curvature); (5) the Euclidean parallel property (exactly one parallel
   through an exterior point). Not a consequence of the Flower construction (Thm 4.X.P8 notes
   1–5 "are not consequences of Theorems 4.X.P3–P5 alone").
7. **S1–S6** — solid postulates (admitted, Book 4 §4.V.A): noncoplanar extension (S1), determination
   of a plane (S2), perpendicular to a plane (S3), sphere construction (S4), equal-sphere flower
   intersection (S5), rigid solid congruence (S6). Third direction is *not* a planar consequence.
8. **Congruence Principles A and C** (ASA and friends) used in the Q1–Q10 re-presented proofs, plus
   the re-presented **Definitions**: transversal, alternate interior angles, parallelogram
   ("quadrilateral whose opposite sides are parallel"), rectangle ("four right angles"), square
   ("four equal sides and four right angles") — all carried by the Flower-space re-presentation,
   not by Euclid's own definitions.
9. **Gates A–H** (admitted working rules): rank before dimension language; Flower before metric,
   metric after right angle; continuous carrier before discrete lattice; coframe before connection;
   connection before curvature; orientation before handedness; geometry before physics;
   coordinate-novelty firewall (Gate H: no new invariant geometry from a coordinate change alone).
10. **New geometric definitions** with no Euclid counterpart, used by the extension's quadratic-form
    machinery: Gram matrix G₂ = r²[[1,1/2],[1/2,1]], G₃ = r²[[1,1/2,1/2],[1/2,1,1/2],[1/2,1/2,1]];
    the quadratic form u²+uv+v²; the coframe criterion θ¹∧⋯∧θⁿ ≠ 0; connection, torsion, curvature
    (Rᵃ_b), volume form, Hodge star; Book 6's Hermitian carrier h and complex-volume reduction
    (conditional extensions, declared). Book 0 additionally admits M₂(ℝ) Clifford presentations and
    the bilinear/reflection theorems as explicit extensions or presentation data.

**Honest bottom line.** The audited Volume I establishes a dependency-minimized synthetic route to a
right angle, a metric, Gram/quadratic forms, and Euclidean completion — but it does not prove
Euclid's Book 2 identities from Euclid's axioms, and it does not claim to (4.X.P6.1 disclaimer,
4.X.P10 no-wholesale theorem). Anyone asserting "R Theory extends Euclid's geometric algebra" must
therefore mean the *conceptual* succession — area dissection replaced by the admitted bilinear form —
not a proved derivation chain. The eleven INCOMPLETE entries above are the exact gaps that would
have to be closed (or explicitly re-scoped as axioms) for the extension claim to hold deductively.

*Ledger compiled 2026-09-21 from the files cited above. Not from memory.*
