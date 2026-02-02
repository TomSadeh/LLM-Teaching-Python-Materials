# Writing Guide

Guidelines for creating theme-agnostic exercises and lessons.

**Before writing:**
- Read [REFERENCES.md](REFERENCES.md) for pedagogical context
- Review [theme_mappings/_TEMPLATE.json](../theme_mappings/_TEMPLATE.json) for available placeholders
- Check [NARRATIVE_SYSTEM.md](NARRATIVE_SYSTEM.md) for narrative template patterns

---

## The Three-Layer Theme System

Exercises use a three-layer placeholder system that makes them work with **any** theme:

### Layer 1: Entity Names

Simple noun replacements. Use for characters, places, and objects.

```python
name = "{{hero}}"           # → "Harry Potter" / "Captain Nova" / "Alex"
school = "{{school}}"       # → "Hogwarts" / "Starship Academy" / "Code Academy"
ability = "{{spell1}}"      # → "Lumos" / "sensor scan" / "debugging"
```

**Available Layer 1 placeholders:**

| Category | Placeholders |
|----------|-------------|
| Characters | `{{hero}}`, `{{heroine}}`, `{{friend}}`, `{{mentor}}`, `{{villain}}` |
| Places | `{{school}}`, `{{house}}`, `{{location}}`, `{{place}}` |
| Abilities | `{{spell1}}`, `{{spell2}}`, `{{spell3}}`, `{{spell4}}` |
| Objects | `{{creature}}`, `{{pet}}`, `{{item}}`, `{{transport}}` |
| Phrases | `{{group}}`, `{{exclamation}}`, `{{greeting}}`, `{{password}}` |

### Layer 2: Context Blocks

Full sentences that provide narrative framing. Use for introductions, instructions, and feedback.

```python
# {{CONTEXT_INTRO}}
# → "Welcome to Hogwarts! Your magical education continues..."
# → "Welcome aboard, Cadet! All crew must complete training..."
# → "Let's build this step by step."
```

**Key Layer 2 placeholders:**

| Category | Placeholders |
|----------|-------------|
| Introductions | `{{CONTEXT_INTRO}}`, `{{CONTEXT_PROJECT_INTRO}}`, `{{CONTEXT_ROLE_INTRO}}` |
| Learning | `{{CONTEXT_LEARNING_OBJECTIVE}}`, `{{CONTEXT_STUDENT_TASK}}` |
| Guidance | `{{CONTEXT_SUCCESS_CRITERIA}}`, `{{CONTEXT_IMPLEMENTATION_GUIDANCE}}` |
| Completion | `{{CONTEXT_ROLE_COMPLETE}}`, `{{CONTEXT_FINAL_ASSEMBLY}}` |

See [theme_mappings/_TEMPLATE.json](../theme_mappings/_TEMPLATE.json) for complete list.

### Layer 3: Framework Concepts

Structural terms that define how the universe works. Use sparingly in meta-descriptions.

```python
# As a {{PRACTITIONER_SINGULAR}}, you'll learn {{ABILITY_TYPE}}
# → "As a wizard, you'll learn magic"
# → "As an engineer, you'll learn engineering"
```

---

## Core Principles

### 1. Theme-Agnostic by Default

**Every exercise must work perfectly with ANY theme.**

The Python code is identical. Only the narrative context changes.

```python
# GOOD: Theme-agnostic
def create_profile():
    """Create a profile for {{hero}}."""
    profile = {
        "name": "{{hero}}",
        "skill": "{{spell1}}"
    }
    return profile

# BAD: Theme-locked
def create_wizard():
    """Create a wizard profile."""  # "wizard" locks to fantasy
    profile = {
        "name": "Harry",            # Hardcoded name
        "spell": "Lumos"            # Hardcoded ability
    }
    return profile
```

### 2. Use Context Blocks for Narrative

Don't write narrative directly. Use context block placeholders.

```python
# GOOD: Context block placeholder
# {{CONTEXT_INTRO}}
# {{CONTEXT_STUDENT_TASK}}

# BAD: Hardcoded narrative
# Welcome to Hogwarts! Today you'll learn to cast spells.
```

### 3. Teach Proper Python

- Follow PEP 8 conventions
- Use meaningful variable names (not single letters except `i` in loops)
- Explain trade-offs when multiple approaches exist
- Never oversimplify to the point of teaching bad habits

### 4. Progressive Complexity

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
- Numbered sequentially within exercise type
- Located in: `exercises/{module}/{type}/`

### Directory Structure

```
exercises/
└── module_N_topic/
    ├── write_code/
    │   └── exercise_1_name.py
    ├── bug_hunt/
    │   └── exercise_1_name.py
    ├── decode_error/
    │   └── exercise_1_name.py
    ├── output_prediction/
    │   └── exercise_1_name.py
    ├── complete_function/
    │   └── exercise_1_name.py
    └── which_is_better/
        └── exercise_1_name.py
```

### Standard Exercise Structure

```python
"""
{{CONTEXT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    """{{PHASE_1_DESCRIPTION}}"""
    # ✏️ YOUR CODE HERE ✏️
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Hint: {{CONTEXT_IMPLEMENTATION_GUIDANCE}}
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    """{{PHASE_2_DESCRIPTION}}"""
    # ✏️ YOUR CODE HERE ✏️
    pass


def main():
    print("{{CONTEXT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    exercise_a()

    print("\n=== {{PHASE_2_TITLE}} ===")
    exercise_b()

    print("=" * 50)
    print("{{CONTEXT_ROLE_COMPLETE}}")


main()
```

### Key Requirements

| Requirement | Description |
|-------------|-------------|
| `✏️` marker | Use `# ✏️ YOUR CODE HERE ✏️` to mark student code locations |
| `pass` placeholder | All student functions must contain `pass` |
| Context blocks | Use `{{CONTEXT_*}}` for all narrative text |
| Entity placeholders | Use `{{hero}}`, `{{school}}`, etc. for all theme-specific nouns |
| `main()` function | Call all exercises with clear output headers |
| Hints | Include guidance using `{{CONTEXT_IMPLEMENTATION_GUIDANCE}}` |

---

## Exercise Types and Templates

Each exercise type has a corresponding narrative template. Match your exercise to the right template.

| Exercise Type | Narrative Template | Use When |
|--------------|-------------------|----------|
| `write_code` | Tutorial Guide, Incremental Builder | Teaching new concepts |
| `bug_hunt` | Forensic Debugger | Finding and fixing bugs |
| `decode_error` | Forensic Debugger | Understanding error messages |
| `output_prediction` | Prediction Challenger | Testing mental execution |
| `complete_function` | Specification Implementer | Building from specs |
| `which_is_better` | Comparison Analyst | Comparing approaches |
| `code_tracing` | Table Tracer | Tracking state changes |
| `fix_style` | Quality Auditor | Improving code quality |

See [NARRATIVE_SYSTEM.md](NARRATIVE_SYSTEM.md) for detailed template structures.

---

## Writing for Specific Exercise Types

### write_code (Incremental Builder)

Build complexity across multiple sub-exercises.

```python
"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_INCREMENTAL_NARRATIVE}}
"""

# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}

def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a dictionary for {{hero}} with:
    # - "name": "{{hero}}"
    # - "skill": "{{spell1}}"
    pass

# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}

def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Access and print the skill from the dictionary
    pass
```

### bug_hunt (Forensic Debugger)

Present broken code for students to fix.

```python
"""
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_MISSION}}
"""

# ============================================================
# {{CASE_1_TITLE}}
# ============================================================
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# ERROR MESSAGE:
# KeyError: 'level'
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

def case_1_buggy():
    """This code has a bug. Find it!"""
    character = {"name": "{{hero}}", "health": 100}
    print(f"Level: {character['level']}")  # 🐛 BUG!


# ✏️ FIX THE CODE ✏️
def case_1_fixed():
    """Fixed version."""
    pass
```

### output_prediction (Prediction Challenger)

Students predict output before running.

```python
"""
{{CONTEXT_PREDICTION_INTRO}}
{{CONTEXT_PREDICTION_PURPOSE}}
"""

# ============================================================
# {{CHALLENGE_1_TITLE}}
# ============================================================
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}
#
# ✏️ YOUR PREDICTION ✏️
# What will this code print? Write your answer BEFORE running:
#
# Line 1: _______________
# Line 2: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_1}}

def challenge_1():
    items = ["{{item}}", "potion", "key"]
    print(f"First item: {items[0]}")
    print(f"Total items: {len(items)}")
```

### which_is_better (Comparison Analyst)

Compare two approaches and analyze tradeoffs.

```python
"""
{{CONTEXT_COMPARISON_INTRO}}
{{CONTEXT_COMPARISON_DECISION}}
"""

# ============================================================
# {{APPROACH_1_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_1_NARRATIVE}}

def approach_a():
    """Flat structure."""
    data = {
        "hero_name": "{{hero}}",
        "hero_health": 100,
        "hero_skill": "{{spell1}}"
    }
    return data


# ============================================================
# {{APPROACH_2_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_2_NARRATIVE}}

def approach_b():
    """Nested structure."""
    data = {
        "hero": {
            "name": "{{hero}}",
            "health": 100,
            "skill": "{{spell1}}"
        }
    }
    return data


# ============================================================
# ✏️ YOUR ANALYSIS ✏️
# ============================================================
# {{CONTEXT_ANALYSIS_PROMPT}}
#
# Which approach do you prefer and why?
# Consider: {{CONTEXT_DECISION_GUIDANCE}}
```

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

| Anti-Pattern | Why It's Bad |
|--------------|--------------|
| Hardcoded theme references | Locks exercise to one theme |
| Over-engineering | Confuses beginners |
| Hiding complexity | Prevents learning |
| Features before teaching | Uses concepts not yet introduced |
| Unnecessary error handling | Adds noise without value |

### Checklist Before Committing

#### Exercises
- [ ] All narrative uses `{{CONTEXT_*}}` placeholders
- [ ] All nouns use Layer 1 placeholders (`{{hero}}`, `{{school}}`, etc.)
- [ ] No hardcoded theme references (no "wizard", "spell", "Hogwarts", etc.)
- [ ] Uses `pass` as placeholder in all student functions
- [ ] Instructions use `✏️` marker
- [ ] `main()` function calls all exercises
- [ ] Code follows PEP 8
- [ ] Hebrew translations added to `convert_exercises.py`
- [ ] Progressive difficulty within module

#### Lessons
- [ ] Both English and Hebrew versions exist
- [ ] Part metadata is correct
- [ ] Single, focused learning objective per part
- [ ] Practice exercises reference valid files
- [ ] Part 1 has Prerequisites and Real-World Connection

---

## Adding Context Blocks to Themes

When you create exercises using new context block placeholders, add them to theme files.

### Location

Theme definitions live in `theme_mappings/`:

```
theme_mappings/
├── _TEMPLATE.json              # Blank template (don't edit)
├── _EXAMPLE_fantasy_complete.json  # Reference example
├── THEME_CREATOR_GUIDE.md      # Documentation
├── fantasy_magic.json          # Fantasy theme
├── scifi_engineering.json      # Sci-fi theme
└── professional_coding.json    # Plain coding theme
```

### Adding a New Context Block

1. Add the placeholder to your exercise:
   ```python
   # {{CONTEXT_NEW_BLOCK}}
   ```

2. Add values for each theme in `theme_mappings/*.json`:
   ```json
   {
     "layer_2_context_blocks": {
       "introduction": {
         "CONTEXT_NEW_BLOCK": "Your theme-specific text here"
       }
     }
   }
   ```

3. Update `_TEMPLATE.json` to document the new placeholder.

---

## Generating Output Files

### After modifying exercises:

```bash
python scripts/convert_exercises.py
```

This reads `.py` files from `exercises/` and generates:
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

1. Create directory: `exercises/module_N_topic/`
2. Create exercise type subdirectories as needed
3. Update `exercises_config.json` with module metadata
4. Update `scripts/convert_exercises.py` with translations
5. Create lesson files in `en/lessons/` and `he/lessons/`
6. Run both generation scripts

### New Exercise Type

1. Create template in `templates/exercise_types/{type}.py`
2. Update `templates/EXERCISE_TYPE_MODULE_MAPPING.md`
3. Add translations to `exercises_config.json`
4. Document in [NARRATIVE_SYSTEM.md](NARRATIVE_SYSTEM.md)
5. Create exercises in appropriate modules

---

## Quick Reference

| Need | Document |
|------|----------|
| All placeholders | [theme_mappings/_TEMPLATE.json](../theme_mappings/_TEMPLATE.json) |
| Narrative templates | [NARRATIVE_SYSTEM.md](NARRATIVE_SYSTEM.md) |
| Theme creation | [theme_mappings/THEME_CREATOR_GUIDE.md](../theme_mappings/THEME_CREATOR_GUIDE.md) |
| Complete example | [theme_mappings/_EXAMPLE_fantasy_complete.json](../theme_mappings/_EXAMPLE_fantasy_complete.json) |
| Exercise type templates | [templates/](../templates/) |
| Pedagogical context | [REFERENCES.md](REFERENCES.md) |
