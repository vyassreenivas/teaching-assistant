# Fall 2026 — Course Intake & Decisions

> Working spec for standing up the Fall 2026 teaching assistants. Captures what Vyas provides, the locked design decisions, and the build order. Update as decisions land.
> **Started:** 2026-06-23.

---

## Courses

| Course | Sections | Status vs Spring | Notes |
|---|---|---|---|
| **MGMT164** | 2 sections | New prep (no Spring instance) | One course brain, section-level data for both sections. Borrow structure from 162/165. |
| **MGMT165** | 1 section | Refresh (Spring 165 exists) | Keep course similar to Spring; apply the two changes below. |

One `courses/` folder per course. MGMT164's two sections live inside the single MGMT164 brain as a sections list, not as two separate brains (hold content constant, vary delivery — see master_skill_log).

---

## Inputs Vyas provides (per course)

These are the primary inputs from Vyas's side. He hands over the documents; Claude structures them into the generator's intake.

1. **Syllabus** (the course syllabus document).
2. **Week-by-week + session-by-session topic plan** (what gets covered each session).
3. **Learning objectives** (course-level and ideally per-unit).
4. **Textbook** for the course (164 and 165) — title/edition or the file.

Claude supplies (from the existing system): roster handling, brain scaffold, shared protocols, the consolidated knowledge layer, and the skills.

**Licensing note:** textbooks and any licensed readings stay gitignored (same rule as HBP cases). Reference them in the brain, never commit the file.

---

## Locked decisions

### D1 — MGMT165: start venture/customer check-ins BEFORE the midterm
Spring ran the team check-ins later. Fall moves them earlier so teams get in front of real customers early (customer discovery before, not after, the midpoint). This is a sequencing change to the 165 session plan; exact placement set once the session-by-session plan is in. Rationale: earlier customer contact = better ventures by Pitch Day, and it front-loads the highest-value coaching.

### D2 — Midterm goes digital: Camino + LockDown Browser (both courses, from now on)
Replaces the handwritten midterm. Delivery is on Camino with LockDown Browser.

**What changes (plumbing):**
- No more quiz scans, no handwriting OCR/transcription step.
- Question mix shifts to LMS-native: auto-graded MCQ and fill-in-the-blank, plus short-essay items graded manually in SpeedGrader.
- Watch the Spring SpeedGrader gotcha: essay items auto-score 0 until manually full-credited.

**What carries over from Spring 162/165 (methodology — keep verbatim):**
- Calibration-first: grade 3-5 to set the stance, document it in writing, then batch.
- "Generous middle" partial-credit stance; hold firm on misclassification and framework mislabels.
- Open-prompt key = principles + likely class examples + correct classification + explicit zero-rules (not one model answer).
- Borderline-within-0.5 flags with the deciding rounding rule named.
- 3-part feedback voice (strengths with evidence → gaps with a concrete better answer → forward guidance).

This change feeds both the `case-class-design` midterm-question generation and the planned `course-grader` skill.

### D3 — Learning objectives are the alignment spine (constructive alignment)
LOs drive everything. Each assessment (quiz, midterm, project, presentation, peer eval) maps to one or more LOs; each rubric criterion maps to an assessment. The brain holds an **LO → assessment → rubric coverage matrix** as instance data, and a coverage-check routine flags LOs that are taught but never assessed (or assessed but not taught).

- Doubles as **AACSB assurance-of-learning** (162 already has `AACSB Questions.xlsx` — same work, done once).
- Spring rubrics already exist: **ingest and align, don't rebuild.** Vyas brings the rubrics + LOs; Claude maps criteria → LOs and produces the coverage matrix + gap list.
- Caveat: alignment is only as sharp as the LOs. Item-level objectives ("diagnose five forces and predict margin pressure") map cleanly; vague ones ("understand strategy") don't constrain anything.

### D4 — Score prediction from the Camino/Canvas gradebook
A mode of `course-grader`. Input: gradebook export + syllabus weights. Output: each student's running and projected final letter at any point in term, plus an early-warning list for at-risk students. Method carries over from Spring: **quiz percentage as the primary predictor.** Reuses the export weight-validation routine.

---

## Build approach (do the thing, then skillify)

Per the gbrain principle (and Spring's own lesson): build the first course brain by hand from Vyas's docs, inspect it, then harden the generator to accept document-based intake. Don't pre-engineer the generator for inputs we haven't seen yet.

1. **Start with MGMT165** (refresh — lower risk, proves the pipeline against a known-good Spring instance).
2. Vyas drops the four inputs; Claude structures them into the generator's intake and produces `brain/`.
3. Inspect against Spring 165, apply D1 + D2.
4. Harden `generate_brain.py` from what the real intake looked like (closes the config-vs-Excel contradiction).
5. **Then MGMT164** (new prep) using the hardened pipeline.

---

## Deferred / scheduled threads (not now, but tracked)

- **Spring session video → transcript ingestion.** Download Spring session recordings, transcribe, feed into the knowledge layer and Fall session prep. Vyas plans this ~next week or the week after. Shape: an ingestion loop (like gbrain's media-ingest) → playbook / session-design input. Build the pipeline when the videos are in hand.
- **Standardize in-class recording via Granola** (or similar) going forward, so every Fall class produces a transcript automatically — same ingestion loop, live instead of retroactive. Feeds `debrief` and the playbook without the Spring archaeology problem.

## Open questions (resolve as we go)

- **164 assessment structure:** does it use the same scaffold as 162/165 (quizzes on case days, midterm, participation, peer eval, group project)? Need this to set its config.
- **164 content:** what is the course about, and what's the textbook? (New prep for Claude.)
- **Midterm placement:** which class number / date is the midterm in each course?
- **Rosters:** available now, or closer to term start? (Brain can be built without; roster slots in later.)
- **165 check-in timing:** exact sessions for the early check-ins, set once the session plan is in.

---

## D5 — MGMT165 gold standard: replicate Spring 2026, not Fall 2025

For Fall 2026 MGMT165, the template is **Spring 2026** (TtH 10:20 section). Evidence: Spring drew strong unsolicited student praise and Vyas gave fast, detailed feedback throughout (Claude-assisted). **Fall 2025** had weak SET scores and thin feedback — it is the cautionary baseline, used to learn what to avoid, not to copy. Spring 2026 SET scores are not in yet; revisit when they land, but the qualitative signal + the Fall-vs-Spring feedback contrast is strong enough to set Spring as the model now.

**The causal lever to preserve:** fast + detailed feedback. This is the single biggest driver of the Spring reception and is exactly what the grading/feedback workflow (course-grader skill) exists to make sustainable. Fall 165 must protect the feedback turnaround above almost everything else.

Reconstructed Spring 2026 165 skeleton (from the .imscc): 20 sessions, weights = Participation 20 / Case Presentation 10 / Case Challenge 10 / Quizzes 10 / Midterm 20 / BMC 10 / Final Pitch 20; customer-discovery spine Sessions 1-9, midterm S10, build-and-pitch S11-19; guest speakers S6 (Karen Runde) + S12 (Morgan Slain).
