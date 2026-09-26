# Book 5 Ledger — Euclid Extension Proof Campaign

**Book:** Elements Book 5 — Eudoxus's theory of proportion for magnitudes
(25 propositions, 5.1–5.25; 18 definitions; 2 corollaries).
**Euclid source:** `/home/hatch/workspace/euclid_work/text/book5.txt`
(Fitzpatrick/Heiberg English translation with Greek alongside; 1375 lines, read in full).
**Historical context:** `euclid-encyclopedia-article.html` (Encyclopedia.com);
the Fitzpatrick footnote to the book's title states the proportion theory "is
generally attributed to Eudoxus of Cnidus" and that its novel feature is
handling irrational magnitudes. The article itself situates Euclid after
Eudoxus and before Archimedes.
**Creative-deductive framing:** TESS-India "Developing creative thinking in
mathematics: trigonometry" — its operative theme: trigonometry "links concepts
about shape and space with other mathematical ideas such as ratio, deduction
and mathematical proof." R Theory's trig core (the srx/cxp primitive system,
the transfer circle p²+q² = 2, the reciprocal-odds atlas Ω, χ) is exactly a
ratio-native construction of this kind.
**R Theory side:** rewrite series `r-theory-rewrite/bookM/index.html`
(books 0–22 read for ratio/proportion content); audit records
`vol4/NOTATION_LEDGER.md` (v5) and `vol4/DEPENDENCY_CHAIN.md`.

## Book summary

Book 5 builds the entire classical theory of ratio and proportion for
*general* magnitudes (commensurable or not — this is the point of the
Eudoxean construction). The architecture:

1. **Definitions 1–4** set up the vocabulary: part, multiple, ratio (of
   same-kind magnitudes only), and "having a ratio" (the Archimedean
   condition: mα > β and nβ > α for some m, n).
2. **Definition 5** is the kernel: the Eudoxus criterion for "same ratio"
   (α:β :: γ:δ iff mα ≷ nβ exactly when mγ ≷ nδ, for all m, n) — valid for
   irrationals, no numbers required.
3. **Definitions 6–18** name the derived notions: proportional, greater
   ratio, three-term proportion, squared/cubed ratios, corresponding
   (antecedent/consequent) terms, and the six ratio transformations:
   alternate, inverse, composition, separation, conversion, ex aequali
   (ordered and perturbed).
4. **Propositions 5.1–5.6** are the arithmetic of integer multiples
   (mα+mβ = m(α+β), mα+nα = (m+n)α, m(nα) = (mn)α, subtraction forms).
5. **Propositions 5.7–5.15** are the order/identity theory of ratios
   (equal magnitudes share ratios; inversion corollary; greater-ratio
   ordering; transitivity 5.11; sums of proportionals 5.12).
6. **Propositions 5.16–5.19** are the ratio transformations: alternando,
   dividendo, componendo, and whole/part/remainder (with the conversion
   corollary). Note: 5.18's proof assumes without proof that a fourth
   proportional to three given magnitudes exists (Fitzpatrick footnote).
7. **Propositions 5.20–5.23** are the ex aequali family (ordered and
   perturbed, three magnitudes; transitivity across chains).
8. **Propositions 5.24–5.25** close the book: addition of proportionals and
   the greatest+least > middle-two inequality.

**The R Theory relationship, stated plainly.** R Theory does not re-derive
Book 5 from Euclid's definitions, and it does not take Euclid wholesale:
Book 4 §4.X states the "No-Euclid-wholesale theorem (4.X.H)" — the theory
imports only *declared* premises (P4.1 pre-metric substrate, P4.1-C SSS
congruence, P4.3 global Euclidean declaration; ledger row 232, status AA)
plus "standard mathematics declared at point of use". For ratio theory that
standard import is the complete ordered field ℝ. Consequences:

- Every Book 5 proposition, restricted to positive real magnitudes, is a
  theorem of ℝ's ordered-field axioms. R Theory's ratio content (reciprocal
  pairs, the Ω cross-layer identity, RP² cyclic ratios, block-scalar
  proportionality) lives inside ℝ, so Euclid 5 holds there *by import*, not
  by re-proof. The import itself is a stipulation (ASSERTED), never PROVED
  from Euclid in this campaign.
- Euclid's magnitude generality is strictly *weaker* than ℝ: Eudoxus needs
  Def 5.5's multiple-criterion because magnitudes needn't be numbers;
  in ℝ it collapses to quotient equality (α:β :: γ:δ ⟺ α/β = γ/δ), and R
  Theory always works with quotients (division), never with the
  multiple-exceed criterion.
- The Def 5.4 Archimedean condition is inherited from ℝ's Archimedean
  property (completeness); no R Theory text names or re-proves it.
- Where R Theory has a *specific* ratio identity that was verified by a
  completed computation, it is marked CHECKED with the computation
  described. Where the correspondence is only the ℝ import, it is marked
  ASSERTED (import-level stipulation). PROVED appears nowhere in the
  extension column: no deductive proof from Euclid's definitions/postulates
  was produced in this campaign. INCOMPLETE is used where the audit record
  does not establish the claim.

Proof dependencies below are extracted from the proof texts in
`book5.txt` (each proposition's bracketed citations, e.g. "[Prop. 5.3]",
"[Def. 5.5]").

## Inventory table

Legend — extension scope labels (Kit's four):
**PROVED** = deductive proof from Euclid's definitions/postulates/propositions
shown in this campaign (never occurs below — see note above);
**CHECKED** = verified by a completed computation (computation described);
**ASSERTED** = manuscript stipulation or new axiom, including the standard-import
stipulations; **INCOMPLETE** = not established. "—" in the extension column
means R Theory makes no corresponding claim; the Euclid content then reaches
R Theory only through the stipulated ℝ import.

### Definitions

| # | Statement (one line) | Euclid proof dependencies | R Theory extension | Scope |
|---|---|---|---|---|
| D1 | α is a *part* of β (α < β) iff β = mα for integer m | n/a (definition) | Integer-multiple language reused in trig doubling (double-angle rational formulas, quarter-turn τ_{π/2} of order 4, η = τ_{π/4} order 8 — Book 3 B46 exact) | ASSERTED (ℕ arithmetic via the standard import; no re-derivation from Euclid) |
| D2 | β is a *multiple* of α (α < β) iff α measures β | n/a | Same as D1 | ASSERTED (standard import) |
| D3 | A *ratio* is a size-relation of two magnitudes **of the same kind** | n/a | R Theory forms only same-kind ratios: λ/(1−λ) (dimensionless transfer coordinate, Book 0 §H); saw_r/saw_x = uxp/urx = cxp/srx (same-dimension channels, Book 0 T0.III.T8); m_1/m_2 (mass/mass, Book 14 Fig 1, ledger row 641, CLEAN); pc/(E+mc²) (energy/energy, Book 2 §2, ledger row 480, CLEAN); Y/X on RP² (Book 3 §3.VI). The same-kind discipline is honored operationally; the correspondence itself is stipulated, not proved | ASSERTED (the specific ratio identities are CHECKED separately, but D3-as-definition is not re-derived) |
| D4 | Magnitudes *have a ratio* iff multiples of each can exceed the other (Archimedean) | n/a | Inherited from ℝ's Archimedean property via the complete-ordered-field import; no R Theory text names or re-proves it | ASSERTED (import-level stipulation) |
| D5 | *Same ratio*: α:β :: γ:δ iff mα ≷ nβ exactly when mγ ≷ nδ, all m,n (Eudoxus criterion) | n/a | Direct instantiation: the cross-layer ratio Ω = λ/(1−λ) = saw_r/saw_x = uxp/urx = cxp/srx — "one projective coordinate in several presentations" (Book 0 §H, T0.III.T8). In ℝ the criterion collapses to quotient equality; the four-way identity was re-derived independently (13 symbolic + 9 numerical checks, all pass, per Book 0 §H) | CHECKED (the identity; the general criterion is the ℝ import, ASSERTED) |
| D6 | Magnitudes with the same ratio are *proportional* | n/a | Same content as D5 (Ω chain) | CHECKED (same re-derivation as D5) |
| D7 | *Greater ratio*: α:β > γ:δ iff some mα > nβ while mγ ≯ nδ | n/a | No direct R Theory use; ordering of ratios in the theory is analytic (e.g. 0 < λ < 1, sharp rate bounds 1/2 < λ′ ≤ 1/√2, Book 0 §H), not Eudoxean | ASSERTED (ℝ import only; no extension claim) |
| D8 | A proportion in three terms (α:β :: β:γ) is the smallest possible | n/a | No direct R Theory use (the λ = 1/2 midpoint inflection is a three-point structure but not a proportion in Euclid's sense) | ASSERTED (import only; no extension claim) |
| D9 | *Squared ratio*: if α:β :: β:γ then α:γ is the squared ratio of α:β | n/a | No direct R Theory use (double-angle rational formulas use ratio algebra but are not "squared ratios" in D9's sense) | ASSERTED (import only; no extension claim) |
| D10 | *Cubed ratio* (and so on) for continued proportion | n/a | No direct R Theory use | ASSERTED (import only; no extension claim) |
| D11 | *Corresponding magnitudes*: antecedent↔antecedent, consequent↔consequent | n/a | No direct R Theory use (the audit's "antecedent" language in Books 13/16 is about audit antecedents, not Euclid D11) | ASSERTED (import only; no extension claim) |
| D12 | *Alternate ratio*: from α:β :: γ:δ take α:γ :: β:δ | n/a | Projective chart changes in Book 3 §3.VI: RP² completeness "(a,b) ↦ [1:a:ab] — exact continuous rank 2" (page tag: checked proof; ledger rows 177–179 CLEAN); B43 u_XY·u_YZ·u_ZX = 1 exact cancellation, corroborated by 20,001-sample numerical check (residual ≤1e-12, verify_book3.py) | CHECKED (the chart-completeness/ratio-rearrangement claims; the alternando *principle* is ℝ arithmetic, ASSERTED) |
| D13 | *Inverse ratio*: from α:β take β:α | n/a | Direct instantiations: sxp = 1/srx, crx = 1/cxp (Book 0/2, V1: exact algebra (|csc|±cot)(|csc|∓cot) = csc²−cot² = 1, checked on grid residual ≤1e-9, tagged CP, verify_book0.py); Ωχ = 1 (Book 0 §H, part of the §H re-derivation) | CHECKED |
| D14 | *Composition*: from α:β take (α+β):β | n/a | Direct instantiation: Ω = U_λ − 1 = λ/(1−λ) with U_λ = 1/(1−λ) (Book 0 §H, part of the 13-symbolic/9-numeric re-derivation, all pass) | CHECKED |
| D15 | *Separation*: from α:β take (α−β):β | n/a | Direct instantiation: χ = R_λ − 1 = (1−λ)/λ with R_λ = 1/λ (Book 0 §H, same re-derivation) | CHECKED |
| D16 | *Conversion*: from α:β take α:(α−β) | n/a | No distinct R Theory claim (the conversion-shaped algebra appears only inside the §H ratio-identity family already counted) | ASSERTED (import only; no distinct extension claim) |
| D17 | *Ex aequali*: chained ratios α:β:γ :: δ:ε:ζ give α:γ :: δ:ζ | n/a | The T8 identity chain is ex-aequali reasoning across presentations (Ω = … = …); covered by the §H re-derivation | CHECKED (as part of the T8 chain re-derivation) |
| D18 | *Perturbed proportion*: α:β :: ε:ζ with β:γ :: δ:ε | n/a | No R Theory use | ASSERTED (import only; no extension claim) |

### Propositions

| # | Statement (one line) | Euclid proof dependencies | R Theory extension | Scope |
|---|---|---|---|---|
| 5.1 | mα + mβ + ⋯ = m(α + β + ⋯) | definitions only (counting parts) | No direct claim; used only as ordinary distributivity inside ℝ | ASSERTED (ℝ import; no extension claim) |
| 5.2 | mα + nα = (m+n)α | definitions only | Same as 5.1 | ASSERTED (import; no extension claim) |
| 5.3 | m(nα) = (mn)α | [5.2] | Same as 5.1 | ASSERTED (import; no extension claim) |
| 5.4 | α:β :: γ:δ ⇒ mα:nβ :: mγ:nδ (scaling preserves sameness of ratio) | [5.3], Def 5.5 | Homogeneous coordinates [X:Y:Z] = [λX:λY:λZ] — scale-invariance of ratios (Book 3 §3.VI, "homogeneous triples modulo scaling", page tag: standard imported theorem) | ASSERTED (standard projective-geometry import ST; no R Theory re-proof) |
| 5.5 | mα − mβ = m(α−β) | [5.1] | Same as 5.1 | ASSERTED (import; no extension claim) |
| 5.6 | mα − nα = (m−n)α | [5.2] | Same as 5.1 | ASSERTED (import; no extension claim) |
| 5.7 | Equal magnitudes have the same ratio to the same (and conversely) | Def 5.5 | The reciprocal-pair identities are the ratio form of this: sxp = 1/srx etc. depend on equal-magnitude cancellation (V1, exact algebra on grid, CP). The *principle* is not re-derived | CHECKED for the specific identities (V1); ASSERTED for the principle (import) |
| 5.7 cor. | Inversion: α:β :: γ:δ ⇒ β:α :: δ:γ | (from 5.7's proof) | Ωχ = 1; sxp = 1/srx (same V1/§H checks as D13) | CHECKED |
| 5.8 | Of unequal magnitudes, the greater has the greater ratio to the same (and the same has greater ratio to the lesser) | [5.1], Def 5.4 (existence of exceeding multiple), Def 5.7 | No direct R Theory claim | ASSERTED (import only; no extension claim) |
| 5.9 | Same ratio to the same ⇒ equal | [5.8] | No direct R Theory claim | ASSERTED (import only; no extension claim) |
| 5.10 | Greater ratio to the same ⇒ greater magnitude (and converse) | [5.7], [5.8] | No direct R Theory claim | ASSERTED (import only; no extension claim) |
| 5.11 | Transitivity: ratios same as a common ratio are same as each other | Def 5.5 | The T8 chain Ω = λ/(1−λ) = saw_r/saw_x = uxp/urx = cxp/srx asserts transitivity across four presentations; the equalities were re-derived (13 symbolic + 9 numerical, all pass) | CHECKED (the identity chain; logical transitivity of equality is not a theory claim) |
| 5.12 | α:α′ :: β:β′ :: γ:γ′ ⇒ α:α′ :: (α+β+γ):(α′+β′+γ′) (sums of proportionals) | [5.1], Def 5.5 | No direct claim — the UNA sum urx+uxp = 4/sin(2x) (Book 0 §3, CERTIFIED, V7 CP exact on grid) is a sum *identity*, not a proportion-of-sums | ASSERTED (import only; no extension claim) |
| 5.13 | α:β :: γ:δ and γ:δ > ε:ζ ⇒ α:β > ε:ζ | Def 5.5, Def 5.7 | No direct R Theory claim | ASSERTED (import only; no extension claim) |
| 5.14 | α:β :: γ:δ ⇒ order is preserved (α ≷ γ as β ≷ δ) | [5.8], [5.10] | No direct R Theory claim | ASSERTED (import only; no extension claim) |
| 5.15 | α:β :: mα:mβ (parts have the same ratio as similar multiples) | [5.7], [5.12] | Homogeneous-coordinate scale invariance [X:Y:Z] = [mX:mY:mZ] (Book 3 §3.VI, ST) — same content as 5.4's extension | ASSERTED (standard import; no re-proof) |
| 5.16 | Alternando: α:β :: γ:δ ⇒ α:γ :: β:δ | [5.15], [5.11], [5.14], Def 5.5 | RP² chart completeness (a,b) ↦ [1:a:ab] with u_XY·u_YZ·u_ZX = 1 (Book 3 §3.VI, page tag checked proof; B43 exact cancellation + 20,001-sample check residual ≤1e-12) — the ratio rearrangement Euclid 5.16 licenses | CHECKED |
| 5.17 | Dividendo: (α+β):β :: (γ+δ):δ ⇒ α:β :: γ:δ | [5.1], [5.2], Def 5.5 | χ = R_λ − 1 = (1−λ)/λ from R_λ = 1/λ (Book 0 §H, within the §H re-derivation) | CHECKED |
| 5.18 | Componendo: α:β :: γ:δ ⇒ (α+β):β :: (γ+δ):δ | [5.17], [5.11], [5.14]; **plus Euclid's own unproved assumption** (Fitzpatrick footnote): a fourth proportional to three given magnitudes always exists | Ω = U_λ − 1 = λ/(1−λ) from U_λ = 1/(1−λ) (Book 0 §H, within the §H re-derivation). Note: R Theory never needs Euclid's fourth-proportional assumption — ℝ division supplies it | CHECKED |
| 5.19 | Whole:whole :: part:part ⇒ remainder:remainder :: whole:whole | [5.16], [5.17] | No distinct R Theory proposition (the remainder-shaped algebra is inside the §H ratio family already counted under D15/5.17) | ASSERTED (import; no distinct extension claim) |
| 5.19 cor. | Conversion: α:β :: γ:δ ⇒ α:(α−β) :: γ:(γ−δ) | (from 5.19's proof) | No distinct R Theory claim | ASSERTED (import; no extension claim) |
| 5.20 | Ex aequali (ordered, 3 magnitudes): α:β :: δ:ε, β:γ :: ε:ζ ⇒ (α ≷ γ as δ ≷ ζ) | [5.8], [5.7 cor.], [5.13], [5.10] | No direct R Theory proposition | ASSERTED (import only; no extension claim) |
| 5.21 | Ex aequali (perturbed, 3 magnitudes): α:β :: ε:ζ, β:γ :: δ:ε ⇒ (α ≷ γ as δ ≷ ζ) | [5.8], [5.7 cor.], [5.13], [5.10] | No direct R Theory proposition | ASSERTED (import only; no extension claim) |
| 5.22 | Ex aequali transitivity: α:β :: δ:ε, β:γ :: ε:ζ ⇒ α:γ :: δ:ζ | [5.4], [5.20], Def 5.5 | The T8 chain's transitivity across presentations (same re-derivation as 5.11: 13 symbolic + 9 numerical, all pass) | CHECKED |
| 5.23 | Perturbed ex aequali transitivity: α:β :: ε:ζ, β:γ :: δ:ε ⇒ α:γ :: δ:ζ | [5.15], [5.11], [5.16], [5.21], Def 5.5 | No direct R Theory proposition (R Theory never uses perturbed proportions) | ASSERTED (import only; no extension claim) |
| 5.24 | α:β :: γ:δ and ε:β :: ζ:δ ⇒ (α+ε):β :: (γ+ζ):δ (sums of proportionals to a common consequent) | [5.7 cor.], [5.22], [5.18] | No direct proportion claim in R Theory (cf. 5.12 note on the UNA sum) | ASSERTED (import only; no extension claim) |
| 5.25 | If α:β :: γ:δ with α greatest and δ least, then α+δ > β+γ | [5.19], [5.14], plus an uncited "equals added to unequals" step | No R Theory counterpart | ASSERTED (import only; no extension claim) |

**Scope-label accounting for the extension column:** PROVED × 0, CHECKED × 9
(D5, D6, D12, D13, D14, D15, D17, 5.7/5.7-cor./5.11/5.16/5.17/5.18/5.22 — the
specific ratio identities), ASSERTED × all remaining items (the ℝ / ℕ /
projective-geometry import stipulations; several also carry page-level
ST tags), INCOMPLETE × 0. No extension claim was found to be missing or
failed — but most of Book 5 reaches R Theory only through the stipulated
import, not through re-proof. Nothing in R Theory contradicts any Book 5
proposition (all hold in ℝ⁺).

## New axioms/definitions the extension introduces beyond Euclid

These are the load-bearing assumptions. Euclid's Book 5 needs none of them;
R Theory does not derive them from Euclid.

1. **The ℝ substrate (strongest silent assumption).** R Theory's magnitudes
   are real numbers — a complete ordered field. This is strictly stronger
   than Eudoxus's axioms: it adds Dedekind completeness and makes division
   total, so Def 5.5's multiple-criterion collapses to quotient equality and
   Euclid's fourth-proportional gap (5.18 footnote) vanishes. Imported as
   "standard mathematics declared at point of use" (Book 4 §4.X, status AA
   per ledger row 232). **ASSERTED** — stipulated, never proved from Euclid.

2. **Axiom Zero — A0.1 and A0.2** (Book 5 §5.2; ledger rows 261–266, 326).
   (A0.1) There exists an independent isomorphic partner carrier U♯ with a
   declared block-compatible linear isomorphism ι: U → U♯ (ι(E) = E♯,
   ι(V) = V♯) and the sum W = U ⊕ U♯ is direct (dim_ℝ W = 10 — the Decadic
   Carrier Theorem, conditional on A0.1). (A0.2) No primitive U↔U♯ couplings:
   off-diagonal Hom(U, U♯) maps are mathematical, not active primitive
   couplings. Ledger status: **AXIOM — "Granted, not proved. First
   R-specific mathematical axiom in the revised chain."** Nothing in Euclid
   licenses an independent partner copy or a noncoupling declaration.

3. **P4.1, P4.1-C, P4.3** (Book 4 §§4.IV, 4.X; ledger row 232). Imported
   premises: pre-metric construction substrate (points, straight
   continuation, copied congruence unit r, equal-circle operation, continuous
   triangular filling); SSS admitted as a congruence principle; the global
   Euclidean declaration (global flatness and unique parallels). Status AA
   (assumption/axiom). **ASSERTED.**

4. **Gates A–H** (Book 4 preparation constitution; ledger row 233): ordering
   gates (rank before dimension, Flower before metric, metric after right
   angle, …, coordinate-novelty firewall). Status AA. **ASSERTED.**

5. **Book 1 constitutional stipulations.** Declaration 1.I.D1 (Book 0 corpus
   M0–M4 frozen as source boundary); the no-smuggling rules R1–R5 —
   "constitutional stipulations — declared, not derived" (page tag M);
   formal isolation T4. **ASSERTED.**

6. **Cophase** (Book 3 §3.I): the symmetric adjacency Δx ≡ ±π/2 (mod 2π) on
   𝕋_{2π}; page tag "assumption or axiom (definition)". **ASSERTED.**

7. **Projective ratio geometry** (Book 3 §3.VI): RP² as homogeneous triples
   modulo scaling with the affine cover U_X, U_Y, U_Z; P° = {XYZ ≠ 0}; the
   cyclic ratios u_IJ. Page tag: standard imported theorem (ST); ledger
   rows 177–179 CLEAN. **ASSERTED** as import; the specific identities
   (B43–B45) are CHECKED.

8. **The ratio-specific definitions** (all new, none Euclid's): the transfer
   coordinate λ = (1−p)/2 with 0 < λ < 1; the reciprocal-odds pair
   Ω = λ/(1−λ), χ = (1−λ)/λ with Ωχ = 1; the displaced-access hyperbolas
   χ = R_λ − 1, Ω = U_λ − 1; the UNA pair urx = srx − crx, uxp = cxp − sxp.
   All CLEAN in the ledger; the identities among them re-derived
   (13 symbolic + 9 numerical checks, all pass — Book 0 §H). **CHECKED.**

9. **Methodological (non-mathematical) declarations**, load-bearing for how
   the theory may be read: the **No-Euclid-wholesale theorem (4.X.H)** —
   Euclid is not adopted as a foundation; only declared imports enter
   (section 4.X is page-tagged MA); the **no-novelty-from-coordinate-change
   rule (4.X.I = Gate H)**; Book 5's **5.6 anti-circularity firewall**
   (Standard-Model/Spin(10)/E8 content may test but never justify Axiom
   Zero — page tag M). **ASSERTED** (manuscript assertions/declarations).

**What was NOT added:** Book 0's T0 layer (where all the ratio identities
live) is certified with "zero R-specific axioms" (book0/index.html §§H–I,
inheritance ledger). No new axiom of *proportion* was introduced: the
Eudoxean content R Theory uses is exactly the ℝ-shadow of Book 5, inherited
through the stipulated import (item 1).

## Gaps and non-verifications (disclosed per standing protocol)

- R Theory never re-proves any Book 5 proposition from Euclid's
  definitions; the "extension" is subsumption via the ℝ import. The import
  itself is a stipulation (ASSERTED), so the whole Book 5 correspondence
  rests on an unproved-in-this-campaign premise: that the declared
  "standard mathematics" includes the complete ordered field with its
  Archimedean property. Nothing in the audit derives ℝ from Euclid.
- The nine CHECKED items are specific identities (Ω four-way equality,
  reciprocal pairs, χ/Ω displaced hyperbolas, u_XY·u_YZ·u_ZX = 1, RP² chart
  completeness), not the general Book 5 theorems. Their computations:
  `validation/book0/verify_book0.py` (V1 exact algebra on grid, residual
  ≤1e-9; all 15 assertions pass), `validation/book3/verify_book3.py`
  (B43: 20,001 random samples on P°, residual ≤1e-12; B44/B45 exact), and
  the Book 0 §H independent re-derivation (13 symbolic + 9 numerical
  checks, all pass). No timeouts or failures in any of these runs per the
  audit record.
- Euclid-side gap inherited honestly: 5.18's proof assumes a fourth
  proportional exists without proof (Fitzpatrick footnote). R Theory does
  not need it (ℝ division), but the gap is in Euclid's own chain, not
  repaired by the extension.
- Defs 5.7–5.10, 5.13, 5.14, 5.20, 5.21, 5.23, 5.24, 5.25 and Props
  5.1–5.6, 5.8–5.10, 5.12–5.15, 5.19–5.21, 5.23–5.25 have **no direct R
  Theory proposition**; they are marked ASSERTED (import-level) with no
  extension claim. This is not a defect — it is the accurate scope: R
  Theory uses ratios, not the Eudoxean deductive chain.
- Historical note: the attribution of Book 5 to Eudoxus comes from the
  Fitzpatrick footnote in the source text itself; the encyclopedia article
  confirms only the chronological frame (Euclid after Eudoxus, before
  Archimedes) and was not independently verified beyond the passages read.
