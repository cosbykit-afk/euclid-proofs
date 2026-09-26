# Book 5 Extension Proofs — Axiom Zero and the Decadic Carrier

**Rewrite book:** `r-theory-rewrite/book5/index.html` — *Book 5 — Axiom Zero and the Decadic Carrier*.
**Campaign:** Euclid book-proofs (R Theory as an extension of Euclid's work).
**Date:** 2026-09-22.
**Seed available:** `../books/seed_double_angle.md` (Kit's double-angle secant/cosecant identity, PROVED).
No claim in this book needs it; it is recorded as available, not invoked.

## Scope discipline

- **PROVED** = exact deductive mathematics shown below (definitions first, dependency order).
- **CHECKED** = a completed computation that corroborates (does not establish) an analytic proof.
- **ASSERTED** = assumption, axiom, or methodological declaration — granted, not proved.
- **INCOMPLETE** = failed, timed out, or unfinished. None below.

## On Euclid citations and the No-Euclid-wholesale boundary

No proposition of Euclid's *Elements* is used deductively in these proofs.
The mathematics below is finite-dimensional real linear algebra and elementary
arithmetic. It rests on the **stipulated standard import** (the complete ordered
field ℝ and ordinary linear algebra: direct sums, dimension additivity,
exterior algebra, the Hodge dual on finite-dimensional inner-product spaces) —
exactly the import discipline the Euclid Book 5 ledger records ("No-Euclid-wholesale
theorem (4.X.H)": only declared premises plus standard mathematics declared at
point of use). The "Euclid-style" content of this file is the *method* —
definitions first, dependency order, nothing used before it is established —
not a derivation from Euclid's postulates. The campaign seed (double-angle
identity) is not invoked: Book 5 contains no trigonometric claims.

## Book-local premises (ASSERTED datum, not proved in this batch)

The task's batch-independence rule means Books 1–4 of the rewrite are not
available as established results. Book 5 therefore takes as *granted premises*:

- **P-inherit:** real vector spaces E (rank 2) and V (rank 3), inherited from
  the frozen M0–M4 spine, with **no** preferred identification E→V or V→E.
  (Scope: ASSERTED book-local datum; the book itself tags this `M`.)
- **P-import:** the standard-import stipulation above (ℝ, finite-dimensional
  real linear algebra, exterior algebra, Hodge duality on inner-product spaces).
- **P-method:** the anti-circularity firewall (5.6): downstream physics may test
  or contextualize the carrier but never justify Axiom Zero. (Scope: ASSERTED
  methodological rule, not a mathematical theorem.)

---

# Part I — Definitions (in dependency order)

- **D1.** A *real carrier* is a finite-dimensional real vector space; its
  *real rank* is its dimension.
- **D2.** The *direct sum* of real spaces X, Y is X ⊕ Y with dim(X ⊕ Y) =
  dim X + dim Y (basis concatenation). A decomposition is *block-compatible*
  for E ⊕ V when maps send E to the E-block and V to the V-block.
- **D3.** U := E ⊕ V, with E, V as in P-inherit. (Definition; dim computed in C1.)
- **D4.** A *complex structure* on a real space W is a real-linear I: W → W
  with I² = −id. Then tr(I) = 0 and W has complex rank (dim_ℝ W)/2.
- **D5.** Λ^k U is the k-th exterior power; ⋆ is the Hodge dual on a
  finite-dimensional inner-product space, ⋆: Λ^j → Λ^{n−j}.

---

# Part II — Claim inventory (scope-labeled)

| # | Claim | Scope |
|---|---|---|
| C1 | U = E ⊕ V is a real rank-5 carrier (2 + 3 = 5) | PROVED |
| C2 | Axiom Zero A0.1: independent isomorphic partner U^♯ with declared block-compatible pairing ι: U → U^♯; W := U ⊕ U^♯ | ASSERTED (new axiom) |
| C3 | Axiom Zero A0.2: primitive diagonal noncoupling (primitive operators preserve the summands; off-diagonal maps in Hom(U,U^♯) not active primitive couplings) | ASSERTED (new axiom) |
| C4 | dim_ℝ W = 5 + 5 = 10 | PROVED (conditional on C2) |
| C5 | I_ι(u,v) := (−ι^{−1}v, ιu) satisfies I_ι² = −id; W has complex rank 5; I_ι depends on the declared pairing ι, not merely on U^♯ ≅ U | PROVED (conditional on C2) |
| C6 | Corollary 5.3.1: W_ext = W ⊕ Z has dim_ℝ = 10 + dim Z ≥ 10, equality iff Z = {0}; if Z is an I-invariant summand, dim_ℝ W_ext = 10 + 2m, m = 0,1,2,… | PROVED (conditional on C2) |
| C7 | Theorem 5.4.1: for k := dim_ℝ(U ∩ IU), k ∈ {0,2,4} and dim_ℝ(U + IU) = 10 − k ∈ {10,8,6} with complex ranks 5,4,3; k = 0 is exactly Axiom Zero, k = 2,4 lawful counterfactuals excluded only by the axiom | PROVED (conditional on C2 for the I = I_ι reading) |
| C8 | 2n = n(n−1)/2 has the unique positive-integer solution n = 5, value 10 | PROVED (+ CHECKED corroboration) |
| C9 | (dim Λ^0U,…,dim Λ^5U) = (1,5,10,10,5,1) | PROVED (+ CHECKED corroboration) |
| C10 | The Hodge one-step condition ⋆(Λ²U ∧ Λ²U) ⊂ Λ^1U demands n − 4 = 1, i.e. n = 5 | PROVED (+ CHECKED corroboration) |
| C11 | Status/exclusions (5.5) and the anti-circularity firewall (5.6): no physical dimensionality, no dynamics, no SM content; k = 2,4 lawful mathematics excluded from M5 by the adopted independence | ASSERTED (methodological declarations) |

---

# Part III — Proofs in dependency order

## Proof of C1. dim_ℝ(E ⊕ V) = 2 + 3 = 5

Let {e1, e2} be a basis of E and {v1, v2, v3} a basis of V (P-import).
The five vectors (e1,0), (e2,0), (0,v1), (0,v2), (0,v3) are linearly independent
in E ⊕ V and span it: any (x,y) = Σ a_i e_i + Σ b_j v_j by the basis property
of each summand. Hence they form a basis and dim_ℝ U = 5. ∎ (Scope: PROVED.)

## C2, C3 — recorded, not proved

Axiom Zero (A0.1, A0.2) is the book's declared starting point. The book is
explicit that nothing in it proves the axiom; it is *granted*. ∎
(Scope: ASSERTED — the theory's new axiom. The book's honesty tagline is
preserved: "If you do not grant Axiom Zero, you do not get ten.")

## Proof of C4. dim_ℝ W = 10

Given C2, W = U ⊕ U^♯ with U^♯ ≅ U via ι, so dim U^♯ = dim U = 5.
By basis concatenation (same argument as C1), dim_ℝ W = 5 + 5 = 10. ∎
(Scope: PROVED, conditional on Axiom Zero.)

## Proof of C5. The declared-pairing complex structure

Define I_ι: U ⊕ U^♯ → U ⊕ U^♯ by I_ι(u,v) = (−ι^{−1}v, ιu), where
ι^{−1}: U^♯ → U is the inverse of the declared isomorphism (D2, C2).
Then

I_ι²(u,v) = I_ι(−ι^{−1}v, ιu)
          = (−ι^{−1}(ιu), ι(−ι^{−1}v))
          = (−u, −v) = −(u,v),

so I_ι² = −id: I_ι is a complex structure (D4). In block form relative to
U ⊕ U^♯, I_ι = [[0, −ι^{−1}],[ι, 0]], whence tr(I_ι) = 0; the ±i eigenspaces
over ℂ have equal complex dimension, so dim_ℂ W = (dim_ℝ W)/2 = 10/2 = 5. ∎

*Dependence on the pairing datum.* If ι' = ι ∘ A for A ∈ GL(U), A ≠ ±id, then
I_{ι'} ≠ I_ι in general (e.g. A = 2·id gives I_{ι'}(u,v) = (−(1/2)ι^{−1}v, 2ιu));
the complex structure is determined by the *chosen pairing*, not by the bare
existence statement U^♯ ≅ U. ∎ (Scope: PROVED, conditional on Axiom Zero.)

## Proof of C6. Minimality corollary

Let W_ext = W ⊕ Z with Z an independent real sector. By basis concatenation,
dim_ℝ W_ext = dim_ℝ W + dim_ℝ Z = 10 + dim Z ≥ 10, with equality iff
dim Z = 0 iff Z = {0}. If the complex structure must extend to Z — i.e. Z is
an I-invariant summand — then Z, being a nonzero I-invariant real subspace,
has even real dimension (the minimal polynomial of I is x² + 1, irreducible
over ℝ, so every nonzero invariant subspace has dimension a multiple of 2;
P-import). Hence dim Z = 2m and dim_ℝ W_ext = 10 + 2m, m = 0,1,2,…. ∎
(Scope: PROVED, conditional on Axiom Zero. Ten is the smallest *forced* rank,
not a proof that every future realization has exactly ten real dimensions —
the book's Corollary 5.3.1 bound is preserved.)

## Proof of C7. Even-overlap enumeration

Fix I = I_ι (C5). IU = I(U) is a real subspace of W with dim IU = dim U = 5
(I is injective). Let k = dim_ℝ(U ∩ IU).

*Step 1.* U ∩ IU is I-invariant: if x ∈ U ∩ IU, write x = Iy, y ∈ U;
Ix = I²y = −y ∈ U, and Ix = I(x) ∈ I(U) = IU since x ∈ U. So Ix ∈ U ∩ IU.

*Step 2.* k is even: a nonzero I-invariant real subspace has even real
dimension (minimal polynomial x² + 1, as in C6). So k ∈ {0, 2, 4} given
k ≤ dim U = 5 (k = 5 is odd, and U itself cannot be I-invariant since
dim_ℝ U = 5 is odd).

*Step 3.* dim_ℝ(U + IU) = dim U + dim IU − k = 5 + 5 − k = 10 − k ∈ {10, 8, 6}.
U + IU is I-invariant (I(U) = IU, I(IU) = I²U = U ⊂ U + IU), hence of even
real dimension, with complex rank (10 − k)/2 ∈ {5, 4, 3}.

*k = 0 is exactly Axiom Zero* (the direct-independence condition C2); k = 2, 4
are lawful mathematical completions, excluded from M5 only by the adopted
axiom, not by contradiction. ∎ (Scope: PROVED as an enumeration of lawful
completions; the *selection* of k = 0 is the axiom, ASSERTED.)

## Proof of C8. 2n = n(n−1)/2 ⟺ n = 5 (n positive integer)

For n ≠ 0: n(n−1)/2 = 2n ⟺ n − 1 = 4 ⟺ n = 5. The positive-integer solution
is unique, and 2·5 = 5·4/2 = 10. ∎ (Scope: PROVED; corroborated by
validation run V9.)

## Proof of C9. Exterior-algebra dimensions of a five-space

For an n-space with basis {b1,…,bn}, the wedge products
b_{i1} ∧ ⋯ ∧ b_{ik} (i1 < ⋯ < ik) form a basis of Λ^k, so
dim Λ^k = C(n,k). For n = 5: C(5,k) for k = 0,…,5 is (1,5,10,10,5,1). ∎
(Scope: PROVED; corroborated by validation run V10.)

## Proof of C10. Hodge one-step condition

Λ²U ∧ Λ²U ⊂ Λ^4U (wedge degrees add). ⋆: Λ^4 → Λ^{n−4} (D5).
Asking the image to lie in the vector degree Λ^1 in one step requires
n − 4 = 1, i.e. n = 5. ∎ (Scope: PROVED; corroborated by validation run V11.)

## C11 — recorded, not proved

The status/exclusion declarations (5.5: no physical spacetime dimensionality,
no dynamics, no quantum probability, no Standard Model content; no 10→11
construction as a theorem) and the anti-circularity firewall (5.6) are
methodological rules of the manuscript, not mathematical theorems. ∎
(Scope: ASSERTED declarations. They constrain how the argument may be read;
they are not proved here.)

## Computational corroboration cited

`~/workspace/r-theory-rewrite/validation/book5/verify_book5.py`, re-run
2026-09-22 in this campaign: exit 0, all 15 checks pass, no timeouts —
11 checked proofs of exact integer/block-algebra identities (V1–V3, V5–V7,
V9–V11) and 4 completed numerical checks: V4 (I_ι² = −I over 50 random
orthogonal pairings, max_err 3.9e-16), V8 (J-invariant subspaces even-dimensional
on 20 random instances, residual ≤1.2e-15), V12 (dim(U+IU) = 10−k on 20 random
instances, max_err 0.0). Worst-case floating-point error 1.2e-15. Per the
proof-over-sampling rule these runs corroborate the analytic proofs above;
they do not establish anything the proofs don't. `test_embeds.py` covers
Desmos caption consistency only, not cited for mathematics.

---

# Part IV — New axioms/assumptions beyond Euclid + seed

1. **Axiom Zero A0.1** (the theory's new axiom): an independent isomorphic
   partner carrier U^♯ exists together with a declared block-compatible linear
   isomorphism ι: U → U^♯ (ι(E) = E^♯, ι(V) = V^♯); W := U ⊕ U^♯. Granted, not
   proved. Everything in C4–C7 is conditional on it.
2. **Axiom Zero A0.2** (same axiom, second clause): primitive admissible
   operators preserve the two summands separately (lifting as A ⊕ ιAι^{−1});
   mathematical off-diagonal maps in Hom(U,U^♯), Hom(U^♯,U) may exist but are
   not active primitive couplings; any later U↔U^♯ coupling is additional
   structure.
3. **Book-local inheritance datum** (assumed premise, not a theory axiom):
   E real rank 2, V real rank 3, no inherited E↔V identification (P-inherit);
   the standard ℝ/linear-algebra import (P-import); the anti-circularity
   firewall as a methodological rule (P-method).

**Honest bottom line.** This book's mathematics is short and entirely
conditional: *if* Axiom Zero is granted, *then* the decadic carrier W (real
rank 10, complex rank 5, canonical relative to the declared pairing), the
10 + 2m minimality ladder, and the {10, 8, 6} overlap enumeration all follow
by exact linear algebra. The axiom itself is assumed, the pairing datum is
part of the assumption, and nothing here is physical spacetime dimensionality.
