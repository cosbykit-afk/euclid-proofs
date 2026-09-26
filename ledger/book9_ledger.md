# Book 9 Ledger — Euclid Extension Proof Campaign

**Source:** `/home/hatch/workspace/euclid_work/text/book9.txt`
(Fitzpatrick/Heiberg English translation with Greek alongside, 1351 lines)
**Compiled:** 2026-09-21 by Book-9 campaign worker
**Rule of evidence:** Kit's standing standard — only what the math has proven,
or what a completed computation measured, counts; everything else is labeled
as it is. No status rounding, up or down.

---

## 1. Book summary

Elements Book 9 is the third and last of the arithmetic books (Books 7–9).
Fitzpatrick's running title is **"Applications of Number Theory"** (Book 7 is
titled "Elementary Number Theory"); the editorial footnote (†, line 8 of
`book9.txt`) states that the propositions of Books 7–9 are generally
attributed to the school of Pythagoras. The Encyclopedia.com biography
context confirms the standard reading: Book 9 is a "miscellany" containing
Euclid's proof of the infinitude of primes (9.20) and the perfect-number
theorem (9.36), with 9.14 being the fundamental theorem in the theory of
numbers — unique prime factorization in Euclid's formulation ("If a number be
the least that is measured by prime numbers, it will not be measured by any
other prime number except those originally measuring it").

**Definitions / postulates / common notions stated in Book 9: none.**
A full-text grep found no "Definition", "Postulate", or "Common notion" in
Book 9, and no `[CN n]` citations inside any of its proofs. All of Book 9's
logical ground is inherited from **Book 7's 22 definitions** (Defs 7.1–7.22:
unit, number, part/parts, multiple, even, odd, even-times-even,
even-times-odd, odd-times-odd, prime, numbers prime to one another, composite,
multiply, plane number, solid number, square, cube, proportion, similar plane
and solid numbers, perfect number), plus propositions proved earlier in Books
2, 7, 8 and earlier propositions within Book 9 itself. Book 7's Def 7.22
("A perfect number is that which is equal to its own parts") is the definition
9.36 rests on.

**Internal structure of the 36 propositions (9.1–9.36):**
- **9.1–9.7** — Closure laws for square and cube products (product of similar
  plane numbers is square; products of cubes are cubes; composite × number is
  solid).
- **9.8–9.11** — Anatomy of a continued proportion (geometric progression)
  starting from a unit: which terms are squares, cubes, or both (9.8);
  propagation of square-ness/cube-ness (9.9); exclusion of squares/cubes
  elsewhere (9.10); measurability of a greater term by a lesser "according to"
  some term among them (9.11, with a **porism/corollary** — the only corollary
  in Book 9, stating that the measuring number's place from the unit matches
  the quotient's place from the measured number).
- **9.12–9.14** — Prime-divisor structure of geometric progressions; **9.14
  is Euclid's unique-prime-factorization theorem** (proved from 7.30 alone).
- **9.15–9.19** — Coprimality in continued proportions; constructibility of a
  third (9.18) and fourth (9.19) proportional to given numbers.
- **9.20** — The infinitude of primes: primes are more numerous than any
  assigned multitude (proved by 7.28, 7.31, 7.36).
- **9.21–9.34** — Complete parity arithmetic: sums and differences of
  even/odd numbers (9.21–9.27), products odd×even / odd×odd (9.28–9.29),
  odd divisors of even numbers and their halves (9.30), coprimality with
  doubles (9.31), and the classification of even numbers into
  even-times-even-only (9.32), even-times-odd-only (9.33), and both (9.34).
- **9.35–9.36** — The geometric-series excess identity (9.35) feeding the
  **perfect-number theorem 9.36**: if powers of 2 summed from a unit yield a
  prime, that sum times the last term is perfect.

**Editorial marks:** Propositions 9.19, 9.35, and 9.36 carry a dagger (†) in
the Fitzpatrick edition. The same mark appears on propositions in Books
1, 2, 5, 6, 7, 10, and 11, so it is an edition-level editorial flag, not
Book-9-specific. Its meaning cannot be decoded from the text alone and is
recorded here without interpretation.

**Proof-dependency extraction method:** every explicit `[Prop. n.m]`,
`[Def. n.m]`, and `[CN n]` bracket cited in each proposition's proof text was
collected mechanically and spot-verified by reading the proof passages
(notably 9.4 and 9.5, which genuinely cite 9.3 of the same book, and 9.7,
whose proof cites only Def. 7.15).

---

## 2. Proposition inventory

Scope labels (Kit's four-way discipline):
- **PROVED** — deductive proof from Euclid's definitions/postulates/
  propositions, shown.
- **CHECKED** — verified by a completed computation (computation described).
- **ASSERTED** — manuscript stipulation or new axiom.
- **INCOMPLETE** — not established.

**Convention for this ledger:** the "R Theory extension" column records any
claim in the R Theory rewrite series or its audit records that builds on or
generalizes the Euclid proposition. Where the search (below) found **no such
claim**, the extension entry is "None identified" and the scope label is
**N/A — no extension claim** (the four labels apply to extension *claims*;
applying one of them to a non-existent claim would itself be a status
invention).

**Search method (all files read, nothing assumed):** the full text of all 23
rewrite-series book index pages (`r-theory-rewrite/book0/`–`book22/`,
including vol0), the vol0 sub-pages, and the manuscript text files
(`r-theory-rewrite/manuscript/R-Theory-Volume-{I,II,III}-original.txt`) were
searched for: `prime`, `perfect number`, `Mersenne`, `infinitude of prime`,
`number theory`, `Elements Book 9`, `Book IX`, `continued proportion`,
`mean proportion`. **Zero hits** — no book page contains any of these terms.
Every `euclid`/`Euclid` mention in the rewrite series (book0, book4, book6,
book8, book21) is geometric: Book 4's Flower-plane re-certification of
Elements Books I–II (§4.IV, "Historical Flower Plane Books I–II proofs
re-presented and re-certified"), the Euclidean postulate audit (§4.X),
Euclidean carriers/metrics, and the A₂ hexagon geometry in book21. Every
`odd`/`even`/`square`/`cube` mention in the rewrite series is analytic or
geometric (chart quadrants, RPⁿ orientability parity `n ≡ 3 (mod 4)` in Book 3
— re-verified by exact integer arithmetic as a *computation*, not a citation
of 9.21–9.29 — dimension parity in Book 5). The audit records
(`vol4/NOTATION_LEDGER.md`, `vol4/DEPENDENCY_CHAIN.md`) contain no
number-theoretic entries.

**Verdict on the mapping:** R Theory, as documented in the rewrite series,
manuscript, and audit records, contains **no extension, generalization, or
application of any of the 36 propositions of Elements Book 9**. The theory's
"extension of Euclid" claim, as actually embodied in the pages, is carried by
the *geometric* books (I–II via the Flower plane, V–VI via proportion theory
in carriers) — the arithmetic program of Books 7–9 is untouched by it.

| # | Statement (one line) | Euclid proof dependencies | R Theory extension | Scope |
|---|---|---|---|---|
| 9.1 | Product of two similar plane numbers is square. | 7.17, 8.18, 8.8, 8.22 | None identified | N/A — no extension claim |
| 9.2 | Two numbers whose product is a square are similar plane numbers. | 7.17, 8.18, 8.20, 8.8 | None identified | N/A — no extension claim |
| 9.3 | A cube number multiplied by itself is a cube. | Def 7.15, Def 7.20, 8.8, 8.23 | None identified | N/A — no extension claim |
| 9.4 | The product of two cube numbers is a cube. | 7.17, 9.3, 8.19, 8.8, 8.23 | None identified | N/A — no extension claim |
| 9.5 | If a cube number times some number makes a cube, that number is a cube. | 7.17, 9.3, 8.19, 8.8, 8.23 | None identified | N/A — no extension claim |
| 9.6 | If a number times itself makes a cube, the number itself is a cube. | 8.19, 8.8, 8.23 | None identified | N/A — no extension claim |
| 9.7 | A composite number times some number makes a solid number. | Def 7.15 (via Defs 7.13, 7.17) | None identified | N/A — no extension claim |
| 9.8 | In a continued proportion from a unit: the 3rd from the unit is square (and every alternate term after), the 4th is cube (and every 3rd after), the 7th is both square and cube (and every 6th after). | Def 7.15, Def 7.20, 8.22, 8.23 | None identified | N/A — no extension claim |
| 9.9 | Continued proportion from a unit: if the 2nd term is square, all remaining terms are square; if cube, all are cube. | 9.3, 9.8, 8.22, 8.23 | None identified | N/A — no extension claim |
| 9.10 | If the 2nd from the unit is not square, no term is square except the 3rd and every alternate term after; if not cube, no term is cube except the 4th and every 3rd term after. | 9.6, 9.8, 8.26 | None identified | N/A — no extension claim |
| 9.11 | In a continued proportion from a unit, a lesser term measures a greater according to some term among the proportional numbers. (Plus porism: the measuring number's place from the unit matches the quotient's place from the measured number.) | 7.15 | None identified | N/A — no extension claim |
| 9.12 | If the last of a continued proportion from a unit is measured by primes, the number next to the unit is measured by the same primes. | Def 7.11, Def 7.14; 7.19, 7.20, 7.21, 7.29, 9.8 | None identified | N/A — no extension claim |
| 9.13 | If the number after the unit is prime, the greatest term is measured by no numbers except those among the proportional numbers. | 7.19, 7.31, 9.8, 9.11, 9.12 | None identified | N/A — no extension claim |
| 9.14 | The least number measured by given primes is measured by no other prime (Euclid's unique-prime-factorization theorem). | 7.30 | None identified | N/A — no extension claim |
| 9.15 | If three continuously proportional numbers are least in their ratio, any two added together are prime to the third. | 2.3, 2.4, 7.22, 7.24, 7.25, 7.28, 8.2 | None identified | N/A — no extension claim |
| 9.16 | If two numbers are prime to one another, then as the first is to the second, the second is not to any other number (in that ratio). | 7.20, 7.21 | None identified | N/A — no extension claim |
| 9.17 | In a continued proportion whose extremes are prime to one another, as the first is to the second, so the last is to no other number. | Def 7.20, 7.13, 7.20, 7.21 | None identified | N/A — no extension claim |
| 9.18 | For two given numbers, determine whether a third proportional to them can be found. | 7.19, 9.16 | None identified | N/A — no extension claim |
| 9.19† | For three given numbers, determine when a fourth proportional to them can be found. | 7.14, 7.19, 7.20, 7.21, 9.17 | None identified | N/A — no extension claim |
| 9.20 | Primes are more numerous than any assigned multitude (infinitude of primes). | 7.28, 7.31, 7.36 | None identified | N/A — no extension claim |
| 9.21 | The sum of any multitude of even numbers is even. | Def 7.6 | None identified | N/A — no extension claim |
| 9.22 | The sum of an even multitude of odd numbers is even. | Def 7.7, 9.21 | None identified | N/A — no extension claim |
| 9.23 | The sum of an odd multitude of odd numbers is odd. | Def 7.7, 9.21, 9.22 | None identified | N/A — no extension claim |
| 9.24 | Even minus even is even. | Def 7.6 | None identified | N/A — no extension claim |
| 9.25 | Even minus odd is odd. | Def 7.7, 9.24 | None identified | N/A — no extension claim |
| 9.26 | Odd minus odd is even. | Def 7.7, 9.24 | None identified | N/A — no extension claim |
| 9.27 | Odd minus even is odd. | Def 7.7, 9.24 | None identified | N/A — no extension claim |
| 9.28 | Odd times even is even. | Def 7.15, 9.21 | None identified | N/A — no extension claim |
| 9.29 | Odd times odd is odd. | Def 7.15, 9.23 | None identified | N/A — no extension claim |
| 9.30 | An odd number measuring an even number also measures half of it. | 9.23 | None identified | N/A — no extension claim |
| 9.31 | An odd number prime to a number is also prime to its double. | 9.30 | None identified | N/A — no extension claim |
| 9.32 | Each number continually doubled from a dyad is even-times-even only. | Def 7.8, 9.13 | None identified | N/A — no extension claim |
| 9.33 | A number with an odd half is even-times-odd only. | Def 7.8, Def 7.9 | None identified | N/A — no extension claim |
| 9.34 | A number neither doubled from a dyad nor having an odd half is both even-times-even and even-times-odd. | Def 7.8, Def 7.9 | None identified | N/A — no extension claim |
| 9.35† | In a continued proportion, subtracting first-term-sized pieces from the second and last terms: as the excess of the second is to the first, so the excess of the last is to the sum of all terms before it. | 7.12, 7.13 | None identified | N/A — no extension claim |
| 9.36† | If powers of 2 set out continuously from a unit sum to a prime, then that sum multiplied into the last term is a perfect number (Euclid's perfect-number theorem). | Def 7.20, Def 7.22; 7.14, 7.19, 7.20, 7.21, 7.29, 9.13, 9.35 | None identified | N/A — no extension claim |

---

## 3. New axioms / definitions introduced by the extension beyond Euclid

**For the subject matter of Book 9 (number theory: squares, cubes, continued
proportions, primes, parity, perfect numbers): none.**

The R Theory rewrite series introduces no new axiom or definition that
extends, generalizes, or re-grounds any Book 9 proposition, because — per the
inventory above — it makes no claims in this territory at all. There is no
R Theory prime-number theory, no perfect-number theory, no parity arithmetic
beyond ordinary integer arithmetic used as a computational tool (e.g. Book 3's
exact integer check of `orientability ⟺ (n+1) even` for n = 1…7, and exact
integer-arithmetic matrix identities in Books 5/16). Using elementary
arithmetic in a computation is not an extension of Euclid's theorems and is
not recorded as one.

**For clarity (not as Book 9 extensions):** R Theory does introduce new
axioms elsewhere — e.g. **Axiom Zero** (rewrite Book 5, the primitive
U↔U♯ non-mixing pairing ι: U → U♯) — but these attach to the geometric
carrier program (Books 0–8's Euclidean/Clifford/spinor machinery), not to
Elements Book 9. The "extension of Euclid" actually documented in the series
runs through the *geometric* books: Book 4 re-presents and re-certifies the
Flower-plane proofs of Elements Books I–II and audits the Euclidean
postulates, and Book 8 rebuilds exterior calculus/Hodge duality on the
Euclidean carrier. No load-bearing assumption connects any R Theory axiom to
any Book 9 proposition.

**TESS-India framing note:** the TESS-India "Developing creative thinking in
mathematics: trigonometry" unit (shape/space linked with ratio, deduction,
and proof) was read as assigned. It is a pedagogy document about trigonometric
teaching, not number theory; since no extension of Book 9 was found to exist,
there was no constructive step where its creative-deductive framing was
needed. It is recorded as read, not used.

---

## 4. Honest limitations of this ledger

1. **Mapping search boundary:** the "None identified" verdict rests on
   text search of the 23 rewrite-series book index pages, the vol0 sub-pages,
   the three original manuscript text files, and the vol4 notation ledger /
   dependency chain. If a Book-9 extension exists in a document not searched
   (e.g. an unindexed working note), it is not captured here. Nothing in the
   searched corpus suggests such a document exists.
2. **Dependency lists** are the translator's explicit bracket citations in
   the Fitzpatrick proof texts, mechanically extracted and spot-verified —
   not an independent logical re-derivation of each proposition's minimal
   dependency set.
3. **Dagger (†) marks** on 9.19, 9.35, 9.36 are recorded as found in the
   edition; their editorial meaning was not decoded from the source text.
4. **Book 9 itself is not a rewrite target:** the null mapping is a finding
   about R Theory's scope, not a criticism of Euclid. Euclid's proofs stand
   on their own deductive footing from Book 7's definitions; the extension
   simply has not engaged them.
