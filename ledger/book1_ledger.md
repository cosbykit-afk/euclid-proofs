# Book 1 Ledger — Euclid Extension Proof Campaign

**Worker:** Book 1 (depth 2/2) · **Date:** 2026-09-21 (PDT)
**Sources read:** `/home/hatch/workspace/euclid_work/text/book1.txt` (Fitzpatrick/Heiberg, full text, 2262 lines — read end to end); `/home/hatch/workspace/user/files/euclid-encyclopedia-article.html` (context); `/home/hatch/workspace/user/files/a3cd8c26d8eb63f6315ac09d5f1d1ef5071b2fe3.pdf` (TESS-India, theme only); `/home/hatch/workspace/r-theory-rewrite/book{0..6}/index.html` (+book7, book8 spot checks); `/home/hatch/workspace/vol4/NOTATION_LEDGER.md`; `/home/hatch/workspace/vol4/DEPENDENCY_CHAIN.md`.

**Scope vocabulary (this ledger):** PROVED — deductive proof shown; CHECKED — verified by a completed computation (computation described); ASSERTED — manuscript stipulation or new axiom; INCOMPLETE — not established. The label applies to the *extension claim* (the claim that R Theory builds on/generalizes the Euclid item), never to Euclid's own proposition, which stands as written in the Elements.

## Book summary

Euclid's Book 1 is the foundation of plane geometry involving straight lines: 23 definitions, 5 postulates, 5 common notions, then 48 propositions — 14 problems (constructions, "which was to be done," Q.E.F.) and 34 theorems (Q.E.D.). Per the encyclopedia article, each complete proposition has a six-part anatomy: general enunciation, setting-out, definition/diorismos (conditions of possibility), construction, proof, conclusion; the demonstrations proceed entirely by **synthesis** (from the known to the unknown), never by analysis. The book's arc: basic constructions (1.1–1.15), triangle inequalities (1.16–1.26), the parallel theory (1.27–1.34, turning on Postulate 5), area/equality of parallelograms and triangles (1.35–1.45), the square construction (1.46), and the Pythagorean theorem with its converse (1.47–1.48).

**Campaign verdict on the extension claim (read before using the table).** The audit records do **not** establish R Theory as a deductive extension of the Elements:

- Book 4 §4.X contains the **No-Euclid-wholesale theorem (4.X.H)** — Euclid is not imported wholesale (the §4.X outline is itself tagged MA on the book page). The dependency chain in `/home/hatch/workspace/vol4/DEPENDENCY_CHAIN.md` contains **zero** references to Euclid as a dependency source; nothing from the Elements sits in any layer.
- The extension's synthetic-geometry layer (Book 4, "Flower") starts from its **own** declared substrate — Import P4.1, congruence principle P4.1-C, declaration P4.3, Gates A–H, solid postulates S1–S6 (all AA; see §6). The series' own master chain (4.XIII, CP) runs "one-generator calculus → rank obstruction → **P4.1** → Flower → right angle → …" — it begins at P4.1, not at Euclid.
- Where R Theory rebuilds the same constructions (Book 4 P1–P3: equilateral triangle, angle bisection, perpendicular), they are **re-derivations from the extension's own substrate**, explicitly not citations of Euclid 1.1/1.9/1.11 (No-Euclid-wholesale). Book 4 records them CP, with the perpendicularity additionally re-verified by a completed numerical check (dot(OA,OD) = 0); the series also records elsewhere (book8 page) that the Volume I ledger counts the synthetic Flower proofs as "read but not machine-checked." Both facts are kept in the table below — this is why those rows are CHECKED, never PROVED.
- Outside Book 4, Euclidean geometry enters R Theory only as **standard imported background mathematics** ("Euclidean declaration," Euclidean metric (U,G), Euclidean vector calculus ST) — used, never derived from the Elements.
- **Axiom Zero (Book 5, A0.1–A0.2)** is recorded in NOTATION_LEDGER.md as AXIOM: "Granted, not proved. First R-specific mathematical axiom in the revised chain."

Consequence for the inventory: for most of the 48 propositions the honest entry is "no deductive link in the records," scope INCOMPLETE (as an extension claim). The table never upgrades a thematic resemblance into a derivation.

## Definitions (1–23)

One-line statements; Euclid's definitions are stipulations, so they have no proof dependencies. The extension does not adopt Euclid's definitions as axioms (No-Euclid-wholesale); where Book 4's P4.1 substrate supplies its own primitive, it is named.

| No. | Euclid statement | R Theory extension | Scope |
|---|---|---|---|
| 1.1 | A point is that of which there is no part | P4.1 substrate admits "points" as construction data (AA); not Euclid's definition | ASSERTED |
| 1.2 | A line is a length without breadth | No deductive link; only standard-background use of curves | INCOMPLETE |
| 1.3 | Extremities of a line are points | No deductive link in the records | INCOMPLETE |
| 1.4 | A straight-line lies evenly with points on itself | Replaced by P4.1's "straight continuation" (AA), not Euclid's phrasing | ASSERTED |
| 1.5 | A surface has length and breadth only | No deductive link in the records | INCOMPLETE |
| 1.6 | Extremities of a surface are lines | No deductive link in the records | INCOMPLETE |
| 1.7 | A plane surface lies evenly with the straight-lines on itself | 4.V rank-three extension uses solid postulates S1–S6 (AA), not this definition | ASSERTED |
| 1.8 | A plane angle is the inclination of two meeting non-straight lines | Book 4 Flower works with 60° sectors/natural angle units; not derived from Def. 1.8 | INCOMPLETE |
| 1.9 | A rectilinear angle has straight containing lines | No deductive link in the records | INCOMPLETE |
| 1.10 | A right angle: adjacent equal angles; the standing line is a perpendicular | Thematic analogue only: Book 4 4.IV.P0 synthetic right angle (60° sector + bisected 30° half-sector), CHECKED via completed numerical verification dot(OA,OD)=0 (book4 page); not a citation of Def. 1.10 | CHECKED (analogue) |
| 1.11 | Obtuse angle > right angle | No deductive link in the records | INCOMPLETE |
| 1.12 | Acute angle < right angle | No deductive link in the records | INCOMPLETE |
| 1.13 | A boundary is the extremity of something | No deductive link in the records | INCOMPLETE |
| 1.14 | A figure is contained by boundary/boundaries | No deductive link in the records | INCOMPLETE |
| 1.15 | A circle: plane figure with all radii from an interior point equal | Thematic analogue: P4.1's "equal-circle operation" (AA) is the extension's own circle primitive; not imported from Def. 1.15 | ASSERTED |
| 1.16 | The center of the circle | No deductive link in the records | INCOMPLETE |
| 1.17 | A diameter is a center-drawn line terminated both ways by the circumference (halves the circle — the edition notes this clause is really a postulate) | No deductive link in the records | INCOMPLETE |
| 1.18 | A semi-circle; its center = the circle's | No deductive link in the records | INCOMPLETE |
| 1.19 | Rectilinear figures: trilateral/quadrilateral/multilateral | No deductive link in the records | INCOMPLETE |
| 1.20 | Triangle taxonomy: equilateral/isosceles/scalene | No deductive link in the records | INCOMPLETE |
| 1.21 | Triangle taxonomy by angle: right-/obtuse-/acute-angled | No deductive link in the records | INCOMPLETE |
| 1.22 | Quadrilateral taxonomy: square, rectangle, rhombus, rhomboid, trapezia | Square used only as standard background (1.46's construction is standard imported math); not derived from Def. 1.22 | INCOMPLETE |
| 1.23 | Parallel lines: coplanar, produced to infinity in both directions, never meeting | Thematic analogue: Book 4's unique-parallels claim is the **separate declaration P4.3** (AA), not Def. 1.23; local vs global Euclidean completion explicitly distinguished in §4.X | ASSERTED |

## Postulates (1–5)

| No. | Euclid statement | R Theory extension | Scope |
|---|---|---|---|
| P1 | Draw a straight-line from any point to any point | P4.1's "straight continuation" (AA) is the extension's own construction licence; not P1 | ASSERTED |
| P2 | Produce a finite straight-line continuously | P4.1 "straight continuation" (AA); "continuous triangular filling" covers the extension's continuity needs | ASSERTED |
| P3 | Draw a circle with any center and radius | P4.1's "equal-circle operation" (AA) is the extension's own circle primitive | ASSERTED |
| P4 | All right-angles are equal | No deductive link; the synthetic right angle (4.IV.P0) is CHECKED by numerical verification, not by P4 | CHECKED (analogue) |
| P5 | Parallel postulate (interior angles < two right-angles ⇒ lines meet) | Thematic analogue: **declaration P4.3** (AA) — "global flatness and unique parallels need the separate declaration P4.3" (§4.X). The parallel postulate is *re-declared*, not proved or imported | ASSERTED |
## Common notions (1–5)

| No. | Euclid statement | R Theory extension | Scope |
|---|---|---|---|
| CN1 | Things equal to the same thing are equal to one another | Used throughout as ordinary arithmetic equality (standard background); not cited as a premise of any R Theory theorem in the records | INCOMPLETE |
| CN2 | Equals added to equals → wholes equal | Same as CN1: standard arithmetic, no deductive link | INCOMPLETE |
| CN3 | Equals subtracted from equals → remainders equal | Same as CN1: standard arithmetic, no deductive link | INCOMPLETE |
| CN4 | Things coinciding with one another are equal | No deductive link; the extension's congruence principle is P4.1-C (SSS admitted, AA) — a *replacement* for superposition, not a use of CN4 | INCOMPLETE |
| CN5 | The whole is greater than the part | Used as ordinary order reasoning (standard background); not cited as a premise in the records | INCOMPLETE |

(Edition footnotes used above: 1.1 assumes the two circles actually intersect — counted as an extra postulate; 1.1/1.4 assume two straight-lines cannot share a common segment; 1.4's application of one figure to another is counted as an extra postulate, with Post. 1 implicitly giving uniqueness of the joining line; 1.6, 1.19, 1.25 use the unstated notions "not unequal ⇒ equal" and "neither greater nor less ⇒ equal"; 1.16 assumes point F lies inside angle ABC; 1.37/1.47 use "halves/doubles of equals are equal"; 1.48 uses "squares of equals are equal" and its converse; 1.40 is regarded by Heiberg as an early interpolation. These are recorded here so no hidden assumption of Euclid's is laundered into the extension.)

## Proposition inventory (1.1–1.48)

Euclid proof dependencies are extracted from the proof text as printed (bracketed citations). "No deductive link in the records" means: the R Theory rewrite pages (books 0–8) and the Volume IV ledgers contain no theorem whose dependency list cites the Euclid proposition; and §4.X's No-Euclid-wholesale theorem (4.X.H, section tagged MA) forbids treating Euclid as a wholesale premise set.

| No. | Statement (one line) | Euclid proof dependencies | R Theory extension | Scope |
|---|---|---|---|---|
| 1.1 | Construct an equilateral triangle on a given finite straight-line (problem) | Post. 1, Post. 3, Def. 1.15, CN1 (+ extra postulates: the circles intersect; two lines share no segment) | Thematic analogue: Book 4 Flower P1 "equilateral triangle," rebuilt from P4.1, recorded CP on the book4 page; re-verified CN in the rewrite. Not a citation of 1.1 | CHECKED (analogue; proof "read but not machine-checked" per book8 page) |
| 1.2 | Place a segment equal to a given segment at a given point (problem) | Post. 1, 1.1, Post. 2, Post. 3, Def. 1.15, CN3, CN1 | Thematic analogue: P4.1's "copied congruence unit r" (AA) is the extension's own compass primitive; not derived from 1.2 | ASSERTED |
| 1.3 | Cut off from the greater of two unequal segments one equal to the lesser (problem) | 1.2, Post. 3, Def. 1.15, CN1 | No deductive link in the records | INCOMPLETE |
| 1.4 | SAS congruence: two sides + included angle equal ⇒ bases, triangles, remaining angles equal (theorem) | CN4 via superposition (+ extra postulate: application of figures; Post. 1 for line uniqueness) | No deductive link; the extension's congruence foundation is P4.1-C (SSS admitted as a principle, AA) — a declared replacement for superposition, which §4.X names the "congruence debt" | INCOMPLETE |
| 1.5 | Isosceles triangle: base angles equal; produced equal sides give equal under-base angles | Post. 2, 1.3, Post. 1, 1.4, CN3 | No deductive link in the records | INCOMPLETE |
| 1.6 | Equal base angles ⇒ equal subtending sides (converse of 1.5) | 1.3, Post. 1, 1.4, CN5 (+ "not unequal ⇒ equal") | No deductive link in the records | INCOMPLETE |
| 1.7 | Uniqueness of the triangle on a base on one side (no two distinct apexes) | Post. 1, 1.5, CN5 | No deductive link in the records | INCOMPLETE |
| 1.8 | SSS congruence: two sides + base equal ⇒ included angles equal | 1.7, CN4 (superposition) | Thematic analogue: **P4.1-C "SSS admitted as a congruence principle" (AA)** — the extension takes SSS as a *declared principle*, i.e. asserts what Euclid proves via 1.7+superposition | ASSERTED |
| 1.9 | Bisect a given rectilinear angle (problem) | 1.3, Post. 1, 1.1, 1.8 | Thematic analogue: Book 4 Flower P2 "angle bisection," rebuilt from P4.1, recorded CP; not a citation of 1.9 | CHECKED (analogue; same caveat as 1.1) |
| 1.10 | Bisect a given finite straight-line (problem) | 1.1, 1.9, 1.4 | No deductive link in the records | INCOMPLETE |
| 1.11 | Draw a perpendicular to a line from a point on it (problem) | 1.3, 1.1, Post. 1, 1.8, Def. 1.10 | Thematic analogue: Book 4 Flower P3 "perpendicular" and 4.IV.P0 synthetic right angle (60° sector + bisected 30° half-sector = 90°), CHECKED by completed numerical verification dot(OA,OD) = 0 (book4 page; re-verified CN in the rewrite) | CHECKED (analogue; proof "read but not machine-checked" per book8 page) |
| 1.12 | Draw a perpendicular to an infinite line from an exterior point (problem) | Post. 3, 1.10, Post. 1, 1.8, Def. 1.10 | No deductive link in the records | INCOMPLETE |
| 1.13 | A line standing on a line makes two right angles or a sum of two right angles | Def. 1.10, 1.11, CN2, CN1 | No deductive link in the records | INCOMPLETE |
| 1.14 | Converse of 1.13: adjacent angles summing to two right angles ⇒ straight-on lines | 1.13, CN1, CN3, CN5 | Used in Book 4's 1.44-analogue construction (straight-on verification via 1.14) — but the citation chain there is internal to the extension's own geometry, not to Euclid's text; no deductive link to 1.14 itself | INCOMPLETE |
| 1.15 | Vertical angles of intersecting lines are equal | 1.13 (×2), CN1, CN3 | No deductive link in the records | INCOMPLETE |
| 1.16 | Exterior angle of a triangle exceeds either opposite interior angle | 1.10, Post. 2, 1.3, Post. 1, 1.4, 1.15 (+ F-interior assumption) | No deductive link in the records | INCOMPLETE |
| 1.17 | Any two angles of a triangle sum to less than two right angles | 1.16, 1.13 | No deductive link in the records | INCOMPLETE |
| 1.18 | Greater side subtends greater angle | 1.3, Post. 1, 1.16, 1.5 | No deductive link in the records | INCOMPLETE |
| 1.19 | Greater angle subtended by greater side | 1.5, 1.18 (+ trichotomy notion) | No deductive link in the records | INCOMPLETE |
| 1.20 | Triangle inequality: any two sides exceed the third | Post. 2, 1.3, Post. 1, 1.5, 1.19 | No deductive link in the records | INCOMPLETE |
| 1.21 | Two interior segments on one side: shorter sum, larger included angle | 1.20, 1.16 | No deductive link in the records | INCOMPLETE |
| 1.22 | Construct a triangle from three given segments (problem; needs 1.20) | 1.3, Post. 3, Def. 1.15, CN1 (1.20 as possibility condition) | No deductive link in the records | INCOMPLETE |
| 1.23 | Copy a given rectilinear angle at a point on a line (problem) | 1.22, 1.8 | No deductive link in the records | INCOMPLETE |
| 1.24 | Hinge theorem: two sides equal, larger included angle ⇒ larger base | 1.23, 1.3, Post. 1, 1.4, 1.5, 1.19 | No deductive link in the records | INCOMPLETE |
| 1.25 | Converse hinge: larger base ⇒ larger included angle | 1.4, 1.24 (+ trichotomy) | No deductive link in the records | INCOMPLETE |
| 1.26 | ASA/AAS congruence: two angles + one side equal ⇒ remaining sides/angle equal | 1.3, Post. 1, 1.4, 1.16 (two cases) | No deductive link in the records | INCOMPLETE |
| 1.27 | Equal alternate interior angles ⇒ lines parallel | Def. 1.23, 1.16 | No deductive link in the records | INCOMPLETE |
| 1.28 | Corresponding angle equal, or same-side interiors = two right angles ⇒ parallel | 1.15, 1.27, 1.13, CN3 | No deductive link in the records | INCOMPLETE |
| 1.29 | A transversal of parallels makes alternate angles equal, etc. (uses Post. 5) | 1.13, 1.15, Post. 5, Def. 1.23 | No deductive link; the extension's parallel theory rests on declaration P4.3 (AA), not on 1.29 | INCOMPLETE |
| 1.30 | Lines parallel to the same line are parallel | 1.29 (×2), 1.27, CN1 | No deductive link in the records | INCOMPLETE |
| 1.31 | Draw a parallel to a line through a point (problem) | 1.23, Post. 2, 1.27 | No deductive link in the records | INCOMPLETE |
| 1.32 | Exterior angle = sum of opposite interiors; interior angles sum to two right angles | 1.31, 1.29, 1.13, CN2 | No deductive link in the records (angle-sum facts used only as standard background) | INCOMPLETE |
| 1.33 | Segments joining equal parallel segments on the same side are equal and parallel | Post. 1, 1.29, 1.4, 1.27 | No deductive link in the records | INCOMPLETE |
| 1.34 | Parallelogram: opposite sides/angles equal; diagonal bisects it | 1.29, 1.26, 1.4, CN2 | No deductive link in the records | INCOMPLETE |
| 1.35 | Parallelograms on the same base between the same parallels are equal (in area — first area use) | 1.34, 1.29, 1.4, CN3, CN2 | No deductive link in the records | INCOMPLETE |
| 1.36 | Parallelograms on equal bases between the same parallels are equal | 1.34, 1.33, 1.35 | No deductive link in the records | INCOMPLETE |
| 1.37 | Triangles on the same base between the same parallels are equal | 1.31, 1.35, 1.34 (+ "halves of equals") | No deductive link in the records | INCOMPLETE |
| 1.38 | Triangles on equal bases between the same parallels are equal | 1.31, 1.36, 1.34 | No deductive link in the records | INCOMPLETE |
| 1.39 | Equal triangles on the same base on the same side are between the same parallels | 1.31, Post. 1, 1.37, CN5 | No deductive link in the records | INCOMPLETE |
| 1.40 | Equal triangles on equal bases on the same side are between the same parallels (Heiberg: likely interpolation) | 1.31, 1.38 | No deductive link in the records | INCOMPLETE |
| 1.41 | A parallelogram is double a triangle on the same base between the same parallels | 1.37, 1.34 | The extension's area/doubling reasoning uses standard arithmetic (doubles of equals), not 1.41; no deductive link | INCOMPLETE |
| 1.42 | Construct a parallelogram equal to a given triangle in a given angle (problem) | 1.10, Post. 1, 1.23, 1.31, 1.38, 1.41 | No deductive link in the records | INCOMPLETE |
| 1.43 | Complements about the diagonal of a parallelogram are equal | 1.34, CN2, CN3 | No deductive link in the records | INCOMPLETE |
| 1.44 | Apply a parallelogram equal to a triangle to a given line in a given angle (problem; uses Post. 5) | 1.42, 1.31, 1.29, 1.15, 1.43, 1.14 | No deductive link in the records | INCOMPLETE |
| 1.45 | Construct a parallelogram equal to a given rectilinear figure in a given angle (problem) | Post. 1, 1.42, 1.44, 1.29, 1.14, 1.34, 1.30, 1.33 | No deductive link in the records | INCOMPLETE |
| 1.46 | Describe a square on a given segment (problem) | 1.11, 1.3, 1.31, 1.34, 1.29, Def. 1.22 | Squares on segments are used throughout (e.g. 1.47's use in the extension's metric reasoning) only as standard imported mathematics; 1.46 is never cited as a premise | INCOMPLETE |
| 1.47 | Pythagoras: square on hypotenuse = sum of squares on the legs | 1.46, 1.31, Post. 1, 1.14, 1.4, 1.41, CN2 (+ halves/doubles notions) | **Used as standard background, not extended from Euclid's proof.** R Theory's metric apparatus (book6 (U,G), J_G; book8 Euclidean vector calculus, ⋆₃²=+1) presupposes the Pythagorean metric as standard imported mathematics. No record derives it from, or generalizes, Euclid 1.47's proof | INCOMPLETE (as an extension claim) |
| 1.48 | Converse of Pythagoras (uses "squares of equals" notion) | 1.11, 1.3, Post. 1, 1.47, 1.8 | No deductive link in the records | INCOMPLETE |
## New axioms/definitions the extension introduces beyond Euclid

These are the load-bearing assumptions — every one of them is *granted*, not derived from the Elements. Exact wording is quoted from the records cited.

1. **Import P4.1** (Book 4; AA = admitted assumption). "pre-metric construction substrate: points, straight continuation, copied congruence unit r, equal-circle operation, continuous triangular filling." This is the extension's replacement for Euclid's Postulates 1–3 and the existential assumptions behind them. Everything synthetic in Book 4 bottoms out here, not in the Elements.
2. **P4.1-C** (Book 4; AA). "SSS admitted as a congruence principle." This is how the extension settles what §4.X calls the **congruence debt** — Euclid's unaxiomatized superposition in 1.4 and 1.8. Euclid proves SSS via superposition + 1.7; the extension *declares* SSS instead. That is a strictly weaker (more assumptive) foundation than Euclid's, and the records label it honestly.
3. **Declaration P4.3** (Book 4 §4.X; AA). "global flatness and unique parallels need the separate declaration P4.3." This is the extension's re-declaration of the parallel postulate. Euclid's Postulate 5 is neither proved nor imported — it is re-asserted, with local vs. global Euclidean completion explicitly distinguished.
4. **Gates A–H** (Book 4; AA). Ordering constraints on what may be used when: rank before dimension language; Flower before metric; **metric after right angle (Gate B)**; continuous carrier before discrete lattice; coframe before connection; connection before curvature; orientation before handedness; geometry before physics; coordinate-novelty firewall (Gate H = 4.X.I, the no-novelty-from-coordinate-change rule; the isometry identity was additionally re-verified by completed numerical check).
5. **Solid postulates S1–S6** (Book 4 §4.V; AA). "noncoplanar extension, plane determination, perpendicular to a plane, sphere construction, equal-sphere intersection, rigid solid congruence — admitted explicitly — the third direction is not a planar consequence." The extension's analogue of Euclid's solid-geometry beginnings, admitted by declaration.
6. **Flower-role lock** (Book 4; MA). Flower coordinates are an instrument only — "never as a preferred coordinate system, tetrahedral lattice, physical substrate, or source of rank three." A methodological stipulation, not a theorem.
7. **No-Euclid-wholesale theorem (4.X.H)** (Book 4 §4.X; section tagged MA). Euclid is not imported wholesale. This is the theorem that caps the extension claim: the extension may rebuild Euclid-like constructions, but it may not cite the Elements as a premise set.
8. **Axiom Zero (Book 5, A0.1–A0.2)** (NOTATION_LEDGER.md §0.5; AXIOM). "(A0.1) independent partner + pairing + direct sum; (A0.2) primitive diagonal noncoupling." "Granted, not proved. First R-specific mathematical axiom in the revised chain." Every downstream construction (Books 6+) inherits this conditional.
9. **Levi-Civita existence/uniqueness** (Book 4; standard imported theorem). Used after the metric is declared — imported from standard differential geometry, not from Euclid.

Where the extension needs a genuinely new constructive idea rather than a new axiom, it follows the TESS-India pattern — linking shape/space with ratio and deduction creatively: e.g. **4.IV.P0** builds a right angle with no protractor, no dot product, no angle function, out of a 60° sector plus a bisected 30° half-sector (OA north, OB/OC at ±30°, equal circles through B and C meeting again at D = (√3, 0), OD ⊥ OA), with perpendicularity earned by the completed numerical check dot(OA,OD) = 0. That is a creative recombination of checked pieces, not a new postulate.

## Method notes and open gaps (disclosed per Kit's standard)

- **What I could not verify:** the rewrite pages give section outlines with status tags (CP/CN/MA/AA), not the full proof texts. The Flower P1–P3 and 4.IV.P0 constructions are therefore CHECKED (completed numerical verification exists for the right angle) but not PROVED in this ledger's sense, and book8's page notes the Volume I ledger records them as "read but not machine-checked." No status was rounded up.
- **Search boundary:** the "no deductive link" verdicts rest on the rewrite series pages (books 0–8), NOTATION_LEDGER.md, and DEPENDENCY_CHAIN.md — the records the task pointed to. The Volume I manuscript Google Doc is read-only and was not searched for Euclid citations; if the manuscript cites the Elements explicitly, it is not visible in these audited records.
- **Terminology mapping:** the series' own labels CP/CN/MA/AA/ST were mapped to this ledger's four labels as: CP/CN → CHECKED (with the computation or proof-check described); MA/AA/AXIOM → ASSERTED; claims absent from the records → INCOMPLETE. The mapping is stated so nothing is laundered.
- **Genuine kinship, honestly bounded:** the encyclopedia article stresses that Euclid's demonstrations are entirely synthetic (never analytic). The extension's Flower constructions are likewise synthetic straightedge-and-compass-style constructions. That methodological kinship is real — but kinship is not derivation, and the ledger does not count it as one.
- **Bottom line for the campaign:** the records support "R Theory rebuilds a small synthetic-geometry kernel (P4.1 → Flower → right angle) *in the spirit of* Euclid while explicitly refusing to import him (4.X.H), and everything else Euclidean is either re-declared (P4.3, S1–S6, P4.1-C) or used as standard background." They do not support "R Theory is a deductive extension of Euclid's Elements," and this ledger was written so that no row can be read that way.
