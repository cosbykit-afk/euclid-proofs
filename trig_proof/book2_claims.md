# Book 2 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book2_proof.md` (claim inventory
P1–P74, A1–A11, C1–C12) and rewrite page
`~/workspace/r-theory-rewrite/book2/index.html` (*Book 2 — Canonical
R-Operator Calculus*; its "Established (abridged)" principal theorems are
exactly this inventory — nothing extra, nothing missing). Evaluated
2026-09-22.

**Verification method.** All 74 proofs read in full. The load-bearing
algebraic identities were independently re-derived and check out exactly
(P1 reciprocity; P6 half-angle chart; P12–P13 stereographic/double-angle;
P14–P16 symmetry actions; P21–P23 magnitude/same-phase forms; P28 product;
P32 FlatWave collapse; P41–P45 Möbius reduction and fixed points; P49
extraction; P52 harmonic system; P54 fibers; P58–P61
derivative/antiderivative forms). The analysis/limit arguments (P7–P11,
P30, P33–P34, P38, P43, P50, P55, P62–P64, P66–P67) were checked by reading
for domain errors and circularity — none found. The book page's reported
numerical re-verification (129 assertions, all passing, no timeouts) is
cited as CHECKED, not re-run, per the proof-over-sampling rule.

**Scope labels:** PROVED (exact mathematics, complete), CHECKED
(completed numeric run), ASSERTED (manuscript claim/assumption/convention),
INCOMPLETE (failed, timed out, or unfinished — none here).

## PROVED claims (74)

| Claim | Restatement | Verdict | Scope | Folded in? | Notes |
|---|---|---|---|---|---|
| P1 | sxp = 1/srx, crx = 1/cxp on D (reciprocity) | proof verified (re-derived: csc²−cot² = 1) | PROVED | no — already registered as Book 0 P1 | trig core is the registered reciprocal identity |
| P2 | strict positivity of all four members | proof verified (re-derived: |csc| > |cot|) | PROVED | no — already registered as Book 0 P2 | — |
| P3 | regular value 1 at opposite-channel seams | proof verified | PROVED | no — definitional audit point, no new identity | — |
| P4 | conjugate sum/difference recovery of 2|csc|, 2cot, 2|sec|, 2tan | proof verified | PROVED | no — algebra from P1 | — |
| P5 | global form must keep |·|; chart-local droppings not global | proof verified (counterexample at 5π/4 checks) | PROVED | no — definitional audit point | — |
| P6 | principal half-angle chart: srx = cot(x/2), sxp = tan(x/2), cxp = tan(π/4+x/2), crx = tan(π/4−x/2) | proof verified (re-derived, incl. cross-multiplied identity) | PROVED | **yes — P17** | genuine half-angle trig principle |
| P7 | maximal channel coordinates; bijection of each component onto (0,∞) | proof verified by reading (monotonicity) | PROVED | no — analysis (monotonicity), not an identity | — |
| P8 | common-domain transport; two chart types selected by ε | proof verified by reading | PROVED | no — book machinery (chart transport), not an identity | — |
| P9 | range law: z > 1, w > 1 ⇔ ε = +1; 0 < z,w < 1 ⇔ ε = −1 | proof verified by reading | PROVED | no — reads the branch sign from range; monotonicity analysis | — |
| P10 | midpoint values √2 ± 1 | proof verified | PROVED | **yes — P20** | exact octant values tan/cot(π/8) |
| P11 | octant crossing order | proof verified by reading (strict decrease of cot) | PROVED | no — monotonicity, not an identity | — |
| P12 | stereographic recovery of (sin x, cos x) from z plus half-turn label | proof verified (re-derived) | PROVED | **yes — P18** | Weierstrass parametrization |
| P13 | rational double-angle formulas from z; branch sign from unit threshold | proof verified (re-derived) | PROVED | **yes — P19** | rational double-angle trig principle |
| P14 | phase reflection is reciprocal inversion; unit threshold the fixed value | proof verified (re-derived: cot odd, |csc| even) | PROVED | no — operator-level; parity identities are M0 background | — |
| P15 | quarter-turn action; induced quarter-turn has order two | proof verified (re-derived; uses π-periodicity P18 — same theorem block, no cycle) | PROVED | no — operator-level; shift identities are M0 background | — |
| P16 | complementary-reflection action | proof verified (re-derived) | PROVED | no — operator-level; cofunction identities are M0 background | — |
| P17 | quartet is one orbit; induced permutation group is the Klein four V₄ | proof verified (re-derived: three involutions, transitive) | PROVED | no — group theory on operators, not trig | — |
| P18 | half-turn invariance, descent to 𝕋_π; no half-turn-branch recovery from z | proof verified (re-derived) | PROVED | no — π-periodicity already registered as Book 0 P3(c) | — |
| P19 | ε transport laws: two symmetries reverse, two preserve the branch sector | proof verified by reading (sum-formula sign rules) | PROVED | no — sign rules from M0 parity/shift formulas | — |
| P20 | ι_d exchanges (urx, uxp); retired reversed sign is wrong | proof verified | PROVED | no — sign-lock bookkeeping | — |
| P21 | exact UNA magnitude forms (ε+a−b)/(ab) | proof verified (re-derived unified, no quadrant split) | PROVED | no — book-operator algebra, not a general trig identity | used in verification of P28 |
| P22 | common UNA sign sgn(urx) = sgn(uxp) = ε; nonvanishing on D | proof verified (re-derived: |a−b| = 1 ⟺ seam) | PROVED | no — book architecture (inequality), not an identity | — |
| P23 | rational same-phase forms urx = (zw−1)/w, uxp = (zw−1)/z; UNA ratio theorem | proof verified (re-derived) | PROVED | no — operator algebra via P1 | — |
| P24 | reversed sign destroys common-sign architecture; π/4 checksum | proof verified (values check: urx = uxp = 2) | PROVED | no — bookkeeping + M0 exact values at a point | — |
| P25 | double-angle closure urx + uxp = 4/sin 2x | proof verified (via Seed; A = cxp, B = srx) | PROVED | no — P0 (the Seed) itself in book notation | — |
| P26 | retired-sign checksum: reversed sign would give 2|csc x| − 2|sec x| | proof verified | PROVED | no — bookkeeping/negative check | — |
| P27 | half-angle-generator form (z²+1)²/[z(z²−1)] | proof verified (P25 + P13 substitution) | PROVED | no — reformulation of P0 via registered P19 | — |
| P28 | unsigned companion urx·uxp = 4/|sin 2x| > 0 | proof verified (re-derived: (ε+a−b)(ε+b−a) = 2ab) | PROVED | no — already registered as Book 0 P8 | — |
| P29 | sign–magnitude relation |urx+uxp| = urx·uxp | proof verified | PROVED | no — corollary of P0 + Book 0 P8 | — |
| P30 | divergence toward every common seam; reciprocal closures vanish | proof verified by reading (one-sided limits) | PROVED | no — limit analysis, not an identity | — |
| P31 | rational Saw forms; FlatWave = (z+w)/(zw−1) | proof verified | PROVED | no — operator algebra via P23 | — |
| P32 | Binary Character Theorem: FlatWave = ε ∈ {−1,+1} | proof verified (re-derived: quotient of signed by unsigned closure) | PROVED | no — already registered as Book 0 P6 | — |
| P33 | FlatWave² = 1; quadrant character (−1)^k; flat per quadrant; period π | proof verified by reading | PROVED | no — already registered as Book 0 P6–P7 | — |
| P34 | exact boundedness: |saw_r|, |saw_x| < 1 on D | proof verified by reading (V₄ transport) | PROVED | no — inequality, not an identity | — |
| P35 | Saw product saw_r·saw_x = |sin 2x|/4 | proof verified | PROVED | no — reciprocal of registered Book 0 P8 | — |
| P36 | signed Saw partition of ε; sum+product determine unordered Saw pair | proof verified | PROVED | no — sum/product algebra, no new trig content | — |
| P37 | FlatWave carries the nontrivial 1-D sign character χ_F of V₄ | proof verified | PROVED | no — representation theory of the book's group | — |
| P38 | opposite one-sided limits ±1 at every common seam; no seam value | proof verified by reading | PROVED | no — limit analysis | — |
| P39 | same-phase cross-family equation z + w = ε(zw−1) | proof verified | PROVED | no — algebraic form of registered Book 0 P6 | — |
| P40 | denominator nonvanishing: εz − 1 ≠ 0 on D | proof verified (range law P9) | PROVED | no — nonvanishing lemma | — |
| P41 | same-phase Möbius reduction w = M_ε(z); reciprocal companion | proof verified (re-derived) | PROVED | no — operator map, not a trig identity | — |
| P42 | involution M_ε(M_ε(z)) = z | proof verified (re-derived: 2z/2) | PROVED | no — fractional-linear algebra | — |
| P43 | branch preservation with strict order reversal | proof verified by reading (derivatives −2/(z−1)², −2/(1+z)²) | PROVED | no — analysis of the Möbius map | — |
| P44 | involution is the z-image of complementary reflection | proof verified | PROVED | no — book architecture; cofunction core is M0 | — |
| P45 | unique positive fixed points √2+1, √2−1; equality with midpoint values | proof verified (re-derived: z²−2z−1 = 0, z²+2z−1 = 0) | PROVED | **yes — P20** | exact values; the fixed-point equations are Möbius algebra |
| P46 | branch selection is internal: FlatWave a derived readout | proof verified | PROVED | no — book architecture (no second generator) | — |
| P47 | one nonconstant generator per open quadrant reconstructs the system | proof verified | PROVED | no — book theorem, not an identity | — |
| P48 | one generator does not recover the discrete half-turn label | proof verified (follows P18) | PROVED | no — negative result | — |
| P49 | harmonic extraction H_D = sin 2x/4; 0 < |H_D| ≤ 1/4, max at midpoints | proof verified (re-derived) | PROVED | no — H = sin 2x/4 already registered as Book 0 P9; extremal values are M0 | — |
| P50 | smooth extension to ℝ; uniqueness (D dense) | proof verified by reading (S5 dense-set argument) | PROVED | no — analysis (continuous extension) | — |
| P51 | seam values H(b_k) = 0 belong to H alone; no regularization of raw operators | proof verified by reading | PROVED | no — extension bookkeeping | — |
| P52 | V = H′, system H′ = V, V′ = −4H; H″ + 4H = 0 | proof verified (re-derived) | PROVED | **yes — P21** | harmonic oscillator law |
| P53 | carrier ellipse v² + 4h² = 1/4; unit circle U² + W² = 1; constant phase speed | proof verified (re-derived) | PROVED | no — already registered as Book 0 P9 | — |
| P54 | carrier map F(x) = (H,V): smooth, π-periodic, exact fibers mod π | proof verified (re-derived fiber argument) | PROVED | no — analysis + M0 periodicity | — |
| P55 | seam classifier by V; transverse H = 0 crossing | proof verified by reading | PROVED | no — pointwise values, not an identity | — |
| P56 | FlatWave = sgn(H) on D; three levels of double-angle information | proof verified | PROVED | no — already registered as Book 0 P6 | — |
| P57 | carrier coordinates from z; seam-safe carrier data | proof verified (re-derived: (z⁴−6z²+1)/(z²+1)²) | PROVED | **yes — P22** | rational cot double-angle forms; rest is book machinery |
| P58 | envelope derivative forms srx′ = −srx|csc x|, etc. | proof verified (re-derived) | PROVED | no — lemma step of registered Book 0 P5 | — |
| P59 | autonomous Riccati pairs; exact monotonicity on maximal components | proof verified (re-derived: −(1+srx²)/2) | PROVED | no — already registered as Book 0 P5 | — |
| P60 | arctangent linearization, slopes ±1/2; phase quadratures | proof verified (re-derived) | PROVED | **yes — P24** | arctan linearization |
| P61 | logarithmic antiderivatives | proof verified (re-derived by differentiation) | PROVED | **yes — P23** | log antiderivatives |
| P62 | first-order zero–pole seam asymptotics; reciprocal zero–pole exchange | proof verified by reading | PROVED | no — asymptotic analysis, not an identity | — |
| P63 | logarithmic divergence on the pole side; integrable/nonintegrable exchange | proof verified by reading | PROVED | no — integral asymptotics | — |
| P64 | exact positive Riccati branches; finite-interval pole intrinsic to the chart | proof verified by reading | PROVED | no — ODE chart analysis | — |
| P65 | differential closure needs no second continuous generator | proof verified | PROVED | no — book theorem (closure) | — |
| P66 | named boundary traces at sine-zero and cosine-zero seams | proof verified by reading | PROVED | no — limit atlas | — |
| P67 | unified FlatWave/carrier seam law | proof verified by reading | PROVED | no — limit/smoothness statement | — |
| P68 | complex carrier Z_car = e^{2ix}; unit modulus; Z′ = 2iZ | proof verified | PROVED | no — Euler formula is M0; trig core already registered (Book 0 P9) | — |
| P69 | symmetry laws; phasor fiber theorem (exact fibers mod π) | proof verified by reading | PROVED | no — transport of P68 + analysis | — |
| P70 | complex seam contrast; complex notation regularizes nothing | proof verified | PROVED | no — architecture audit | — |
| P71 | no circular dependency in the proof chain | proof verified by reading (DAG check) | PROVED | no — meta | — |
| P72 | domain ledger: D used consistently; no silent seam regularization | proof verified by reading | PROVED | no — meta | — |
| P73 | three-climax synthesis | proof verified | PROVED | no — meta | — |
| P74 | zero new mathematical axioms in this file's construction | proof verified by reading | PROVED | no — meta | — |

## ASSERTED claims (11)

| Claim | Restatement | Scope | Folded in? | Notes |
|---|---|---|---|---|
| A1 | one-sided boundary convention | ASSERTED (convention) | no | convention, not mathematics |
| A2 | non-scope declarations are stipulated boundaries | ASSERTED (stipulation) | no | — |
| A3 | no physical seam law is inferred | ASSERTED (non-scope declaration) | no | — |
| A4 | retention decisions for Ψ_U, Z_car | ASSERTED (audit decision) | no | — |
| A5 | no quantum interpretation is admitted | ASSERTED (non-scope declaration) | no | — |
| A6 | the Wolfram audit changes no theorem status | ASSERTED (audit assertion) | no | — |
| A7 | closure certification | ASSERTED (bookkeeping verdict) | no | — |
| A8 | negative closure: 12 things not established (manuscript-wide) | ASSERTED (manuscript claim) | no | — |
| A9 | one-generator closure is task-relative | ASSERTED (stipulation) | no | — |
| A10 | Book 1's C7 rule, inherited | ASSERTED (cited) | no | cited, no Book 1 proof file in this batch |
| A11 | definitions are not axioms | ASSERTED (methodological stance) | no | — |

## CHECKED claims (12)

The book page reports its own completed validation run
(`validation/book2/verify_book2.py`, V1–V40: 129 assertions — 116 CP,
12 NC, 1 ST — all passing, no timeouts, on seam-avoiding grids). Per the
proof-over-sampling rule these were **not re-run here**; they are cited,
not folded as principles (a numerical check of a proved identity is not a
new theorem).

| Claim | What it checks | Scope | Folded in? |
|---|---|---|---|
| C1 | reciprocal conjugacy srx·sxp = cxp·crx = 1 (~3.6e-11) | CHECKED | no — checks proved P1 |
| C2 | double-angle sum (5.0e-16 rel.) | CHECKED | no — checks proved P25/P0 |
| C3 | double-angle product (6.5e-14 rel.) | CHECKED | no — checks proved P28 |
| C4 | sign–magnitude (6.5e-14 rel.) | CHECKED | no — checks proved P29 |
| C5 | FlatWave collapse FlatWave² = 1 (~2.4e-13) | CHECKED | no — checks proved P32 |
| C6 | FlatWave = sgn(sin 2x) (~2.4e-13) | CHECKED | no — checks proved P32 |
| C7 | Möbius involution (~3.6e-15) | CHECKED | no — checks proved P42 |
| C8 | branch preservation (~3.6e-15) | CHECKED | no — checks proved P43 |
| C9 | fixed points (~3.6e-15) | CHECKED | no — checks proved P45 |
| C10 | same-phase reduction agreement (~7.3e-14) | CHECKED | no — checks proved P41 |
| C11 | carrier ellipse and unit circle (~2.3e-16); harmonic system by finite differences (~8.8e-9) | CHECKED | no — checks proved P52–P53 |
| C12 | harmonic extraction through the seams (~7.1e-17) | CHECKED | no — checks proved P49 |

## Counts

- Evaluated: **97** (74 PROVED, 12 CHECKED, 11 ASSERTED, 0 INCOMPLETE)
- Folded into the cumulative proof: **8** (P17–P24), all PROVED
- Not folded: **89** — 13 already registered (P0 / Book 0 P1–P9), 53
  evaluated with no new trigonometric content (standard background, book
  machinery, analysis/limits, meta), 11 asserted, 12 numerical checks

status: complete
