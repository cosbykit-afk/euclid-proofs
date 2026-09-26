# Book 8 Ledger — Continued Proportion and Mean Proportionals

Source: `~/workspace/euclid_work/text/book8.txt` (Fitzpatrick/Heiberg English translation, Greek alongside).
Worker: Book-8 campaign worker, 2026-09-21. Read from the file; not from memory.

## Book summary

Book 8 (27 propositions, 8.1–8.27; Propositions 1–2 plus one corollary) is the second book
of the arithmetic sequence (Books 7–9, attributed to the Pythagorean school). It develops
**continued proportion** for numbers: least sets in a given ratio, mean proportionals
between squares, cubes, similar plane numbers, and similar solid numbers. It relies on
Book 7's arithmetic definitions and propositions plus Book 5's definitions of duplicate
(Def. 5.9) and triplicate (Def. 5.10) ratio.

**No new definitions, postulates, or common notions are introduced in Book 8 itself.**
All definitions it uses are inherited:

- Def. 7.15 (multiplication as measure), 7.16, 7.17, 7.18 (product-ratio lemmas)
- Def. 7.20 (proportion of numbers: a:b :: c:d iff equimultiples), 7.21 (similar plane/solid
  numbers), 7.22 (least numbers of a ratio are prime to one another)
- Def. 5.9 (duplicate ratio of three continued proportionals), Def. 5.10 (triplicate ratio
  of four continued proportionals)

Dependency backbone: 8.1 (least-set criterion) and 8.2 (construction of least continued
proportional sets, with the corollary that 3-term least sets have square extremes and
4-term least sets cube extremes) are used by 8.3, 8.4 (the multi-ratio chaining tool, a long
two-case construction using 7.34/7.35 lcm machinery), 8.6, 8.8, 8.9, 8.13, 8.21, 8.26, 8.27.
Propositions 8.11/8.12 (mean proportional between squares / two mean proportionals between
cubes, plus duplicate/triplicate ratio claims) feed 8.14/8.15 and 8.18/8.19; 8.20/8.21
(the converses: mean proportional ⇒ similar plane; two mean proportionals ⇒ similar solid)
feed 8.22/8.23 and 8.24/8.25.

**Known defect (per the translator's footnote in the source text):** the proof of 8.20
contains a defective step — it is not demonstrated that F × E = C (and the step shown
is unnecessary for the conclusion). This does not affect the later dependence chain in the
translation's presentation, but it is recorded here rather than smoothed over.

## Proposition inventory

Format: number | statement (one line) | Euclid proof dependencies (from the proof text)
| R Theory extension | scope label.

| # | Statement | Euclid dependencies | R Theory extension | Scope |
|---|---|---|---|---|
| 8.1 | If the outermost of a continued proportional set are prime to one another, the set is least in that ratio | 7.14 (via equality), 7.21, 7.20 | None found — no documented extension claim builds on it | n/a |
| 8.2 | Construction: given least ratio pair A:B, produce the least continued proportional sets of 3, 4, … terms (Corollary: 3-term least sets have square extremes; 4-term, cube extremes) | 7.17, 7.18, 7.22, 7.27, 8.1 | None found | n/a |
| 8.3 | Converse: a least continued proportional set has prime outermost | 7.33, 7.22, 8.2, 8.2 corollary, 7.27 | None found | n/a |
| 8.4 | Given several ratios in least terms, construct the least continued proportional numbers realizing them in sequence | 7.34, 7.35, 7.20, Def. 7.20, 7.13 (two cases: next divisor measures / does not measure) | None found | n/a |
| 8.5 | Ratio of plane numbers is compounded (multiplied) out of the ratios of their sides | 8.4, 7.17, 7.16, 7.14 | None found | n/a |
| 8.6 | If the first term of a continued proportional set does not measure the second, no term measures any other | 7.33, 7.14, Def. 7.20, 8.3 | None found | n/a |
| 8.7 | If the first term measures the last, it measures the second | 8.6 (contrapositive) | None found | n/a |
| 8.8 | The number of mean proportionals between two numbers is preserved when the ratio is transported to another pair with the same ratio | 7.33, 8.3, 7.14, 7.21, 7.20, Def. 7.20 | None found | n/a |
| 8.9 | Between coprime A,B, as many mean proportionals fall between A,B as between each of A,B and the unit | 7.33, 8.2, 8.2 corollary, Def. 7.20, Def. 7.15 | None found | n/a |
| 8.10 | Converse of 8.9: the unit-anchored mean-proportional count transports back between the two numbers | Def. 7.20, Def. 7.15, 7.17, 7.18 | None found | n/a |
| 8.11 | Between two square numbers one mean proportional exists; the square-to-square ratio is the duplicate (squared) ratio of side-to-side | 7.17, 7.18, Def. 5.9 | None found | n/a |
| 8.12 | Between two cube numbers two mean proportionals exist; the cube-to-cube ratio is the triplicate (cubed) ratio of side-to-side | 7.17, 7.18, Def. 5.10 | None found | n/a |
| 8.13 | Squaring/cubing every term of a continued proportional set preserves continued proportionality | 7.14 (via equality, with the 8.11/8.12 constructions) | None found | n/a |
| 8.14 | Square measures square ⇔ side measures side (both directions) | 8.11, 8.7, Def. 7.20 | None found | n/a |
| 8.15 | Cube measures cube ⇔ side measures side (both directions) | 8.12, 8.7, Def. 7.20 | None found | n/a |
| 8.16 | Contrapositive of 8.14: square does not measure square ⇔ side does not measure side | 8.14 | None found | n/a |
| 8.17 | Contrapositive of 8.15: cube does not measure cube ⇔ side does not measure side | 8.15 | None found | n/a |
| 8.18 | Between two similar plane numbers one mean proportional exists; the ratio is the duplicate ratio of corresponding sides | Def. 7.21, 7.13, 7.17, Def. 5.9 | None found | n/a |
| 8.19 | Between two similar solid numbers two mean proportionals exist; the ratio is the triplicate ratio of corresponding sides | Def. 7.21, 7.13, 7.17, 7.18, 8.18, Def. 5.10 | None found | n/a |
| 8.20 | One mean proportional between two numbers ⇒ they are similar plane numbers (proof has a defective step — see summary) | 7.33, 7.20, Def. 7.15, 7.17, 7.13, Def. 7.21 | None found | n/a |
| 8.21 | Two mean proportionals between two numbers ⇒ they are similar solid numbers | 8.2, 8.3, 8.20, 7.14, 7.21, 7.20, Def. 7.15, 7.18, Def. 7.21 | None found | n/a |
| 8.22 | Three continued proportionals with square first term have square third term | 8.20, Def. 7.21 | None found | n/a |
| 8.23 | Four continued proportionals with cube first term have cube fourth term | 8.21, Def. 7.21 | None found | n/a |
| 8.24 | Similar plane numbers are in the ratio of a square to a square | 8.18, 8.8, 8.2, 8.2 corollary | None found | n/a |
| 8.25 | Similar solid numbers are in the ratio of a cube to a cube | 8.19, 8.8, 8.2, 8.2 corollary | None found | n/a |
| 8.26 | Similar plane numbers have the ratio of some square to some square | 8.18, 8.2, 8.2 corollary | None found | n/a |
| 8.27 | Similar solid numbers have the ratio of some cube to some cube | 8.19, 8.2, 8.2 corollary | None found | n/a |

(8.26/8.27 as stated in this translation are restatements of 8.24/8.25 proved via the
8.2 least-set construction with square/cube extremes; the proof texts match the
8.2-corollary route.)

## R Theory extension mapping — finding: no documented extension claims

I searched the rewrite series (`book0`–`book22`, `vol4`, `vol4-audit`), the Volume IV
notation ledger (`~/workspace/vol4/NOTATION_LEDGER.md`), and the dependency chain
(`~/workspace/vol4/DEPENDENCY_CHAIN.md`) for: "continued proportion", "mean
proportional", "duplicate ratio", "triplicate ratio", "Elements 8.", "Proposition 8.".
**Zero hits.** R Theory's Euclid contact is entirely with Euclid's *geometry* (Books 1–6:
constructions, congruence, the parallel postulate region), not with the arithmetic of
Books 7–9. The manuscript's "built as an extension of Euclid's work" claim is
documented at Book 4 §4.X ("Euclidean postulate audit"), which (a) imports only the
geometric substrate as premises P4.1 / P4.1-C / P4.3 (all scope-labeled **AA** —
assumed axioms), and (b) states the **No-Euclid-wholesale theorem (4.X.H)**: the theory
does not import Euclid's postulates as a block. Nothing in the corpus draws on any
proposition 8.1–8.27.

**Explicitly not claimed here:** modern analogues are *not* extension claims. E.g. the
R3a result `Sym²(128) = 1 + V(w4) + V(2w8)` with Casimir eigenvalues 0/48/64 (now a
CP theorem, `~/workspace/icloud_pyto/rebuilt/PROOFS_Casimir.md` K-1..K-9) is formally
a symmetric-square decomposition, and 8.11 is formally a statement about squaring a
ratio — but the R Theory work derives it from Clifford/representation theory, cites no
Book 8 proposition, and asserts no lineage. Treating them as the same claim would be
rounding up a status that the corpus does not assert. Per Kit's standard, I record the
formal parallel and mark it as **not an extension claim**.

## New axioms/definitions the extension introduces beyond Euclid

These are the theory's load-bearing assumptions at its Euclid contact point
(Book 4 §4.X and Book 5). They are **asserted, not proved from Euclid** — the audit
scope-labels them AA (assumed axiom) and A (Axiom Zero). Book 8 itself adds no
definitions or postulates, so the comparison baseline is Books 7's and 5's arithmetic
definitions plus the geometric substrate.

1. **Axiom Zero (A0.1, A0.2)** — Book 5. "Primitive diagonal noncoupling of a doubled
   carrier": independent partner U♯, declared block-compatible pairing ι, direct sum
   W = U ⊕ U♯, real–imaginary independence, dim ℝ W = 5+5 = 10. Granted, not proved;
   the audit's "What this book does not establish" list states explicitly: "Axiom Zero
   itself — the independence, the pairing data, and the primitive noncoupling are
   granted, not proved." Scope: **ASSERTED**.
2. **P4.1 (pre-metric construction substrate)** — Book 4 §4.X. Points, straight
   continuation, copied congruence unit r, equal-circle operation, continuous triangular
   filling. This is a *selected subset* of Euclidean-constructive material, not the
   postulates themselves. Scope: **ASSERTED** (AA).
3. **P4.1-C (SSS congruence principle)** — Book 4 §4.X. Admitted as a congruence
   principle alongside P4.1. Scope: **ASSERTED** (AA).
4. **P4.3 (global Euclidean declaration)** — Book 4 §4.X. Global flatness and unique
   parallels are a *separate declaration*, not derived from the local synthetic work;
   "no arrow reversible without a new theorem". Scope: **ASSERTED** (AA).
5. **Gates A–H / no-novelty-from-coordinate-change rule (4.X.I = Gate H)** — Book 4
   §4.X. Methodological declarations (rules about how the argument may be read),
   including the No-Euclid-wholesale theorem (4.X.H). These are rules of the audit
   itself, not mathematical theorems. Scope: **ASSERTED** (declarations).
6. **Flower geometry construction primitives** — Book 4 §§4.IV. Six native sectors,
   the synthetic right-angle construction, rank-two/rank-three carriers. These are
   *new* constructive definitions with no counterpart in Euclid (proved where marked
   CP, e.g. Lemma 4.IV.L1). The new definitions are: the Flower plane construction,
   native-sector decomposition, rank-vs-dimension gate language. Scope: mixed
   **PROVED** (CP items) / **ASSERTED** (the imported premises feeding them).

No new axiom or definition in the extension derives from, specializes, or generalizes
any proposition of Book 8. The extension's Book-8-relevant scorecard is therefore: no
PROVED, no CHECKED, no ASSERTED extension claims; all 27 rows are "none found", which
is itself the complete finding.

## Method notes and caveats

- Proposition statements and dependency lists were extracted directly from the proof
  texts in `book8.txt`; cited bracket references (e.g. "[Prop. 7.14]") are the
  translator's and were verified against the local argument each cites.
- Scope labels: the task's PROVED/CHECKED/ASSERTED/INCOMPLETE labels apply to
  *extension claims*; since the corpus contains no extension claims touching Book 8,
  every row is "none found" rather than a label. This is not a gap in the search — the
  corpus-wide grep returned zero hits for every Book-8-specific term.
- The 8.20 defective-step note comes from the translator's footnote in the source
  file, not from independent verification by this worker (marked INCOMPLETE as a
  claim about the proof's correctness beyond the translator's word).
