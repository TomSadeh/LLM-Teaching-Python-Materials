# Writing Guide: Lessons

Guidelines for creating lesson files that guide LLM teachers.

**Before writing:** Load [REFERENCES.md](REFERENCES.md) for pedagogical context on the topic.

---

## Core Rules

### 1. One Objective Per Part

Each lesson part has a single, focused learning objective. If you need multiple objectives, split into separate parts.

### 2. Both Languages Required

Every lesson must exist in both `lessons/en/` and `lessons/he/`.

### 3. Valid Exercise References

All exercises referenced must exist in the `exercises/` directory.

---

## File Structure

**Location**: `lessons/{lang}/lesson_module_X_topic_part_N.md`

**Parts**: Split lessons into focused parts (3-8 minutes each).

---

## Templates

| Template | Use When |
|----------|----------|
| [LESSON_TEMPLATE_V2.md](../templates/LESSON_TEMPLATE_V2.md) | Primary template with OBSERVE/PRACTICE/CREATE/DEBUG phases |
| [lessons/en/TEMPLATE_PART1.md](../lessons/en/TEMPLATE_PART1.md) | First part (includes prerequisites, real-world connection) |
| [lessons/en/TEMPLATE_PART.md](../lessons/en/TEMPLATE_PART.md) | Subsequent parts (minimal context) |

---

## Required Metadata

```markdown
> **Module**: module_X_name
> **Part**: N of M
> **Difficulty**: [1-3]
> **Duration**: [3-8] minutes
```

---

## Lesson Flow (OBSERVE → PRACTICE → CREATE → DEBUG)

| Phase | Exercise Types | Goal |
|-------|---------------|------|
| OBSERVE | `output_prediction`, `match_output` | Read and predict before writing |
| PRACTICE | `fill_blanks`, `complete_function` | Scaffolded completion |
| CREATE | `write_code` | Independent writing |
| DEBUG (optional) | `decode_error`, `bug_hunt` | Error diagnosis |

---

## After Writing

1. Create both `lessons/en/` and `lessons/he/` versions
2. Run: `python scripts/build_lessons_json.py`
3. Verify lesson appears in `lessons.json`

---

## Checklist

- [ ] Both en and he versions exist
- [ ] Metadata block is correct
- [ ] Single objective per part
- [ ] Exercise references are valid
- [ ] Part 1 has Prerequisites and Real-World Connection
