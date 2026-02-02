# Exercise Addition Plan

Based on audit of `exercises/` against `EXERCISE_TYPE_MODULE_MAPPING.md`.

---

## Current State Summary

| Module | Existing Types | Existing Exercises |
|--------|---------------|-------------------|
| module_0_basics | write_code, complete_function, decode_error, output_prediction, bug_hunt | 23 |
| module_1_turtle_loops | write_code, output_prediction | 11 |
| module_2_decisions | write_code, output_prediction | 10 |
| module_3_lists | write_code, decode_error | 10 |
| module_4_games | write_code | 9 |
| module_5_functions | write_code | 9 |
| module_6_final_project | write_code | 3 |
| module_7_dictionaries | write_code | 9 |
| module_8_modules | write_code | 9 |
| module_9_oop | write_code, complete_function | 9 |

**Total existing:** 102 exercises across 10 types (but mostly write_code)

---

## Gap Analysis by Exercise Type

### Completely Missing Types (0 exercises exist)

| Type | Should Exist In | Priority | Rationale |
|------|-----------------|----------|-----------|
| **code_tracing** | turtle, decisions, lists, dicts | HIGH | Essential for understanding program flow |
| **match_output** | basics, turtle, lists | HIGH | Quick pattern recognition, easy to create |
| **fill_blanks** | basics, turtle, functions | HIGH | Syntax reinforcement for beginners |
| **code_ordering** | basics, turtle, functions | MEDIUM | Understanding program structure |
| **fix_style** | basics, functions, oop | MEDIUM | Learn conventions early |
| **simplify_code** | lists, functions, dicts | MEDIUM | Refactoring skills |
| **add_error_handling** | games, functions, modules | MEDIUM | Real-world robustness |
| **which_is_better** | lists, functions, dicts, oop | MEDIUM | Critical thinking about code |
| **spot_difference** | basics, lists, functions | MEDIUM | Find subtle bugs |
| **blank_page** | functions, final, dicts, oop | LOW | Advanced independence |
| **mini_project** | basics, functions, final | LOW | Integration exercises |

### Partially Implemented Types

| Type | Exists In | Missing From |
|------|-----------|--------------|
| output_prediction | basics(1), turtle(1), decisions(1) | - (complete!) |
| complete_function | basics(3), oop(2) | lists, functions, dicts |
| decode_error | basics(3), lists(1) | functions, dicts |
| bug_hunt | basics(1) | turtle, decisions, lists, games |

---

## Priority 1: High-Impact, Easy to Create (12 exercises)

These types are pedagogically important and straightforward to develop.

### 1.1 match_output (3 exercises)

Quick reading exercises - show code, ask what it outputs.

| Module | Exercise Ideas |
|--------|---------------|
| basics | `match_print_statements.py` - Match print() calls to outputs |
| turtle | `match_turtle_paths.py` - Match code to shape it draws |
| lists | `match_list_operations.py` - Match list methods to results |

### 1.2 fill_blanks (3 exercises)

Complete the syntax with missing pieces.

| Module | Exercise Ideas |
|--------|---------------|
| basics | `fill_string_formatting.py` - Complete f-strings and format() |
| turtle | `fill_loop_syntax.py` - Complete for loop structures |
| functions | `fill_function_syntax.py` - def, parameters, return |

### 1.3 code_tracing (4 exercises)

Track variable values through execution.

| Module | Exercise Ideas |
|--------|---------------|
| turtle | `trace_turtle_position.py` - Track x,y coordinates |
| decisions | `trace_if_else_flow.py` - Follow branching paths |
| lists | `trace_list_mutations.py` - Track list changes in loops |
| dicts | `trace_dict_updates.py` - Follow dictionary modifications |

### 1.4 bug_hunt (2 exercises)

Find and fix bugs in themed scenarios.

| Module | Exercise Ideas |
|--------|---------------|
| turtle | `bug_broken_shapes.py` - Shapes that don't close properly |
| decisions | `bug_wrong_comparisons.py` - Logic errors in conditions |

---

## Priority 2: Skill-Building Types (14 exercises)

### 2.1 code_ordering (3 exercises)

Put scrambled code in correct order.

| Module | Exercise Ideas |
|--------|---------------|
| basics | `order_program_structure.py` - imports, variables, functions, main |
| turtle | `order_drawing_steps.py` - Setup, draw, display sequence |
| functions | `order_function_calls.py` - Define before use, return before print |

### 2.2 complete_function (3 exercises)

Implement function body given signature and docstring.

| Module | Exercise Ideas |
|--------|---------------|
| lists | `complete_list_functions.py` - find_max, filter_evens, etc. |
| functions | `complete_helper_functions.py` - validate_input, format_output |
| dicts | `complete_dict_functions.py` - lookup, update, merge |

### 2.3 decode_error (2 exercises)

Interpret error messages and fix the code.

| Module | Exercise Ideas |
|--------|---------------|
| functions | `decode_function_errors.py` - missing args, wrong return |
| dicts | `decode_dict_errors.py` - KeyError, unhashable type |

### 2.4 spot_difference (3 exercises)

Find the bug between two similar code snippets.

| Module | Exercise Ideas |
|--------|---------------|
| basics | `spot_variable_typos.py` - name vs Name, off-by-one |
| lists | `spot_index_errors.py` - len vs len-1, range issues |
| functions | `spot_return_vs_print.py` - return None implicitly |

### 2.5 bug_hunt (3 exercises)

Narrative debugging with visual/interactive feedback.

| Module | Exercise Ideas |
|--------|---------------|
| lists | `bug_list_manipulation.py` - append vs extend, index issues |
| games | `bug_game_logic.py` - win/lose conditions wrong |

---

## Priority 3: Critical Thinking Types (10 exercises)

### 3.1 which_is_better (4 exercises)

Compare two working solutions, explain trade-offs.

| Module | Exercise Ideas |
|--------|---------------|
| lists | `compare_loop_vs_comprehension.py` |
| functions | `compare_many_params_vs_dict.py` |
| dicts | `compare_nested_vs_flat.py` |
| oop | `compare_inheritance_vs_composition.py` |

### 3.2 fix_style (3 exercises)

Improve code to follow PEP 8 and best practices.

| Module | Exercise Ideas |
|--------|---------------|
| basics | `fix_naming_conventions.py` - camelCase to snake_case |
| functions | `fix_function_style.py` - docstrings, parameter names |
| oop | `fix_class_style.py` - __init__, method order, naming |

### 3.3 simplify_code (3 exercises)

Refactor verbose code to be more Pythonic.

| Module | Exercise Ideas |
|--------|---------------|
| lists | `simplify_to_comprehension.py` - for loops to list comp |
| functions | `simplify_repeated_code.py` - extract helper functions |
| dicts | `simplify_with_get_setdefault.py` - if key in dict to .get() |

---

## Priority 4: Advanced/Specialized Types (8 exercises)

### 4.1 add_error_handling (3 exercises)

Add try/except to make code robust.

| Module | Exercise Ideas |
|--------|---------------|
| games | `handle_game_input.py` - validate user guesses |
| functions | `handle_function_input.py` - type checking, bounds |
| modules | `handle_file_io.py` - file not found, JSON decode |

### 4.2 blank_page (4 exercises)

Write from scratch given only docstrings/specifications.

| Module | Exercise Ideas |
|--------|---------------|
| functions | `blank_utility_functions.py` |
| final | `blank_mini_app.py` |
| dicts | `blank_data_processor.py` |
| oop | `blank_class_design.py` |

### 4.3 mini_project (1 exercise)

Combination of scaffolded helpers + creative main.

| Module | Exercise Ideas |
|--------|---------------|
| functions | `project_calculator_app.py` - helpers provided, main to build |

---

## Implementation Order

### Phase 1: Quick Wins (Week 1)
Focus on types that are easy to create and high pedagogical value.

1. **match_output** - 3 exercises (basics, turtle, lists)
2. **fill_blanks** - 3 exercises (basics, turtle, functions)
3. **code_tracing** - 2 exercises (decisions, lists)

**Total: 8 exercises**

### Phase 2: Core Skills (Week 2)
Build out debugging and function types.

4. **bug_hunt** - 4 exercises (turtle, decisions, lists, games)
5. **complete_function** - 3 exercises (lists, functions, dicts)
6. **decode_error** - 2 exercises (functions, dicts)

**Total: 9 exercises**

### Phase 3: Analysis & Improvement (Week 3)
Types requiring more code comparison.

7. **code_ordering** - 3 exercises (basics, turtle, functions)
8. **spot_difference** - 3 exercises (basics, lists, functions)
9. **which_is_better** - 4 exercises (lists, functions, dicts, oop)

**Total: 10 exercises**

### Phase 4: Style & Simplification (Week 4)
Improvement-focused exercises.

10. **fix_style** - 3 exercises (basics, functions, oop)
11. **simplify_code** - 3 exercises (lists, functions, dicts)
12. **code_tracing** - 2 exercises (turtle, dicts) - remaining

**Total: 8 exercises**

### Phase 5: Advanced (Week 5)
Independence and robustness.

13. **add_error_handling** - 3 exercises (games, functions, modules)
14. **blank_page** - 4 exercises (functions, final, dicts, oop)
15. **mini_project** - 1 exercise (functions)

**Total: 8 exercises**

---

## Summary

| Priority | Type Count | Exercise Count |
|----------|------------|----------------|
| P1 (High-Impact) | 4 types | 12 exercises |
| P2 (Skill-Building) | 5 types | 14 exercises |
| P3 (Critical Thinking) | 3 types | 10 exercises |
| P4 (Advanced) | 3 types | 8 exercises |
| **TOTAL** | **15 types** | **44 exercises** |

This would bring the repository from 102 to 146 exercises with much better type diversity.

---

## Template Requirements

All exercise type templates exist in `templates/`:

- [x] `template_output_prediction.py`
- [x] `template_code_tracing.py`
- [x] `template_match_output.py`
- [x] `template_fill_blanks.py`
- [x] `template_code_ordering.py`
- [x] `template_complete_function.py`
- [x] `template_fix_style.py`
- [x] `template_simplify_code.py`
- [x] `template_add_error_handling.py`
- [x] `template_which_is_better.py`
- [x] `template_spot_difference.py`
- [x] `template_decode_error.py`
- [x] `template_bug_hunt.py`
- [x] `template_blank_page.py`

Missing template (may need to create):
- [ ] `template_mini_project.py` - hybrid scaffolded + creative

---

## Notes

1. All exercises must use `{{placeholder}}` syntax per CLAUDE.md
2. Each exercise needs Hebrew translations in `convert_exercises.py`
3. Run `python scripts/convert_exercises.py` after adding exercises
4. New exercise types need entries in `exercises_config.json`
