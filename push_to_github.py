#!/usr/bin/env python3
"""Push the local euclid_work git tree to cosbykit-afk/euclid-proofs via the Git Data API."""
import base64
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request, read_response_body

API = "https://api.github.com"
REPO = "cosbykit-afk/euclid-proofs"
CRED = "custom.github"
WORK = os.path.expanduser("~/workspace/euclid_work")


def api(method, path, data=None):
    url = API + path
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(
        url, data=body, method=method,
        headers={"Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28",
                 "Content-Type": "application/json",
                 "User-Agent": "muse-github-skill"},
    )
    add_surrogate_to_request(req, CRED, allowed_hosts=["api.github.com"])
    try:
        resp = urllib.request.urlopen(req, timeout=120)
    except urllib.error.HTTPError as exc:
        raw = read_response_body(exc).decode("utf-8", "replace")
        raise RuntimeError(f"HTTP {exc.code} {path}: {raw[:500]}")
    return json.loads(read_response_body(resp).decode("utf-8"))


def main():
    os.chdir(WORK)
    files = subprocess.run(
        ["git", "ls-files", "-z"], capture_output=True, check=True, text=True
    ).stdout.split("\0")
    files = [f for f in files if f]
    print(f"{len(files)} files", flush=True)

    tree_entries = []
    for i, path in enumerate(files, 1):
        with open(os.path.join(WORK, path), "rb") as fh:
            content = base64.b64encode(fh.read()).decode("ascii")
        blob = api("POST", f"/repos/{REPO}/git/blobs",
                   {"content": content, "encoding": "base64"})
        tree_entries.append({"path": path, "mode": "100644",
                             "type": "blob", "sha": blob["sha"]})
        if i % 25 == 0:
            print(f"  blobs {i}/{len(files)}", flush=True)

    tree = api("POST", f"/repos/{REPO}/git/trees", {"tree": tree_entries})
    print("tree", tree["sha"], flush=True)

    parent = api("GET", f"/repos/{REPO}/git/refs/heads/main")["object"]["sha"]
    print("parent", parent, flush=True)
    msg = subprocess.run(
        ["git", "log", "-1", "--format=%s"], capture_output=True, check=True,
        text=True, cwd=WORK).stdout.strip()
    commit = api("POST", f"/repos/{REPO}/git/commits",
                 {"message": msg, "tree": tree["sha"], "parents": [parent]})
    print("commit", commit["sha"], flush=True)

    ref = api("PATCH", f"/repos/{REPO}/git/refs/heads/main",
              {"sha": commit["sha"]})
    print("ref", ref["ref"], "->", ref["object"]["sha"], flush=True)
    print("PUSH OK")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        sys.stderr.write(f"PUSH FAILED: {exc}\n")
        sys.exit(1)
