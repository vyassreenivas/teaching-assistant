# MGMT162 Teaching Assistant — Operating Manual

> **This file is an index, not a manual.** It tells any LLM assistant where to find what, what rules to follow, and what files to load. Detailed protocols live in the linked files below.

---

## Quick start (load order)

Every conversation starts by reading these files in order:

1. `./course_tracker.json` — live state: schedule, action items, quiz tracker, key dates
2. `../students.json` — name-to-ID mapping (FERPA-protected, gitignored)
3. `./memory.md` — durable facts about this course and cohort
4. `./weekly_rhythm.md` — prep cadence, session design process, deadlines
5. `./set_protocol.md` — SET scores, mantras, pre/post-class checklists
6. `./skill_log.md` — teaching craft journal (what worked, what flopped)
7. `./contingency.md` — backup activities, pivot plans
8. Task-specific files as needed: `class_logs/`, `quiz_bank.md`, `exam_bank.md`, `class_prep_reference.md`, `archive_completed_actions.md`

---

## Course basics

| Field | Value |
|---|---|
| Course | MGMT 162: Strategic Analysis |
| Quarter | Spring 2026 |
| University | Santa Clara University |
| Instructor | Vyas Sreenivas |
| Section 2 | Tuesday, Thursday, 2:00-3:40 PM (~30 students) |
| Section 3 | Tuesday, Thursday, 5:40-7:20 PM (~20 students) |
| Class duration | 100 minutes |
| Total classes | 20 |
| First class | 2026-03-31 |
| Last class | 2026-06-04 |
| Midterm | Class 11 () |
| Capstone | Due Class 20 |
---

## Terminology

- **Class** = a scheduled meeting (Class 1, Class 2, ..., Class 20).
- **Section** = a group of students. Prep is done ONCE per class and taught to all sections. Post-class notes may vary by section.
- **Tracker** = `course_tracker.json`, the single source of truth for live state.
- **Class log** = raw post-class notes in `class_logs/class_NN.md`.

---

## Invariants (non-negotiable rules)

1. **FERPA compliance.** Student real names appear ONLY in `../students.json` (gitignored). Everywhere else — tracker, class logs, commit messages, any file that touches disk — use anonymized IDs: `s2_NNN`. If a name appears in a task description, stop and ask for the ID before writing.

2. **Tracker is single source of truth.** Edit it surgically (targeted field updates). Never regenerate the full JSON. Never delete action items — mark them `"status": "done"` and move to archive after ~2 weeks.

3. **`next_action_id` is monotonic.** Always increment, never reuse, never reset.

4. **Files are never deleted.** Move unwanted files to a `Delete/` staging folder for manual review.

5. **Licensed content is read-only.** Case packs, HBS articles, and purchased readings are never modified, copied, or quoted at length in any file that could be committed to git.

6. **Prep once per class, not per section.** Session plans, slides, quizzes, and activities are designed once. Section-specific tweaks (energy adjustments, pacing notes) go in the class log, not in separate prep.

7. **Post-class notes: sweep for names.** Before any git commit, verify that class logs and tracker entries contain IDs only, never student names.

---

## Folder map

```
MGMT162/
├── brain/                           [you are here — Claude/LLM operating layer]
│   ├── ASSISTANT.md                 [this file]
│   ├── course_tracker.json          [live state]
│   ├── memory.md                    [durable facts]
│   ├── weekly_rhythm.md             [prep cadence]
│   ├── set_protocol.md              [SET discipline]
│   ├── skill_log.md                 [craft journal]
│   ├── contingency.md               [backup plans]
│   ├── class_prep_reference.md      [per-class readings & activities]
│   ├── quiz_bank.md                 [running quiz question bank]
│   ├── exam_bank.md                 [midterm/final question bank]
│   ├── archive_completed_actions.md [resolved action items]
│   └── class_logs/                  [one file per class]
│       ├── class_01.md
│       └── ...
├── inputs/                          [setup files — gitignored]
│   ├── weekly_plan.xlsx             [session-by-session plan]
│   ├── roster.xlsx                  [student roster]
│   └── config.yaml                  [course configuration]
├── students.json                    [name→ID mapping — gitignored]
└── outputs/                         [generated deliverables]
    ├── canvas_pages/                [LMS announcements]
    ├── slides/                      [slide decks]
    ├── quizzes/                     [quiz documents]
    └── handouts/                    [activity sheets, rubrics]
```

---

## Interaction style

**Write-then-confirm, not propose-then-approve.** When the instructor asks to add a task, log something, or edit the tracker, write immediately and confirm in one line. The instruction IS the approval.

**Pause only when a safety check fires:** FERPA (student name needs an ID), licensed content risk, or genuine ambiguity. Ask one targeted question, get the answer, write, confirm. One round-trip.

**Response length scales with the task.** Task additions, status checks, quick lookups: 1–3 lines. Session design, triage, cross-class analysis: as long as needed.

---

## Tracker protocol

The tracker JSON holds: course metadata, class schedule (with status: upcoming/completed), quiz tracker, action items, and `next_action_id`.

**Adding an action item:**
```json
{
  "id": <next_action_id>,
  "created_date": "YYYY-MM-DD",
  "category": "<prep|admin|student|grading|SET|general>",
  "description": "...",
  "due_date": "YYYY-MM-DD or null",
  "status": "open",
  "resolved_date": null,
  "notes": "..."
}
```
Increment `next_action_id` after every addition.

**Completing an action item:** Set `"status": "done"` and `"resolved_date": "YYYY-MM-DD"`. After ~2 weeks, move to `archive_completed_actions.md`.

---

## Session design process (4 rounds)

When designing a class session, follow this sequence:

1. **Intent** — What should students walk out knowing/feeling/able to do?
2. **Energy** — What's the energy arc? (hook → build → peak → reflect)
3. **Activities** — What activities serve the intent and fit the energy?
4. **Timed plan** — Map activities to the 100-minute template.

The standard time template:
- Attendance + Agenda: 5 min
- Hook / Recap: 10 min
- Concept 1: 20 min
- Activity 1: 20 min
- Break: 5 min
- Concept 2 / Discussion: 20 min
- Activity 2: 10 min
- Recap + Preview: 10 min

---

## Pre-class checklist (run before every class)

- [ ] Agenda slide ready and will be displayed (SET Q1.2)
- [ ] Key takeaways identified for recap at end (SET Q1.2)
- [ ] Activities prepped, materials printed/uploaded (SET Q1.3)
- [ ] Any grading due within 7 days is posted or on track (SET Q1.7)
- [ ] Plan to mention office hours / availability (SET Q1.5, every 2 classes)
- [ ] Quiz ready if this is a case class (printed, Canvas version live)
- [ ] Slides reviewed, no student names visible
- [ ] Class log template ready (`class_logs/class_NN.md`)

## Post-class checklist (run after every class)

- [ ] Raw class notes dumped into `class_logs/class_NN.md`
- [ ] Class log swept for student names (replace with IDs)
- [ ] Tracker updated: class status → completed, any new action items added
- [ ] Skill log updated if something notable worked or flopped
- [ ] Look-ahead: is next class fully prepped? If not, add action item.

---

## SET discipline (5 mantras)

1. **Grade everything within 7 days.** This is the highest-leverage SET move.
2. **Display an agenda every class.** Organization (Q1.2) is visible and controllable.
3. **Say "my door is open" aloud every 2 classes.** Interaction (Q1.5) is built by repetition.
4. **Pulse survey at Classes 7–8 and 14–15, close the loop next class.** Students need to see their feedback acted on.
5. **Protect respect (Q1.6).** This is the superpower — never compromise it.

Detailed SET scores, targets, and milestone calendar are in `set_protocol.md`.

---

## Model-agnosticism note

This operating manual is designed to work with any LLM assistant (Claude, GPT, Codex, Gemini, or future models). It uses only markdown, JSON, and standard file operations. No vendor-specific features are assumed. The assistant reads files, follows instructions, and writes to the tracker and class logs. Platform-specific integrations (scheduled tasks, MCP tools, Canvas API) are optional layers on top — the core system works with just file access.

---

## Knowledge layer (optional, cross-course)

If a `../../knowledge/` folder exists, the assistant can search it for inspiration:
- `playbook.md` — proven activities, openers, debrief formats from past courses
- `set_history.md` — SET trends across courses and quarters
- `master_skill_log.md` — consolidated teaching craft observations

These files are read-only from the course instance. Updates happen at end-of-quarter retrospectives.
