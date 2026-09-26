# Trig-cumulative campaign — STATUS

Campaign: Euclid trig-cumulative — R Theory as an extension of Euclid's
work, evaluated claim by claim, growing one cumulative trigonometric proof.

Manifest: seed, then Books 0..20 in strict dependency order.

## Seed

| Item | Status |
|---|---|
| seed — initialize cumulative trigonometric proof | **done** (2026-09-22) — `cumulative_trig_proof.md` created with Principle 0 (PROVED) and the principles register; idempotence note: later appends check for existing chapters first |

## Books

| Book | Status | Notes |
|---|---|---|
| Book 0 | **done** (2026-09-22) | 53 claims evaluated (43 PROVED, 10 ASSERTED, 0 CHECKED, 0 INCOMPLETE); 16 folded as new Principles P1–P16 (all PROVED), registered as "1 (Book 0)"–"16 (Book 0)". `book0_claims.md` complete. |
| Book 1 | pending | |
| Book 2 | **done** (2026-09-22) | 97 claims evaluated (74 PROVED, 12 CHECKED, 11 ASSERTED, 0 INCOMPLETE); 8 folded — P17 (half-angle chart forms, P6), P18 (stereographic parametrization, P12), P19 (rational double-angle, P13), P20 (exact octant values tan/cot(π/8), P10/P45), P21 (harmonic oscillator law H″+4H=0, P52), P22 (rational cot double-angle forms, P57), P23 (log antiderivatives, P61), P24 (arctan linearization, P60), all PROVED in dependency order (no Elements proposition is a logical premise — book-2 ledger confirms the Elements contain no trig; book file's own §7 no-wholesale boundary). `book2_claims.md` complete. Cumulative principles: 25 (P0–P24) |
| Book 3 | pending | |
| Book 4 | **done** (2026-09-22) | 59 claims evaluated (22 PROVED, 8 with verification runs, 15 ASSERTED, 19 INCOMPLETE; +1 ST A5 imported). Folded: 2 — Principle 3 (exact 30°/60° trig values, from E1/L1/P0/DC, proved via Euclid 4.15 + 1.5, 1.12, 1.26, 1.32, 1.47, ledgers verified) and Principle 4 (oblique-axis isometry / 60° cosine law, from ISO, via P3 + 1.47), both PROVED. `book4_claims.md` complete. Cumulative principles: 5 (P0–P4) | |
| Book 5 | **done** (2026-09-22) | 11 claims evaluated (8 PROVED, 3 ASSERTED, 0 CHECKED, 0 INCOMPLETE); 0 folded — Book 5 has no trigonometric claims (carrier ranks / Axiom Zero / exterior algebra). `book5_claims.md` complete. Cumulative principles: 1 (P0 seed, unchanged) |
| Book 6 | **done** (2026-09-22) | 27 claims evaluated (22 PROVED, 2 CHECKED, 1 ASSERTED, 0 INCOMPLETE; +1 ST C8 imported). Folded: 2 — Principle 1 (operator Euler formula, C6) and Principle 2 (CHI-orbit double-angle identities, C7), both PROVED analytically (power-series provenance, not Elements). `book6_claims.md` complete. Cumulative principles: 3 (P0, P1, P2) |
| Book 7 | pending | |
| Book 8 | **done** (2026-09-22) | 26 claims evaluated (18 PROVED, 0 CHECKED, 17 ASSERTED incl. declared premises, 0 INCOMPLETE); 0 folded — no claim yields a trig principle provable in dependency order (E12a's cos 4nφ/Chebyshev core is conditional on ASSERTED P-Car and rests on unestablished Fourier theory). `book8_claims.md` complete. Book 8 added 0 principles (register has grown via sibling book workers; see register) |
| Book 9 | **done** (2026-09-22) | 23 claims evaluated (14 PROVED, 2 CHECKED, 8 ASSERTED, 0 INCOMPLETE); 1 folded — Principle 17 (reciprocal-defect trig identity, PROVED) from B9.3c; B9.1a's trig content already registered as "1 (Book 0)", not re-folded. `book9_claims.md` complete. Cumulative principles: highest id P17 (register note: pre-existing numbering collisions at ids 1–2 flagged for reevaluation, not renumbered) |
| Book 10 | **done** (2026-09-22) | 14 claims evaluated (3 PROVED, 4 CHECKED, 7 ASSERTED, 0 INCOMPLETE); 4 new principles folded — 1 (Book 10) half-angle inversion, 2 (Book 10) hyperbolic half-angle, 3 (Book 10) Prüfer polar form, 4 (Book 10) mass-shell ratio chain (PROVED-conditional on asserted import I1). `book10_claims.md` complete. Register note: parallel workers collided on plain ids (Book 11 added plain "1", Book 6 added plain "1"/"2"); Book 0 and Book 10 rows are book-namespaced — a final renumber pass is recommended before the campaign closes | |
| Book 11 | **done** (2026-09-22) | 30 claims evaluated: 13 PROVED / 6 CHECKED / 7 ASSERTED / 4 INCOMPLETE; 1 new principle folded — 1 (Book 11) helicity reciprocal identity (PROVED); claims file `book11_claims.md` (status: complete); chapter appended once, no earlier material touched; register row book-namespaced to avoid the parallel-worker id collision |
| Book 12 | pending | |
| Book 13 | pending | |
| Book 14 | **done** (2026-09-22) | 25 claims evaluated (16 PROVED — 2 of them conditional on ST imports, 1 CHECKED — the book's own conditional NC report, not re-run, 8 ASSERTED incl. 2 ST imports, 0 INCOMPLETE); 9 folded as new Principles P17–P25 (all PROVED; P21 conditional on the 14.II.P1 ST import), proved from definitions + earlier Principles in dependency order, every proof step re-verified by independent recomputation (17 checks, exit 0). `book14_claims.md` complete. Highest Principle number: P25 |
| Book 15 | pending | |
| Book 16 | pending | |
| Book 17 | pending | |
| Book 18 | pending | |
| Book 19 | pending | |
| Book 20 | pending | |

Rule: each book appends its chapter only after reading the cumulative
document and confirming its chapter does not already exist (or is not
already marked complete). No principle may be used before it is
established. Every claim carries a scope label: PROVED / CHECKED /
ASSERTED / INCOMPLETE.

## Known issue (flagged by the Book 0 worker, 2026-09-22)

The Principles register in `cumulative_trig_proof.md` has **duplicate
principle ids**: the id `1` appears four times, `2` three times, `3` and
`4` twice each (from parallel Book 6 / Book 10 / Book 11 workers numbering
from 1 independently), the register header table appears twice, and the
Book 6 block of rows 1–9 is duplicated in full. Only the Seed id `0` and
Book 0's suffixed ids ("1 (Book 0)"–"16 (Book 0)") are unique. Some folded
rows cite bare ids (e.g. "Principles 0, 2") whose referents are now
ambiguous. A coordinator repair pass is needed: renumber every folded
principle to a globally unique id (suffixed by book, or sequential) and
update each chapter's depends-on fields before any later book cites a
bare "P<i>n</i>". Book 0's own chapter defines its P1–P16 internally in
dependency order and is unaffected.
