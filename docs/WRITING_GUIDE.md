# Writing Guide

Guidelines for creating exercises and lessons in this repository.

**Before writing:** Consult [REFERENCES.md](REFERENCES.md) for pedagogical context on your topic.

---

## Core Principles

### 1. Always Use Theme Placeholders

**Every exercise must contain at least one `{{placeholder}}`** for dynamic theming.

Available placeholders are documented in [TEMPLATE.md](../TEMPLATE.md):
- Characters: `{{hero}}`, `{{heroine}}`, `{{friend}}`, `{{mentor}}`, `{{villain}}`
- Places: `{{school}}`, `{{house}}`, `{{location}}`, `{{place}}`
- Abilities: `{{spell1}}` through `{{spell4}}`
- Objects: `{{creature}}`, `{{pet}}`, `{{item}}`, `{{transport}}`
- Phrases: `{{exclamation}}`, `{{greeting}}`, `{{password}}`

### 2. Teach Proper Python

- Follow PEP 8 conventions
- Use meaningful variable names (not single letters except `i` in loops)
- Explain trade-offs when multiple approaches exist
- Never oversimplify to the point of teaching bad habits

### 3. Progressive Complexity

Within each module:
1. Start with the simplest form of a concept
2. Each exercise introduces one new element
3. Later exercises combine concepts
4. Final exercises are integrative

---

## Exercise File Format

### File Naming

Pattern: `exercise_N_descriptive_name.py`

- Lowercase with underscores
- Numbered sequentially within a module
- Located in: `raw_exercises/{module}/{type}/`

### Standard Structure

```python
# Exercise N: Title Here
#
# Brief description of the concept being taught


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Instructions for this task
    # Hint: helpful guidance
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Next task in progression
    pass


def main():
    print("=== Exercise A: Description ===")
    exercise_a()

    print("\n=== Exercise B: Description ===")
    exercise_b()


main()
```

### Key Requirements

1. **✏️ marker** - Use `# ✏️ YOUR CODE HERE ✏️` to mark student code locations
2. **`pass` placeholder** - All student functions must contain `pass`
3. **Hints** - Include `# Hint: ...` when helpful
4. **`main()` function** - Call all exercises with clear output headers

---

## Lesson File Format

### Multi-Part Structure

Lessons are split into focused parts (3-8 minutes each):

```
lesson_module_X_topic_part_1.md  # Full context
lesson_module_X_topic_part_2.md  # Minimal context
...
lesson_module_X_topic_part_N.md  # Final part
```

### Part 1 Template

Use [en/lessons/TEMPLATE_PART1.md](../en/lessons/TEMPLATE_PART1.md):
- Prerequisites
- Learning Objective (single, focused)
- Key Concepts
- Lesson Content
- Practice Exercises
- Checkpoint
- If the Student Struggles
- Real-World Connection
- Notes for the LLM Teacher

### Parts 2+ Template

Use [en/lessons/TEMPLATE_PART.md](../en/lessons/TEMPLATE_PART.md):
- Learning Objective
- Key Concepts
- Lesson Content (with "Building on Part N-1")
- Practice Exercises
- Checkpoint
- If the Student Struggles

### Metadata Block

```markdown
> **Module**: module_X_name
> **Part**: N of M
> **Difficulty**: [1-3]
> **Duration**: [3-8] minutes
```

---

## Quality Standards

### What to Avoid

1. **Over-engineering** - Keep solutions simple and focused
2. **Hiding complexity** - Show the steps, don't abstract them away
3. **Features before teaching** - Don't use concepts not yet introduced
4. **Unnecessary error handling** - Only validate at system boundaries

### Checklist Before Committing

#### Exercises
- [ ] Contains at least one `{{placeholder}}`
- [ ] Uses `pass` as placeholder
- [ ] Instructions use ✏️ marker
- [ ] `main()` function calls all exercises
- [ ] Code follows PEP 8
- [ ] Hebrew translations in `convert_exercises.py`
- [ ] Progressive difficulty within module

#### Lessons
- [ ] Both English and Hebrew versions exist
- [ ] Part metadata is correct
- [ ] Single, focused learning objective per part
- [ ] Practice exercises reference valid files
- [ ] Part 1 has Prerequisites and Real-World Connection

---

## Generating Output Files

### After modifying exercises:

```bash
python scripts/convert_exercises.py
```

This reads `.py` files from `raw_exercises/` and generates:
- `exercises.json` per module
- `manifest.json` with module list
- Updated `version.json`

### After modifying lessons:

```bash
python scripts/build_lessons_json.py
```

This reads `.md` files from `{lang}/lessons/` and generates `lessons.json`.

---

## Adding New Content

### New Module

1. Create directory: `raw_exercises/module_N_topic/`
2. Update `exercises_config.json` with module metadata
3. Update `scripts/convert_exercises.py` with translations
4. Create lesson files in `en/lessons/` and `he/lessons/`
5. Run both generation scripts

### New Exercise Type

1. Create template in `templates/template_{type}.py`
2. Update `templates/EXERCISE_TYPE_MODULE_MAPPING.md`
3. Add translations to `exercises_config.json`
4. Create exercises in appropriate modules

---

## Anti-Patterns

### Don't Do This

```python
# Too much abstraction for beginners
class ExerciseValidator:
    def __init__(self, validator_func):
        self.validate = validator_func
```

```python
# Magic that hides learning
from our_helper import do_everything
do_everything()
```

```python
# Skipping error handling when it matters
number = int(input("Enter a number: "))  # Could crash!
```

### Do This Instead

```python
# Direct and clear
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer
```

```python
# Show the steps
user_input = input("Enter text: ")
words = user_input.split()
count = len(words)
print(f"Word count: {count}")
```

```python
# Proper error handling at input boundaries
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
```

---

## Theme Testing

Verify no hardcoded theme references:

```bash
python scripts/apply_theme_placeholders.py --raw --check
```
