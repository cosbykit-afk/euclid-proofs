# Book 19 — The UV Boundary: Extension Proofs

**Rewrite book:** `r-theory-rewrite/book19/index.html` — *Book 19 — The UV Boundary*
(rewrite of Book 19 and Appendices A–C of R Theory — Volume IV v1, the audit authority).
**Campaign:** Euclid book-proofs (R Theory as an extension of Euclid's work).
**Date:** 2026-09-22.
**Seed:** `../books/seed_double_angle.md` (Kit's double-angle secant/cosecant identity, PROVED) —
available, not invoked: Book 19 contains no claim that needs it. It is recorded here as
available, not used.

## Scope discipline

- **PROVED** = exact mathematics or verifiable internal logic shown below
  (definitions first, dependency order, nothing used before it is established).
- **CHECKED** = a completed computation or completed textual cross-check that ran to
  completion (the re-run below exited 0, all checks passing, no timeouts).
- **ASSERTED** = manuscript claim, audit verdict carried by reference, or assumption —
  granted/recorded, not proved here.
- **INCOMPLETE** = failed, timed out, or unfinished. None below.
- **ST** = standard imported theorem, stated not proved here (used once: T18's
  dependency on Book-17 audit findings is carried, not re-derived).

## On Euclid citations and the No-Euclid-wholesale boundary

No proposition of Euclid's *Elements* is used deductively in these proofs. The
mathematics below is exact real arithmetic, elementary trigonometry, and
verifiable internal logic of the manuscript record (claims of the form "the
text both asserts X and denies X," checked against the local v1 copy
`~/workspace/vol4/volume_iv_v1_raw.txt`). It rests on the **stipulated standard
import** (the complete ordered field ℝ and elementary calculus-free
trigonometry) — the same import discipline recorded in the campaign's earlier
proof files. The "Euclid-style" content of this file is the *method* —
definitions first, dependency order, nothing used before it is established —
not a derivation from Euclid's postulates. **No wholesale inheritance of the
Elements is claimed:** this is a synthetic-constructive stratum on a declared
substrate.

The campaign seed (double-angle identity) is not invoked; the Elements ledgers
(`~/workspace/euclid_work/ledger/book1_ledger.md`..`book13_ledger.md`) contribute
only lineage, not premises.

---

# Part I — Definitions (in dependency order)

- **D1.** *Rapidity product (propagator).* The book's declared value for the four
  decay octants is (√2)⁴ = 4 (Addendum 4.A line 3542's established reading;
  §17.3.4, §17.7.2, §17.18.9.3).
- **D2.** *All-eight product.* (√2)⁸ = 16 — v1's own terminology distinguishes
  this *total* product from the propagator product (D1); the two are not
  interchangeable labels (verified verbatim: v1 carries both "cosh(wᵢ) = 4" and
  "the total rapidity product is 16, not 4").
- **D3.** *E-contact dominant value.* V_E := √(4 + 2√2) + 1 + √2, a positive real
  number. Its fourth power V_E⁴ is the "product over the four decay octants" of
  line 3542.
- **D4.** *crx.* crx(x) := |1/cos x| − sin x / cos x, for cos x ≠ 0. The book
  asserts crx(112.5°) = V_E.
- **D5.** *Δ_op(Volume IV).* The set of established physical promotions
  (parameter determinations promoted to physical content) anywhere in Volume IV.
- **D6.** *Open gate.* A quantity the manuscript itself admits has no numerical
  address (S_F, N_1820, ζ_parent, η_{−4}, c_ord/K_parent, …).
- **D7.** *Audit record.* The chunk-5 audit of Book 19 + Appendices A–C
  (108 assertions, 0 failed; `~/workspace/vol4/book19/LEDGER_19.md`) and the
  completed figure/quotation verification run
  (`~/workspace/r-theory-rewrite/validation/book19/verify_book19.py`), re-run
  in this batch: exit 0, all checks passing, no timeouts, worst measured error
  2.751e-05 (V10, V_E⁴ vs 638.7823).

---

# Part II — Claim inventory (scope-labeled)

| # | Claim | Scope |
|---|-------|-------|
| T1 | (√2)⁴ = 4, the propagator rapidity product | PROVED |
| T2 | (√2)⁸ = 16, the all-eight product | PROVED |
| T3 | crx(112.5°) = V_E exactly | PROVED |
| T4 | V_E⁴ = 638.7823 | CHECKED |
| T5 | Line-3542 "638.78": value right; printed "638.7" is a truncation (1 dp), not a rounding | PROVED (conditional on T4) |
| T6 | IC-18: "the propagator rapidity product is 16" is incorrect as stated | PROVED (internal logic) |
| T7 | "This factors out of S_F, preserving field-redefinition invariance": unsupported, conflicting | ASSERTED (grounds CHECKED: V13/V14/V15) |
| T8 | Δ_op(Volume IV) = ∅ — no physical promotion established anywhere in Volume IV | CHECKED (audit-record accounting) |
| T9 | Appendix B no-go ledger B1–B4 verified accurate against §§19.2–19.4 | CHECKED |
| T10 | FLAG-A1: arithmetic 4·(1/4) = 1 and (1/4)⁴ = 1/256 is exact; the per-contact 1/4 input is archive-sourced | PROVED (arithmetic) / ASSERTED (input) |
| T11a | FLAG-A2: Appendix A lists "· Wick sign" as a bare bullet — the "(from archive)" qualifier was dropped | CHECKED |
| T11b | σ_Wick^(t) = −1 is not derived anywhere in v1 | ASSERTED (audit's negative-search verdict) |
| T12 | FLAG-A3: graded-connection rigidity λ = ±1 — bridge-essay §3.2, logged unaudited | ASSERTED |
| T13 | FLAG-A4: the reduced-matrix-element firewall is a methodological principle (AX), not a theorem | ASSERTED |
| T14 | FLAG-A5: the "ancestry criterion" EXACT row overstates — contradicts the manuscript's own CONDITIONAL labels (§17.5.1, §17.5.2, premise §19.2 OPEN) | ASSERTED (audit's textual verdict) |
| T15 | FLAG-A6…A8: soft CONDITIONAL labels do not overclaim | ASSERTED (recorded) |
| T16 | CONTR-1: Addendum item-6 "Theorem / Proof sketch" (EBEOEBEO unique cyclic word) contradicts NO-GO B1 | PROVED (internal logic) |
| T17 | CONTR-2: Addendum item-8 states the DG bypass as fact, contradicting §19.3 ("not a proven evasion") and NO-GO B2; the E8(−24) host is MA per the Volume III ledger | PROVED (contradiction) / ASSERTED (host) |
| T18 | Appendix C duplicates the §17.18.8.2 skeleton and thereby carries IC-13…IC-16 by reference | ASSERTED (carried; conditional on Book-17 audit findings) |
| T19 | Open gates: S_F, N_1820, ζ_parent, η_{−4}, c_ord/K_parent, P_54 location, the N_1820 1/2→1/4 gap, P_6435, the explicit 1820 projector, the Frobenius norms, the role of 638.78, the C3/C4 forcing question — all OPEN per the manuscript's own admissions | ASSERTED |
| T20 | The v3 draft's EXACT/CERTIFIED claims (S_F = 0.48958371, N_1820 = 3, c_rest = 1.30555656) are not established under the v1-authority rule; the unsigned certification report's "MASTER CERTIFICATION COMPLETE" is contradicted by the open gates | ASSERTED (authority rule) / PROVED (contradiction, grounds CHECKED) |
| T21 | Figure data (the three tension points on y = x⁴; the empty baseline with five open gates) matches the captions; figures illustrate audit verdicts, they are not the proofs | CHECKED / recorded |

---

# Part III — Proofs in dependency order

## Proof of T1. (√2)⁴ = 4

(√2)⁴ = ((√2)²)² = 2² = 4, exact integer arithmetic. ∎ (Scope: PROVED.)

## Proof of T2. (√2)⁸ = 16

(√2)⁸ = ((√2)⁴)² = 4² = 16 by T1, exact. ∎ (Scope: PROVED.)

## Proof of T3. crx(5π/8) = V_E

Let x = 5π/8 = 112.5°. cos(5π/8) = −cos(3π/8) = −√(2−√2)/2 < 0, so
|1/cos x| = 1/|cos x| = 2/√(2−√2).

Rationalize: 2/√(2−√2) = 2√(2+√2)/√((2−√2)(2+√2)) = 2√(2+√2)/√2 = √(4+2√2).

sin x / cos x = tan(5π/8) = −tan(3π/8), and tan(3π/8) = √(2+√2)/√(2−√2).
Now (√(2+√2)/√(2−√2))² = (2+√2)/(2−√2) = ((2+√2)/√2)² = 3 + 2√2 = (1+√2)²,
and √(2+√2)/√(2−√2) > 0, so it equals 1 + √2. Hence sin x / cos x = −(1+√2).

Therefore crx(5π/8) = √(4+2√2) − (−(1+√2)) = √(4+2√2) + 1 + √2 = V_E (D3). ∎
(Scope: PROVED — exact algebra; no computation involved. This is the book's
"(√2)⁴ = 4, (√2)⁸ = 16, and crx(112.5°) = V_E identities are exact" claim,
recast with the algebra shown.)

## T4. V_E⁴ = 638.7823 (CHECKED)

No closed-form simplification of the fourth power is offered; the value is a
completed numerical check. The figure-verification run recomputed V_E⁴ and
matched 638.7823 with max error 2.751e-05 (tolerance 5e-05); the re-run in this
batch reproduced the pass (exit 0, no timeouts). ∎ (Scope: CHECKED — a completed
run, never a proof. V_E = 5.027339492125848… was used.)

## Proof of T5. "638.7" is a truncation, not a rounding

Given the checked value V_E⁴ = 638.7823… (T4): truncating to one decimal place
gives ⌊638.7823·10⌋/10 = ⌊6387.823⌋/10 = 638.7, while rounding to one decimal
gives 638.8 (the .0823 fraction rounds up). Hence the manuscript's printed
"638.7" is a truncation, not a rounding — the page's claim is correct, and
"638.78" (two decimals) is faithful to the computed value. ∎ (Scope: PROVED,
conditional on T4. The three tension values 4 / 16 / 638.78 are pairwise
distinct by inspection of T1, T2, T4.)

## Proof of T6. IC-18 — "the propagator rapidity product is 16" is incorrect as stated

*Grounds (machine-checked against the v1 text, re-run passing).* The v1 text
contains both "cosh(wᵢ) = 4" (the propagator cosh product, §17.3.4/§17.7.2/
§17.18.9.3) and "the total rapidity product is 16, not 4" — v1's own
terminology distinguishes the propagator product (D1: 4, by T1) from the total
(all-eight) product (D2: 16, by T2).

*Logic.* Under v1's own terminology, "propagator rapidity product" denotes the
quantity established as 4. Asserting it to be 16 mislabels the all-eight
product as the propagator product; the charitable all-eight reading is
foreclosed by the book's own explicit distinction ("is 16, not 4" attaches 16
to the *total* product). Therefore the line-3542 sentence is incorrect as
stated: IC-18. ∎ (Scope: PROVED as internal logic of the manuscript record —
the truth of the contradiction rests on the checked textual grounds, not on
new mathematics. The book's verdict "IC" is preserved exactly.)

## T7. "Factors out of S_F" — recorded, not proved

The manuscript sentence "This factors out of S_F, preserving
field-redefinition invariance" is classified MA (unsupported) by the audit.
Supporting grounds are machine-verified (re-run passing): the exact phrase
"field-redefinition invariance" occurs exactly once in v1 and is never defined
or proved; §17.3.5's honest "its role in the Clifford contraction remains to
be determined" is present in v1; the §17.18.6.4 stripped list contains no V_E
or dominant-function term. Not IC: S_F is uncomputed (T19), so no established
result is contradicted — the claim is unsupported, not refuted. ∎ (Scope:
ASSERTED. The three supporting textual facts are CHECKED; the classification
itself is the audit's verdict, recorded not re-derived.)

## T8. Δ_op(Volume IV) = ∅ (CHECKED accounting)

The chunk-5 audit ran 108 assertions over Book 19 + Appendices A–C with
0 failed and established no physical promotion; the page carries the audit
verdict that this extends to the volume ("no physical promotion is established
anywhere in Volume IV"), and the manuscript itself says so (its gate
admissions, T19). The Figure-2 schematic (empty baseline y = 0 with five open
gates above) was re-verified as data-accurate. ∎ (Scope: CHECKED — an
accounting of the finite audit record, not a mathematical theorem. It is
*corroborated* by the manuscript's own admissions, not contradicted by them;
this is the book's honesty: it says what is open.)

## T9. Appendix B no-go ledger verified accurate (CHECKED)

The four no-go entries (B1: C8↔octant not a theorem, C3/C4 forcing OPEN;
B2: Distler–Garibaldi not evaded — candidate, not resolution; B3: uniform-action
premise not established; B4: Airy transition not established, only J₀
unconditional) were found verbatim in the v1 text by the completed
cross-check (re-run passing). The "verified accurate" verdict is the audit's
consistency reading (§§19.2–19.4 agreement), carried by reference. ∎ (Scope:
CHECKED for the verbatim textual grounds; the accuracy verdict is the audit's,
recorded.)

## Proof of T10. FLAG-A1 arithmetic

4·(1/4) = 1 and (1/4)⁴ = 1/256, exact rational arithmetic. ∎ (Scope: PROVED.)
The input — the per-contact 1/4 — is archive-sourced MA; its relation to the
certified 1/2 projection coefficient is OPEN per Tier 3.1's own warning. The
arithmetic is sound; the qualifier ("input not established") is missing from
the EXACT row, which is the flag's whole content. (Scope of the input:
ASSERTED.)

## T11. FLAG-A2 — Wick sign

(a) The Appendix A EXACT list carries "· Wick sign" as a bare bullet; the
"(from archive)" qualifier present in the source row was dropped — machine-checked
against the v1 text (re-run passing). (Scope: CHECKED.)
(b) σ_Wick^(t) = −1 is not derived anywhere in v1 — the chunk-5 audit's
negative-search verdict; not independently re-searched in this batch.
(Scope: ASSERTED — recorded.)

## T12–T15. Flags A3–A8 — recorded, not proved

- **A3** (graded-connection rigidity λ = ±1): bridge-essay §3.2 content, logged
  unaudited; Volume I–III coverage not established. (ASSERTED import.)
- **A4** (reduced-matrix-element firewall): a methodological principle (AX in
  the book's tag system), not a proved result; the audit treats it as sound,
  not as a theorem. (ASSERTED rule.)
- **A5** (ancestry criterion): the EXACT row overstates — it contradicts the
  manuscript's own labels (§17.5.1 CONDITIONAL, §17.5.2 CONDITIONAL on the
  uniform-action premise, §19.2 premise OPEN). (ASSERTED — the audit's textual
  verdict; the §17.5.1/§17.5.2 label grounds were not re-checked in this batch.)
- **A6–A8** (Veronese condition at octant boundaries; quasi-linear parent
  magnitude k₀ = β²/(2α); functional form 1/S = cosh w): unaudited bridge
  imports; the soft CONDITIONAL/STRUCTURAL-ID labels do not overclaim.
  (ASSERTED — recorded.)

## Proof of T16. CONTR-1 — Addendum item 6 vs NO-GO B1

*Grounds (machine-checked, re-run passing).* The v1 text contains both
Addendum item 6's "Theorem" with "Proof sketch. ∎" asserting EBEOEBEO is "the
unique cyclic word preserving parity and boundary continuity," and Appendix B
B1's "C8 ↔ octant correspondence is not a theorem. The C3/C4 forcing question
remains OPEN."

*Logic.* The same text asserts theoremhood of the C8↔octant correspondence and
denies it. The proof sketch assumes E contacts "can only reside at
zero-crossing decay nodes" and propagation "must alternate B and O" — neither
forced in v1. This is a direct internal contradiction; the manuscript cannot
both certify and disavow the same theorem. ∎ (Scope: PROVED as internal logic
of the manuscript record; the grounds are checked, the contradiction is
deductive.)

## Proof of T17. CONTR-2 — Addendum item 8 vs §19.3 / NO-GO B2

*Grounds (machine-checked, re-run passing).* The v1 text contains both item 8's
"The real-form E8(−24) framework bypasses this by using: E8(−24) ⊃ A1 + G2 +
C3 …" (stating the DG bypass as fact) and §19.3's "not a proven evasion"
(together with NO-GO B2's "not evaded… candidate, not a resolution").

*Logic.* The text states the bypass as fact while elsewhere denying it is
proven — a direct internal contradiction. The DG-bypass mechanism is at best a
proposal (MA); the E8(−24) host itself is MA per the Volume III ledger
(recorded, not re-derived here). ∎ (Scope: PROVED contradiction / ASSERTED
host.)

## T18. Appendix C defect carry-over — recorded, not proved

The audit's textual finding: Appendix C duplicates the §17.18.8.2 skeleton and
thereby carries IC-13…IC-16 by reference (the NullSpace/8255 defect, the
Kronecker/sandwich mismatch, the −(1/256) double count, the unassigned
wickSign). The duplication was not re-verified in this batch, and the IC-13…16
findings themselves are the Book-17 audit's verdicts (ST import here). ∎
(Scope: ASSERTED — carried, conditional on the Book-17 audit. The book's "IC"
verdict is preserved exactly.)

## T19. The open gates — recorded, not proved

S_F, N_1820, ζ_parent (k₀ power), η_{−4} (UV selection), c_ord/K_parent values,
P_54 location (135 vs 1820 unreconciled), the N_1820 1/2→1/4 gap, P_6435, the
explicit 1820 projector, the Frobenius norms, the role of 638.78, and the C3/C4
forcing question: each OPEN, none with a numerical address, per the
manuscript's own admissions, confirmed by the audit. The v1-text ground for the
ζ_parent assignment ("propagator cosh factors … belong to ζ_parent") was
machine-checked present. ∎ (Scope: ASSERTED — the manuscript's own admissions,
confirmed. This is the honest content of the book.)

## T20. The v3 claims and the certification report — recorded, with one proved contradiction

(a) *Grounds (machine-checked, re-run passing):* the v3 text carries
S_F = 0.48958371, N_1820 = 3, c_rest = 1.30555656; the unsigned, undated
certification report carries "MASTER CERTIFICATION COMPLETE." (Scope: CHECKED.)
(b) Under the standing audit rule that **v1 is the sole audit authority**
(ASSERTED methodological rule, T0), the v3 EXACT/CERTIFIED claims contradict
v1/v2's admissions and the September 15 normalization verdict, and are not
established. (Scope: ASSERTED — follows from the granted authority rule and
the ASSERTED open gates.)
(c) *Proof.* The report's "MASTER CERTIFICATION COMPLETE" cannot hold while
the open gates of T19 stand admitted open: completeness of certification and
admitted openness of the certified quantities are mutually exclusive. ∎
(Scope of (c): PROVED as internal logic.)

## T21. The figures — data-checked; figures are not proofs

The three tension points (√2, 4), (2, 16), (V_E, V_E⁴) lie on y = x⁴
(re-run: max error ≤ 8.882e-16); the Figure-2 baseline is y = 0 with exactly
five gates at y = 1; all plotted points lie inside their Desmos viewports; the
PNG fallbacks were regenerated from the same expressions as the embeds. ∎
(Scope: CHECKED — figure-data consistency only. Recorded declaration: figures
illustrate audit verdicts; they are not the proofs.)

---

# Part IV — New axioms/assumptions beyond Euclid + seed

No new *mathematical* axioms are introduced: every PROVED item is exact
arithmetic, elementary trigonometry, or verifiable internal logic of the
manuscript record. The book's argument rests on the following granted items:

1. **Audit-authority rule** (ASSERTED methodological rule): v1 is the sole
   audit authority; the v3 draft's EXACT/CERTIFIED claims and the unsigned
   certification report are context only. Used in T20.
2. **The reduced-matrix-element firewall** (ASSERTED methodological principle;
   AX in the book's tag system): treated as sound, not as a theorem. (FLAG-A4,
   T13.)
3. **Book-local textual datum** (ASSERTED): v1's own terminology distinction —
   propagator product (4) vs total/all-eight product (16) — is the standard
   against which "incorrect as stated" is adjudicated in T6 (IC-18).
4. **The stipulated standard import**: ℝ, exact real arithmetic, elementary
   trigonometry, finite verifiable textual cross-checks — the same substrate
   declared by the campaign's earlier proof files.

## Computational corroboration cited

`~/workspace/r-theory-rewrite/validation/book19/verify_book19.py`, re-run
2026-09-22 in this batch: exit 0, all checks passing, no timeouts. Exact
(symbolic/text-match) checks V1, V2, V5–V9, V11–V24; completed numerical
checks V3 (V_E⁴ = 638.7823, max_err 2.751e-05), V4 (truncation vs rounding),
V10 (4-decimal rounding). Per the proof-over-sampling rule, the runs that
overlap the analytic proofs above (V1, V2, V5, V7) corroborate them; they do
not establish anything the proofs don't. The PNG fallbacks were regenerated
by the script from the verified expressions after all checks passed.
`test_embeds.py` covers Desmos caption/viewport consistency, not cited for
mathematics.

**Honest bottom line.** Book 19 proves almost nothing new — and that is its
point. What is *proved* here: three exact identities (T1–T3), the truncation
arithmetic (T5), the FLAG-A1 rational arithmetic, and four verifiable internal
contradictions/retractions of the manuscript's own text (IC-18, CONTR-1,
CONTR-2, the certification-report contradiction). What is *checked*: the
638.78 value, the empty-promotion accounting, the Appendix B grounds, the
v1-text grounds of the flags and contradictions, and the figure data. What
remains *asserted*: everything the book's open gates name — above all the
numerical value of S_F, without which no contraction closes and no physical
promotion follows. Book 19 is the boundary where the volume's honesty is
tested: it passes, because it says what is open.
