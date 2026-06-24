# Migration Handoff — run these on your Mac

> **Status: copy phase DONE and verified. Nothing deleted. Originals intact.**
> The remaining steps are git + GitHub + backups, which must run natively on your Mac (the Cowork sandbox can't manage git lock files on the mounted disk, and the pushes need your credentials).

---

## What's already done (by Claude, verified)

- `Projects/TeachingAssistant/` — the perpetual system, copied out of `Spring 2026/`. Has `.gitignore` protecting future course inputs.
- `Projects/Teaching/Spring 2026/MGMT162/` and `MGMT165/` — full copies (568M / 946M), the frozen archive. Loose spring artifacts (both Pulse Surveys, `next_week_open_points.md`) swept in.
- `Projects/Teaching/Fall 2026/` — empty, ready for the new courses.
- `Projects/Teaching/.gitignore` — lean: excludes media, FERPA, HBP, and the whole frozen `Spring 2026/` archive (it stays on disk for cold storage, not version-controlled).
- **Originals in `Spring 2026/` are untouched.** This is fully reversible until Part 5.

The two `.git/` folders I created have stuck lock files. Part 2 deletes and re-inits them cleanly, so don't worry about them.

---

## Part 1 — Snapshot the Spring repo (clears the stale lock)

```bash
cd ~/Documents/Claude/Projects/"Spring 2026"
rm -f .git/index.lock
git add -A && git commit -m "pre-migration snapshot 2026-06-24" && git push
```

## Part 2 — Re-init the two new repos cleanly

```bash
cd ~/Documents/Claude/Projects
rm -rf TeachingAssistant/.git Teaching/.git      # remove the sandbox's stuck repos

cd TeachingAssistant
git init && git add -A && git commit -m "init perpetual teaching system"

cd ../Teaching
git init && git add -A && git commit -m "init teaching home; Spring 2026 archived on disk"
```
After the Teaching commit, confirm the archive was NOT committed (should print nothing):
```bash
git ls-files | grep "Spring 2026/" ; echo "^ empty = archive correctly excluded"
```

## Part 3 — Create the GitHub repos and push (matches your spring-2026 style)

Create two **private** repos on github.com: `teaching-assistant` and `teaching`. Then:
```bash
cd ~/Documents/Claude/Projects/TeachingAssistant
git remote add origin https://github.com/vyassreenivas/teaching-assistant.git
git push -u origin main

cd ../Teaching
git remote add origin https://github.com/vyassreenivas/teaching.git
git push -u origin main
```

## Part 4 — Nightly backups for the new repos

Clone your existing tooling (`Spring 2026/.tooling/spring2026-backup.sh` + the launchd plist) once per new repo: copy the script, change its `REPO_DIR` to the new path, copy the plist with a new `Label` (e.g. `com.vyas.teaching-backup`) and a staggered time, then `launchctl load` it. I can generate these two script+plist pairs for you in-session if you want.

## Part 5 — Verify, then delete originals (IRREVERSIBLE — do last)

Only after Parts 1-3 succeed and you've eyeballed `Projects/Teaching/` and `Projects/TeachingAssistant/`:
```bash
cd ~/Documents/Claude/Projects/"Spring 2026"
rm -rf MGMT162 MGMT165 TeachingAssistant
# plus the now-archived loose files:
rm -f "Pulse Survey 1 - MGMT162.docx" "Pulse Survey 1 - MGMT165.docx" next_week_open_points.md
git add -A && git commit -m "migration: teaching moved to Projects/Teaching + Projects/TeachingAssistant" && git push
```

---

## What Claude will do in-session (just say go)

- Update `Spring 2026/CLAUDE.md` (master): drop MGMT162/MGMT165 from the folder layout and "six subfolders"; point teaching to `Projects/Teaching/` and the system to `Projects/TeachingAssistant/`.
- Trim the dead course-specific FERPA/HBP rules out of `Spring 2026/.gitignore` (they now live in the Teaching repo).
- Generate the two backup script+plist pairs for Part 4.

I'll hold off on those edits until your snapshot (Part 1) is pushed, so the master repo has a clean restore point first.
