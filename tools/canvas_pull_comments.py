#!/usr/bin/env python3
"""
canvas_pull_comments.py — download instructor submission comments from Canvas/Camino.

Pulls every submission's comments for a course and writes one Markdown file per
assignment into an output folder. Used to capture Vyas's FINAL edited comments
(the ones he copy-pasted from Claude and then edited in Camino) so the
comment-writing skill can learn the draft -> final voice delta.

NO DEPENDENCIES (stdlib only). Your token stays in your shell — never in code or chat.

--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------
1. Get a token:  Camino -> Account -> Settings -> Approved Integrations ->
                 + New Access Token -> Generate. Copy it (shown once).
2. Find the course ID: it's the number in the course URL,
                 e.g. https://camino.scu.edu/courses/28714  -> 28714
3. Run, e.g. for Spring 165:

   export CANVAS_HOST="camino.instructure.com"  # your Canvas host, no https://
   export CANVAS_TOKEN="paste-your-token-here"  # stays in your shell only

   python3 canvas_pull_comments.py \
       --course 28714 \
       --out "/Users/vsreenivas/Documents/Claude/Projects/Teaching/Fall 2026/MGMT165/inputs/prior_reference/MGMT165_Spring2026/grading_comments"

FERPA: output contains student names + feedback. It lands in prior_reference/,
which is gitignored and stays local. Never commit or push it.
--------------------------------------------------------------------------------
"""
import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.parse
from pathlib import Path


def api_get(host, token, path, params=None):
    """GET a Canvas API path, following pagination via the Link header."""
    url = f"https://{host}/api/v1/{path.lstrip('/')}"
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True)
    results = []
    while url:
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            results.extend(data if isinstance(data, list) else [data])
            # find rel="next" in the Link header for pagination
            link = resp.headers.get("Link", "")
            m = re.search(r'<([^>]+)>;\s*rel="next"', link)
            url = m.group(1) if m else None
    return results


def safe(name):
    return re.sub(r'[^A-Za-z0-9._ -]', '_', name).strip()[:120]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True, help="Canvas course ID (from the URL)")
    ap.add_argument("--out", required=True, help="output folder for grading_comments")
    args = ap.parse_args()

    host = os.environ.get("CANVAS_HOST")
    token = os.environ.get("CANVAS_TOKEN")
    if not host or not token:
        sys.exit("Set CANVAS_HOST and CANVAS_TOKEN environment variables first (see header).")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    print(f"Fetching assignments for course {args.course} ...")
    assignments = api_get(host, token, f"courses/{args.course}/assignments", {"per_page": 100})
    print(f"  {len(assignments)} assignments")

    total_comments = 0
    for a in assignments:
        aid, aname = a["id"], a.get("name", f"assignment_{a['id']}")
        subs = api_get(
            host, token,
            f"courses/{args.course}/assignments/{aid}/submissions",
            {"include[]": ["submission_comments", "user"], "per_page": 100},
        )
        lines, n = [f"# {aname}\n\n_Course {args.course} · assignment {aid}_\n"], 0
        for s in subs:
            comments = s.get("submission_comments") or []
            if not comments:
                continue
            student = (s.get("user") or {}).get("name", f"user_{s.get('user_id')}")
            score = s.get("score")
            lines.append(f"\n## {student}" + (f"  (score: {score})" if score is not None else ""))
            for c in comments:
                author = c.get("author_name", "?")
                when = (c.get("created_at") or "")[:10]
                body = (c.get("comment") or "").strip()
                lines.append(f"- _{author}, {when}:_ {body}")
                n += 1
        if n:
            (out / f"{safe(aname)}.md").write_text("\n".join(lines), encoding="utf-8")
            total_comments += n
            print(f"  {aname}: {n} comments")

    print(f"\nDone. {total_comments} comments written to {out}")


if __name__ == "__main__":
    main()
