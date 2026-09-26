# Book 18 extension proofs — R Theory, "The Contraction Module"

**Source:** `~/workspace/r-theory-rewrite/book18/index.html` (Volume IV, Book 18 rewrite;
restructured audit; every theorem/import/contract/status label below comes from the
manuscript page, no mathematics added — except §3.14–3.16, which record
post-page campaign results that supersede two of the page's v1 admissions, flagged
as such).
**Method:** definitions first, dependency order, nothing used before it is proved.
Scope labels: PROVED / CHECKED / ASSERTED / INCOMPLETE (see standing rules).
**Generated:** 2026-09-22, by workflow agent `euclid-book-proofs` (book-18).
**Verification run:** `~/workspace/r-theory-rewrite/validation/book18/verify_book18.py`
re-run by this worker 2026-09-22 — exit 0, all 42 checks passed (41 CP, 1 NC),
no timeouts. Log: `/tmp/b18_verify.log`.

## 0. Citation availability and Euclid contact (disclosed limitations)

- The campaign seed (`seed_double_angle.md`) was read. **It is not used** by any
  proof below: no Book 18 claim rests on the double-angle identity, so it is
  cited nowhere and nothing is silently invoked through it.
- `book0_proof.md` .. `book13_proof.md`: only book1/5/10/12/14 exist on disk at
  write time; Book 18's proofs depend on none of them (its load-bearing content
  is integer/rational arithmetic, one completed numerical bound, standard
  representation-theory imports, and audit-verified manuscript readings).
- Euclid's *Elements* is cited from the inventoried
  `~/workspace/euclid_work/ledger/book1_ledger.md` .. `book13_ledger.md`. The
  integer arithmetic in §3 rests on the **common notions** (CN 1–3) and on
  multiplication as Def VII.15 / commutativity 7.16, used in the using
  direction only. **No proposition of the Elements is extended by any R Theory
  claim here** — consistent with the ledger mappings, which record no R Theory
  extension for the cited items.
- **No-Euclid-wholesale boundary (honored):** R Theory extends a
  synthetic-constructive stratum on its declared substrate; wholesale
  inheritance of the Elements is not claimed. Only the items named above enter.

## 1. Definitions

- **D1 (ST import).** A named standard result from outside the R Theory chain,
  admitted as a conditional premise (book label ST): the SO(16) irrep
  decompositions, the 135 → SO(10)×SU(4) branching content, Schur's lemma /
  Frobenius–Schur machinery, and the so(10)⊕so(6) ⊂ so(16) branching rules.
  Nothing proved *from* an import exceeds the import.
- **D2 (conditional inference).** A conclusion proved outright from premises
  stated with it; the conclusion is only as established as its premises. The
  γ₁₇ projector (§3.10) is of this form.
- **D3 (manuscript-reading fact).** A statement about what v1 prints, verified
  by a completed text search (this run or the cited chunk-4 audit) — a fact
  about the manuscript, not a theorem.
- **D4 (IC exhibit).** A verified refutation: the negated manuscript claim is
  proved from established premises.
- **D5 (manuscript admission).** The book's own "OPEN" / "NOT established"
  statements: true statements about what the chain does not supply, recorded
  here as ASSERTED admissions, never as proved results.

## 2. Claim inventory (from the book page)

| # | Claim (page label) | Page scope | Worker scope |
|---|---|---|---|
| C1 | C(16,4) = 1820 (Fig 1) | CP | **PROVED** |
| C2 | 1820 invariant pairing symmetric; FS indicator +1 (Fig 1 note) | CP | **PROVED** (direct properties); uniqueness step conditional on ST import; M_e/Oprop equivariance question **ASSERTED** (open) |
| C3 | Sym²(128)/Λ²(128) dimension spine; IC-12 refutation (Fig 2) | CP/ST; IC | **PROVED** (arithmetic + refutation, conditional on ST decomposition import) |
| C4 | Branching arithmetic 135 (Fig 3) | CP/ST | **PROVED** (arithmetic, conditional on ST content import) |
| C5 | Conversion-chain algebraic closure (Fig 4) | CP | **PROVED**; S_F value OPEN (admission); prefactor physical content **ASSERTED** (MA) |
| C6 | Conditional projector idempotency (Fig 5) | CP (conditional) | **PROVED** (conditional on γ₁₇²=+1); γᵢ relations OPEN (admission) |
| C7 | C8 word structure (Fig 6) | CP | **PROVED** (word bookkeeping); contraction/target 54 NOT established (admission) |
| C8 | 2⁷ = 128; dimension spine (Part II) | CP | **PROVED** |
| C9 | T-matrix spine, exact rationals (Part II) | CP | **PROVED** |
| C10 | (√2)⁴ = 4, (√2)⁸ = 16 (Part II) | CP | **PROVED** |
| C11 | V_E⁴ ≈ 638.78 within 0.05 (Part II) | NC | **CHECKED** (this run) |
| C12 | IC-13: 1820-basis construction defects (§18.8 Step 1) | IC | **PROVED** (rank-nullity arithmetic) on **CHECKED** audit reading |
| C13 | IC-14: 128⁴ vs 1820×8256 sandwich (§18.8 Steps 2–3) | IC | **PROVED** (exact inequality) on **CHECKED** audit reading |
| C14 | IC-15: −(1/256) double-counted (§18.8 Steps 6–7) | IC | **PROVED** (exact substitution) on **CHECKED** text fact |
| C15 | IC-16: wickSign never assigned (§18.8 Step 5) | IC | **CHECKED** (completed text search) |
| C16 | IC-17: §18.2 gamma template (new) | IC | **PROVED** (dimension mismatch) + **CHECKED** (textual facts) |
| C17 | P_54 location adjudicated: 54 ⊂ 135; no equivariant 1820→54 map (W1/U-19; **postdates the page**) | SC (campaign) | **CHECKED** |
| C18 | Explicit P_54 projector matrix constructed (W6a; **postdates the page**) | SC (campaign) | **CHECKED** |
| C19 | IC-19: v1:3470 "1820 … projects onto the 54 of SO(10)" incorrect as stated under the standard embedding (W1/U-19/W6a; **postdates the page**) | SC (campaign) | **CHECKED** (refutation) |
| C20 | Closure: roadmap, algebra checked, construction open (Part IV) | — | **ASSERTED** (bookkeeping) |

Open admissions carried through (D5): explicit 1820×1820 E, B, O matrices; the
explicit 1820 projector (blocked at P_6435); the 120 embedding; the S_F numerical
value; N_1820; the γᵢ Clifford relations; the physical content of the −√10/1536
prefactor; the physical embedding selection (which 10 of the 16 is "the" SO(10)).

## 3. Proofs in dependency order

### 3.1 Arithmetic basis (used by §3.2–§3.9)

Integer/rational identities below are proved by direct closed-form arithmetic:
multiplication as repeated addition (Def VII.15, used), commutativity (7.16,
used), and the common notions (CN 1: things equal to the same thing are equal;
CN 2: equals added to equals give equal wholes; CN 3: equals subtracted from
equals leave equal remainders). No further Euclid is invoked.

### 3.2 C(16,4) = 1820 (C1) — PROVED

C(n,4) counts 4-element subsets of an n-element set: n(n−1)(n−2)(n−3) ordered
choices, each 4-set occurring 4! = 24 times, so C(n,4) = n(n−1)(n−2)(n−3)/24.
At n = 16: 16·15·14·13 = 43680; 43680/24 = 1820 exactly. ∎ (This run:
`math.comb(16,4) == 1820`, exact, exit 0.)

### 3.3 Dimension spine (C8, and the arithmetic of C3) — PROVED

2⁷ = 128. dim Sym²(128) = 128·129/2: 128·129 = 16512, /2 = 8256.
1 + 1820 + 6435 = 8256 (CN 2). dim Λ²(128) = 128·127/2: 128·127 = 16256,
/2 = 8128. 120 + 8008 = 8128. ∎ (This run: all exact, exit 0.)

### 3.4 IC-12 refutation (C3) — PROVED, conditional on the ST decomposition

Admit as ST import (D1): as SO(16) representations,
Sym²(128) = 1 ⊕ 1820 ⊕ 6435 and Λ²(128) = 120 ⊕ 8008 — standard representation
theory, not derived here. The list of Sym² parts is then exactly {1, 1820, 6435};
by inspection 120 ≠ 1, 120 ≠ 1820, 120 ≠ 6435, so the 120 occurs in none of the
Sym² parts. Hence §18.4's "the 120 = Λ²(16) sits inside Sym²(128)" is false as
stated (it repeats the §17.18 IC-6 error). ∎ (This run re-verified the
"120 not in (1,1820,6435)" exclusion, exit 0.)

### 3.5 Branching arithmetic (C4) — PROVED, conditional on the ST content

54 + 20 + 60 + 1 = 135 (CN 2). 135 = 16·17/2 − 1: 16·17 = 272, /2 = 136,
136 − 1 = 135 (CN 3) — i.e. 135 = dim Sym²₀(16). 54 = 55 − 1 — i.e.
54 = dim Sym²₀(10). For the restriction
135|_{SO(10)×SU(4)} = (54,1) ⊕ (1,20′) ⊕ (10,6) ⊕ (1,1):
54·1 + 1·20 + 10·6 + 1·1 = 54 + 20 + 60 + 1 = 135, dimensionally exact. ∎
The SO(10)/SU(4) representation content itself is an ST import (D1), not derived
here. (This run: staircase partial sums 54 → 74 → 134 → 135 exact, exit 0.)

### 3.6 T-matrix spine (C9) — PROVED

T = diag(1, 1, −1/4 ×8): trace = 1 + 1 − 8·(1/4) = 2 − 2 = 0 (traceless).
‖T‖² = 1² + 1² + 8·(1/4)² = 2 + 8/16 = 5/2.
‖Q_F‖² = (6/5)²·(5/2) = (36/25)·(5/2) = 180/50 = 18/5.
(1/4)⁴ = 1/256. ∎ (Exact rationals; this run: all exact, exit 0.)

### 3.7 Conversion-chain algebraic closure (C5) — PROVED; no established point

(6/5)(5/2) = 30/10 = 3. From S_F = 3a_{2222}: a = S_F/3 (S_F a free parameter).
From a = (6/5)c: c = (5/6)a = (5/6)(S_F/3) = 5S_F/18.
−(1/256)(√10/6) = −√10/1536 by the field axioms (256·6 = 1536). ∎
The chain closes algebraically for every value of the parameter S_F — and there
is no established point on it: the S_F numerical value is OPEN (manuscript
admission, D5), and the physical content of the −√10/1536 prefactor is a
manuscript assertion (ASSERTED). (This run: chain identities exact, exit 0.)

### 3.8 Tension arithmetic (C10) — PROVED

(√2)⁴ = ((√2)²)² = 2² = 4; (√2)⁸ = ((√2)⁴)² = 4² = 16. ∎ (Exact; this run:
residuals ≤ 7.2e-15, pure float rounding.) The page's textual observation that
the value 16 at v1:3542 matches the all-eight product, not the propagator
product, is a manuscript-reading fact (D3), verified against v1 by the audit.

### 3.9 V_E⁴ bound (C11) — CHECKED

This run: 5.0273⁴ = 638.762201; |5.0273⁴ − 638.78| = 0.0178 < 0.05. ∎
(Completed numerical run, exit 0 — a bound check, not a proof.)

### 3.10 Conditional projector idempotency (C6) — PROVED as a conditional inference

Lemma: let γ₁₇ satisfy γ₁₇² = +1. Then for Π± = (1 ± γ₁₇)/2,
Π±² = (1 ± 2γ₁₇ + γ₁₇²)/4 = (2 ± 2γ₁₇)/4 = (1 ± γ₁₇)/2 = Π±. ∎
Sign: (−1)^120 = +1 since 120 is even. ∎
The premise γ₁₇² = +1 (the γᵢ Clifford relations) is OPEN in v1 (manuscript
admission, D5) — so the conclusion is a conditional inference, not an established
fact about the manuscript's operators. ASSERTED as premise where used.

### 3.11 C8 word structure (C7) — PROVED (bookkeeping); contraction not established

The cyclic word (E,B,E,O)×2 has 8 entries: E ×4, B ×2, O ×2 (counting). Entry k
at 22.5° + 45°(k−1): E on 22.5, 112.5, 202.5, 292.5 (octants 1,3,5,7); B on
67.5, 247.5 (octants 2,6); O on 157.5, 337.5 (octants 4,8). ∎ (This run: exact,
exit 0.) The contraction itself is NOT established: the skeleton has the four
defects C12–C15, the 1820 projector is blocked (P_6435), and the "→ 54" target
via the 1820 route is additionally barred by the C19 no-go. (Manuscript
admissions, D5; the page's center label "NOT established" is accurate.)

### 3.12 The 1820's invariant pairing is symmetric (C2) — PROVED (direct part), uniqueness conditional on ST import

Work with the complex-bilinear extension of the real dot product to ℂ¹⁶
(⟨e_i, e_j⟩ = δ_ij on a basis). On W = Λ⁴(ℂ¹⁶) set
B(v₁∧v₂∧v₃∧v₄, w₁∧w₂∧w₃∧w₄) = det(⟨v_k, w_ℓ⟩).

*Well-defined.* The right-hand side is multilinear in the eight arguments;
swapping two v's swaps two rows of the Gram matrix, flipping the determinant's
sign — matching the wedge sign — so it factors through Λ⁴ ⊗ Λ⁴ and extends by
linearity. ∎
*Symmetric.* Gram(w, v) = Gram(v, w)ᵀ for symmetric ⟨·,·⟩; det is transpose-
invariant. ∎
*SO(16)-invariant.* g ∈ SO(16) acts orthogonally: ⟨gv_k, gw_ℓ⟩ = ⟨v_k, w_ℓ⟩,
so the Gram matrix — and its determinant — is unchanged. ∎
*Nondegenerate.* On basis 4-vectors e_I, e_J (I, J increasing 4-tuples):
B(e_I, e_J) = det(δ_{i_k, j_ℓ}); if I ≠ J as sets some row vanishes (det 0);
if I = J as sets the Gram matrix is a permutation matrix (det ±1). Diagonal
±1 on the basis: nondegenerate. ∎

*Uniqueness.* An SO(16)-invariant pairing is an element of Hom_G(W⊗W, 1) ≅
Hom_G(W, W*). By Schur's lemma (ST import, D1) and the Frobenius–Schur indicator
+1 — i.e. W ≅ W* via a symmetric isomorphism (ST import, D1) — this space is
one-dimensional, spanned by the symmetric B above; every invariant pairing is
λB, hence symmetric. No alternating invariant pairing exists. ∎
(Conditional on the two ST imports; the constructed B's properties are proved
directly.)
*Scope retained from the page:* this constrains pairings, not operators —
whether the manuscript's M_e/Oprop are SO(16)-equivariant at all is still a
manuscript-reading question (ASSERTED, open).

### 3.13 The IC exhibits (C12–C16)

**C12 — IC-13 (rank-nullity).** For an m×n matrix, nullity = n − rank.
An 8256×1 matrix has nullity = 1 − rank ∈ {0, 1}: nonzero column → rank 1 →
nullity 0 (the code as written yields {}). A 1×8256 matrix has nullity =
8256 − rank: generic rank 1 → nullity 8255; and 8255 ≠ 1820 (CN 3), so the
intended reading yields 8255 dimensions, not 1820. ∎ (Nullity arithmetic
PROVED; this run re-verified it, exit 0.) The premise — what §18.8 Step 1
prints "as written" vs. the "intended reading" — is the chunk-4 audit's
verified manuscript reading (CHECKED; `~/workspace/vol4/book18/LEDGER_18.md`).
"Needs P_6435; unfixable within v1" is the audit's judgment (ASSERTED).

**C13 — IC-14 (dimension incompatibility).** 128⁴ = (2⁷)⁴ = 2²⁸ = 268435456
exactly; 8256 ≠ 268435456. The §18.8 Steps 2–3 sandwich pairs a 128⁴×128⁴
Kronecker product against 1820×8256 inner dimensions — dimensionally
incompatible as written. ∎ (Exact inequality PROVED, on the audit's verified
reading of the steps — CHECKED.)

**C14 — IC-15 (double-counted −(1/256)).** This run verified by text search
that v1's Book 18 range prints both `S_F = -(1/256) * S_F_raw;` and
`nHat54 = -(Sqrt[10]/1536) * S_F * m2^(-4);` (CHECKED, D3). Substituting the
first into the second: nHat54 = +(√10/393216)·S_F_raw·m2^{−4} — the −(1/256)
factor is applied twice relative to the section's own stripped definition
S_F := ⟨Q_F, R̃⟩. ∎ (Exact substitution algebra PROVED; this run: err 0.0.)

**C15 — IC-16 (wickSign never assigned).** This run: `wickSign` occurs exactly
once in the v1 Book 18 range and is never assigned there (completed text
search, exit 0) — CHECKED (D3). Hence the Step-5 sum cannot execute as written;
its ranges are further abbreviated away in the duplicate. ∎

**C16 — IC-17 (gamma template).** Eight factors of 2×2 matrices tensor to
(2⁸)×(2⁸) = 256×256 matrices (dimension multiplication); the section requires
explicit 128×128 matrices acting on the 128-dimensional chiral spinor;
256 ≠ 128. ∎ (Dimension mismatch PROVED.) Textual: σ_a is never defined; the
template shows only i = 1…8 for the 16 required matrices; the "appropriate
extensions for i = 9…16" are undefined — verified by this run's text search
(CHECKED, D3). The printed template cannot produce what the section asks for. ∎

### 3.14 P_54 location adjudicated (C17) — CHECKED (postdates the page)

The page's "135 vs 1820 unreconciled in v1" is accurate for v1, but the
campaign has since closed the location question. W1 (`~/workspace/vol4/
w1_54_branching/`, SC, exit 0, two independent implementations with exact
A/B agreement), under the standard so(10)⊕so(6) ⊂ so(16) embedding with
standard branching rules (ST import, D1):
135 = (54,1) ⊕ (10,6) ⊕ (1,20′) ⊕ (1,1) — exactly one 54, multiplicity 1;
1820 = (210,1) ⊕ (120,6) ⊕ (45,15) ⊕ (10,10) ⊕ (10,10′) ⊕ (1,15) — **no**
54 constituent (dim sum 210+720+675+100+100+15 = 1820 ✓).
Hence v1:2265 "the physical 54 inside the 135 of SO(16)" is CONFIRMED and
v1:1956 "embedding of 54 in 1820" is REFUTED as an equivariant embedding under
the standard embedding (consistent with the U-19 no-go: no SO(10)-equivariant
1820→54 map exists). ∎ (CHECKED — exact-integer branching computation,
independently re-implemented; the branching rules themselves are ST imports.)
Remaining open: the physical embedding selection (which 10 of the 16 is "the"
SO(10)) — awaits the E/B/O operators (manuscript admission, D5).

### 3.15 Explicit P_54 projector constructed (C18) — CHECKED (postdates the page)

W6a (`~/workspace/vol4/w6_remaining_puzzles/`, SC): the (54,1) ⊂ 135 projector
as an explicit 135×135 matrix, via two independent routes agreeing to 4.4e-15:
(i) the so(10)-Casimir 54-dimensional eigenspace (eigenvalue 20; joint
(c10,c6) spectrum (20,0)×54 + (9,5)×60 + (0,12)×20 + (0,0)×1, all
Weyl-predicted); (ii) closed form P_54(T) = P_10·T·P_10 −
(1/10)·tr(P_10·T·P_10)·P_10 on 16×16 traceless symmetric matrices. Hermitian,
idempotent, tr = 54, commutes with so(10)⊕so(6) (max residual 3.4e-15).
Artifacts: `P54_135.npy`, `P54_basis_135x54.npy`, `P54_as_16x16.npy`
(54 explicit 16×16 matrices, orthonormal, supported on the 10-block). ∎
(CHECKED — completed computation; not an analytic proof. Manifest:
`w6a_manifest.json`, 23/23 checks.) The page's "where the P_54 projector
lives" gap is filled at the matrix level; the physical selection (§3.14) is
still open.

### 3.16 IC-19: v1:3470 incorrect as stated (C19) — CHECKED refutation (postdates the page)

From C17: under the standard embedding the 1820 has no 54 constituent, so no
SO(10)-equivariant 1820→54 map exists (U-19). Therefore v1:3470 — "the 1820
antisymmetric rank-4 SO(16) tensor projects onto the 54 of SO(10)" — is
incorrect as stated under the standard embedding. ∎ (CHECKED refutation;
recorded in `NOTATION_LEDGER.md` §P_54-location row as IC-19 CONFIRMED.)
Consequence for this book: the C8 word's "→ 54" target cannot be reached by a
1820→54 projection route; the contraction's target must be the (54,1) ⊂ 135 —
whose explicit projector now exists (C18) but whose physical selection and
executing skeleton remain open.

### 3.17 Closure (C20) — ASSERTED

Bookkeeping, consistent with the above: established — the
dimension/combinatorics spine, the branching arithmetic, the conversion chain's
algebraic closure, the conditional projector idempotency, the P_54 location
(135) and its explicit matrix (C17–C18, post-page); not established — the
explicit E/B/O matrices, the 1820 projector, the 120 embedding, the S_F value,
the γᵢ relations, the executing contraction skeleton (defective in both
printings), and the physical embedding selection. Book 18 remains a roadmap
with the algebra checked and the construction open. ∎ (ASSERTED.)

## 4. New axioms/assumptions beyond Euclid + seed + earlier books

Introduced by Book 18 itself (v1's, unless noted):

1. **A18.1 — Contraction input data.** Explicit 1820×1820 E, B, O matrices
   exist and are available. ASSERTED (manuscript assumption; OPEN — the
   manuscript admits them missing).
2. **A18.2 — Explicit 1820 projector.** Exists (blocked at P_6435). ASSERTED
   (OPEN).
3. **A18.3 — M_e / Oprop SO(16)-equivariance.** Assumed wherever equivariance
   is invoked. ASSERTED (manuscript-reading question, OPEN).
4. **A18.4 — The γᵢ Clifford relations**, including γ₁₇² = +1 (conditional
   premise of the projector inference). ASSERTED (OPEN in v1).
5. **A18.5 — Physical content** of the −√10/1536 prefactor and of S_F.
   ASSERTED (manuscript assertion).
6. **A18.6 — Numerical values**: S_F, N_1820. ASSERTED (OPEN admissions).
7. **The standard embedding** so(10)⊕so(6) ⊂ so(16) as the reference embedding
   for C17/C19 — a declared choice, not proved canonical (ASSERTED).
8. **ST imports** (premises, not axioms of the theory): ST1 — SO(16) irrep
   decompositions Sym²(128) = 1⊕1820⊕6435, Λ²(128) = 120⊕8008; ST2 — the
   135 → SO(10)×SU(4) branching content; ST3 — Schur's lemma + Frobenius–Schur
   indicator machinery (C2 uniqueness step); ST4 — the so(10)⊕so(6) branching
   rules (C17/C19).

No new Euclidean postulate, no new common notion. No Elements proposition is
extended by this book (per the ledger mappings and §0).

## 5. Counts

Claim-level (C1–C20):
- **PROVED: 14** — C1, C2 (direct construction + properties; uniqueness step
  conditional on ST3), C3 (conditional on ST1), C4 (conditional on ST2), C5, C6
  (conditional on A18.4), C7 (word bookkeeping), C8, C9, C10, C12 (nullity
  arithmetic, on the CHECKED audit reading), C13 (on the CHECKED audit reading),
  C14 (substitution, on the CHECKED text fact), C16 (dimension mismatch).
- **CHECKED: 5** — C11 (numerical bound, this run), C15 (text search, this
  run), C17 (W1 exact-integer branching, two implementations), C18 (W6a
  projector construction), C19 (refutation via C17/U-19).
- **ASSERTED: 1** — C20 (closure bookkeeping); plus the 6 open manuscript
  admissions (A18.1–A18.6) and the 4 ST imports recorded as ASSERTED premises.
- **INCOMPLETE: 0** — every check this worker attempted ran to completion
  (verify_book18.py exit 0, 42/42, no timeouts; worst deviation 0.0178 on the
  NC bound check, all exact-integer checks at 0).
