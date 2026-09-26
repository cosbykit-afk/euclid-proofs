# Book 11 Ledger — Euclid Extension Proof Campaign

**Source:** `/home/hatch/workspace/euclid_work/text/book11.txt` (Fitzpatrick/Heiberg English
translation, with Greek; pages 423–468 of the edition).
**R Theory side read:** `/home/hatch/workspace/r-theory-rewrite/book0/`–`book22/`
(index.html pages), `manuscript/R-Theory-Volume-I-original.txt` (Book 4 §§4.V, 4.X, 4.XI, 4.XII, 4.XIII),
`/home/hatch/workspace/vol4/NOTATION_LEDGER.md` (S1–S6, P4.1/P4.1-C/P4.3, G₃ rows),
`/home/hatch/workspace/vol4/DEPENDENCY_CHAIN.md`.
**Historical context:** encyclopedia.com biography of Euclid — the final three books (XI–XIII)
are devoted to solid geometry; Book XI "deals largely with parallelepipeds."
**Framing note:** the TESS-India paper's theme (linking shape/space with ratio, deduction, and
proof) is the same move the extension makes: Book 4's solid stage certifies its canonical cell
by *ratio* (the tetrahedral Gram matrix G₃, its spectrum {2, ½, ½}, det = r⁶/2) rather than by
synthetic solid-angle theory.

## Book summary

**Subject.** Book 11 is Euclid's elementary stereometry: 28 definitions (solid, surface,
line⊥plane, plane⊥plane, line–plane and plane–plane inclination, parallel planes, similar
and equal-similar solids, solid angle, pyramid, prism, sphere with axis/center/diameter,
cone and its three species, cylinder with axis/bases, similar cones/cylinders, and the five
regular solids as bounded figures) and 39 propositions in three blocks:

- 11.1–11.19: solid-geometric foundations — a straight line is wholly in one plane (11.1);
  intersecting lines and triangles lie in one plane (11.2); the section of two planes is a
  straight line (11.3); the perpendicularity/parallelism apparatus for lines and planes
  (11.4–11.19).
- 11.20–11.23: solid angles — the triangle inequality for three plane angles of a trihedral
  angle (11.20), the < 4-right-angle bound (11.21), the triangle-construction lemma (11.22),
  and the construction of a solid angle from three given plane angles (11.23).
- 11.24–11.39: the parallelepiped block (11.24–11.37, minus 11.35) — equality of opposite
  faces, section ratios, base×height volume theory, triplicate (cubed) ratio for similar
  solids; plus 11.35 (the "raised lines on equal angles" prism lemma), 11.38 (cube mid-plane
  bisection), 11.39 (prism from double base).

**Headline result of the extension mapping.** R Theory does not cite, reprove, or build on any
of 11.1–11.39 individually (full-text search of the Volume I source manuscript and all
rewrite pages 0–22 finds zero references to Euclid XI proposition numbers). The theory's
whole position on this territory is stated in Book 4:

- **The No-Euclid-wholesale theorem (4.X.P10):** "The starting data P4.1 do not contain a
  real-valued distance between arbitrary point pairs, a dot product, Cartesian coordinates,
  numerical angles, the parallel postulate, the Pythagorean theorem, or global flatness…
  Therefore Revised Book 4 does not accept Euclidean metric geometry wholesale before the
  Flower construction." (Rewrite book4 page, §4.X — section tagged MA, manuscript
  assertion; the isometry identity behind 4.X.I additionally re-verified, CN.)
- **The plane→solid passage is replaced by explicitly admitted declarations** S1–S6 plus
  P4.4 (§4.XIII.D "Solid-extension audit"), from which Book 4 §4.V proves only a
  *canonical-cell* solid geometry: the regular tetrahedron (4.V.P0, CP) and regular octahedron
  (4.V.P5, CP) from equal-sphere constructions, with all metric facts (edges, altitude
  r√(2/3), volume r³/(6√2), Gram spectrum {2, ½, ½}, det = r⁶/2) verified exactly
  (V6–V12; e.g. (4I−J)(2G₃) = 4I exactly).

Consequence for every row below: where the theory has no counterpart claim, the scope label
is INCOMPLETE with the reason stated; where the admitted substrate would *cover* a Euclid
result without the theory stating it, the column says so and the label stays INCOMPLETE
(never upgraded to ASSERTED, because the manuscript does not stipulate the Euclid
proposition itself).

**Editorial notes in the source (logical hygiene):**
- Footnote to 11.1: "The proofs of the first three propositions in this book are not at all
  rigorous. Hence, these three propositions should properly be regarded as additional axioms."
- Footnote to 11.34: "This proposition assumes that (a) if two parallelepipeds are equal,
  and have equal bases, then their heights are equal, and (b) if the bases of
  [two equal parallelepipeds are reciprocally proportional to the heights, then the solids
  are equal]" — i.e. 11.34 assumes unstated lemmas.
- Footnote to 11.37: "This proposition assumes that if two ratios are equal then the cube
  of the former is also equal to the cube of the latter, and vice versa."

**Definitions inventory (28).** Book 11 states 28 definitions and no new postulates/common
notions of its own (it uses the five postulates and five common notions from Book 1; 11.1–11.3
function as additional axioms per the note above).

| # | Definition (one line) | R Theory extension | Scope |
|---|---|---|---|
| D1 | A solid is (a figure) having length, breadth, and depth. | Replaced by declared rank-three carrier (G₃, metric h = H_ab θᵃ⊗θᵇ, §4.V/§4.XI); S1 (noncoplanar extension exists) is the explicit admission that a solid stage is not a planar consequence. | ASSERTED (S1); metric facts CHECKED |
| D2 | The extremity of a solid is a surface. | Not redefined; surfaces enter as the Flower plane / declared global structure. | INCOMPLETE (no counterpart claim) |
| D3 | A straight line is at right angles to a plane when it makes right angles with all lines in the plane through the point. | Replaced by S3 (a perpendicular to a plane exists uniquely through a point, ASSERTED) + synthetic Flower right angle (4.IV.P0) + post-metric orthogonality (G₃ inner product, CP). | ASSERTED (S3); orthogonality facts CHECKED |
| D4 | A plane is at right angles to (another) plane when lines drawn ⊥ the common section in one plane are ⊥ the other plane. | No independent counterpart; covered only by the declared metric framework. | INCOMPLETE |
| D5 | Inclination of a line to a plane: angle between the line and the join of its foot to the dropped perpendicular's foot. | No counterpart claim. | INCOMPLETE |
| D6 | Inclination of a plane to a plane: the acute angle between lines drawn ⊥ the common section at one point, one in each plane. | No counterpart claim. | INCOMPLETE |
| D7 | Similarly inclined planes: those whose inclination angles (D6) are equal. | No counterpart claim. | INCOMPLETE |
| D8 | Parallel planes are those which do not meet. | No independent definition; "do not meet" is used inside admitted global completion P4.3. | INCOMPLETE |
| D9 | Similar solid figures: contained by equal numbers of similar planes (similarly arranged). | Similarity enters only via "similar parallelepiped" usage imported nowhere; no counterpart. | INCOMPLETE |
| D10 | Equal and similar solid figures: contained by similar planes equal in number and magnitude. | No counterpart claim. | INCOMPLETE |
| D11 | Solid angle: inclination of more than two non-coplanar lines meeting at a point; otherwise, contained by more than two non-coplanar plane angles meeting at one point. | Not reconstructed in general. The theory proves only the regular-tetrahedral case (trihedral angle with three 60° plane angles, 4.V.P0). | INCOMPLETE for general D11; regular case PROVED/CHECKED at 4.V.P0 |
| D12 | Pyramid: solid contained by planes, constructed from one plane to one point. | No counterpart claim. | INCOMPLETE |
| D13 | Prism: solid contained by planes, two opposite ones equal, similar, parallel, the rest parallelograms. | No counterpart claim (11.39's prism result has no extension either). | INCOMPLETE |
| D14 | Sphere: figure enclosed when a semicircle, diameter fixed, is carried round back to its start. | Constructive sphere: S4 (spheres of copied radius constructible) + S5 (three equal spheres on an equilateral Flower face meet in two points on opposite sides of the face plane) — the equal-sphere construction behind 4.V.P0. Euclid's rotational definition is not used. | ASSERTED (S4, S5); construction used in 4.V.P0 (CP) |
| D15 | Axis of the sphere: the fixed straight line about which the semicircle is turned. | No counterpart claim. | INCOMPLETE |
| D16 | Center of the sphere: the same as that of the semicircle. | Used implicitly in S4/S5 (centers at Flower-face vertices); not separately defined. | ASSERTED (via S4/S5) |
| D17 | Diameter of the sphere: any line through the center terminated both ways by the surface. | No counterpart claim. | INCOMPLETE |
| D18 | Cone: figure enclosed when a right triangle, one leg about the right angle fixed, is carried round back to its start; right-angled if the fixed leg equals the moving leg, obtuse-angled if less, acute-angled if greater. | No counterpart claim. | INCOMPLETE |
| D19 | Axis of the cone: the fixed straight line about which the triangle is turned. | No counterpart claim. | INCOMPLETE |
| D20 | Base of the cone: the circle described by the moving leg. | No counterpart claim. | INCOMPLETE |
| D21 | Cylinder: figure enclosed when a right-angled parallelogram, one side about the right angle fixed, is carried round back to its start. | No counterpart claim. | INCOMPLETE |
| D22 | Axis of the cylinder: the stationary line about which the parallelogram is turned. | No counterpart claim. | INCOMPLETE |
| D23 | Bases of the cylinder: circles described by the two opposite moving sides. | No counterpart claim. | INCOMPLETE |
| D24 | Similar cones and cylinders: those whose axes and base diameters are proportional. | No counterpart claim. | INCOMPLETE |
| D25 | Cube: solid contained by six equal squares. | No counterpart definition; cubes appear only as coordinate boxes in the coordinate audit (4.XIII.F), not as a constructed solid. | INCOMPLETE |
| D26 | Octahedron: solid contained by eight equal equilateral triangles. | Re-derived: Definition 4.V.A6 defines octahedron; 4.V.P5 proves six specified Flower-lattice points form a regular octahedron (CP). | PROVED (4.V.P5; base declarations S1–S6 ASSERTED) |
| D27 | Icosahedron: solid contained by twenty equal equilateral triangles. | No counterpart claim. | INCOMPLETE |
| D28 | Dodecahedron: solid contained by twelve equal equilateral equiangular pentagons. | No counterpart claim. | INCOMPLETE |

## Proposition inventory

Scope-label vocabulary (Kit's four-way scope): PROVED = deductive proof shown (base
declarations named); CHECKED = verified by a completed computation (computation described);
ASSERTED = manuscript stipulation or new axiom; INCOMPLETE = not established (reason given).

| # | Statement (one line) | Euclid proof dependencies | R Theory extension | Scope |
|---|---|---|---|---|
| 11.1 | No part of a straight line is in one plane and another part in a different plane (a line is wholly in the plane containing two of its points). | — (proof by circle construction; footnote: treat as additional axiom) | Subsumed in admitted P4.1 incidence substrate ("point/line construction substrate"), which the No-wholesale theorem (4.X.P10) explicitly lists as *inherited synthetic assumption*, not proved. | ASSERTED (as part of P4.1) |
| 11.2 | Two intersecting straight lines lie in one plane, and every triangle on them lies in one plane. | 11.1 | Plane determination is admitted as S2 (three noncollinear points determine one plane) for the solid stage; the intersecting-lines case is used inside P4.1 incidence. | ASSERTED (S2/P4.1); not independently proved |
| 11.3 | The common section of two intersecting planes is a straight line. | — (reductio via enclosed area; footnote: additional axiom) | Plane–plane section behavior enters only through declared global completion P4.3; no counterpart claim. | INCOMPLETE |
| 11.4 | A line set up ⊥ to two intersecting lines at their intersection is ⊥ to the plane through them. | 1.4, 1.8, 1.15, 1.26 | No counterpart. S3 admits perpendicular-to-a-plane existence/uniqueness outright rather than proving 11.4's criterion. | INCOMPLETE |
| 11.5 | A line set up ⊥ to three concurrent lines at their intersection implies the three lines are coplanar. | 11.4 | No counterpart claim. | INCOMPLETE |
| 11.6 | Two straight lines ⊥ to the same plane are parallel. | 1.28, 1.4, 1.8, 11.2, 11.5 | No counterpart claim. | INCOMPLETE |
| 11.7 | The join of two points, one on each of two parallel lines, lies in the same plane as the parallels. | 11.3 | No counterpart claim. | INCOMPLETE |
| 11.8 | If one of two parallel lines is ⊥ to a plane, so is the other. | 1.29, 1.4, 1.8, 11.2, 11.4, 11.7 | No counterpart claim. | INCOMPLETE |
| 11.9 | Lines parallel to the same line (not coplanar with it) are parallel to one another. | 11.4, 11.6, 11.8 | No counterpart claim. | INCOMPLETE |
| 11.10 | Angles contained by pairs of respectively parallel non-coplanar lines are equal. | 1.33, 1.8, 11.9 | No counterpart claim (angle transport in the Flower enters via sixfold sector structure P4.2-L, not via 11.10). | INCOMPLETE |
| 11.11 | Construction: drop a perpendicular from a raised point to a given plane. | 1.11, 1.12, 1.31, 11.4, 11.8 | Existence is admitted as S3 ("a perpendicular to a plane exists uniquely through a point") — the construction itself is not reproduced. | ASSERTED (S3); construction not proved |
| 11.12 | Construction: erect a perpendicular to a given plane at a given point of it. | 1.31, 11.11, 11.8 | Same as 11.11: admitted via S3, construction not reproduced. | ASSERTED (S3); construction not proved |
| 11.13 | Two distinct lines ⊥ to the same plane at the same point, on the same side, are impossible (uniqueness of the perpendicular). | 11.3 | Uniqueness is folded into S3 ("exists uniquely") by stipulation, not proved. | ASSERTED (S3); not proved |
| 11.14 | Planes to which the same line is ⊥ are parallel. | 1.17, 11.3 | No counterpart claim. | INCOMPLETE |
| 11.15 | Planes through respectively parallel non-coplanar line pairs are parallel. | 1.29, 1.31, 11.11, 11.14, 11.4, 11.9 | No counterpart claim. | INCOMPLETE |
| 11.16 | A plane cutting two parallel planes makes parallel sections. | 11.1 | No counterpart claim. | INCOMPLETE |
| 11.17 | Two lines cut by parallel planes are cut in the same ratios. | 11.16, 5.11, 6.2 | No counterpart claim. | INCOMPLETE |
| 11.18 | Every plane through a line ⊥ to a plane is itself ⊥ to that plane. | 1.11, 1.28, 11.8 | No counterpart claim. | INCOMPLETE |
| 11.19 | The common section of two intersecting planes, each ⊥ to a third plane, is ⊥ to that third plane. | 11.13 | No counterpart claim. | INCOMPLETE |
| 11.20 | A solid angle contained by three plane angles: any two exceed the third (taken any way). | 1.20, 1.25, 1.4 | Not established in general. Only the regular case is proved: 4.V.P0's trihedral angle has three 60° plane angles and all six edges = r (edge equality P3, CP from G₃). | INCOMPLETE (general); regular 60° case CHECKED via G₃ (see 4.V.P0) |
| 11.21 | Every solid angle is contained by plane angles summing to less than four right angles. | 1.32, 11.20 | Not established in general. Regular-tetrahedron instance only: three 60° angles sum to 180° < 360° (immediate from 4.V.P0 edge data). | INCOMPLETE (general); regular case CHECKED |
| 11.22 | Lemma: from three plane angles with the 11.20 property and equal containing lines, a triangle can be built on the joins of the equal lines. | 1.20, 1.24, 1.4 | Not established in general. The equilateral-face construction (P4.2-L sixfold completion + 4.X.P3 equilateral Flower triangle) is the special case actually used. | INCOMPLETE (general); equilateral case PROVED at 4.X.P3 |
| 11.23 | Construction of a solid angle from three given plane angles satisfying 11.20's condition. | 1.25, 1.29, 1.4, 1.47, 1.8, 11.12, 11.21, 11.22, 3.31, 4.1, 4.5, 5.14, 5.16, 6.2, 6.4 | Not established. The theory constructs one solid angle — the regular tetrahedron 4.V.P0 via S5's equal-sphere intersection — not the general 11.23 construction. | INCOMPLETE (general); regular case PROVED at 4.V.P0 |
| 11.24 | A solid contained by six parallel planes has opposite faces equal and parallelogrammic. | 1.34, 1.4, 11.10, 11.16 | No counterpart claim; parallelepiped theory is not rebuilt. | INCOMPLETE |
| 11.25 | A parallelepiped cut by a plane parallel to opposite faces is divided as base:base = solid:solid. | 11.24 | No counterpart claim. | INCOMPLETE |
| 11.26 | Construction of a solid angle equal to a given solid angle on a given line at a given point. | 1.23, 1.4, 1.8, 11.11, 11.12 | Not established in general; 4.V.P1 proves the two S5 intersection points give congruent tetrahedra on opposite sides of the face (CP) — a congruence result for the regular case only. | INCOMPLETE (general); regular-tetrahedron congruence PROVED at 4.V.P1 |
| 11.27 | Construction of a parallelepiped similar and similarly situated to a given one on a given line. | 11.26, 5.22, 6.12 | No counterpart claim. | INCOMPLETE |
| 11.28 | A parallelepiped cut by a plane through the diagonals of opposite faces is bisected by the plane. | 1.34, 11.24 | No counterpart claim. | INCOMPLETE |
| 11.29 | Parallelepipeds on the same base, same height, with uprights on the same lines, are equal. | 1.34, 1.36, 11.24 | No counterpart claim. General volume: 4.XII.P2 determinant law (θ′ = Aθ ⇒ vol′ = det(A)·vol, CP; CN re-verified over 1,999 random matrices) and 4.XII.P3 tetrahedral Flower volume (CP) are the theory's volume facts — neither proves 11.29. | INCOMPLETE |
| 11.30 | Same as 11.29 with uprights not on the same lines. | 11.29 | No counterpart claim. | INCOMPLETE |
| 11.31 | Parallelepipeds on equal bases with the same height are equal. | 1.23, 1.35, 11.24, 11.25, 11.29, 11.30, 5.11, 5.7, 5.9, 6.14 | No counterpart claim. | INCOMPLETE |
| 11.32 | Parallelepipeds of the same height are as their bases. | 1.45, 11.25, 11.31 | No counterpart claim. | INCOMPLETE |
| 11.33 | Similar parallelepipeds are in the triplicate (cubed) ratio of corresponding sides. | 11.24, 11.32, 6.1 | No counterpart claim. | INCOMPLETE |
| 11.34 | Equal parallelepipeds have bases reciprocally proportional to heights, and conversely. | 11.25, 11.31, 11.32, 5.7, 5.9, 6.1 (plus the footnote's two unstated lemmas) | No counterpart claim. | INCOMPLETE |
| 11.35 | Two equal plane angles with raised lines making respectively equal angles, and equal segments cut off: the joins and inclinations match (prism lemma). | 1.26, 1.4, 1.47, 1.48, 1.8, 11.8 | No counterpart claim. | INCOMPLETE |
| 11.36 | From three continuously proportional lines, the parallelepiped on the three equals the equilateral parallelepiped on the mean. | 11.23, 11.31, 6.14 | No counterpart claim. | INCOMPLETE |
| 11.37 | Four proportional lines ⇔ similar similarly-described parallelepipeds on them proportional (both directions). | 11.33 (plus the footnote's unstated cube-of-ratio lemma) | No counterpart claim. | INCOMPLETE |
| 11.38 | Mid-planes through a cube's opposite faces bisect each other and the cube's diameter. | 1.14, 1.15, 1.26, 1.29, 1.33, 1.4, 11.9 | No counterpart claim. | INCOMPLETE |
| 11.39 | Two equal-height prisms, one on a parallelogram base, one on a triangular base with the parallelogram double the triangle, are equal. | 1.34, 11.28, 11.31 | No counterpart claim. | INCOMPLETE |

## The genuinely established solid-geometry results (the extension's actual content)

These are the only solid-geometry results R Theory proves or checks. Everything else in
the 11.1–11.39 inventory above has no counterpart claim in the corpus.

1. **4.V.P0 — regular tetrahedron from equal spheres on an equilateral face (CP).** Three
   equal spheres (S4, S5) centered on the vertices of an equilateral Flower face meet in two
   points on opposite sides of the face plane; with the three face vertices these are the
   vertices of a regular tetrahedron. **Proof base:** S1 (a noncoplanar point exists),
   S4, S5 (both ASSERTED — see below), S6 (rigid solid congruence). **Exact metric facts
   (CHECKED, V6–V12 in NOTATION_LEDGER.md):** dimensionless Gram G₃/r² has spectrum
   {2, ½, ½}, det G₃ = r⁶/2 > 0 certifying linear independence of the three edge directions
   (4.XIII.P3 — "the third direction is neither hidden in the plane nor produced by
   Projection phase"); inverse certified exactly by (4I−J)(2G₃) = 4I; all six edges = r
   (4.V.P3); altitude OG = r√(2/3), DE = 2r√(2/3) (4.V.P4); volume r³/(6√2) (4.V.P4).
   This is the extension's substitute for the whole 11.20–11.23 solid-angle apparatus —
   one canonical trihedral angle instead of the general theory.
2. **4.V.P1 — the two S5 intersections give congruent tetrahedra on opposite sides (CP);**
   4.V.P2 — DE perpendicularly bisected by the base plane (CP).
3. **4.V.P5 — six specified Flower-lattice points form a regular octahedron (CP)**
   (Definition 4.V.A6; source manuscript lines 22888–22922). With 4.V.P6 the primitive
   Flower rhombohedron decomposes into two regular tetrahedra + one regular octahedron.
4. **4.XII.P2 — determinant transformation law** θ′ = Aθ ⇒ vol′ = (det A)·vol (CP;
   additionally CN re-verified over 1,999 random matrices). **4.XII.P3 — tetrahedral Flower
   volume (CP).** These are the theory's volume facts; they do not prove 11.29–11.34.
5. **4.XIII.P5 — Flower coordinates locally isometric to Cartesian after metric completion
   (CP).** Local Euclidean structure is recovered; global flatness and unique parallels
   require the separate declaration P4.3 (ASSERTED), per the 4.X postulate audit.

## NEW axioms/definitions introduced beyond Euclid (the load-bearing assumptions)

Exact wording from the source manuscript, Book 4 §4.XIII.C–D ("Foundation audit" and
"Solid-extension audit"). All are explicitly admitted, never derived — this is the point of
the No-Euclid-wholesale theorem (4.X.P10): "P4.1 and P4.1-C are genuine inherited synthetic
assumptions. The Flower does not derive incidence, segment congruence, compass transfer, or
SSS from nothing."

**Planar-stage declarations (used before any solid result):**
- **P4.1** — point/line construction substrate, segment congruence, compass transfer,
  intersection, and continuous triangular construction capacity. (NOTATION_LEDGER: CLEAN, AA)
- **P4.1-C** — SSS congruence principle: OB≅OC, BD≅CD, OD≅OD ⇒ ∠BOD=∠DOC
  (the admitted inference behind the Flower right-angle theorem 4.X.P2). (CLEAN, AA)
- **P4.2-L** — sixfold local completion: at every ordinary interior Flower center O, six
  congruent primitive Flower triangles meet cyclically without gap or overlap, and rays
  separated by three consecutive native sectors form one straight line.
- **P4.2-M** — real rank-two affine/vector realization, used only after the synthetic
  right-angle construction to formalize a bilinear metric.
- **P4.3** — global Euclidean completion: global flatness and unique parallel continuation,
  admitted only when required. (CLEAN, AA)

**Solid-stage declarations (the Euclid-XI-replacing axioms):**
- **S1** — noncoplanar extension exists. (The logical point where rank three becomes
  admissible; "the Flower Plane by itself contains no theorem asserting a noncoplanar
  point," 4.XIII.P3.)
- **S2** — three noncollinear points determine one plane.
- **S3** — a perpendicular to a plane exists uniquely through a point.
- **S4** — spheres of copied radius are constructible.
- **S5** — three equal spheres centered on an equilateral Flower face have two common
  points on opposite sides of the face plane.
- **S6** — rigid solid congruence.
- **P4.4** — global defect-free tetrahedral–octahedral continuation when completed F³ is
  required.

(NOTATION_LEDGER.md line 231: S1–S6 — "solid postulates (noncoplanar extension, …)" —
status CLEAN, "AA: explicitly admitted".)

**What is NOT among the new axioms:** no parallel postulate is admitted at the start (it
arrives only inside P4.3's global completion); no real-valued distance, dot product,
Cartesian coordinates, or numerical angle measure is assumed before construction (4.X.P10).
The theory is therefore strictly weaker than Euclid Books I–XI taken wholesale, and
deliberately so.

## Method notes and disclosures

- The dependency column above was extracted mechanically from every `[Prop. x.y]` citation
  in each proposition's proof text in `book11.txt`; implicit construction steps (e.g. use
  of 1.11/1.12/1.31 in 11.11–11.12) are included as cited in the text.
- The R Theory mapping was checked by full-text search of the Volume I source manuscript
  and all 23 rewrite pages for Euclid XI references; none exist. The "INCOMPLETE (no
  counterpart claim)" entries record an actual absence found by reading, not an oversight.
- No computation was run for this ledger; "CHECKED" entries above report computations
  recorded in NOTATION_LEDGER.md (V6–V12 exact checks, V27, the 1,999-matrix CN check),
  not new verifications. Per the standing rule, they are reported as the ledger reports
  them: exact symbolic checks on the stated Gram-matrix facts.
- Nothing in this ledger promotes any R Theory claim beyond what the audit's scope tags
  already certify. In particular: the theory proves a regular tetrahedron and a regular
  octahedron — it does not prove Euclid's solid-angle theorems (11.20–11.23) in general,
  any of the parallelepiped volume theorems (11.24–11.37), the cube bisection (11.38), or
  the prism equality (11.39). Those are INCOMPLETE as extension claims, full stop.
