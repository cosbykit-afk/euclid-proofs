# Book 17 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book17_proof.md` (claim inventory
P1–P21, C1–C4, A1–A7, I1–I7 with proofs) and rewrite page
`~/workspace/r-theory-rewrite/book17/index.html` (*Book 17 — The Discrete
Octant*, §§17.1–17.8). Evaluated 2026-09-22.

**Verification method.** All 21 proofs read in full and independently
re-derived where algebraic. Re-derived exactly: P1 (regrouping from the
seed lemmas), P2, P3 (both identities), P4 (Q1 factorization, plus the Q2
and Q4 branch factorizations checked directly), P5 (octants 1 and 2 by
t = tan(x/2) substitution, octant 3 at its midpoint), P6 (all eight
3-bit codes recomputed), P7 (periodicity, the four midpoint points, the
√10/8 radius, the boundary values), P8, P9 (all ladder values including
the full +,−,−,+,+,−,−,+ sign pattern), P10 (numerator/denominator
algebra plus all four quadrant branches), P11 (period, minimality, zeros),
P12, P13, P14 (shift-by-4), P15 (conditional arithmetic), P16, P17 (the
nested-radical identity step by step), P18, P19, P20 (dimension
arithmetic; the Casimir decomposition itself cited from the CP proof).
The book page's reported NC/CP/V checks (C1–C4) are cited as CHECKED, not
re-run, per the proof-over-sampling rule. The page's own audit exhibits
I4–I7 (IC-8..IC-11) are reproduced as reported, not re-derived — the
book worker states this boundary explicitly and it is honored here.

**Scope labels:** PROVED (exact mathematics, complete), CHECKED
(completed numeric run), ASSERTED (manuscript claim/assumption/convention),
INCOMPLETE (failed, timed out, or unfinished — all seven here are the
book page's own exhibited defects or blocked inputs, reproduced as its
verified audit).

## PROVED claims (21)

| Claim | Restatement | Verdict | Scope | Folded in? | Notes |
|---|---|---|---|---|---|
| P1 | harmonic carrier: srx−1/srx = 2cot x, cxp−1/cxp = 2tan x, urx+uxp = 4/sin(2x), sin(2x)/4 = 1/(urx+uxp) | proof verified (re-derived regrouping via seed Lemmas 1–2) | PROVED | no — subsumed by P0 (seed) and register P9 | — |
| P2 | imbalance: K₂/(2D₂) = cos(2x)/2 | proof verified (re-derived: common factor 2/(sin x cos x) cancels) | PROVED | no — definition-unfolding of D3, no new content | — |
| P3 | elliptic carrier: V_R² + 4H² = 1/4; D₂² − K₂² = 16 | proof verified (re-derived both, using sin(2x) = 2 sin x cos x) | PROVED | no — first identity is register P9; second is D3 substitution | — |
| P4 | octant ordering: srx − cxp = (cos x − sin x)(1 + cos x + sin x)/(sin x cos x); per-octant sign charts | Q1 factorization re-derived; Q2 and Q4 branch factorizations checked directly (same pattern with per-branch factors) | PROVED | no — sign-analysis tool for the primitive difference, not an identity about angles or circular measure | — |
| P5 | active pair: on each open octant exactly the two named active primitives exceed 1 | octants 1, 2 re-derived by t = tan(x/2) substitution (srx = 1/t, cxp = (1+t)/(1−t)); octant 3 verified at its midpoint (5π/8); page's CP t-proof covers the remaining branches | PROVED | no — finite case analysis, no identity | — |
| P6 | three-bit code: eight codes distinct, cover ℤ₂³ | all eight codes recomputed: (odd,+,+), (even,−,+), (odd,−,−), (even,+,−), (odd,+,−), (even,−,−), (odd,−,+), (even,+,+) — all distinct | PROVED | no — finite combinatorics | — |
| P7 | 2:1 map: π-periodicity of (V_R, H); midpoints land on (±√2/4, ±√2/8) concyclic at √10/8; boundary points (±1/2, 0), (0, ±1/4) | proof verified (re-derived in full) | PROVED | **yes — P17** | the book proof file's "for k even … for k odd the same four points recur" is loose wording (even k gives two of the four points, odd k the other two); the chapter's "exactly four points, each taken twice" is the correct statement and was verified |
| P8 | IC-1 correction: ε = sgn(sin 2x) is deck-invariant (records ellipse halves, not the sheet) | proof verified (re-derived: ε(x+π) = ε(x); ε = +1 on H > 0, −1 on H < 0, 0 on the axes) | PROVED | **folded with P17** | — |
| P9 | rapidity ladder: sinh w₀ = 1, cosh w₀ = √2 for w₀ = ln(1+√2); cot(π/8) = 1+√2, cot(3π/8) = √2−1; sign pattern +,−,−,+,+,−,−,+; dw/dx = −2/sin(2x) | proof verified (re-derived all parts; the sign pattern tracks ln\|cot x_k\| with \|cot\| ∈ {1+√2, √2−1}) | PROVED | **yes — P18** | Euclid citation (Prop. 10.9, diagonal–side incommensurability) is bookkeeping for √2's irrationality, verified in book10_ledger.md, not a logical premise — kept |
| P10 | Flatwave identity: 1/urx + 1/uxp = (srx+cxp)/(srx·cxp − 1) = sgn(sin 2x), all four quadrants | proof verified (re-derived the (A+B)/(AB−1) algebra and all four quadrant branches: +1, −1, +1, −1) | PROVED | no — already registered as Book 0 P6 | the Books 2–3 name-collision identification is exact algebra given the Books 2–3 definition, not re-established here — honest boundary, kept |
| P11 | paired footprint: cos(4(x+π)) = cos(4x); minimal period π/2 (π/4 not a period); zeros at all eight octant midpoints | proof verified (re-derived; minimality argument is terse but the standard cos(4T) = 1 ⟹ 4T = 2πn argument closes it exactly) | PROVED | **yes — P19** | — |
| P12 | IC-4 correction: cos(4x) takes ±1 (never 0) at octant boundaries; zeros are at midpoints | proof verified (re-derived: cos(4·π/4) = cos π = −1, cos(4·3π/4) = cos 3π = −1) | PROVED | **folded inside P19** | the manuscript's "vanishes at the octant boundaries" is false as stated — correction stands |
| P13 | E contacts are the decay-octant midpoints, strictly inside their octants | checked (finite: 22.5°, 112.5°, 202.5°, 292.5° lie in the open octants (0°,45°), (90°,135°), (180°,225°), (270°,315°)) | PROVED | no — finite check | — |
| P14 | five footprints' x→x+π evenness; C8 shift-by-4 = kernel map | proof verified (re-derived: adding π shifts octant indices by exactly 4; E/B/O sets preserved as sets) | PROVED | **folded inside P19** | the "even under the code group" clause is excluded per A2 — honest, kept |
| P15 | S_F arithmetic: ⟨Q_F, aT + R_⊥⟩ = 3a; ⟨Q_F, R_⊥⟩ = 0, given ‖T‖² = 5/2 and ⟨T, R_⊥⟩ = 0 | proof verified (re-derived, explicitly conditional on the stated premises) | PROVED (conditional) | no — linear algebra, no trig content | ‖T‖² = 5/2 is established in P16; ⟨T, R_⊥⟩ = 0 is a given premise |
| P16 | T traceless, ‖T‖² = 5/2, ‖Q_F‖² = 18/5; (1/4)⁴ = 1/256 | proof verified (re-derived: tr T = 1+1−8/4 = 0; ‖T‖² = 1+1+8/16 = 5/2) | PROVED | no — exact arithmetic | — |
| P17 | srx(π/8) = √(4+2√2) + 1 + √2 exactly | proof verified (re-derived the full nested-radical identity: √(4+2√2) = √(2+√2)+√(2−√2) and (1+√2)√(2−√2) = √(2+√2), then the product check) | PROVED | **yes — P20** | the page tags it SC; here the analytic proof is complete — no numerical sampling was run on top of it |
| P18 | conversion-chain closure: S_F = 3a, a = (6/5)c, c = 5S_F/18 consistent; −(1/256)(√10/6) = −√10/1536 | proof verified (re-derived: a = (6/5)(5S_F/18) = S_F/3) | PROVED | no — rational algebra; the physical content of the prefactor is excluded (A4) | — |
| P19 | bound arithmetic: (1/256)(18/5)(4) = 9/160 = 0.05625 | proof verified (72/1280 = 9/160) | PROVED | no — arithmetic; whether it bounds anything is excluded (A5) | — |
| P20 | IC-6/IC-7 corrections: the 120 lives in Λ²(128) = 120 ⊕ 8008, not Sym²(128); the SO(16) adjoint has dim 120; the 135 is Sym²₀(16) | verified (dimension arithmetic: 128·127/2 = 8128 = 120+8008; 16·15/2 = 120; 16·17/2−1 = 135; the Sym²(128) = 1⊕1820⊕6435 decomposition cited from the CP proof, which shows no 120 summand) | PROVED | no — representation theory, no trig content | — |
| P21 | §17.8 octant→ellipse table, √10/8 concyclicity, boundary points consistent with carrier formulas | checked (each entry is a direct substitution into the proved P3/P7 formulas; the page's V-checks corroborate) | PROVED | no — read-off of established formulas | CHECKED corroboration only, not sampling on top of a proof |

## ASSERTED claims (7)

| Claim | Restatement | Scope | Folded in? | Notes |
|---|---|---|---|---|
| A1 | C8 ↔ octant correspondence as a *theorem* | ASSERTED (manuscript assertion) | no | disputed inside v1 itself (CONTR-1 on the Book 19 page) — recorded honestly |
| A2 | footprints "even under the code group" | ASSERTED (unverifiable as stated: the code group is never defined as an x-map) | no | correctly excluded from P14 |
| A3 | charge-matching substitution y₂ ∼ η₋₄·ζ_parent·n̂₅₄ with η₋₄ = η₀cos(4x) ansatz | ASSERTED (manuscript assertion) | no | — |
| A4 | physical content of the −(√10/1536) prefactor | ASSERTED (manuscript assertion) | no | the arithmetic is proved (P18); the physics is not |
| A5 | form of the §17.7.4 heuristic bound (the number 9/160 is proved; that it bounds is open) | ASSERTED/OPEN | no | — |
| A6 | §17.5 gate admissions: S_F, the 1820 projector, downstream contraction inputs declared open | ASSERTED (the manuscript's own admissions, confirmed) | no | — |
| A7 | role of 638.78 in the Clifford contraction ("remains to be determined", §17.3.5) | ASSERTED/OPEN | no | — |

## CHECKED claims (4)

The book page reports its own completed checks (NC/CP/V); per the
proof-over-sampling rule these were **not re-run here**; they are cited,
not folded as principles (a numerical check of a proved identity is not a
new theorem).

| Claim | What it checks | Scope | Folded in? |
|---|---|---|---|
| C1 | V_E⁴ ≈ 638.7823 | CHECKED (page NC) | no — checks the proved P17 exact value; sanity: V_E ≈ 5.0273, V_E⁴ ≈ 638.78 |
| C2 | all four E-contact dominant values coincide | CHECKED (page NC) | no |
| C3 | C8 word pattern (E,B,E,O)×2 internal consistency; exactly two O's | CHECKED (page CP; the two-O's count is read off D7) | no |
| C4 | §17.8 table against the proved carrier formulas | CHECKED (page V-checks) | no — corroborates proved P21 |

## INCOMPLETE claims (7)

All seven are the book page's own exhibited defects and blocked inputs,
reproduced as its verified audit (the book worker explicitly did not
re-derive the IC exhibits; that boundary is honored here).

| Claim | Restatement | Scope | Notes |
|---|---|---|---|
| I1 | Frobenius norms ⟨Γ,Γ⟩_F = 128, ⟨Γ,PKPK⟩_F = 64 | INCOMPLETE | IN-1: γᵢ, B, Π₋ conventions open in v1 |
| I2 | explicit 1820 projector | INCOMPLETE | IN-2: blocked at P₆₄₃₅ |
| I3 | numerical value of S_F | INCOMPLETE | IN-3: OPEN |
| I4 | skeleton Step 1: NullSpace[Transpose[{traceVector}]] yields {} as written; intended reading gives 8255-dim, not 1820 | INCOMPLETE | page's audit finding IC-8, reproduced not re-derived |
| I5 | skeleton Steps 2–3: 128⁴×128⁴ Kronecker product dimensionally incompatible with an 1820×8256 basis | INCOMPLETE | page's audit finding IC-9, reproduced not re-derived |
| I6 | skeleton Steps 6–7: −(1/256) double-counted | INCOMPLETE | page's audit finding IC-10, reproduced not re-derived |
| I7 | skeleton Step 5: wickSign never assigned | INCOMPLETE | page's audit finding IC-11, reproduced not re-derived |

## Euclid citations (verified)

- **Def. 1.15** (circle: "plane figure with all radii from an interior
  point equal") — verified in `~/workspace/euclid_work/ledger/book1_ledger.md`;
  the chapter cites it as the classical definition for Principle 17's
  concyclicity, explicitly *not* as a deductive premise. Kept as cited.
- **Prop. 10.9** (commensurability in length ⟺ squares in the ratio of a
  square number to a square number) — verified in
  `~/workspace/euclid_work/ledger/book10_ledger.md`; the chapter cites it
  for Principle 18 as the classical grounding of √2's irrationality
  (2/1 is not a square-number ratio, so the diagonal is incommensurable
  with the side), explicitly bookkeeping, not a logical dependency. Kept
  as cited.

## Counts

- Evaluated: **39** (21 PROVED, 4 CHECKED, 7 ASSERTED, 7 INCOMPLETE)
- Folded into the cumulative proof: **4** (P17–P20), all PROVED:
  P17 (carrier-ellipse 2:1 cover, from P7 with P8 as corollary),
  P18 (rapidity derivative + √2 ladder, from P9),
  P19 (cos 4x period/zero structure, from P11 with P12 and P14),
  P20 (exact srx(π/8), from P17-book-claim P17)
- Not folded: **35** — 8 already registered or subsumed (P1, P2, P3, P10,
  P18-algebra, P19-arithmetic are register/subsumed/definition-level;
  P4, P5, P6, P13, P15, P16, P20-book-claim, P21 are sign-analysis tools,
  finite case checks, non-trigonometric algebra, or read-offs), 4 CHECKED,
  7 ASSERTED, 7 INCOMPLETE

status: complete
