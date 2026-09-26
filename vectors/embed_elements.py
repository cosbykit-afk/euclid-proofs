#!/usr/bin/env python3
"""Embed all Euclid chunks with Ollama nomic-embed-text and store in SQLite.

Resumable: skips chunks already in the DB. Embeds a truncated prefix
(6000 chars ~ <1900 tokens, under the model's 2048 physical batch);
the full text is stored for display.

Schema:
  chunks(id INTEGER PK, book INT, kind TEXT, number INT, label TEXT,
         statement TEXT, text TEXT, embedding BLOB float32)
  chunks_fts(label, statement, text)  -- FTS5 for keyword / exact lookup
"""
import json, os, sqlite3, struct, sys, time, urllib.request, urllib.error

VEC_DIR = os.path.expanduser("~/workspace/euclid_work/vectors")
DB = os.path.join(VEC_DIR, "elements.db")
MODEL = "nomic-embed-text"
MAX_CHARS = 6000
FALLBACK_CHARS = 3000

def embed_one(text):
    for limit in (MAX_CHARS, FALLBACK_CHARS):
        body = json.dumps({"model": MODEL, "prompt": text[:limit],
                           "options": {"num_ctx": 2048}}).encode()
        req = urllib.request.Request("http://localhost:11434/api/embeddings",
                                     data=body,
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.loads(r.read())["embedding"]
        except urllib.error.HTTPError as e:
            if limit == FALLBACK_CHARS:
                raise
            print(f"  retry shorter ({e.code})", flush=True)
    raise RuntimeError("unreachable")

def main():
    chunks = json.load(open(os.path.join(VEC_DIR, "chunks.json")))
    new_db = not os.path.exists(DB)
    con = sqlite3.connect(DB)
    cur = con.cursor()
    if new_db:
        cur.execute("""CREATE TABLE chunks(
            id INTEGER PRIMARY KEY, book INT, kind TEXT, number INT,
            label TEXT, statement TEXT, text TEXT, embedding BLOB)""")
        cur.execute("CREATE VIRTUAL TABLE chunks_fts USING fts5(label, statement, text)")
        con.commit()
    done = {r[0] for r in cur.execute("SELECT id FROM chunks").fetchall()}
    todo = [(i, c) for i, c in enumerate(chunks) if i not in done]
    print(f"{len(done)} already embedded, {len(todo)} to go", flush=True)
    t0 = time.time()
    for n, (i, c) in enumerate(todo):
        v = embed_one(c["text"])
        blob = struct.pack(f"{len(v)}f", *v)
        cur.execute("INSERT INTO chunks VALUES (?,?,?,?,?,?,?,?)",
                    (i, c["book"], c["kind"], c["number"], c["label"],
                     c["statement"], c["text"], blob))
        cur.execute("INSERT INTO chunks_fts(label, statement, text) VALUES (?,?,?)",
                    (c["label"], c["statement"], c["text"]))
        if (n + 1) % 25 == 0:
            con.commit()
            print(f"  {n+1}/{len(todo)} ({time.time()-t0:.0f}s)", flush=True)
    con.commit()
    total = cur.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    dim = len(cur.execute("SELECT embedding FROM chunks LIMIT 1").fetchone()[0]) // 4
    print(f"stored {total} rows, dim={dim} -> {DB}")
    con.close()

if __name__ == "__main__":
    main()
