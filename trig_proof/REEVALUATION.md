# REEVALUATION — Deterministic Rebuild of the Cumulative Trigonometric Proof

**Date:** 2026-09-22. **Rebuild:** second pass, deterministic.
**First pass:** discarded (parallel workers raced on shared files).

## Why a rebuild was necessary

The first campaign pass (workflow `euclid-trig-cumulative`, run
`workflow-run-70c0ea659a8949b49106d5fe4cfaa67d`) dispatched concurrent
agents against a shared cumulative document. The result had:

- chapters out of book order;
- principle numbering collisions (bare ids reused across books;
  book-local P-schemes colliding with register rows);
- non-sequential, non-deterministic principle ids (e.g. "26 (Book 4)",
  "26 (Book 12)", "26 (Book 13)" as three different principles);
- duplicate folding (the same identity registered as new in two books);
- unverified dedup (some marked duplicate by numerical comparison, not
  algebra).

The raced document is preserved as evidence only. This rebuild was done
by a single coordinator: 10 independent per-book auditors wrote only
their `bookN_claims.md` files; the coordinator then wrote
`cumulative_trig_proof.md` sequentially, assigning P0–P61 in strict book
order with analytic (not numerical) dedup.

## Corrected per-book totals

See STATUS.md for the full table. Category totals from the corrected
claim files: **PROVED 502 · CHECKED 73 · ASSERTED 188 · INCOMPLETE 33**
(489/71/180/33 through Book 20; Books 21–22 evaluated 2026-09-26 added
6/2/5/0 and 7/0/3/0 respectively, no new principles).
Arithmetic inconsistencies in five books' own tallies are disclosed in
STATUS.md, not smoothed.

## Dependency chain (principle-level)

P0 (seed) → Book 0 (P1–P16: folded primitives, FlatWave, transfer) →
Book 1 (P17–P18: half-angle chart, octant values) →
Book 2 (P19–P24: Weierstrass, double-angle rationals, oscillator, logs,
arctan) → Book 3 (P25–P34: cophase/quarter-turn group, Möbius, sign laws;
P33–P34 conditional on quaternion import I6) →
Book 4 (P35–P36: 30°/60° from Euclid 4.15; 60° cosine law) →
Book 6 (P37–P38: operator Euler, CHI double-angle) →
Book 7 (P39–P42: λ-identities, companion cosine, log-derivative) →
Book 10 (P43–P44: hyperbolic half-angle; P44 conditional on Dirac
import I1) → Book 12 (P45–P46: reciprocal spine, (3,4,5) values) →
Book 13 (P47–P48: λ chart, cofunction symmetry) →
Book 14 (P49–P55: hyperbolic half-angle machinery; P51–P52 conditional
on two-body import) → Book 15 (P56–P57: complement interchange,
transfer-angle) → Book 16 (P58: hyperbolic Pythagorean) →
Book 17 (P59–P61: carrier 2:1 cover, cos4x structure, srx(π/8)).

Books 5, 8, 9, 11, 18, 19, 20 contribute no new principles (verified
duplicates, corollaries, or non-trig content — see the "not folded"
sections). Books 21–22 (evaluated 2026-09-26, stop lifted by Kit's
directive) likewise contribute no new principles: Book 21's trigonometric
content is P17/P19/P30/P49/P51 (verified analytically, not re-folded)
and Book 22's exact content is differential/symplectic geometry of the
(F,G) phase plane plus conditional reconstructions of imported physics;
see the Book 21 and Book 22 chapters and book21_claims.md /
book22_claims.md.

**No forward references.** Every principle's proof cites only
lower-numbered principles, M0, definitions, or named asserted imports.

## Old (raced) → new (deterministic) numbering map

The raced document's numbering is not mapped 1:1 — it was
non-sequential and collided. The correspondence for the principles that
survive:

| Raced id | New id | Identity |
|---|---|---|
| P0 (seed) | P0 | 4/sin(2x) identity |
| "1 (Book 0)"–"16 (Book 0)" | P1–P16 | Folded primitives … log representation |
| "17 (Book 2)" (half-angle chart) | P17 | Folded at Book 1 (first in book order) |
| "20 (Book 2)" (octant values) | P18 | Folded at Book 1 (first in book order) |
| "18 (Book 2)" (Weierstrass) | P19 | — |
| "19 (Book 2)" (rational double-angle) | P20 | — |
| "21 (Book 2)" (oscillator) | P21 | — |
| "22 (Book 2)" (cot double-angle) | P22 | — |
| "23 (Book 2)" (log antiderivatives) | P23 | — |
| "24 (Book 2)" (arctan) | P24 | — |
| "28 (Book 3)"–"47 (Book 3)" select | P25–P34 | Cophase/Möbius/sign laws (10 of 25 candidates) |
| "26 (Book 4)", "27 (Book 4)" | P35, P36 | 30°/60° values, 60° cosine law |
| "1 (Book 6)", "2 (Book 6)" | P37, P38 | Operator Euler, CHI double-angle |
| (Book 7, unnumbered in raced doc) | P39–P42 | λ-identities, companion cosine, log-derivative |
| "2 (Book 10)" (tanh half-angle) | P43 | — |
| "4 (Book 10)" (mass-shell chain) | P44 | Conditional (I1) |
| "27 (Book 12)" (reciprocal spine) | P45 | — |
| "28 (Book 12)" (native state) | P46 | — |
| "26 (Book 12)" (λ(1−λ)) | — | Duplicate of P39; not re-folded |
| "26 (Book 13)" (λ chart) | P47 | — |
| "27 (Book 13)" (λ symmetry) | P48 | — |
| "18 (Book 14)"–"25 (Book 14)" select | P49–P55 | Hyperbolic machinery (7 of 9; P17 dup of P43, P20 dup of P19) |
| "1 (Book 15)" (complement) | P56 | — |
| "6 (Book 15)" (transfer-angle) | P57 | — |
| "3 (Book 16)" (hyperbolic Pythag.) | P58 | — |
| "17 (Book 17)" (carrier cover) | P59 | — |
| "19 (Book 17)" (cos4x) | P60 | — |
| "20 (Book 17)" (srx(π/8)) | P61 | — |
| "18 (Book 17)" (rapidity) | — | Duplicate of P42; not re-folded |

Raced ids not in this table were duplicates, non-trig, or CHECKED-only
and were not folded.

## Unresolved / conditional principles and what would close them

1. **P33, P34** (PROVED-conditional on quaternion-model import I6,
   Book 3): ~~close by proving the quaternion axis-angle model from
   first principles, or by re-deriving q(θ+2π,n) = −q(θ,n) and
   ‖r‖ = tan(θ/2) without the import.~~ **CLOSED 2026-09-26.** Both
   re-derived from the unit-quaternion definition
   q(θ,n) = cos(θ/2) + sin(θ/2)·n without I6: P33 is M0 shift identities
   (no property of n used); P34 uses admitted definitions (quaternion
   norm, unit n, Rodrigues vector r = q_V/q₀) plus P17. I6's unproven
   content (Spin(3) ≅ S³, covering map, covering theory) is not used.
   Upgraded to PROVED — see P33/P34 addenda in cumulative_trig_proof.md
   and book3_claims.md register rows 20–21.
2. **P40** (companion cosine; PROVED on (0,π/2), off-chart analytic
   proof INCOMPLETE, Book 7): ~~close by extending the squaring+sign
   argument to the other three quadrants (sign bookkeeping for ε and
   the √ branch).~~ **CLOSED 2026-09-26.** The off-chart analytic proof
   exists (`T2_EPS_OFFCHART_PROOF.md`) and was independently re-verified
   here. The extension requires a CORRECTED sign factor:
   σ(x) = sgn(cos x + sin x); the stated ε = sgn(sin 2x) is falsified
   off-chart (counterexample x = 2π/3: stated RHS = +1/2 ≠ −1/2 =
   cos(4π/3)). Corrected identity PROVED for all real x — see P40
   addendum in cumulative_trig_proof.md. book7_claims.md updated
   (INCOMPLETE → PROVED); STATUS.md Book 7 row updated.
3. **P44** (PROVED-conditional on free-Dirac import I1, Book 10): ~~close
   by deriving the mass-shell parametrization E = mc²cosh α,
   pc = mc²sinh α within the campaign instead of importing it.~~
   **CLOSED 2026-09-26.** Derived from the admitted mass-shell premise
   E² − p²c² = m²c⁴ (m > 0, E > mc², p > 0): cosh:[0,∞) → [1,∞) is a
   bijection (continuous, strictly increasing, limits 1 and ∞), giving a
   unique α ≥ 0 with E = mc²cosh α; then p²c² = m²c⁴sinh²α and p > 0
   give pc = mc²sinh α. P44 is now PROVED, conditional only on the
   admitted mass-shell premise — see P44 addendum in
   cumulative_trig_proof.md and the book10_claims.md C3 note. The Dirac
   theory itself stays a named import.
4. **P51, P52** (PROVED-conditional on two-body import 14.II.P1,
   Book 14): ~~close by proving s/(2m₁m₂) = cosh λ_m + cosh η from the
   book's kinematics instead of importing it.~~ **ATTEMPTED 2026-09-26
   — NOT CLOSED.** 14.II.P1 (p₁·p₂ = m₁m₂cosh η,
   s = m₁²+m₂²+2m₁m₂cosh η) is labeled "Physics Import — standard
   two-particle relativity" by the book itself; the book's own 14.0
   boundary says it "inherits ... standard two-body kinematics." Deriving
   it inside the campaign would require building special-relativistic
   kinematics (Lorentz-invariant 4-momentum products) from the
   campaign's premises — out of proportion for a trigonometric campaign.
   Exact gap: the import itself; the algebraic consequence
   s/(2m₁m₂) = cosh λ_m + cosh η (with cosh λ_m := (m₁²+m₂²)/(2m₁m₂))
   is exact given the import and is already shown in P51's proof.
5. **Book 3, C28** (reciprocal compatibility surface): ~~the book file
   labels it CHECKED, the register PROVED-modulo-I3; independent
   re-derivation confirms the analytic substitution is complete, so it
   is PROVED-conditional here. The label conflict is disclosed, not
   hidden. It was not folded (algebraic, not trig).~~ **CLOSED
   2026-09-26.** Independent re-derivation completed and verified:
   C16's inverse u = (1−σ²)/(2σ) (verified) turns C27's
   u_{XY}u_{YZ}u_{ZX} = 1 (verified from the declared atlas I3) into
   (1−a²)(1−b²)(1−c²)/(8abc) = 1 with a,b,c > 0 — exact algebra.
   Upgraded to PROVED-conditional (declared RP²-atlas import I3) in
   book3_claims.md (C28 row, register row 25, counts 35/7/15/0);
   STATUS.md Book 3 row and totals updated. The B44 numeric run stands
   as cited corroboration.
6. **Book 7, 7.1.T2 off-chart branches:** ~~CHECKED numerically; analytic
   proof INCOMPLETE (stated gap). Does not affect P40 (principal chart).~~
   **CLOSED 2026-09-26** — same as item 2 above.

## Corrections applied during this rebuild

- **Book 1, T34:** source labels PROVED; it is an import by its own
  description → ASSERTED.
- **Book 1, T40:** "only earlier-numbered theorems" sub-claim is false
  (T24 cites T25 forward); no cycle (T25 does not cite T24). Noted.
- **Book 3, C5:** "independent of reference basis" imprecise; only the
  unlabeled partition is invariant. Proved substance kept.
- **Book 4, T2:** first embedding attempt inconsistent; corrected run
  is the cited one. Disclosed in book4_claims.md.
- **Book 7, 7.4.CL2:** manuscript sign error (printed
  2λ−1 = cos x − sin x); corrected 2λ−1 = sin x − cos x, PROVED.
- **Book 14, P22 (now P52):** scope corrected from PROVED to
  PROVED-conditional (inherits P21's asserted import).
- **Book 15, claim 24:** displayed dot product should be (2,2), not
  (2,1). Noted.
- **Book 16:** wording corrected (−16cos4φ_a positive at odd quarter
  phases); conditional proof's |a||b|≠0 requirement documented.
- **Book 17:** even/odd midpoint wording corrected (they divide the
  four carrier points).
- **Book 20:** Bloch-vector sign erratum documented; claim PROVED
  conditional on the standard Bloch convention.

## Self-evaluation

None. All 21 books were audited by independent subagents (10 workers
across two coordinators); the coordinator wrote only the deterministic
assembly. No book was evaluated by the same agent that wrote its proof
file.

## Books 21–22

**Evaluated 2026-09-26.** The campaign stop before Books 21–22 was lifted
by Kit's directive on 2026-09-26. Both books were evaluated claim by
claim from their rewrite pages (no `book21_proof.md` / `book22_proof.md`
exist; the earlier campaign covered Books 0–20 only). Neither book
invokes any proposition of Euclid's *Elements* as a premise, so no
ledger verification was required. **No new principles were folded** —
the register stands at P0–P61.

| Book | Evaluated | PROVED | CHECKED | ASSERTED | INCOMPLETE | New principles |
|---|---|---|---|---|---|---|
| 21 | 13 | 6 | 2 | 5 | 0 | — (0) |
| 22 | 10 | 7 | 0 | 3 | 0 | — (0) |

**Why nothing folded.** Book 21: the two-fermion invariant's R-form is
P30's Möbius map Q₊ in the q variable, and R(q)+R(q)⁻¹ = 2cosh λ is a
two-line corollary of P49 — so s = 2m₁m₂(cosh λ_m + cosh η) is P51's
premise form; u = tan(θ/2) is P19's Weierstrass form; u_pair = sxp(x)
is P17's half-angle tangent under the asserted imports. The rest is Lie
algebra, representation theory, analysis, empirics, imports, and
negatives. Book 22: the exact content is differential/symplectic
geometry of the (F,G) phase plane (Prüfer pair, the primitive symplectic
atlas) and conditional reconstructions of imported physics; no identity
about trigonometric functions, angles, or circular/hyperbolic measure
was found.

**New ASSERTED items and what would close them:**

1. Book 21's QCD import (quarks in 3, antiquarks in 3̄, gluons in 8,
   su(3) connection, V₃↔color-carrier contract) — closes only by
   deriving QCD from the campaign's own premises. **SKIPPED 2026-09-26:**
   deriving SU(3) gauge theory inside a trigonometric campaign is out of
   proportion; the import is standard physics, not trigonometry.
2. Book 21's Coulomb + radial Dirac–Coulomb imports (point-Coulomb
   Dirac equation, circular-state spinor-ratio theorem) — close by
   proving the imported theorems inside the campaign. **SKIPPED
   2026-09-26:** proving the Dirac–Coulomb spinor-ratio theorem from the
   campaign's premises is out of proportion for a trigonometric campaign.
3. Book 21's E8(−24) higher-carrier audit — ledger-cited, not proved in
   the text; closes by rerunning the project's Verification Ledger and
   its code. **SKIPPED 2026-09-26:** rerunning the Verification Ledger is
   a separate computational campaign, not a trigonometric proof.
4. Book 22's imported machinery (radial Dirac dynamics, first-order
   Einstein–Hilbert action, Maxwell, Kerr geometry, Einstein–Cartan)
   and the declared contracts C6a/C6b — close by deriving them inside
   the campaign. **SKIPPED 2026-09-26:** deriving general relativity,
   electrodynamics, and spin-torsion gravity from trigonometric premises
   is out of proportion for this campaign.
5. Book 22's Kerr/Kerr–Newman half-angle identities: the explicit
   formula is not stated on the rewrite page, so no identity could be
   verified or folded — closes by supplying the formula from the source
   T6 essay-book or the Kerr-geometry derivation. **ATTEMPTED 2026-09-26
   — NOT CLOSED.** Searched the workspace (book22 rewrite page §6, the
   symbol dictionary, staging notes, book14 page): every occurrence
   states the claim in words only ("the horizon radii satisfy exact
   half-angle identities in the book's coordinates") — no explicit
   formula exists anywhere in the workspace, and the source T6
   essay-book is not present. Exact gap: the formula itself.

**New INCOMPLETE items:** none.

## Euclid ledger impact

The only *Elements* propositions entering as logical premises are
Euclid 4.15, 1.5, 1.12, 1.26, 1.32, 1.47 (all in P35–P36, verified in
the ledgers). The campaign's standing boundary is unchanged: R Theory is
not proved a deductive extension of all of the *Elements*.

## Final exam (2026-09-26) — all 188 ASSERTED items adjudicated

Ledger: `FINAL_EXAM.md`. Verdicts: **PROVED 3** · **PERMANENT 179** ·
**NEEDS-INPUT 4** · **NEEDS-DERIVATION 2** (3 + 179 + 4 + 2 = 188 ✓).

- **PROVED 3:** Book 1 T34 (Exam Proof E1 — uniqueness of continuous
  extension, completing the correction noted above); Book 3 C45 (Exam
  Proof E3 — the quaternion double cover S³ → SO(3), so SI import I6 is
  now derived, not imported); Book 20 B0 (Exam Proof E2 — the one-generator
  reduction, satisfying the pending premise). STATUS.md: PROVED 504 → 507,
  ASSERTED 188 → 185.
- **PERMANENT 179:** correctly remain ASSERTED by design (declared
  premises, imports, conventions, audit verdicts, scope declarations,
  open-gate records). Not failures.
- **NEEDS-INPUT 4** (Kit's actionable items): 17.A6 (**S_F**, **the 1820
  projector**, **downstream contraction inputs**); 17.A7 (**the physical
  role of 638.78** in the Clifford contraction); 19.T10b (**FLAG-A1's
  per-contact 1/4**); 19.T19 (**S_F**, **N_1820**, **ζ_parent**, **η_{−4}**,
  **c_ord**, **K_parent**, **P_54** where still open in source scope,
  **role of 638.78**, **C3/C4 forcing**).
- **NEEDS-DERIVATION 2** (OUT-OF-PROPORTION, carried gaps): 12.A2 and
  14.4 — both are the same missing block: two-body special-relativistic
  kinematics derived from campaign premises (the 2026-09-26 carried gap;
  P51/P52 territory). Out of proportion: no identity in either book depends
  on the closed form.
