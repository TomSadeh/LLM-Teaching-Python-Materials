# Plan: Module 0 - Basics

Recreation plan for module_0_basics using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_0_basics |
| **Topic** | Python fundamentals |
| **Prerequisites** | None (first module) |
| **Target Hybrid Ratio** | 10-20% |

### Learning Objectives

By the end of this module, students will be able to:

1. Use `print()` to display output
2. Create and use variables with meaningful names
3. Work with strings (creation, concatenation, basic operations)
4. Perform arithmetic with integers and floats
5. Get user input with `input()` and convert types
6. Format strings using f-strings
7. Apply mathematical operators including `//, %, **`

### Curriculum Constraints

| Available Concepts | NOT Available (later modules) |
|--------------------|-------------------------------|
| print() | for/while loops |
| variables, assignment | if/elif/else |
| strings, concatenation | lists, indexing |
| integers, floats | functions (def) |
| input(), type conversion | turtle graphics |
| f-strings | dictionaries |
| math: +, -, *, /, //, %, ** | classes, methods |
| comments | import statements |

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types for Module 0 (see "module_0_basics" section) |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Exercise format standards |

**Note:** Phase-specific templates are listed in each implementation phase below.

---

## 2. Exercise Distribution

### Available Exercise Types (11 total)

| Category | Types |
|----------|-------|
| **Core** | write_code, complete_function, mini_project |
| **Reading** | output_prediction, match_output |
| **Scaffolded** | fill_blanks, code_ordering |
| **Debugging** | decode_error, bug_hunt |
| **Quality** | fix_style, spot_difference |

### Target Distribution

| Type | Count | Rationale |
|------|:-----:|-----------|
| write_code | 5 | Core practice for each concept cluster |
| output_prediction | 2 | Build mental model of execution |
| match_output | 1 | Pattern recognition for output |
| fill_blanks | 2 | Syntax reinforcement |
| code_ordering | 1 | Program structure understanding |
| complete_function | 1 | Guided function body writing |
| fix_style | 1 | Learn conventions early |
| spot_difference | 1 | Catch common typos/errors |
| decode_error | 2 | Understand common error messages |
| bug_hunt | 1 | Find logical errors |
| mini_project | 1 | Integration capstone |
| **hybrid** | 2 | Multi-part narrative exercises |
| **TOTAL** | **20** | |

### Hybrid Ratio Calculation

- Total exercises: 20
- Hybrid exercises: 2
- Ratio: **10%** (within 10-20% target)

---

## 3. Exercise Inventory

### Concept Progression

Exercises are organized into concept clusters, progressing from simple to complex.

| Cluster | Concepts | Difficulty |
|---------|----------|:----------:|
| A | print() basics | 1 |
| B | Variables, assignment | 2 |
| C | Numbers, arithmetic | 2-3 |
| D | Strings | 3 |
| E | Input, type conversion | 3-4 |
| F | f-strings | 4 |
| G | Integration | 5 |

### Isolated Exercises

#### Cluster A: print() Basics (Difficulty 1)

| # | Type | Concept Focus |
|---|------|---------------|
| 1 | output_prediction | Predict what print statements display |
| 2 | write_code | Write basic print statements |

#### Cluster B: Variables (Difficulty 2)

| # | Type | Concept Focus |
|---|------|---------------|
| 3 | fill_blanks | Variable assignment syntax |
| 4 | spot_difference | Variable naming errors, typos |
| 5 | write_code | Create and use variables |

#### Cluster C: Numbers and Arithmetic (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 6 | output_prediction | Predict arithmetic results |
| 7 | code_ordering | Order of operations, program flow |
| 8 | write_code | Basic calculator operations |

#### Cluster D: Strings (Difficulty 3)

| # | Type | Concept Focus |
|---|------|---------------|
| 9 | match_output | String concatenation patterns |
| 10 | decode_error | String-related errors (quotes, types) |
| 11 | write_code | String manipulation |

#### Cluster E: Input (Difficulty 3-4)

| # | Type | Concept Focus |
|---|------|---------------|
| 12 | fill_blanks | input() syntax and type conversion |
| 13 | decode_error | Input-related errors (TypeError) |
| 14 | write_code | Interactive program with input |

#### Cluster F: f-strings (Difficulty 4)

| # | Type | Concept Focus |
|---|------|---------------|
| 15 | complete_function | Function returning formatted string |
| 16 | write_code | f-string formatting with expressions |

#### Cluster G: Integration (Difficulty 5)

| # | Type | Concept Focus |
|---|------|---------------|
| 17 | bug_hunt | Find bugs across all concepts |
| 18 | fix_style | Fix naming conventions and style |
| 19 | mini_project | Combine all concepts in one program |

### Hybrid Exercises

#### Hybrid 1: The Apprentice - Variables and Strings

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | output_prediction | Study variable/string behavior |
| 2 | GUIDANCE | fill_blanks | Practice with scaffolding |
| 3 | GROWTH | write_code | Create independently |

**Placement:** After Cluster D (strings), before input
**Difficulty:** 3

#### Hybrid 2: The Apprentice - Complete Program

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | output_prediction | Study a complete program |
| 2 | GUIDANCE | complete_function | Implement part of it |
| 3 | GROWTH | write_code | Build your own version |

**Placement:** End of module, before mini_project
**Difficulty:** 4-5

---

## 4. Difficulty Progression Map

```
Difficulty:  1 -----> 2 -----> 3 -----> 4 -----> 5
             |       |        |        |        |
Exercises:   1,2     3,4,5    6,7,8    9,10,11  17,18,19
                              H1       12,13,14 H2
                                       15,16
```

H1 = Hybrid 1, H2 = Hybrid 2

---

## 5. File Structure

```
exercises/
└── module_0_basics/
    ├── output_prediction/
    │   ├── exercise_1_print_basics.py
    │   └── exercise_2_arithmetic.py
    ├── write_code/
    │   ├── exercise_1_hello.py
    │   ├── exercise_2_variables.py
    │   ├── exercise_3_calculator.py
    │   ├── exercise_4_strings.py
    │   ├── exercise_5_input.py
    │   └── exercise_6_fstrings.py
    ├── fill_blanks/
    │   ├── exercise_1_variables.py
    │   └── exercise_2_input.py
    ├── spot_difference/
    │   └── exercise_1_variable_errors.py
    ├── code_ordering/
    │   └── exercise_1_program_flow.py
    ├── match_output/
    │   └── exercise_1_string_output.py
    ├── decode_error/
    │   ├── exercise_1_string_errors.py
    │   └── exercise_2_input_errors.py
    ├── complete_function/
    │   └── exercise_1_format_output.py
    ├── bug_hunt/
    │   └── exercise_1_basics_bugs.py
    ├── fix_style/
    │   └── exercise_1_naming.py
    ├── mini_project/
    │   └── exercise_1_profile_builder.py
    └── hybrid/
        ├── exercise_1_apprentice_variables.py
        └── exercise_2_apprentice_program.py
```

---

## 6. Implementation Phases

Implementation is organized into 7 phases following the concept progression.

**After completing each phase:** Mark it with ✅ COMPLETE below the phase header.

### Phase 1: print() Basics (Cluster A) ✅ COMPLETE

**Exercises:** 1, 2
**Difficulty:** 1
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| 1 | output_prediction | `output_prediction/exercise_1_print_basics.py` |
| 2 | write_code | `write_code/exercise_1_hello.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| output_prediction | [templates/exercise_types/output_prediction.py](../../templates/exercise_types/output_prediction.py) |
| write_code | [templates/exercise_types/write_code.py](../../templates/exercise_types/write_code.py) |

---

### Phase 2: Variables (Cluster B) ✅ COMPLETE

**Exercises:** 3, 4, 5
**Difficulty:** 2
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 3 | fill_blanks | `fill_blanks/exercise_1_variables.py` |
| 4 | spot_difference | `spot_difference/exercise_1_variable_errors.py` |
| 5 | write_code | `write_code/exercise_2_variables.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| fill_blanks | [templates/exercise_types/fill_blanks.py](../../templates/exercise_types/fill_blanks.py) |
| spot_difference | [templates/exercise_types/spot_difference.py](../../templates/exercise_types/spot_difference.py) |

---

### Phase 3: Numbers and Arithmetic (Cluster C) ✅ COMPLETE

**Exercises:** 6, 7, 8
**Difficulty:** 2-3
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 6 | output_prediction | `output_prediction/exercise_2_arithmetic.py` |
| 7 | code_ordering | `code_ordering/exercise_1_program_flow.py` |
| 8 | write_code | `write_code/exercise_3_calculator.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| code_ordering | [templates/exercise_types/code_ordering.py](../../templates/exercise_types/code_ordering.py) |

*(output_prediction and write_code templates already read in Phase 1)*

---

### Phase 4: Strings + Hybrid 1 (Cluster D) ✅ COMPLETE

**Exercises:** 9, 10, 11, Hybrid 1
**Difficulty:** 3
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 9 | match_output | `match_output/exercise_1_string_output.py` |
| 10 | decode_error | `decode_error/exercise_1_string_errors.py` |
| 11 | write_code | `write_code/exercise_4_strings.py` |
| H1 | hybrid (apprentice) | `hybrid/exercise_1_apprentice_variables.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| match_output | [templates/exercise_types/match_output.py](../../templates/exercise_types/match_output.py) |
| decode_error | [templates/exercise_types/decode_error.py](../../templates/exercise_types/decode_error.py) |
| hybrid_arcs README | [templates/hybrid_arcs/README.md](../../templates/hybrid_arcs/README.md) |
| apprentice arc | [templates/hybrid_arcs/apprentice.md](../../templates/hybrid_arcs/apprentice.md) |

---

### Phase 5: Input (Cluster E) ✅ COMPLETE

**Exercises:** 12, 13, 14
**Difficulty:** 3-4
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 12 | fill_blanks | `fill_blanks/exercise_2_input.py` |
| 13 | decode_error | `decode_error/exercise_2_input_errors.py` |
| 14 | write_code | `write_code/exercise_5_input.py` |

**Read Before This Phase:**

*(All templates already read in previous phases)*

---

### Phase 6: f-strings (Cluster F) ✅ COMPLETE

**Exercises:** 15, 16
**Difficulty:** 4
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| 15 | complete_function | `complete_function/exercise_1_format_output.py` |
| 16 | write_code | `write_code/exercise_6_fstrings.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| complete_function | [templates/exercise_types/complete_function.py](../../templates/exercise_types/complete_function.py) |

---

### Phase 7: Integration + Hybrid 2 (Cluster G) ✅ COMPLETE

**Exercises:** 17, 18, Hybrid 2 (note: mini_project merged into hybrids)
**Difficulty:** 5
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 17 | bug_hunt | `bug_hunt/exercise_1_basics_bugs.py` |
| 18 | fix_style | `fix_style/exercise_1_naming.py` |
| 19 | mini_project | `mini_project/exercise_1_profile_builder.py` |
| H2 | hybrid (apprentice) | `hybrid/exercise_2_apprentice_program.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| bug_hunt | [templates/exercise_types/bug_hunt.py](../../templates/exercise_types/bug_hunt.py) |
| fix_style | [templates/exercise_types/fix_style.py](../../templates/exercise_types/fix_style.py) |
| mini_project | [templates/exercise_types/mini_project.py](../../templates/exercise_types/mini_project.py) |

---

### Phase Summary

| Phase | Cluster | Exercises | Files | New Templates |
|:-----:|---------|-----------|:-----:|---------------|
| 1 | print() | 1-2 | 2 | output_prediction, write_code |
| 2 | Variables | 3-5 | 3 | fill_blanks, spot_difference |
| 3 | Numbers | 6-8 | 3 | code_ordering |
| 4 | Strings | 9-11, H1 | 4 | match_output, decode_error, hybrid_arcs |
| 5 | Input | 12-14 | 3 | *(none)* |
| 6 | f-strings | 15-16 | 2 | complete_function |
| 7 | Integration | 17-19, H2 | 4 | bug_hunt, fix_style, mini_project |
| **Total** | | **20** | **21** | |

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every exercise contains at least one `{{placeholder}}`
- [ ] NO concepts from later modules used
- [ ] All 7 learning objectives covered
- [ ] Progressive difficulty (1 to 5)
- [ ] Hybrid ratio within 10-20%

### Format Requirements

- [ ] All functions use `pass` placeholder
- [ ] Instructions use `# ✏️ YOUR CODE HERE ✏️` marker
- [ ] Each file has `main()` that calls all exercises
- [ ] PEP 8 compliant
- [ ] Follows templates from `templates/exercise_types/`

### Curriculum Compliance

| Concept | Used In |
|---------|---------|
| print() | Exercises 1, 2 (+ most others) |
| variables | Exercises 3, 4, 5, Hybrid 1 |
| numbers/math | Exercises 6, 7, 8 |
| strings | Exercises 9, 10, 11, Hybrid 1 |
| input() | Exercises 12, 13, 14 |
| f-strings | Exercises 15, 16, Hybrid 2 |
| integration | Exercises 17, 18, 19, Hybrid 2 |

---

## 8. Implementation Notes

### Key Constraints

1. **No loops** - Cannot iterate; must use sequential statements
2. **No conditionals** - Cannot branch; all code paths execute
3. **No functions defined by student** - They complete function bodies, not define functions
4. **No imports** - Cannot use any modules

### Narrative Considerations

- Use `{{hero}}`, `{{school}}`, `{{item}}` for theming
- Apprentice arc fits well: observation → guided practice → independence
- Keep narratives simple; first exposure to Python

### Common Pitfalls to Avoid

- Accidentally using `for` or `while` loops
- Assuming `if` statements are available
- Using list operations
- Importing random or other modules

---
