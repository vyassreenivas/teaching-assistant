---
name: skill-index
description: Show the interface contracts for all custom teaching skills — what each one expects as input, what it produces, and how to trigger it. Use this skill whenever the user asks "what skills do I have", "skill index", "show me my skills", "what does [skill name] need", "how do I use [skill name]", "what are the inputs for [skill]", or any question about which skill to use for a task. Also trigger when the user seems unsure which skill fits their situation, says something like "I don't know which skill to use", or asks "what can you do". This is a quick-reference card, not a full skill loader — it tells the user what's available and how to call it.
---

# Skill Index — Quick Reference

You are showing the user a quick-reference card for their custom teaching skills. The goal is to help them know exactly what to say, what to have ready, and what they'll get back — so they never have to guess.

## When to use this skill

- The user asks what skills they have or what a specific skill does
- The user is unsure which skill fits their current task
- The user wants to know what inputs a skill needs before calling it
- The user asks "what can you do" in a teaching context

## What to do

Present the relevant skill interfaces from the reference below. If the user asked about a specific skill, show just that one. If they asked generally, show all of them. Keep it conversational — don't just dump the table. Help them pick the right skill if they're deciding.

If the user then wants to use one of the skills, tell them the trigger phrase and what to have ready. Don't load the skill yourself — let them call it naturally.

---

## The Skills

### debrief

**What it does:** Structured post-class extraction. Asks you targeted questions about what happened in class, then auto-generates a class log, tracker updates, skill log entry, and FERPA sweep.

**Say:** "debrief" or "class N done" or "log this class"
**Have ready:** Which course (MGMT162/165), which class number, which section(s)
**Bonus:** If you recorded with Granola, the transcript gets pulled automatically — you don't need to do anything
**You'll get:**
  1. `brain/class_logs/class_NN.md` — narrative class log
  2. `brain/course_tracker.json` — class marked completed, action items added
  3. `brain/skill_log.md` — craft insight logged (if one emerged)
  4. FERPA sweep confirmation
**Your time:** 3–5 minutes of answering questions

---

### case-class-design

**What it does:** Designs a full case-study class session — company research, discussion questions, quiz, activities, timed session plan, cross-case map, and midterm questions. Seven phases, can be done across multiple sittings.

**Say:** "prep the [Company] case" or "case prep for class N" or "quiz questions for [case]"
**Have ready:** Case name, which concept it teaches, class number/date
**Bonus:** Upload the case PDF and teaching note for dramatically better output. If a course prep prompt file exists (e.g., `MGMT162-case-prep-prompt.md`), it gets used automatically.
**You'll get:**
  1. Company research brief (videos, articles, post-case trajectory)
  2. 5–7 discussion questions with instructor notes
  3. Quiz pool (T/F + MC, you pick from the pool)
  4. Activity design (concept bridge + killer activity + closer)
  5. Timed session plan (minute-by-minute)
  6. Cross-case cumulative map
  7. Midterm question candidates
**Your time:** 20–40 minutes across phases (you pick and edit between phases)

---

### case-presentation-grader

**What it does:** Grades student case presentations and challenge teams against a fixed rubric. Produces feedback you can paste directly into Camino — written in your voice, not AI-speak.

**Say:** "grade this presentation" or "grade the challenge team" or "feedback on [team]'s presentation"
**Have ready:**
  - Presentation transcript (paste it or let Granola provide it)
  - Team roster (names + section)
  - Case name
  - Which to grade: presenting team, challenge team, or both
**Bonus:** Give a target score range (e.g., "high 80s") and it calibrates. Upload the slide deck for slides-criterion grading.
**You'll get:**
  1. Criterion-by-criterion feedback with scores (plain text, Camino-pasteable)
  2. Total score within your target range
  3. Instructor-only flags (things to know but not put in student feedback)
**Your time:** 5–10 minutes per team

---

### first-level-coding

**What it does:** Performs rigorous first-cycle qualitative coding on interview transcripts following Saldana's framework. Produces a coded document and an updated codebook every time.

**Say:** "code this interview" or "qualitative coding" or "first-level coding"
**Have ready:**
  - Interview transcript (upload the file)
  - Research question (type it or point to an existing codebook)
**Bonus:** For the 2nd+ interview, upload the existing codebook — it switches to cumulative mode and maintains cross-case consistency. You can also provide a deductive framework (a priori concepts to watch for).
**You'll get:**
  1. Coded interview document (segments, quotes, summaries, codes, rationales)
  2. Updated codebook (cumulative across interviews)
**Your time:** 15–30 minutes depending on transcript length

---

## Quick Reference Table

| Skill | Say this | Have this ready | Time |
|-------|---------|----------------|------|
| debrief | "debrief" / "class N done" | course + class # + section | 3–5 min |
| case-class-design | "prep the [X] case" | case + concept + date | 20–40 min |
| case-presentation-grader | "grade this presentation" | transcript + roster + case | 5–10 min |
| first-level-coding | "code this interview" | transcript + research question | 15–30 min |

---

## Which skill do I need?

If the user is deciding, use this decision tree:

- **Just finished teaching?** → debrief
- **Preparing for an upcoming case class?** → case-class-design
- **Have a presentation transcript to score?** → case-presentation-grader
- **Have an interview transcript for research?** → first-level-coding
- **Something else entirely?** → These four skills cover teaching workflow and qualitative research. For other tasks (documents, spreadsheets, PDFs, presentations), there are built-in skills for those — just describe what you need.
