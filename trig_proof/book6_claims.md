# Book 6 claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book6_proof.md` (26 numbered claims C1–C26
plus the status/closure row; rewrite page `~/workspace/r-theory-rewrite/book6/index.html`
— *Book 6 — Local Symmetry and Carrier Mathematics*).
**Date:** 2026-09-22 (PDT).
**Highest Principle before this book:** P0 (Kit's double-angle secant-cosecant identity).
**Boundary note:** the book's own proof file declares (Theorem 4.X.P10 boundary) that
no Euclid *Elements* proposition is used deductively anywhere in Book 6; the 13
Euclid ledgers record that Elements 6.1–6.33 (similar figures) is deliberately not
extended. The two trigonometric principles folded in below are proved by modern
analytic means (power-series definitions of sin/cos/exp) — stated explicitly as their
proved-from provenance — because the *Elements* contains no sine, cosine, or circular
measure, and nothing here is forced into a Euclid citation.

## Claim table

| Claim | Restatement | Verdict | Scope | Folded-in? | Notes |
|---|---|---|---|---|---|
| C1 (6.1) | Aut_blk(U,g;E,V) = O(2)×O(3); Lie algebra so(2)⊕so(3), dim 1+3=4 | verified | PROVED | no — block automorphism group; no trig functions, angles, or circular measure | boundary: absence of primitive E↔V maps inherited from M3/M4 seam + Axiom Zero, declared not computed |
| C2 (6.2) | Λ²U = Λ²E ⊕ (E⊗V) ⊕ Λ²V, dims 1+6+3=10; outer sectors reproduce block Lie algebra | verified | PROVED | no — exterior-algebra decomposition | exact bivector→skew-adjoint identification |
| C3 (6.2 ext) | adjoining one nonzero simple cross generator closes brackets to so(5), rank 4→10 | verified | CHECKED | no — extension theorem, no trig content | completed iterated-commutator rank run in verify_book6.py (V-run, NC) |
| C4 (6.3) | I_ι(u,v) = (−ι⁻¹v, ιu), I_ι²=−1; commutes with diagonal lifts; W complex rank 5 | verified | PROVED | no — complex-structure algebra, not a trig identity | exact; conflation with internal M3 operator J explicitly firewalled |
| C5 (6.3A) | J_CHI²=−1; J_CHI conjugate to I_ι via Π (Π itself AX-6.1) | verified | PROVED | no — conjugacy of complex structures, no trig | conjugation map Φ(u,v)=(u,Πι⁻¹v) checked exactly |
| C6 (6.3A) | exp(χJ_CHI) = cosχ·1 + sinχ·J_CHI for J²=−1 | verified | PROVED | **yes — Principle 1** | the operator Euler formula: genuine trig identity; proved by exact even/odd power-series splitting (CHECKED Taylor corroboration noted only) |
| C7 (6.3A) | orbit weights w_U=cos²χ, w_U♯=sin²χ: sum 1, diff cos2χ, 2√(w_Uw_U♯)=\|sin2χ\|; norm preserved | verified | PROVED | **yes — Principle 2** | the double-angle identities; proved from cos²+sin²=1 exactly |
| C8 (6.4) | single real-type M3/SO(3) module: no scalar complex structure in its commutant; multiplicity two minimal | imported | ST | no — representation theory, no trig | standard theorems imported, not re-derived |
| C9 (6.5) | Hermitian transport through ι compatible with I_ι; block maps act unitarily | verified | PROVED | no — metric/Hermitian-form compatibility | canonicality proved conditional on declared ι |
| C10 (6.6) | maximal complex-linear block envelope U(2)×U(3); real form O(2)×O(3) | verified | PROVED | no — unitary automorphism envelope | blocks inequivalent as Hermitian spaces, exact |
| C11 (6.7) | Z(U(2)×U(3)) = U(1)_E × U(1)_V; diagonal vs relative phase | verified | PROVED | no — group-center computation | Schur's lemma used (ST) |
| C12 (6.8) | volume datum ⇒ S(U(2)×U(3)), su(2)⊕su(3)⊕u(1); traceless line 2a+3b=0; normalization (1/2,−1/3) | verified | PROVED | no — Lie-algebra constraint arithmetic | volume form AX-6.2; not permission for physical identification |
| C13 (6.9) | Hodge-return criterion; C(n,4)=n ⟺ n=5 (n≥4); grade pattern 0:1, 2:10, 4:5 | verified | PROVED | no — combinatorics/fingerprint | criterion itself AX-6.3 |
| C14 (6.10) | complexification 2m=10−k; faithful ⟺ k=0; unique faithful equivariant completion ℂ⁵ | verified | PROVED (mod ST) | no — dimension counting | stronger form conditional on AX-6.4 |
| C15 (6.10) | k=4 real-rank-5 embedding into ℂ³ | verified | CHECKED | no — no trig content | completed SVD intersection-rank run (NC); the k=2 ℂ⁴ example is ASSERTED, not recomputed |
| C16 (6.11) | ω\|_U=0 ⟺ IU=U^⊥; graph(A) Lagrangian ⟺ A symmetric; totally real ⟺ I+A² invertible | verified | PROVED | no — symplectic linear algebra | exact ω((x,Ax),(z,Az)) = xᵀ(A−Aᵀ)z |
| C17 (6.11) | nonsymmetric nilpotent witness: totally real, not Lagrangian | verified | PROVED | no — matrix-algebra witness | exact: A²=0, A≠Aᵀ |
| C18 (6.12) | dim_ℂW ≥ 5 with equality at ℂ³_geom⊕ℂ²_orient | verified | PROVED (mod ST) | no — representation-theoretic bound | inside AX-6.4 class only |
| C19 (6.13) | 2n=n(n−1)/2 ⟺ n=5; C(n,r)=2n ⟺ (n,r)=(5,2),(5,3) | verified | PROVED | no — Diophantine/balance equation | exact integer argument; no trig functions |
| C20 (6.13) | exterior dims 1,5,10,10,5,1; even/odd sectors 16 each | verified | PROVED | no — binomial arithmetic | exact |
| C21 (6.14) | Möbius identities; p′du′=pdu, dp′∧du′=dp∧du; reciprocal-coordinate momentum law | verified | PROVED | no — Möbius/calculus, no trig content as proved | u′=(au+b)/(cu+d) with ad−bc=1; exact differentiation, no forced trig reading |
| C22 (6.14) | J_G²=−1 cotangent completion compatible with canonical symplectic form | verified | PROVED | no — symplectic geometry | exact; physical-momentum reading explicitly firewalled |
| C23 (6.15) | simplex: \|v_A\|²=(N−1)/N, dots −1/N, edge²=2 | verified | PROVED | no — Euclidean geometry of the regular simplex | exact algebra; universal in N |
| C24 (6.15) | Gram spectrum {(d+1)/2, ½×(d−1)}, det=(d+1)/2^d | verified | PROVED | no — eigenvalue arithmetic | exact via J_d eigenvalues |
| C25 (6.15) | det(T\|_{V(N−1)}) = sgn(T); odd permutations exchange orientation classes | verified | PROVED | no — permutation determinants | exact |
| C26 (6.0/6.16/closure) | status grammar, terminal firewall, Volume-I inheritance boundary | declared | ASSERTED | no — methodological declarations | A/B/C/D grammar and the no-passage-to-gauge-group firewall are declared boundaries, not theorems |

## Per-book counts

- Evaluated: **27** (C1–C26 + the status/closure row).
- **PROVED: 22** — C1, C2, C4, C5, C6, C7, C9, C10, C11, C12, C13, C14, C16, C17, C18, C19, C20, C21, C22, C23, C24, C25.
- **CHECKED: 2** — C3 (bracket-closure rank run), C15 (k=4 embedding SVD run).
- **ASSERTED: 1** — C26 (status grammar / terminal firewall / closure declarations).
- **INCOMPLETE: 0** — no computation failed or timed out; the boundary items (Elements 6.1–6.33 not extended, χ_CHI dynamics, physical selectors) are INCOMPLETE-as-extension: deliberate, not failed, recorded in the book's §5 boundary ledger.
- **ST (imported standard theorem): 1** — C8 (representation-theoretic commutant fact, not re-derived).
- **Folded into the cumulative proof: 2** — C6 → Principle 1, C7 → Principle 2.
- New axioms/data beyond Euclid + seed + earlier books: AX-6.1 (Π), AX-6.2 (volume form), AX-6.3 (Hodge-return criterion), AX-6.4 (common-complex-carrier premise), AX-6.5 (U♯≅U* duality) — declared mathematical data, never promoted to primitive axioms (Book 6's own Part IV records 0 new primitive axioms).

## Why only C6 and C7 were folded

Book 6 is the first book of the campaign with genuine trigonometric content, and it
comes in exactly two places: the operator Euler formula (C6) and the double-angle
weight identities on the CHI orbit (C7). Everything else is block-group Lie theory,
exterior algebra, Hermitian/symplectic linear algebra, combinatorics, and Euclidean
simplex geometry — established mathematics, but none of it an identity, lemma, or
exact relation about trigonometric functions, angles, or circular measure. Per the
standing rule, none of it was forced in. The folded principles are proved analytically
(power-series definitions of sin/cos/exp), not from Elements propositions: the
*Elements* contains no sine, cosine, or circular measure, and the book's own proof
file declares no Elements proposition is used deductively in Book 6 (Theorem 4.X.P10
no-Euclid-wholesale boundary). Their proved-from is stated as modern analytic
definitions rather than an invented Euclid citation.

status: complete
