Living document — update these diagrams when adding features.

# euclid-proofs — Architecture

## 1. Context diagram (level 0)

```mermaid
flowchart
    E1["Kit"]
    E2["R Theory proof work"]
    E3["Ollama embed model"]
    E4["GitHub readers"]
    SYS("Euclid proofs archive")
    E1 -->|"proof drafts and ledgers"| SYS
    E1 -->|"numeric check notes"| SYS
    SYS -->|"lookup answers"| E2
    E3 -->|"768 dim embeddings"| SYS
    SYS -->|"published files and pages"| E4
```

## 2. Level-1 data flow diagram

```mermaid
flowchart
    E1["Kit"]
    E2["WolframAlpha"]
    E3["Ollama embed model"]
    E4["R Theory proof work"]
    E5["Local working tree"]
    P1("1.0 Write proof files")
    P2("2.0 Maintain claim ledgers")
    P3("3.0 Run numeric checks")
    P4("4.0 Build vector reference")
    P5("5.0 Generate web pages")
    P6("6.0 Publish to GitHub")
    D1[("D1 Proof files")]
    D2[("D2 Claim ledgers")]
    D3[("D3 Elements source text")]
    D4[("D4 Vector index")]
    D5[("D5 Web pages")]
    D6[("D6 Check notes")]
    E1 -->|"proof drafts"| P1
    P1 -->|"bookN proof md"| D1
    D1 -->|"claim listings"| P2
    P2 -->|"ledger rows"| D2
    E1 -->|"numeric queries"| E2
    E2 -->|"check results"| P3
    P3 -->|"session notes"| D6
    D3 -->|"clean English chunks"| P4
    E3 -->|"embeddings"| P4
    P4 -->|"chunks plus sqlite db"| D4
    D4 -->|"lookup answers"| E4
    D2 -->|"claim tables"| P5
    P5 -->|"html pages"| D5
    E5 -->|"git file tree"| P6
    P6 -->|"synced proof files"| D1
    P6 -->|"synced ledgers"| D2
    P6 -->|"synced pages"| D5
```

## 3. Entity–relationship diagram

```mermaid
erDiagram
    PROOF_FILE ||--|{ CLAIM : contains
    PROOF_FILE {
        string path PK
        int book
        int proved
        int checked
        int asserted
        int incomplete
    }
    CLAIM {
        string claim_id PK
        string label
        string source_file
    }
    PROOF_FILE ||--o{ LEDGER : tallied_in
    LEDGER {
        int book PK
        int proved
        int checked
        int asserted
        int incomplete
    }
    TEXT_FILE ||--|{ CHUNK : parsed_into
    TEXT_FILE {
        string path PK
        int book
    }
    CHUNK {
        string chunk_id PK
        string kind
        string reference
        blob embedding
    }
    CLAIM ||--o{ SESSION_NOTE : verified_by
    SESSION_NOTE {
        string date PK
        string topic
        int queries
    }
```

## Grounding notes

- OBSERVED: 152 files across `books/`, `ledger/`, `trig_proof/`, `vectors/`, `docs/`, `guide/`, `text/`, `wa_sessions/` plus `verify_P21.py`, `verify_P21.wl`, `push_to_github.py`. No root README exists (404).
- OBSERVED: `books/` holds 21 proof files `seed_double_angle.md` plus `book0_proof.md` through `book20_proof.md`, and `MASTER_LEDGER.md` states campaign totals of 493 PROVED, 79 CHECKED, 209 ASSERTED, 32 INCOMPLETE.
- OBSERVED: `trig_proof/` holds per-book `bookN_claims.md` files, cumulative proofs, `STATUS.md`, `REEVALUATION.md`, `FINAL_EXAM.md`.
- OBSERVED: `vectors/README.md` describes `parse_elements.py` to 606 chunks, `embed_elements.py` via Ollama `nomic-embed-text`, `search_elements.py` lookup, and `elements.db` with `chunks` and `chunks_fts` FTS5 tables. It calls the reference the standing source for Euclid lookups in R Theory extension-proof work.
- OBSERVED: `docs/build_pages.py` generates the HTML pages from claim data; `wa_sessions/` holds dated WolframAlpha numeric-check transcripts; `push_to_github.py` pushes the local working tree to this repo.
- INFERRED: external entity "GitHub readers" — the repo is public, but no reader activity was observed.
- INFERRED: the overall purpose framing "published archive of the proof campaign" — there is no README; the purpose was assembled from file contents.
- INFERRED: the exact trigger cadence of the publish script was not observed; the script itself and its docstring are observed.
