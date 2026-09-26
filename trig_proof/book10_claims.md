# Book 10 — claim-by-claim evaluation (2026-09-22)

**Source:** `~/workspace/euclid_work/books/book10_proof.md` (claim inventory
C1–C14 with proofs, verified 2026-09-22 by the book-10 worker) and
`~/workspace/r-theory-rewrite/book10/index.html` (*Book 10 — Quantum
Kinematics and the Measurement Boundary*, Volume II rewrite). Scope labels
(PROVED / CHECKED / ASSERTED / INCOMPLETE) are inherited from the book's
proof file and re-checked against the rewrite page. No claim was re-labeled
upward.

Folded-in principles live in the cumulative document
`~/workspace/euclid_work/trig_proof/cumulative_trig_proof.md`, registered as
1 (Book 10) – 4 (Book 10) (namespaced by book, following the Book 0
convention).

| # | Claim | Verdict | Scope | Folded-in? | Notes |
|---|---|---|---|---|---|
| C1 | 10.II.T1 — projective-rank obstruction: ℂP¹ needs 2 real local coordinates; the real meridian q = tan(x/2) supplies 1 | verified | PROVED | No — dimension/rank argument; no trig identity, lemma, or exact relation about trig functions/angles/circular measure | The book's SVD rank check (1 vs 2) is the numeric witness of the same rank fact |
| C2 | 10.II.C1 — q alone selects a 1-dim subfamily or silently supplies a phase rule | verified | PROVED | No — corollary of C1; no trig content | Imposing a phase rule is a contract, not a theorem |
| C3 | 10.III.P1 — free-Dirac import; ratio identities pc/(E+mc²) = √((E−mc²)/(E+mc²)) = tanh(α/2) | verified | import (ASSERTED premise); identities CHECKED by the book worker (500 random mass-shell pairs, worst err 4.3e-15) | Partially — exact algebraic content folded as 2 (Book 10) and 4 (Book 10); the Dirac theory itself stays a named import | 2 (Book 10) is the exact hyperbolic half-angle identity proved from definitions; 4 (Book 10) is the full ratio chain, PROVED-conditional on the asserted import |
| C4 | 10.III.PC1 — rapidity-contract identification q = sxp | declared, not derived | ASSERTED | No — a declared contract/axiom; no trig content | Every claim downstream of it (C5) is explicitly conditional on it |
| C5 | 10.III.T1 — exact free-spinor ratio correspondence, conditional on C3+C4 | verified | CHECKED (book: 300 samples, max err 1.5e-15) | Partially — identity content folded as 1 (Book 10); the spinor/rapidity physics reading stays conditional | 1 (Book 10) is the definitional half-angle inversion r = tan(x/2) ⟺ x = 2·arctan r |
| C6 | 10.IV.P1 — radial Dirac–Coulomb import; ground-sector constant ratio \|G/F\| = Zα/(1+γ) | verified | import (ASSERTED premise); constant-ratio content CHECKED on the analytic ground state (book: rel. spread 3.4e-16) | No — the inversion it uses is already 1 (Book 10); no new trig identity | The half-angle reading x = 2·arctan(\|G/F\|) ≈ 0.007297 rad is an application, not a new principle |
| C7 | 10.IV.T1 — ground-sector half-angle correspondence \|G/F\| = tan(x/2) | verified | CHECKED (conditional on C6; book: exact to 1e-14) | No — application of 1 (Book 10) to an imported constant | Not folded separately: no identity beyond the inversion |
| C8 | 10.IV.N1 — no universal constant half-angle for excited states (n=2, κ=−1) | as stated | ASSERTED | No — delimiting manuscript assertion, not a trig principle | Book worker did not re-run the radial-Dirac integrator; generic qualifier noted (circular n_r=0 states have constant but state-dependent ratios) |
| C9 | 10.V.T1 — Prüfer completion: F = A cos Θ, G = A sin Θ regular through nodes | standard ODE import | ASSERTED premise (import); reconstruction exact per the book's audit | Partially — polar-form identity folded as 3 (Book 10); the ODE regularity theory stays a standard import | 3 (Book 10): (F,G) = A(cos Θ, sin Θ), A = √(F²+G²) (Euclid 1.47), tan Θ = G/F where F ≠ 0, Θ defined through nodes |
| C10 | 10.VI.T1 — shared symplectic form ω_spin = 4·dF∧dG; du∧dv = 2·dF∧dG for (u,v) = (F−G, F+G) | verified | PROVED (exact Jacobian algebra; book's scope note: close to definitional) | No — wedge-form linear algebra, no trig content | Book explicitly disclaims quantum commutator/ℏ/quantization; so does this evaluation |
| C11 | 10.VII.P1 — left-chiral projector + V–A import | standard import | ASSERTED premise | No — named import used only for the comparison in C12; no trig content | |
| C12 | 10.VII.N1 — chirality not selected upstream | as stated | ASSERTED | No — structural observation about the dependency chain, not an impossibility proof | True of the chain as built; not a claim about what could exist |
| C13 | 10.VIII.N1 — representation does not imply measurement ontology | as stated | ASSERTED | No — structural observation about the chain, not an impossibility proof | Book's §8 scoping honored: no Born rule, collapse, QFT ontology, or spin-statistics derived |
| C14 | 10.IX closure; Δ_op(Book 10) = ∅ | as stated | ASSERTED | No — status bookkeeping | Consistent with C12/C13 |

## Explicitly excluded (stated plainly)

The meridian derivative identity dq/dx = 1/(2cos²(x/2)) and the meridian's
strict injectivity on (0, π) (D3/C1's calculus content) is genuine
trigonometry, but its proof route — differentiation — is neither Euclid's
*Elements* nor an earlier Principle, so it cannot be earned under this
campaign's dependency discipline. Evaluated here, not folded. Nothing was
forced in.

## Counts

- Evaluated: 14
- PROVED: 3 (C1, C2, C10)
- CHECKED: 4 (C3 identities, C5, C6 constant-ratio content, C7)
- ASSERTED: 7 (C4, C8, C9-import, C11-import, C12, C13, C14)
- INCOMPLETE: 0 — every check the book worker attempted ran to completion; no timeouts
- Folded into the cumulative proof: 4 principles — 1 (Book 10) half-angle
  inversion (PROVED), 2 (Book 10) hyperbolic half-angle (PROVED),
  3 (Book 10) Prüfer polar form (PROVED), 4 (Book 10) mass-shell ratio chain
  (PROVED-conditional on ASSERTED import I1)

## Euclid contact

Negative, recorded from the book's own audit: full-text search of rewrite
books 0–22 found zero relevant hits for incommensurable/apotome/bimedial/
medial — no R Theory claim extends any proposition of Euclid's Book 10
(10.1–10.115). The one genuine *Elements* citation used deductively in a
folded principle is Euclid 1.47 (Pythagoras), verified at
`~/workspace/euclid_work/ledger/book1_ledger.md` ("square on hypotenuse =
sum of squares on the legs"), for Principle 3 (Book 10).

## status: complete
