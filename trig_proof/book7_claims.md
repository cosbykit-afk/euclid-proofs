# Book 7 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book7_proof.md` (claim inventory §2,
proofs §3, axioms §4; 23 inventory rows + 4 axioms). Evaluated 2026-09-22.

**Verification method.** Every proof in §3 read in full and each algebraic step
re-checked by hand. The existing exact SymPy log
(`book7_sympy_check.log`, 26/26 PASS) was read but **not re-run** (proof-over-sampling
rule: an exact symbolic pass already on record is cited, not repeated). The page's
reported numerical runs (T2 off-chart branches at 2.2e-13; A-7.1 grounding at
3.3e-16) are cited as CHECKED, not re-run. Two steps the book file left to audit
authority were **independently re-derived here from registered PROVED Book 2
material**: Lemma 7.12 (A-7.2) from Book 2 P4, and 7.2.T2 from Book 2 P4 — both
are one-line consequences, shown below. No new computations were run on top of
any complete analytic proof.

**Scope labels:** PROVED (complete analytic proof, verified by reading) ·
PROVED-conditional (proved given a named asserted import) · CHECKED (completed
run, no analytic proof) · ASSERTED (manuscript claim/assumption/convention/import) ·
INCOMPLETE (failed/timed out/unfinished).

**Euclid boundary.** No proposition of Euclid's Elements is used as a logical
premise anywhere in Book 7 — the proof file's §5 states this, and reading the
derivations confirms it: every step is algebra, calculus, or standard
trigonometry. The candidate principles below cite no Euclid; stated plainly.

**Hyperbolic note.** No hyperbolic *functions* (sinh/cosh) appear in Book 7;
the "hyperbolic parent" is the real hyperbola Σ²−Δ² = 16 in the (Σ,Δ) plane.
There is nothing to prove from exponential definitions.

## PROVED claims (21 rows)

| Claim | Restatement | Verdict | Reason / proof sketch | Principle candidate? |
|---|---|---|---|---|
| 7.1.T1 | Sine carrier as signed balance product `H = ελ(1−λ)`; `\|H\| ≤ 1/4`, sharp at λ=1/2 | PROVED (A-7.1 resolved 2026-09-27: λ chart-local) | Proof read and verified: given A-7.1, `saw_r·saw_x = ε²λ(1−λ) = λ(1−λ)` (ε²=1) and `saw_r+saw_x = ε`, so `H = λ(1−λ)/ε = ελ(1−λ)` since `1/ε = ε`. Bound: `λ(1−λ) ≤ 1/4` is the vertex of the concave quadratic at λ=1/2 (elementary); sharpness attained at x=π/4 (λ=1/2, H=1/4 on the principal chart). | no — trig kernel is candidate **P1** (Lemma 7.2); the ε-form and bound are transfer bookkeeping + `\|sin2x\| ≤ 1` |
| 7.1.C1 | Endpoint/balance structure of the saw pair | PROVED (A-7.1 resolved 2026-09-27: λ chart-local) | Elementary given A-7.1: the pair sums to ε with product λ(1−λ); H→0 at the λ∈{0,1} endpoints. | no — operator bookkeeping |
| 7.1.T2 | Companion cosine `cos2x = ε(1−2λ)√(1+4λ(1−λ))` | PROVED on all charts — analytic off-chart branch proof written 2026-09-26 (T2_EPS_OFFCHART_PROOF.md), conditional on Lemma 7.2 (PROVED) | Principal-chart proof (Prop 7.3) read and verified step by step: with λ=(1+sin x−cos x)/2, `RHS² = (cos x−sin x)²(1+sin2x) = (1−sin2x)(1+sin2x) = cos²2x` (uses Lemma 7.2: `1−2λ = cos x−sin x`, `4λ(1−λ) = sin2x`). Sign: on (0,π/2), ε=+1 and √≥0 so `sgn(RHS) = sgn(cos x−sin x)`; `cos2x = (cos x−sin x)(cos x+sin x)` with `cos x+sin x > 0`, so signs match (zero case x=π/4 gives 0=0). Hence RHS = cos2x. | **yes — P2** (principal-chart identity) |
| 7.1.C2 | Differential companion `cos2x = 2H′` | PROVED | `H = sin2x/4`, so `H′ = 2cos2x/4 = cos2x/2`; `2H′ = cos2x`. Exact differentiation. | no — M0 calculus |
| 7.1.D/N | `N = 4cot2x`, `D² − N² = 16` (D = 4csc2x) | PROVED | `D²−N² = 16(csc²2x − cot²2x) = 16` by the standard identity. | no — M0 background identity |
| 7.1.T3 | Carrier phasor `Z = C+iS = e^{2ix}`; quadrature `S′=2C`, `C′=−2S` | PROVED | `C²+S²=1` is Pythagorean; `e^{2ix}` is Euler's formula (standard import); `S′ = 2cos2x = 2C`, `C′ = −2sin2x = −2S` by differentiation. "Frequency doubling" is bookkeeping (φ_c = 2x). | no — Euler + M0 derivatives |
| 7.1.T4 | Transfer–carrier quadratic map `U+iW = εζ²` (U=sin2x, W=cos2x); no independent phase | PROVED (open quadrants) | Props 7.4–7.5 read and verified: on open quadrants α²=β²=1; `p²+q² = 2` exactly; `pq = αβ(cos²x−sin²x) + (α²−β²)sinx cosx = αβcos2x`, and `αβ = sgn(sin x)sgn(cos x) = sgn(sin2x) = ε`, so `pq = εcos2x`. Then `a²−b² = (q²−p²)/2 = αβsin2x = εsin2x`, `2ab = pq = εcos2x`; with U=sin2x, W=cos2x: `U+iW = ε(a+ib)² = εζ²`. Negative corollary is definitional: every quantity is a function of the single scalar x. | no — the ordinary two-to-one circle-squaring map in book variables; no new trig identity |
| 7.2.L1 | `sec²−tan² = csc²−cot² = 1` | PROVED (standard import) | `csc²x−cot²x = (1−cos²x)/sin²x = 1`; `sec²x−tan²x = (1−sin²x)/cos²x = 1`. | no — M0 background, not a Book 7 result |
| 7.2.T1 | UNA reciprocal-sum `sin2x/4 = 1/(urx+uxp)` | PROVED | Seed lemma verified: with A=tan x+\|sec x\|, B=cot x+\|csc x\|, `A−1/A = 2tan x` (since `1/A = \|sec x\|−tan x` via `(tan²x−sec²x) = −1`), `B−1/B = 2cot x`, and `2tan x+2cot x = 2/(sinx cosx) = 4/sin2x`. Summand identification `A−1/B = uxp`, `B−1/A = urx` is Book 2 P25's proof (independently verified in the book2 campaign as PROVED). Hence `urx+uxp = 4/sin2x` on D. | **yes — P3** (seed in channel notation; duplicates registered P0 / book2 P25 — dedup later) |
| 7.2.T2 | Reciprocal-square `cos2x/4 = 1/(cxp+crx)² − 1/(srx+sxp)²` | PROVED | **Re-derived here** (the book file accepted the page's audit; the derivation below is mine): from registered PROVED Book 2 P4, `srx+sxp = 2\|csc x\|` and `cxp+crx = 2\|sec x\|`. Hence `1/(cxp+crx)² = 1/(4sec²x) = cos²x/4` and `1/(srx+sxp)² = 1/(4csc²x) = sin²x/4`; difference `= (cos²x−sin²x)/4 = cos2x/4`. Valid on D (sin x≠0, cos x≠0; denominators `2\|sec x\|`, `2\|csc x\|` never vanish). | **yes — P4** (trig kernel is the standard cos²−sin²=cos2x; new only in channel-function packaging) |
| 7.3.T1 | Closed flow `P′=V`, `V′=−4P` (P=sin2x/4, V=cos2x/2) | PROVED | `P′ = 2cos2x/4 = V`; `V′ = −2sin2x/2 = −sin2x = −4P`. Exact differentiation; closed (no new state variable) is definitional. | **yes — P5** (doubled-frequency harmonic oscillator; probable duplicate of registered P21 — dedup later) |
| 7.3.T2 | Conserved `E = V²+4P² = 1/4` | PROVED | `V²+4P² = cos²2x/4 + 4sin²2x/16 = 1/4` exactly on the orbit. | no — Pythagorean corollary |
| 7.3.C2–C4 | Generator `A²=−4I`, `AᵀG+GA=0` (G=diag(4,1)); evolution `dM/dx = AM`, `M(0)=I`; circular normalization `Q₂²+V²=1/4` | PROVED | Matrix identities verified by hand: `A=[[0,1],[−4,0]]`, `A² = [[−4,0],[0,−4]]`; `AᵀG = [[0,−4],[4,0]] = −GA`. `M=[[cos2x,sin2x/2],[−2sin2x,cos2x]]`: `dM/dx = [[−2sin2x,cos2x],[−4cos2x,−2sin2x]] = AM`; `M(0)=I`. `Q₂=2P`: `Q₂²+V² = sin²2x/4+cos²2x/4 = 1/4`. | no — linear-algebra/ODE machinery; trig kernel is M0 derivatives |
| 7.3.T3 | Formal Hamiltonian `H=V²/2+2P²=1/8` after declaring `ω=dP∧dV` | PROVED, conditional on the declared two-form A-7.3 | On the orbit `H = cos²2x/8+sin²2x/8 = 1/8`; Hamilton's equations `∂H/∂V = V = P′`, `−∂H/∂P = −4P = V′` check exactly; equivalently `P″+4P=0`. The two-form is an explicit declaration, part of the result. The book does not call H physical energy. | no — conditional formalism, no trig content |
| L7.12 (= A-7.2) | Primitive factorization `Σ+Δ = 4cot x`, `Σ−Δ = 4tan x` | PROVED | **Re-derived here** (the book file took it on the page's audit authority): with Σ=urx+uxp, Δ=(srx+crx)−(sxp+cxp), urx=srx−crx, uxp=cxp−sxp (Book 2 D2), and registered PROVED Book 2 P4 (`srx−sxp = 2cot x`, `cxp−crx = 2tan x`): `Σ+Δ = 2(srx−sxp) = 4cot x`; `Σ−Δ = 2(cxp−crx) = 4tan x`. One line each. Domain D (sin x≠0, cos x≠0). This upgrades the book's own "conditional on A-7.2" labels below to unconditional-on-Book-2-PROVED. | no — operator-level corollary of P4; adds no trig content beyond P4 |
| 7.4.T1 | Hyperbolic parent `Σ²−Δ² = 16` | PROVED (via L7.12) | `(Σ+Δ)(Σ−Δ) = 16cot x·tan x = 16`. One-line corollary of L7.12. | no — kernel is `cot x·tan x = 1` (M0); the hyperbolic form is book-variable bookkeeping |
| 7.4.T2 | Projective completion `(Q,S) = (Δ/Σ, 4/Σ)` on the unit circle | PROVED (via T1) | `Q²+S² = (Δ²+16)/Σ² = (Δ²+Σ²−Δ²)/Σ² = 1` using T1. Exact. | no — Pythagorean in (Q,S) |
| 7.4.T3–T5 | Parent flow `Σ′=−ΣΔ/2`, `Δ′=−Σ²/2`; first integral `d(Σ²−Δ²)/dx=0`; projective linearization `Q′=−2S`, `S′=2Q` | PROVED (via L7.12) | From L7.12, Σ=2(cot x+tan x)=4/sin2x, Δ=2(cot x−tan x)=4cos2x/sin2x (verified). Differentiation verified by hand: `Σ′ = −8cos2x/sin²2x = −ΣΔ/2`; `Δ′ = −8/sin²2x = −Σ²/2`. Then `Q′ = (Δ′Σ−ΔΣ′)/Σ² = −32/(sin2x)·sin²2x/16 = −2sin2x = −2S`; `S′ = −4Σ′/Σ² = 2cos2x = 2Q`. First integral: `2ΣΣ′−2ΔΔ′ = −Σ²Δ+Σ²Δ = 0`. | no — calculus; the linearization is M0 derivatives of sin/cos |
| 7.4.T6–T7, C6–C10 | `L₊L₋=1`; `w′=−Σ/2` (w=ln\|cot x\|); rational `Q=(L²−1)/(L²+1)`, `S=2εL/(L²+1)`; Riccati `L′=−ε(1+L²)` | PROVED (open quadrants; via L7.12 for the w′ form) | `L₊L₋=1` definitional. `w′ = −csc²x/cot x = −1/(sinx cosx) = −2/sin2x = −Σ/2` (last step via Σ=4/sin2x from L7.12). Rational: `Q²+S² = ((L²−1)²+4ε²L²)/(L²+1)² = 1` (ε²=1); indeed `(L²−1)/(L²+1) = (cot²x−1)/(cot²x+1) = cos2x` and `2εL/(L²+1) = 2ε\|cot x\|sin²x = 2ε\|cos x\|\|sin x\| = sin2x` since `ε = sgn(sin x)sgn(cos x)` on open quadrants. Riccati: `L′ = sgn(cot x)(−csc²x) = −sgn(cot x)(1+L²)` with `sgn(cot x) = ε`. All steps verified. | **yes — P6** (rational parametrization; dup-suspect of registered P13/P19), **P7** (signed Riccati; dup-suspect of registered Book 0 P5), **P8** (log-derivative; differential form of registered P23) |
| 7.4.CL2 (corrected) | Corrected identity `2λ−1 = sin x − cos x`; the book's printed `cos x − sin x` is a sign error | PROVED | Lemma 7.2: `1−2λ = 1−(1+sin x−cos x) = cos x−sin x`, so `2λ−1 = sin x−cos x`. The printed version is a verified manuscript slip (also caught by the SymPy log's CL2 check); the clarification's conclusion (`2λ−1 ≠ cos2x`) is unaffected. | **yes — P1** (part of the λ-lemma); the printed slip is a documented error, not a live claim |
| Negatives / clarifications (7.1.N1, 7.2.N1, 7.3.N1–N2, 7.4.N1, 7.1.CL1, 7.4.CL2 coord part) | Scope statements: no physical time, energy, force law, gauge structure, or independent U(1) phase is derived; bare `2λ−1` is not the cosine; `2λ−1 ≠ cos2x` | PROVED (statements about the construction) | Verified by reading: no derivation assigns physical meaning to x, H, E, or Σ²−Δ²; "no independent phase" is a definitional corollary of T4 (everything is a function of x). 7.1.CL1 follows from T2 (the envelope factor `ε√(1+4λ(1−λ))` is essential). `2λ−1 ≠ cos2x` follows from CL2 (sin x−cos x vs cos2x). | no — scope statements, no trig content |

## CHECKED claims (1)

| Claim | What it checks | Scope | Principle? | Notes |
|---|---|---|---|---|
| 7.1.T2 off-chart branches | The companion-cosine identity on the three non-principal charts | PROVED | no — sign bookkeeping of an established identity, not a new principle | Analytic branch proof written 2026-09-26 (T2_EPS_OFFCHART_PROOF.md): ε = sgn(cos x+sin x) forced wherever 1+sin2x > 0; both sides vanish on the complement; the manuscript ε = sgn(sin x)sgn(cos x) is falsified on (π/2,3π/4)∪(π,3π/2)∪(7π/4,2π). Machine-corroborated per step (local sympy + WolframAlpha session 2026-09-26-1051). The manuscript page's 2.2e-13 numeric run stands as cited NC. |

## ASSERTED claims (7)

| Claim | Restatement | Scope | Principle? | Notes |
|---|---|---|---|---|
| A-7.1 | Book 2 transfer data import: principal-chart `λ=(1+sin x−cos x)/2`, `saw_r=ελ`, `saw_x=ε(1−λ)`, `saw_r+saw_x=ε=sgn(sin2x)`, `p=1−2λ` | RESOLVED 2026-09-27 (Kit: λ chart-local) | no | The page's audit notes a dependency-labeling defect on the "certified" λ in the Volume I Book 2 ledger and marks the transfer sections read-but-not-independently-checked; numerically grounded at 3.3e-16 per the page (cited, not re-run). Conditions 7.1.T1 and 7.1.C1. Chart note (WA session 2026-09-26-1740, NC only): with the raw principal-chart λ, `\|saw_r\|+\|saw_x\| ≈ 1.32544 ≠ 1` and `ελ(1−λ) ≈ +0.1892 ≠ sin(2x)/4 ≈ −0.1892` at off-chart x=2.0; on-chart control x=1.0 gives {1, 0.227324, 0.227324}, fully consistent. Whether the saw framework's λ is chart-local (per-chart sawtooth in [0,1]) or the unqualified saw identities need the principal-chart qualifier is RESOLVED 2026-09-27 — Kit's call: λ is chart-local, not principal-formula-global. Forced per-chart form (derived from `saw_r=ελ`, `saw_x=ε(1−λ)` + the FW-T12 input identity): `λ=(1±√(1−\|sin2x\|))/2`, branch per chart; naive frac-mod-1 wrapping does NOT preserve `(saw_r²−saw_x²)²=1−\|sin2x\|`. Per-chart identities PROVED by substitution on each chart minus the nodal set `{sin2x=0}` (where ε=0 — pre-existing, same as principal chart), CHECKED ~1e-16 incl. off-chart x=2.0 (`chart_local_lambda_check.py`). The principal formula `(1+sin x−cos x)/2` is the principal-chart branch (piecewise ±). 7.1.T1, 7.1.C1 now PROVED outright under this reading. |
| A-7.3 | Declared two-form `ω = dP∧dV` enabling the formal Hamiltonian | ASSERTED (explicit declaration) | no | Part of the result by declaration, not smuggled in. Conditions 7.3.T3. |
| A-7.4.E1 | Conserved-level extension hypothesis: study the parent ODE on a larger initial-data space with `K = Σ²−Δ²` as a level | ASSERTED (extension hypothesis) | no | Explicitly labeled a lawful extension, not an inherited theorem. NC 2026-09-27 (WA manual session, transcript wa_sessions/2026-09-27-0245.md): K=9 instance Σ(1)≈3.5696, Δ(1)≈−1.9344, Σ²−Δ²≈9.0000; K=−16 instance Σ(2)≈0.04884, Δ(2)≈4.00030, Σ²−Δ²≈−16.0000; WA independently returned matching closed forms. K=0 instance: corroborated in round 2 via the reduced single ODE y′=−y²/2, y(0)=4 → y(x)=4/(2x+1), y(1)=4/3 exactly. Corroboration only — status unchanged. |
| 7.4.E1 | Conserved-level deformation + elliptic/parabolic/hyperbolic classification by sgn(K) | ASSERTED as extension | no | The classification mathematics is exact **conditional on the extension hypothesis**; the certified carrier fixes K=16. Not proved as a theorem of the carrier. NC 2026-09-27 (WA manual session, transcript wa_sessions/2026-09-27-0245.md): K=9 → elliptic behavior confirmed numerically (Σ(1)≈3.5696, invariant 9.0000); K=−16 → hyperbolic/exponential-decay behavior confirmed (Σ(2)≈0.04884, invariant −16.0000); K=0 parabolic instance corroborated in round 2 (reduced ODE y′=−y²/2 → y(x)=4/(2x+1), y(1)=4/3). Corroboration only — status unchanged. |
| 7.4.CL1 | Signature firewall: no physical reading of `x, H, E, Σ²−Δ²` | ASSERTED (non-scope stipulation) | no | A methodological boundary declaration, not mathematics — cf. book2 A2/A3. |
| "certified" status of the core | Status label for the carrier | ASSERTED | no | The manuscript's own term; the page's own finding. Not a mathematical claim. |
| §7.4 closing link | "Book 5 flow / Axiom Zero realized at doubled phase" | ASSERTED-conditional | no | Inherits Book 5's Axiom Zero as an assumption (per the Volume I ledger); Book 7's use is conditional on it. |

## INCOMPLETE (1)

| Claim | Gap | Notes |
|---|---|---|
| 7.1.T2 off-chart analytic branch proof | RESOLVED 2026-09-26 — the analytic proof now exists (T2_EPS_OFFCHART_PROOF.md). | Row retired from INCOMPLETE; see the PROVED 7.1.T2 rows above. Nothing timed out or failed; the proof was written, not carried over. |

## Candidate trigonometric principles (8)

All are PROVED (two PROVED-conditional on named asserted imports). None cites Euclid
(none used). Report includes suspected duplicates per instruction — dedup happens later.

**P1 — λ-coordinate double-angle identities.** *Statement:* For `λ := (1+sin x−cos x)/2`
(all real x): (i) `1−2λ = cos x−sin x` (i.e. `2λ−1 = sin x−cos x`); (ii)
`4λ(1−λ) = sin 2x`. *Proof:* (i) `1−2λ = 1−(1+sin x−cos x) = cos x−sin x`. (ii)
`4λ(1−λ) = (1+(sin x−cos x))(1−(sin x−cos x)) = 1−(sin x−cos x)² = 1−(1−sin2x) =
sin2x`. *Scope:* PROVED. *Source:* Lemma 7.2; 7.4.CL2 (corrected). *Euclid:* none.

**P2 — Companion cosine (principal chart).** *Statement:* For x∈(0,π/2), with λ as
in P1 and `ε = sgn(sin2x) = +1`: `cos2x = ε(1−2λ)√(1+4λ(1−λ))`. *Proof:* Square the
RHS and use P1: `RHS² = (cos x−sin x)²(1+sin2x) = (1−sin2x)(1+sin2x) = cos²2x`;
`sgn(RHS) = sgn(cos x−sin x) = sgn(cos2x)` since `cos2x = (cos x−sin x)(cos x+sin x)`
with `cos x+sin x > 0` on (0,π/2) (zero case x=π/4 gives 0=0). *Scope:* PROVED on all charts (analytic branch proof 2026-09-26;
T2_EPS_OFFCHART_PROOF.md). *Source:* 7.1.T2.
*Euclid:* none.

**P3 — Reciprocal-sum / seed in channel notation.** *Statement:* On D
(`sin x≠0, cos x≠0`): `urx+uxp = 4/sin2x`, i.e. `sin2x/4 = 1/(urx+uxp)`. *Proof:*
Campaign seed (PROVED analytically at
`~/workspace/kit_theorems/secant-cosecant-identity/PROOF.md`): with
A=tan x+|sec x|, B=cot x+|csc x|, `A−1/A = 2tan x`, `B−1/B = 2cot x`, and
`2tan x+2cot x = 4/sin2x`; the summands identify as `A−1/B = uxp`, `B−1/A = urx`
(Book 2 P25, independently verified PROVED in the book2 campaign). *Scope:*
PROVED. *Duplicates:* registered P0 (the seed) / book2 P25 in other notation —
dedup later. *Source:* 7.2.T1. *Euclid:* none.

**P4 — Reciprocal-square decomposition of cos2x.** *Statement:* On D:
`cos2x/4 = 1/(cxp+crx)² − 1/(srx+sxp)²`. *Proof (re-derived here):* registered
PROVED Book 2 P4 gives `srx+sxp = 2|csc x|`, `cxp+crx = 2|sec x|`; hence RHS
`= cos²x/4 − sin²x/4 = cos2x/4`. *Scope:* PROVED. *Note:* trig kernel is the
standard `cos²x−sin²x = cos2x`; new only in channel-function packaging. *Source:*
7.2.T2. *Euclid:* none.

**P5 — Doubled harmonic flow.** *Statement:* For P=sin2x/4, V=cos2x/2:
`P′ = V`, `V′ = −4P` (hence `P″+4P = 0`). *Proof:* exact differentiation.
*Scope:* PROVED. *Duplicates:* probable duplicate of registered P21 (book2 P52
harmonic law, undoubled) — dedup later. *Source:* 7.3.T1. *Euclid:* none.

**P6 — Rational double-angle parametrization in L=|cot x|.** *Statement:* On open
quadrants, with L=|cot x| and `ε = sgn(sin2x)`: `cos2x = (L²−1)/(L²+1)`,
`sin2x = 2εL/(L²+1)`. *Proof:* `(cot²x−1)/(cot²x+1) = cos2x`;
`2ε|cot x|/(cot²x+1) = 2ε|cot x|sin²x = 2ε|cos x||sin x| = sin2x` since
`ε = sgn(sin x)sgn(cos x)`. *Scope:* PROVED. *Duplicates:* dup-suspect of
registered P13/P19 (rational double-angle) — dedup later. *Source:* 7.4.T6–T7.
*Euclid:* none.

**P7 — Signed Riccati law.** *Statement:* On open quadrants, L=|cot x| satisfies
`L′ = −ε(1+L²)` with `ε = sgn(sin2x)`. *Proof:* `L′ = sgn(cot x)(−csc²x) =
−sgn(cot x)(1+L²)`; `sgn(cot x) = sgn(cos x)sgn(sin x) = ε`. *Scope:* PROVED.
*Duplicates:* dup-suspect of registered Book 0 P5 (book2 P59 Riccati pair) —
dedup later. *Source:* 7.4.T6–T7. *Euclid:* none.

**P8 — Log-derivative.** *Statement:* For `w = ln|cot x|` (x not a multiple of
π/2): `w′ = −2/sin2x`. *Proof:* `w′ = −csc²x/cot x = −1/(sinx cosx) = −2/sin2x`.
(The book's `−Σ/2` form additionally uses Σ=4/sin2x from L7.12.) *Scope:*
PROVED. *Duplicates:* differential form of registered P23 (book2 P61 log
antiderivatives) — dedup later. *Source:* 7.4.T6. *Euclid:* none.

## Not made into principles (grouped, with reasons)

- **M0 background / standard imports (4):** 7.2.L1, 7.1.D/N (`csc²−cot²=1`
  packaging), 7.1.T3 (Euler + derivatives), 7.1.C2 (plain differentiation) —
  true but standard mathematics, not Book 7 results.
- **Book machinery / operator algebra, no new trig identity (6):** 7.1.C1,
  7.1.T1 (ε-form; kernel is P1), 7.1.T4 (standard circle-squaring map in
  αβ-variables), L7.12 (one-line corollary of P4), 7.4.T1 (kernel `cot·tan=1`),
  7.4.T2 (Pythagorean in (Q,S)).
- **Calculus/ODE/matrix consequences with M0 trig kernel (3):** 7.3.T2,
  7.3.C2–C4, 7.4.T3–T5 (the linearization `S′=2Q, Q′=−2S` is M0 derivatives).
- **Conditional formalism, no trig content (1):** 7.3.T3 (conditional on the
  declared two-form A-7.3).
- **Scope/meta/negative statements (8 sub-items):** 7.1.N1, 7.2.N1, 7.3.N1–N2,
  7.4.N1, 7.1.CL1, 7.4.CL1, 7.4.CL2-coord — verified statements about the
  construction, not identities.
- **Asserted, not proved (5):** 7.4.E1, A-7.3, A-7.4.E1, "certified"
  status label, §7.4 Book 5 link. (A-7.1 resolved 2026-09-27 — see row.)
- **CHECKED: 0** (the 7.1.T2 off-chart branch check is superseded by the
  2026-09-26 analytic proof).
- **INCOMPLETE: 0** (the 7.1.T2 off-chart analytic branch proof was written
  2026-09-26; no gaps remain in this file).

## Counts

- Evaluated: **27** inventory items (23 claim rows + 4 axioms) in **28** table
  rows — the negatives group splits by verdict (7 PROVED scope statements +
  7.4.CL1 ASSERTED), and 7.1.T2's split verdict is resolved 2026-09-26 (PROVED on all branches).
- **PROVED: 22** rows (21 unconditional-on-Book-7 + 1 PROVED-conditional:
  7.3.T3 on A-7.3; 7.1.T1/7.1.C1 upgraded from conditional to unconditional
  2026-09-27 when A-7.1 resolved). Includes three upgrades over the
  book's own labels: L7.12 (A-7.2) and 7.2.T2 were re-derived here from
  registered PROVED Book 2 P4 rather than taken on audit authority, so the
  7.4 chain is PROVED outright, not PROVED-conditional; and the 7.1.T2
  off-chart branches are PROVED outright by the 2026-09-26 analytic branch
  proof (T2_EPS_OFFCHART_PROOF.md).
- **CHECKED: 0** (the former 7.1.T2 off-chart branch check is superseded by
  the 2026-09-26 analytic proof).
- **ASSERTED: 6** (A-7.3, A-7.4.E1, 7.4.E1, 7.4.CL1, "certified" status,
  Book 5 link; A-7.1 resolved 2026-09-27).
- **INCOMPLETE: 0** (the 7.1.T2 off-chart analytic branch proof was written
  2026-09-26; no timeout or failure was ever involved).
- Folded into the cumulative proof as candidates: **8** (P1–P8), all PROVED;
  5 carry duplication notes for the later dedup pass (P3→P0/P25, P4 kernel M0,
  P5→P21, P6→P13/P19, P7→Book 0 P5, P8→P23).

status: complete
