# Book 8 claims — claim-by-claim evaluation (trig-cumulative campaign)

**Book:** R Theory Volume II, Book 8 — *Pre-Maxwell Geometry and the
Compact-Carrier Field Boundary* (not Euclid's *Elements* Book 8, which is
arithmetic — continued proportion — and has zero R Theory extension claims
touching any of its propositions 8.1–8.27, per `ledger/book8_ledger.md`).

**Sources:** `~/workspace/euclid_work/books/book8_proof.md` (claim inventory
E1–E21b with proofs, evaluated 2026-09-21/22); rewrite page
`~/workspace/r-theory-rewrite/book8/index.html` (principal-theorem table —
every row cross-checked against the inventory; nothing missing, nothing
extra); `~/workspace/euclid_work/ledger/book8_ledger.md` (read for the
Euclid-contact boundary).

**Method:** each claim restated, its proof verified (analytic proofs
re-derived by this worker; standard imports accepted under their ST label;
ASSERTED items reported at the book's scope with the gap named), scope
labeled, and the fold question answered: does the claim yield a genuine
trigonometric principle (an identity, lemma, or exact relation about trig
functions / angles / circular measure) provable from Euclid's *Elements*
(ledger-verified propositions) or from earlier Principles 0..P in the
cumulative document, in dependency order?

**Euclid contact:** none. The book's proof file states its own boundary:
no proposition of the *Elements* (Books 1–13, as inventoried in the
ledgers) is used deductively in any Book 8 derivation; the contact is
stylistic/methodological. This worker cites zero Euclid propositions.

## Claim-by-claim table

| # | Book claim (restated) | Verdict | Scope | Folded in? | Notes |
|---|---|---|---|---|---|
| E1 | 8.1.T1 — d²=0 on forms; B=dA is gauge invariant under A↦A+dχ; dB=0 | proof verified (L0) | PROVED | no — exterior calculus; no trig content | |
| E2 | 8.1.C1 (incl. 8.1.T2) — grad/curl/div in form language; ⋆₃²=+1 | standard dictionary, verified | PROVED (ST) | no — vector-calculus dictionary; no trig content | firewall retained: EM projection needs a separate contract |
| E3 | 8.2 — ⋆₄²=−1 on 2-forms, given the declared Lorentzian metric | computation verified on the coframe | PROVED (ST, conditional on D-η) | no — the "quarter-turn" is Hodge-star language on 2-forms, not trig functions/angles/circular measure | minus sign comes from the declared signature |
| E4 | 8.2 — constitutive boundary: G=λ⋆₄F is an identification, dG=J a sourced law; neither forced by exterior calculus | not proved — manuscript status discipline | ASSERTED | no | the book's own firewall, kept |
| E5 | 8.2.C1 — current closure dJ=0 from the admitted dG=J | proof verified (d²=0 on the admitted equation) | PROVED (conditional on E4's admission) | no — no trig content | |
| E6 | 8.3.N1, C1–C2 — {±1}⊂U(1) does not generate continuous local U(1); relabeling creates no Čech data, no connection | proof verified (definitional: 0-dimensional structure group) | PROVED | no — group-theoretic negative result; the e^{i0}, e^{iπ} packaging is incidental, not a trig principle yielded by the claim | |
| E7 | 8.4.L1, T1 — declared local phase redundancy forces the Abelian connection: A′=A+dχ, D²ψ=iqFψ, F=dA, dF=0 | proof verified (covariance forces the transformation law) | PROVED (conditional on D-Phase) | no — no trig content | |
| E8 | 8.5.L1 — exactly two quadratic 4-forms in F: F∧⋆F and F∧F | standard invariant theory, accepted | PROVED (ST) | no — no trig content | |
| E9 | 8.5.L2 — F∧F=d(A∧F): the theta term is a boundary term | proof verified (Leibniz + d²=0) | PROVED | no — exterior calculus; no trig content | |
| E10 | 8.5.T1 — Maxwell bulk uniqueness within D-Class; 8.5.C1 source coupling | not proved — class boundary declared | ASSERTED (conditional) | no | does not promote Maxwell theory into a carrier theorem |
| E11 | 8.6.T1 — two-derivative action class S=∫√−g[−½K(φ)(∇φ)²−V(φ)]; E–L equation K□φ+½K_,φ(∇φ)²−V_,φ=0; stress tensor as stated | proof verified (variation + integration by parts) | PROVED (conditional on D-φ) | no — no trig content | |
| E12a | 8.6.T2 — discrete symmetries force K, V to be functions of C=cos 4φ (harmonics cos 4nφ) | proof verified: π-periodicity → modes e^{i2nφ}; φ↦φ+π/2 kills odd n; φ↦−φ keeps cosines; cos(4nφ)=T_n(cos 4φ) | PROVED (conditional on P-Car symmetries) | **no** — the one claim with genuine trig content (Fourier mode selection + Chebyshev), but: (a) it is conditional on ASSERTED carrier symmetries (P-Car) — assertions cannot found principles; (b) its trig core rests on Fourier analysis and angle-addition theory not established in this document's dependency order (not in the seed, no earlier chapter, no ledger proposition; the book's own proof file uses no *Elements* proposition deductively). Folding it would break dependency order. | the honest trig core is real mathematics, but it is not yet provable from the cumulative document's allowed sources |
| E12b | 8.6.T2 carrier algebra C=X²−Y²=4V_car²−16H²=1−32H²=8V_car²−1 | rests on P-Car | ASSERTED | no | pending the Book 2/7 audits |
| E12c | 8.6.T3 — one-dimensional metric-flattening change of variables | not re-derived here | ASSERTED | no | book's audit verified it numerically; not re-derived |
| E13a | 8.6.N1 — symmetry classifies but does not select: exhibited inequivalent symmetric vacua V₊, V₋ | proof verified (the exhibited pair respects the symmetries with distinct vacuum sets) | PROVED | no — meta-claim about non-selection; the trig functions are examples, no new identity/lemma yielded | |
| E13b | 8.6.C1 — round-metric selection principle | further declaration | ASSERTED | no | |
| E14 | 8.7.T1, T2 — free scalar field, Noether current; winding ∮w∈ℤ | standard, accepted | PROVED (ST) | no — standard import; winding is topological (degree of S¹→S¹), not a trig identity/lemma about functions/angles | |
| E15 | 8.7.T3 — carrier wave identity □Z=2iZ□φ−4Z(dφ)² | proof verified (dZ=2iZ·dφ, Leibniz, d⋆d) | PROVED | no — complex-phasor exterior calculus (Z=e^{2iφ}); not a real trig-function identity/lemma | |
| E16 | 8.7.T4 — null-carrier sector (five items) | not re-derived here | ASSERTED | no | reported at the book's scope |
| E17a | 8.7A.T1, T2 — sphere identity S₁²+S₂²+S₃²=1; coherency ceiling \|c\|²≤λ(1−λ)=\|H\| | proof verified (positivity → det≥0; Bloch algebra sums to 1) | PROVED (conditional on D-2S; the λ(1−λ)=\|H\| identification is P-Car ASSERTED) | no — Bloch-sphere algebra; no trig functions | |
| E17b | 8.7A.T3 — Fubini–Study coefficients g_λλ=1/(4\|H\|), g_φφ=\|H\| | not re-derived here | ASSERTED | no | textual slip on the book page recorded (displayed ds² line omits ⟨dψ\|dψ⟩; proof text and metric correct) |
| E18 | 8.7A.N1 — one-scalar projective-curvature obstruction: dλ∧dφ=0 | proof verified (dx∧dx=0) | PROVED | no — exterior algebra; no trig content | |
| E19 | 8.7B.N1 — direct E/B quadrature no-go: E²−c²B²=−E₀²cos 4x≢0 | proof verified (sin²2x−cos²2x=−cos 4x, direct computation) | PROVED | no — the claim is a negative result about field quadrature; the double-angle step is incidental computational machinery, not the claim's content, and double-angle is not established in this document's dependency order | book page labels it a numerical check; the analytic computation is exact, so PROVED (proof over sampling) |
| E20 | 8.7B.T1 — circular-polarization witness: all five identities hold for both helicity signs | proof verified (E², (cB)², E·B=0, E×B=(E₀²/c)k̂ all re-derived) | PROVED (conditional on D-EM) | no — vector identities about E, B under an EM import contract; C²+S²=1 is trivial, no new trig principle | compatibility witness, not a derivation of EM |
| E21a | 8.7B.3 — A=g(x)dx ⇒ F=0 | proof verified (dx∧dx=0) | PROVED | no — exterior algebra; no trig content | |
| E21b | 8.7B.3 — A=Σf_a(x)θ^a ⇒ F∧F=0 | not re-derived here | ASSERTED | no | book's audit verified numerically on test configurations |

## Per-book counts

- Inventory claims evaluated: **26** (E1–E21b)
- PROVED: **18** (E1, E2, E3, E5, E6, E7, E8, E9, E11, E12a, E13a, E14, E15, E17a, E18, E19, E20, E21a) — all analytic, complete in the text; no numerical sampling run (proof-over-sampling rule). Several are conditional on declared premises (E3 on D-η; E5 on the admitted dG=J; E7 on D-Phase; E11 on D-φ; E12a on P-Car; E14 on declared premises; E17a on D-2S; E20 on D-EM) — the conditions are stated, never hidden.
- CHECKED: **0** — no numeric runs needed or performed.
- ASSERTED (inventory): **8** (E4, E10, E12b, E12c, E13b, E16, E17b, E21b). With the book's declared premises (D1–D6, D-EM, P-Car, Book 8→9 dependency lock) the full book accounting is **18 PROVED / 0 CHECKED / 17 ASSERTED / 0 INCOMPLETE**, matching `book8_proof.md` §F.
- INCOMPLETE: **0** — nothing timed out or failed; gaps are named ASSERTED premises, not unfinished work.
- Folded into the cumulative trigonometric proof: **0**.

## Fold decision

Book 8 contributes **no new Principles**. Its eighteen proved claims are
established mathematics (several conditional on declared premises) but
concern exterior calculus, gauge structure, invariant theory, scalar field
theory, and Bloch-sphere algebra — none is an identity, lemma, or exact
relation about trigonometric functions, angles, or circular measure that
is provable from the cumulative document's allowed sources in dependency
order. The single claim with genuine trigonometric content (E12a: the
cos 4nφ harmonic restriction and Chebyshev relation) is conditional on
ASSERTED carrier symmetries and its trig core rests on Fourier/angle-addition
theory not yet established from the seed, earlier chapters, or any
ledger-verified *Elements* proposition — folding it would break dependency
order. Per the standing rule, nothing was forced: forcing a non-foldable
claim in would misrepresent both the book and the proof.

Highest Principle number added by Book 8: none (P0 was the highest at this
worker's read time; sibling book workers have since appended their own
chapters and principles to the register — see the concurrency note in the
cumulative document's Book 8 chapter). The principles register gains
nothing from Book 8.

## status: complete
