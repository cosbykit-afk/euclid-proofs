# Book 3 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book3_proof.md` (claim inventory
C1–C57 plus one zero-counts bookkeeping row), evaluated 2026-09-22.

**Verification method.** All 57 claim proofs plus the zero-counts row read
in full. The load-bearing algebraic identities were independently
re-derived and check out exactly: C3 (addition formulas), C13
(Q₋∘Q₊ = id, Q₊²(t) = −1/t, exact order 4, marked orbit
0→1→∞→−1→0), C14 (cross-ratio limit → −1), C15 (conjugation
−Q₊(−t) = Q₋(t)), C16 (inverse u = (1−s²)/(2s), reciprocal, e^{−arsinh u}),
C18 (primitive generation via 1+cot²x = csc²x), C19 (threshold), C25
(sin 2x = 4t(1−t²)/(1+t²)² re-derived from tan x = 2t/(1−t²) and
sin 2x = 2tan x/(1+tan²x)), C27 (cyclic product), C33 (sign
factorization), C37–C43 (Stiefel–Whitney binomial arithmetic, e.g.
C(n+1,2) = (m+1)(2m+1) even ⟺ m odd for n = 2m+1), C48 (sxp(θ) =
csc θ − cot θ = tan(θ/2) on (0,π)). The book's reported numerical runs
(`~/workspace/r-theory-rewrite/validation/book3/verify_book3.py`, 67
checks, exit 0, no timeouts, worst plotted-identity residual 3.7e-13)
are cited as CHECKED, not re-run, per the proof-over-sampling rule.

**Euclid boundary.** No proposition of Euclid's *Elements* is a logical
premise of any Book 3 claim. The proof file states this explicitly (the
No-Euclid-wholesale boundary: rewrite Book 3's circle is the analytic
phase circle, not Euclid's synthetic circle; the book-3 Euclid ledger
finds the extension program INCOMPLETE across all 37 circle
propositions), and no Elements proposition is cited in any proof. This is
stated plainly rather than via ledger citation, since no ledger
proposition is used.

**Scope labels:** PROVED (exact mathematics, complete), CHECKED
(completed numeric run, no analytic proof), ASSERTED (manuscript
claim/assumption/import/convention/status declaration), INCOMPLETE
(failed, timed out, or unfinished — none here).

## PROVED claims (34, incl. the zero-counts bookkeeping row)

| Claim | Restatement | Verdict | Folded in? | Notes |
|---|---|---|---|---|
| C1 | τ_{π/2} has exact order 4 on 𝕋₂π; τ_{π/2}² = τ_π ≠ id | proof verified (re-derived: translations compose by addition; π ≢ 0 mod 2π) | yes — already registered as row 29 (Book 3) | — |
| C2 | cophase relation symmetric, irreflexive, not transitive | proof verified (0→π/2→π is the non-transitivity witness) | no — relation logic, not a trig identity | — |
| C3 | sin(x+π/2) = cos x, cos(x+π/2) = −sin x (and −π/2 forms up to sign) | proof verified from declared standard-analysis premises I1 | yes — already registered as row 28 (Book 3) | — |
| C4 | on 𝕋_π the two cophase directions coincide as one involution of exact order 2 | proof verified (x+π/2 ≡ x−π/2 mod π; one step ≠ id since π/2 ≢ 0 mod π) | yes — already registered as row 30 (Book 3) | — |
| C5 | ordered bases of ℝ² split into two determinant-sign classes | proof verified from I2 | no — linear algebra, not a trig identity | wording caveat: what is reference-independent is the unlabeled two-class *partition*; the assigned ±1 values flip if the change of reference basis has det < 0. The proved substance is the partition. |
| C6 | each translation τ_a is orientation-preserving on the circle | proof verified (derivative +1 on ℝ, inherited by the quotient) | no — analysis, not an identity | — |
| C8 | η = τ_{π/4} has exact order 8; faithful cyclic action on the eight octants | proof verified (8·(π/4) = 2π; k·(π/4) ≡ 0 mod 2π ⟺ 8\|k) | yes — already registered as row 31 (Book 3) | — |
| C12 | t = tan(x/2) is a bijection 𝕋₂π → ℝ̂; x = ±π ↦ ∞ | proof verified from I1 (strict monotonicity on (−π,π), endpoint limits) | yes — already registered as row 32 (Book 3) | — |
| C13 | directed cophase acts as t ↦ Q_±(t); Q₊²(t) = −1/t; Q₊ exact order 4 in PGL(2,ℝ); marked orbit = cardinal phases | proof verified (re-derived: tan addition formula, Q-algebra, orbit via C12) | yes — already registered as row 33 (Book 3) | — |
| C14 | harmonic cross-ratio (0,∞;1,−1) = −1 (ordering matters) | proof verified (re-derived projective limit) | yes — already registered as row 34 (Book 3) | — |
| C15 | det A₊ = +2 (orientation-preserving) vs det R = −1 (reversing); R∘Q₊∘R = Q₋ | proof verified (re-derived conjugation) | yes — already registered as row 35 (Book 3) | — |
| C16 | f(u) = √(1+u²)−u is a strictly decreasing bijection ℝ → (0,∞); inverse u = (1−s²)/(2s); f(−u)f(u) = 1; f(u) = e^{−arsinh u} | proof verified (re-derived all four) | yes — already registered as row 36 (Book 3) | — |
| C17 | sgn(u) = sgn(1−s²) with s = f(u) | proof verified from C16 (s = 1 ⟺ u = 0; strict decrease) | yes — already registered as row 37 (Book 3) | — |
| C18 | sxp = f(cot x), srx = f(−cot x), crx = f(tan x), cxp = f(−tan x); ln srx = −ln sxp = arsinh(cot x) | proof verified (re-derived via 1+cot² = csc²) | yes — already registered as row 38 (Book 3) | log-coordinate half duplicates Book 0 P16 (srx = e^{asinh(cot x)}) |
| C19 | sgn(1−sxp²) = sgn(srx²−1) (and cxp/crx analogue) | proof verified (srx = 1/sxp, srx²−1 = (1−sxp²)/sxp²) | yes — already registered as row 39 (Book 3) | — |
| C20 | unequal limits lim_{+∞}f = 0⁺, lim_{−∞}f = +∞ bar a single-valued global RP¹ coordinate via f | proof verified from C16 | yes — already registered as row 40 (Book 3) | — |
| C21 | Γ_c = ⟨τ_{π/2}⟩ ≅ C4 preserves the FlatWave domain D | proof verified (seams x = kπ/2 permuted k↦k+1; C1 gives C4) | yes — already registered as row 41 (Book 3) | — |
| C22 | FlatWave(x±π/2) = −FlatWave(x); FlatWave(x+π) = FlatWave(x); orbit ε→−ε→ε→−ε→ε | proof verified from I1 | no — already registered as Book 0 P7 (duplicative; listed as candidate for dedup) | — |
| C23 | χ_c(τ_{kπ/2}) = (−1)^k is a homomorphism Γ_c → {±1} with FlatWave(g·x) = χ_c(g)·FlatWave(x); ker = {id, τ_π}; factors C4 → C2 | proof verified (from C22, C1) | yes — already registered as row 42 (Book 3) | — |
| C24 | FlatWave\|_{O_j} = (−1)^{⌊j/2⌋} | proof verified (re-derived sign-of-sin interval check for all 8 octants) | yes — already registered as row 43 (Book 3) | — |
| C25 | FlatWave(x) = sgn[t(1−t²)], t = tan(x/2); cophase reverses, half-turn preserves the sign polynomial | proof verified (re-derived sin 2x = 4t(1−t²)/(1+t²)²) | yes — already registered as row 44 (Book 3) | — |
| C27 | on P° = {XYZ ≠ 0}: u_{XY}·u_{YZ}·u_{ZX} = 1; two ratios complete, inverse (a,b) ↦ [1:a:ab] | proof verified from the declared atlas I3 | no — ratio algebra on the declared projective atlas, conditional on import; not a trig identity | — |
| C33 | FlatWave = sgn(t)·sgn(1−t²) = (ρ*ζ_{YX})·sgn(1−t²); agrees with the tautological sign sgn(t) exactly on \|t\|<1, differs on \|t\|>1 | proof verified (exact sign algebra from C25; pullback cited from the page computation) | yes — already registered as row 45 (Book 3) | — |
| C35 | the ratio-transition signs (not FlatWave) realize w₁(γ) | proof verified conditional on the declared import I4 (sign-cocycle ⇒ w₁ identification) | no — bundle-class conclusion, not a trig identity | scope is PROVED-conditional (import I4 named) |
| C37 | w(T RP^n) = (1+a_n)^{n+1}; w₁ = (n+1)a_n; RP^n orientable iff n odd | proof verified modulo declared I5 | no — Stiefel–Whitney topology, not trig | — |
| C38 | RP¹ orientable while γ₁ nonorientable; RP² nonorientable with w₁ = a₂; RP³ orientable | proof verified modulo I5 (n = 1,2,3 substitutions re-derived) | no — topology, not trig | — |
| C40 | global positive-vs-mirror frame classification exists exactly for odd n, non-canonically | proof verified modulo I5 | no — topology, not trig | — |
| C42 | w₂(T RP^n) = C(n+1,2)·a_n²; n = 1 gives w₂ = 0 | proof verified modulo I5 | no — topology, not trig | — |
| C43 | RP^n spin iff n = 1 or n ≡ 3 mod 4; RP⁵ orientable but not spin; orientability strictly weaker | proof verified (parity argument re-derived) modulo I5 | no — topology, not trig | the "exactly two spin structures" clause is ASSERTED (SI import), not part of the proved claim |
| C48 | on 0 < θ < π: ‖r‖ = tan(θ/2) = sxp(θ); FlatWave seam θ = π/2 regular (q₀ = 1/√2 ≠ 0); chart boundary q₀ = 0 at θ → π | proof verified modulo I6 (sxp(θ) = tan(θ/2) re-derived via C18 + I1) | yes — already registered as row 48 (Book 3) | scope is PROVED-conditional (quaternion-model import I6 named) |
| C49 | no continuous lift selector s: SO(3) → S³ with Φ∘s = id; smooth local sections exist (Rodrigues q₀ > 0 hemisphere) | proof verified modulo I6 (section ⇒ trivial cover; S³ connected vs disconnected total space) | no — covering theory, not a trig identity | scope is PROVED-conditional (covering-theory import I6 named) |
| C50 | nothing factoring through SO(3) distinguishes q from −q; cophase/half-turn/deck have distinct quotient effects | proof verified (first clause definitional; rest via C22, C46, B47e, B26) | no — not a trig identity | the "every certified Book 2 operator is deck-invariant" bookkeeping clause is ASSERTED (not re-audited) |
| C54 | the twelve vocabulary items are kept distinct absent an explicit identifying theorem | proof verified as bookkeeping (absence of declared identification; C7, C33–C35, C40, C50 are the proved non-identifications) | no — meta/bookkeeping | — |
| C57 | provenance discipline; the three climaxes mutually compatible; no physical chirality from the math alone | proof verified as bookkeeping (follows from the proved separations) | no — meta/bookkeeping | the inheritance lock (3.XII.T6) is a constitutional rule — ASSERTED |
| zero counts | new axioms 0, external physics imports 0, projection contracts 0, preferred-orientation/lift/chirality axioms 0, empirical calibrations 0, new physical interactions 0 | proof verified as a bookkeeping count over the declaration list | no — meta | — |

## ASSERTED claims (15)

| Claim | Restatement | Scope | Folded in? | Notes |
|---|---|---|---|---|
| C7 | cophase–mirror separation (no declared bridge between phase and frame worlds); prohibited-substitutions list (x ↦ x±π/2, x ↦ −x, s ↦ 1/s, q ↦ −q may not be called "mirror") | ASSERTED (scope declaration / terminological stipulation) | no | bookkeeping about what was declared, not a theorem |
| C11 | π-periodicity inheritance of the primitives (Book 2) | ASSERTED (page MA; no Book 2 proof file in this batch) | no | — |
| C26 | χ_c detects cophase parity, not the four orbit positions | ASSERTED (interpretive gloss, page MA) | no | immediate from C23's {±1}-valuedness, but recorded as interpretation |
| C29 | compatibility lives only on P°; σ = 1 records a signed-ratio zero, not automatically mirror/orientation; u ↦ −u ≠ u ↦ 1/u | ASSERTED (methodological rules) | no | first and third clauses are immediate from C27's domain and algebra; the middle is the page's rule |
| C30 | seam-taxonomy overlap computations (e.g. overlap Jacobian J_{XY} = −u^{−3}) | ASSERTED (page MA; read at section level, not re-derived) | no | — |
| C36 | stable tangent relation T RP^n ⊕ 1 ≅ (n+1)γ_n + Whitney product law | ASSERTED (SI import I5) | no | — |
| C39 | the fixed minus sign in sgn J_{XY} = −ε_{XY} is a coboundary-level chart-order convention | ASSERTED (page CP; overlap computation not re-derived) | no | — |
| C41 | spin criterion (w₁ = w₂ = 0), w₂ stability under ⊕1, H*(RP^n;ℤ₂) ≅ ℤ₂[a_n]/(a_n^{n+1}) | ASSERTED (SI import I5) | no | — |
| C44 | explicit stable Clifford-lift audit with the corrected sign cocycle | ASSERTED (page CP; computation not reproduced here) | no | — |
| C45 | quaternion model Spin(3) ≅ S³; covering map Φ(q)(v) = qv q̄; covering-space theory | ASSERTED (SI import I6) | no | — |
| C51 | nonselection theorem: none of the nine structures (i)–(ix) selects a preferred lift sign or physical chirality | ASSERTED (page CP; component arguments proved, but the global negative claim rests on bookkeeping + the un-re-derived Book 0 naturality obstruction) | no | honestly kept at ASSERTED, not upgraded |
| C52 | four necessary conditions for any future chirality mechanism (NC1–NC4) | ASSERTED (forward-looking, page MA) | no | — |
| C53 | twelve definitions frozen (3.XII) | ASSERTED (definitions) | no | — |
| C55 | dependency graph acyclic, no retroactive use | ASSERTED (page MA; "acyclicity was not machine-checked") | no | the §§A–K order exhibited is acyclic by construction, but the book's own audit is recorded at its status |
| C56 | binary/two-sheeted objects do not reduce to one universal ℤ₂ | ASSERTED (bookkeeping synthesis; page CP) | no | survey over proved separations, not a theorem |

## CHECKED claims (8)

The book's verification runs (`~/workspace/r-theory-rewrite/validation/book3/verify_book3.py`,
67 checks, all passed, exit 0, no timeouts, run 2026-09-22) are cited,
not re-run here, per the proof-over-sampling rule.

| Claim | What it checks | Scope | Folded in? | Notes |
|---|---|---|---|---|
| C9 | dominance cycle: one primitive strictly largest per octant interior, cycle srx→cxp→crx→sxp (×2), min strict gap 3.531 at midpoints (B10, NC) | CHECKED | yes — already registered as row 51 (Book 3) | the analytic octant-by-octant argument was read on the page but not independently re-derived |
| C10 | cophase permutation P_c = (srx crx)(sxp cxp); C_dom² = P_c; C_dom order 4 (B46b/c, exact permutation runs) | CHECKED | no — permutation group arithmetic on labels, not a trig identity | — |
| C28 | reciprocal compatibility surface (1−σ_{XY}²)(1−σ_{YZ}²)(1−σ_{ZX}²) = 8σ_{XY}σ_{YZ}σ_{ZX} on P° (B44, NC, residual 5.684e-12) | PROVED-conditional (declared RP²-atlas import I3) | yes — registered as row 50 (Book 3); label dispute resolved 2026-09-26 | independent re-derivation 2026-09-26: with a=σ_{XY}, b=σ_{YZ}, c=σ_{ZX} (all >0 as values of f), C16's inverse u=(1−σ²)/(2σ) turns C27's u_{XY}u_{YZ}u_{ZX}=1 into (1−a²)(1−b²)(1−c²)/(8abc)=1 — exact algebra, division by 8abc valid |
| C31 | transition-sign Čech cocycle ζ_{ZY}·ζ_{YX} = ζ_{ZX} (B45, exact) | CHECKED | no — cocycle arithmetic; the w₁(γ)-identification is the ASSERTED import I4 | — |
| C32 | lift flip v(x+2π) = −v(x) (B48, NC, residual 5.829e-16) | CHECKED | no — not a trig identity | the bijectivity/nontriviality reasoning is PROVED modulo the declared imports I1/I3/I6 |
| C34 | monodromy test: four cophase FlatWave multipliers −1,−1,−1,−1 with product +1 around one 2π circuit, against the tautological lift's single −1 (B37, exact) | CHECKED | yes — already registered as row 46 (Book 3) | the type-separation half of C34 (character vs cohomology class, different kinds of object) is PROVED by inspection |
| C46 | Φ lands in SO(3): norm preservation, scalar-part vanishing, Φ(−q) = Φ(q), RᵀR = I, det = +1 (B47a–e, NC) | CHECKED | yes — already registered as row 47 (Book 3) | the half-angle flip q(θ+2π,n) = −q(θ,n) is PROVED modulo I6; surjectivity of Φ and exactness of ker = {±1} are ASSERTED (SI) |
| C47 | Rodrigues chart: ‖q₊(r)‖ = 1 (B39), collinear composition = tangent addition (B40, residual 6.079e-16) | CHECKED | yes — already registered as row 49 (Book 3) | lift-blindness r(−q) = r(q) is immediate from the formula; the ij = k convention is ASSERTED (I8) |

## Candidate trigonometric principles (25)

Genuine proved identities/lemmas about trigonometric functions, angles,
or circular measure, reported with full statements, domains, complete
proofs, scope, and source claims — including duplicates, for later dedup.
24 of the 25 are already in the Principles register as rows 28–51
(Book 3); one (C22) duplicates Book 0 P7 and is flagged. Euclid citation:
none — no Elements proposition is a premise of any principle below; all
rest on the declared analytic substrate (real analysis with sin/cos/tan,
linear algebra, declared imports named where conditional).

### 1. Quarter-turn shift identities (PROVED) — Book 3, C3; register row 28

**Statement.** For all real x: sin(x+π/2) = cos x; cos(x+π/2) = −sin x;
sin(x−π/2) = −cos x; cos(x−π/2) = sin x.
**Domain.** All real x.
**Proof.** The addition formulas (declared standard import):
sin(x+π/2) = sin x cos(π/2) + cos x sin(π/2) = cos x;
cos(x+π/2) = cos x cos(π/2) − sin x sin(π/2) = −sin x.
The −π/2 forms follow by the same formulas with −π/2. ∎
**Scope:** PROVED (from declared standard-analysis premises).

### 2. Directed quarter-turn has exact order 4 (PROVED) — Book 3, C1; register row 29

**Statement.** On 𝕋₂π = ℝ/2πℤ, τ_{π/2}⁴ = id, τ_{π/2}² = τ_π ≠ id,
τ_{π/2} ≠ id.
**Domain.** The phase circle 𝕋₂π.
**Proof.** Translations compose by addition: τ_a ∘ τ_b = τ_{a+b}.
Hence τ_{π/2}² = τ_π, τ_{π/2}⁴ = τ_{2π} = id on 𝕋₂π, and τ_π ≠ id since
it moves 0 to π ≢ 0 (mod 2π). ∎
**Scope:** PROVED.

### 3. Fold lemma: one involution of exact order 2 on 𝕋_π (PROVED) — Book 3, C4; register row 30

**Statement.** After the fold κ: 𝕋₂π → 𝕋_π, the two directed cophase
steps coincide as a single involution of exact order 2.
**Domain.** 𝕋_π = ℝ/πℤ.
**Proof.** On 𝕋_π, x + π/2 ≡ x − π/2 (mod π), so the two directions
coincide. Applying the map twice gives x + π ≡ x (mod π); applying it
once gives x + π/2 ≢ x (mod π) since π/2 ≢ 0 (mod π). Hence order
exactly 2. ∎
**Scope:** PROVED.

### 4. Eighth-turn has exact order 8 (PROVED) — Book 3, C8; register row 31

**Statement.** η = τ_{π/4} satisfies η⁸ = id with no smaller positive
power the identity, and permutes the eight octants O_j cyclically
(faithful action).
**Domain.** 𝕋₂π; octants O_j = (jπ/4, (j+1)π/4), j = 0,…,7.
**Proof.** 8·(π/4) = 2π ≡ 0 (mod 2π), and k·(π/4) ≡ 0 (mod 2π) requires
8 | k; hence order exactly 8. η(O_j) = O_{j+1 mod 8}, so the action is a
faithful cyclic permutation. ∎
**Scope:** PROVED.

### 5. Half-angle tangent is a bijection of the phase circle onto the projective line (PROVED) — Book 3, C12; register row 32

**Statement.** t = tan(x/2): 𝕋₂π → ℝ̂ = ℝ ∪ {∞} is bijective; the
circle point x = ±π maps to the single projective point ∞.
**Domain.** The phase circle 𝕋₂π.
**Proof.** On (−π, π) the map x ↦ tan(x/2) is continuous and strictly
increasing (declared analysis) from −∞ to +∞; the endpoint x = ±π (the
same point of 𝕋₂π) is sent to ∞. Strict monotonicity gives injectivity
on the circle; the limits give surjectivity onto ℝ̂. ∎
**Scope:** PROVED (from declared standard-analysis premises).

### 6. Directed cophase is Möbius of exact order 4 (PROVED) — Book 3, C13; register row 33

**Statement.** With Q₊(t) = (1+t)/(1−t), Q₋(t) = (t−1)/(1+t): directed
cophase x ↦ x ± π/2 acts as t ↦ Q_±(t); Q₋ ∘ Q₊ = id; Q₊²(t) = −1/t;
Q₊ has exact order 4 in PGL(2,ℝ); the marked orbit
0 → 1 → ∞ → −1 → 0 is the four cardinal phases 0, π/2, π, 3π/2.
**Domain.** t = tan(x/2) on 𝕋₂π; projective values allowed.
**Proof.** By the tan addition formula,
tan((x+π/2)/2) = tan(x/2 + π/4) = (tan(x/2)+1)/(1−tan(x/2)) = Q₊(t),
and similarly tan(x/2 − π/4) = (t−1)/(1+t) = Q₋(t). Direct algebra:
Q₋(Q₊(t)) = t; Q₊(Q₊(t)) = (1+(1+t)/(1−t))/(1−(1+t)/(1−t)) = −1/t;
iterating, Q₊⁴(t) = t with Q₊²(t) = −1/t ≠ t (e.g. at t = 0: ∞ ≠ 0), so
order exactly 4 in PGL(2,ℝ). Orbit: Q₊(0) = 1, Q₊(1) = ∞ (projective),
Q₊(∞) = −1, Q₊(−1) = 0; via Principle 5 these are x = 0, π/2, π, 3π/2. ∎
**Scope:** PROVED (from declared standard-analysis premises).

### 7. Harmonic cross-ratio (PROVED) — Book 3, C14; register row 34

**Statement.** The ordered quadruple (0, ∞; 1, −1) has cross-ratio −1
(ordering matters).
**Domain.** The projective line ℝ̂.
**Proof.** With λ(z₁,z₂;z₃,z₄) = (z₃−z₁)(z₄−z₂)/((z₃−z₂)(z₄−z₁)),
substituting (0,∞;1,−1) and taking the projective limit at ∞ gives
λ = (1−0)(−1−∞)/((1−∞)(−1−0)) → −1. ∎
**Scope:** PROVED.

### 8. Determinant separates cophase from reflection (PROVED) — Book 3, C15; register row 35

**Statement.** With A₊ = [[1,1],[−1,1]] (so Q₊(t) = (t+1)/(−t+1)) and
R(t) = −t: det A₊ = +2 > 0 (orientation-preserving on RP¹) while the
reflection matrix diag(−1,1) has det −1 (orientation-reversing); scalar
reflection conjugates Q₊ to Q₋, R∘Q₊∘R = Q₋.
**Domain.** PGL(2,ℝ) action on RP¹.
**Proof.** det [[1,1],[−1,1]] = 1 + 1 = 2; det diag(−1,1) = −1.
Conjugation: −Q₊(−t) = −(1−t)/(1+t) = (t−1)/(1+t) = Q₋(t). ∎
**Scope:** PROVED.

### 9. Universal positive reciprocal transform (PROVED) — Book 3, C16; register row 36

**Statement.** f(u) = √(1+u²) − u is strictly positive, strictly
decreasing, a bijection ℝ → (0,∞) with inverse u = (1−s²)/(2s);
f(−u)·f(u) = 1; and f(u) = e^{−arsinh u}.
**Domain.** u ∈ ℝ; s ∈ (0,∞).
**Proof.** √(1+u²) > |u| ≥ u gives f(u) > 0. Derivative
f′(u) = u/√(1+u²) − 1 < 0 since u < √(1+u²); strictly decreasing,
continuous, limits +∞ at −∞ and 0⁺ at +∞ — hence a bijection
ℝ → (0,∞). Inverse: s = √(1+u²) − u ⇒ √(1+u²) = s + u ⇒
1 + u² = s² + 2su + u² ⇒ u = (1 − s²)/(2s), valid for s > 0.
Reciprocal: f(−u)·f(u) = (√(1+u²)+u)(√(1+u²)−u) = (1+u²) − u² = 1.
Exponential form: arsinh u = ln(u + √(1+u²)); then
e^{−arsinh u} = 1/(u + √(1+u²)) = (√(1+u²) − u)/((1+u²) − u²) = f(u). ∎
**Scope:** PROVED.

### 10. Unit threshold recovers the sign (PROVED) — Book 3, C17; register row 37

**Statement.** sgn(u) = sgn(1 − s²) where s = f(u).
**Domain.** u ∈ ℝ.
**Proof.** s = 1 ⟺ u = 0 by Principle 9's inverse
((1−s²)/(2s) = 0 ⟺ s = 1); f strictly decreasing (Principle 9) gives
u > 0 ⟺ s < 1 ⟺ 1 − s² > 0. ∎
**Scope:** PROVED.

### 11. One map generates the four canonical primitives (PROVED) — Book 3, C18; register row 38

**Statement.** sxp(x) = f(cot x), srx(x) = f(−cot x), crx(x) = f(tan x),
cxp(x) = f(−tan x), with logarithmic coordinates arsinh(cot x) =
ln srx = −ln sxp.
**Domain.** x with sin x ≠ 0 and cos x ≠ 0.
**Proof.** sxp(x) = |csc x| − cot x; with u = cot x,
f(u) = √(1+cot²x) − cot x = √((sin²x+cos²x)/sin²x) − cot x
     = |1/sin x| − cot x = |csc x| − cot x = sxp(x).
The other three are identical with tan/cot and signs. Logarithms: from
Principle 9's exponential form, ln f(u) = −arsinh u; hence
ln srx = ln f(−cot x) = arsinh(cot x) and
ln sxp = ln f(cot x) = −arsinh(cot x) = −ln srx, using f(−u) = 1/f(u). ∎
**Scope:** PROVED.

### 12. Threshold formulas (PROVED) — Book 3, C19; register row 39

**Statement.** sgn(1 − sxp²) = sgn(srx² − 1) (and the cxp/crx analogue).
**Domain.** x with sin x ≠ 0 and cos x ≠ 0.
**Proof.** From Principle 11, srx = 1/sxp; so
srx² − 1 = (1 − sxp²)/sxp², and sxp² > 0 gives equal signs. ∎
**Scope:** PROVED.

### 13. Unequal limits bar a single-valued global RP¹ coordinate (PROVED) — Book 3, C20; register row 40

**Statement.** lim_{u→+∞} f(u) = 0⁺ and lim_{u→−∞} f(u) = +∞; these
unequal limits bar a single-valued global RP¹ coordinate via f.
**Domain.** u ∈ ℝ.
**Proof.** The limits are Principle 9. A global RP¹ coordinate would
have to identify the two ends compatibly, but the reciprocal pair takes
distinct unequal limit values 0 and ∞ — no single-valued continuous
extension assigns one value to both ends. ∎
**Scope:** PROVED.

### 14. Cophase group preserves FlatWave's domain (PROVED) — Book 3, C21; register row 41

**Statement.** Γ_c = ⟨τ_{π/2}⟩ ≅ C4 preserves D = ℝ \ {kπ/2}.
**Domain.** The phase line minus the seams.
**Proof.** The seams are x = kπ/2; τ_{π/2} permutes them (k ↦ k+1), so
D is invariant; Principle 2 gives Γ_c ≅ C4. ∎
**Scope:** PROVED.

### 15. FlatWave reversal and invariance (PROVED — duplicative) — Book 3, C22; NOT folded (already Book 0 P7)

**Statement.** FlatWave(x ± π/2) = −FlatWave(x); FlatWave(x + π) =
FlatWave(x); the cophase orbit is ε → −ε → ε → −ε → ε.
**Domain.** D (seams x = kπ/2 excluded).
**Proof.** sin(2(x+π/2)) = sin(2x+π) = −sin(2x); sgn flips.
sin(2(x+π)) = sin(2x+2π) = sin(2x); invariant. Iterating the reversal
gives the orbit. ∎
**Scope:** PROVED — but already registered as Book 0 P7
(FW(x+π/2) = −FW(x), FW(x+π) = FW(x)); reported here for dedup, not a
new principle.

### 16. Cophase–FlatWave character (PROVED) — Book 3, C23; register row 42

**Statement.** χ_c(τ_{kπ/2}) = (−1)^k is a homomorphism Γ_c → {±1} with
FlatWave(g·x) = χ_c(g)·FlatWave(x); ker χ_c = {id, τ_π}; it factors
through C4/{0,2} ≅ C2.
**Domain.** Γ_c acting on D.
**Proof.** (−1)^{k+l} = (−1)^k(−1)^l gives the homomorphism;
Principle 15 is the equivariance; kernel = {τ_{kπ/2} : k even} =
{id, τ_π}; the quotient by the kernel is C2. ∎
**Scope:** PROVED.

### 17. Octant sign law (PROVED) — Book 3, C24; register row 43

**Statement.** FlatWave|_{O_j} = (−1)^{⌊j/2⌋}.
**Domain.** The eight octant interiors O_j.
**Proof.** On O_j, jπ/4 < x < (j+1)π/4, so jπ/2 < 2x < (j+1)π/2. The
sign of sin on successive half-π intervals: j = 0,1 → 2x ∈ (0,π),
sin > 0 = (−1)^0; j = 2,3 → 2x ∈ (π,2π), sin < 0 = (−1)^1;
j = 4,5 → (−1)^2 = +1; j = 6,7 → (−1)^3 = −1. ∎
**Scope:** PROVED.

### 18. FlatWave as a projective sign polynomial (PROVED) — Book 3, C25; register row 44

**Statement.** FlatWave(x) = sgn[t(1 − t²)] with t = tan(x/2);
cophase reverses and the half-turn preserves this sign polynomial.
**Domain.** D in the t-coordinate (t(1−t²) ≠ 0).
**Proof.** tan x = 2t/(1−t²) and sin 2x = 2 tan x/(1+tan²x); substituting
gives sin 2x = 4t(1−t²)/(1+t²)² (numerator (1−t²)²+4t² = (1+t²)²).
The prefactor 4/(1+t²)² > 0, so sgn(sin 2x) = sgn(t(1−t²)).
Cophase sends t ↦ Q_±(t); a direct sign check gives
sgn(Q₊(t)(1−Q₊(t)²)) = −sgn(t(1−t²)) (reversal), while the half-turn
t ↦ −1/t preserves it. ∎
**Scope:** PROVED.

### 19. FlatWave versus the tautological sign (PROVED) — Book 3, C33; register row 45

**Statement.** FlatWave = sgn(t)·sgn(1−t²) = (ρ*ζ_{YX})·sgn(1−t²),
agreeing with the tautological sign sgn(t) exactly on |t| < 1 and
differing on |t| > 1.
**Domain.** The half-angle coordinate t = tan(x/2).
**Proof.** Principle 18 gives FlatWave = sgn(t(1−t²)) =
sgn(t)·sgn(1−t²) (exact sign algebra; no zero factors on D). The page's
computed pullback gives ρ*ζ_{YX} = sgn(t). The agreement/disagreement
regions are immediate: 1−t² > 0 exactly on |t| < 1. ∎
**Scope:** PROVED.

### 20. Half-angle flip of the quaternion lift (PROVED 2026-09-26) — Book 3, C46; register row 47

**Statement.** q(θ+2π,n) = −q(θ,n) for q(θ,n) = cos(θ/2) + sin(θ/2)n.
**Domain.** θ ∈ ℝ; n a unit pure quaternion.
**Proof.** With the declared quaternion model (import I6),
q(θ+2π,n) = cos(θ/2+π) + sin(θ/2+π)n = −q(θ,n). ∎
**Scope:** PROVED-conditional (declared quaternion-model import I6 named).
**2026-09-26 upgrade:** I6 not needed — from the definition of q alone,
q(θ+2π,n) = cos(θ/2+π) + sin(θ/2+π)n = −cos(θ/2) − sin(θ/2)n = −q(θ,n)
(M0 shift identities); no property of n used. Scope now PROVED. See
cumulative_trig_proof.md P33 addendum.

### 21. Rodrigues bridge, chart-qualified (PROVED-conditional) — Book 3, C48; register row 48

**Statement.** On 0 < θ < π: ‖r‖ = tan(θ/2) = sxp(θ); the FlatWave seam
θ = π/2 (ρ = 1) is regular in the Rodrigues chart (q₀ = 1/√2 ≠ 0); the
chart boundary is q₀ = 0 at θ → π (ρ → ∞).
**Domain.** 0 < θ < π.
**Proof.** From the axis-angle lift (import I6), q₀ = cos(θ/2),
q_V = sin(θ/2)n, so ‖r‖ = tan(θ/2). From Principle 11, sxp(θ) =
f(cot θ); for θ ∈ (0,π), |csc θ| = csc θ, so
sxp(θ) = csc θ − cot θ = (1 − cos θ)/sin θ = tan(θ/2) (half-angle
identity). Hence ‖r‖ = tan(θ/2) = sxp(θ). At θ = π/2: ρ = tan(π/4) = 1,
q₀ = cos(π/4) = 1/√2 ≠ 0 — seam regular. At θ → π: q₀ → 0, ρ → ∞ —
chart boundary. ∎
**Scope:** PROVED-conditional (declared quaternion-model import I6 named).
**2026-09-26 upgrade:** I6's unproven content (Spin(3) ≅ S³, covering map,
covering theory) not needed. With admitted definitions (quaternion norm,
unit n, Rodrigues vector r = q_V/q₀ on q₀ > 0): on (0,π),
‖q_V‖ = sin(θ/2), q₀ = cos(θ/2), so ‖r‖ = tan(θ/2) = sxp(θ) by P17.
Scope now PROVED. See cumulative_trig_proof.md P34 addendum.

### 22. Dominance cycle (CHECKED) — Book 3, C9; register row 51

**Statement.** On each octant interior exactly one canonical primitive
is strictly largest, cycling srx → cxp → crx → sxp (×2); the winner at
each octant midpoint has a strict positive gap to the runner-up.
**Domain.** The eight octant interiors.
**Proof/measurement.** Completed numerical run: verify_book3.py B10,
"winner cycle srx>cxp>crx>sxp (x2), min strict gap = 3.531" — status OK
[NC], run 2026-09-22. No analytic proof was re-derived in this campaign.
∎
**Scope:** CHECKED.

### 23. Cophase monodromy product (CHECKED) — Book 3, C34; register row 46

**Statement.** The four cophase FlatWave multipliers around one 2π
circuit are −1,−1,−1,−1 with product +1, against the tautological
lift's single −1.
**Domain.** One 2π cophase circuit.
**Proof/measurement.** Completed run: verify_book3.py B37 ("exact",
run 2026-09-22). ∎
**Scope:** CHECKED.

### 24. Collinear Rodrigues composition (CHECKED) — Book 3, C47; register row 49

**Statement.** Collinear Rodrigues composition a⊕b = (a+b+a×b)/(1−a·b)
reduces to the tangent addition formula.
**Domain.** Collinear Rodrigues vectors.
**Proof/measurement.** Completed run: verify_book3.py B40 (residual
6.079e-16, run 2026-09-22). ∎
**Scope:** CHECKED.

### 25. Reciprocal compatibility surface (PROVED-conditional; label dispute resolved 2026-09-26) — Book 3, C28; register row 50

**Statement.** On P°: (1−σ_{XY}²)(1−σ_{YZ}²)(1−σ_{ZX}²) =
8σ_{XY}σ_{YZ}σ_{ZX} with σ_{IJ} = f(u_{IJ}).
**Domain.** P° = {XYZ ≠ 0} in the declared RP² affine atlas.
**Proof.** Substitute σ = f(u) with inverse u = (1−σ²)/(2σ)
(Principle 9) into the cyclic-ratio identity u_{XY}u_{YZ}u_{ZX} = 1
(C27) and clear denominators — exact algebra. ∎
**Scope:** PROVED-conditional (declared RP²-atlas import I3 named).
**Discrepancy note — RESOLVED 2026-09-26:** the book file's CHECKED label
(the witnessed B44 float run) vs the register's PROVED-conditional (I3).
Independent re-derivation 2026-09-26 confirms the exact substitution is
complete: C16's inverse u = (1−σ²)/(2σ) (verified) turns C27's
u_{XY}u_{YZ}u_{ZX} = 1 (verified from the declared atlas I3) into
(1−a²)(1−b²)(1−c²)/(8abc) = 1 with a,b,c > 0 — exact algebra. The row
verdict is now PROVED-conditional (declared RP²-atlas import I3); the
B44 numeric run stands as cited corroboration, not the proof.

## Claims not made into principles (with reasons)

- **C2** — relation-logic properties of cophase (symmetric/irreflexive/
  not transitive); no trig content.
- **C5** — linear-algebraic det-sign classes; not a trig identity
  (with the noted wording caveat on reference-dependence of the ±1 labels).
- **C6** — orientation-preservation of translations; analysis, not an identity.
- **C10** — permutation-group arithmetic on four primitive labels (CHECKED);
  group theory, not a trig identity.
- **C11** — ASSERTED (π-periodicity inheritance, page MA).
- **C27** — cyclic-ratio identity; ratio algebra conditional on the declared
  projective-atlas import I3, not a trig identity.
- **C31** — Čech cocycle arithmetic (CHECKED); the w₁-identification is the
  ASSERTED import I4; cohomology, not trig.
- **C32** — half-angle bijectivity + lift flip (CHECKED); not a trig identity.
- **C35** — bundle-class conclusion conditional on import I4; not a trig identity.
- **C37, C38, C40, C42, C43** — Stiefel–Whitney topology of RP^n; not trig.
- **C49** — covering theory (no continuous section of the double cover);
  not a trig identity.
- **C50** — deck-blindness and quotient effects; not a trig identity.
- **C7, C26, C29, C30, C36, C39, C41, C44, C45, C51, C52, C53, C55, C56**
  — ASSERTED (declarations, imports, interpretations, bookkeeping, scope rules).
- **C54, C57, zero counts** — PROVED bookkeeping/meta, not trig principles.
- **C22** — PROVED but duplicative of Book 0 P7; listed above as candidate 15
  for the dedup pass.

## Counts

- Evaluated: **58** (57 claims C1–C57 + 1 zero-counts bookkeeping row):
  **PROVED 35** · **CHECKED 7** · **ASSERTED 15** · **INCOMPLETE 0**.
  (2026-09-26: C28 CHECKED → PROVED-conditional (I3) after independent
  re-derivation; the B44 run stands as corroboration.)
- Recount audit: PROVED — C1, C2, C3, C4, C5, C6, C8, C12, C13, C14, C15,
  C16, C17, C18, C19, C20, C21, C22, C23, C24, C25, C27, C28, C33, C35,
  C37, C38, C40, C42, C43, C48, C49, C50, C54, C57 + zero-counts row = 35.
  CHECKED — C9, C10, C31, C32, C34, C46, C47 = 7.
  ASSERTED — C7, C11, C26, C29, C30, C36, C39, C41, C44, C45, C51, C52,
  C53, C55, C56 = 15. Total 57 + 1 = 58. INCOMPLETE: none — no timeouts,
  no failures, nothing unfinished.
- Candidate principles reported: **25** (18 PROVED, 3 PROVED-conditional,
  4 CHECKED). 24 already registered as rows 28–51 (Book 3); 1 (C22)
  duplicates Book 0 P7.

status: complete
