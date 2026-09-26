# Book 7 — Euclid Extension Ledger

**Source text:** `/home/hatch/workspace/euclid_work/text/book7.txt` (Fitzpatrick/Heiberg
English translation with Greek alongside; page images pp. 193–225).
**Historical context:** `/home/hatch/workspace/user/files/euclid-encyclopedia-article.html`.
**Creative-deductive framing:** `/home/hatch/workspace/user/files/a3cd8c26d8eb63f6315ac09d5f1d1ef5071b2fe3.pdf`.
**R Theory side:** `/home/hatch/workspace/r-theory-rewrite/bookM/index.html` (all M=0..22,
plus `vol0/`, `vol4/`), `~/workspace/vol4/NOTATION_LEDGER.md`, `~/workspace/vol4/DEPENDENCY_CHAIN.md`.

**Scope key (task vocabulary):**
- **PROVED** — deductive proof from Euclid's definitions/postulates/propositions shown.
- **CHECKED** — verified by a completed computation (computation described).
- **ASSERTED** — manuscript stipulation or new axiom (e.g. anything like "Axiom Zero").
- **INCOMPLETE** — not established; reason stated.

Kit's rule is enforced throughout: what the theory does not claim, build on, or prove is
marked INCOMPLETE and the gap is stated, not filled with interpretation.

---

## Book summary

Book 7 is Euclid's elementary number theory (the encyclopedia article: Books VII–IX are
arithmetical, "generally attributed to the school of Pythagoras"; the proportion theory in
7.4–7.19 is the older Pythagorean theory for commensurables, not the general Book V
theory; final group 7.33–7.39 treats least common multiples).

**Inventory:** 22 definitions (Def 7.1–7.22), **0 postulates**, **0 common notions**,
39 propositions (7.1–7.39). The zero count is verified by reading the full text: Book 7
states no postulates and no common notions of its own. Its proofs rely on the Book 1
common notions implicitly, plus two unstated ones the translator flags in footnotes at
7.1/7.2: (a) if *a* measures *b* and *b* measures *c* then *a* measures *c*; (b) if *a*
measures *b* and *a* measures a part of *b* then *a* measures the remainder of *b*.
Internal structure: 7.1–7.3 the Euclidean algorithm / greatest common measure;
7.4 part-or-parts; 7.5–7.19 arithmetic theory of proportion (part/parts arithmetic,
alternando, componendo, ex aequali, *ad = bc* ↔ proportion); 7.20–7.29 coprimality and
least-ratio numbers; 7.30 Euclid's lemma; 7.31–7.32 prime divisors; 7.33–7.39 least
numbers in a ratio / least common multiples / named parts. Two propositions also cite
outside Book 7: 7.19 cites Book 5 (5.7, 5.9); 7.33 cites Book 5 (5.13); 7.24 cites
Book 6 (6.15).

**TESS-India framing:** that document's theme is linking shape/space with ratio,
deduction, and mathematical proof. Applied honestly to Book 7, its lesson lands as a
negative: the R Theory extension draws its "new constructive ideas" from geometry
(Axiom Zero's decadic doubling, the Flower-plane synthetic substrate), not from Book 7's
arithmetic. No Book 7 proposition supplies a constructive idea the extension reuses.

**Headline finding (stated first, per Kit's rule):** R Theory builds on Euclid's
*geometric* program (Books 1–6, re-presented through the Flower-plane synthetic
construction in R Theory Book 4 and the declared Euclidean carriers in Books 0–6). It
builds on **none** of Book 7's number-theoretic propositions. The only arithmetic facts
the theory uses are elementary integer computations stated as standard lemmas, not as
extensions of Euclid's proofs. Book 12 explicitly *rejects* the one number-theoretic
program Euclid 7–8 style reasoning would suggest (rational-lattice mass matching):
"The direct harmonic search — hunting mass ratios in musical lattices — closes
negatively" and "finding a close rational is numerology with[parts-per-10⁷ precision]."

---

## Definition inventory (Def 7.1–7.22)

Definitions have no proof dependencies. None is extended by R Theory; each row states
exactly what (if anything) the theory does with the concept.

| Def | One-line statement | Euclid proof deps | R Theory extension | Scope |
|---|---|---|---|---|
| 7.1 | A unit (μονάς) is that by which each existing thing is said to be one. | — | None. R Theory works over ℝ/ℂ carriers and trig primitives; it never defines or uses a Euclidean unit, and no claim in the series is built on Def 7.1. | **INCOMPLETE** — no extension claim exists in the corpus; reason: the theory has no unit concept to extend. |
| 7.2 | A number is a multitude composed of units (i.e. a positive integer > 1). | — | None. The theory's objects are real/complex quantities, not multitudes of units. | **INCOMPLETE** — no claim builds on it. |
| 7.3 | A number *a < b* is a *part* of *b* when *a* measures *b* (some *n* with *na = b*). | — | None. | **INCOMPLETE** |
| 7.4 | A number is *parts* of another when it does not measure it. | — | None. | **INCOMPLETE** |
| 7.5 | The greater is a *multiple* of the lesser when measured by it. | — | None. | **INCOMPLETE** |
| 7.6 | Even number: divisible in half. | — | None. | **INCOMPLETE** |
| 7.7 | Odd number: not divisible in half / differs from an even by a unit. | — | None. | **INCOMPLETE** |
| 7.8 | Even-times-even: product of two evens. | — | None. | **INCOMPLETE** |
| 7.9 | Even-times-odd: product of an even and an odd. | — | None. | **INCOMPLETE** |
| 7.10 | Odd-times-odd: product of two odds. | — | None. | **INCOMPLETE** |
| 7.11 | Prime: measured by a unit alone. | — | None. R Theory never defines or uses "prime number" (the term does not occur in the series; audit ledgers contain no prime-number claims). | **INCOMPLETE** — reason: prime numbers play no role in the theory. |
| 7.12 | Relatively prime: measured by a unit alone as common measure. | — | Nearest touch only: R Theory Book 11, §11.IX uses the *elementary fact* gcd(3,2) = 1 as a lemma — primitivity of the integral cocharacter X = i(3I₂ ⊕ −2I₃); weights x(p,q) = 3p − 2q verified exactly ("CHECKED PROOF", formal home §11.IX.A–C, Thm 11.IX.T1, Cor 11.IX.C1; ledger NOTATION_LEDGER.md: `X … CLEAN, V4: gcd(3,2) = 1`). This is **not** derived from Euclid's definition and **not** an extension of it; it is a one-line arithmetic lemma used as a standard import. | R Theory claim **CHECKED** (exact integer verification of the weights + elementary gcd(3,2)=1); the *extension mapping* itself is **INCOMPLETE** — no claim in the theory extends or re-proves Euclid's Def 7.12. |
| 7.13 | Composite: measured by some number. | — | None. | **INCOMPLETE** |
| 7.14 | Composite to one another: some common measure exists. | — | None. | **INCOMPLETE** |
| 7.15 | Multiplication: *a* multiplies *b* when *b* is added to itself as many times as there are units in *a*. | — | None (the theory's products are ring products of functions/matrices, never this repeated-addition definition). | **INCOMPLETE** |
| 7.16 | Plane number: product of two numbers, with the factors as sides. | — | None. | **INCOMPLETE** |
| 7.17 | Solid number: product of three numbers. | — | None. | **INCOMPLETE** |
| 7.18 | Square number: equal × equal. | — | None. | **INCOMPLETE** |
| 7.19 | Cube number: equal × equal × equal. | — | None. | **INCOMPLETE** |
| 7.20 | Proportional: first is the same multiple/part/parts of the second as the third is of the fourth. | — | None. R Theory never adopts the part/parts definition of proportion. Its ratio identities (reciprocal products = 1, Möbius maps, Casimir ratios C_A/C_F = 9/4 in Book 12) are proved by modern algebra/trigonometry, not from Def 7.20. | **INCOMPLETE** — reason: the series contains no theory of numerical proportion; the encyclopedia article's note applies here (Book 7's is the old Pythagorean theory, and the theory does not revive it). |
| 7.21 | Similar plane/solid numbers: proportional sides. | — | None. | **INCOMPLETE** |
| 7.22 | Perfect number: equal to the sum of its own parts (factors). | — | None. | **INCOMPLETE** |

---

## Proposition inventory (7.1–7.39)

Dependencies are taken from the bracketed citations in the proof text ([Prop. X.Y],
[Def. X.Y], [Prop. 7.2 corr.]) plus the translator's footnoted unstated common notions.

| Prop | One-line statement | Euclid proof dependencies | R Theory extension | Scope |
|---|---|---|---|---|
| 7.1 | Continued-subtraction algorithm: unequal numbers whose remainders never divide until a unit remains are coprime (Euclidean-algorithm correctness). | Def 7.12; unstated CN (transitivity of "measures"; remainder measuring). | None. R Theory contains no Euclidean-algorithm computation. | **INCOMPLETE** — no claim builds on it. |
| 7.2 | Find the greatest common measure of two non-coprime numbers by continued subtraction; corollary: every common measure divides the GCD. | 7.1 (cited "[Prop. 7.1]"); unstated CN. | None. | **INCOMPLETE** |
| 7.3 | GCD of three given non-coprime numbers (iterate 7.2). | 7.2, 7.2-corollary (3 citations). | None. | **INCOMPLETE** |
| 7.4 | Every lesser number is part or parts of every greater. | 7.2 (takes the GCD). | None. | **INCOMPLETE** |
| 7.5 | If a = (1/n)b and c = (1/n)d then a + c = (1/n)(b + d). | None cited (elementary from definitions). | None. | **INCOMPLETE** |
| 7.6 | If a = (m/n)b and c = (m/n)d then a + c = (m/n)(b + d). | 7.5 (cited). | None. | **INCOMPLETE** |
| 7.7 | If a = (1/n)b and c = (1/n)d then a − c = (1/n)(b − d). | 7.5 (cited). | None. | **INCOMPLETE** |
| 7.8 | Same for parts: (m/n) remainder rule. | 7.5 (2 citations). | None. | **INCOMPLETE** |
| 7.9 | Alternando for equal parts: a = (1/n)b, c = (1/n)d, a = (k/l)c ⇒ b = (k/l)d. | 7.5, 7.6 (cited "[Props. 7.5, 7.6]"). | None. | **INCOMPLETE** |
| 7.10 | Alternando for parts. | 7.9 (2 citations), 7.5, 7.6 (cited). | None. | **INCOMPLETE** |
| 7.11 | a:b :: c:d and a−c:d−... → (a−c):(b−d) :: a:b. | Def 7.20, 7.7, 7.8 (cited). | None. | **INCOMPLETE** |
| 7.12 | a:b :: c:d → a:b :: (a+c):(b+d) (componendo). | Def 7.20, 7.5, 7.6 (cited). | None. | **INCOMPLETE** |
| 7.13 | Proportions alternate: a:b :: c:d → a:c :: b:d. | Def 7.20, 7.9, 7.10 (cited). | None. | **INCOMPLETE** |
| 7.14 | Ex aequali for numbers: a:b :: d:e and b:c :: e:f → a:c :: d:f. | 7.13 (3 citations). | None. | **INCOMPLETE** |
| 7.15 | Unit–number measure alternation (special case of 7.9, per translator note). | 7.12 (cited), Def 7.20. | None. | **INCOMPLETE** |
| 7.16 | Commutativity: a×b = b×a. | Def 7.15, 7.15 (Prop, cited). | None. (The theory's ab = ba instances are matrix/operator commutativities, proved independently, not from this.) | **INCOMPLETE** |
| 7.17 | (a×b):(a×c) :: b:c. | Def 7.15, Def 7.20, 7.13 (cited). | None. | **INCOMPLETE** |
| 7.18 | (a×c):(b×c) :: a:b. | 7.16, 7.17 (cited). | None. | **INCOMPLETE** |
| 7.19 | a:b :: c:d ↔ ad = bc (the proportion–rectangle equivalence; the converse uses Book 5). | 7.17, 7.18 (cited); 5.9, 5.7 (Book 5, cited for the converse). | None. | **INCOMPLETE** |
| 7.20 | Least-ratio numbers divide any others in that ratio equally, greater the greater, lesser the lesser. | 7.12, 7.4, Def 7.20, 7.13 (all cited). | None. | **INCOMPLETE** |
| 7.21 | Coprime numbers are least in their ratio. | 7.20, 7.16 (cited). | None (see Def 7.12 row: the theory uses coprimality once as an elementary lemma, never this theorem). | **INCOMPLETE** |
| 7.22 | Least in a ratio are coprime. | Def 7.15, 7.17 (cited). | None. | **INCOMPLETE** |
| 7.23 | d divides a and gcd(a,b) = 1 ⇒ gcd(d,b) = 1. | None cited (unstated transitivity of "measures"). | None. | **INCOMPLETE** |
| 7.24 | gcd(a,c) = gcd(b,c) = 1 ⇒ gcd(ab,c) = 1. | 7.23, 7.16 (cited); Def 7.15; 6.15 (Book 6, cited for rectangle→proportion); 7.19, 7.21, 7.20 (cited). | None. | **INCOMPLETE** |
| 7.25 | gcd(a,b) = 1 ⇒ gcd(a²,b) = 1. | 7.24 (cited). | None. | **INCOMPLETE** |
| 7.26 | a,b coprime to c,d respectively ⇒ gcd(ab,cd) = 1. | 7.24 (cited). | None. | **INCOMPLETE** |
| 7.27 | Coprime bases have coprime powers (a² vs b², a³ vs b³, etc.). | 7.25, 7.26 (cited). | None. | **INCOMPLETE** |
| 7.28 | gcd(a,b) = 1 ⇒ gcd(a+b,a) = gcd(a+b,b) = 1; converse holds. | None cited. | None. | **INCOMPLETE** |
| 7.29 | Prime p not dividing a ⇒ gcd(a,p) = 1. | Def 7.11 (cited). | None (prime numbers unused in the theory). | **INCOMPLETE** |
| 7.30 | Euclid's lemma: prime p dividing a×b divides a or b. | 7.29, Def 7.15, 7.19, 7.21, 7.20 (all cited). | None. | **INCOMPLETE** |
| 7.31 | Every composite is measured by some prime (infinite-descent argument). | None cited. | None. | **INCOMPLETE** |
| 7.32 | Every number is prime or measured by some prime. | 7.31 (cited). | None. | **INCOMPLETE** |
| 7.33 | Least numbers in the ratio of any given multitude. | 7.22, 7.3, 7.15, 7.19 (cited); 5.13 (Book 5, cited). | None. | **INCOMPLETE** |
| 7.34 | Find the least number measured by two given numbers (LCM). | 7.16, 7.33, 7.19, 7.21, 7.20, 7.17 (all cited). | None. | **INCOMPLETE** |
| 7.35 | If two numbers both measure some number, their LCM also measures it. | None cited. | None. | **INCOMPLETE** |
| 7.36 | LCM of three given numbers. | 7.34, 7.35 (cited). | None. | **INCOMPLETE** |
| 7.37 | b dividing a ⇒ a has a part named after b ("b-th part"). | 7.15 (cited). | None. | **INCOMPLETE** |
| 7.38 | a having a named part ⇒ the name-number divides a. | 7.15 (cited). | None. | **INCOMPLETE** |
| 7.39 | Find the least number having given named parts. | 7.36, 7.37, 7.38 (cited). | None. | **INCOMPLETE** |

**Honesty note on the whole table:** every "R Theory extension" entry above is "None"
because a full-text search of the rewrite series (`book0/`–`book22/`, `vol0/`, `vol4/`,
`tables/`) finds no use of Euclid's algorithm, coprimality theorems, Euclid's lemma,
prime-divisor theory, or least-common-multiple theory, and the two audit records
(`NOTATION_LEDGER.md`, `DEPENDENCY_CHAIN.md`) contain exactly one number-theoretic
item: the Book 11 gcd(3,2) = 1 lemma (Def 7.12 row above). The manuscript originals
likewise reference Euclid only as Euclidean geometry (the "reciprocal Pythagorean
identities" are trigonometric identities, not Euclid's number theory).

---

## New axioms / definitions introduced by the extension beyond Euclid

These are the load-bearing assumptions — stated exactly, with their series status.
None of them is proved from Euclid's definitions, postulates, or propositions.

1. **Axiom Zero (Book 5, A0.1–A0.2).** Declared block-compatible linear isomorphism
   ι: U → U♯ between a 5-dim real carrier U and an *independent* isomorphic partner
   U♯, primitive diagonal noncoupling, W = U ⊕ U♯, dim ℝ W = 10 (Decadic Carrier
   Theorem conditional on the axiom). Series status: **A** (assumption/axiom) —
   "granted, not proved"; k = 2, 4 counterfactual completions are "lawful
   mathematical completions, excluded only by the adopted independence axiom".
   → **ASSERTED**.

2. **Anti-circularity firewall (Book 5).** Methodological declaration: later physics
   (E6/E8, generations, CKM, strings, cosmology) may test or contextualize the decadic
   carrier but never retroactively justify Axiom Zero. A rule about how the argument
   may be read, not a theorem. → **ASSERTED**.

3. **Book 4 pre-metric Import statement.** Admits: points may be joined, straight
   segments continuously extended, one construction length copied congruently, equal
   circles drawn and intersected, triangular faces continuously filled — *without*
   assuming a Euclidean inner product, Cartesian coordinates, Pythagorean distance,
   numerical angle, or the parallel postulate. The manuscript re-presents the proofs
   of the historical Flower-plane books "included, not merely cited"; the audit
   records the synthetic proofs as read but not machine-checked (Book 8 page:
   "The Volume I ledger records the synthetic Flower proofs (Book 4) as read but not
   machine-checked"). → **ASSERTED** (import + re-presentation claim).

4. **Index divisibility, Book 16 (Theorem 16.I.104.T1): Ind(D₁₆) ∈ 4ℤ.**
   Series status **MA** (manuscript assertion): "whose topological proof is asserted,
   not re-derived, in this chunk." The oriented Fujikawa closure J(R_D) =
   e^(−iπ·4k/2) = 1 for all integer k (104.T2) is exact **conditional** on it
   (series: CP conditional; per task vocabulary → **CHECKED** conditional on the
   ASSERTED divisibility). → divisibility itself **ASSERTED**.

5. **Orientation declarations (Books 0/1).** "Once an oriented Euclidean two-plane is
   declared, exactly one orthogonal complex structure is compatible" — the declaration
   is a stipulation; what is proved from it (J ↔ −J under reversal) is proved, the
   declaration itself is not. → **ASSERTED**.

6. **Global-quotient / primitivity data (Book 11, §11.IX.A–C).** The global group
   (not just its Lie algebra) fixes the primitive integral cocharacter
   X = i(3I₂ ⊕ −2I₃); primitivity via the elementary gcd(3,2) = 1; six weights
   x(p,q) = 3p − 2q verified exactly (series: CHECKED PROOF). The *computation*
   is exact; the step "the global group fixes this cocharacter" is the theory's own
   Lie-theoretic construction, not a consequence of Euclid. → computation
   **CHECKED**; its role as an extension of Euclid: none (see Def 7.12 row).

7. **Book 12 negative result (worth listing because it is load-bearing honesty):**
   the direct harmonic program — deriving masses from integer/rational lattices in
   the Euclid 7–8 spirit — was run and "closes negatively": "rational lattices are
   dense with near-misses… finding a close rational is numerology"; "no
   Projection-specific mass spectrum has been obtained." The surviving exact
   integer fact is Theorem 12.IX.T1 (C_A/C_F − Ω² = N²(N²−9)/[4(N²−1)], zero for
   integer N ≥ 2 iff N = 3; verifies exactly in SymPy → per task vocabulary
   **CHECKED**), but it is a Lie-algebra Casimir computation, not built on any
   Book 7 proposition.

---

## What the extension does NOT add beyond Euclid (disclosed gaps)

- **No number-theoretic axioms at all.** The extension adds no axiom or definition in
  the domain of Book 7 (positive integers, divisibility, primality). Its new axioms
  are geometric (Axiom Zero, pre-metric import) or methodological (firewall).
- **No re-derivation of any Book 7 result.** None of 7.1–7.39 is re-proved,
  generalized, or cited as a premise anywhere in the series, the Volume I original
  manuscript, or the audit ledgers (verified by full-text search).
- **Domain mismatch, stated plainly:** Euclid's Book 7 defines number as a multitude
  of units (Def 7.2) — it speaks only of positive integers. R Theory's carriers,
  primitives, and operators are real/complex analytic objects; there is no point in
  the theory where an integer-valued Euclid-7 proposition could attach. The claim
  "the theory is built as an extension of Euclid's work" is true of the *geometric*
  books via the Flower-plane synthetic program and the declared Euclidean carriers
  (Books 0–6, especially Book 4 §§4.IV, 4.X), and is **not** true of Book 7's
  arithmetic: that branch of the extension is empty, and this ledger records it as
  INCOMPLETE throughout rather than inventing a lineage.
