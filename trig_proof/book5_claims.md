# Book 5 claim-by-claim evaluation — Euclid trig-cumulative campaign

**Book:** 5 — Axiom Zero and the Decadic Carrier.
**Sources:** `~/workspace/euclid_work/books/book5_proof.md` (claim inventory
C1–C11 with proofs in dependency order);
`~/workspace/r-theory-rewrite/book5/index.html` (principal theorems).
**Date:** 2026-09-22.
**Trig criterion:** a claim is folded into the cumulative trigonometric proof
only if it yields a genuine trigonometric principle — an identity, lemma, or
exact relation about trigonometric functions, angles, or circular measure.

## Claim table

| Claim | Restatement | Verdict | Scope | Folded-in? | Notes |
|---|---|---|---|---|---|
| C1 | U = E ⊕ V is a real rank-5 carrier (2 + 3 = 5) | correct | PROVED | no — dimension arithmetic | Basis-concatenation argument verified; nothing trigonometric |
| C2 | Axiom Zero A0.1: independent isomorphic partner U^♯ with declared block-compatible pairing ι: U → U^♯; W := U ⊕ U^♯ | granted as axiom | ASSERTED | no — a new axiom, not mathematics | The theory's first R-specific axiom; book is explicit it is assumed |
| C3 | Axiom Zero A0.2: primitive diagonal noncoupling (primitive operators preserve the summands; off-diagonal Hom(U,U^♯) maps not active primitive couplings) | granted as axiom | ASSERTED | no — a new axiom, not mathematics | Second clause of Axiom Zero; assumed |
| C4 | dim_ℝ W = 5 + 5 = 10 (conditional on C2) | correct | PROVED | no — dimension arithmetic | Follows by basis concatenation given the axiom |
| C5 | I_ι(u,v) := (−ι^{−1}v, ιu) satisfies I_ι² = −id; W has complex rank 5; I_ι depends on the declared pairing ι (conditional on C2) | correct | PROVED | no — complex structure on a real space, not a trig relation | Direct block computation verified; dependence-on-pairing datum checked (ι' = ι∘A changes I_ι) |
| C6 | Corollary 5.3.1: W_ext = W ⊕ Z has dim_ℝ = 10 + dim Z ≥ 10, equality iff Z = {0}; I-invariant Z forces dim_ℝ W_ext = 10 + 2m (conditional on C2) | correct | PROVED | no — rank bound, not a trig relation | Even-dimension argument for I-invariant subspaces verified (x² + 1 irreducible over ℝ) |
| C7 | Theorem 5.4.1: for k := dim_ℝ(U ∩ IU), k ∈ {0, 2, 4} and dim_ℝ(U + IU) = 10 − k ∈ {10, 8, 6}, complex ranks 5, 4, 3; k = 0 is the axiom, k = 2, 4 lawful counterfactuals | correct as enumeration | PROVED (enumeration; the *selection* of k = 0 is the axiom, ASSERTED) | no — invariant-subspace dimension theory | I-invariance of U ∩ IU and k-even steps verified; nothing trigonometric |
| C8 | 2n = n(n−1)/2 has the unique positive-integer solution n = 5, value 10 | correct | PROVED (+ CHECKED corroboration V9 — the exact proof needs nothing more) | no — a Diophantine equation in n, no trig functions involved | Exact algebra n(n−1)/2 = 2n ⟺ n = 5; proof-over-sampling respected |
| C9 | (dim Λ^0U,…,dim Λ^5U) = (1, 5, 10, 10, 5, 1) | correct | PROVED (+ CHECKED corroboration V10) | no — binomial coefficients | dim Λ^k = C(n,k) verified; proof-over-sampling respected |
| C10 | The Hodge one-step condition ⋆(Λ²U ∧ Λ²U) ⊂ Λ^1U demands n − 4 = 1, i.e. n = 5 | correct | PROVED (+ CHECKED corroboration V11) | no — exterior-degree index arithmetic | Wedge degrees add; ⋆: Λ^4 → Λ^{n−4} verified; proof-over-sampling respected |
| C11 | Status/exclusions (5.5) and the anti-circularity firewall (5.6): no physical dimensionality, no dynamics, no SM content; downstream physics may test but never justify Axiom Zero | recorded | ASSERTED | no — methodological declarations, not mathematical theorems | Rules about how the argument may be read; constrain reading, are not proved |

## Per-book counts

- Claims evaluated: **11**
- PROVED: **8** (C1, C4, C5, C6, C7, C8, C9, C10)
- CHECKED (as verdict): **0** (numeric checks V4, V8, V9, V10, V11, V12 exist
  as corroboration only; all carry complete analytic proofs, so none is
  CHECKED-status per the proof-over-sampling rule)
- ASSERTED: **3** (C2, C3, C11)
- INCOMPLETE: **0**
- Folded into the cumulative trigonometric proof as new Principles: **0**

## Why nothing was folded in

Book 5's proved content is finite-dimensional real linear algebra
(carrier ranks, the declared-pairing complex structure, invariant-subspace
dimensions, exterior-algebra dimension identities). None of it is an
identity, lemma, or exact relation about trigonometric functions, angles,
or circular measure — the campaign's stated trig criterion. The book's own
proof file states this plainly: "Book 5 contains no trigonometric claims."
No Euclid proposition is used deductively in the book's proofs (the file
records the No-Euclid-wholesale boundary), so no Euclid citations were
needed for this evaluation either. Forcing any claim in would
misrepresent the book and weaken the cumulative proof's dependency
discipline. The three asserted items (Axiom Zero A0.1/A0.2, the
methodological firewall) cannot found trigonometric principles.

## Principles register impact

None. Highest Principle number remains **P0** (Kit's double-angle
secant-cosecant identity, PROVED). The `## Book 5` chapter in
`cumulative_trig_proof.md` records "none added" with this reason.

status: complete
