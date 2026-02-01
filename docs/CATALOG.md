# Content Catalog

This document catalogs all exercises, lessons, and reference materials in the repository.

## Modules

| Module | Topic | Difficulty | Description |
|--------|-------|:----------:|-------------|
| `module_0_basics` | Fundamentals | 1 | print, variables, math, input/output |
| `module_1_turtle_loops` | For Loops | 1 | Turtle graphics with for loops |
| `module_2_decisions` | Conditionals | 2 | if/elif/else, comparisons |
| `module_3_lists` | Lists | 2 | Lists, iteration, list methods |
| `module_4_games` | While Loops | 2 | Games with while loops, random |
| `module_5_functions` | Functions | 3 | Parameters, return values, reuse |
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

## Exercise Templates

All exercise templates are in the `templates/` directory:

| Template | Purpose |
|----------|---------|
| `template_write_code.py` | Standard write-code exercises |
| `template_output_prediction.py` | Predict program output |
| `template_code_tracing.py` | Track variables through execution |
| `template_match_output.py` | Match code to output |
| `template_fill_blanks.py` | Complete missing syntax |
| `template_code_ordering.py` | Arrange scrambled code |
| `template_complete_function.py` | Implement function bodies |
| `template_fix_style.py` | Apply style conventions |
| `template_simplify_code.py` | Refactor for clarity |
| `template_add_error_handling.py` | Add error handling |
| `template_which_is_better.py` | Compare solutions |
| `template_spot_difference.py` | Find subtle differences |
| `template_decode_error.py` | Interpret error messages |
| `template_bug_hunt.py` | Narrative debugging |
| `template_blank_page.py` | Write from scratch |

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
| module_5_functions | - | en, he |
| module_7_dictionaries | - | en, he |
| module_8_modules | - | en, he |
| module_9_oop | - | en, he |
| free_practice | 1 | en, he |

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
- `dumblecode` - Harry Potter
- `chirthon` - Percy Jackson
- `compile-games` - Hunger Games
- `pyfire` - Keeper of the Lost Cities
- `pymentor` - Plain/generic

---

## Configuration Files

| File | Purpose |
|------|---------|
| `exercises_config.json` | Module metadata, translations |
| `theme_variables.json` | Theme placeholder values |
| `manifest.json` | Module list for remote sync |
| `version.json` | Content version tracking |
| `lessons.json` | Generated lesson index |
