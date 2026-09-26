# Euclid's Elements — Book 13: Extension Proof Ledger

Worker: Book 13 campaign (subagent 45a16709). Written 2026-09-21 from direct reads of
`~/workspace/euclid_work/text/book13.txt` (Fitzpatrick/Heiberg, pp. 505–538), the
Encyclopedia.com Euclid biography (`~/workspace/user/files/euclid-encyclopedia-article.html`),
the TESS-India trigonometry unit, and the R Theory rewrite series (`~/workspace/r-theory-rewrite/`,
books 0–22) plus `~/workspace/vol4/NOTATION_LEDGER.md` and `~/workspace/vol4/DEPENDENCY_CHAIN.md`.

## Book summary

Book 13 is the culmination of the Elements: the construction of the five regular ("Platonic")
solids inscribed in a given sphere, with the edge of each figure determined in relation to the
circumscribing sphere's diameter. Per the encyclopedia article, the solid-construction theorems —
especially those for the last two solids — are ascribed to **Theaetetus of Athens**; Proclus reports
Euclid "perfected many of Theaetetus'" theorems, and the article notes Euclid (as a Platonist)
"would have derived pleasure from making the Elements end with the construction of the five
regular solids." The mathematical problem of the book is: determine the edge of each figure in
relation to the radius of the circumscribing sphere. For the pyramid, octahedron, and cube Euclid
evaluates the edge numerically in terms of the diameter; for the icosahedron and dodecahedron he
shows the edge is one of the Book-10 irrational lines — a **minor** (icosahedron) and an
**apotome** (dodecahedron).

The book's architecture (TESS-India framing: Book 13 is where *shape/space* meets *ratio,
deduction, and mathematical proof*):
- **13.1–13.6 — the extreme-and-mean-ratio (golden-section) lemma battery.** 13.1–13.5 are
  identities about a line cut in extreme and mean ratio (EMR); 13.6 places the pieces in Book 10's
  irrational classification (both pieces are apotomes when the line is rational).
- **13.7–13.12 — pentagon/decagon lemmas.** Pentagon angle/diagonal theory (13.7, 13.8), the
  hexagon+decagon EMR identity (13.9), pentagon² = hexagon² + decagon² (13.10), the pentagon
  side as a "minor" irrational (13.11), the inscribed equilateral triangle (13.12).
- **13.13–13.17 — the five solids**, each constructed and enclosed in a given sphere:
  pyramid/tetrahedron (13.13), octahedron (13.14), cube (13.15), icosahedron (13.16),
  dodecahedron (13.17).
- **13.18 — comparison**: the five edges set out side by side and compared.

**Definitions / postulates / common notions in Book 13: none.** Book 13 introduces no
definitions, postulates, or common notions of its own (verified by full-text scan). It cites
earlier-book definitions only: Def. 6.3 (extreme and mean ratio), Def. 10.4 (rational square),
Def. 10.14 (fourth apotome), Def. 11.3 (line at right angles to a plane), Def. 11.11 (solid
angle), Def. 5.9 (duplicate ratio).

**Full-text search result (R Theory side):** a case-insensitive search of all 23 rewrite book
pages (`book0/`–`book22/`) for *golden ratio, extreme and mean ratio, apotome, pentagon,
dodecahedron, icosahedron, "minor" irrational* returns **zero hits**. Searched 2026-09-21;
the rewrite corpus contains no EMR/golden-section machinery, no pentagon theory, and no
cube/icosahedron/dodecahedron constructions. (Note: the rewrite series' own "Book 13" is the
Volume II thermodynamic/statistical book — a name collision with Euclid's Book 13, with no
mathematical relation.)

The only R Theory solid-geometry counterparts are in Book 4 §4.V: the regular tetrahedron
(P0–P4) and regular octahedron (P5), built independently from R Theory's own solid postulates
— plus Book 0's tetrahedral carrier retained as declared geometric data. R Theory does **not**
inscribe these in a sphere and does **not** establish Euclid's edge–diameter ratios.

---

## Proposition inventory

Scope labels apply to the **R Theory extension claim** only, never to Euclid's own result
(which stands proved inside the Elements). Labels per Kit's standard:
PROVED = deductive proof shown; CHECKED = completed computation; ASSERTED = manuscript
stipulation / new axiom; INCOMPLETE = not established (reason given).

| No. | Statement (one line) | Euclid proof dependencies | R Theory extension | Scope |
|---|---|---|---|---|
| 13.1 | EMR cut: (greater piece + half of whole)² = 5·(half of whole)² | Def. 6.3, 6.17, 6.1, 1.43 | none — no EMR machinery in the corpus (full-text search, zero hits) | INCOMPLETE — not attempted; absent from the corpus |
| 13.2 | Converse: if AB² = 5·AC² and 2·AC cut EMR, the greater piece is the remaining part of AB | 6.1, 1.43, 6.17, 5.14 | none | INCOMPLETE — not attempted; absent from the corpus |
| Lemma (after 13.2) | In the 13.2 figure, double AC > BC (reduces to 2.4 impossibility) | 2.4 | none | INCOMPLETE — not attempted; absent from the corpus |
| 13.3 | EMR cut: (lesser piece + half of greater)² = 5·(half of greater)² | Def. 6.3, 6.17 | none | INCOMPLETE — not attempted; absent from the corpus |
| 13.4 | EMR cut: whole² + lesser² = 3·greater² | Def. 6.3, 6.17, 1.43 | none | INCOMPLETE — not attempted; absent from the corpus |
| 13.5 | EMR cut + greater piece adjoined: whole is again cut EMR, original line = greater piece | Def. 6.3, 6.17, 1.43, 5.14 | none | INCOMPLETE — not attempted; absent from the corpus |
| 13.6 | Rational line cut EMR → both pieces are apotomes | 13.1, 10.6, Def. 10.4, 10.9, 10.73, Def. 6.3, 6.17, 10.97 | none — Book 10 irrational taxonomy unused by R Theory | INCOMPLETE — not attempted; absent from the corpus |
| 13.7 | Equilateral pentagon with three equal angles (consecutive or not) is equiangular | 1.4, 1.6, 1.8, 1.5 | none | INCOMPLETE — not attempted; absent from the corpus |
| 13.8 | Diagonals of a regular pentagon cut each other EMR; greater pieces = pentagon sides | 4.14, 1.4, 1.32, 3.28, 6.33, 1.6, 1.5, 6.4, 5.14 | none | INCOMPLETE — not attempted; absent from the corpus |
| 13.9 | Hexagon side + decagon side (same circle), joined end to end, are cut EMR at the junction; greater piece = hexagon side | 3.1, 6.33, 1.5, 1.32, 4.15 (cor.), 6.4, 5.14 | none | INCOMPLETE — not attempted; absent from the corpus |
| 13.10 | Pentagon² = hexagon² + decagon² (same circle) | 3.1, 1.5, 3.26, 6.33, 1.32, 6.4, 6.17, 1.4, 3.29, 2.2, 4.15 | none | INCOMPLETE — not attempted; absent from the corpus |
| 13.11 | Pentagon in a rational-diameter circle → side is the "minor" irrational | 3.1, 1.4, 1.32, 6.4, 5.18, 13.8, 13.1, 10.9, 10.73, 10.15, 10.12, 5.19, Def. 10.14, 10.94, 6.8 | none | INCOMPLETE — not attempted; absent from the corpus |
| 13.12 | Inscribed equilateral triangle: side² = 3·radius² | 4.2, 3.1, 4.15, 3.31, 1.47 | none for the radius relation; planar equilateral-triangle construction exists separately (Book 4 §4.IV.P1, CP) but is not the inscribed-radius claim | INCOMPLETE — the radius relation is not attempted |
| 13.13 | Construct regular pyramid (tetrahedron) in a given sphere; sphere diameter² = 3/2 · pyramid side² | 6.10, 4.2, 3.1, 11.12, Def. 11.3, 1.4, 13.12, 6.8, 6.17, 3.31 | **Constructibility:** Book 4 §4.V P0–P4 — regular tetrahedron from equal spheres on an equilateral face; Gram matrix G₃, spectrum {2, 1/2, 1/2}, det = r⁶/2, edges = r, altitude r√(2/3), volume r³/(6√2). **Sphere-inscription and the diameter ratio:** no counterpart | PROVED (constructibility: CP construction + independent exact re-verification V12: (4I−J)(2G₃) = 4I, spectrum/det/edges/altitude/volume all re-verified exactly for the rewrite) / CHECKED (the Gram numerics are completed exact computations) ; **INCOMPLETE** for the sphere diameter² = 3/2·side² relation — not attempted |
| Lemma (after 13.13) | In the semicircle figure, AB:BC = AD²:DC² (DC is the mean proportional) | 6.8, 6.4, 6.17, 6.1, 6.8 (cor.) | none — the lemma feeds only 13.13's ratio claim, which has no R Theory counterpart | INCOMPLETE — not attempted |
| 13.14 | Construct regular octahedron in a sphere; diameter² = 2·side² | 11.12, Def. 5.9, 1.47, 1.4, 3.31, 6.8 | **Constructibility:** Book 4 §4.V P5 — "six specified flower-lattice points form a regular octahedron." **Sphere-inscription and the diameter ratio:** no counterpart | PROVED (constructibility, CP) ; **INCOMPLETE** for diameter² = 2·side² — not attempted |
| 13.15 | Construct cube in a sphere; diameter² = 3·side² | 11.4, Def. 11.3, Def. 5.9, 1.47, 6.8 | none — no cube construction in the corpus | INCOMPLETE — not attempted; absent from the corpus |
| 13.16 | Construct icosahedron in a sphere; side is the "minor" irrational | 6.10, 4.11, 11.6, 1.33, 13.10, 3.1, Def. 11.3, 1.29, 4.15, 13.9, 6.8, 3.31, 13.3, Def. 5.9, 13.11 | none — no icosahedron in the corpus | INCOMPLETE — not attempted; absent from the corpus |
| Corollary (after 13.16) | Sphere diameter² = 5·(icosahedron base-circle radius)²; diameter = hexagon side + 2·decagon sides | (immediate from 13.16) | none | INCOMPLETE — not attempted |
| 13.17 | Construct dodecahedron in a sphere; side is an apotome | 13.4, 1.47, 11.6, 6.32, 11.1, Def. 11.3, 13.5, 1.8, 13.7, 11.38, 13.15, 5.15, 5.14 | none — no dodecahedron in the corpus | INCOMPLETE — not attempted; absent from the corpus |
| Corollary (after 13.17) | Dodecahedron side = greater piece of the cube side cut EMR | (immediate from 13.17) | none | INCOMPLETE — not attempted |
| 13.18 | Set out the five solids' sides and compare them with one another | Def. 5.9, 6.8, 13.13, 13.15, 13.14, 6.4, 1.47, 13.16, 4.15, 13.10, 13.17, 6.20, 13.9, Def. 11.11, 11.21 | none — comparison presupposes the five constructions and EMR machinery, none of which the corpus carries | INCOMPLETE — not attempted |
| Lemma (after 13.18) | Regular pentagon angle = 1 + 1/5 right angles | 4.14, 3.1, 1.4, 1.32 | none | INCOMPLETE — not attempted; absent from the corpus |

**Bottom line on the extension map:** R Theory extends exactly two of Book 13's eighteen
propositions — the constructibility half of 13.13 (tetrahedron) and of 13.14 (octahedron) —
and it does so by *independent reconstruction* from its own solid postulates, not by
derivation from Euclid's chain (per Book 4 §4.X "No-Euclid-wholesale theorem" 4.X.H, Euclid is
not imported wholesale). The sixteen other propositions, all three lemmas, both corollaries,
the Book 10 irrational classifications (apotome/minor), the golden-section machinery, and the
sphere–edge ratio relations have no R Theory counterpart.

---

## New axioms / definitions beyond Euclid (load-bearing assumptions)

These are admitted in the R Theory corpus to carry the constructions above. Wording is quoted
verbatim from the rewrite pages; tags are the corpus's own (AA = admitted axiom/data layer,
CP = certified proof, MA = manuscript assertion, CN/CS = completed numeric/symbolic checks).

1. **Solid postulates S1–S6** (Book 4 §4.V, AA — "admitted explicitly"): (S1) noncoplanar
   extension, (S2) plane determination, (S3) perpendicular to a plane, (S4) sphere
   construction, (S5) equal-sphere intersection, (S6) rigid solid congruence. The corpus states
   the third direction "is not a planar consequence." These play the role Euclid's Book 11
   definitions/postulates play for 13.13–13.17, but they are R Theory's own, not Euclid's.
2. **P4.1 / P4.1-C / P4.3** (imported premises, AA): the pre-metric substrate and SSS
   congruence (P4.1, P4.1-C), and the global Euclidean declaration (P4.3) — "global flatness
   and unique parallels need the separate declaration P4.3."
3. **Gate B** (Book 4 §4.IV, AA): "Metric introduced only after the synthetic right angle" —
   a methodological postulate ordering the synthetic/metric layers.
4. **Flower-role lock** (Book 4 §4.VI, AA): supplementary diagnostics (§4.VI, §4.VII) "may not
   be used as foundational premises" — a negative axiom constraining the dependency chain.
5. **No-Euclid-wholesale theorem 4.X.H**: Euclid is not imported as a block; geometry is
   re-certified inside the corpus. (This is the declared reason the Book 13 chain is not
   inherited: the tetrahedron/octahedron are rebuilt, everything else is absent.)
6. **Book 0 retained-as-declared geometric data** (AA): "the tetrahedral carrier itself;
   discrete center lattice; simplicial refinement; dual complex; finite Hodge or mass matrices;
   variable triad; temporal covector (as pure coframe data); edge coframes; face holonomies."
   The corpus simultaneously states "R-SPECIFIC AXIOM COUNT ADDED: 0" — i.e., these are
   counted as retained declarations, not as new axioms; they remain stipulations the
   downstream theorems rest on, and are listed here so they are not hidden.
7. **The Flower re-presentation claim** (Book 4 §4.IV, MA): the audit labels as *manuscript
   assertion* the claim that the Flower plane re-presents Euclid's Books I–II, while the
   individual constructions (right angle P0, equilateral triangle P1, angle bisection,
   perpendicular P2–P3) are each CP. The tetrahedron/octahedron constructions rest on the CP
   constructions; identification of those with Euclid's Book 1 results rests on the MA claim.
   The independent exact re-verifications (V12 Gram identity, spectrum, determinant, edges,
   altitude, volume — all CP/CS re-verified for the rewrite) do not depend on the
   re-presentation claim.

No other new axioms or definitions are introduced by the Book 13 extension: in particular, no
new definition of irrational lines, no golden-ratio constant, no sphere-inscription postulate,
and no axiom covering cubes, icosahedra, or dodecahedra.

## Caveats and open questions

- The "no counterpart" verdicts for 13.1–13.12 and 13.15–13.18 rest on a full-text search of
  the 23 rewrite book pages plus the vol4 ledgers (2026-09-21). A proposition could in
  principle be used implicitly without its name appearing; no such implicit use was found.
- Euclid's own propositions are proved within the Elements; every INCOMPLETE label above
  concerns only the R Theory extension claim, not Euclid's result.
- The sphere–edge ratio relations (13.13's d² = 3/2·s², 13.14's d² = 2s²) and the
  icosahedron/dodecahedron classifications are the largest unextended portion of the book;
  extending them would require a sphere-inscription construction R Theory does not currently
  attempt.
- Book 13's role in Euclid is terminal (the Elements ends with the solids); in R Theory the
  tetrahedron/octahedron serve instead as the rank-three spatial carrier (Book 0 T3 → M4),
  so the extension re-purposes the solids rather than completing Euclid's arc.
