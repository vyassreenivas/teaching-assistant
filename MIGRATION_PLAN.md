# Migration Plan — Split Teaching into a Perpetual Home (Option B)

> **Status:** PLAN ONLY. Nothing executes until Vyas says "proceed." This is a structural change to a live, git-backed system.
> **Goal:** Decouple the reusable teaching system + knowledge (perpetual, compounding) from per-term course instances (disposable, archivable), so the system improves quarter on quarter while disk and git stay lean.
> **Written:** 2026-06-23.

---

## Target structure

```
Projects/
├── TeachingAssistant/        # MOVED out of Spring 2026. The perpetual system. Own git repo. ~736 KB.
│   ├── generator/  templates/  shared/  skills/
│   ├── knowledge/            # master_skill_log, playbook, set_history — compounds across ALL terms
│   └── courses/              # generation intake (FALL2026_intake.md, MGMT16x inputs)
│
├── Teaching/                 # NEW. Holds per-term course instances. Own git repo.
│   ├── .gitignore            # lean: media + FERPA + HBP excluded from commit #1
│   ├── Spring 2026/          # MGMT162 + MGMT165 MOVED here. The first frozen archive.
│   │   ├── MGMT162/
│   │   └── MGMT165/
│   └── Fall 2026/            # NEW term. Built from the system.
│       ├── MGMT164/          # one course, two sections
│       └── MGMT165/          # one course, one section (no name clash — different parent)
│
└── Spring 2026/              # STAYS. Now purely the life OS + master infra.
    ├── CLAUDE.md (master)  JOURNAL.md  LIFE_DATABASE.md  VYAS_CONTEXT.md
    ├── EMAIL_ROUTING.md  _inbox/  .tooling/
    └── Health/  Personal/  Productivity/  Research/
```

Three git repos after this: `Spring 2026` (life OS, existing repo, unchanged), `TeachingAssistant` (new, perpetual system), `Teaching` (new, term instances). The first two stay tiny. `Teaching` stays lean because media is gitignored from the start.

---

## Why fresh repos (the 611 MB fix)

The current `Spring 2026/.git` is 611 MB because large binaries were committed early. That weight is permanent in that history. The new `TeachingAssistant` and `Teaching` repos start clean, with media gitignored from commit #1, so the bloat does not travel forward. We do **not** rewrite the old history (that violates the never-rewrite-history rule); we just leave it behind.

---

## Reversibility

- **Reversible until the final step.** The plan copies first, verifies, and only removes originals from the `Spring 2026` working tree at the very end. Until then, both copies exist and you can abort by deleting the new folders.
- **Irreversible once done:** removing `TeachingAssistant/`, `MGMT162/`, `MGMT165/` from the `Spring 2026` working tree (recoverable from git history, but it is a real change). The new repos' histories start fresh (old per-file history not carried into them).
- **Hard prereq:** a clean committed + pushed snapshot of `Spring 2026` before anything moves (Step 0).

---

## Steps

Each step is tagged **[Finder]** (you do it) or **[Terminal]** (paste the command, or I run it if you mount `Projects/`).

### Step 0 — Snapshot (do not skip)
**[Terminal]** From inside `Spring 2026`:
```
git add -A && git commit -m "pre-migration snapshot $(date +%F)" && git push
```
Optional belt-and-suspenders: zip the whole `Spring 2026` folder to an external drive before touching anything.

### Step 1 — Lift the system out
**[Finder]** Move `Spring 2026/TeachingAssistant/` → `Projects/TeachingAssistant/`.
(It is only 736 KB and nothing in the master infra depends on its location.)

### Step 2 — Create the Teaching home
**[Finder]** Create `Projects/Teaching/`, and inside it `Spring 2026/` and `Fall 2026/`.

### Step 3 — Relocate the Spring courses into the archive
**[Finder]** Move `Spring 2026/MGMT162/` → `Projects/Teaching/Spring 2026/MGMT162/`.
**[Finder]** Move `Spring 2026/MGMT165/` → `Projects/Teaching/Spring 2026/MGMT165/`.
(Per-course `brain/CLAUDE.md` files use relative paths, so they keep working after the move.)

### Step 4 — Initialize the two new repos
**[Terminal]** In `Projects/TeachingAssistant/`:
```
git init && git add -A && git commit -m "init perpetual teaching system"
```
**[Terminal]** In `Projects/Teaching/`: drop in the `.gitignore` below FIRST, then:
```
git init && git add -A && git commit -m "init teaching instances; Spring 2026 archived"
```
Create matching private GitHub repos (`teaching-assistant`, `teaching`) and `git remote add origin … && git push -u origin main` for each. Mirror the existing `spring-2026` remote setup.

### Step 5 — Backup jobs
**[Terminal]** Copy `.tooling/spring2026-backup.sh` + the launchd plist as templates; make one per new repo (or one script that loops over all three repo paths). Schedule nightly like the existing 11:30 PM job. Point each at its repo, log to a local `.backup.log` (gitignored).

### Step 6 — Update references
**[Claude can do]** Update `Spring 2026/CLAUDE.md` (master): remove MGMT162/MGMT165 from the folder-layout and "six subfolders" sections; note teaching now lives in `Projects/Teaching/` and the system in `Projects/TeachingAssistant/`. The master assistant's scope becomes life-OS only.
**[Claude can do]** Trim the now-dead FERPA/HBP course rules out of `Spring 2026/.gitignore` (they move to the Teaching repo's gitignore).

### Step 7 — Verify, then remove originals
**[Terminal / Claude]** Before deleting anything from `Spring 2026`:
- FERPA leak check in the new Teaching repo: `git ls-files | grep -iE 'roster|students\.json|participation|\.xlsx$|Student Work' ` returns nothing.
- HBP leak check: `git ls-files | grep -iE 'HBS|Readings|\.pdf$'` returns nothing.
- Size check: `du -sh Projects/Teaching/.git` is small (single-digit MB, not hundreds).
Only after all three pass: the `MGMT162/`, `MGMT165/`, `TeachingAssistant/` entries are removed from the `Spring 2026` working tree and committed there (`git rm -r --cached` + delete, or just delete and `git add -A`).

---

## `.gitignore` for the new `Teaching` repo

Ported from the Spring master gitignore, path-independent globs kept, course-specific prefixes generalized, plus media exclusions to stop the bloat. Drop this in `Projects/Teaching/.gitignore` BEFORE the first commit.

```gitignore
# OS / editor / tooling junk
.DS_Store
._*
*.tmp
*.temp
*.swp
*~
*.bak
*.bak.*
~$*
.~lock.*#
__pycache__/
.ipynb_checkpoints/

# Secrets
.env
.env.*
*secret*
*credentials*
*.pem
*.key
*token*.json

# FERPA — student data (path-independent)
**/03_Student_Data/
**/Student Work/
**/students.json
**/*Roster*.xlsx
**/*Roster*.xls
**/*Roster*.csv
**/*Participation*
**/*Team_Assignments*
**/*.csv
**/*.xlsx
**/*.xls
**/Case Presentations*/
**/past_evaluations/
**/*Feedback*.md
.claude/

# HBP-licensed content
**/Final HBS Cases/
**/Final HBS Articles/
**/Final Articles & Cases/
**/Readings/
**/Readings - Articles & Cases/
**/*.pdf

# Heavy media — keep OUT of git forever (this is the 611 MB lesson)
**/*.mp4
**/*.mov
**/*.m4a
**/*.wav
**/*.png
**/*.jpg
**/*.jpeg
**/*Captions/
**/*Caption*/
**/HDD*/
**/Slides/

# Tracker backups + scratch
*.json.bak
*.json.bak_*
**/Delete/
.backup.log
```

Note: this is deliberately aggressive on `.pdf`, `.xlsx`, `.csv`, and media because in course folders those are almost always student or licensed content. If a specific safe file needs committing (e.g., a public rubric PDF), add a negation (`!path/to/file`) below the rule.

---

## What I need from you to run it

- **If you want me to execute:** mount/grant access to `Projects/` (one level up from where I am now), and I run Steps 1-7 with a checkpoint after Step 3 and before Step 7.
- **If you'd rather drive:** do the Finder moves (Steps 1-3) yourself, then tell me and I'll handle the git init, gitignore, backups, reference updates, and verification (Steps 4-7).

Either way, Step 0 (snapshot) happens first, and nothing is deleted from `Spring 2026` until the Step 7 leak checks pass.
```
