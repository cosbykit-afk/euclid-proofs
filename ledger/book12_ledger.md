# Euclid's Elements — Book 12: Extension Proof Ledger

Worker: Book 12 campaign (subagent e97e9138). Written 2026-09-21 from direct reads of
`~/workspace/euclid_work/text/book12.txt` (Fitzpatrick/Heiberg, pp. 471–503), the
Encyclopedia.com Euclid biography (`~/workspace/user/files/euclid-encyclopedia-article.html`),
the TESS-India trigonometry unit (17 pp.), and the R Theory rewrite series
(`~/workspace/r-theory-rewrite/`, books 0–22 plus vol0/vol4) plus
`~/workspace/vol4/NOTATION_LEDGER.md` and `~/workspace/vol4/DEPENDENCY_CHAIN.md`.

## Book summary

Book 12 is the **Eudoxan exhaustion book**: proportional stereometry — the areas and volumes
of circles, pyramids, prisms, cones, cylinders, and spheres, proved by the so-called method of
exhaustion (inscription of successive figures, resting on the axiom of 10.1). The
encyclopedia article attributes this body of results to **Eudoxus of Cnidus**: Book XII
"applies the method of exhaustion, that is, the inscription of successive figures in the
body to be evaluated, in order to prove that circles are to one another as the squares on
their diameters, that pyramids of the same height with triangular bases are in the ratio
of their bases, that the volume of a cone is one-third of the cylinder which has the same
base and equal height, that cones and cylinders [are in ratio], ..." — i.e. 12.2, 12.5,
12.10, 12.11–12.15, and (via 12.16–12.17) the spheres theorem 12.18. (TESS-India framing:
Book 12 is Euclid's most *creative-deductive* book — a constructive idea, repeated
inscription, turned into a proof engine, the precursor of integration.)

The book's architecture:
- **12.1–12.2 — circles.** 12.1: similar inscribed polygons ∝ squares on diameters (a
  purely Book-6/3 triangle argument). 12.2: circles themselves ∝ squares on diameters, by
  exhaustion (inscribe squares, bisect the residual arcs repeatedly — "cutting the
  circumferences remaining behind in half ... and always doing this"), double reductio ad
  absurdum, plus a ratio-inversion **lemma** (after 12.2).
- **12.3–12.6 — pyramids.** 12.3: the pyramid-bisection construction (triangular-base
  pyramid splits into two equal-and-similar smaller pyramids plus two equal prisms,
  the prisms exceeding half the whole). 12.4 + a **lemma** (prism : prism = base :
  base): the prisms of two divided equal-height pyramids are as the bases. 12.5:
  equal-height triangular-base pyramids ∝ their bases, by exhaustion on the division of
  12.3. 12.6: the same for polygonal bases.
- **12.7–12.9 — prism/pyramid relations.** 12.7: any triangular-base prism divides into
  three equal triangular pyramids; **corollary:** any pyramid is the third part of the
  prism on the same base and height. 12.8: similar triangular-base pyramids ∝ cubed
  (triplicate) ratio of corresponding sides; **corollary:** the same for polygonal-base
  similar pyramids. 12.9: equal pyramids ↔ bases reciprocal to heights.
- **12.10–12.15 — cones and cylinders.** 12.10: every cone is a third of the cylinder
  on the same base and equal height (exhaustion using 12.2 + 12.7 cor.). 12.11:
  same-height cones/cylinders ∝ bases. 12.12: similar cones/cylinders ∝ cubed ratio
  of base diameters. 12.13: a plane parallel to the bases cuts a cylinder in the ratio
  of the axes. 12.14: equal-base cones/cylinders ∝ heights. 12.15: equal cones/cylinders
  ↔ bases reciprocal to heights.
- **12.16–12.18 — spheres.** 12.16: inscribe an equilateral even-sided polygon in the
  greater of two concentric circles without touching the lesser (the exhaustion-enabler
  for the sphere). 12.17: inscribe a polyhedral solid in the greater of two concentric
  spheres without touching the lesser sphere's surface; **corollary:** similar inscribed
  polyhedra ∝ cubed ratio of the sphere diameters. 12.18: spheres ∝ cubed ratio of
  their diameters, by exhaustion, closing the book.

**Definitions / postulates / common notions in Book 12: none.** Book 12 introduces no
definitions, postulates, or common notions of its own (verified by full-text scan). It
cites earlier-book definitions only: Def. 6.1 (similar figures), Def. 11.9 (equal-height
solids), Def. 11.10, Def. 11.24 (similar solids), Def. 11.14, Def. 11.4, Def. 11.3
(perpendicular to a plane), Def. 3.1 (equal circles), Def. 3.28 (equal circumferences),
Def. 5.5, Def. 5.9 (duplicate ratio).

**Full-text search result (R Theory side):** a case-insensitive search of all 23 rewrite
book pages (`book0/`–`book22/`) plus `vol0/` and `vol4/` for *exhaustion, Eudoxus,
method of exhaustion, inscribed polygon, one-third of the cylinder, third part of the
prism, cubed ratio of, duplicate ratio, quadrature, circumference, ball volume* returns
**zero hits** on every term that names Book 12's machinery (2026-09-21). The "exhaustion"
and "quadrature" hits elsewhere are unrelated (legal/organizational text, oscillator
quadratures). (Note: the rewrite series' own "Book 12" is the Volume II two-particle /
block-projector notation book — a name collision with Euclid's Book 12, with no
mathematical relation.) The vol4 ledgers likewise contain no Euclid citation at all
(only §0.12 two-particle and §4.XII frame-change notation collisions).

**The only R Theory adjacency** is Book 4 §4.V: the regular tetrahedron carries an
exactly-computed volume V<sub>tet</sub> = r³/(6√2) (CP, from the Gram form — exact
linear algebra, not exhaustion). The corpus never states or uses 12.7 (pyramid = third
of prism), never invokes 10.1, and never runs an exhaustion argument. A computed
tetrahedron volume is not an extension of the exhaustion theorems.

---

## Proposition inventory

Scope labels apply to the **R Theory extension claim** only, never to Euclid's own result
(which stands proved inside the Elements). Labels per Kit's standard:
PROVED = deductive proof shown; CHECKED = completed computation; ASSERTED = manuscript
stipulation / new axiom; INCOMPLETE = not established (reason given).

| No. | Statement (one line) | Euclid proof dependencies | R Theory extension | Scope |
|---|---|---|---|---|
| 12.1 | Similar polygons inscribed in circles are to one another as the squares on the diameters | Def. 6.1, 6.6, 3.27, 3.31, 1.32, 6.4, 6.20 | none — no inscribed-polygon ratio machinery in the corpus (full-text search, zero hits) | INCOMPLETE — not attempted; absent from the corpus |
| Lemma (after 12.2) | If S > circle B then circle A : circle B = S : T for some T < circle A (ratio inversion) | 5.16, 5.14 | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.2 | Circles are to one another as the squares on their diameters (exhaustion via repeated arc-bisection) | 4.6, 1.47, 10.1, 12.1, 5.11, 5.16, 5.7 cor., 5.14 | none — the corpus has no circle-area theory, no 10.1 axiom, no exhaustion argument | INCOMPLETE — not attempted; absent from the corpus |
| 12.3 | Any triangular-base pyramid divides into two equal-and-similar-to-whole pyramids + two equal prisms, the prisms exceeding half the whole | 6.2, 1.34, 1.29, 1.4, 11.10, Def. 11.10, Def. 6.1, 6.6, Def. 11.9, 1.41, 11.39 | none — no pyramid division in the corpus | INCOMPLETE — not attempted; absent from the corpus |
| Lemma (in 12.4) | Equal-height prisms are to one another as their (triangular) bases | 11.17, 11.32, 11.28 | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.4 | Two equal-height triangular-base pyramids, each divided per 12.3: base : base = (all) prisms : (all) prisms | 12.3, 6.22, 5.16, 5.12, 11.17, 11.32, 11.28 | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.5 | Equal-height triangular-base pyramids are to one another as their bases (exhaustion) | 12.3, 10.1, 12.4, 5.11, 5.16, 5.14, 5.7 cor., 12.2 lemma | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.6 | Equal-height polygonal-base pyramids are to one another as their bases | 12.5, 5.18, 5.22 | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.7 | Any prism having a triangular base is divided into three equal triangular-base pyramids | 1.34, 12.5 | none — no prism decomposition in the corpus | INCOMPLETE — not attempted; absent from the corpus |
| Corollary (of 12.7) | Any pyramid is the third part of the prism having the same base and equal height | (immediate from 12.7) | none — the corpus never states or uses this; the adjacent V<sub>tet</sub> = r³/(6√2) (Book 4 §4.V P4, CP from the Gram form) is an independent exact computation, not derived from nor invoking this corollary | INCOMPLETE — the third-of-prism claim is not attempted; the Gram volume is adjacent, not an extension |
| 12.8 | Similar pyramids with triangular bases are in the cubed (triplicate) ratio of their corresponding sides | Def. 11.9, 11.24, 11.33, 11.28, 12.7, 6.20, 5.12 | none — no triplicate-ratio machinery in the corpus (full-text search, zero hits) | INCOMPLETE — not attempted; absent from the corpus |
| Corollary (of 12.8) | Similar pyramids with polygonal bases are in the cubed ratio of their corresponding sides | 12.8 (immediate) | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.9 | Equal triangular-base pyramids: bases are reciprocally proportional to heights, and conversely | 11.34, 1.34, 5.11 | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.10 | Every cone is the third part of the cylinder having the same base and equal height (exhaustion) | 4.6, 12.2, 4.7, 11.32, 10.1, 12.7 cor. | none — the corpus has no cones, no cone/cylinder volume theory | INCOMPLETE — not attempted; absent from the corpus |
| 12.11 | Cones and cylinders of the same height are to one another as their bases | 4.6, 12.2, 4.7, 12.6, 12.10, 10.1, 6.18, 12.1, 5.11, 5.16, 5.14, 5.7 cor., 12.2 lemma | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.12 | Similar cones and cylinders are in the cubed ratio of the diameters of their bases | 4.6, 12.2, 12.10, 10.1, 6.18, Def. 11.24, 5.16, 6.6, Def. 6.1, 5.22, 6.5, Def. 11.9, 12.8, 5.12, 5.7 cor. | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.13 | A cylinder cut by a plane parallel to its opposite planes: cylinder : cylinder = axis : axis | 12.11, Def. 5.5 | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.14 | Cones and cylinders on equal bases are to one another as their heights | 12.11, 12.13, 12.10 | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.15 | Equal cones and cylinders: bases are reciprocally proportional to heights, and conversely | 12.11, 5.7, 12.13, 5.11, 5.9 | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.16 | Inscribe an equilateral even-sided polygon in the greater of two concentric circles, not touching the lesser | 3.16 cor., 10.1, 1.28, 4.1 | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.17 | Inscribe a polyhedral solid in the greater of two concentric spheres, not touching the lesser sphere's surface | Def. 11.14, 3.15, 12.16, 11.18, Def. 3.1, 11.11, Def. 11.4, Def. 3.28, 6.2, 11.6, 1.33, 11.1, 11.7, 11.2, Def. 11.3, 1.47, 12.8 cor., 5.12 | none — the corpus has no sphere-inscription construction (contrast Book 13: tetrahedron/octahedron are built, not inscribed in a sphere) | INCOMPLETE — not attempted; absent from the corpus |
| Corollary (of 12.17) | Similar polyhedral solids inscribed in spheres are in the cubed ratio of the sphere diameters | 12.8 cor., 5.12 (immediate from 12.17) | none | INCOMPLETE — not attempted; absent from the corpus |
| 12.18 | Spheres are to one another in the cubed ratio of their diameters (exhaustion) | 12.17, 12.17 cor., 5.16, 5.14, 5.7 cor., 12.2 lemma | none — no sphere-volume or cubed-ratio theory in the corpus | INCOMPLETE — not attempted; absent from the corpus |

**Bottom line on the extension map:** R Theory extends **none** of Book 12's eighteen
propositions, two lemmas, or three corollaries. The method of exhaustion, the 10.1 axiom,
circle-area ratios, pyramid/cone volume ratios, triplicate ratios, and sphere ratios are
all absent from the rewrite corpus — verified by full-text search of all 23 book pages
plus vol0/vol4 (2026-09-21). The single adjacency, Book 4's exact Gram-form computation
of the regular tetrahedron's volume V<sub>tet</sub> = r³/(6√2) (CP), is computed by
independent linear algebra and neither states, uses, nor implies 12.7's pyramid-third
relation. Per Kit's calculation priority (proving-ground first), the corpus rebuilds only
the constructions its own theorems need (Book 4's solid postulates S1–S6); ratio/volume
theory of the Book-12 kind is not on the proving-ground queue, and this is not a gap
being worked.

---

## New axioms / definitions beyond Euclid (load-bearing assumptions)

**For Book 12 specifically: none.** Because R Theory makes no extension claim on any
Book 12 proposition, it introduces no new axiom, definition, or postulate to carry Book
12 content. There are no Book-12 extension axioms to list, and the ledger does not
manufacture any.

The adjacent geometric content (Book 4 §4.V, the only R Theory material in Book 12's
subject area) rests on load-bearing assumptions documented verbatim in the Book 13
ledger's §7, which are referenced — not duplicated — here so they stay in one place:

1. **Solid postulates S1–S6** (Book 4 §4.V, AA — "admitted explicitly"): noncoplanar
   extension, plane determination, perpendicular to a plane, sphere construction,
   equal-sphere intersection, rigid solid congruence. Note: these authorize
   *constructions* (including the tetrahedron whose volume is computed); they do not
   authorize exhaustion, limits, or volume ratios.
2. **P4.1 / P4.1-C / P4.3** (imported premises, AA): pre-metric substrate, SSS
   congruence, and the global Euclidean declaration.
3. **Gate B** (Book 4 §4.IV, AA): metric introduced only after the synthetic right angle.
4. **Flower-role lock** (Book 4 §4.VI, AA): supplementary diagnostics may not be used as
   foundational premises.
5. **No-Euclid-wholesale theorem 4.X.H**: Euclid is not imported as a block. This is
   the declared reason no Book-12 result is inherited: the corpus carries neither the
   10.1 axiom nor the exhaustion chain, and does not claim them.
6. **Book 0 retained-as-declared geometric data** (AA): tetrahedral carrier, discrete
   center lattice, simplicial refinement, dual complex, finite Hodge/mass matrices —
   counted by the corpus as "R-SPECIFIC AXIOM COUNT ADDED: 0", i.e. stipulations, not
   new axioms, but listed so they are not hidden.

Also explicitly noted so as not to be hidden: the "jinc | Bessel jinc, conditional on
uniform Euclidean disk measure" entry in the Book 19 audit ledger (§19.4, CONDITIONAL)
touches *disk measure*, the only corpus item within shouting distance of circle-area
theory — but it is a self-labeled conditional inside the Volume I manuscript audit, not
an extension of 12.2, and it does not appear in the rewrite series pages at all.

## Caveats and open questions

- The "no counterpart" verdicts rest on a full-text search of the 23 rewrite book pages
  plus vol0/vol4 and both vol4 ledgers (2026-09-21). A proposition could in principle be
  used implicitly without its name appearing; no such implicit use was found (in
  particular, no exhaustion-style bisection-and-limit argument occurs anywhere).
- Euclid's own propositions are proved within the Elements; every INCOMPLETE label above
  concerns only the R Theory extension claim, not Euclid's result.
- Book 12 is the only one of the final three solid-geometry books (XI–XIII) that R
  Theory does not extend at all: Book 11's constructions are partially re-certified via
  S1–S6, Book 13's tetrahedron/octahedron constructions are rebuilt (CP) — but the
  exhaustion engine of Book 12 has no counterpart, and the proving-ground queue does
  not call for one. If sphere/circle volume ratios ever enter the proving ground, 10.1
  and the exhaustion machinery would be new axioms to admit explicitly; at present
  nothing requires them.
- The encyclopedia article's Book XII description (Eudoxan exhaustion for circles,
  pyramids, cones, cylinders) is the historical framing used here; the TESS-India unit's
  creative-deductive framing (linking shape/space with ratio, deduction, and proof)
  applies directly to 12.2/12.5/12.10/12.18's repeated-inscription arguments, but no
  corresponding constructive-deductive step exists in the R Theory corpus to cite —
  which is itself the finding.
