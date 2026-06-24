# Skill Index — Teaching Assistant

Every skill is a function: clear trigger, clear inputs, clear outputs. This index tells you what each skill expects and what it produces, so you never have to guess.

---

## debrief

**What it does:** Structured post-class extraction → class log + tracker updates + skill log + FERPA sweep

**Trigger:** "debrief", "class debrief", "log this class", "class N done", "post-class", "just finished teaching"
**Required inputs:** Course (MGMT162 or MGMT165) + class number + section(s)
**Optional inputs:** Granola transcript (auto-pulled if available), raw notes dump
**Outputs:**
  1. `brain/class_logs/class_NN.md` — formatted narrative class log (FERPA-safe)
  2. `brain/course_tracker.json` — class status → completed, action items added
  3. `brain/skill_log.md` — entry appended (only if a transferable craft insight emerged)
  4. FERPA sweep confirmation
**Duration:** 3–5 min of your time
**Mode:** Conversational Q&A → file generation

---

## case-class-design

**What it does:** Designs a full case-study class session across 7 phases — from company research through midterm question generation

**Trigger:** "case prep", "design class for [case name]", "prep the [Company] case", "quiz questions for [case]", "midterm questions for [case]", "discussion questions for [case]"
**Required inputs:** Case name + concept it teaches + class number/date
**Optional inputs:** Case PDF, teaching note PDF, course prep prompt file (e.g., `MGMT162-case-prep-prompt.md`)
**Outputs:**
  1. Company research brief (videos, articles, post-case trajectory)
  2. 5–7 discussion questions with instructor notes
  3. Quiz pool (5–6 T/F + 8–10 MC, instructor picks from pool)
  4. Activity design (concept bridge + one killer activity + closer)
  5. Timed session plan (minute-by-minute table)
  6. Cross-case cumulative map (updated each time)
  7. Midterm question candidates (fill-in, T/F, MC, short essay)
**Duration:** 20–40 min across multiple phases (can be done across sessions)
**Mode:** Iterative — run phases in order, instructor picks/edits between phases

---

## case-presentation-grader

**What it does:** Grades student presentations and challenge teams against a fixed rubric, produces Camino-pasteable feedback in the instructor's voice

**Trigger:** "grade this presentation", "grade the challenge team", "feedback on [team]'s presentation", uploads a transcript + asks for grading
**Required inputs:**
  - Presentation transcript (text paste or Granola/Zoom export)
  - Team roster (names + section)
  - Case name
  - Which deliverable(s) to grade: presenting team, challenge team, or both
**Optional inputs:** Slide deck (PDF/PPTX), target score range (default: 85–92), course context (frameworks taught so far)
**Outputs:**
  1. Criterion-by-criterion feedback with scores (plain text, Camino-pasteable)
  2. Total score within target range
  3. Instructor-only flags (weird things to know but not put in student feedback)
**Duration:** 5–10 min per team
**Mode:** Read inputs → score → draft feedback → calibrate → deliver as plain text in chat

---

## first-level-coding

**What it does:** Performs rigorous first-cycle qualitative coding on interview transcripts following Saldana's framework

**Trigger:** "code this interview", "qualitative coding", "first-level coding", "open coding", uploads transcript + mentions research question
**Required inputs:**
  - Interview transcript (uploaded file)
  - Research question (typed or stored in existing codebook)
**Optional inputs:** Existing codebook (required for 2nd+ interview), deductive framework (a priori concepts)
**Outputs:**
  1. Coded interview document (segments, quotes, first-level summaries, codes, rationales — per `references/output_template.md`)
  2. Updated codebook (cumulative across interviews — per `references/codebook_template.md`)
**Duration:** 15–30 min depending on transcript length
**Mode:** Auto-detects Seed Mode (first interview, inductive) vs. Cumulative Mode (subsequent, hybrid). Produces both outputs every time.

---

## Quick reference table

| Skill | Trigger phrase | Key input | Key output | Time |
|-------|---------------|-----------|------------|------|
| debrief | "debrief" / "class N done" | course + class # | class log + tracker update | 3–5 min |
| case-class-design | "prep the [X] case" | case + concept + date | session plan + quiz + activities | 20–40 min |
| case-presentation-grader | "grade this presentation" | transcript + roster | Camino feedback + score | 5–10 min |
| first-level-coding | "code this interview" | transcript + RQ | coded doc + codebook | 15–30 min |
