# Elements vector reference

Parsed + vectorized **Euclid's Elements** (Fitzpatrick/Heiberg edition, the
Elements.pdf Kit uploaded) — the "bible" for the R Theory extension-proof work.

## Contents
- `parse_elements.py` — bilingual text → clean English chunks (book1..13.txt)
- `chunks.json` — 606 chunks: 465 propositions, 118 definitions, 5 postulates,
  5 common notions, 13 book intros. English translation column only; translator
  footnotes kept with their proposition.
- `embed_elements.py` — embeds with Ollama `nomic-embed-text` → `elements.db`
- `search_elements.py` — the lookup tool (see below)
- `elements.db` — SQLite: `chunks` table (metadata + float32 embedding blob)
  plus `chunks_fts` FTS5 table for keyword search

## Use
```bash
python3 search_elements.py "infinitely many primes"   # semantic top-5
python3 search_elements.py -k 10 "method of exhaustion"
python3 search_elements.py --exact 9.20               # Book 9 Prop 20, full text
python3 search_elements.py --exact "def 1.15"         # Book 1 Definition 15
python3 search_elements.py --keyword "perfect number" # FTS keyword
```
Requires `ollama serve` running with `nomic-embed-text` pulled (semantic mode only).

## Rebuild
```bash
python3 parse_elements.py && python3 embed_elements.py
```
Parsing is deterministic from `~/workspace/euclid_work/text/bookN.txt`.
Re-embed only if the parse changes.

## Status (2026-09-22, verified)

- Parse: complete, 606 chunks, spot-checked (Book 9 Prop 20, Book 1 Prop 1,
  Postulate 5, Definition 1). English column clean: hyphenated line-breaks
  repaired, Greek column stripped (remaining Greek letters are genuine
  mathematical notation in the translation, e.g. α, β as variables).
- Embeddings: complete — 606/606 rows, 768-dim `nomic-embed-text` vectors,
  FTS5 populated. Search tests pass: semantic ("angles of a triangle sum to
  two right angles" → I.17, I.32), keyword ("perfect number" → VII Def 22,
  IX.36), exact (9.20 → infinitude of primes, full text).
- This is the standing reference for Euclid lookups in the R Theory
  extension-proof work. Use it instead of re-reading the PDF.
