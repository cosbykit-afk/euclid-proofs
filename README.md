# euclid-proofs

Euclid extension proofs for R Theory: claim-by-claim evaluations of Books 0-20
and the cumulative trigonometric proof (P0-P61).

## Layout

- `books/` — per-book proof files (book0_proof.md ... book20_proof.md), the seed
  double-angle identity, and MASTER_LEDGER.md with campaign totals.
- `trig_proof/` — the cumulative trigonometric proof: cumulative_trig_proof.md
  (62 principles P0-P61, each with statement, proof, domain, scope, provenance),
  book0_claims.md ... book20_claims.md (claim-by-claim tables), STATUS.md,
  REEVALUATION.md. Books 21-22 not started (explicit stop).
- `ledger/` — the 13 Euclid's Elements book ledgers used for citation verification.
- `vectors/` — parsed/vectorized Elements (chunks, embeddings, search).
- `guide/` — A Guide to Creative Reason (after Euclid).
- `wa_sessions/` — WolframAlpha session transcripts (CHECKED-only inputs).

## Scope labels

PROVED = exact mathematics shown. CHECKED = a completed numeric run.
ASSERTED = manuscript claim or assumption. INCOMPLETE = failed, timed out, or unfinished.
