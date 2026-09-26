# Book 20 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book20_proof.md` (claim inventory
§B, items 1–16; item 11 expands to W1–W9) and rewrite page
`~/workspace/r-theory-rewrite/book20/index.html` (*Book 20 — Relativistic
and Spinor Witnesses*). Evaluated 2026-09-22. This is the last book of the
campaign (stops before Books 21–22).

**Verification method.** All proofs in §C read in full, step by step. The
load-bearing algebraic identities were independently re-derived and checked
exactly (Lemma L1 half-angle identities; K1 kinematic/rapidity algebra;
N2 counter-rotating decomposition; T2 ξ formula; T3 rationality
substitutions; W2 duality-rotation action; W7 dimension count; W9 3:1
arithmetic; F1/F2/A1/C0 definition-unpacking). One genuine erratum found in
§C's S1 proof (sign slips in the stated r_z / r_y definitions — the stated
Bloch vector itself is exact under standard Bloch conventions, verified by
an independent numeric check, see claim 3 row). Per the proof-over-sampling
rule nothing was numerically sampled on top of a complete analytic proof.

**Scope labels:** PROVED (exact mathematics, complete — conditional where
the book names imports, the conditions stated), CHECKED (completed numeric
run), ASSERTED (manuscript claim/assumption/convention/import), INCOMPLETE
(failed, timed out, or unfinished — none here).

**Euclid contact:** none. No proposition of the *Elements* is used as a
logical premise anywhere in Book 20's proofs (the book states this itself
in §0, and every derivation in §C was read and uses only the modern
substrate: SR kinematics, Dirac theory, Bloch geometry, SM weak sector,
Coulomb/Dirac–Coulomb analysis, classical EM). The contact with Euclid is
stylistic only. No ledger citation is claimed.

## PROVED claims (18 distinct)

| Claim | Restatement | Verdict / scope | Reason / proof sketch |
|---|---|---|---|
| 1 — 20.1.K1 | Kinematic dictionary: `sxp(χ) = pc/(E+mc²) = tan(χ/2)`, `cxp = e^η`, `cxp·crx = 1` as the mass shell; chart invertible on χ ∈ [0, π/2) | PROVED, conditional on I-SR + I-Dirac (imports named) | From D-χ: sin χ = p/E, cos χ = m/E; sin²+cos² = (p²+m²)/E² = 1 by the imported mass shell. L1 (verified below) gives tan(χ/2) = sin χ/(1+cos χ) = (p/E)/((E+m)/E) = p/(E+m); the pc/(E+mc²) form is the imported Dirac ratio. Rapidity: e^{2η} = (1+tanh η)/(1−tanh η) = (1+β)/(1−β); and (E+p)²/m² = (E+p)²/(E²−p²) = (E+p)/(E−p), so cxp = (E+p)/m = e^η, crx = (E−p)/m = e^{−η}; product (E²−p²)/m² = 1. sin strictly increasing on [0,π/2) gives invertibility. All steps re-derived; the physics identities are declared imports, the matching algebra is proved. |
| 3 — 20.2.S1 | Spinor completion with independent phase φ; exact Bloch vector `(cos χ cos 2φ, cos χ sin 2φ, sin χ)`; reciprocal pair as component-amplitude odds | PROVED, conditional on I-Bloch — **with noted erratum in the text's intermediate definitions** | **Erratum (disclosed plainly):** the text's stated definitions `r_z = \|c₁\|² − \|c₀\|²` and `r_y = 2 Im(c₀*c̄₁)` do NOT yield the stated vector from the stated amplitudes c₀ = cos(π/4−χ/2), c₁ = sin(π/4−χ/2)e^{2iφ}: they give r_z = −sin χ (the text drops a minus: −cos(π/2−χ) = −sin χ) and r_y = −cos χ sin 2φ (sign of the imaginary part). Verified numerically: χ=π/3, φ=0.2 → definitions give (−0.866025, 0.46053, −0.194709) vs claimed (0.866025, 0.46053, 0.194709). **Correction:** under the standard Bloch convention r_z = \|c₀\|² − \|c₁\|² = cos(π/2−χ) = sin χ and r_x + i r_y = 2c₀*c₁ = sin(π/2−χ)e^{2iφ} = cos χ(cos 2φ + i sin 2φ), the stated vector `(cos χ cos 2φ, cos χ sin 2φ, sin χ)` is exact (same numeric point: 0.866025, 0.46053, 0.194709 ✓). So the *theorem* is proved; the proof text's two definition lines need the sign/conjugation fix. |
| 4 — 20.2.N2 | Native carrier `Ψ = H + iV` exactly `(i/8)(e^{2ix} + 3e^{−2ix})` (1:3 counter-rotating decomposition) | PROVED (exact algebra) | (i/8)[(cos 2x + i sin 2x) + 3(cos 2x − i sin 2x)] = (i/8)(4cos 2x − 2i sin 2x) = i cos 2x/2 + sin 2x/4 = Ψ from H = sin 2x/4, V = cos 2x/2. Re-derived exactly. The Class B embedding verdict is ASSERTED (see ASSERTED table). |
| 5 — 20.3.V1 | V−A helicity correspondence: after importing left-chiral orientation, `√(P_fav/P_wrong) = cxp` exactly | PROVED, conditional on I-VA + K1 | With imported weights P_fav = (1+β)/2, P_wrong = (1−β)/2: √(P_fav/P_wrong) = √((1+β)/(1−β)) = e^η = cxp by the K1 rapidity identity; likewise √(P_wrong/P_fav) = crx. Algebra re-derived; the SM orientation and weights are named imports. |
| 7 — 20.4.T1 | Two-angle necessity: a and χ generically independent; `a = χ` would force `β = Zα` | PROVED, conditional on I-Coulomb | sin a = Zα (Coulomb datum) and sin χ = β (kinematic datum) are two independently imported data; a = χ on the common branch would give Zα = β, collapsing the imported continuous beta spectrum to a charge-selected velocity — contradiction with the import. Logic read and sound; conditional on the named imports. |
| 8 — 20.4.T2 | `ξ = Zα/β = sin a / sin χ = u(1+q²)/(q(1+u²))` exactly | PROVED | ξ = sin a/sin χ by T1's definitions; L1 gives sin a = 2u/(1+u²), sin χ = 2q/(1+q²), so the ratio is u(1+q²)/(q(1+u²)). Re-derived exactly. Pure corollary of L1. |
| 9 — 20.4.T3 | Allowed beta phase space fully rational in (q, q₀) | PROVED, conditional on the stated allowed-approximation integrand (ST) + I-Coulomb | Standard weight ∝ pE(E₀−E)² (ST). Under the §1 chart: β = sin χ = 2q/(1+q²), E = m sec χ = m(1+q²)/(1−q²) (cos χ = (1−q²)/(1+q²), valid as χ/2 ∈ [0,π/4) so q ∈ [0,1)), p = Eβ = 2mq/(1−q²), all rational in q; endpoint E₀ = m sec χ₀ rational in q₀ = tan(χ₀/2). Substitution read and correct; conditional on the imported integrand form. |
| 11a — W1 correspondence | Jones vector `(cos(α/2), sin(α/2)e^{iφ})` has component ratio `e^{iφ} tan(α/2) = e^{iφ} sxp(α)` | PROVED, conditional on I-EM (Jones/ST import) | Exact by the definition sxp(α) = tan(α/2); phase φ and intensity scale are named imported coherency data. Stripping assessment ASSERTED (see table). |
| 11b — W2 rotation action | With 2V = cos 2x, 4H = sin 2x, the pair (2V, 4H) is a unit vector at angle 2x; the shift x ↦ x+δ acts as the SO(2) rotation by 2δ on it | PROVED | Norm cos²2x + sin²2x = 1; under the shift, (cos(2x+2δ), sin(2x+2δ)) = R(2δ)(cos 2x, sin 2x) by the standard angle-addition formulas (M0 background). Re-derived. The "accepted symmetry, not a new prediction" assessment is ASSERTED. |
| 11c — W3 carrier | Same carrier identity as N2 | PROVED (same proof as claim 4 — counted once) | Identical algebra to N2. The potential-first repair analysis (reproduces Maxwell rather than a new law) is ASSERTED. |
| 11e — W5 match | NP boost weights are reciprocal tetrad-gauge weights matching cxp/crx by the K1 identity | PROVED, conditional on I-EM (NP formalism ST) + K1 | Match is the K1 rapidity identity applied; read and sound. "Tetrad-gauge weights, not new observables" ASSERTED. |
| 11f — W6 map form | `[1:w:w²]` is the degree-two Veronese map CP¹ → CP² | PROVED (by definition), conditional on the book's imported I-EM specification of the null rank-one sector | Definitionally true; covers only the null rank-one sector per the imported specification. Algebraic geometry, no trig content. |
| 11g — W7 dimension count | Polarization CP¹ and propagation-direction CP¹ are independent state spaces; 2+2 = 4 real d.o.f. > 1, so one real scalar cannot supply both | PROVED | A CP¹ has 2 real d.o.f.; two independent factors have 4; one real scalar carries 1. Count read and correct. Not trig. |
| 11i — W9 arithmetic | At β = 1/2 the weak odds (1+β)/(1−β) = 3:1 exactly | PROVED | (3/2)/(1/2) = 3, arithmetic. The EM-sector q = 1/2 coincidence is numeric (noted in text). "Promotes no cross-sector law" ASSERTED. |
| 12 — 20.6.F1 | Firewall theorem: invertible representation change cannot create nonempty Δ_op | PROVED (from D-Δ_op) | R is defined to be a bijection on representation labels preserving every operational configuration's outcome probabilities, P_P(·|c) = P_0(·|c) for all c; then Δ_op = ∅ by the definition of Δ_op. Read and sound — essentially definitional unpacking; the load is carried by D-Δ_op. Not trig. |
| 13 — 20.6.F2 | Incompleteness is not novelty | PROVED (from D-Δ_op) | Class B is defined by Δ_op *undefined*; an open ansatz has no prediction set, hence no nonempty prediction-difference set, hence cannot falsify C0. Read and sound. Not trig. |
| 14 — 20.6.A1 | Every fully specified construction of §§1–5 lands Class A, Δ_op = ∅ | PROVED, conditional on the correspondence proofs 1, 3, 5, 7–9, 11 | Each correspondence (K1, S1, V1, T1–T3, W1–W9) is, by the proofs above, an exact invertible coordinate/parametrization change on its declared branch, conditional on the named imports; F1 then gives Δ_op = ∅ for each. Read and sound; inherits the conditionals. Not trig. |
| 16 — 20.6.C0 | Book closure: Δ_op = ∅ for every fully specified construction in Book 20; C0 retained as undefeated null hypothesis | PROVED, conditional theorem about the book's content | By A1 every fully specified construction has Δ_op = ∅; by A2/F2 the unfinished proposals are Class B, not Class-C counterexamples. Hence no Book-20 construction alters its reference theory's invariant predictions. Read and sound; the text is explicit that this is an audit-logic result *for the book's content*, not a universal no-go. Not trig. |

Supporting lemma used above (proved in §C, verified here):

- **L1 (half-angle rational identities, PROVED).** For t = tan(x/2) (x ≠ π mod 2π): `sin x = 2t/(1+t²)` and `tan(x/2) = sin x/(1+cos x)`. Proof re-derived: sin x = 2 sin(x/2)cos(x/2) = 2t cos²(x/2) = 2t/(1+t²) via cos²(x/2) = 1/(1+tan²(x/2)); and sin x/(1+cos x) = 2 sin(x/2)cos(x/2)/(2cos²(x/2)) = tan(x/2) via 1+cos x = 2cos²(x/2). Exact; no Euclid used.

## ASSERTED claims (10)

| Claim | Restatement | Scope | Notes |
|---|---|---|---|
| 2 — 20.1.N1 | Rank is not created by notation — many functions of one χ give one angle's worth of content | ASSERTED (retained obstruction) | Stated as a meta-claim, not derived; the one-generator obstruction itself belongs to unavailable Book 0 (B0). |
| 4b — bare-carrier Class B | Ψ as an unspecified physical embedding determines no unique observable (Class B) | ASSERTED (status declaration) | No complete contract or dynamics supplied for the bare carrier; the book's verdict retained. |
| 6 — 20.3.N2 | Chirality-orientation obstruction: the left-chiral orientation is imported, not derived | ASSERTED (retained obstruction) | Projection-only chirality selection declared Class B (unspecified). |
| 10 — 20.4.N3 | Complex-Gamma factor `exp(πξ)\|Γ(λ+iξ)\|²` lies outside finite rational primitive closure; Fermi function, matrix elements, radiative/finite-size corrections, endpoint energy, R imported | ASSERTED (retained obstruction + named imports) | No proof of the non-elementarity is given; imports named (I-Coulomb). |
| 11a-s — W1 stripping | Phase φ / intensity scale independent; no Projection-specific invariant from W1 | ASSERTED (book's audit verdict) | — |
| 11b-s — W2 assessment | Constant duality is an accepted symmetry, not a new prediction | ASSERTED (book's retained assessment) | — |
| 11c-s — W3 repair | Potential-first contract A ∝ H reproduces the standard wave after differentiation (reproduces Maxwell, not a new law); direct H↔E, V↔B assignment fails an ordinary traveling wave | ASSERTED (book's repair analysis; full differentiation check is the book's, I-EM) | — |
| 11d — W4 conclusion | Scalar-only local duality promotion is pure gauge; does not defeat C0 | ASSERTED (book's conclusion; the standard gauge argument is ST/I-EM) | — |
| 11e-s — W5 assessment | NP weights are tetrad-gauge weights, not new observables | ASSERTED | — |
| 11h — W8 | In 4D the vacuum Maxwell equations are conformally invariant on 2-forms, so a scalar conformal factor changes nothing in source-free propagation | ASSERTED (standard theorem ST, stated not proved here) | — |
| 11i-s — W9 assessment | The 3:1 coincidence promotes no cross-sector law | ASSERTED | — |
| §5 verdict — 20.5 no-invariant | No Projection-specific invariant survives the nine witnesses | ASSERTED (book's audit conclusion) | Terminal verdict of the redundancy analysis; the correspondence identities are proved but the stripping verdicts are retained. |
| 15 — 20.6.A2 | Bare-carrier embedding, Projection-only chirality selection, scalar-only local duality dynamics land Class B | ASSERTED (status declarations) | Correctly scoped book declarations; retained. |
| — no-Class-C | No fully specified Class-C model exists in Book 20's inventory | ASSERTED (book's audit verdict) | Used in C0 closure. |
| B0 | Book 0 primitive calculus and one-generator reduction (rewrite Book 0) | PROVED (2026-09-26 final exam, Exam Proof E2) | `book0_proof.md` is on disk and its primitive calculus is P1–P16 (all PROVED); the one-generator reduction is proved in cumulative_trig_proof.md Appendix X (every primitive is a rational function of z = srx by P1/P4; d/dx preserves ℝ(z) by P5). The pending premise is satisfied. |

(Count convention per the book: the W-stripping assessments fold into the
§5 no-invariant verdict; the distinct ASSERTED items are now 10: N1, §3
orientation obstruction, N3, bare-carrier Class B, W3 repair, W4
conclusion, W8 ST, §5 no-invariant verdict, A2 declarations, no-Class-C
declaration. B0 was the 11th and is PROVED as of the 2026-09-26 final exam.)

## CHECKED claims (0)

No numerical runs were performed or needed in this file (proof-over-sampling
rule); every PROVED item is analytic. The book's own earlier numeric work
is not re-run here.

## INCOMPLETE claims (0)

Nothing timed out or failed; all gaps are named ASSERTED premises.

## Candidate trigonometric principles (3)

### P-T1 — Half-angle rational identities (Weierstrass form)

- **Statement.** For t = tan(x/2), with x ≠ π (mod 2π) (so cos(x/2) ≠ 0):
  `sin x = 2t/(1+t²)` and `tan(x/2) = sin x/(1+cos x)`.
- **Domain.** x ∈ ℝ \ {π + 2πk}; t ∈ ℝ.
- **Proof.** sin x = 2 sin(x/2)cos(x/2) (double-angle, standard) =
  2 tan(x/2)·cos²(x/2) = 2t·cos²(x/2), and cos²(x/2) = 1/sec²(x/2) =
  1/(1+tan²(x/2)) = 1/(1+t²). Hence sin x = 2t/(1+t²). Also
  sin x/(1+cos x) = 2 sin(x/2)cos(x/2)/(2cos²(x/2)) = tan(x/2), using
  1+cos x = 2cos²(x/2). ∎
- **Scope.** PROVED (unconditional mathematical identity).
- **Source.** Book 20, §C Lemma L1; used in K1, T2, T3.
- **Euclid.** None used.
- **Note.** Almost certainly a duplicate of the registered Weierstrass
  principle (Book 2 P12/P17–P19 folded items); reported for later dedup.

### P-T2 — Rapidity–velocity hyperbolic identity

- **Statement.** Let η ∈ ℝ and β = tanh η ∈ (−1, 1). Then
  `e^η = √((1+β)/(1−β))`, `e^{−η} = √((1−β)/(1+β))`, and `e^η·e^{−η} = 1`.
- **Domain.** η ∈ ℝ (equivalently β ∈ (−1,1)).
- **Proof.** From exponential definitions,
  tanh η = (e^η − e^{−η})/(e^η + e^{−η}) = (e^{2η} − 1)/(e^{2η} + 1).
  Setting β = (e^{2η}−1)/(e^{2η}+1) and solving,
  β(e^{2η}+1) = e^{2η} − 1 ⟹ e^{2η}(1−β) = 1+β ⟹ e^{2η} = (1+β)/(1−β);
  taking the positive square root (e^η > 0) gives e^η = √((1+β)/(1−β)).
  Replacing η by −η gives e^{−η} = √((1−β)/(1+β)); the product is 1. ∎
- **Scope.** PROVED (unconditional as a mathematical identity; its
  physical reading — η as rapidity, β as velocity — is conditional on the
  I-SR import).
- **Source.** Book 20, §C proof of 20.1.K1 (also used in 20.3.V1).
- **Euclid.** None used.
- **Note.** The hyperbolic half-angle content: e^η is the exponential
  form of the velocity–rapidity relation, proved here directly from the
  exponential definition of tanh.

### P-T3 — Counter-rotating 1:3 phasor decomposition

- **Statement.** For x ∈ ℝ:
  `(i/8)(e^{2ix} + 3e^{−2ix}) = sin(2x)/4 + i·cos(2x)/2`.
- **Domain.** x ∈ ℝ.
- **Proof.** By Euler's formula,
  (i/8)(e^{2ix} + 3e^{−2ix})
  = (i/8)[(cos 2x + i sin 2x) + 3(cos 2x − i sin 2x)]
  = (i/8)(4cos 2x − 2i sin 2x)
  = i·cos 2x/2 + sin 2x/4. ∎
- **Scope.** PROVED (exact algebra; conditional only on the book's
  normalization definitions H = sin 2x/4, V = cos 2x/2).
- **Source.** Book 20, §C proof of 20.2.N2 (also the W3-carrier identity).
- **Euclid.** None used.
- **Note.** An exact algebraic consequence of Euler's formula (M0
  background); the 1:3 weighting of the two counter-rotating phasors is
  the book's content. Reported as a candidate; dedup may fold it into
  background.

## Claims not made into principles — reasons

- **Physics-correspondence claims (K1 full form, V1, T1, T3, W1, W5, W6,
  W8):** proved correspondences conditional on named physical imports
  (I-SR, I-Dirac, I-VA, I-Coulomb, I-EM); the *matching algebra* is proved
  but the claims are not free-standing trig identities — the trig content
  in them is L1/P-T1 or P-T2 applied to imported kinematics. Not forced
  into principles.
- **S1 Bloch vector:** a spherical parametrization application, not an
  identity; all trig used is standard double-angle / sin²−cos² background.
  (Erratum in the text's intermediate definitions documented in the PROVED
  table; the theorem itself is exact under standard Bloch conventions.)
- **T2 ξ formula:** pure corollary of L1 — no new trig content.
- **W2 duality rotation:** application of standard angle-addition (M0
  background); the SO(2) action statement is representation content, not a
  new identity.
- **W7 dimension count, W9 3:1 arithmetic:** counting/arithmetic, no trig
  content.
- **F1, F2, A1, C0:** definition-unpacking / audit-logic theorems about
  Δ_op and the book's inventory; no trig content.
- **All ASSERTED items (11):** manuscript claims, obstructions, status
  declarations, or named imports — not proved, hence not principles.
- **CHECKED/INCOMPLETE:** 0 / 0 — nothing to report.

## Counts

- Evaluated: **18 distinct PROVED claims** (19 inventory slots; N2's proof
  serves both §2 N2 and the W3-carrier identity, counted once; B0 added as
  a proved premise 2026-09-26), **0
  CHECKED**, **10 ASSERTED**, **0 INCOMPLETE**.
- Candidate trigonometric principles: **3** (P-T1 half-angle rational
  identities, P-T2 rapidity–velocity hyperbolic identity, P-T3 1:3
  counter-rotating phasor decomposition), all PROVED, none citing Euclid.
- Genuine erratum found and documented: two sign slips in the S1 proof
  text's stated r_z / r_y definitions (theorem itself exact under standard
  Bloch conventions; correction given in the claim-3 row).

status: complete
