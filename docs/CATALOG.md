# Content Catalog

This document catalogs all exercises, lessons, and reference materials in the repository.

## Modules

| Module | Topic | Difficulty | Description |
|--------|-------|:----------:|-------------|
| `module_0_basics` | Fundamentals | 1 | print, variables, math, input/output |
| `module_1_turtle_loops` | For Loops | 1 | Turtle graphics with for loops |
| `module_2_decisions` | Conditionals | 2 | if/elif/else, comparisons |
| `module_3_lists` | Lists | 2 | Lists, iteration, list methods |
| `module_4_functions` | Functions | 2 | Parameters, return values, code reuse |
| `module_5_games` | Games & While Loops | 2 | Building games with while loops and random |
| `module_6_final_project` | Integration | 3 | Capstone projects |
| `module_7_dictionaries` | Dictionaries | 2 | Keys, values, nested dicts |
| `module_8_modules` | Modules | 3 | Standard library, custom modules |
| `module_9_oop` | OOP | 3 | Classes, objects, inheritance |

---

## Exercise Types

### By Category

#### Reading (understand code)
- **output_prediction** - Predict what code will print
- **code_tracing** - Track variable values through execution
- **match_output** - Match code snippets to their outputs

#### Scaffolded Writing (guided creation)
- **write_code** - Write code following instructions
- **fill_blanks** - Complete code with missing pieces
- **code_ordering** - Arrange scrambled code correctly
- **complete_function** - Implement function body from signature

#### Improvement (make code better)
- **fix_style** - Apply PEP 8 conventions
- **simplify_code** - Refactor for clarity
- **add_error_handling** - Add try/except blocks

#### Analysis (compare and evaluate)
- **which_is_better** - Compare working solutions
- **spot_difference** - Find subtle bugs between versions

#### Debugging (find and fix)
- **decode_error** - Interpret error messages
- **bug_hunt** - Find and fix bugs in narrative context

#### Free Writing (independent creation)
- **blank_page** - Write from docstrings/specifications only
- **mini_project** - Combine scaffolded + creative elements

### Type-Module Matrix

See [templates/EXERCISE_TYPE_MODULE_MAPPING.md](../templates/EXERCISE_TYPE_MODULE_MAPPING.md) for which types apply to which modules.

### Gap Analysis

See [templates/EXERCISE_ADDITION_PLAN.md](../templates/EXERCISE_ADDITION_PLAN.md) for planned exercise additions.

---

## Templates

Templates are organized into four directories:

### Exercise Type Templates (`templates/exercise_types/`)

| Template | Purpose |
|----------|---------|
| `write_code.py` | Standard write-code exercises |
| `output_prediction.py` | Predict program output |
| `code_tracing.py` | Track variables through execution |
| `match_output.py` | Match code to output |
| `fill_blanks.py` | Complete missing syntax |
| `code_ordering.py` | Arrange scrambled code |
| `complete_function.py` | Implement function bodies |
| `fix_style.py` | Apply style conventions |
| `simplify_code.py` | Refactor for clarity |
| `add_error_handling.py` | Add error handling |
| `which_is_better.py` | Compare solutions |
| `spot_difference.py` | Find subtle differences |
| `decode_error.py` | Interpret error messages |
| `bug_hunt.py` | Narrative debugging |
| `blank_page.py` | Write from scratch |

### Activity Patterns (`templates/activity_patterns/`)

15 task-level narrative templates for individual tasks within exercises.
See [README.md](../templates/activity_patterns/README.md) for full list.

### Structure Patterns (`templates/structure_patterns/`)

6 exercise-level narrative patterns that wrap multiple tasks:
- Progressive Chapter
- Tutorial Walkthrough
- Challenge Quest
- Mystery Investigation
- World Builder
- Spec Implementation

### Hybrid Arcs (`templates/hybrid_arcs/`)

7 narrative arcs for multi-part hybrid exercises:
- Rivalry, Inheritance, Rescue, Apprentice, Mystery, Upgrade, Competition

---

## Lessons

### Structure

Lessons are split into multi-part files for manageable context:

```
{lang}/lessons/
├── lesson_module_X_topic_part_1.md   # Full context (prerequisites, objectives)
├── lesson_module_X_topic_part_2.md   # Builds on part 1
├── lesson_module_X_topic_part_N.md   # Final part
└── lesson_free_practice.md           # Open-ended practice
```

### Templates

| Template | Purpose |
|----------|---------|
| `TEMPLATE_PART1.md` | First part of a lesson (full context) |
| `TEMPLATE_PART.md` | Subsequent parts (minimal context) |
| `TEMPLATE.md` | Single-part lesson (legacy) |

### Available Lessons

| Module | Parts | Languages |
|--------|:-----:|:---------:|
| module_0_basics | 5 | en, he |
| module_1_turtle_loops | 5 | en, he |
| module_2_decisions | 5 | en |
| module_3_lists | 5 | en |
| module_4_games | 4 | en |
| module_5_functions | 5 | en, he |
| module_7_dictionaries | 5 | en, he |
| module_8_modules | 6 | en, he |
| module_9_oop | 5 | en, he |
| free_practice | 1 | en, he |

---

## Narrative Archetypes

See [NARRATIVE_ARCHETYPES.md](NARRATIVE_ARCHETYPES.md) for reusable narrative patterns for exercise design.

Quick access:
- [Full archetype documentation](NARRATIVE_ARCHETYPES.md) - 10 core patterns with examples
- [Quick reference](../templates/ARCHETYPE_QUICK_REFERENCE.md) - Templates and selection guide

The 10 archetypes:
1. Random Assignment (Sorting Hat)
2. Inventory Management (RPG Inventory)
3. Character Creation (Profile Builder)
4. Challenge/Attempt (Quest)
5. Knowledge Check (Quiz)
6. Progression Tracking (Level Up)
7. Relationship Mapping (Social Network)
8. Decision Tree (Choose Your Path)
9. Collection Building (Favorites List)
10. Resource Exchange (Shop/Trade)

---

## Reference Materials

See [REFERENCES.md](REFERENCES.md) for the complete catalog with topic tables and lookup guides.

Summary:

| Source | Focus |
|--------|-------|
| Think Python | CS fundamentals, recursion, OOP |
| Python for Everybody | Data processing, web, APIs |
| Automate Boring Stuff | Practical automation projects |
| Pedagogy research | Learning science, common struggles |

---

## Theme Variables

See [TEMPLATE.md](../TEMPLATE.md) for the complete list of `{{placeholder}}` variables for dynamic theming.

Available themes:

**Open License (production use):**
- `dnd-srd` - D&D Fantasy (CC-BY-4.0)
- `cepheus` - Space Opera (OGL)
- `pymentor` - Plain/generic

**Test-Only (proprietary IP):**
- `dumblecode` - Harry Potter
- `chirthon` - Percy Jackson
- `compile-games` - Hunger Games
- `pyfire` - Keeper of the Lost Cities

---

## Configuration Files

| File | Purpose |
|------|---------|
| `exercises_config.json` | Module metadata, translations |
| `theme_variables.json` | Theme placeholder values |
| `manifest.json` | Module list for remote sync |
| `version.json` | Content version tracking |
| `lessons.json` | Generated lesson index |
