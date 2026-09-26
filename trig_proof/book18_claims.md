# Book 18 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book18_proof.md` (claim inventory
C1–C20; §3.14–3.16 record post-page campaign results W1/W6a/U-19 that supersede
two of the page's v1 admissions, flagged as such). Evaluated 2026-09-22.

**Verification method.** All 20 proofs read in full. The load-bearing exact
arithmetic was independently re-derived and checks exactly: C(16,4) = 1820;
the dimension spine 128·129/2 = 8256, 1+1820+6435 = 8256, 128·127/2 = 8128,
120+8008 = 8128; the 135 branching sums; the T-matrix exact rationals
(trace 0, ‖T‖² = 5/2, ‖Q_F‖² = 18/5, (1/4)⁴ = 1/256); the conversion chain
(6/5)(5/2) = 3, c = 5S_F/18; 128⁴ = 268435456. The book's verification script
`~/workspace/r-theory-rewrite/validation/book18/verify_book18.py` was
**re-run here** 2026-09-22 — exit 0, all 42 checks passed (41 CP, 1 NC), no
timeouts. The NC bound check (C11) was re-computed: 5.0273⁴ = 638.7622,
deviation 0.0178 < 0.05. Euclid common notions CN 1–3 and Def VII.15 / 7.16
are cited in the book as used-only arithmetic substrate; no Elements
proposition is extended by any Book 18 claim, and no trig principle here
needs a Euclid citation — none is made.

**Scope labels:** PROVED (exact mathematics, complete; some conditional on a
named ST import or open premise, stated in Notes), CHECKED (a completed
computation supports it, no analytic proof), ASSERTED (manuscript
claim/assumption/convention/status declaration), INCOMPLETE (failed, timed
out, or unfinished — none here).

## PROVED claims (14)

| Claim | Restatement | Verdict | Notes |
|---|---|---|---|
| C1 | C(16,4) = 1820: 16·15·14·13 = 43680, /24 = 1820 | proof verified (re-derived; `math.comb(16,4) == 1820`) | PROVED — pure combinatorics, no trig content |
| C2 | the 1820's invariant pairing is symmetric (direct construction B(v∧…,w∧…) = det⟨v_k,w_ℓ⟩: well-defined, symmetric, SO(16)-invariant, nondegenerate) | proof verified by reading each step | PROVED (direct part); uniqueness step conditional on ST import (Schur + Frobenius–Schur indicator +1); whether M_e/Oprop are SO(16)-equivariant at all is ASSERTED (open manuscript-reading question) — rep. theory, no trig content |
| C3 | dim Sym²(128) = 8256 = 1+1820+6435; dim Λ²(128) = 8128 = 120+8008; IC-12 refutation: 120 occurs in none of the Sym² parts | arithmetic verified exactly; exclusion by inspection | PROVED, conditional on ST import Sym²(128) = 1⊕1820⊕6435 (the decomposition itself is admitted, not derived) — rep. theory, no trig content |
| C4 | 135 branching arithmetic: 54+20+60+1 = 135; 135 = 16·17/2−1 = dim Sym²₀(16); 54 = 55−1 = dim Sym²₀(10); restriction dims sum to 135 | verified exactly (staircase 54→74→134→135) | PROVED, conditional on ST import of the SO(10)/SU(4) representation content (not derived here) — rep. theory, no trig content |
| C5 | conversion-chain algebraic closure: (6/5)(5/2) = 3, a = S_F/3, c = 5S_F/18, −(1/256)(√10/6) = −√10/1536 | verified exactly | PROVED as formal algebra; S_F numerical value is OPEN (manuscript admission) and the −√10/1536 prefactor's physical content is ASSERTED (manuscript assertion) — algebra, no trig content |
| C6 | conditional projector idempotency: γ₁₇² = +1 ⇒ Π± = (1±γ₁₇)/2 idempotent; (−1)^120 = +1 | lemma verified step by step | PROVED as conditional inference; the premise γᵢ Clifford relations are OPEN in v1 (manuscript admission) — matrix algebra, no trig content |
| C7 | C8 word bookkeeping: (E,B,E,O)×2 has 8 entries (E×4, B×2, O×2); entry k at 22.5° + 45°(k−1); octant assignments | verified by counting | PROVED; the angles are positional labels, not trig functions — no trig identity |
| C8 | 2⁷ = 128 | PROVED | arithmetic, no trig content |
| C9 | T-matrix spine exact rationals: trace 0, ‖T‖² = 5/2, ‖Q_F‖² = 18/5, (1/4)⁴ = 1/256 | verified exactly (Fraction arithmetic) | PROVED — rational arithmetic, no trig content |
| C10 | (√2)⁴ = 4, (√2)⁸ = 16 | verified | PROVED (exact; the float residuals ≤ 7.2e-15 are a completed float check of the same identity) — algebraic power, no trig content |
| C12 | IC-13 nullity arithmetic: 8256×1 matrix nullity ∈ {0,1}; 1×8256 generic nullity 8255 ≠ 1820 | nullity arithmetic verified (rank–nullity) | PROVED, on the chunk-4 audit's CHECKED manuscript reading of §18.8 Step 1; "unfixable within v1" is the audit's ASSERTED judgment — refutation, no trig content |
| C13 | IC-14: 128⁴ = 268435456 exactly, incompatible with the 1820×8256 sandwich of §18.8 Steps 2–3 | exact inequality verified | PROVED, on the CHECKED audit reading of the steps — refutation, no trig content |
| C14 | IC-15: v1 prints both S_F = −(1/256)·S_F_raw and nHat54 = −(√10/1536)·S_F·m2^{−4}; substitution gives nHat54 = +(√10/393216)·S_F_raw·m2^{−4} — the −(1/256) is applied twice | substitution algebra verified (err 0.0); the textual premise is a CHECKED text-search fact (re-run passes) | PROVED, on a CHECKED manuscript-reading fact — refutation, no trig content |
| C16 | IC-17 dimension mismatch: eight 2×2 factors tensor to 256×256 ≠ the required 128×128; σ_a undefined; only i = 1…8 shown of 16 required | mismatch verified; textual facts are CHECKED text-search results (re-run passes) | PROVED, on CHECKED textual facts — refutation, no trig content |

## CHECKED claims (5)

| Claim | What it rests on | Scope | Folded in? | Notes |
|---|---|---|---|---|
| C11 | V_E⁴ ≈ 638.78 within 0.05: completed numerical run — 5.0273⁴ = 638.7622, deviation 0.0178 < 0.05 (re-computed here; script NC check passes) | CHECKED | no — a decimal bound check, no analytic proof, and no trig content | — |
| C15 | IC-16: `wickSign` occurs exactly once in the v1 Book 18 range and is never assigned — completed text search (re-run passes) | CHECKED | no — manuscript-reading fact, not trig | — |
| C17 | P_54 location adjudicated: W1 exact-integer branching under the standard so(10)⊕so(6) ⊂ so(16) embedding — 135 = (54,1)⊕(10,6)⊕(1,20′)⊕(1,1), 1820 has no 54 constituent (dim sums check); two independent implementations in exact agreement | CHECKED | no — representation-theory computation; the branching rules are ST imports and the embedding choice is ASSERTED, not proved canonical | — |
| C18 | explicit P_54 projector: W6a 135×135 matrix via two independent routes agreeing to 4.4e-15; Hermitian, idempotent, tr = 54, commutes with so(10)⊕so(6) (residual 3.4e-15); manifest 23/23 checks | CHECKED | no — completed computation, not an analytic proof | — |
| C19 | IC-19: v1:3470 "1820 … projects onto the 54 of SO(10)" incorrect as stated under the standard embedding — refutation via C17/U-19 (no SO(10)-equivariant 1820→54 map) | CHECKED | no — refutation grounded in the CHECKED C17 result | — |

## ASSERTED claims (1)

| Claim | Restatement | Scope | Notes |
|---|---|---|---|
| C20 | closure: roadmap established (dimension/combinatorics spine, branching arithmetic, conversion-chain algebra, conditional projector idempotency, P_54 location + explicit matrix) vs. not established (explicit E/B/O matrices, 1820 projector, 120 embedding, S_F value, γᵢ relations, executing contraction skeleton, physical embedding selection) | ASSERTED (bookkeeping verdict) | status declaration, not mathematics |

## Candidate TRIGONOMETRIC PRINCIPLES

**None.** Book 18 contains no trigonometric content. Its proved material is
combinatorics (C1), integer/rational dimension arithmetic (C3, C4, C8, C9),
exact algebra (C5, C10), matrix/operator algebra (C2 direct part, C6
conditional lemma), and representation-theoretic refutations (C3, C12–C14,
C16). The angular positions in C7 (22.5°, 45° octant labels) are bookkeeping
labels for the word entries, not statements about trigonometric functions,
and yield no identity. Forcing a "principle" out of this book would be
inflation. No Euclid proposition is needed or cited for any candidate —
there are no candidates.

## Claims not made into principles

- **C1, C8, C9, C10** — exact combinatorics/arithmetic: no trig functions, no
  identities.
- **C2 (direct part), C3, C4, C6** — representation theory and matrix
  algebra: identities, but about irreps/pairings/projectors, not about
  trigonometric, circular, or hyperbolic measure.
- **C5** — formal algebraic closure of a conversion chain: no trig content.
- **C7** — angular labels are positional bookkeeping, not trig functions.
- **C11** — a completed decimal bound on a fourth power: no trig content.
- **C12–C16** — refutation exhibits (dimension mismatches, double-counted
  factor, unassigned symbol): negative manuscript findings, no identities.
- **C17–C19** — post-page campaign computations (branching, projector matrix,
  refutation): no trig content.
- **C20** — bookkeeping verdict: asserted, not a theorem.

## Counts

- Evaluated: **20** (14 PROVED, 5 CHECKED, 1 ASSERTED, 0 INCOMPLETE)
- Folded into the cumulative trigonometric proof: **0** (no claim has
  trigonometric content)
- Not folded: **20** — 19 evaluated with no new trigonometric content
  (combinatorics/arithmetic, representation theory, refutations, one
  numerical bound), 1 asserted bookkeeping verdict

status: complete
