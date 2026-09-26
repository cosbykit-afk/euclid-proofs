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
claim files: **PROVED 489 · CHECKED 71 · ASSERTED 180 · INCOMPLETE 33.**
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
sections).

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
   Book 3): close by proving the quaternion axis-angle model from
   first principles, or by re-deriving q(θ+2π,n) = −q(θ,n) and
   ‖r‖ = tan(θ/2) without the import.
2. **P40** (companion cosine; PROVED on (0,π/2), off-chart analytic
   proof INCOMPLETE, Book 7): close by extending the squaring+sign
   argument to the other three quadrants (sign bookkeeping for ε and
   the √ branch).
3. **P44** (PROVED-conditional on free-Dirac import I1, Book 10): close
   by deriving the mass-shell parametrization E = mc²cosh α,
   pc = mc²sinh α within the campaign instead of importing it.
4. **P51, P52** (PROVED-conditional on two-body import 14.II.P1,
   Book 14): close by proving s/(2m₁m₂) = cosh λ_m + cosh η from the
   book's kinematics instead of importing it.
5. **Book 3, C28** (reciprocal compatibility surface): the book file
   labels it CHECKED, the register PROVED-modulo-I3; independent
   re-derivation confirms the analytic substitution is complete, so it
   is PROVED-conditional here. The label conflict is disclosed, not
   hidden. It was not folded (algebraic, not trig).
6. **Book 7, 7.1.T2 off-chart branches:** CHECKED numerically; analytic
   proof INCOMPLETE (stated gap). Does not affect P40 (principal chart).

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

**Not started.** The campaign stops at Book 20 by explicit directive.
No claim files, no principles, no evaluation exists for Books 21–22.

## Euclid ledger impact

The only *Elements* propositions entering as logical premises are
Euclid 4.15, 1.5, 1.12, 1.26, 1.32, 1.47 (all in P35–P36, verified in
the ledgers). The campaign's standing boundary is unchanged: R Theory is
not proved a deductive extension of all of the *Elements*.
