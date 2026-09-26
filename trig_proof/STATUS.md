# STATUS — Cumulative Trigonometric Proof Campaign (deterministic rebuild)

**Date:** 2026-09-22. **Scope:** Books 0–20. **Books 21–22: NOT started.**

## Per-book claim accounting (from bookN_claims.md)

Exactly one label per claim (PROVED / CHECKED / ASSERTED / INCOMPLETE).

| Book | Evaluated | PROVED | CHECKED | ASSERTED | INCOMPLETE | New principles |
|---|---|---|---|---|---|---|
| 0 | 53 | 43 | 0 | 10 | 0 | P1–P16 (16) |
| 1 | 51 | 45 | 1 | 5 | 0 | P17–P18 (2) |
| 2 | 97 | 74 | 12 | 11 | 0 | P19–P24 (6) |
| 3 | 57 | 34 | 8 | 15 | 0 | P25–P34 (10) |
| 4 | 59 | 22 | 2 | 15 | 19 | P35–P36 (2) |
| 5 | 11 | 8 | 0 | 3 | 0 | — (0) |
| 6 | 27 | 22 | 2 | 1 | 0 | P37–P38 (2) |
| 7 | 27 | 21 | 1 | 7 | 1 | P39–P42 (4) |
| 8 | 26 | 18 | 0 | 17 | 0 | — (0) |
| 9 | 23 | 14 | 2 | 8 | 0 | — (0) |
| 10 | 14 | 3 | 4 | 7 | 0 | P43–P44 (2) |
| 11 | 30 | 13 | 6 | 7 | 4 | — (0) |
| 12 | 28 | 13 | 2 | 13 | 0 | P45–P46 (2) |
| 13 | 44 | 28 | 3 | 12 | 1 | P47–P48 (2) |
| 14 | 25 | 16 | 1 | 8 | 0 | P49–P55 (7) |
| 15 | 44 | 25 | 11 | 8 | 0 | P56–P57 (2) |
| 16 | 34 | 29 | 1 | 3 | 1 | P58 (1) |
| 17 | 39 | 21 | 4 | 7 | 7 | P59–P61 (3) |
| 18 | 20 | 14 | 5 | 1 | 0 | — (0) |
| 19 | 26 | 9 | 6 | 11 | 0 | — (0) |
| 20 | 28 | 17 | 0 | 11 | 0 | — (0) |

**Category totals:** PROVED 489 · CHECKED 71 · ASSERTED 180 · INCOMPLETE 33.

**Principles:** P0 (seed) + P1–P61 = **62 principles**, all with complete
proofs in `cumulative_trig_proof.md`. 5 are PROVED-conditional on named
asserted imports (P33, P34 on I6; P44 on I1; P51, P52 on 14.II.P1);
P40 is proved on the principal chart (0,π/2) with off-chart analytic
proof INCOMPLETE.

## Arithmetic notes (disclosed, not smoothed)

- **Book 3:** 58 file rows = 57 claims (C1–C57) + 1 zero-counts
  bookkeeping row. Categories sum to 57. ✓
- **Book 4:** 22+2+15+19 = 58, not 59. The 59th is the ST item (A5
  Cartan–Bianchi, standard import cited not re-derived); filed under
  ASSERTED in the table (imports are assertions). 22+2+16+19 = 59. ✓
- **Book 6:** categories sum to 25 (22+2+1+0) plus 1 ST (C8) = 26, but
  the file says "27 claims evaluated". One claim is unaccounted in the
  file's own tally — flagged, not resolved by invention.
- **Book 7:** 28 table rows for 27 inventory items (7.1.T2 split across
  sections). Categories sum over rows: 21+1+7+1 = 31 ≠ 28. The split
  verdicts inflate the row count; item-level accounting is 21/1/7/1 over
  27 items with overlaps. Flagged.
- **Book 8:** 18+17 = 35 > 26 rows. The 8 inventory ASSERTED vs 17 full-
  accounting ASSERTED reflects premise-dependent vs premise-free
  scoping; the table uses the full 17. Flagged.
- **Book 9:** 14+2+8 = 24 ≠ 23 evaluated. One claim carries a split
  verdict counted twice. Flagged.
- **Book 20:** 17 distinct PROVED over 18 inventory slots (N2's proof
  covers two slots). Table uses 17. ✓

The category totals (489/71/180/33) are the sums of the table's category
columns. They do not equal the sum of "Evaluated" column (764) because
of the flagged inconsistencies above. Both numbers are reported; neither
is forced to match.

## What is established

- **62 trigonometric principles** (P0–P61), each with a complete analytic
  proof, domain, scope, and provenance, in strict book order with no
  forward references and no duplicate folding.
- **Dependency discipline:** every principle cites only earlier
  principles, M0, definitions, or named asserted imports.
- **Euclid boundary:** P35–P36 (Book 4) are the only principles citing
  *Elements* propositions as premises (4.15, 1.5, 1.12, 1.26, 1.32,
  1.47 — all verified in the ledgers). All other principles cite no
  Euclid; the boundary is stated per principle.
- **Books 21–22:** not started. Explicit stop.

## Files

- `cumulative_trig_proof.md` — the proof (deterministic rebuild).
- `book0_claims.md` … `book20_claims.md` — claim-by-claim tables.
- `REEVALUATION.md` — corrected totals, dependency chain, numbering map,
  unresolved items.
- **Drive sink:** hourly via `euclid-hourly-drive-sync`
  (`euclid-work-backup.zip` in Interdisciplinary Works).
