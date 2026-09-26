# Book 3 Ledger — Circles (Euclid Extension Proof Campaign)

**Source:** `/home/hatch/workspace/euclid_work/text/book3.txt` (Fitzpatrick/Heiberg English
translation, Greek alongside; page refs 69–106).
**Historical context:** `/home/hatch/workspace/user/files/euclid-encyclopedia-article.html`
(Encyclopedia.com: "Book III treats circles, including their intersections and touchings. Book IV
consists entirely of problems about circles…").
**Constructive framing:** the TESS-India paper ("Developing creative thinking in mathematics:
trigonometry") — deductions must be anchored to constructible shape and ratio, built stepwise
from what is already established, not imported from authority.

**Method:** every proposition statement and every proof dependency below was extracted from the
actual proof text in `book3.txt` (bracket citations `[Prop. n]`, `[Def. n]`, `[C.N. n]`), not from
memory. R Theory mappings were read from the rewrite series pages
(`/home/hatch/workspace/r-theory-rewrite/bookM/index.html`, M=0..22) and from the audit records
(`/home/hatch/workspace/vol4/NOTATION_LEDGER.md`, `/home/hatch/workspace/vol4/DEPENDENCY_CHAIN.md`).

**Scope-label key (Kit's standard):** PROVED = deductive proof from Euclid's definitions /
postulates / earlier propositions shown in the ledger; CHECKED = verified by a completed
computation (computation described); ASSERTED = manuscript stipulation or new axiom, granted not
proved; INCOMPLETE = not established (reason given). Statuses are never rounded up or down.

---

## Book summary

Book 3 is Euclid's theory of the circle, in 11 definitions, 37 propositions, and 2 corollaries.
It introduces **no new postulates and no new common notions** — all construction goes through
Book 1 Postulates 1–3 and the Book 1 common notions. The book has four movements:

1. **Center machinery (3.1–3.4):** finding the center (3.1, with corollary: the perpendicular
   bisector of a chord passes through the center), chords fall inside (3.2), diameter/line
   through center bisects ⟂ chord (3.3), off-center chords don't bisect each other (3.4).
2. **Circle–circle relations (3.5–3.13):** concentric circles can't cut/touch (3.5, 3.6);
   extremal distances from interior/exterior points (3.7, 3.8); >2 equal radii ⇒ center (3.9);
   at most 2 intersection points (3.10); centers–contact collinearity for internal (3.11) and
   external (3.12) touchings; at most 1 touching point (3.13).
3. **Chords and distances (3.14–3.15):** equal chords equally distant from center, converse
   (3.14); diameter is the greatest chord, nearness ordering (3.15).
4. **Tangents, inscribed angles, arcs (3.16–3.37):** tangent characterization (3.16 with
   corollary, 3.17–3.19); central vs. inscribed angle, Thales-type theorems (3.20–3.22);
   similar segments (3.23–3.24); completing a circle from a segment (3.25); angle–arc–chord
   correspondences (3.26–3.29); bisecting a circumference (3.30); angle in a semicircle is a
   right angle (3.31); tangent–chord angle = alternate-segment angle (3.32); segment
   constructions (3.33, 3.34); power of a point (3.35–3.37).

**Corollaries:** 3.1 corr. — a line bisecting a chord at right angles carries the center;
3.16 corr. — a line perpendicular to a diameter at its end touches the circle (used in 3.17,
3.33, 3.37).

### Definitions (Book 3, as numbered by Euclid)

| # | Definition |
|---|-----------|
| 3.Def.1 | Equal circles are those with equal diameters, or equal radii (distances from centers). |
| 3.Def.2 | A straight line touches a circle if, meeting it and produced, it does not cut the circle. |
| 3.Def.3 | Circles touch one another if, meeting, they do not cut one another. |
| 3.Def.4 | Chords are equally far from the center when the perpendiculars from the center are equal. |
| 3.Def.5 | A chord is "further" from the center when the greater perpendicular falls on it. |
| 3.Def.6 | A segment of a circle is the figure contained by a straight line and a circumference. |
| 3.Def.7 | The angle of a segment is the angle contained by the straight line and the circumference. |
| 3.Def.8 | The angle *in* a segment is the angle formed by joining a point on the arc to the ends of the base chord. |
| 3.Def.9 | An angle is said to "stand upon" a circumference when its sides cut off that circumference. |
| 3.Def.10 | A sector is the figure at the center bounded by two radii and the intercepted arc. |
| 3.Def.11 | Similar segments are those accepting equal angles (equal inscribed angles). |

---

## Full proposition inventory

The "R Theory extension" column is the honest finding: **no proposition of Euclid Book 3 is
re-derived from Euclid's definitions/postulates anywhere in the R Theory corpus.** Book 4 §4.IV
states that "Books I–II proofs [are] re-presented and re-certified inside the corpus (included,
not merely cited)" — with a *manuscript assertion* tag on that re-presentation claim itself —
but Book III is not re-presented. R Theory's circles are the *analytic* unit circle in carrier
spaces (phase circle 𝕋, carrier identity U²+W²=1), imported as standard mathematics (tag ST),
not proved from 3.Def.1–11. Where a genuine nearby R claim exists (Book 4 Flower synthetic
geometry; Book 2 carrier-circle numeric checks), it is named with its own corpus scope label.

| # | Statement | Euclid proof dependencies (from proof text) | R Theory extension | Scope |
|---|-----------|--------------------------------------------|--------------------|-------|
| 3.1 | To find the center of a given circle. (Corr.: a line bisecting a chord at right angles carries the center.) | 1.9, 1.11, 1.8, Def. 1.10 | None. No center-finding construction exists in the corpus; carrier spaces are assumed coordinatized. | INCOMPLETE — not attempted in R Theory. |
| 3.2 | The chord joining two points on a circumference falls inside the circle. | 3.1, 1.5, 1.16, 1.19 | None. The corpus's circle is the analytic locus U²+W²=1 (Book 2, D5/C5); chord-interiority is imported, not derived. | INCOMPLETE — used implicitly as ST, never derived. |
| 3.3 | A line through the center bisecting a chord is perpendicular to it; and conversely. | 3.1, 1.8, Def. 1.10, 1.5, 1.26 | None. No synthetic chord-bisector theorem in the corpus. | INCOMPLETE |
| 3.4 | Two chords not through the center cannot bisect each other. | 3.1, 3.3 | None. | INCOMPLETE |
| 3.5 | Two circles cutting one another cannot share a center. | None — proof uses only Def. 1.15 (radii equal) and C.N. 1 (transitivity of equals). | None. | INCOMPLETE |
| 3.6 | Two circles touching one another cannot share a center. | None — Def. 1.15, C.N. 1. | None. | INCOMPLETE |
| 3.7 | From a non-center point on a diameter, the segment toward the center is greatest, away from center least; nearer segments exceed farther ones. | 1.20, 1.24, 1.23, 1.4 | None. No radial-extremum theorem in the corpus. | INCOMPLETE |
| 3.8 | From an exterior point, the line through the center to the concave side is greatest, to the convex side least; nearer exceed farther. | 3.1, 1.20, 1.24, 1.21, 1.23, 1.4 | None. | INCOMPLETE |
| 3.9 | If more than two equal segments radiate from an interior point to the circumference, that point is the center. | 1.10, 1.8, Def. 1.10, 3.1 corr. | None. | INCOMPLETE |
| 3.10 | A circle cuts another circle in at most two points. | 1.11, 3.1 corr., 3.5 | None. | INCOMPLETE |
| 3.11 | If two circles touch internally, the line joining their centers, produced, passes through the point of contact. | 3.1, 1.20 | None. | INCOMPLETE |
| 3.12 | If two circles touch externally, the line joining their centers passes through the point of contact. | 3.1, 1.20 | None. | INCOMPLETE |
| 3.13 | A circle touches another circle in at most one point, internally or externally. | 3.1, 3.11, 3.2, Def. 3.3 | None. | INCOMPLETE |
| 3.14 | Equal chords are equally distant from the center; chords equally distant from the center are equal. | 3.1, 1.12, 3.3, 1.47, Def. 3.4 | None. | INCOMPLETE |
| 3.15 | The diameter is the greatest chord; of other chords, nearer to the center exceeds farther. | 1.12, Def. 3.5, 1.3, 1.11, 3.14, 1.20, 1.24 | None. | INCOMPLETE |
| 3.16 | A perpendicular to a diameter at its end falls outside the circle (tangent); the "horn angle" between tangent and circumference admits no inserted straight line. (Corr.: the perpendicular to a diameter at its end touches the circle.) | 1.5, 1.17, 1.12, 1.19, 3.2 | None as a synthetic tangent theorem. Book 3 (rewrite) §3.VIII treats *tangent orientation of RPⁿ* — tangent spaces of manifolds, a different object; it is a checked proof / standard imported theorem (ST), not an extension of 3.16. | INCOMPLETE as extension of 3.16; the manifold-tangent claim is separately scoped on its page (ST), not derived from Euclid. |
| 3.17 | To draw a tangent to a given circle from a given point. | 3.1, 1.11, 1.4, 3.16 corr. | None. | INCOMPLETE |
| 3.18 | The radius joined to the point of contact is perpendicular to the tangent. | 3.1, 1.12, 1.17, 1.19 | None as synthetic theorem. The orthonormal polar coframe θ¹=dr, θ²=r dφ (Book 4, Fig. "radial spokes and concentric circles") *uses* radius⟂circle implicitly as imported analytic geometry (ST). | INCOMPLETE — assumed, not proved, in the corpus. |
| 3.19 | A perpendicular erected to the tangent at the point of contact carries the center. | 1.11, 3.18 | None. | INCOMPLETE |
| 3.20 | The central angle is double the inscribed angle standing on the same arc. | 1.5, 1.32 | None. No central/inscribed-angle relation is derived in the corpus; phase doubling (U+iW = εζ², Book 7) is analytic trigonometry (ST/P), not this theorem. | INCOMPLETE |
| 3.21 | Angles in the same segment are equal. | 3.1, 3.20 | None. | INCOMPLETE |
| 3.22 | Opposite angles of a cyclic quadrilateral sum to two right angles. | 1.32, 3.21 | None. | INCOMPLETE |
| 3.23 | Two similar unequal segments cannot be constructed on the same side of the same straight line. | Def. 3.11, 1.16 | None. | INCOMPLETE |
| 3.24 | Similar segments on equal straight lines are equal (by superposition). | 3.10, C.N. 4 | None. Superposition (C.N. 4) is used by Euclid here; R Theory's Book 4 §4.X admits a "congruence debt" in its pre-metric synthetic substrate — see §New axioms, item 5. | INCOMPLETE |
| 3.25 | To complete the circle of a given circular segment. | 1.10, 1.11, 1.23, 1.6, 1.4, 3.9 | None. | INCOMPLETE |
| 3.26 | In equal circles, equal angles (at center or circumference) stand on equal circumferences. | 1.4, Def. 3.11, 3.24 | None. The "equal circles" of Def. 3.1 are not the corpus's object; R Theory uses unit circles of *declared* radius in carrier metrics (ST). | INCOMPLETE |
| 3.27 | In equal circles, angles standing on equal circumferences are equal. | 1.23, 3.26, 3.20 | None. | INCOMPLETE |
| 3.28 | In equal circles, equal chords cut off equal circumferences (major to major, minor to minor). | 3.1, Def. 3.1, 1.8, 3.26 | None. | INCOMPLETE |
| 3.29 | In equal circles, equal circumferences are subtended by equal chords. | 3.1, 3.27, Def. 3.1, 1.4 | None. | INCOMPLETE |
| 3.30 | To bisect a given circumference. | 1.10, 1.11, 1.4, 1.28 | None. | INCOMPLETE |
| 3.31 | The angle in a semicircle is a right angle; in a greater segment less than a right angle; in a lesser segment greater. | 1.5, 1.32, Def. 1.10, 1.17, 3.22 | The nearest corpus item is Book 4 **Proposition 4.IV.P0**: a *synthetic* right angle built from Flower native geometry (60° sector + bisected 30° half-sector = 90°) — checked proof (CP), with perpendicularity additionally re-verified numerically (CN). This is a *different* construction: it does not use a semicircle, does not invoke 3.31's hypotheses, and is not derived from 3.31. It is not a proof of 3.31. | INCOMPLETE — 3.31 itself is neither proved nor assumed in the corpus; 4.IV.P0 is proved (CP) but is an independent Flower construction. |
| 3.32 | The angles a tangent makes with a chord through the contact equal the angles in the alternate segments. | 1.11, 3.19, 3.31, 1.32, 3.22, 1.13 | None. | INCOMPLETE |
| 3.33 | To construct a circular segment containing a given rectilinear angle on a given straight line. | 1.23, 1.11, 1.10, 1.4, 3.16 corr., 3.32, 3.31 | None. | INCOMPLETE |
| 3.34 | To cut off a segment containing a given rectilinear angle from a given circle. | 1.23, 1.32, 3.1, 1.11 | None. | INCOMPLETE |
| 3.35 | If two chords cut one another, the rectangle on the segments of one equals the rectangle on the segments of the other (power of a point, interior). | 3.1, 1.12, 3.3, 2.5, 1.47 | None. No power-of-a-point theorem in the corpus. | INCOMPLETE |
| 3.36 | For a tangent and a secant from an exterior point, the rectangle on the whole secant and its external part equals the square on the tangent. | 3.18, 2.6, 1.47, 1.12, 3.3 | None. | INCOMPLETE |
| 3.37 | Converse of 3.36: if the secant–tangent rectangle relation holds, the outer line touches the circle. | 3.17, 3.18, 3.36, 1.8, 3.16 corr. | None. | INCOMPLETE |

### R Theory circle claims that are *not* extensions of Book 3 (kept separate so as not to overclaim)

These corpus claims involve circles but are **not** proved from, and do not prove, any Euclid
Book 3 proposition; they are scoped here to block any reading that smuggles them in as
"the theory extends Book 3":

- **Book 2, D5/C5 — carrier circle identity** U²+W²=1 with U=sin 2x, W=cos 2x: the ellipse
  identity checked to ~6e-17, the unit-circle identity to ~2e-16 — **CHECKED** (completed
  numerical check). This is analytic trigonometry on a declared coordinate, not a synthetic
  circle theorem.
- **Book 1, Fig. 7 / T5 — phase circle** 𝕋 with four seam classes; "no continuous injective
  𝕋→ℝ" proved via standard circle topology S — corpus labels: P (checked proof) resting on ST
  (standard imported theorem). The topology is imported, not earned from Euclid.
- **Book 4, Fig. 2 — Flower quadratic form's unit locus is exactly the ordinary unit circle**:
  re-verified numerically, max error 1.42e-14 over 20,000 samples — **CHECKED** (CN).
  Corpus calls this "Gate H's no-novelty firewall."
- **Book 4, §4.IV — Lemma 4.IV.L1** (six native sectors equal, complete one turn): **CP**
  (checked proof); **Proposition 4.IV.P0** (synthetic right angle, 60°+30°=90°): **CP**, plus CN
  numeric re-verification; **P1–P3** (equilateral triangle, angle bisection, perpendicular):
  **CP**. All synthetic, all Flower-native — none cites Euclid Book 3.
- **Book 0, §6** — no continuous injective parametrization of a circle by one real scalar
  (topology argument) — analytic, ST-adjacent.

Net finding: **Kit's claim "the theory is built as an extension of Euclid's work" is
realized, in the audited corpus, for Books I–II only** (Book 4 §4.IV, MA-tagged
re-presentation). For Book 3's 37 theorems the extension program is INCOMPLETE across the
board: the corpus neither re-derives them nor proves its analytic circle from them.

---

## NEW axioms/definitions the extension introduces beyond Euclid

These are the load-bearing assumptions. Each is *granted, not proved* — stated exactly as the
corpus states it, with its corpus status.

### A0. Axiom Zero (Book 5, §5.2) — the first R-specific mathematical axiom in the revised chain
*(NOTATION_LEDGER.md §0.5: "Granted, not proved. First R-specific mathematical axiom in the
revised chain." Corpus close-the-book count for Book 5: "New axioms: 1 (Axiom Zero, A0.1–A0.2).
External imports: 0.")*

- **A0.1 — independent partner + declared pairing + direct sum.** "An independent isomorphic
  partner carrier U♯ is introduced together with a declared block-compatible linear isomorphism
  ι: U → U♯ ; U ∩ U♯ = {0}; W = U ⊕ U♯ ; the pairing preserves the earned block ancestry,
  ι(E) = E♯ , ι(V) = V♯." Status on the page: **A** (assumption/axiom). The existence of the
  partner, the isomorphism, and its block-compatibility are all declared, not constructed.
- **A0.2 — primitive diagonal noncoupling.** "Maps in Hom(U,U♯) may exist mathematically, but
  A0.2 declares they are not active primitive couplings. Any later U↔U♯ coupling must be
  declared as additional structure." Status: **A**. This is a stipulation about what counts as
  primitive — it cannot be derived from anything earlier in the chain.
- Consequence stated as bookkeeping (not axiom): dim_ℝ W = 10, complex rank 5, with
  I_ι(u,v) = (−ι⁻¹v, ιu), I_ι² = −1, "canonical relative to the declared pairing" — the
  complex structure is proved (P) *conditional on* the declared pairing.

### A1. Book 4, Gate B — metric enters only after the synthetic right angle
*(Book 4 §4.IV: "Metric introduced only after the synthetic right angle (Gate B)" — tag AA,
assumption or axiom.)* The ordering (synthetic construction first, metric second) is a
constitutional gate, not a theorem. Euclid's Book 3, by contrast, works entirely inside the
metric-free congruence framework of Books I–III.

### A2. Book 4, declaration P4.3 — global flatness and unique parallels are separately declared
*(Book 4 §4.X: "local vs global Euclidean completion (global flatness and unique parallels need
the separate declaration P4.3)" — tag AA.)* This is where the Fifth-Postulate analog lives:
the Flower synthetic substrate does **not** entail global flatness or unique parallels; they
must be declared. Euclid *postulates* unique parallels (Postulate 5); R Theory's Flower plane
makes the same move explicitly as a declaration. Load-bearing: anything downstream that
assumes a global Euclidean plane rests on P4.3.

### A3. Book 4 §4.X — the "congruence debt" (pre-metric synthetic substrate)
*(Book 4 §4.X: "Pre-metric synthetic substrate; the congruence debt; the exact point where
metric enters" — tag MA, manuscript assertion.)* The corpus admits it has not closed the
foundations of congruence without a metric: superposition-style moves (cf. Euclid's C.N. 4,
used in 3.24) are used in the Flower constructions while their pre-metric justification is an
outstanding *debt*, asserted not proved. Any Flower result that leans on congruence before
Gate B leans on A3.

### A4. Axiom Zero's declared (non-canonical) pairing propagates
*(NOTATION_LEDGER.md §0.5 on ι: "Declared pairing; construction ι-dependent, not canonical
(page MA).")* Every construction built through ι (Book 6's I_ι, the Hermitian carrier theorem
6.5, etc.) inherits A0.1's declared status: proved *relative to* the pairing, not canonical.
The ledger marks the U♯ and ι rows CLEAN/AXIOM, i.e., internally consistent but resting on
the grant.

### Not new axioms (kept explicit so they are not mistaken for A0–A3)
- Books 1, 2, and 3 (rewrite) each close with **"New axioms: 0"** (Book 1: "zero new axioms
  (T7), zero external imports (T8) P by ledger audit"; Book 2: "0 new axioms"; Book 3:
  "New axioms: 0… Preferred-orientation/lift/chirality axioms: 0").
- Book 0: no new axiom is needed to represent handedness/orientation (J²=−I follows from
  declaring an oriented Euclidean two-plane).
- "Standard imported theorem" (ST) items — e.g. the circle topology S used in Book 1 T5, the
  Jacobian/area computations in Book 10 — are imports, not axioms; the corpus tags them ST
  rather than proving them.

### Structural admission relevant to this ledger
- **No-Euclid-wholesale theorem (4.X.H)** and the **no-novelty-from-coordinate-change rule
  (4.X.I = Gate H)**: the corpus explicitly refuses to take Euclid's geometry wholesale and
  refuses to count coordinate changes as new geometry (isometry identity re-verified CN).
  This is consistent with the table above: Book 3's synthetic theorems are neither absorbed
  nor re-derived — the corpus works in analytic/coordinate geometry imported as ST.

---

## Dependency graph notes (for the master ledger)

- The most-depended-on Book 3 proposition is **3.1** (find the center): cited by 3.2, 3.3, 3.4,
  3.8, 3.9 (corr.), 3.10 (corr.), 3.11, 3.12, 3.13, 3.14, 3.17, 3.18, 3.21, 3.25, 3.28, 3.29,
  3.34, 3.35 — 19 of 37 propositions. It is the load-bearing construction of the book.
- Second tier: **3.3** (3.4, 3.13, 3.14, 3.35, 3.36), **3.20** (3.21, 3.26-via?, 3.27), **3.31**
  (3.32, 3.33), **3.18** (3.19, 3.36, 3.37), **3.16 corr.** (3.17, 3.33, 3.37).
- Heaviest single proofs by citation count: 3.33 (1.23, 1.11, 1.10, 1.4, 3.16 corr., 3.32,
  3.31), 3.32 (1.11, 3.19, 3.31, 1.32, 3.22, 1.13), 3.36 (3.18, 2.6, 1.47, 1.12, 3.3).
- Only propositions with **zero** proposition citations: 3.5, 3.6 (rely on Def. 1.15 + C.N. 1
  alone).
- Book 2 is first needed at 3.35 (2.5) and 3.36 (2.6); Book 1's 1.47 (Pythagoras) enters at
  3.14, 3.35, 3.36; 1.32 (exterior angle) is the workhorse for 3.20, 3.22, 3.31, 3.32, 3.34.

---

## Gaps and caveats (disclosed, not rounded)

1. **Every "R Theory extension" cell for a Book 3 theorem is INCOMPLETE**, because no
   derivation of any 3.n theorem from Euclid's definitions/postulates exists in the audited
   corpus. This is a finding, not a failure of the search: the search covered all 23 rewrite
   book pages plus vol0, the notation ledger, and the dependency chain; circle-Euclid linkage
   in the corpus is confined to Books I–II (Book 4 §4.IV, itself MA-tagged).
2. **Scope of the numeric checks cited** (Book 2 carrier identity ~2e-16; Book 4 unit-locus
   1.42e-14 over 20,000 samples; 4.IV.P0 CN re-verification): these check analytic identities
   on declared coordinates; they do not check, and cannot be upgraded into, Euclid 3.n
   theorems.
3. **The TESS-India framing** was used as requested where a new constructive idea was
   needed: the honest constructive candidate is Book 4's Flower right angle (4.IV.P0) — a
   deduction anchored to constructible shape (native 60° sectors, bisection) with the metric
   deliberately withheld until Gate B. But 4.IV.P0 is not a proof of 3.31 and is recorded as
   CP, not as an extension of Book 3.
4. **R Theory-side statuses quoted above** (CP/CN/ST/MA/AA/P/A) are the rewrite pages'
   *self-reported* labels, read from the pages; I did not re-audit those computations in
   this task.
5. The encyclopedia article's remark that Proclus cites "the finding of the center of a
   circle" (3.1) as a *porism* is context only; it changes no status above.
