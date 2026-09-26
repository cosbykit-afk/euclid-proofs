#!/usr/bin/env python3
"""Semantic + exact search over the vectorized Euclid's Elements.

Usage:
  python3 search_elements.py "infinitely many primes"        # semantic
  python3 search_elements.py --exact "9.20"                   # Book 9 Prop 20
  python3 search_elements.py --exact "def 1.15"               # Book 1 Def 15
  python3 search_elements.py --keyword "perfect number" -k 5  # FTS keyword
  python3 search_elements.py -k 10 "exhaustion"               # semantic top-10
"""
import json, math, os, re, sqlite3, struct, sys, urllib.request

VEC_DIR = os.path.expanduser("~/workspace/euclid_work/vectors")
DB = os.path.join(VEC_DIR, "elements.db")
MODEL = "nomic-embed-text"

def embed_query(q):
    body = json.dumps({"model": MODEL, "prompt": q}).encode()
    req = urllib.request.Request("http://localhost:11434/api/embeddings",
                                 data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())["embedding"]

def rows():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT id, book, kind, number, label, statement, text, embedding FROM chunks")
    data = cur.fetchall()
    con.close()
    out = []
    for (i, book, kind, number, label, stmt, text, blob) in data:
        v = struct.unpack(f"{len(blob)//4}f", blob)
        out.append({"id": i, "book": book, "kind": kind, "number": number,
                    "label": label, "statement": stmt, "text": text, "vec": v})
    return out

def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    na = math.sqrt(sum(x*x for x in a)); nb = math.sqrt(sum(x*x for x in b))
    return dot/(na*nb) if na and nb else 0.0

def show(c, score=None, full=False):
    head = f"[{c['id']}] {c['label']}" + (f"  (score {score:.3f})" if score is not None else "")
    print(head)
    print("  " + c["statement"][:500])
    if full:
        print("  ---\n  " + c["text"][:3000])
    print()

def semantic(q, k):
    qv = embed_query(q)
    scored = sorted(((cosine(qv, c["vec"]), c) for c in rows()),
                    key=lambda x: -x[0])[:k]
    for s, c in scored:
        show(c, s)

def keyword(q, k):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("""SELECT c.id, c.book, c.kind, c.number, c.label, c.statement, c.text
                   FROM chunks_fts f JOIN chunks c ON c.id = f.rowid - 1
                   WHERE chunks_fts MATCH ? LIMIT ?""", (q, k))
    for (i, book, kind, number, label, stmt, text) in cur.fetchall():
        show({"id": i, "book": book, "kind": kind, "number": number,
              "label": label, "statement": stmt, "text": text})
    con.close()

EXACT_RES = [
    (r"^(\d{1,2})[.\s]+(\d{1,3})$", "proposition"),          # 9.20
    (r"^book\s*(\d{1,2})\s+prop(?:osition)?\s*(\d{1,3})$", "proposition"),
    (r"^prop(?:osition)?\s*(\d{1,2})[.\s]+(\d{1,3})$", "proposition"),
    (r"^def(?:inition)?\s*(\d{1,2})[.\s]+(\d{1,3})$", "definition"),
    (r"^post(?:ulate)?\s*(\d{1,2})[.\s]+(\d{1,3})$", "postulate"),
    (r"^cn\s*(\d{1,2})[.\s]+(\d{1,3})$", "common-notion"),
]

def exact(q):
    q = q.strip().lower()
    for pat, kind in EXACT_RES:
        m = re.match(pat, q)
        if m:
            book, num = int(m.group(1)), int(m.group(2))
            con = sqlite3.connect(DB)
            cur = con.cursor()
            cur.execute("SELECT id, book, kind, number, label, statement, text FROM chunks "
                        "WHERE book=? AND kind=? AND number=?", (book, kind, num))
            r = cur.fetchone(); con.close()
            if r:
                show({"id": r[0], "book": r[1], "kind": r[2], "number": r[3],
                      "label": r[4], "statement": r[5], "text": r[6]}, full=True)
            else:
                print(f"not found: book {book} {kind} {num}")
            return
    print("couldn't parse exact reference; try e.g. --exact 9.20")

def main():
    args = sys.argv[1:]
    k, mode, q = 5, "semantic", None
    i = 0
    while i < len(args):
        if args[i] in ("-k", "--top") and i+1 < len(args):
            k = int(args[i+1]); i += 2
        elif args[i] == "--exact":
            mode = "exact"; i += 1
            if i < len(args): q, i = args[i], i + 1
        elif args[i] == "--keyword":
            mode = "keyword"; i += 1
            if i < len(args): q, i = args[i], i + 1
        else:
            q = " ".join(args[i:]); break
    if not q:
        print(__doc__); return
    if mode == "exact":
        exact(q)
    elif mode == "keyword":
        keyword(q, k)
    else:
        semantic(q, k)

if __name__ == "__main__":
    main()
