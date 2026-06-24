# TeachingAssistant — Meta README

This folder contains a **model-agnostic, self-learning teaching assistant system** that generates a complete LLM-powered course brain from three inputs: a weekly plan Excel, a student roster, and a small config file.

---

## Folder structure

```
TeachingAssistant/
├── CLAUDE.md               (this file)
├── templates/               (parameterized templates for brain/ files)
│   ├── ASSISTANT.md.template
│   └── memory.md.template
├── shared/                  (protocol files copied into every brain/)
│   ├── set_protocol.md
│   ├── weekly_rhythm.md
│   ├── contingency.md
│   └── skill_log.md
├── generator/               (Python script that builds a brain/)
│   ├── generate_brain.py
│   └── requirements.txt
├── courses/                 (one subfolder per course instance)
│   └── example_config.yaml  (annotated config reference)
└── knowledge/               (persistent, grows across quarters)
    ├── playbook.md          (proven activities and patterns)
    ├── set_history.md       (SET scores across courses)
    └── master_skill_log.md  (consolidated craft observations)
```

## How to set up a new course

1. Create a folder under `courses/` (e.g., `courses/MGMT162_Fall2026/`)
2. Create `inputs/` inside it with:
   - `config.yaml` (copy from `example_config.yaml` and fill in)
   - `weekly_plan.xlsx` (your session-by-session plan)
   - `roster.xlsx` (student roster from registrar)
   - Optionally: `syllabus.pdf`, `rubrics/`, past SET CSV
3. Run: `python generator/generate_brain.py courses/MGMT162_Fall2026/`
4. The script produces a complete `brain/` folder ready for any LLM assistant.
5. Mount the course folder in your assistant (Cowork, ChatGPT, Codex, etc.) and start teaching.

## Design principles

- **Model-agnostic**: Everything is Markdown + JSON + Python. No vendor lock-in.
- **Self-learning**: Class logs and skill logs feed the knowledge/ playbook at end of quarter.
- **FERPA-safe**: Student names only in gitignored files. IDs everywhere else.
- **Minimal input**: Three files in, complete brain out. Five minutes to set up a new course.
