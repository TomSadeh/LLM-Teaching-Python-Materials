# Claude Code Guidelines

Python exercises for Maya Chat, a teaching app with dynamic theming.

## Before Creating or Editing Content

**Always load relevant context before writing:**

1. **Read** [docs/WRITING_GUIDE.md](docs/WRITING_GUIDE.md) for format and style rules
2. **Search** [docs/CATALOG.md](docs/CATALOG.md) to understand existing content
3. **Search** [docs/REFERENCES.md](docs/REFERENCES.md) for pedagogical context on the topic
4. **Load** the relevant template from [templates/](templates/)

---

## After Creating or Editing Content

**Always update documentation after changes:**

### Single Exercise Checklist
- [ ] Run `python scripts/convert_exercises.py`
- [ ] Verify exercise appears in generated JSON
- [ ] Add Hebrew translation to `convert_exercises.py` if new

### Batch of Exercises Checklist
- [ ] Run `python scripts/convert_exercises.py`
- [ ] Update [docs/CATALOG.md](docs/CATALOG.md) if new exercise type or module
- [ ] Add Hebrew translations to `convert_exercises.py`

### Single Lesson Checklist
- [ ] Create both `en/` and `he/` versions
- [ ] Run `python scripts/build_lessons_json.py`
- [ ] Verify lesson appears in `lessons.json`

### Batch of Lessons Checklist
- [ ] Create both `en/` and `he/` versions for all
- [ ] Run `python scripts/build_lessons_json.py`
- [ ] Update [docs/CATALOG.md](docs/CATALOG.md) lesson table

### New Module Checklist
- [ ] Create `raw_exercises_new/module_N_topic/` directory
- [ ] Add module to `exercises_config.json`
- [ ] Add translations to `scripts/convert_exercises.py`
- [ ] Create lesson files in `en/lessons/` and `he/lessons/`
- [ ] Update [docs/CATALOG.md](docs/CATALOG.md) modules table
- [ ] Update [docs/REFERENCES.md](docs/REFERENCES.md) lookup tables
- [ ] Run both generation scripts

### New Exercise Type Checklist
- [ ] Create template in `templates/exercise_types/{type}.py`
- [ ] Update [templates/EXERCISE_TYPE_MODULE_MAPPING.md](templates/EXERCISE_TYPE_MODULE_MAPPING.md)
- [ ] Update [docs/CATALOG.md](docs/CATALOG.md) exercise types section
- [ ] Add type translations to `exercises_config.json`

---

## Quick Reference

| Need | Document |
|------|----------|
| Content inventory | [docs/CATALOG.md](docs/CATALOG.md) |
| Writing exercises/lessons | [docs/WRITING_GUIDE.md](docs/WRITING_GUIDE.md) |
| Narrative archetypes | [docs/NARRATIVE_ARCHETYPES.md](docs/NARRATIVE_ARCHETYPES.md) |
| Archetype quick templates | [templates/ARCHETYPE_QUICK_REFERENCE.md](templates/ARCHETYPE_QUICK_REFERENCE.md) |
| Archetype visual guide | [docs/ARCHETYPE_VISUAL_GUIDE.md](docs/ARCHETYPE_VISUAL_GUIDE.md) |
| Curriculum & pedagogy | [docs/REFERENCES.md](docs/REFERENCES.md) |
| Theme placeholders | [TEMPLATE.md](TEMPLATE.md) |
| Exercise type templates | [templates/exercise_types/](templates/exercise_types/) |
| Activity patterns (task-level) | [templates/activity_patterns/](templates/activity_patterns/) |
| Structure patterns (exercise-level) | [templates/structure_patterns/](templates/structure_patterns/) |
| Hybrid arcs | [templates/hybrid_arcs/](templates/hybrid_arcs/) |
| Exercise type mapping | [templates/EXERCISE_TYPE_MODULE_MAPPING.md](templates/EXERCISE_TYPE_MODULE_MAPPING.md) |
| Raw reference files | [references/](references/) |
| Lesson templates | [en/lessons/TEMPLATE_PART1.md](en/lessons/TEMPLATE_PART1.md) |
| Theme system | [docs/THEME_SYSTEM.md](docs/THEME_SYSTEM.md) |
| Create a theme | [docs/QUICK_START_THEMES.md](docs/QUICK_START_THEMES.md) |
| Narrative templates | [docs/NARRATIVE_SYSTEM.md](docs/NARRATIVE_SYSTEM.md) |
| Module recreation plan | [docs/META_PLAN_MODULE_RECREATION.md](docs/META_PLAN_MODULE_RECREATION.md) |

---

## Core Rules

### 1. No Hardcoded Theme References

Use `{{placeholder}}` syntax. See [TEMPLATE.md](TEMPLATE.md) for available variables.

**Every exercise must contain at least one placeholder.**

### 2. Teach Proper Python

- Follow PEP 8
- Use meaningful variable names
- No shortcuts or oversimplification
- Explain trade-offs

### 3. Progressive Complexity

Each exercise within a module should introduce one new element.

---

## Repository Structure

```
LLM-Teaching-Python-Materials/
├── raw_exercises_new/          # Source exercise files (recreated)
│   └── module_X_topic/
│       └── {exercise_type}/
│           └── exercise_N_name.py
├── templates/                  # Exercise type templates
├── en/lessons/                 # English lessons (multi-part)
├── he/lessons/                 # Hebrew lessons
├── references/                 # Curriculum analysis
├── docs/                       # Documentation
├── scripts/                    # Build scripts
├── theme_mappings/             # Theme definitions (one JSON per theme)
│   ├── _TEMPLATE.json          # Complete placeholder reference
│   └── *.json                  # Individual theme files
├── exercises_config.json       # Module/exercise translations
├── manifest.json               # Module list for sync
└── version.json                # Content version
```

---

## Common Tasks

### Add/modify exercises

1. Edit files in `raw_exercises_new/{module}/{type}/`
2. Run: `python scripts/convert_exercises.py`

### Add/modify lessons

1. Edit files in `en/lessons/` and `he/lessons/`
2. Run: `python scripts/build_lessons_json.py`

### Add new module

1. Create `raw_exercises_new/module_N_topic/`
2. Update `exercises_config.json`
3. Update `scripts/convert_exercises.py` with translations
4. Create lesson files in both languages
5. Run both scripts

### Verify no hardcoded themes

```bash
python scripts/audit_all_themes.py raw_exercises_new/
```

---

## Checklist

Before committing exercises:
- [ ] At least one `{{placeholder}}` per file
- [ ] All functions use `pass` placeholder
- [ ] Instructions use ✏️ marker
- [ ] `main()` calls all exercises
- [ ] Hebrew translations added
- [ ] Follows PEP 8

Before committing lessons:
- [ ] Both en and he versions exist
- [ ] Metadata block is correct
- [ ] Single objective per part
- [ ] Exercise references are valid
