# euclid-proofs

Claim-by-claim evaluations of Euclid's *Elements* (Books 0–20, plus 21–22)
for R Theory, and the cumulative trigonometric proof (P0–P61). Every claim
carries exactly one scope label: **PROVED**, **CHECKED**, **ASSERTED**, or
**INCOMPLETE** — nothing is promoted beyond what the mathematics supports.

## Contents

| Directory | What it is |
|---|---|
| `books/` | Per-book proof files (Book 0–20) + `MASTER_LEDGER.md` |
| `trig_proof/` | The cumulative trigonometric proof: `STATUS.md` (per-book claim accounting), `REEVALUATION.md` |
| `ledger/` | Per-book claim ledgers (`bookN_ledger.md`) |
| `guide/` | *A Guide to Creative Reason (after Euclid)* — finished |
| `vectors/` | Embedding vectors for the proof corpus |
| `text/` | Source text extracts |
| `docs/` | Architecture diagrams (context, DFD, ERD) |
| `wa_sessions/` | Wolfram session records |
| `drive_upload/` | Drive backup staging |

## Status (2026-09-29)

- **Re-audit complete** — all seven counted PROVED rows confirmed (137/137).
- **Ledger arithmetic fixed** — 22 files; 493 PROVED / 32 CHECKED (per the
  2026-09-29 MASTER_LEDGER correction).
- **Cumulative trig proof** — P0–P61 across Books 0–22; per-book PROVED /
  CHECKED / ASSERTED / INCOMPLETE accounting in `trig_proof/STATUS.md`.
- **Creative-reason guide** — finished; guide work closed 2026-09-30.

## Status discipline

One label per claim: PROVED (complete proof), CHECKED (completed symbolic
or numerical check), ASSERTED (manuscript claim, not independently verified),
INCOMPLETE (open). The `MASTER_LEDGER.md` in `books/` is the authority for
per-book totals.

## Related

- [r-theory-rewrite](https://github.com/cosbykit-afk/r-theory-rewrite) — the
  public intuition-first rewrite this audit work feeds.
- [R-Theory](https://github.com/cosbykit-afk/R-Theory) — backup mirror.

## License

Public domain ([The Unlicense](https://unlicense.org)).
