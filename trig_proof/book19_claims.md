# Book 19 — claim-by-claim evaluation (trig-cumulative campaign)

**Source:** `~/workspace/euclid_work/books/book19_proof.md` (claim inventory
T1–T21; 26 scope rows after splitting the book's own dual-verdict claims
T10, T17, T20 so each row carries exactly one label). Evaluated 2026-09-22.

**Verification method.** Read the full proof file: definitions D1–D7, the
inventory, all of Part III's proofs, and Part IV. The exact-algebra proofs
(T1, T2, T3, T5, T10a) were independently re-derived by hand and all check
out exactly; T3's full half-angle chain was verified step by step. The
internal-logic proofs (T6, T16, T17a, T20c) were checked for valid deduction
from their stated textual grounds — each is a genuine contradiction, not a
rhetorical one. CHECKED claims are accepted on the file's own completed
re-run report (`verify_book19.py`, exit 0, all checks passing, no timeouts)
and were **not** re-run, per the proof-over-sampling rule — except T4, whose
numerical value was spot-verified with an independent 50-digit computation
(see T4 notes): 638.782272…, matching the claimed 638.7823.

The file states explicitly, and it checks out: **no proposition of Euclid's
*Elements* is used deductively anywhere**; the substrate is the stipulated
standard import (ℝ, exact arithmetic, elementary trigonometry, finite
verifiable textual cross-checks). The Euclid ledgers contribute lineage only.
The campaign seed (double-angle identity, `seed_double_angle.md`) is recorded
as available and is *not invoked* by any Book 19 claim.

**Scope labels:** PROVED (exact mathematics, complete proof read step by
step), CHECKED (completed computation or textual cross-check), ASSERTED
(manuscript claim, audit verdict carried by reference, assumption,
convention), INCOMPLETE (failed, timed out, or unfinished — none here).

## PROVED claims (9)

| Claim | Restatement | Verdict | Folded in? | Notes |
|---|---|---|---|---|
| T1 | (√2)⁴ = 4, the propagator rapidity product | proof verified (re-derived: ((√2)²)² = 2² = 4) | no — exact integer/radical arithmetic, no trig content | — |
| T2 | (√2)⁸ = 16, the all-eight product | proof verified (re-derived: (T1)² = 16) | no — arithmetic, no trig content | — |
| T3 | crx(112.5°) = V_E exactly | proof verified (re-derived in full; see candidate principle §) | **yes — candidate principle** | the one genuine trig identity in the book |
| T5 | printed "638.7" is a 1-dp truncation of 638.7823…, not a rounding | proof verified (re-derived: ⌊6387.823⌋/10 = 638.7 vs rounding 638.8) | no — decimal-arithmetic bookkeeping | conditional on CHECKED T4 |
| T6 | IC-18: "the propagator rapidity product is 16" is incorrect as stated under v1's own terminology | deduction verified (the grounds — both phrases present in v1 — are machine-checked; the contradiction is genuine) | no — manuscript-terminology adjudication, not trig | PROVED as internal logic over CHECKED textual grounds |
| T10a | FLAG-A1 arithmetic: 4·(1/4) = 1 and (1/4)⁴ = 1/256 | proof verified (exact rational arithmetic) | no — arithmetic, no trig content | — |
| T16 | CONTR-1: Addendum item-6 "Theorem / Proof sketch" (EBEOEBEO) contradicts NO-GO B1 | deduction verified (same text asserts and denies theoremhood of the C8↔octant correspondence) | no — internal manuscript contradiction | grounds CHECKED |
| T17a | CONTR-2: Addendum item-8 states the DG bypass as fact, contradicting §19.3 ("not a proven evasion") + NO-GO B2 | deduction verified (stated-as-fact vs denied-as-proven is a genuine contradiction) | no — internal manuscript contradiction | grounds CHECKED |
| T20c | the unsigned certification report's "MASTER CERTIFICATION COMPLETE" is contradicted by the admitted open gates | deduction verified (certification completeness and admitted openness of the certified quantities are mutually exclusive) | no — internal logic, not trig | grounds CHECKED |

## CHECKED claims (6)

| Claim | Restatement | Verdict | Folded in? | Notes |
|---|---|---|---|---|
| T4 | V_E⁴ = 638.7823 | completed numerical check (re-run exit 0; max err 2.751e-05 vs tol 5e-05); independently spot-verified: 638.782272… | no — a decimal value of an algebraic number, not an identity | no closed-form simplification offered; stays CHECKED |
| T8 | Δ_op(Volume IV) = ∅ — no physical promotion established anywhere in Volume IV | audit-record accounting (108 assertions, 0 failed); a counting of the finite audit record, corroborated by the manuscript's own admissions | no — bookkeeping, not trig | not a mathematical theorem |
| T9 | Appendix B no-go ledger B1–B4 verified accurate against §§19.2–19.4 | verbatim textual cross-check, completed run | no — textual, not trig | the accuracy verdict is the audit's, carried by reference |
| T11a | FLAG-A2: "· Wick sign" bare bullet (the "(from archive)" qualifier dropped) | machine-checked against v1 text, completed run | no — textual, not trig | — |
| T20a | v3 text carries S_F = 0.48958371, N_1820 = 3, c_rest = 1.30555656; the certification report carries "MASTER CERTIFICATION COMPLETE" | machine-checked, completed run | no — textual grounds | — |
| T21 | figure data matches captions (points on y = x⁴, max err ≤ 8.882e-16; baseline y = 0 with five gates) | figure-data consistency check, completed run | no — the file declares figures illustrate verdicts, they are not proofs | — |

## ASSERTED claims (11)

| Claim | Restatement | Scope | Folded in? | Notes |
|---|---|---|---|---|
| T7 | "This factors out of S_F, preserving field-redefinition invariance" | ASSERTED (the audit's MA verdict; recorded, not proved) | no — manuscript sentence | three supporting textual facts are CHECKED; the classification is carried |
| T10b | FLAG-A1's per-contact 1/4 input | ASSERTED (archive-sourced MA; relation to the 1/2 coefficient OPEN) | no — input, not mathematics | the arithmetic T10a is sound; the input is not established |
| T11b | σ_Wick^(t) = −1 is not derived anywhere in v1 | ASSERTED (audit's negative-search verdict, not independently re-searched) | no — negative audit verdict | — |
| T12 | FLAG-A3: graded-connection rigidity λ = ±1 | ASSERTED (bridge-essay import, logged unaudited) | no — import | — |
| T13 | FLAG-A4: reduced-matrix-element firewall is a methodological principle (AX), not a theorem | ASSERTED (methodological rule) | no — rule, not mathematics | — |
| T14 | FLAG-A5: "ancestry criterion" EXACT row overstates vs the manuscript's own CONDITIONAL labels | ASSERTED (audit's textual verdict; §17.5.1/§17.5.2 grounds not re-checked this batch) | no — textual verdict | — |
| T15 | FLAG-A6–A8: soft CONDITIONAL labels do not overclaim | ASSERTED (recorded unaudited imports) | no — import | A8's "1/S = cosh w" is an ASSERTED import, not a proved hyperbolic identity |
| T17b | the E8(−24) host is MA per the Volume III ledger | ASSERTED (carried, not re-derived) | no — carried verdict | — |
| T18 | Appendix C duplicates the §17.18.8.2 skeleton, carrying IC-13…IC-16 by reference | ASSERTED (carried; conditional on Book-17 audit findings; duplication not re-verified this batch) | no — carried verdict | ST import discipline |
| T19 | the open gates (S_F, N_1820, ζ_parent, η_{−4}, c_ord/K_parent, P_54, …, role of 638.78, C3/C4 forcing) are all OPEN per the manuscript's own admissions | ASSERTED (manuscript's own admissions, confirmed) | no — status declaration | the book's honest content; none carries a numerical address |
| T20b | the v3 EXACT/CERTIFIED claims are not established under the v1-authority rule | ASSERTED (follows from the granted authority rule + ASSERTED open gates) | no — authority-rule consequence | the v1-as-sole-authority rule is a granted methodological stipulation |

## Counts

- Evaluated: **26** (9 PROVED, 6 CHECKED, 11 ASSERTED, 0 INCOMPLETE)
- Folded into the cumulative proof: **1**, PROVED (T3)
- Not folded: **25** — 24 with no trigonometric content (exact
  arithmetic: T1, T2, T5, T10a; internal manuscript logic: T6, T16, T17a,
  T20c; textual cross-checks: T4, T9, T11a, T20a, T21; audit-record
  accounting: T8; manuscript claims/imports/status declarations: T7, T10b,
  T11b, T12–T15, T17b, T18, T19, T20b)

status: complete

---

## Candidate trigonometric principles

### Principle: exact crx value at 5π/8 (Book 19, T3)

**Statement.** Let crx(x) := |sec x| − tan x (book notation; = |1/cos x| −
sin x / cos x) for cos x ≠ 0. Then

|sec(5π/8)| − tan(5π/8) = √(4 + 2√2) + 1 + √2

i.e. crx(112.5°) = V_E with V_E := √(4+2√2) + 1 + √2 (book D3).

**Domain.** x = 5π/8 exactly (cos x ≠ 0; cos(5π/8) < 0).

**Scope.** PROVED (complete analytic proof; verified by independent
re-derivation below).

**Source book claim.** Book 19, T3; rests on definitions D3 (V_E) and D4
(crx). No Euclid proposition is used as a premise (per the file's own
declaration, verified: the only ingredients are the supplementary-angle,
half-angle, and sign identities of the stipulated elementary-trigonometry
import).

**Proof.**
1. cos(5π/8) = −cos(3π/8) (supplementary-angle identity, 5π/8 = π − 3π/8).
   By the half-angle formula, cos²(3π/8) = (1 + cos(3π/4))/2 =
   (1 − √2/2)/2 = (2−√2)/4, and cos(3π/8) > 0 (3π/8 = 67.5° < 90°), so
   cos(3π/8) = √(2−√2)/2 and cos(5π/8) = −√(2−√2)/2 < 0.
2. Hence |1/cos(5π/8)| = 2/√(2−√2). Rationalizing,
   2/√(2−√2) = 2√(2+√2)/√((2−√2)(2+√2)) = 2√(2+√2)/√2 = √(4+2√2).
3. tan(5π/8) = −tan(3π/8) (supplementary-angle identity). With
   sin(3π/8) = √(2+√2)/2 (half-angle, sin > 0) and the cosine from step 1,
   tan(3π/8) = √(2+√2)/√(2−√2). Squaring:
   (2+√2)/(2−√2) = (2+√2)²/(4−2) = (6+4√2)/2 = 3+2√2 = (1+√2)²,
   and tan(3π/8) > 0, so tan(3π/8) = 1+√2, i.e. tan(5π/8) = −(1+√2).
4. Therefore crx(5π/8) = √(4+2√2) − (−(1+√2)) = √(4+2√2) + 1 + √2 = V_E. ∎

*Note for dedup:* the proof's internal steps (tan(3π/8) = 1+√2,
cos(3π/8) = √(2−√2)/2, sin(3π/8) = √(2+√2)/2) are standard exact
half-angle values, folded here as lemmas of this single principle rather
than separate principles.

---

## Claims not made into principles — reasons

- **T1, T2, T10a (PROVED, arithmetic):** exact real arithmetic
  ((√2)⁴ = 4, (√2)⁸ = 16, 4·(1/4) = 1, (1/4)⁴ = 1/256) — no
  trigonometric content. The "rapidity product" reading is manuscript
  terminology, not part of the proved identity.
- **T5 (PROVED):** decimal truncation/rounding bookkeeping — arithmetic,
  no trig content.
- **T6, T16, T17a, T20c (PROVED, internal logic):** genuine contradictions
  in the manuscript's own text, but they are manuscript-terminology
  adjudications, not identities about trig functions, angles, or measure.
- **T4 (CHECKED):** a decimal approximation (638.7823) of the algebraic
  number V_E⁴ — a value, not an identity; independently spot-verified
  (638.782272…).
- **T8, T9, T11a, T20a, T21 (CHECKED):** audit-record accounting and
  verbatim-text/figure-data cross-checks — no trig content.
- **T7, T10b, T11b, T12, T13, T14, T15, T17b, T18, T19, T20b (ASSERTED):**
  manuscript claims, unaudited imports, carried audit verdicts, and status
  declarations (including the open gates — above all the uncomputed value
  of S_F). None is proved or computed; none is a proved trig identity.
  (T15's "1/S = cosh w" is an unaudited bridge import — no proved
  hyperbolic identity exists in this book; per the rules, hyperbolic
  identities would have to be proved from exponential definitions, and
  none is.)
