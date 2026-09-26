# Book 9 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book9_proof.md`
(claim inventory B9.1a–B9.8, evaluated 2026-09-22 PDT).
**Rewrite page:** `~/workspace/r-theory-rewrite/book9/index.html` —
*Book 9 — Relativity and Gravitation: Conditional Reconstruction*
(principal theorems: conditional rapidity/rapidity-weight identities;
coframe-rank obstruction; fixed-generator pure gauge; reciprocal
half-weight hyperbola and defect identities; first-integral equivalence;
on-shell AN = 1 selection; boundary-term collapse; asserted imports and
manuscript assertions listed as not-derived).

Scope labels (Kit's, standing): PROVED / CHECKED / ASSERTED / INCOMPLETE.
For each claim: verdict, scope, folded-in? (Principle id or no + reason).

## Claim-by-claim table

| Claim | Verdict | Scope | Folded-in? | Notes |
|---|---|---|---|---|
| B9.1a Reciprocal-product identities s_rx·s_xp = c_xp·c_rx = 1 | PROVED (D0 trigonometry) | PROVED | No — trigonometric content already registered as Principle "1 (Book 0)" (srx·sxp = cxp·crx = 1; proved-from the Pythagorean identities csc²−cot² = 1, sec²−tan² = 1) | exact; proved directly from csc²−cot² = 1, sec²−tan² = 1 |
| B9.1b Lorentz-weight identities s_xp(χ) = pc/(E+mc²), … | PROVED conditional on D-RP | PROVED-conditional (D-RP ASSERTED) | No — correspondence between trig primitives and relativistic variables (p, E, m, c) under the asserted projection contract; not a pure trigonometric theorem | book's unstated β ≥ 0 branch made explicit in D-RP |
| B9.1c Boost weights c_xp = e^η, c_rx = e^{−η} with β = tanh η | PROVED conditional on D-RP | PROVED-conditional | No — same reason as B9.1b; hyperbolic/trig relation under the asserted contract | — |
| B9.1d Mass-shell factorization c_xp·c_rx = 1 reproduces mass shell | PROVED conditional on D-RP | PROVED-conditional | No — physics correspondence, conditional on D-RP | consistent with B9.1a independently |
| B9.2a Coframe-rank obstruction (rank ≤ 1 for single-variable coframes) | PROVED (D0 linear algebra) | PROVED | No — no trigonometric content | — |
| B9.2b Fixed-generator pure gauge (ω = K·dη ⇒ R = 0) | PROVED (D0 forms: d² = 0, wedge antisymmetry) | PROVED | No — differential geometry, no trig content | — |
| B9.2c Nonzero curvature requires additional structure | PROVED (contrapositive of B9.2a/B9.2b) | PROVED | No — logical contrapositive | — |
| B9.3a Half-weight hyperbola (uv = 1, E_r²−O_r² = 4) | PROVED (algebra) | PROVED | No — (u+v)²−(u−v)² = 4uv is pure algebra in defined symbols, not a trig identity | — |
| B9.3b Defect identities N = (1−q)/(1+q), r(1−N²) = 4a, N² = 1−4a/r | PROVED conditional on D-HR | PROVED-conditional | No — algebra in the chart variables N, q, r, a | r > 0, q > 0 |
| B9.3c Reciprocal-defect identity (1−q)/(1+q) = c_rx, q = s_xp(χ) | PROVED (conditional on D-RP branch + D-HR in the book file) | PROVED | **Yes — Principle 17**: the trigonometric core (1−q)/(1+q) = (1−sin χ)/cos χ with q = (1−cos χ)/sin χ on sin χ, cos χ > 0 is a pure exact identity; it stands with no physics contract | exact cross-multiplication; uses the Pythagorean identity (register row "1 (Book 0)" basis) |
| B9.4a Static reciprocal spherical metric | Imported | ASSERTED (D-GR(i) standard import) | No — imported, not trig | book line 90 |
| B9.4b Vacuum reduction r·f′ + f − 1 = 0 | Imported theorem | ASSERTED (D-GR(ii) import) | No — imported, not trig | — |
| B9.4c First-integral equivalence d[r(1−f)]/dr = 0 ⟺ r·f′ + f − 1 = 0 | PROVED (calculus) | PROVED | No — exact calculus equivalence, no trigonometric content | — |
| B9.4d Schwarzschild form f = N² = 1−4a/r = 1−2GM/(rc²) | PROVED conditional on D-CAL | PROVED-conditional; D-CAL (a = GM/(2c²)) ASSERTED (external, not derived) | No — physics calibration | book's conditional-theorem status sentence is accurate |
| B9.5a On-shell selection of AN = 1 in vacuum | CHECKED + ASSERTED import | CHECKED (SymPy 1.12 run 2026-09-22 PDT, script work/book9_sympy_95.py, identity G^r_r − G^t_t = 2(NA)′/(rNA³), residual exactly 0; Schwarzschild-vacuum tripwire passed) + D-GR(iii) ASSERTED | No — GR identity, not trigonometry | earlier Christoffel sign error in a draft script caught by the tripwire and corrected before the passing run (disclosed) |
| B9.5b Boundary-term collapse under A = N^{−1} before variation | CHECKED | CHECKED (same SymPy run, residual exactly 0; branch θ ∈ (0,π) declared) | No — variational methodology consequence | methodological consequence is the D-GR standard import (ASSERTED) |
| B9.6a Chart inversion q = (1−N)/(1+N) | PROVED (D-CH algebra) | PROVED | No — chart algebra, N ≠ −1 | — |
| B9.6b Radial-strain variable σ = ln(AN); σ = 0 ⟺ AN = 1 | PROVED conditional on B9.5a | PROVED-conditional | No — follows from D-CH + B9.5a | — |
| B9.6c Newtonian Poisson recovery in weak-field limit | Manuscript assertion, not verified | ASSERTED | No — no derivation shown in the book, not computed here; explicitly not earned | must not be inherited as earned upstream |
| B9.6d Static-dust obstruction (second coframe variable necessary) | Manuscript assertion, not verified | ASSERTED | No — no computation shown, not checked here; explicitly not earned | must not be inherited as earned upstream |
| B9.7a Metric compatibility does not imply zero torsion | Standard import | ASSERTED (D-GR(iv)) | No — not trig | — |
| B9.7b Palatini: independent connection variation gives T^a = 0 only with nondegenerate coframe and no spin current | Standard import | ASSERTED (D-GR(iv)) | No — not trig | book's "T6 Einstein–Cartan witness" cites T6, not a valid upstream dependency; not used as a premise |
| B9.8 Closure ledger consistency | Audit bookkeeping | ASSERTED | No — bookkeeping, not a theorem | book's certified/conditional/not-derived lists consistent with the audit; 9-item not-derived list honored |

## Counts

- Evaluated: 23
- Folded into the cumulative proof: 1 (Principle 17, from B9.3c)
- PROVED: 14 (B9.1a–d, B9.2a–c, B9.3a–c, B9.4c, B9.4d, B9.6a, B9.6b — several conditional on declared contracts D-RP / D-HR / D-CAL / D-CH)
- CHECKED: 2 (B9.5a, B9.5b — completed SymPy runs, residuals exactly 0)
- ASSERTED: 8 (B9.4a, B9.4b, D-CAL calibration, B9.6c, B9.6d, B9.7a, B9.7b, B9.8)
- INCOMPLETE: 0

## Notes for the campaign

- No proposition of Euclid's *Elements* is used deductively for Book 9;
  the Euclid Book 9 ledger records a null extension mapping (36
  number-theoretic propositions). Rewrite Book 9 is a conditional
  reconstruction on the modern substrate — recorded plainly in the
  cumulative document's Book 9 chapter, not dressed in invented Euclid
  citations.
- B9.1a's trigonometric content was already registered as Principle
  "1 (Book 0)"; it was verified but not re-folded.
- The register contains pre-existing numbering collisions (three rows
  numbered "1", two numbered "2"); Principle 17 was numbered one above
  the highest numeric id in use (16) and cites register rows by
  unambiguous labels. Flagged for the reevaluation stage, not renumbered.
- Dependency-labeling defects in the book (T4/T6/Towards-Unification/
  Reverse-Engineering-Einstein provenance; T6 Einstein–Cartan witness)
  are flagged in the table, not used as premises.

status: complete
