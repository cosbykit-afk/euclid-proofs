# MASTER LEDGER — Euclid book-proofs campaign (seed + books 0–20)

**Compiled:** 2026-09-22 (PDT), recompiled from the actual files on disk.
**Repaired:** 2026-09-22 (PDT) — Book 14 row updated after the file's rebuild
(see repair note at the end of §4). No other file changed since the compile
(mtimes verified: only `book14_proof.md` is newer than this ledger's compile).
**Source of this ledger:** `~/workspace/euclid_work/books/seed_double_angle.md` and
`book0_proof.md`–`book20_proof.md` — all 21 files read in full (three extraction passes,
results reconciled here). The previous ledger (compiled 2026-09-22 by the `reevaluate`
agent) was inaccurate: it claimed 14 books had no proof files. **That is wrong. All 21
files exist.** This ledger supersedes it entirely.

**Scope rule (Kit's standing standard):** PROVED = exact mathematics shown in the proof
file; CHECKED = a completed computation with its run cited; ASSERTED = assumption,
import, stipulation, or methodological declaration — granted, never proved here;
INCOMPLETE = failed, timed out, unfinished, or absent work.

**Counting rule:** a file's own stated totals are used verbatim when present. Where a
file states no totals, claims were counted from its own scope labels (flagged "counted"
in the table). **Book 14** was rebuilt 2026-09-22 (24,283 bytes, clean ending, no
truncation marker); its own §F ledger counts (16 / 1 / 8 / 0) were verified against
its 24-row inventory (§C proofs all present) and are used verbatim. Its ST imports
are counted under ASSERTED per the file's own rule (the pre-repair ledger's "2 ST
rows kept separate" no longer applies).

**Campaign-wide totals (claim level, all 21 files):**
- PROVED: **493** · CHECKED: **79** · ASSERTED: **209** · INCOMPLETE: **32**
- Book 14 now counted at 16 PROVED / 1 CHECKED / 8 ASSERTED / 0 INCOMPLETE
  (repaired file; verified 2026-09-22).
- Book 6's ASSERTED includes its 17 framing annotations; book 18's ASSERTED includes
  6 manuscript admissions + 4 ST imports; book 14's ST imports (14.II.P1, 14.V.P1,
  Coulomb law, 1⊕3⊕5 decomposition) are inside its 8 ASSERTED per the file's rule.

## 1. Per-book table

| File | PROVED | CHECKED | ASSERTED | INCOMPLETE | New axioms / declared premises introduced |
|---|---|---|---|---|---|
| seed (Kit's double-angle identity) | 1 | 1 (cited run, corroborating only) | 0 | 0 | none |
| book0 | 43 | 0 | 10 groups | 0 | none (added-axiom ledger 0/0/0/0; Axiom Zero referenced forward-looking) |
| book1 | 46 | 1 | 4 groups | 0 | none (B1.T44: zero new axioms) |
| book2 | 74 | 12 | 11 | 0 | none (P74); substrate S1–S5 + definitions D0–D7 declared |
| book3 | 34 | 8 | 15 | 0 | none; premises N1–N6 (substrate, declarations, imports, inheritances) |
| book4 | 22 | 8 | 10 groups | 19 (Euclid 4.2–4.5, 4.8–4.9, 4.10–4.14, 4.16; Defs 4.1–4.7 — no R extension) | P4.1, P4.1-C, P4.2-L, P4.2-M, P4.3, P4.4, S1–S6, Gates A–H, N1 differential framework |
| book5 | 8 (7 conditional on Axiom Zero) | 1 | 3 | 0 | **A0.1, A0.2** (Axiom Zero; granted, not proved) |
| book6 | 22 (counted) | 2 | 2 claim-level + 17 framing annotations | 0 | AX-6.1…AX-6.5 (declared mathematical data; "0 new primitive axioms") |
| book7 | 19 (counted) | 1 | 4 | 1 (off-chart branch analytic proof for T2; numeric only) | A-7.1…A-7.4 (transfer data, factorization lemma, two-form ω, E1 extension) |
| book8 | 18 | 0 | 17 | 0 | D1–D6, D-EM (vacuum EM import contract) |
| book9 | 14 | 2 | 8 | 0 | none (D-RP/D-HR/D-CAL/D-GR declared contracts; GR content imported) |
| book10 | 3 | 4 | 7 | 0 | A10.1 (rapidity projection contract; stipulated) |
| book11 | 13 | 6 | 7 | 4 (I1 forward book map 12–19; I2 Book-12 forward ref; I3 physical debts; I4 Euclid XI) | AX-C1, AX-C2, AX-C4 (imported physics bundle; YM candidate-class uniqueness ASSERTED not proved), AX-C5 |
| book12 | 13 | 2 | 13 | 0 | none genuinely new (rests on inherited Axiom Zero + notation bridge + imports) |
| book13 | 29 (1 conditional on P20 Fisher-form premise) | 3 | 12 | 0 | AX-1…AX-5 (Bernoulli, Gibbs, Markov, path/reversal, many-body contracts) |
| book14 | 16 | 1 | 8 (ST imports counted under ASSERTED per the file's rule) | 0 | none in the logical sense — declared substrate (background real/complex analysis, linear algebra, calculus); ST imports (14.II.P1, 14.V.P1, Coulomb binding law, Herm(Sym²(C²)) = 1⊕3⊕5); notation import (Book 7 `sxp`); inherited §2.XI.L9 "certified" wording flagged |
| book15 | 28 | 11 | 18 | 0 | NA-15-1…NA-15-7 (trig substrate, UNA/Saw data, Pauli/Bloch lift, quarter-turn, bigrading, E8(−24) host, firewalls M15-A…H) |
| book16 | 29 (labeled, conditional; row 19 split) | 1 | 3 | 1 (four IC defects documented incorrect, not repaired) | AX-16.1…AX-16.5 (heavy-54 selector, index divisibility, dim≤4 truncation, Hodge completion, authority convention) |
| book17 | 21 (counted) | 4 | 7 | 7 (I1 Frobenius norms; I2 1820 projector blocked at P_6435; I3 S_F OPEN; I4–I7 skeleton defects IC-8/9/10/11) | N-17-1…N-17-6 (definitional stratum, ST imports, C8↔octant correspondence as asserted theorem, charge-matching ansatz, contraction physics, open inputs) |
| book18 | 14 | 5 | 11 (1 + 6 manuscript admissions + 4 ST imports) | 0 | A18.1…A18.6 (E/B/O matrices, 1820 projector, M_e/Oprop equivariance, γᵢ relations, prefactor/S_F physics, S_F/N_1820 values — all ASSERTED OPEN) |
| book19 | 9 (counted; 2 split) | 6 | 11 | 0 | none ("proves almost nothing new — and that is its point": audit-honesty file) |
| book20 | 17 | 0 | 11 | 0 | none (B0 Book-0 premise ASSERTED pending; D-χ declared contract) |

**New-axiom register, campaign-wide:** A0.1, A0.2 (Bk 5) · P4.1, P4.1-C, P4.2-L, P4.2-M,
P4.3, P4.4, S1–S6, Gates A–H, N1 (Bk 4) · AX-6.1…AX-6.5 (Bk 6) · A-7.1…A-7.4 (Bk 7) ·
D1–D6, D-EM (Bk 8) · A10.1 (Bk 10) · AX-C1, AX-C2, AX-C4, AX-C5 (Bk 11) · AX-1…AX-5
(Bk 13) · NA-15-1…NA-15-7 (Bk 15) · AX-16.1…AX-16.5 (Bk 16) · N-17-1…N-17-6 (Bk 17) ·
A18.1…A18.6 (Bk 18). Books 0, 1, 2, 3, 9, 12, 19, 20 introduce none; Book 14's
register is now recorded (see its table row): no new axioms in the logical sense —
declared background-mathematics substrate, four ST imports, one notation import, and
the inherited §2.XI.L9 "certified" wording flag.

## 2. Dependency chain: seed → book 20

- **Seed** — Kit's double-angle secant/cosecant identity: **PROVED** (analytic, complete;
  independently verified 2026-09-22 against `~/workspace/kit_theorems/secant-cosecant-identity/PROOF.md`;
  the cited 500,000-sample run corroborates but is not needed by the proof). Established;
  every book may cite it without re-proving it.
- **Seed's actual uses in this campaign:**
  - **Book 7:** the seed identity is quoted verbatim (seed file did not exist at write
    time; cited from the kit_theorems proof). Used in the half-angle machinery.
  - **Book 8:** seed on disk and PROVED; cited where used.
  - **Book 13:** seed used in P2.
  - **Book 14:** 14.I.C2 is PROVED with the seed double-angle identity as its
    lineage (the seed's Lemma 1 is the circular counterpart of the hyperbolic
    half-to-full-angle step proved from definitions here). The campaign's only
    deductive use of the seed that reaches the identity's normalized-square form —
    now complete, with the proof text fully shown.
  - **Books 6, 9, 11:** seed explicitly *not* used (Bk 6: disclosed as not directly
    needed; Bk 9: not invoked; Bk 11: unused). **Book 12:** seed absent at run time.
  - Books 0–5, 10, 15–20: no seed dependence recorded (Books 18/20 rest on their own
    declared substrates).
- **Book 0:** source-boundary/corpus audit; 43 PROVED. New-axiom ledger 0/0/0/0.
- **Books 1–3:** independent analytic core (46 / 74 / 34 PROVED). Cross-file seams
  (batch-parallelism artifacts, each disclosed in its file): Book 1 notes the seed file
  was absent at its write; Book 2 cites Book 1's C7 rule without a Book 1 file in its
  batch; Book 3 keeps Book 2 periodicity inheritance (C11) ASSERTED at the page's MA
  status. Now that all files exist, these seams are reconcilable but were not
  re-verified in this compilation.
- **Book 4:** the Euclid contact is exactly one construction — 4.15's sixfold hexagon
  (via declared P4.2-L) — and nothing else; 19 Euclid Book 4 items deliberately
  unextended (INCOMPLETE ledger, not failures).
- **Book 5:** Axiom Zero (A0.1/A0.2) introduced; C4–C7 all conditional on it.
  Book-local inheritance datum P-inherit (E rank 2, V rank 3) ASSERTED pending the
  Books 2–4 audits — now that book2/3/4 files exist, this premise is reconcilable.
- **Book 6 → Book 11:** Book 11 cites `book6_proof.md` P10/P12/P14 as PROVED
  (conditional on AX-6.2, AX-6.4) — consistent with what Book 6's file contains.
- **Book 8 → Book 9:** dependency lock is an ASSERTED manuscript assertion. Book 9's
  file (14 PROVED, 2 CHECKED) stands on declared contracts D-RP/D-HR/D-CAL/D-GR;
  Poisson recovery (B9.6c) and static-dust obstruction (B9.6d) remain ASSERTED, not
  independently verified.
- **Book 12:** no new axioms; rests on Axiom Zero lineage + notation bridge + imports.
- **Book 13 → Book 14:** Book 13's AX-contracts feed forward; Book 14's repaired
  file (§D) records that it uses no Book 13 content — only the certified Books 0–7
  and 9–10 calculus, entering here purely as background mathematics.
- **Books 15–18 (Volume IV block):** E8/Saw/contraction machinery; the heaviest
  ASSERTED-OPEN load (E/B/O matrices, 1820 projector blocked at P_6435, S_F, N_1820,
  γᵢ relations). Campaign results C17–C19 in Book 18 (CHECKED) close the P_54 location
  question (54 ⊂ 135 exactly once); M_e/Oprop equivariance remains ASSERTED-open.
- **Book 19:** audit-honesty file; records the v1 open gates (S_F, N_1820, ζ_parent,
  η_{−4}, c_ord/K_parent, P_54 reconciliation, N_1820 1/2→1/4 gap, P_6435, Frobenius
  norms, 638.78 role) and rejects the v3 draft's values under the v1-authority rule.
- **Book 20:** 17 PROVED; conditional on B0 (Book 0 primitive calculus/one-generator
  reduction) as an ASSERTED premise — book0_proof.md did not exist when Book 20's
  worker ran; it exists now, so this premise is reconcilable.

## 3. Consolidated open-items list

ASSERTED items fall into three classes: (i) **permanent imports/declarations** — never
"closable" by proof, only by adoption or supersession; (ii) **pending audits** — closable
by completing the named audit; (iii) **bookkeeping** — closed by writing the missing
text. INCOMPLETE items are listed first.

### INCOMPLETE (33)

1. **Book 4 (19):** Euclid defs 4.1–4.7 and props 4.2–4.5, 4.8, 4.9, 4.10–4.14
   (pentagon/golden-section chain), 4.16 (15-gon) — deliberate non-extension; the
   campaign takes only 4.15's hexagon.
2. **Book 7 (1):** off-chart branch analytic proof for T2 — stated gap, numeric only.
3. **Book 11 (4):** I1 forward book map 12–19; I2 Book-12 later-Casimir forward reference;
   I3 A7 physical debts (scalar ontology, VEV, masses, couplings, RG flow, flavor);
   I4 Euclid XI 11.1–11.39, no counterpart.
4. **Book 16 (1):** four IC defects documented incorrect and *not repaired*: 16.I.80 sign
   error, line-1614 Schur formula, line-1925 rank biconditional, 16.I.106.T2/C1 sign
   error (retracted at 16.I.107).
5. **Book 17 (7):** I1 Frobenius norms (γᵢ, B, Π₋ conventions open); I2 explicit 1820
   projector (blocked at P_6435); I3 numerical S_F (OPEN); I4–I7 skeleton defects
   (IC-8 NullSpace {}; IC-9 dimension mismatch; IC-10 double-counted −1/256; IC-11
   unassigned wickSign).

(Book 14's former INCOMPLETE item — the truncated file — is closed by the 2026-09-22
repair; the rebuilt file has 0 INCOMPLETE.)

### ASSERTED — pending audits / reconcilable now that all files exist

8. **Book 5 P-inherit** (E rank 2, V rank 3, no E↔V identification) — pending the
   Books 2–4 audits; book2/3/4 files now exist, reconcile by checking their claims.
9. **Book 8 P-Car** (carrier premise package) — pending Volume I Books 2–3 and Book 7
   audits; book7 file now exists, reconcile its side.
10. **Book 20 B0** (Book 0 primitive calculus/one-generator reduction) — entered
    ASSERTED because book0_proof.md was absent; it exists now (43 PROVED), reconcile by
    citing the actual file.
11. **Book 2 A10 / Book 3 C11** — Book 1's C7 rule / Book 2 periodicity inheritance
    cited across the batch-independence seam; book1_proof.md now exists, reconcile.
12. **Book 10 C8** (no universal half-angle for excited states) — ASSERTED; the
    radial-Dirac integrator was not re-run. Close by re-running it.
13. **Book 11 AX-C4** — Yang–Mills candidate-class uniqueness is ASSERTED, not proved.
    Close only by an actual uniqueness proof or by keeping it fenced as a declared
    candidate class.
14. **Book 13 P25** — crossing-rule half leans on the uncertified source-boundary
    theorem; "certified λ" labeling defect inherited from 2.XI.L9 flagged, not repaired.
15. **Book 15 A1** — C8↔octant correspondence as *theorem* is ASSERTED and disputed
    inside v1 itself (CONTR-1); E8 threshold admission (38) and closure (39) asserted
    by design.
16. **Book 16** — global anomaly cancellation OPEN; λ₂≠0 forced by nothing (E8/T_w/D4
    covariance, reduced q parity, fermion-pair ancestry all fail to force it); radius
    stabilization OPEN; action-level gates (BRST survival, healthy spin-2, mirror
    selection) OPEN; c_ord, N_1820, K_parent not established (manuscript's own Sept-15
    verdict).
17. **Book 17 A1/A3/A5/A7** — C8↔octant correspondence, charge-matching ansatz,
    contraction prefactor physics, 638.78 role all ASSERTED; A5, A7 marked OPEN.
18. **Book 18 A18.1–A18.6** — explicit 1820×1820 E/B/O matrices, explicit 1820
    projector (blocked at P_6435), M_e/Oprop SO(16)-equivariance, γᵢ relations
    (incl. γ₁₇²=+1), physical content of −√10/1536, S_F and N_1820 values — all
    ASSERTED OPEN. C17–C19 (CHECKED) closed the P_54 location; the 120 embedding and
    physical embedding selection remain open.
19. **Book 19 T19** — v1 open gates: S_F, N_1820, ζ_parent, η_{−4}, c_ord/K_parent,
    P_54 135-vs-1820 reconciliation, N_1820 1/2→1/4 gap, P_6435, explicit 1820
    projector, Frobenius norms, role of 638.78. The v3 draft's S_F=0.48958371 /
    N_1820=3 / c_rest=1.30555656 and the unsigned "MASTER CERTIFICATION COMPLETE"
    are not established under the v1-authority rule.
20. **Book 9 B9.6c/B9.6d** — Poisson recovery and static-dust obstruction ASSERTED,
    not independently verified; external calibration D-CAL (a = GM/(2c²)) ASSERTED.

### Permanent imports / declarations (aggregate, by book)

These are not closable by proof; they are the declared substrate. Listed so nothing
is mistaken for proved mathematics: Bk 0 M0 substrate + source rule; Bk 1 standard
trig/analysis block S, rules R1–R5, Declaration 1.I.D1, status grammar; Bk 2 S1–S5,
D0–D7, A1–A11; Bk 3 N1–N6 (analytic substrate, D1–D9, π-periodicity, RP²/Spin(3)/w₁
machinery, bookkeeping inheritances); Bk 5 P-inherit/P-import/P-method; Bk 6 S1, ST
imports; Bk 7 standard substrate + A-7.2/A-7.3; Bk 8 D-Ext/D-⋆/D-Cov + seven
declarations D1–D6/D-EM; Bk 9 D0/D-PRIM/D-CH/D-BRANCH + GR bundle; Bk 10 I1–I3
(Dirac, radial Dirac–Coulomb, V–A); Bk 11 AX-C4 ST bundle + Euclid I Common Notions;
Bk 12 A2/A5/A9 math imports, A6/A7 physics imports, A1/A8/A13 empirical inputs; Bk 13
real analysis background; Bk 14 ST kinematics + Dirac–Coulomb formula; Bk 15 NA
substrates (ST theorems kept as imports); Bk 16 ST (PROOFS_Casimir K-1..K-9,
Spin(10) invariants, Hodge, Schur/Frobenius–Schur) + SC computations; Bk 17 N-17-2
ST theorems; Bk 18 ST1–ST4 + so(10)⊕so(6)⊂so(16) reference; Bk 19 ℝ/arithmetic/trig;
Bk 20 I-SR/I-Dirac/I-Bloch/I-VA/I-Coulomb/I-EM imports, D-χ contract.

## 4. Honest bottom line

- **What is established:** 492 PROVED claims (exact mathematics shown in the files)
  and 79 CHECKED completed computations across all 21 files. The seed identity is
  PROVED and is actually used (Books 7, 8, 13, 14). The analytic core is thickest in
  Books 2 (74), 1 (46), 0 (43), 3 (34), 13 (28), 15 (28), 6 (22), 4 (22).
- **What is conditional:** the great majority of physical content rests on declared
  premises — Axiom Zero (Bk 5), the P4/Gates substrate (Bk 4), AX-6.1…6.5 (Bk 6),
  A-7.1…7.4 (Bk 7), the seven Book-8 declarations + carrier package, the rapidity
  contract + three physics imports (Bk 10), AX-C contracts (Bk 11), the AX-1…5
  contracts (Bk 13), NA-15/E8 host (Bk 15), AX-16 selector block (Bk 16), the N-17
  contraction premises (Bk 17), A18.1…18.6 open admissions (Bk 18). The files are
  honest about this throughout; no expectation or manuscript label is presented as
  proved mathematics.
- **What is missing or broken:** 33 INCOMPLETE items in total (the 19 deliberate
  Euclid-4 non-extensions, 7 Book-17 open/skeleton items, 4 Book-11 forward-map/debt
  items, and singles in Books 7, 13, 16). The batch-parallelism seams (items 8–11)
  are reconcilable now that all 21 files exist, but were not re-verified in this
  compilation. The pending audits that would close the carrier/inheritance premises
  are largely a matter of cross-citing the now-complete file set.
- **Manuscript corrections found by this campaign (PROVED as corrections):**
  Bk 7 CL2 sign slip (`2λ−1 = cos x − sin x` → `sin x − cos x`); Bk 12 P13
  (`(1/5)Tr(Q_ε²) = |H|` holds only at λ ∈ {1/2, 3/5}, counterexamples at
  λ = 0.7, 0.3, 0.9); Bk 13 two IC false claims disproved by counterexample
  ("|urx| is exactly the canonical partition function"; "λ is quarter-turn
  invariant"); Bk 16 four IC defects documented incorrect (not repaired); Bk 17
  IC-1/IC-4/IC-6/IC-7 correction exhibits.

**Book 14 repair note (2026-09-22):** the pre-repair `book14_proof.md` (6,590 bytes,
84 lines) ended mid-sentence in §C partway through the proof of 14.I.C2, its final
text reading `…with `c_2 = sech η = (1-q²)/(1+q²)` and `tanh²+s` followed by a
literal `...[truncated 10943 chars]` marker — the worker had pasted a truncated read
into the file itself. Only 14.I.T1 and 14.I.C1 had complete proof text; the other 14
inventory-labeled PROVED items had labels but no proofs, and the new-axioms section
was never written. The file was rebuilt from the actual Book 14 rewrite source
(`~/workspace/r-theory-rewrite/book14/index.html`): current file is 24,283 bytes
with a clean ending (closes with §E source-text defects and §F ledger counts), no
truncation marker. Its own §F counts — PROVED 16, CHECKED 1, ASSERTED 8,
INCOMPLETE 0 — were verified against the 24-row inventory (row 7 split into its
proved math and asserted physical caveat: 25 scoped items = 16+1+8+0 ✓) and against
§C, where every PROVED item's proof text is present in full. The new-axiom register
is now recorded (§D): no new axioms in the logical sense; declared
background-mathematics substrate; ST imports 14.II.P1, 14.V.P1, the Coulomb binding
law, and the Herm(Sym²(C²)) = 1⊕3⊕5 decomposition (counted under ASSERTED per the
file's rule); notation import of Book 7's `sxp` convention; the inherited §2.XI.L9
"certified" wording is flagged, not repaired. Campaign totals revised by arithmetic:
PROVED 478 − 2 + 16 = **492**; CHECKED 79 − 1 + 1 = **79**; ASSERTED 206 − 5 + 8 =
**209** (the old "2 ST rows kept separate" are now inside the 8 per the file's own
rule); INCOMPLETE 34 − 1 + 0 = **33**. The worker's post-proof random sampling on one
lift identity (noted in the repair handoff) was not repeated and is not the basis of
any PROVED status here, per the proof-over-sampling rule. The Book 14 footer still
references `validation/book14/verify_book14.py`, which is absent on disk — kept
stated honestly in §E of the file and noted here.

*Correction to the previous ledger: the earlier "14 missing book files" claim was
false — all 21 files exist on disk. The earlier totals (104/8/51/15) covered only
the 7 files visible at that time.*
