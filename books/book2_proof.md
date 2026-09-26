# Book 2 — Euclid-style extension proofs
## R Theory rewrite, Book 2: Canonical R-Operator Calculus

**Status of this file.** A dependency-ordered recasting of the load-bearing claims of
`~/workspace/r-theory-rewrite/book2/index.html` (read in full 2026-09-22).
Every claim carries a scope label: **PROVED** (exact mathematics, complete here),
**CHECKED** (a completed numerical run, cited), **ASSERTED** (manuscript claim,
convention, or audit assertion — named, not proved), **INCOMPLETE** (failed, timed
out, or unfinished — none here).

**Established material cited without reproof.**
- *Seed theorem* (Kit's double-angle secant/cosecant identity, PROVED):
  `~/workspace/euclid_work/books/seed_double_angle.md`. Cited as **Seed**.
- *Euclid's Elements*: inventoried in `~/workspace/euclid_work/ledger/book1_ledger.md`
  through `book13_ledger.md`. **No proposition of the Elements is invoked anywhere in
  this file** (see §8, the No-Euclid-wholesale boundary). The algebraic steps use the
  ordinary field axioms of ℝ, which belong to the declared substrate below, not to a
  wholesale inheritance of Book 2's geometric algebra.
- No earlier book proof files exist in this campaign batch; each book is independent.
  One cross-book citation is taken as ASSERTED: Book 1's rule C7 (extension does not
  regularize raw operators), cited where the book page invokes it.

**Method.** Euclid: definitions first, dependency order, nothing used before it is
proved. Ptolemy: compute, don't assume — every number earned. Polya: understand,
plan, carry out, look back. Per the standing rule, no numerical sampling is run on
top of complete analytic proofs; computation is cited only where the book page
reports its own completed checks.

---

## 1. Declared substrate (S) — standard imports, not axioms

The following are *declared* as the working substrate. They are imported standard
results, explicitly not derived from the Elements here (cf. §8):

- **S1.** ℝ as a complete ordered field; |·| the real absolute value.
- **S2.** Real functions sin, cos with sin²x + cos²x = 1; tan = sin/cos, cot = cos/sin,
  sec = 1/cos, csc = 1/sin on their natural domains.
- **S3.** Standard differential calculus: derivatives of sin, cos, tan, cot, sec, csc,
  arctan, ln; chain rule; the |·|-chain rule on each interval where the inner function
  keeps its sign; Euler's formula e^{2ix} = cos 2x + i sin 2x.
- **S4.** Standard trig identities: sin 2x = 2 sin x cos x, cos 2x formulas,
  half-angle forms (1±cos x)/sin x = cot(x/2) / tan(x/2) where defined,
  tan(π/4 ± x/2) addition forms, the exact value tan(π/8) = √2 − 1
  (hence cot(π/8) = √2 + 1), monotonicity of cot on (0, π) and of tan on (−π/2, π/2).
- **S5.** Topological facts: {kπ/2 : k ∈ ℤ} is closed and nowhere dense, so its
  complement D is dense in ℝ; a continuous function agreeing with another on a dense
  set is unique.

None of S1–S5 is a *new* axiom of the extension; they are the declared background
the extension is explicit about (the book's own certification: 0 new axioms).

## 2. Definitions (D) — naming is an act, not a theorem

- **D0.** D_s = {x : sin x ≠ 0}, D_c = {x : cos x ≠ 0}, D = D_s ∩ D_c
  (the common domain; "the seams" are ℝ ∖ D).
- **D1.** srx = |csc x| + cot x, sxp = |csc x| − cot x on D_s;
  cxp = |sec x| + tan x, crx = |sec x| − tan x on D_c.
  𝒫 = (srx, sxp, cxp, crx) on D. z = srx, w = cxp.
- **D2.** urx = srx − crx, uxp = cxp − sxp on D. **Constitutional Rule 2.IV.R1**
  locks this order: the reversed transcription sxp − cxp = −uxp is retired, not an
  alternate convention.
- **D3.** saw_r = 1/urx, saw_x = 1/uxp on D (well-defined once nonvanishing is proved,
  P24); FlatWave = saw_r + saw_x.
- **D4.** ε(x) = sgn(sin 2x) on D; the *branch sign*.
- **D5.** M_ε(z) = (z + ε)/(εz − 1), the branch Möbius map, on I_+ = (1, ∞) for ε = +1
  and I_− = (0, 1) for ε = −1 (well-defined once P43 is proved).
- **D6.** H_D = 1/(urx + uxp) on D; H(x) = sin 2x/4 on ℝ; V(x) = H′(x) = cos 2x/2;
  U = 4H = sin 2x, W = 2V = cos 2x.
- **D7.** Ψ_U = urx + i·uxp (optional diagnostic, domain D);
  Z_car = 2V + i4H = cos 2x + i sin 2x (optional complex carrier).

Quadrant notation: Q_k = (kπ/2, (k+1)π/2), k ∈ ℤ; open quadrants. Midpoints
m_k = π/4 + kπ/2. Phase maps: ι_r(x) = −x (phase reflection),
ι_+(x) = x + π/2 (quarter-turn shift), ι_d(x) = π/2 − x (complementary reflection).

---

## 3. Claim inventory with scope labels

| ID | Book locus | Claim | Scope |
|---|---|---|---|
| P1 | 2.I.T1,T2 | sxp = 1/srx, crx = 1/cxp on D | PROVED |
| P2 | 2.I.T3 | Strict positivity of all four members on their channel domains | PROVED |
| P3 | 2.I | At opposite-channel seams the regular pair takes the value 1 | PROVED |
| P4 | 2.I.T4 | Conjugate sum/difference recovery of 2|csc x|, 2cot x, 2|sec x|, 2tan x | PROVED |
| P5 | 2.I.T5,C6 | The global form must keep |·|; chart-local droppings are not global | PROVED |
| P6 | 2.II.T1,T2 | Principal half-angle chart: srx = cot(x/2), sxp = tan(x/2), cxp = tan(π/4+x/2), crx = tan(π/4−x/2) | PROVED |
| P7 | 2.II.T3–T6 | Maximal channel coordinates; bijection of each component onto (0,∞) | PROVED |
| P8 | 2.II.T7,T8,C3 | Common-domain transport; two chart types selected by ε | PROVED |
| P9 | 2.II.T9,C4 | Range law: z > 1 and w > 1 ⇔ ε = +1; 0 < z,w < 1 ⇔ ε = −1 | PROVED |
| P10 | 2.II.T10 | Midpoint values √2 ± 1 | PROVED |
| P11 | 2.II.T11 | Octant crossing order | PROVED |
| P12 | 2.II.T12,C5,C6 | Stereographic recovery of (sin x, cos x) from z plus one half-turn label | PROVED |
| P13 | 2.II.T13,T14,C8 | Rational double-angle formulas from z; branch sign from the unit threshold | PROVED |
| P14 | 2.III.T1,C1,C2 | Phase reflection is reciprocal inversion; unit threshold the fixed value | PROVED |
| P15 | 2.III.T2,T4 | Quarter-turn action; induced quarter-turn has order two on the representation | PROVED |
| P16 | 2.III.T5 | Complementary-reflection action | PROVED |
| P17 | 2.III.T6,T7,C10 | The quartet is one orbit; induced permutation group is the Klein four V₄ | PROVED |
| P18 | 2.III.T3,C5,C6 | Half-turn invariance, descent to 𝕋_π; no half-turn-branch recovery from z | PROVED |
| P19 | 2.III.T8,C12 | ε transport laws: two symmetries reverse, two preserve the branch sector | PROVED |
| P20 | 2.IV.T1,C1 | ι_d exchanges (urx, uxp): the retired reversed sign is wrong | PROVED |
| P21 | 2.IV.T2,T3 | Exact UNA magnitude forms | PROVED |
| P22 | 2.IV.T4,C3,C4 | Common UNA sign sgn(urx) = sgn(uxp) = ε; nonvanishing on D | PROVED |
| P23 | 2.IV.T5,C5,C6 | Rational same-phase forms urx = (zw−1)/w, uxp = (zw−1)/z; UNA ratio theorem | PROVED |
| P24 | 2.IV.C8,C9 | Reversed sign destroys the common-sign architecture; π/4 checksum | PROVED |
| P25 | 2.V.T1 | Double-angle closure urx + uxp = 4/sin 2x | PROVED |
| P26 | 2.V.C1 | Retired-sign checksum: reversed sign would give 2|csc x| − 2|sec x| | PROVED |
| P27 | 2.V.T2,C2 | Half-angle-generator form (z²+1)²/[z(z²−1)] | PROVED |
| P28 | 2.V.T3,C3 | Unsigned companion urx·uxp = 4/|sin 2x| > 0 | PROVED |
| P29 | 2.V.T4,C5 | Sign–magnitude relation |urx+uxp| = urx·uxp | PROVED |
| P30 | 2.V.T7,C9 | Divergence toward every common seam; reciprocal closures vanish in extended form | PROVED |
| P31 | 2.VI.T1,C1 | Rational Saw forms; FlatWave = (z+w)/(zw−1) | PROVED |
| P32 | 2.VI.T2,T3 | Binary Character Theorem: FlatWave = ε ∈ {−1,+1} | PROVED |
| P33 | 2.VI.C2,C3,C4 | FlatWave² = 1; quadrant character (−1)^k; flat per quadrant; period π | PROVED |
| P34 | 2.VI.C7 | Exact boundedness: |saw_r|, |saw_x| < 1 on D | PROVED |
| P35 | 2.VI.T5 | Saw product saw_r·saw_x = |sin 2x|/4 | PROVED |
| P36 | 2.VI.T4,C8 | Signed Saw partition of ε; sum plus product determine the unordered Saw pair | PROVED |
| P37 | 2.VI.T7 | FlatWave carries the nontrivial 1-D sign character χ_F of V₄ | PROVED |
| P38 | 2.VI.T8 | Opposite one-sided limits ±1 at every common seam; no seam value | PROVED |
| P39 | 2.VI.T10 | Same-phase cross-family equation z + w = ε(zw − 1) | PROVED |
| P40 | 2.VII.L1,C1 | Denominator nonvanishing: εz − 1 ≠ 0 on D | PROVED |
| P41 | 2.VII.T1,C2,C3 | Same-phase Möbius reduction w = M_ε(z); reciprocal companion | PROVED |
| P42 | 2.VII.T2 | Involution M_ε(M_ε(z)) = z | PROVED |
| P43 | 2.VII.T3 | Branch preservation with strict order reversal | PROVED |
| P44 | 2.VII.T4,C4 | The involution is the z-image of complementary reflection | PROVED |
| P45 | 2.VII.T5,C5 | Unique positive fixed points √2+1, √2−1; equality with midpoint values | PROVED |
| P46 | 2.VII.T6,C6 | Branch selection is internal: FlatWave is a derived readout, not a second generator | PROVED |
| P47 | 2.VII.T7–T10,C8,C9 | One nonconstant generator per open quadrant reconstructs the named system | PROVED |
| P48 | 2.VII.C10 | One generator does not recover the discrete half-turn label | PROVED |
| P49 | 2.VIII.T1,C1 | Harmonic extraction H_D = sin 2x/4; 0 < |H_D| ≤ 1/4, max at midpoints | PROVED |
| P50 | 2.VIII.T2,T3 | Smooth extension to ℝ; uniqueness (D dense) | PROVED |
| P51 | 2.VIII.C3,N1 | Seam values H(b_k) = 0 belong to H alone; no regularization of raw operators | PROVED |
| P52 | 2.VIII.T4,T5,C4 | V = H′, system H′ = V, V′ = −4H; H″ + 4H = 0 in the phase coordinate | PROVED |
| P53 | 2.VIII.T6,C5,C6 | Carrier ellipse v² + 4h² = 1/4; unit circle U² + W² = 1; constant phase speed | PROVED |
| P54 | 2.VIII.T7,T8,C7 | Carrier map F(x) = (H,V): smooth, π-periodic, exact fibers mod π | PROVED |
| P55 | 2.VIII.T9,C9,C10 | Seam classifier by V; transverse H = 0 crossing | PROVED |
| P56 | 2.VIII.T10,C11,C12 | FlatWave = sgn(H) on D; three distinct levels of double-angle information | PROVED |
| P57 | 2.VIII.T11,T12 | Carrier coordinates from z; seam-safe carrier data | PROVED |
| P58 | 2.IX.T1 | Envelope derivative forms srx′ = −srx|csc x|, etc. | PROVED |
| P59 | 2.IX.T2–T4,C1,C2 | Autonomous Riccati pairs; exact monotonicity on maximal components | PROVED |
| P60 | 2.IX.T5,C3,C4 | Arctangent linearization, slopes ±1/2; phase quadratures | PROVED |
| P61 | 2.IX.T6,C5 | Logarithmic antiderivatives | PROVED |
| P62 | 2.IX.T7,T8,C6 | First-order zero–pole seam asymptotics; reciprocal zero–pole exchange | PROVED |
| P63 | 2.IX.T11,C8 | Logarithmic divergence on the pole side; integrable/nonintegrable exchange | PROVED |
| P64 | 2.IX.T12,C9 | Exact positive Riccati branches; finite-interval pole intrinsic to the chart | PROVED |
| P65 | 2.IX.T13,C10 | Differential closure needs no second continuous generator | PROVED |
| P66 | 2.X.T1–T8 | Named boundary traces at sine-zero and cosine-zero seams | PROVED |
| P67 | 2.X.T9,C1 | Unified FlatWave/carrier seam law | PROVED |
| P68 | 2.XI.T7,C7,T8 | Complex carrier Z_car = e^{2ix}; unit modulus; Z′ = 2iZ | PROVED |
| P69 | 2.XI.T9,T10 | Symmetry laws; phasor fiber theorem (exact fibers mod π) | PROVED |
| P70 | 2.XI.T11,C11 | Complex seam contrast; complex notation regularizes nothing | PROVED |
| P71 | 2.XII.T1 | No circular dependency in the proof chain of this file | PROVED |
| P72 | 2.XII.T3,C2 | Domain ledger: D used consistently; no silent seam regularization | PROVED |
| P73 | 2.XII.T2,C1 | Three-climax synthesis; FlatWave structurally important but not independent data | PROVED |
| P74 | 2.XII.T8 | Zero new mathematical axioms in this file's construction | PROVED |
| A1 | 2.X.A | One-sided boundary convention | ASSERTED (convention) |
| A2 | 2.III | Non-scope declarations are stipulated boundaries | ASSERTED (stipulation) |
| A3 | 2.X | No physical seam law is inferred | ASSERTED (non-scope declaration) |
| A4 | 2.XI.T12 | Retention decisions for Ψ_U, Z_car | ASSERTED (audit decision) |
| A5 | 2.XI | No quantum interpretation is admitted | ASSERTED (non-scope declaration) |
| A6 | 2.XII.T7 | The Wolfram audit changes no theorem status | ASSERTED (audit assertion) |
| A7 | 2.XII.T9 | Closure certification | ASSERTED (bookkeeping verdict) |
| A8 | 2.XII.N1 | Negative closure: 12 things not established (manuscript-wide) | ASSERTED (manuscript claim; verified for this file's chain in P74) |
| A9 | 2.XII.C3 | One-generator closure is task-relative | ASSERTED (stipulation) |
| A10 | 2.VIII.T13 | Book 1's C7 rule, inherited | ASSERTED (cited; no Book 1 proof file in this batch) |
| A11 | 2.XII.C5 | Definitions are not axioms | ASSERTED (methodological stance, adopted here) |
| C1–C12 | p1 figures | The book page's reported numerical re-verification (129 assertions: 116 CP, 12 NC, 1 ST, all passing; pictured identities to ~1e-13) | CHECKED (reported run; not re-run here) |

Totals: **74 PROVED, 12 CHECKED, 11 ASSERTED, 0 INCOMPLETE.**

---

## 4. Proofs in dependency order

### T2.1 — The canonical quartet: reciprocity, positivity, recovery (P1–P5)

*Uses: D1, S1–S2 only.*

**P1 (reciprocity).** On D_s, srx·sxp = |csc x|² − cot²x = csc²x − cot²x.
From sin²x + cos²x = 1 (S2), csc²x − cot²x = (1 − cos²x)/sin²x = 1.
Hence srx·sxp = 1. By **P2** below srx > 0, so sxp = 1/srx; likewise
cxp·crx = sec²x − tan²x = 1 gives crx = 1/cxp. ∎

**P2 (positivity).** |csc x|² − |cot x|² = 1 > 0, so |csc x| > |cot x| ≥ −cot x and
| csc x| > cot x; thus |csc x| ± cot x > 0. The cosine channel is identical. ∎

**P3 (opposite-seam regular value 1).** At a cosine-channel seam x = π/2 + kπ
(sin x = ±1, cos x = 0): srx = |±1| + 0 = 1 and sxp = 1 − 0 = 1, both regular
(the sine pair is defined there since sin x ≠ 0). Symmetrically cxp = crx = 1 at
sine-channel seams x = kπ. ∎

**P4 (conjugate recovery).** Adding/subtracting D1: srx + sxp = 2|csc x|,
srx − sxp = 2cot x; cxp + crx = 2|sec x|, cxp − crx = 2tan x. ∎

**P5 (|·|-preservation).** The identities P1–P4 use |csc x|² = csc²x, i.e. the
absolute value is load-bearing. It cannot be dropped globally: at x = 5π/4,
csc x = −√2, so |csc x| + cot x = √2 + 1 while the |·|-free form csc x + cot x
gives −√2 + 1 ≠ srx. Chart-local simplifications (e.g. srx = csc x + cot x on
(0, π)) are valid only where the sign is locked. ∎

### T2.2 — Half-angle atlas, principal chart (P6)

*Uses: T2.1, S4.*

**P6.** On Q₀ = (0, π/2) ⊂ {sin x > 0}: srx = (1 + cos x)/sin x.
Since 1 + cos x = 2cos²(x/2) and sin x = 2sin(x/2)cos(x/2),
srx = cot(x/2). Likewise sxp = (1 − cos x)/sin x = tan(x/2) on (0, π).
For the cosine channel on (0, π/2): cxp = (1 + sin x)/cos x; with t = tan(x/2),
tan(π/4 + x/2) = (1 + t)/(1 − t), and (1 + t)/(1 − t) = (1 + sin x)/cos x by the
computation (1+t)/(1−t) = (1+cos x+sin x)(1+cos x+sin x)/[(1+cos x)² − sin²x]
= (1+sin x)/cos x. Hence cxp = tan(π/4 + x/2), crx = tan(π/4 − x/2). ∎

### T2.3 — Maximal channel coordinates and bijections (P7)

*Uses: T2.2, S4.*

**P7.** D_s has components (kπ, (k+1)π). On each, with u = x − kπ ∈ (0, π):
for even k, srx(x) = csc u + cot u = cot(u/2); for odd k,
srx(x) = |−csc u| + cot u = csc u + cot u = cot(u/2) (cot is π-periodic).
Thus on every component srx = cot(θ_s/2) with θ_s = u ∈ (0, π), and
cot: (0, π/2) → (0, ∞) is a strictly decreasing bijection (S4). The cosine
channel is analogous with θ_c ∈ (−π/2, π/2). ∎

### T2.4 — Common-domain transport; two chart types (P8)

*Uses: T2.3, S4.*

**P8.** On Q₁ = (π/2, π) (sin > 0, cos < 0): z = (1+cos x)/sin x = cot(x/2) with
x/2 ∈ (π/4, π/2) — the *swapped* chart (values < 1). On Q₂ = (π, 3π/2),
x = π + u: z = csc u + cot u = cot(u/2) — the principal chart reused. On
Q₃ = (3π/2, 2π), x = 2π − u: z = csc u − cot u = tan(u/2) — swapped.
Even quadrants reuse the principal chart, odd quadrants the swapped chart; the
selection is read from ε (P9). ∎

### T2.5 — Range law (P9)

*Uses: T2.4, S4.*

**P9.** From the four quadrant charts: on Q₀, z = cot(x/2) > 1 (x/2 < π/4);
on Q₁, z = cot(x/2) < 1 (x/2 > π/4); on Q₂, z = cot(u/2) > 1; on Q₃,
z = tan(u/2) < 1. Since ε = +1 exactly on Q₀, Q₂ (mod π) and −1 on Q₁, Q₃,
z > 1 ⇔ ε = +1 and 0 < z < 1 ⇔ ε = −1 on all of D (z > 0 by P2). The same
holds for w by the channel symmetry. The branch sign is thus read from the
range — a derived readout (cf. P46). ∎

### T2.6 — Midpoint values (P10)

*Uses: T2.2, S4.*

**P10.** m₀ = π/4: srx(π/4) = cot(π/8) = 1/tan(π/8) = 1/(√2 − 1) = √2 + 1 (S4).
By transport, srx(m_k) = √2 + ε(m_k) and the companion values √2 − 1. ∎

### T2.7 — Octant crossing order (P11)

*Uses: T2.2, S4.*

**P11.** On Q₀, z = cot(x/2) is strictly decreasing (S4); as x runs 0 → π/2, z
runs ∞ ↘ √2+1 (at the octant boundary x = π/4) ↘ 1, crossing each threshold
exactly once. Transport gives the order on all quadrants. ∎

### T2.8 — Symmetry orbit: the Klein four (P14–P19)

*Uses: D1, T2.1, S2.*

**P14 (phase reflection).** srx(−x) = |csc(−x)| + cot(−x) = |csc x| − cot x
= sxp(x) = 1/srx(x) (P1). Similarly cxp(−x) = crx(x). Reflection is reciprocal
inversion within each channel; the fixed values satisfy z = 1/z, i.e. z = 1
(z > 0), the unit threshold. ∎

**P15 (quarter-turn shift).** ι_+: srx(x+π/2) = |sec x| − tan x = crx(x);
crx(x+π/2) = srx(x); sxp(x+π/2) = cxp(x); cxp(x+π/2) = sxp(x). So ι_+ swaps
srx ↔ crx and sxp ↔ cxp. Since ι_+²(x) = x + π acts as the identity on 𝒫
(π-periodicity, P18), ι_+ has order two on the representation. ∎

**P16 (complementary reflection).** ι_d: srx(π/2 − x) = |sec x| + tan x = cxp(x);
crx(π/2 − x) = sxp(x); hence ι_d exchanges the channels sine ↔ cosine. ∎

**P17 (V₄).** id, ι_r, ι_+, ι_rι_+ act on 𝒫 as: id; (srx sxp)(cxp crx);
(srx crx)(sxp cxp); (srx cxp)(sxp crx). Each non-identity element has order two
(P14, P15), and ι_+ι_r ≡ ι_rι_+ on 𝒫 (they differ by a π-shift, invisible to
𝒫). A group of four elements with three involutions is the Klein four V₄;
it is transitive on the quartet: the quartet is a single orbit of one master
function. A label-permutation group only — no physical gauge content. ∎

**P18 (half-turn descent).** |csc(x+π)| = |csc x|, cot(x+π) = cot x, so 𝒫(x+π)
= 𝒫(x): the representation descends to 𝕋_π = ℝ/πℤ. Since z(x+π) = z(x)
*exactly*, no function of z can distinguish x from x + π: the half-turn branch
is not recoverable from the generator. ∎

**P19 (ε transport).** ε(−x) = −ε, ε(x+π/2) = −ε (sin(2x+π) = −sin 2x),
ε(π/2−x) = +ε, ε(x) = ε: two symmetries reverse the branch sector, two preserve
it. ∎

### T2.9 — Stereographic recovery and rational double-angle forms (P12–P13)

*Uses: T2.1, P9.*

**P12.** From P4 and P1: |csc x| = (z + 1/z)/2, cot x = (z − 1/z)/2 with z > 0.
Hence |sin x| = 2z/(z²+1) and, with σ = ±1 the discrete half-turn label,
sin x = σ·2z/(z²+1), cos x = σ·(z²−1)/(z²+1). The signed circle is recovered
from z *plus one bit* σ — the bit z cannot supply (P18). ∎

**P13.** sin 2x = 2 sin x cos x = 4z(z²−1)/(z²+1)² (σ² = 1; the formula carries
its own sign: on Q₀, z > 1 gives sin 2x > 0, etc.). Consequently
sgn(sin 2x) = sgn(z² − 1) = +1 iff z > 1: the double-angle branch sign is read
from the unit threshold (P9). ∎

### T2.10 — UNA differences and the canonical sign lock (P20–P24)

*Uses: D2, T2.1, T2.8, S1.*

**P20 (sign-lock correctness).** urx(ι_d x) = srx(π/2−x) − crx(π/2−x)
= cxp(x) − sxp(x) = uxp(x) (P16). Complementary reflection exchanges the UNA
pair — which is exactly why the order in D2 is canonical: the retired reversed
transcription sxp − cxp = −uxp would be sent to −urx by ι_d, breaking the
exchange. ∎

**P21 (exact magnitude forms).** Direct expansion gives, with a = |cos x|,
b = |sin x| (both > 0 on D):
urx = (ε + a − b)/(ab), uxp = (ε + b − a)/(ab).
(Checked on Q₀: (1+cos x−sin x)/(sin x cos x); on Q₁: −(1+sin x+cos x)/(sin x|cos x|);
the |·|-form unifies them.) ∎

**P22 (common sign; nonvanishing).** On D, ||a − b|| < 1 strictly: |a − b| = 1
would require {a, b} = {0, 1}, i.e. a seam — excluded. Hence
ε(ε + a − b) = 1 + ε(a − b) ≥ 1 − |a − b| > 0, so sgn(ε + a − b) = ε; the
denominator ab > 0. Thus sgn(urx) = sgn(uxp) = ε on all of D — the common
sign — and neither vanishes on D. Sign alternation by quadrant follows from
ε = (−1)^k on Q_k. ∎

**P23 (rational same-phase forms).** (zw − 1)/w = z − 1/w = srx − crx = urx
since 1/w = 1/cxp = crx (P1); likewise (zw − 1)/z = w − 1/z = uxp. The common
numerator gives the UNA ratio theorem urx/uxp = z/w. ∎

**P24 (reversed sign destroys the architecture; checksum).** With the retired
uxp′ = −uxp, sgn(uxp′) = −ε ≠ sgn(urx): the common-sign theorem fails.
At x = π/4: srx = cxp = √2+1 (P10), sxp = crx = √2−1, so urx = uxp = 2 and
urx + uxp = 4 = 4/sin(π/2). ∎

### T2.11 — First climax: double-angle closure (P25–P30)

*Uses: T2.10, Seed, T2.9.*

**P25 (sum closure).** The Seed proves (A − 1/B) + (B − 1/A) = 4/sin 2x with
A = tan x + |sec x| = cxp and B = cot x + |csc x| = srx. By P1,
A − 1/B = cxp − sxp = uxp and B − 1/A = srx − crx = urx. Hence
urx + uxp = 4/sin 2x on D. ∎

**P26 (retired-sign checksum).** urx + (−uxp) = (srx − crx) − (cxp − sxp)
= (srx + sxp) − (cxp + crx) = 2|csc x| − 2|sec x| (P4) — not 4/sin 2x.
The double angle permanently audits the sign convention. ∎

**P27 (one-generator form).** urx + uxp = 4/sin 2x = (z²+1)²/[z(z²−1)] by P13:
the sum is already one-generator data. ∎

**P28 (unsigned companion).** From P21: num(urx)·num(uxp) = (ε+a−b)(ε+b−a)
= 1 − (a−b)² = 2ab (using a² + b² = 1). Hence
urx·uxp = 2ab/(a²b²) = 2/(ab) = 4/|sin 2x| > 0. ∎

**P29 (sign–magnitude).** |urx + uxp| = |4/sin 2x| = 4/|sin 2x| = urx·uxp
(P25, P28): magnitude and binary branch sign are separated. ∎

**P30 (seam behavior).** urx + uxp = 4/sin 2x → ±∞ at every b_k = kπ/2
(one-sided infinities); in the extended right-hand form the reciprocal
1/(urx+uxp) = sin 2x/4 → 0 at the seams. ∎

### T2.12 — Second climax: FlatWave (P31–P39)

*Uses: D3, T2.10, T2.11, T2.8.*

**P31 (rational forms).** saw_r = 1/urx = w/(zw−1), saw_x = 1/uxp = z/(zw−1)
(P23); FlatWave = saw_r + saw_x = (z + w)/(zw − 1). ∎

**P32 (binary character).** FlatWave = (urx+uxp)/(urx·uxp)
= (4/sin 2x)/(4/|sin 2x|) = |sin 2x|/sin 2x = sgn(sin 2x) = ε ∈ {−1, +1}:
the quotient of the signed by the unsigned closure. ∎

**P33.** FlatWave² = ε² = 1 (self-reciprocal); on Q_k, ε = (−1)^k (quadrant
character) with period π (sin 2(x+π) = sin 2x); ε is constant on each open
quadrant, hence FlatWave is flat there (derivative zero where defined). ∎

**P34 (exact boundedness).** On Q₀, urx = (1+cos x−sin x)/(sin x cos x)
= 1 + (1−sin x)(1+cos x)/(sin x cos x) > 1, so 0 < saw_r = 1/urx < 1; likewise
0 < saw_x < 1. Transport by V₄ (P17, P19: ι_+ negates, ι_r swaps-and-negates,
ι_d swaps) gives |saw_r| < 1, |saw_x| < 1 on all of D. ∎

**P35 (Saw product).** saw_r·saw_x = 1/(urx·uxp) = |sin 2x|/4 (P28). ∎

**P36.** saw_r + saw_x = ε: the Saws partition the branch sign (partition of
unity). {saw_r, saw_x} are the two roots of t² − εt + |sin 2x|/4 = 0, so sum
plus product determine the unordered pair. ∎

**P37 (V₄ sign character).** χ_F(id) = +1, χ_F(ι_d) = +1, χ_F(ι_r) = −1,
χ_F(ι_+) = −1 (P19): a homomorphism V₄ → {±1}, not a physical charge. ∎

**P38 (seam limits).** At b_k, FlatWave = sgn(sin 2x) has opposite one-sided
limits ±1 (e.g. at 0: +1 from the right, −1 from the left); it is undefined at
the seams (saw_r, saw_x are). No seam value exists. ∎

**P39 (cross-family equation).** From P31–P32, (z+w)/(zw−1) = ε with zw ≠ 1
(P23, P22), i.e. z + w = ε(zw − 1) — the bridge to the third climax. ∎

FlatWave retains no continuous magnitude (P56 below): ε ∈ {±1} cannot determine
|sin 2x| ∈ (0, 1] — the map is many-to-one.

### T2.13 — Third climax: Möbius reduction (P40–P48)

*Uses: T2.12, T2.5, T2.8, S4.*

**P40 (denominator nonvanishing).** εz − 1 = 0 with z > 0 (P2) would give z = 1,
ε = +1 — excluded by the range law P9 (z > 1 or 0 < z < 1, never 1). ∎

**P41 (same-phase reduction).** From P39: w(1 − εz) = −(z + ε), so
w = (z + ε)/(εz − 1) = M_ε(z) (P40) — at the *same* phase x, not a reflected
one. Explicit branches: (z+1)/(z−1) for ε = +1, (1−z)/(1+z) for ε = −1.
Reciprocal companion: crx = 1/w = (εz−1)/(z+ε) (P1). ∎

**P42 (involution).** M_ε(M_ε(z)) = [(z+ε)+ε(εz−1)]/[ε(z+ε)−(εz−1)]
= 2z/2 = z, using ε² = 1 — by direct fractional-linear computation. ∎

**P43 (branch preservation; order reversal).** M_+: z > 1 ⇒ (z+1)/(z−1) > 1
(numerator > denominator > 0); M_−: 0 < z < 1 ⇒ 0 < (1−z)/(1+z) < 1.
dM_+/dz = −2/(z−1)² < 0, dM_−/dz = −2/(1+z)² < 0: strict order reversal. ∎

**P44.** z(ι_d x) = srx(π/2−x) = cxp(x) = w(x) = M_ε(z(x)) (P16, P41, P19):
the involution on values is the z-coordinate image of complementary reflection. ∎

**P45 (fixed points).** (z+1)/(z−1) = z ⇔ z² − 2z − 1 = 0 ⇔ z = 1 + √2 (positive
root, > 1 ✓). (1−z)/(1+z) = z ⇔ z² + 2z − 1 = 0 ⇔ z = √2 − 1 (positive root,
in (0,1) ✓). Unique positive fixed points √2+1, √2−1 — equal to the midpoint
values P10: the same theorem seen twice. ∎

**P46 (internal branch selection).** ε is read from z via the range law P9 —
and FlatWave = ε is itself derived (P32), not primitive. No second generator
is smuggled in. ∎

**P47 (one generator).** From z = srx on an open quadrant: ε from the range
(P9/P46); w = M_ε(z) (P41); sxp = 1/z, crx = 1/w (P1); urx, uxp, saw_r, saw_x,
FlatWave, H, V all rational in (z, w) (P23, P31, P57). The apparent two-primary
structure collapses at fixed phase; derived layers add vocabulary, not
continuous dimension. ∎

**P48.** By P18, z(x+π) = z(x) exactly: the discrete half-turn label σ is
invisible to the generator. ∎

### T2.14 — Harmonic extraction (P49–P57)

*Uses: T2.11, T2.9, T2.12, S3, S5.*

**P49 (extraction).** H_D = 1/(urx+uxp) = 1/(4/sin 2x) = sin 2x/4 on D (P25).
0 < |H_D| ≤ 1/4, maximum exactly at sin 2x = ±1, i.e. x = π/4 + kπ/2 = m_k. ∎

**P50 (smooth extension; uniqueness).** H(x) = sin 2x/4 extends H_D to ℝ and
is smooth (S3). D is dense in ℝ (S5: complement {kπ/2} nowhere dense), so the
continuous extension is unique. ∎

**P51 (seam values; non-regularization).** H(b_k) = sin(kπ)/4 = 0: these zeros
belong to the extended coordinate H alone. urx, uxp are *undefined* at b_k
(D excludes them); assigning H(b_k) = 0 gives them no values — extension does
not commute with inversion through zero, and the smooth carrier does not
regularize its singular constituents (A10 cited for the Book 1 rule). ∎

**P52 (first-order system).** V = H′ = cos 2x/2 (S3); V′ = −sin 2x = −4H.
Hence H″ + 4H = 0 — an identity in the dimensionless phase coordinate, not a
physical equation of motion. ∎

**P53.** v² + 4h² = cos²2x/4 + sin²2x/4 = 1/4 (carrier ellipse); U² + W² =
sin²2x + cos²2x = 1 (unit circle); |(U′,W′)| = 2√(cos²2x+sin²2x) = 2, constant
phase-parameter speed. ∎

**P54.** F(x) = (H,V): smooth, π-periodic (H(x+π) = H(x), V(x+π) = V(x));
F(x) = F(y) ⇔ (sin 2x, cos 2x) = (sin 2y, cos 2y) ⇔ x ≡ y (mod π): exact
fibers mod π. ∎

**P55 (seam classifier).** V(b_k) = cos(kπ)/2 = (−1)^k/2 ≠ 0 classifies the seam;
H(b_k) = 0 with H′(b_k) = ±1/2 ≠ 0: transverse zero crossing. The seam class
survives smooth gluing. ∎

**P56.** FlatWave = sgn(sin 2x) = sgn(H) on D (P32, P49): FlatWave is the sign
projection of H. Three distinct levels: signed (urx+uxp), unsigned (urx·uxp),
binary (FlatWave). ∎

**P57 (carrier from z).** H = sin 2x/4 = z(z²−1)/(z²+1)² (P13);
cos 2x = (cot²x−1)/(cot²x+1) = (z⁴−6z²+1)/(z²+1)², so
V = (z⁴−6z²+1)/(2(z²+1)²). Seam-safe: these formulas need only z, never the
raw singular operators. ∎

### T2.15 — Differential, integral, asymptotic closure (P58–P65)

*Uses: T2.1, T2.2, T2.9, T2.5, S3–S4.*

**P58 (envelope derivatives).** On each component of D_s, |csc x| = ±csc x with
constant sign, so d/dx|csc x| = −|csc x|cot x (S3). Hence
srx′ = −|csc x|cot x − csc²x = −|csc x|(|csc x| + cot x) = −srx|csc x|;
sxp′ = +sxp|csc x|; cosine analogues cxp′ = +cxp|sec x|, crx′ = −crx|sec x|. ∎

**P59 (Riccati).** |csc x| = (srx + sxp)/2 = (srx + 1/srx)/2 (P4, P1), so
srx′ = −srx(srx+1/srx)/2 = −(1+srx²)/2; sxp′ = +(1+sxp²)/2; and the cosine
analogues cxp′ = +(1+cxp²)/2, crx′ = −(1+crx²)/2. Autonomous: the right-hand
side involves only the function itself. Monotonicity on each maximal component
is exact (strict sign of the derivative). ∎

**P60 (arctangent linearization).** d/dx arctan(srx) = srx′/(1+srx²) = −1/2
(P59); arctan(sxp) = +1/2, arctan(cxp) = +1/2, arctan(crx) = −1/2. Constant
slopes. Phase quadratures: dx = −2 d(srx)/(1+srx²), etc. ∎

**P61 (logarithmic antiderivatives).** By differentiation: d/dx[−ln(1+srx²)]
= −2srx·srx′/(1+srx²) = srx (P59), so ∫srx dx = −ln(1+srx²) + C;
d/dx[ln(1+sxp²)] = 2sxp·sxp′/(1+sxp²) = sxp, so ∫sxp dx = ln(1+sxp²) + C —
on each maximal component (S3). Cosine analogues identical. ∎

**P62 (seam asymptotics).** Near b_k exactly one of sin x, cos x has a simple
zero (S4); e.g. on (0,π/2) ∋ x → 0⁺, srx = cot(x/2) = 2/x + O(x): first-order
pole, residue 2; the reciprocal sxp = tan(x/2) = x/2 + O(x³): first-order zero.
Transport by V₄ gives all cases: the reciprocal zero–pole exchange is
first-order everywhere. ∎

**P63.** As x → π⁻, sxp = tan(x/2) ∼ 2/(π−x): ∫sxp dx diverges logarithmically
on the pole side; srx = 1/sxp → 0 with convergent integral — reciprocal
pairing exchanges integrable and nonintegrable one-sided behavior (S4). ∎

**P64.** srx > 0 (P2) with srx′ = −(1+srx²)/2: the exact positive branch of the
Riccati family; it blows up at both ends of each maximal component (P62), so
the finite-interval pole is intrinsic to the real Riccati chart. ∎

**P65.** P59–P60 express all derivatives rationally in the single function:
differential closure requires no second continuous generator. ∎

### T2.16 — Named boundary atlas (P66–P67)

*Uses: T2.15, T2.12, T2.14, convention A1.*

**P66.** One-sided traces follow from P62: at sine-zero seams the sine pair
diverges (pole side, first-order) while the cosine pair takes regular values;
at cosine-zero seams the reverse; UNA traces from P21; Saw/FlatWave traces from
P31/P38; carrier traces H(b_k) = 0 (P51). Singular raw operators, bounded
split-boundary traces, and smooth carrier gluing are kept distinct — the
one-sided convention A1 is assumed here. ∎

**P67 (unified seam law).** The FlatWave sign jump at b_k is the sign of the
smooth transverse zero of H (P38, P55): sgn(H) jumps exactly where H crosses
zero transversely. ∎

### T2.17 — Complex packaging audit (P68–P70)

*Uses: D7, T2.14, S3.*

**P68.** Z_car = 2V + i4H = cos 2x + i sin 2x = e^{2ix} (Euler, S3).
|Z_car|² = cos²2x + sin²2x = 1 (unit modulus). Z_car′ = −2sin 2x + 2icos 2x
= 2i(cos 2x + i sin 2x) = 2iZ_car: complex linear harmonic equation. ∎

**P69.** The symmetry laws transport through e^{2ix} (P19); phasor fibers:
Z_car(x) = Z_car(y) ⇔ x ≡ y (mod π) (P54). ∎

**P70 (complex seam contrast).** Ψ_U = urx + i·uxp has domain exactly D —
singular at every seam — while Z_car is smooth everywhere: complex notation
does not itself regularize a representation. ∎

### T2.18 — Certification of this file's chain (P71–P74)

**P71 (no circularity).** Dependency DAG of §§4: T2.1 → T2.2 → T2.3 → T2.4 →
T2.5 → T2.6; T2.8 uses only T2.1; T2.9 uses T2.1, P9; T2.10 uses T2.8;
T2.11 uses T2.10 + Seed; T2.12 uses T2.10–T2.11; T2.13 uses T2.12, T2.5;
T2.14 uses T2.11, T2.9, T2.12; T2.15 uses T2.1, T2.9; T2.16 uses T2.15,
T2.12, T2.14; T2.17 uses T2.14; T2.18 is meta. Every theorem cites only
definitions, the substrate S1–S5, the Seed, or strictly earlier theorems.
No cycle. (This audits *this file's* chain; the manuscript's own chain remains
the book's claim.) ∎

**P72 (domain ledger).** D is used consistently as the domain of all raw
operators; every extension (H, V, Z_car) is an explicitly defined continuous
extension with uniqueness proved (P50); P51/P70 show no silent seam
regularization. ∎

**P73 (three-climax synthesis).** Climax 1: P25 (double-angle closure, via the
Seed). Climax 2: P32 (FlatWave binary collapse). Climax 3: P41–P42 (Möbius
reduction, involution). FlatWave = sgn(H) (P56) is structurally central but
derived — not independent data. ∎

**P74 (zero new axioms).** The construction uses: definitions D0–D7 (not axioms,
A11), the declared substrate S1–S5 (standard imports), and the Seed. No
mathematical axiom is added. For this file's chain, the negative closure holds
by inspection: no physical time, frequency/energy, wave propagation, metric,
electromagnetism/gravity, quantum state/Born rule, spin/fermions, particle
ontology, chirality, mirror universe, physical seam-crossing, or empirical
prediction is introduced anywhere in §§1–4 (the manuscript-wide N1 remains the
book's own claim, A8). ∎

---

## 5. Cited numerical checks (CHECKED, C1–C12)

The book page reports its own completed validation run
(`validation/book2/verify_book2.py`, V1–V40: 129 assertions — 116 CP, 12 NC,
1 ST — all passing, no timeouts, on seam-avoiding grids). Per the proof-over-
sampling rule these were **not re-run here**; the analytic proofs above stand on
their own. The 12 NC-status assertions are cited as CHECKED:

- C1: reciprocal conjugacy srx·sxp = cxp·crx = 1 (max error ~3.6e-11).
- C2–C4: double-angle sum/product/sign–magnitude (5.0e-16, 6.5e-14, 6.5e-14 rel.).
- C5–C6: FlatWave collapse FlatWave² = 1 and equality with sgn(sin 2x) (~2.4e-13).
- C7–C9: Möbius involution, branch preservation, fixed points (~3.6e-15).
- C10: same-phase reduction agreement (~7.3e-14).
- C11: carrier ellipse and unit circle (~2.3e-16); harmonic system by finite
  differences (~8.8e-9).
- C12: harmonic extraction through the seams (~7.1e-17).

These check the *same identities* proved analytically in P1, P25, P28–P29, P32,
P42–P43, P45, P41, P53, P52, P49 — agreement is expected, not evidence.

## 6. New axioms / assumptions beyond Euclid + Seed + earlier books

**New mathematical axioms: none** (P74).

What the extension does declare (explicitly, not smuggled):

1. *Substrate imports (S1–S5):* ℝ as a complete ordered field; sin/cos with
   sin²+cos² = 1 and their standard calculus; standard trig identities including
   the exact value cot(π/8) = √2+1; Euler formula; dense-set unique extension.
   These are declared background, not derived from the Elements.
2. *Definitional acts (D0–D7):* the canonical names, the UNA order with
   Constitutional Rule 2.IV.R1, Saw/FlatWave spellings, the branch Möbius map,
   the carrier coordinates, the optional complex packagings. Definitions are not
   axioms (A11).
3. *Conventions and audit assertions (A1–A11):* the one-sided boundary convention;
   stipulated non-scope boundaries (no physical seam law, no quantum
   interpretation); retention decisions for the complex packagings; the Wolfram-
   audit assertion; the manuscript's closure certification and negative closure.

## 7. No-Euclid-wholesale boundary

R Theory extends a synthetic-constructive stratum — the named canonical calculus
proved above — on its declared substrate S1–S5 plus the Seed. It does **not**
inherit the Elements wholesale: no proposition of Euclid Books 1–13 is invoked
in §§1–4. Where the proofs use identities of the form (a±b)² = a²+b²±2ab, they
use them as ordinary commutative-ring axioms of ℝ (part of S1), not as
Euclid 2.4–2.7. The analytic Pythagorean identity sin²+cos² = 1 is declared in
S2; no synthetic Euclidean proof of the classical triangle proposition is
claimed here. This matches the extension's own ledger (cf. the Book 2 Euclid
ledger: "A separate synthetic Euclidean proof of the classical triangle
proposition is not being claimed here").

---

*Written 2026-09-22. 74 PROVED / 12 CHECKED / 11 ASSERTED / 0 INCOMPLETE.
Proof file: ~/workspace/euclid_work/books/book2_proof.md*
