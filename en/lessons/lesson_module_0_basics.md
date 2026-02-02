# Lesson: Python Basics

> **Module**: module_0_basics
> **Parts**: 6 (Part 0-5)
> **Difficulty**: 1-2
> **Total Duration**: 20-30 minutes

---

## Overview

First programming module. Establishes foundational skills and experimental mindset.

---

## Learning Objectives

By the end of this module, the student will be able to:

1. Use `print()` to display text on the screen
2. Create variables to store text and numbers
3. Perform basic math operations (+, -, *, /)
4. Get user input with `input()` and convert types with `int()`
5. Combine variables and text using f-strings

---

## Parts

| Part | Topic | Duration | Key Concept |
|------|-------|----------|-------------|
| 0 | Welcome to Programming | 2-3 min | Mindset, expectations |
| 1 | Hello World with print() | 3-5 min | `print()`, strings |
| 2 | Variables | 3-5 min | Assignment, using variables |
| 3 | Math Operations | 3-5 min | Operators, integers |
| 4 | User Input | 3-5 min | `input()`, `int()` |
| 5 | Putting It Together | 5-7 min | f-strings, combining skills |

---

## Exercise Flow

### Progression Pattern
Each part follows: **OBSERVE → PRACTICE → CREATE → DEBUG**

See [learning-science.md](../../references/pedagogy/learning-science.md) for rationale.

### Exercise Sequence

| Part | OBSERVE | PRACTICE | CREATE | DEBUG |
|------|---------|----------|--------|-------|
| 1 | `output_prediction/ex1_print_basics` | - | `write_code/ex1_hello` | - |
| 2 | (part of ex1_print_basics) | `fill_blanks/ex1_variables` | `write_code/ex2_variables` | `spot_difference/ex1_variable_errors` |
| 3 | `output_prediction/ex2_arithmetic` | `code_ordering/ex1_program_flow` | `write_code/ex3_calculator` | `decode_error/ex1_string_errors` |
| 4 | (live demo) | `fill_blanks/ex2_input` | `write_code/ex5_input` | `decode_error/ex2_input_errors` |
| 5 | `match_output/ex1_string_output` | `complete_function/ex1_format_output` | `write_code/ex4_strings`, `ex6_fstrings` | `bug_hunt/ex1_basics_bugs` |

### Capstones

| After Part | Hybrid Exercise |
|------------|-----------------|
| Part 2 | `hybrid/exercise_1_apprentice_variables` |
| Part 5 | `hybrid/exercise_2_apprentice_program` (module capstone) |

---

## Key Concepts Summary

| Concept | Introduced | Explanation |
|---------|------------|-------------|
| `print()` | Part 1 | Display output |
| String | Part 1 | Text in quotes |
| Variable | Part 2 | Named storage |
| Assignment (`=`) | Part 2 | Store value |
| Integer | Part 3 | Whole number |
| Operators | Part 3 | `+`, `-`, `*`, `/` |
| `input()` | Part 4 | Get user text |
| `int()` | Part 4 | Convert to number |
| f-string | Part 5 | Format with `f"{}"` |

---

## Common Misconceptions

| Misconception | Reality | Part |
|---------------|---------|------|
| Forgetting quotes around strings | Without quotes, Python looks for variable | 1 |
| `print("name")` shows variable value | Quotes make it literal text | 2 |
| `input()` returns numbers | Always returns string, use `int()` | 4 |
| `=` compares values | `=` assigns, `==` compares (later) | 2 |

---

## References

- [learning-science.md](../../references/pedagogy/learning-science.md)
- [common-struggles.md](../../references/pedagogy/common-struggles.md)
- [exercise-types.md](../../references/pedagogy/exercise-types.md)
