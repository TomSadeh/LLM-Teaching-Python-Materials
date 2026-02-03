# Exercise Type to Module Mapping

This document defines which exercise types are appropriate for each module based on pedagogical analysis.

---

## Quick Reference Grid

| Type | 0_basics | 1_turtle | 2_decisions | 3_lists | 4_games | 5_functions | 6_final | 7_dicts | 8_modules | 9_oop |
|------|:--------:|:--------:|:-----------:|:-------:|:-------:|:-----------:|:-------:|:-------:|:---------:|:-----:|
| **write_code** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **output_prediction** | ✓ | ✓ | ✓ | | | | | | | |
| **code_tracing** | | ✓ | ✓ | ✓ | | | | ✓ | | |
| **match_output** | ✓ | ✓ | | ✓ | | | | | | |
| **fill_blanks** | ✓ | ✓ | | | | ✓ | | | | |
| **code_ordering** | ✓ | ✓ | | | | ✓ | | | | |
| **complete_function** | ✓ | | | ✓ | | ✓ | | ✓ | | ✓ |
| **fix_style** | ✓ | | | | | ✓ | | | | ✓ |
| **simplify_code** | | | | ✓ | | ✓ | | ✓ | | |
| **add_error_handling** | | | | | ✓ | ✓ | | | ✓ | |
| **which_is_better** | | | | ✓ | | ✓ | | ✓ | | ✓ |
| **spot_difference** | ✓ | | | ✓ | | ✓ | | | | |
| **decode_error** | ✓ | | | ✓ | | ✓ | | ✓ | | |
| **bug_hunt** | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | |
| **blank_page** | | | | | | ✓ | ✓ | ✓ | | ✓ |
| **mini_project** | ✓ | | | | | ✓ | ✓ | | | |

---

## Rationale by Category

### Reading (understand existing code)

| Type | Modules | Rationale |
|------|---------|-----------|
| **output_prediction** | basics, turtle, decisions | Deterministic output, clear mental model of execution |
| **code_tracing** | turtle, decisions, lists, dicts | State changes to track through loops/conditions |
| **match_output** | basics, turtle, lists | Pattern recognition, quick code reading |

### Scaffolded Writing (guided creation)

| Type | Modules | Rationale |
|------|---------|-----------|
| **fill_blanks** | basics, turtle, functions | Syntax reinforcement for key constructs |
| **code_ordering** | basics, turtle, functions | Understand program flow and structure |
| **complete_function** | basics, lists, functions, dicts, oop | Requires function concept; body implementation |

### Improvement (make code better)

| Type | Modules | Rationale |
|------|---------|-----------|
| **fix_style** | basics, functions, oop | Learn conventions early; reinforce at key points |
| **simplify_code** | lists, functions, dicts | Requires experience; comprehensions, refactoring |
| **add_error_handling** | games, functions, modules | Real-world robustness; user input, I/O |

### Analysis (compare and evaluate)

| Type | Modules | Rationale |
|------|---------|-----------|
| **which_is_better** | lists, functions, dicts, oop | Multiple valid approaches exist |
| **spot_difference** | basics, lists, functions | Typos, off-by-one, return vs print |

### Debugging (find and fix)

| Type | Modules | Rationale |
|------|---------|-----------|
| **decode_error** | basics, lists, functions, dicts | Common error types for each concept |
| **bug_hunt** | basics, turtle, decisions, lists, games | Narrative debugging; visual/interactive feedback |

### Free Writing (independent creation)

| Type | Modules | Rationale |
|------|---------|-----------|
| **blank_page** | functions, final, dicts, oop | Advanced independence; docstrings only |
| **mini_project** | basics, functions, final | Combine scaffolded + creative elements |

---

## Module-Centric View

### module_0_basics
- **Core:** write_code, complete_function, mini_project
- **Reading:** output_prediction, match_output
- **Scaffolded:** fill_blanks, code_ordering
- **Debugging:** decode_error, bug_hunt
- **Quality:** fix_style, spot_difference

### module_1_turtle_loops
- **Core:** write_code
- **Reading:** output_prediction, code_tracing, match_output
- **Scaffolded:** fill_blanks, code_ordering
- **Debugging:** bug_hunt

### module_2_decisions
- **Core:** write_code
- **Reading:** output_prediction, code_tracing
- **Debugging:** bug_hunt

### module_3_lists
- **Core:** write_code, complete_function
- **Reading:** code_tracing, match_output
- **Improvement:** simplify_code
- **Analysis:** which_is_better, spot_difference
- **Debugging:** decode_error, bug_hunt

### module_4_games
- **Core:** write_code
- **Improvement:** add_error_handling
- **Debugging:** bug_hunt

### module_5_functions
- **Core:** write_code, complete_function, mini_project, blank_page
- **Scaffolded:** fill_blanks, code_ordering
- **Improvement:** fix_style, simplify_code, add_error_handling
- **Analysis:** which_is_better, spot_difference
- **Debugging:** decode_error

### module_6_mid_project
- **Core:** write_code, mini_project, blank_page

### module_7_dictionaries
- **Core:** write_code, complete_function, blank_page
- **Reading:** code_tracing
- **Improvement:** simplify_code
- **Analysis:** which_is_better
- **Debugging:** decode_error

### module_8_modules
- **Core:** write_code
- **Improvement:** add_error_handling

### module_9_oop
- **Core:** write_code, complete_function, blank_page
- **Improvement:** fix_style
- **Analysis:** which_is_better

---

## Type Count by Module

| Module | Types Available |
|--------|---------------:|
| module_0_basics | 11 |
| module_1_turtle_loops | 7 |
| module_2_decisions | 4 |
| module_3_lists | 9 |
| module_4_games | 3 |
| module_5_functions | 12 |
| module_6_mid_project | 3 |
| module_7_dictionaries | 7 |
| module_8_modules | 2 |
| module_9_oop | 5 |

---

## Notes

1. **write_code** is available in ALL modules - it's the foundational exercise type
2. **complete_function** requires understanding of function signatures - available where functions are taught or prerequisite
3. **bug_hunt** works best with visual/interactive feedback - turtle, games, decisions with clear outcomes
4. **blank_page** is advanced - only for modules where students have enough foundation
5. **mini_project** combines scaffolded helpers with creative main tasks - hybrid type
