# Book 11 — claim-by-claim evaluation for the trig-cumulative campaign

**Sources read:** `~/workspace/euclid_work/books/book11_proof.md` (full claim
inventory + proofs; counts PROVED 13 · CHECKED 6 · ASSERTED 7 · INCOMPLETE 4),
`~/workspace/r-theory-rewrite/book11/index.html` (principal theorems; Part I–III;
the page's numbered theorems and 15 MANUSCRIPT ASSERTION labels map onto the
inventory), `~/workspace/euclid_work/trig_proof/cumulative_trig_proof.md`
(highest Principle before this book: **P0**, the seed), and
`~/workspace/euclid_work/ledger/book1_ledger.md` (Common Notions inventoried;
No-Euclid-wholesale boundary 4.X.H).

**Fold rule:** a claim is folded into the cumulative proof only if it yields a
genuine trigonometric principle — an identity, lemma, or exact relation about
trigonometric functions, angles, or circular measure — provable from stated
definitions and/or earlier Principles 0..P, nothing used before it is proved.
Claims with no honest trigonometric content are evaluated with their scope
label and the reason is stated plainly.

## Claim table

| Claim | Verdict | Scope | Folded in? | Notes |
|---|---|---|---|---|
| T1 — UᵀJU = (det U)J; J-preserving ⟺ det U = 1; +Hermitian ⟺ SU(2) (11.PG.T1) | proved as stated | PROVED | No — matrix identity; no trig-function/angle/circular-measure content | proof in book11_proof.md §C |
| T2 — XᵀJ + JX = (tr X)J; infinitesimal algebra = su(2), real dim 3 (11.PG.III) | proved as stated | PROVED | No — Lie-algebra identity; no trig content | — |
| T3 — pure-gauge A = −dUU⁻¹ gives F = dA + A∧A = 0 (11.PG.N1) | proved as stated | PROVED | No — Maurer–Cartan differential identity; no trig content | — |
| T4 — JŪJ⁻¹ = U for U ∈ SU(2) (11.PG.XII) | proved as stated | PROVED | No — SU(2) mirror-automorphism lemma; no trig content | — |
| T5 — unique traceless block phase, 2a+3b=0 forces (a,b) ∝ (1/2,−1/3) (11.III.C) | proved by citation of book6 P12 (conditional on AX-6.2) | PROVED | No — linear-algebra fact; no trig content | cited, not re-verified here |
| T6 — Φ(A,B,z) = (z³A, z⁻²B): S(U(2)×U(3)) ≅ [SU(2)×SU(3)×U(1)]/ℤ₆ (11.III.B) | proved as stated | PROVED | No — group isomorphism; the six roots z⁶=1 are a finite-group kernel fact, not a trigonometric identity | — |
| T7 — primitive integral cocharacter X = i(3I₂⊕−2I₃); weights 0,6,1,−4,2,−3; Y₀ = X/6; primitivity from gcd(3,2)=1 (11.IX.T1, C1) | proved as stated | PROVED | No — number-theory/cocharacter fact; no trig content | — |
| T8 — S₊ = Λ^even W: six blocks 1⊕1⊕6⊕3⊕3⊕2 = 16 with Y₀-weights (11.IV.T1, T2) | proved as stated | PROVED | No — representation branching combinatorics; no trig content | uses ST Λ²V ≅ V̄ (imported, not proved) |
| T9 — A_SU(3)³ = A_SU(3)²Y = A_SU(2)²Y = A_Y³ = A_grav²Y = 0, exact (11.VI.T2–T4) | proved, conditional on AX-C4 | PROVED | No — exact rational arithmetic; no trig content | anomaly *interpretation* additionally needs imported Weyl rules (AX-C4) |
| T10 — vacuum neutrality forces c = 1/6, Q = T₃ + Y₀; full 16-charge pattern (11.IX.T2, T3) | proved, conditional on AX-C1, AX-C2 | PROVED | No — charge arithmetic; no trig content | physical identification stays conditional per the page |
| T11 — cxp(χ) = e^η = √[(1+β)/(1−β)], crx = e^{−η}, cxp·crx = 1 (11.PG.IX) | proved as an identity; the helicity-weight formula itself is ST (imported) | PROVED | **Yes — Principle 1** (helicity reciprocal identity) | the book's P_L↔P_R favored/suppressed reading rests on the imported ST Dirac formula and is not folded |
| T12 — 10_ℂ dims 2+3+2+3 = 10 with conjugate pairing; 4 doublets; g-blindness (11.VIII.T1, 11.VI.T5, 11.VII.T2–T3) | proved as stated | PROVED | No — representation branching; no trig content | branching isomorphism independently CHECKED (K3) |
| T13 — no-go forms: chirality nonselection, singlet-algebra firewall, generation blindness, T7 vs Axiom Zero (11.PG.N3, 11.I.B, 11.II.F1, 11.VII.N1, 11.VI.T7) | proved, conditional on A6 | PROVED | No — elementary-logic no-go forms; no trig content | — |
| K1 — helicity-odds plotted-curve agreement, max err 1.12e-10 < 1e-9 (V1) | completed numeric run 2026-09-22 | CHECKED | No — curve agreement, not a proved identity | supports the ST formula's application in T11 |
| K2 — Λ²V ≅ V* character check, 300 random SU(3), max err 1.3e-15 (V14) | completed numeric run | CHECKED | No — check of an imported isomorphism; no trig identity proved | supports T8's ST use |
| K3 — 10_ℂ branching dims + Sym²(16)=136=10+126, Asym=120, 3⊗3̄, 3⊗3⊗3 (V18) | completed numeric/combinatorial check | CHECKED | No — dimension checks; no trig identity proved | supports T12/T13 |
| K4 — U(2) ≅ (SU(2)×U(1))/ℤ₂ surjectivity/kernel, 6.9e-16 (V10) | completed numeric run | CHECKED | No — group-theoretic check; no trig identity proved | 11.PG.VIII, ST |
| K5 — ℤ₆ kernel acts trivially on all six blocks; quotient descent (V20) | completed check | CHECKED | No — kernel triviality; no trig identity proved | supports T6 |
| K6 — six-block table = one SM generation + neutral singlet under the comparison contract (V25) | completed check, contract-conditional | CHECKED | No — contract-conditional identification; no trig identity proved | 11.V.T1 |
| A1 — physical comparison contract 11.V.A | page's own assumption | ASSERTED | No — physics identification, not a trig claim | AX-C1 |
| A2 — doublet scalar + nonzero vacuum 11.IX.P1 | page's own assumption | ASSERTED | No — field extension, not a trig claim | AX-C2 |
| A3 — imported standard physics bundle (Dirac+P_L, 4D Lorentzian spin base, Weyl anomaly rules, YM candidate-class uniqueness, color projection, Dai–Freed/bordism) | imported/declared | ASSERTED | No — assumption bundle | AX-C4 |
| A4 — closure theorem 11.X.T1 + Δ_op(Book 11) = ∅ | page's own MANUSCRIPT ASSERTION label | ASSERTED | No — scope-labeled summary, not a derivation | kept as the page labels it |
| A5 — fermionic-ontology firewall 11.IV.G | page's own label | ASSERTED | No — ontology separation claim | — |
| A6 — mirror-symmetric premise data for no-go theorems | manuscript-supplied | ASSERTED | No — premise data, not a trig claim | AX-C5 |
| A7 — physical debts ledger (scalar ontology, VEV, masses, couplings, θ_W, EW scale, replication, flavor, RG flow) | explicitly open | ASSERTED (as open) | No — unresolved by the page's own accounting | — |
| I1 — forward book map Books 12–19 | roadmap only, no per-book entries | INCOMPLETE | No — nothing to prove | — |
| I2 — Book 12 "later Casimir correspondence" forward reference | claim about a book not in this corpus | INCOMPLETE | No — recorded without endorsement | — |
| I3 — unresolved physical debts | not derived here | INCOMPLETE | No — see A7 | — |
| I4 — Euclid XI 11.1–11.39 | no counterpart by the No-Euclid-wholesale boundary | INCOMPLETE (boundary) | No — the Elements are deliberately not imported (4.X.H) | book11_proof.md §H |

## Counts

- Evaluated: **30** (T1–T13, K1–K6, A1–A7, I1–I4)
- Folded into the cumulative proof: **1** (Principle 1, PROVED)
- PROVED: 13 · CHECKED: 6 · ASSERTED: 7 · INCOMPLETE: 4

## New principles from Book 11

- **Principle 1 (Book 11) (PROVED)** — helicity reciprocal identity: for
  β ∈ (−1,1), β = tanh η, χ with sin χ = β: √((1+β)/(1−β)) = e^η and
  cxp(χ)·crx(χ) = e^η·e^{−η} = 1. Proved from definitions (exponential
  series, tanh, positive square root, sin) plus an inline-proved
  additive-law lemma e^a·e^b = e^{a+b} (Cauchy product + binomial theorem).
  Uses no earlier principle and no Euclid proposition; respects the
  No-Euclid-wholesale boundary. Full proof in the Book 11 chapter of
  `cumulative_trig_proof.md`.
- Register label is **| 1 (Book 11) |** (suffixed per the campaign's
  concurrent-worker convention, matching Book 0's and Book 10's rows) to
  avoid collision with other bare-numbered rows.
- Notation: Book 11's cxp(χ)/crx(χ) are the helicity pair of §11.PG.IX,
  distinct from the campaign's canonical primitives cxp/crx (Book 0,
  Principle 1) — same names, different objects; no double-counting.

## New axioms beyond Euclid + seed + earlier books

None new for the folded principle. (Book 11's own AX-C1/C2/C4/C5 and
inherited AX-6.2/AX-6.4 are recorded in book11_proof.md §G; they are not
used by Principle 1.)

## Notes

- Book 11's proved core is representation theory and exact algebra over
  the 2+3 carrier; its honest trigonometric yield is exactly one exact
  identity (T11). Nothing was forced in.
- The Book 11 chapter was appended to `cumulative_trig_proof.md` without
  renumbering or rewriting earlier material; the principles register was
  extended with Principle 1. Cumulative principle count is now 2 (P0, P1).
- No timeouts, no failures, no sampling on top of proved results.

**status: complete**
