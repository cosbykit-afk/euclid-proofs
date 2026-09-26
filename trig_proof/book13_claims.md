# Book 13 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book13_proof.md` (claim inventory
P1–P44 with proofs, worker 2026-09-22) and the rewrite page
`~/workspace/r-theory-rewrite/book13/index.html` (principal theorems
13.II.T1, 13.III.T1–T2, 13.IV.T1, 13.V.T1, 13.VI.T1, 13.VII.T1,
13.VIII.T1, 13.X.T1–T2).
**Evaluated:** 2026-09-22. **Worker:** trig book 13 (workflow euclid-trig-cumulative).

**No-Euclid boundary:** rewrite Book 13 (thermodynamics/information/arrow
of time) has no mathematical relation to Euclid's *Elements* Book 13 (the
five regular solids) — pure name collision, confirmed by the book13 ledger
(zero EMR/pentagon/solid hits in the rewrite corpus). Nothing below is
inherited from the *Elements*; proofs are analytic from the campaign seed
(P0), the ordinary trigonometry substrate (M0), and earlier registered
principles.

Scope labels: PROVED = exact mathematics; CHECKED = a completed numeric
run with no analytic proof yet; ASSERTED = manuscript claim, contract, or
standard import; INCOMPLETE = failed/timed out/unfinished.

## Claim table

| Claim | Verdict | Scope | Folded-in? | Notes |
|---|---|---|---|---|
| P1 §2.I — λ:(0,π/2)→(0,1) strictly monotone; λ(0)=0, λ(π/4)=1/2, λ(π/2)=1 | verified | PROVED | **Yes → Principle 26 (Book 13)** | dλ/dx=(sin x+cos x)/2>0 on quadrant; endpoint values by substitution. Genuine trig lemma (the admissible chart). |
| P2 §2.I — λ(1−λ) = sin(2x)/4 | verified | PROVED | No — already registered | Exact trig identity, but content already registered as Principle "9 (Book 0)" (H = 1/(urx+uxp) = sin(2x)/4): 1/(urx+uxp) = λ(1−λ) exactly via urx=1/λ, uxp=1/(1−λ). Re-folding would duplicate a registered principle. |
| P3 §2.I — urx=1/λ, uxp=1/(1−λ) pinned (not swapped) | verified | CHECKED | No | Definitional reciprocal-channel algebra; CHECKED status only (book page's own 2×10⁴/4×10⁴-point runs, not re-run here). No independent trig identity. |
| P4 §2.I — λ(π/2−x) = 1−λ(x) | verified | PROVED | **Yes → Principle 27 (Book 13)** | Cofunction symmetry; exact trig identity from M0 cofunction formulas. |
| P5 §2.I — S_sys→0 as \|H\|→0; S_sys=k_B ln 2 at \|H\|=1/4 | verified | PROVED | No | Entropy-limit analysis; its trig content is P1's endpoint values, already folded. (Recovered reading of the garbled source sentence.) |
| P6 §2.I — Ψ_stat carries no quantum phase/coherence | verified | ASSERTED | No | Status declaration under contract AX-1. No trig content. |
| P7 §2.II — A′(v)=λ(v), A′′(v)=λ(1−λ)=\|H\| | verified | PROVED | No | Calculus of the convex generator A(v)=ln(1+e^v); trig content enters only through registered Principle "9 (Book 0)". |
| P8 §2.II — ln\|uxp\|=A(v), ln\|urx\|=A(−v) | verified | PROVED | No | Logarithm algebra. No trig content. |
| P9 §2.II — Legendre identity λv−A(v)=−S_sys/k_B | verified | PROVED | No | Legendre algebra. No trig content. |
| P10 §2.II — KL = Bregman divergence of A (order convention stated) | verified | PROVED | No | Convention identity. No trig content. |
| P11 §2.II — Fisher metric I_v = A′′(v) | verified | PROVED | No | Exponential-family score identity. No trig content. |
| P12 §2.II — φ_F(v)=2arctan(e^{v/2}): ℝ→(0,π), dφ_F/dv=√A′′=√\|H\| | verified | PROVED | No | Exact identity but analytic geometry of the Fisher/logit coordinate, not a trigonometric identity; its only trig content is Principle "9 (Book 0)". Not forced. |
| P13 §2.II — \|H\|·v̇² = φ̇_F² | verified | PROVED | No | Chain-rule corollary of P12. No new content. |
| Thm 13.II.T1 — Bernoulli exponential-family framing | verified | PROVED (cond. AX-1) | No | Framing summary of P7–P13. No trig content. |
| P14 §2.III — canonical bridge formulas (v, T, λ_∞, S_micro, Z, F_eq, Var(E), C, T_s) | verified | PROVED | No | Thermodynamic bridge (physics); trig enters only via registered principles. |
| P15 §2.III — Thm 13.III.T1 temperature identifiability obstruction | verified | PROVED | No | Algebra of βΔ = v − ln(g_r/g_x). No trig content. |
| P16 §2.III — Thm 13.III.T2 response-kernel unification | verified | PROVED | No | Unification statement; trig content = registered P7/P9 content. |
| P17 §2.III — Schottky peak near kT/Δ≈0.42 | verified | CHECKED | No | Numeric witness of P14 (book NC run, not re-run). No trig identity. |
| IC flag §2.III — "\|urx\| is exactly the canonical partition function" | refuted | refutation PROVED | No | False as printed: P14 gives Z = g_r\|urx\|, so \|urx\| = Z/g_r ≠ Z for g_r=2. Recorded as flag, not a claim. |
| P18 §2.IV — σ̇=k_B(J_+−J_−)ln(J_+/J_−)≥0, detailed balance, free-energy identities | verified | PROVED | No | Markov-contract algebra. No trig content. |
| P19 §2.IV — Thm 13.IV.T1 KL/free-energy relaxation | verified | PROVED | No | Consequence of P18. No trig content. |
| P20 §2.IV — slow-driving Fisher form, metric cost | verified | ASSERTED (ST) | No | Standard imports, stated as approximations. No trig content. |
| P21 §2.IV — duration bound "Sigma_prod ≥ [k_B/(γτ)](Δφ_F)²" | verified | PROVED (conditional on P20 Fisher-form premise) | No | RHS recovered from archived Book 13 consolidated draft 2026-09-25; C–S proof exact; independent sympy check all-pass. |
| P22 §2.V — exact-potential affinities telescope to zero | verified | PROVED | No | Finite telescoping sum. Elementary, not trig. |
| P23 §2.V — four-state ring witness | verified | CHECKED | No | Numeric witness (book NC run, not re-run). No trig content. |
| P24 §2.V — Thm 13.V.T1 visible vs microscopic equilibrium | verified | PROVED | No | Consequence of P22–P23. No trig content. |
| P25a §2.V — N1 telescoping half | verified | PROVED | No | Telescoping half. Not trig. |
| P25b §2.V — N1 crossing-rule half | flagged | ASSERTED | No | Leans on the uncertified "source boundary theorem" (single occurrence, inside Book 13). No trig content. |
| P26 §2.VI — cophase order-four action; ε,H,urx,uxp sign laws; π-periodicity | verified | PROVED | Partial — periodicity already registered | The π-periodicity of H and ε is already covered by M0's 2π-periodicity of sin (basis of Principles "3 (Book 0)" and "7 (Book 0)"). Not re-folded. The as-printed urx/uxp π-periodicity is entangled with FlatWave sign conventions (canonical λ has λ(x+π)=1−λ(x), so urx swaps with uxp) and was not reduced to clean trig identities here. |
| P27 §2.VI — no faithful affine C4 action on one real coordinate | verified | PROVED | No | Affine-map order argument. Algebra, not trig. |
| IC flag §2.VI — "λ is quarter-turn invariant" | refuted | refutation PROVED | No | False under canonical notation: λ(0)=0 ≠ 1=λ(π/2). The true invariant is the constructible ratio ε/urx. |
| P28 §2.VI — Thm 13.VI.T1 cophase kinetic nonselection | verified | ASSERTED | No | Conceptual symmetry argument ("canonical selection" premise does the work). No trig content. |
| P29 §2.VI — rank claims, (λ,η) ansatz correction | verified | ASSERTED | No | Modeling language, no precise definitions. No trig content. |
| P30 §2.VII — S_sys(λ)=S_sys(1−λ); entropy symmetric about π/4 | verified | PROVED | No | Follows from D6 + folded Principle 27. No new trig content. |
| P31 §2.VII — Thm 13.VII.T1 two-ended entropy | verified | PROVED | No | Elementary argument from P30. No trig content. |
| P32 §2.VII — path-space arrow material | verified | ASSERTED (ST) | No | Imported statistical-mechanical reasoning. No trig content. |
| P33 §2.VII — retirement of universal Time=ΔEntropy identity | verified | ASSERTED | No | Status declaration following P31. No trig content. |
| P34 §2.VIII — Thm 13.VIII.T1 state-rank obstruction | verified | PROVED | No | Rank argument. Elementary, not trig. |
| P35 §2.VIII — Jacobian criterion, simplex counts | verified | PROVED | No | Elementary. Not trig. |
| P36 §2.VIII — extensivity S_N=N·S_sys, C_N=N·C | verified | ASSERTED (ST) | No | Standard import. No trig content. |
| P37 §2.VIII — N1: V-independent F ⇒ P=0 | verified | PROVED | No | Two-line proof. Not trig. |
| P38 §2.IX — S_sys′′(λ)=−k_B/\|H\| = −4k_B at λ=1/2 | verified | PROVED | No | Calculus of S_sys; trig content via registered Principle "9 (Book 0)". |
| P39 §2.IX — monotone control coordinate τ=a[logit(λ)−logit(λ₀)] | verified | PROVED | No | Restates folded Principle 26 + defines τ. No new content. |
| P40 §2.IX — N1 BEC promotion no-go | verified | PROVED | No | Coordinate-matching argument. No trig content. |
| P41 §2.X — Thm 13.X.T1 candidate-bounded arrow no-go | verified | ASSERTED | No | Exhaustiveness over the candidate list asserted, not proved. No trig content. |
| P42 §2.X — Thm 13.X.T2 Book 13 closure | verified | ASSERTED | No | Section-pointer bookkeeping. No trig content. |
| P43 §2.X — operational closure Δ_op(Volume II)=∅ | verified | ASSERTED | No | Closure bookkeeping; carries the 2.XI.L9 "certified λ" dependency note. No trig content. |
| P44 §2.X — Two-Volume Boundary, Master-Retirement Condition | verified | ASSERTED | No | Procedural declarations. No trig content. |

## Counts

- Evaluated: **44** (P1–P44)
- **PROVED: 28** · **CHECKED: 3** · **ASSERTED: 12** · **INCOMPLETE: 1**
  (P25's telescoping half counted under PROVED, its crossing-rule half
  under ASSERTED, per the book proof file's ledger.)
- Two IC flags with PROVED analytic refutations (recorded as flags, not
  claims).
- Folded into the cumulative proof: **2** — P1 → Principle 26 (Book 13),
  P4 → Principle 27 (Book 13).
- Not folded: 42 (1 genuine identity already registered as "9 (Book 0)",
  1 periodicity claim already covered by M0/"3 (Book 0)"/"7 (Book 0)",
  40 with no honest trigonometric content).

## New axioms / assumptions beyond Euclid + seed + earlier books

None beyond what the book file declares: AX-1 (Bernoulli contract),
AX-2 (Gibbs canonical contract), AX-3 (Markov contract), AX-4
(path/reversal contract), AX-5 (many-body contract) — all ASSERTED — plus
background real analysis (differentiation, limits, logarithms) used as
ordinary background mathematics, and the flagged uncertified "source
boundary theorem" premise in P25b. No *Elements* proposition is a premise
of any folded principle.

status: complete
