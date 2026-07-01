# Teaching Assistant — Architecture & Lifecycle

> How the whole system is built and how it flows from your syllabus to the end of a quarter, and how it improves itself session to session and quarter to quarter.
> **Model in one line:** fat skills, thin harness, compounding knowledge. The course brain is a thin router holding one course's state; skills are the reusable capabilities; loops run them on a cadence; the knowledge layer is the memory that makes each quarter start smarter than the last.

There are two ways to see it. The **static view** is what the pieces are (the five layers). The **dynamic view** is how they flow start to end, and where the improvement loops live. Read the dynamic view if you want the story; the static view is the reference.

---

## STATIC VIEW — the five layers

```
┌─────────────────────────────────────────────────────────────┐
│  KNOWLEDGE (compounding, lives in TeachingAssistant/)         │  ← read at generation + during loops
│  master_skill_log · playbook · feedback_voice · set_history   │  ← written at end-of-term consolidation
└─────────────────────────────────────────────────────────────┘
            ▲ read                              ▼ written
┌─────────────────────────────────────────────────────────────┐
│  HARNESS (thin, one per course: Teaching/<term>/<course>/)    │
│  brain/ = CLAUDE.md (rules) · memory.md · course_tracker.json │
│  · set_protocol · weekly_rhythm · contingency · banks · logs  │
└─────────────────────────────────────────────────────────────┘
            ▲ dispatches to                     ▲ calls
┌──────────────────────────────┐   ┌──────────────────────────┐
│  SKILLS (fat, reusable)       │   │  ROUTINES (primitives)    │
│  case-class-design            │   │  FERPA leak-check         │
│  course-grader (to build)     │   │  export weight-validation │
│  case-presentation-grader     │   │  calibration-first grade  │
│  debrief                      │   │  borderline flagging      │
│  peer-eval-pipeline (to build)│   │  atomic tracker write     │
└──────────────────────────────┘   └──────────────────────────┘
            ▲ orchestrated on a cadence by
┌─────────────────────────────────────────────────────────────┐
│  LOOPS (cadenced processes — the "when")                      │
│  per-session · grading · weekly · mid-quarter · end-of-term   │
└─────────────────────────────────────────────────────────────┘
```

- **Harness (thin).** The per-course `brain/`. Knows nothing about *how* to grade or design a class. It holds *this* course's state: rules, durable facts (`memory.md`), live state (`course_tracker.json`), the SET targets, the weekly rhythm, the quiz/exam banks, and the class logs. One per course, lives in `Teaching/<term>/<course>/`.
- **Skills (fat).** Self-contained, course-agnostic capabilities. Each reads instance data from the brain and shared rules from the knowledge layer. The "what to do." Exist today: `case-class-design`, `case-presentation-grader`, `debrief`. To build: `course-grader`, `peer-eval-pipeline`.
- **Loops.** Cadenced processes that orchestrate skills on a schedule. The "when." This is the part you asked to add, detailed below.
- **Routines.** Shared sub-skill primitives so every skill doesn't reinvent them. The "how," at the step level. Live as one reference, called by many skills.
- **Knowledge (compounding).** The permanent memory. `master_skill_log.md` (craft), `playbook.md` (activities), `feedback_voice.md` (your grading voice — just built), `set_history.md` (eval scores). Read when a brain is generated and during loops; written at end-of-term. This is the layer that makes the system improve.

---

## DYNAMIC VIEW — the lifecycle, start to end

### Phase 0 — Inputs (YOUR starting point)
Everything flows from what you drop into `Teaching/<term>/<course>/inputs/`:
- **Syllabus**, **session-by-session plan**, **learning objectives**, **textbook** — the new course.
- **Prior-instance reference** (`prior_reference/`): the Canvas `.imscc` export, class transcripts, your final grading comments — what the system learns your style from.
- **Roster** (when available).

This is the only heavy lift that's yours. Everything downstream is generated or assisted.

### Phase 1 — Generate the brain (the generator runs once per course)
`generator/generate_brain.py` reads your inputs **plus the knowledge layer** (so the course is born knowing what prior quarters learned: the playbook activities, your feedback voice, the craft lessons, SET targets) **plus** the shared protocols and templates. It produces:
- the `brain/` (rules, memory, tracker seeded with the schedule + assessments, SET protocol, weekly rhythm, contingency, banks), and
- `canvas_pages/` (the Camino pages, modeled on your prior course's structure).

Output: a complete, ready-to-mount course assistant.

### Phase 2 — Teach (the PER-SESSION LOOP, repeats every class)
For each class, three beats:
1. **Prep** — `case-class-design` builds the session (discussion questions, quiz, activities, timed plan), pulling proven moves from the `playbook` and answering the 6-input prep checklist (concept, case, survey signal, last class, team status, logistics).
2. **Teach** — you run the class. (Transcript captured via Granola/Camino for the record.)
3. **Debrief** — `debrief` writes the class log, updates the tracker, appends a one-line `skill_log` entry, and runs a FERPA sweep — in one pass.

This loop is the **fast improvement engine** (see below).

### Phase 3 — Assess & give feedback (the GRADING LOOP, repeats per assessment)
Assignment due → `course-grader` (to build): ingest the Canvas export, validate effective weights, calibrate on 3-5, batch-grade, flag every borderline within 0.5, and produce both an instructor-review sheet and paste-ready comments **in your voice** (from `feedback_voice.md`, including the "Full marks. as a pivot" rule and scores-as-proposals). Return inside the 7-day SET clock. This loop is the lever that drove your strong Spring reception.

### Phase 4 — Mid-quarter (the FEEDBACK LOOP, once per term)
Pulse survey → analysis → a close-the-loop talk with **specific, falsifiable commitments** ("discussion questions before every quiz, starting today"). Honoring those commitments is the single highest-leverage teaching move on record.

### Phase 5 — End-of-term consolidation (the QUARTER-TO-QUARTER LOOP)
SET review + retrospective → distill this term's class logs and skill logs **up into the knowledge layer** (new playbook entries, craft lessons, SET history, a refreshed `feedback_voice`) → archive the term. This is the loop that makes the *next* generated brain smarter. **It is the loop that failed in Spring** (logs died at Class 11, so the back half had to be reconstructed). The fix is Phase 2's debrief, run every class.

---

## THE IMPROVEMENT ENGINE — two loops, one hinge

You asked for continuous improvement at two timescales. They are two distinct loops:

**Fast loop — session to session (within a term).**
`debrief` after every class → `class_logs/` + `skill_log.md` grow → next session's `case-class-design` prep reads them and the playbook. The course gets better *this* quarter: what flopped Tuesday is fixed by Thursday.

**Slow loop — quarter to quarter (across terms).**
End-of-term consolidation lifts the term's `skill_log` into the permanent knowledge layer → the next term's brain is *generated already knowing it*. Fall teaches the system things; Winter is born with them. The disk stays lean (old terms archive), but the learning compounds.

**The hinge that powers both: debrief discipline.** Both loops are fed by the same act — writing the class log and skill-log entry every session. Skip it and the fast loop degrades and the slow loop has nothing to consolidate (exactly what happened in Spring). So `debrief` from Day 1 is non-negotiable; everything compounds off it.

```
   Phase 0 inputs ─► Phase 1 generate ─► Phase 2 TEACH LOOP ─► Phase 3 GRADE LOOP ─► Phase 4 mid-qtr ─► Phase 5 consolidate
                          ▲                    │  ▲                                                          │
                          │                    └──┘  fast loop (debrief → logs → next prep)                 │
                          │                                                                                  │
                          └──────────────────  slow loop (consolidate → knowledge → next generation)  ◄──────┘
```

---

## Current state vs. to-build

- **Built & populated:** the generator, the brain template + shared protocols, `case-class-design` / `case-presentation-grader` / `debrief` skills, and the knowledge layer now holds a real `master_skill_log` and `feedback_voice`. Spring 165 is reconstructed as the gold-standard reference.
- **To build next:** `course-grader` (Phase 3 — the highest-value skill), the loop automations (scheduled tasks for the weekly/grading/end-of-term cadence), `peer-eval-pipeline`, and populating `playbook.md` from the Spring logs.
- **To wire:** point the generator at `Teaching/<term>/<course>/inputs/`, and decide which loops run as scheduled tasks vs. on-demand.
