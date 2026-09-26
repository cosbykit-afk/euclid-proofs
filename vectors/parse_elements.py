#!/usr/bin/env python3
"""Parse Fitzpatrick's Euclid Elements (per-book text files) into clean
English chunks: book intro, definitions, postulates, common notions,
and per-proposition chunks (statement + proof + translator footnotes).

Output: chunks.json — list of {book, kind, number, label, statement, text}
"""
import json, re, sys, os

TEXT_DIR = os.path.expanduser("~/workspace/euclid_work/text")
PROP_RE = re.compile(r"^\s*\S{0,4}þ\.\s+Proposition\s+(\d+)([†‡]?)\s*$")
SEC_RE = re.compile(r"(Definitions|Postulates|Common Notions)\s*$")
PAGE_HEAD_RE = re.compile(r"STOIQEIWN|ELEMENTS BOOK|GREEK[–-]ENGLISH LEXICON")
PAGE_NUM_RE = re.compile(r"^[\f\s]*\d{1,4}\s*$")
GREEK_CHAR_RE = re.compile(r"[Ͱ-Ͽἀ-῝-ͯ]")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]{1,}")

def english_of(line):
    """Extract the English translation column from a bilingual text line.
    The English is the right-hand column: everything after the last
    Greek-script character on the line."""
    line = line.rstrip("\n")
    if not line.strip():
        return ""
    if PAGE_HEAD_RE.search(line):
        return ""
    if PAGE_NUM_RE.match(line):
        return ""
    # footnote lines (translator notes) are English already
    if line.lstrip().startswith(("†", "‡")):
        return line.strip()
    idx = 0
    for m in GREEK_CHAR_RE.finditer(line):
        idx = m.end()
    eng = line[idx:]
    # strip stray punctuation left by the Greek column (hyphenation etc.)
    eng = re.sub(r"^[^A-Za-z0-9\(\[]+", "", eng)
    eng = re.sub(r"\s+", " ", eng).strip()
    words = WORD_RE.findall(eng)
    if words and any(len(w) > 2 for w in words):
        return eng
    return ""

def join_lines(lines):
    """Join extracted English lines, repairing hyphenated line-breaks."""
    out, buf = [], ""
    for ln in lines:
        if buf.endswith("-") and ln and ln[0].islower():
            buf = buf[:-1] + ln
        else:
            if buf:
                out.append(buf)
            buf = ln
    if buf:
        out.append(buf)
    return " ".join(out)

def split_numbered_items(lines):
    """Split a definitions/postulates/notions block into numbered items
    using the English numbering 'N. ...'."""
    items, cur, cur_n = [], [], None
    for ln in lines:
        m = re.match(r"^\s*(\d+)\.\s+(.*\S)\s*$", ln)
        if m:
            if cur:
                items.append((cur_n, join_lines(cur)))
            cur_n, cur = int(m.group(1)), [m.group(2).strip()]
        else:
            if cur is not None and ln.strip():
                cur.append(ln.strip())
    if cur:
        items.append((cur_n, join_lines(cur)))
    return items

def parse_book(path, book):
    raw = open(path, encoding="utf-8", errors="replace").read().splitlines()
    # cut the Greek-English lexicon at the end of book 13
    for i, ln in enumerate(raw):
        if "GREEK-ENGLISH LEXICON" in ln and "STOIQEIWN" not in ln:
            raw = raw[:i]
            break
    eng = [english_of(ln) for ln in raw]
    chunks = []
    # book title / subtitle from first lines
    title_lines = [ln.strip() for ln in eng[:12] if ln.strip()]
    chunks.append({
        "book": book, "kind": "book", "number": 0,
        "label": f"Book {book}",
        "statement": " ".join(title_lines[:4]),
        "text": " ".join(title_lines),
    })

    # walk sections
    cur_sec = None          # 'definitions' | 'postulates' | 'notions'
    sec_lines = []
    cur_prop = None         # dict being built
    prop_lines = []

    def flush_section():
        nonlocal sec_lines, cur_sec
        if not sec_lines or not cur_sec:
            sec_lines, cur_sec = [], None
            return
        items = split_numbered_items(sec_lines)
        kind = {"definitions": "definition", "postulates": "postulate",
                "notions": "common-notion"}[cur_sec]
        for n, txt in items:
            chunks.append({
                "book": book, "kind": kind, "number": n,
                "label": f"Book {book} {kind.title()} {n}",
                "statement": txt[:400],
                "text": txt,
            })
        sec_lines, cur_sec = [], None

    def flush_prop():
        nonlocal cur_prop, prop_lines
        if not cur_prop:
            return
        txt = join_lines([p for p in prop_lines if p]).strip()
        cur_prop["text"] = txt
        # statement = text up to the first blank-gap: enunciation is the
        # first sentence group (ends with the first '. ' after the header)
        m = re.match(r"(.{20,400}?\.)\s", txt)
        cur_prop["statement"] = (m.group(1) if m else txt[:400]).strip()
        chunks.append(cur_prop)
        cur_prop, prop_lines = None, []

    for raw_ln, ln in zip(raw, eng):
        pm = PROP_RE.match(raw_ln)
        if pm:
            flush_section(); flush_prop()
            cur_prop = {
                "book": book, "kind": "proposition",
                "number": int(pm.group(1)),
                "label": f"Book {book} Proposition {pm.group(1)}",
                "statement": "", "text": "",
            }
            continue
        sm = SEC_RE.search(ln)
        if sm and len(ln) < 60:
            flush_section(); flush_prop()
            name = sm.group(1)
            cur_sec = {"Definitions": "definitions", "Postulates": "postulates",
                       "Common Notions": "notions"}[name]
            continue
        if cur_prop is not None:
            if ln:
                prop_lines.append(ln)
        elif cur_sec is not None:
            if ln:
                sec_lines.append(ln)
    flush_section(); flush_prop()
    return chunks

def main():
    all_chunks = []
    for book in range(1, 14):
        path = os.path.join(TEXT_DIR, f"book{book}.txt")
        all_chunks.extend(parse_book(path, book))
    out = os.path.expanduser("~/workspace/euclid_work/vectors/chunks.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=1)
    kinds = {}
    for c in all_chunks:
        kinds[c["kind"]] = kinds.get(c["kind"], 0) + 1
    print(f"total chunks: {len(all_chunks)}")
    print("by kind:", kinds)

if __name__ == "__main__":
    main()
