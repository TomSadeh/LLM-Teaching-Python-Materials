# Plan: Module 4 - Functions

Recreation plan for module_4_functions using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_4_functions |
| **Topic** | Function definition, parameters, return values, scope |
| **Prerequisites** | module_0_basics, module_1_turtle_loops, module_2_decisions, module_3_lists |
| **Target Hybrid Ratio** | 45-55% |

### Learning Objectives

By the end of this module, students will be able to:

1. Define functions using `def` with meaningful names
2. Use positional parameters to pass data into functions
3. Use default parameter values for optional arguments
4. Return values from functions using `return`
5. Distinguish between `return` and `print` (common confusion point)
6. Understand local scope (variables inside functions)
7. Call functions and use their return values in expressions
8. Design reusable functions that solve specific problems
9. Combine functions with previously learned concepts (loops, conditionals, lists)

### Curriculum Constraints

| Available Concepts | NOT Available (later modules) |
|--------------------|-------------------------------|
| **From Module 0:** | |
| print(), variables | while loops |
| strings, concatenation | random module |
| integers, floats | dictionaries |
| input(), type conversion | try/except (partial - see note) |
| f-strings | classes, methods |
| math: +, -, *, /, //, %, ** | file I/O |
| **From Module 1:** | import (except turtle) |
| for loops | |
| range() variants | |
| turtle graphics | |
| **From Module 2:** | |
| if/elif/else | |
| comparison operators | |
| and, or, not | |
| **From Module 3:** | |
| lists, indexing, slicing | |
| list methods | |
| len(), in operator | |
| mutability, aliasing | |
| **New in Module 4:** | |
| def function_name(): | |
| parameters (positional) | |
| default parameter values | |
| return statement | |
| local scope | |
| calling functions | |

**Note on add_error_handling:** This exercise type is available for Module 4, but should focus on basic validation (if statements checking input) rather than try/except which comes later.

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types for Module 4 (see "module_5_functions" section*) |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Exercise format standards |
| [common-struggles.md](../../references/pedagogy/common-struggles.md) | Function confusion, return vs print |

*Note: The exercise type mapping document uses different numbering. Our module_4_functions corresponds to their "module_5_functions" section.

---

## 2. Exercise Distribution

### Available Exercise Types (12 total)

| Category | Types |
|----------|-------|
| **Core** | write_code, complete_function, mini_project, blank_page |
| **Scaffolded** | fill_blanks, code_ordering |
| **Improvement** | fix_style, simplify_code, add_error_handling |
| **Analysis** | which_is_better, spot_difference |
| **Debugging** | decode_error |

**Note:** Module 4 has the most exercise types available (12). This reflects that functions are a major milestone where students have enough foundation for diverse practice types.

### Target Distribution

| Type | Count | Rationale |
|------|:-----:|-----------|
| write_code | 3 | Core practice for function creation |
| complete_function | 2 | Guided implementation from signatures |
| fill_blanks | 2 | Syntax reinforcement for def/return |
| code_ordering | 1 | Understand function structure |
| fix_style | 1 | Learn function naming conventions |
| simplify_code | 1 | Refactor to use functions |
| which_is_better | 1 | Compare function designs |
| spot_difference | 1 | Catch return vs print errors |
| decode_error | 1 | Interpret function-related errors |
| **hybrid** | 9 | Multi-part narrative exercises (45% of total) |
| **TOTAL** | **22** | |

**Note:** mini_project and blank_page are reserved for hybrids and the capstone, and add_error_handling is used within hybrids.

### Hybrid Ratio Calculation

- Total exercises: 22
- Hybrid exercises: 9
- Ratio: **41%** (close to 45-55% target, accounting for concept density)

---

## 3. Exercise Inventory

### Concept Progression

Exercises are organized into concept clusters, progressing from simple to complex.

| Cluster | Concepts | Difficulty |
|---------|----------|:----------:|
| A | Basic function definition and calling | 1 |
| B | Parameters (positional) | 2 |
| C | Return values | 2-3 |
| D | Return vs print distinction | 3 |
| E | Default parameters | 3 |
| F | Local scope | 3-4 |
| G | Functions with lists | 4 |
| H | Function design and integration | 5 |

### Isolated Exercises

#### Cluster A: Basic Function Definition (Difficulty 1)

| # | Type | Concept Focus |
|---|------|---------------|
| 1 | fill_blanks | Complete function syntax (def, colon, body) |
| 2 | write_code | Write simple functions that print messages |

#### Cluster B: Parameters (Difficulty 2)

| # | Type | Concept Focus |
|---|------|---------------|
| 3 | fill_blanks | Complete function with parameters |
| 4 | code_ordering | Arrange function definition and calls correctly |
| 5 | write_code | Write functions with multiple parameters |

#### Cluster C: Return Values (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 6 | complete_function | Complete function body with return statement |
| 7 | write_code | Write functions that return calculated values |
| 8 | decode_error | Interpret TypeError when using None return |

#### Cluster D: Return vs Print (Difficulty 3)

| # | Type | Concept Focus |
|---|------|---------------|
| 9 | spot_difference | Find return vs print bugs |
| 10 | which_is_better | Compare function that returns vs prints |

#### Cluster E: Default Parameters (Difficulty 3)

| # | Type | Concept Focus |
|---|------|---------------|
| 11 | complete_function | Complete function with default parameters |
| 12 | fix_style | Fix poorly named functions and parameters |

#### Cluster F: Local Scope (Difficulty 3-4)

| # | Type | Concept Focus |
|---|------|---------------|
| 13 | simplify_code | Refactor repeated code into functions |

### Hybrid Exercises

#### Hybrid 1: The Apprentice - Function Foundations

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GUIDANCE | fill_blanks | Study function syntax |
| 2 | GUIDANCE | complete_function | Practice completing functions |
| 3 | GROWTH | write_code | Create functions independently |

**Placement:** After Cluster A (basic definition)
**Difficulty:** 1-2
**Arc:** Apprentice

#### Hybrid 2: The Apprentice - Return Value Mastery

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | spot_difference | Observe return vs print |
| 2 | GUIDANCE | complete_function | Practice return statements |
| 3 | GROWTH | write_code | Create returning functions |

**Placement:** After Cluster C (return values)
**Difficulty:** 2-3
**Arc:** Apprentice

#### Hybrid 3: The Rescue - The Broken Calculator

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | decode_error | Understand the error |
| 2 | INVESTIGATION | spot_difference | Find the bug |
| 3 | IMPROVEMENT | add_error_handling | Add input validation |

**Placement:** After Cluster D (return vs print)
**Difficulty:** 3
**Arc:** Rescue

#### Hybrid 4: The Upgrade - From Repetition to Reuse

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | EVALUATION | which_is_better | Compare repeated vs function approach |
| 2 | IMPROVEMENT | simplify_code | Refactor to use functions |

**Placement:** After Cluster E (default parameters)
**Difficulty:** 3-4
**Arc:** Upgrade (2-part variant)

#### Hybrid 5: The Competition - Design Showdown

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | EVALUATION | which_is_better | Compare two function designs |
| 2 | GROWTH | write_code | Build your own improved version |
| 3 | EVALUATION | which_is_better | Compare yours to the original |

**Placement:** After Cluster F (scope)
**Difficulty:** 4
**Arc:** Competition

#### Hybrid 6: The Inheritance - The Utility Library

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | code_ordering | Understand inherited function library |
| 2 | OWNERSHIP | write_code | Add new functions to the library |
| 3 | INVESTIGATION | decode_error | Fix scope/parameter bugs |

**Placement:** After Cluster F (scope)
**Difficulty:** 4
**Arc:** Inheritance (adapted)

#### Hybrid 7: The Rescue - List Processing Functions

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | decode_error | Error in list function |
| 2 | INVESTIGATION | complete_function | Fix and complete the function |
| 3 | IMPROVEMENT | add_error_handling | Handle edge cases (empty list, etc.) |

**Placement:** Cluster G (functions with lists)
**Difficulty:** 4
**Arc:** Rescue

#### Hybrid 8: The Upgrade - Function Toolkit

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | EVALUATION | which_is_better | Compare monolithic vs modular |
| 2 | IMPROVEMENT | simplify_code | Break into helper functions |
| 3 | GROWTH | write_code | Add more toolkit functions |

**Placement:** Cluster G (functions with lists)
**Difficulty:** 4-5
**Arc:** Upgrade (3-part variant)

#### Hybrid 9: Mini Project - The Function Workshop

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | blank_page | Design function signatures |
| 2 | GROWTH | write_code | Implement core functions |
| 3 | GROWTH | write_code | Build the main program using functions |
| 4 | IMPROVEMENT | fix_style | Polish naming and documentation |

**Placement:** End of module, as capstone
**Difficulty:** 5
**Arc:** Custom (Design -> Build -> Polish)

---

## 4. Difficulty Progression Map

```
Difficulty:  1 -----> 2 -----> 3 -----> 4 -----> 5
             |       |        |        |        |
Exercises:   1,2     3,4,5    9,10     13       H9
             H1      6,7,8    11,12    H5,H6
                     H2       H3,H4    H7,H8
```

H1-H9 = Hybrid exercises

---

## 5. File Structure

```
exercises/
└── module_4_functions/
    ├── write_code/
    │   ├── exercise_1_basic_functions.py
    │   ├── exercise_2_with_parameters.py
    │   └── exercise_3_returning_values.py
    ├── complete_function/
    │   ├── exercise_1_return_statements.py
    │   └── exercise_2_default_params.py
    ├── fill_blanks/
    │   ├── exercise_1_function_syntax.py
    │   └── exercise_2_parameters.py
    ├── code_ordering/
    │   └── exercise_1_function_structure.py
    ├── fix_style/
    │   └── exercise_1_naming_conventions.py
    ├── simplify_code/
    │   └── exercise_1_refactor_to_functions.py
    ├── which_is_better/
    │   └── exercise_1_return_vs_print.py
    ├── spot_difference/
    │   └── exercise_1_return_print_bugs.py
    ├── decode_error/
    │   └── exercise_1_none_type_error.py
    └── hybrid/
        ├── exercise_1_apprentice_foundations.py
        ├── exercise_2_apprentice_returns.py
        ├── exercise_3_rescue_calculator.py
        ├── exercise_4_upgrade_reuse.py
        ├── exercise_5_competition_design.py
        ├── exercise_6_inheritance_library.py
        ├── exercise_7_rescue_lists.py
        ├── exercise_8_upgrade_toolkit.py
        └── exercise_9_project_workshop.py
```

---

## 6. Implementation Phases

Implementation is organized into 8 phases following the concept progression.

**After completing each phase:** Mark it with a checkmark below the phase header.

### Phase 1: Basic Function Definition + Hybrid 1 (Cluster A)

**Exercises:** 1, 2, Hybrid 1
**Difficulty:** 1
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 1 | fill_blanks | `fill_blanks/exercise_1_function_syntax.py` |
| 2 | write_code | `write_code/exercise_1_basic_functions.py` |
| H1 | hybrid (apprentice) | `hybrid/exercise_1_apprentice_foundations.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| fill_blanks | [templates/exercise_types/fill_blanks.py](../../templates/exercise_types/fill_blanks.py) |
| write_code | [templates/exercise_types/write_code.py](../../templates/exercise_types/write_code.py) |
| complete_function | [templates/exercise_types/complete_function.py](../../templates/exercise_types/complete_function.py) |
| hybrid_arcs README | [templates/hybrid_arcs/README.md](../../templates/hybrid_arcs/README.md) |
| apprentice arc | [templates/hybrid_arcs/apprentice.md](../../templates/hybrid_arcs/apprentice.md) |

---

### Phase 2: Parameters (Cluster B)

**Exercises:** 3, 4, 5
**Difficulty:** 2
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 3 | fill_blanks | `fill_blanks/exercise_2_parameters.py` |
| 4 | code_ordering | `code_ordering/exercise_1_function_structure.py` |
| 5 | write_code | `write_code/exercise_2_with_parameters.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| code_ordering | [templates/exercise_types/code_ordering.py](../../templates/exercise_types/code_ordering.py) |

---

### Phase 3: Return Values + Hybrid 2 (Cluster C)

**Exercises:** 6, 7, 8, Hybrid 2
**Difficulty:** 2-3
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 6 | complete_function | `complete_function/exercise_1_return_statements.py` |
| 7 | write_code | `write_code/exercise_3_returning_values.py` |
| 8 | decode_error | `decode_error/exercise_1_none_type_error.py` |
| H2 | hybrid (apprentice) | `hybrid/exercise_2_apprentice_returns.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| decode_error | [templates/exercise_types/decode_error.py](../../templates/exercise_types/decode_error.py) |
| spot_difference | [templates/exercise_types/spot_difference.py](../../templates/exercise_types/spot_difference.py) |

---

### Phase 4: Return vs Print + Hybrid 3 (Cluster D)

**Exercises:** 9, 10, Hybrid 3
**Difficulty:** 3
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 9 | spot_difference | `spot_difference/exercise_1_return_print_bugs.py` |
| 10 | which_is_better | `which_is_better/exercise_1_return_vs_print.py` |
| H3 | hybrid (rescue) | `hybrid/exercise_3_rescue_calculator.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| which_is_better | [templates/exercise_types/which_is_better.py](../../templates/exercise_types/which_is_better.py) |
| add_error_handling | [templates/exercise_types/add_error_handling.py](../../templates/exercise_types/add_error_handling.py) |
| rescue arc | [templates/hybrid_arcs/rescue.md](../../templates/hybrid_arcs/rescue.md) |

---

### Phase 5: Default Parameters + Hybrid 4 (Cluster E)

**Exercises:** 11, 12, Hybrid 4
**Difficulty:** 3
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 11 | complete_function | `complete_function/exercise_2_default_params.py` |
| 12 | fix_style | `fix_style/exercise_1_naming_conventions.py` |
| H4 | hybrid (upgrade) | `hybrid/exercise_4_upgrade_reuse.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| fix_style | [templates/exercise_types/fix_style.py](../../templates/exercise_types/fix_style.py) |
| simplify_code | [templates/exercise_types/simplify_code.py](../../templates/exercise_types/simplify_code.py) |
| upgrade arc | [templates/hybrid_arcs/upgrade.md](../../templates/hybrid_arcs/upgrade.md) |

---

### Phase 6: Local Scope + Hybrids 5, 6 (Cluster F)

**Exercises:** 13, Hybrid 5, Hybrid 6
**Difficulty:** 3-4
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 13 | simplify_code | `simplify_code/exercise_1_refactor_to_functions.py` |
| H5 | hybrid (competition) | `hybrid/exercise_5_competition_design.py` |
| H6 | hybrid (inheritance) | `hybrid/exercise_6_inheritance_library.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| competition arc | [templates/hybrid_arcs/competition.md](../../templates/hybrid_arcs/competition.md) |
| inheritance arc | [templates/hybrid_arcs/inheritance.md](../../templates/hybrid_arcs/inheritance.md) |

---

### Phase 7: Functions with Lists + Hybrids 7, 8 (Cluster G)

**Exercises:** Hybrid 7, Hybrid 8
**Difficulty:** 4
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| H7 | hybrid (rescue) | `hybrid/exercise_7_rescue_lists.py` |
| H8 | hybrid (upgrade) | `hybrid/exercise_8_upgrade_toolkit.py` |

**Read Before This Phase:**

*(All templates already read in previous phases)*

---

### Phase 8: Capstone (Cluster H)

**Exercises:** Hybrid 9
**Difficulty:** 5
**Estimated Files:** 1

| # | Type | File |
|---|------|------|
| H9 | hybrid (mini_project) | `hybrid/exercise_9_project_workshop.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| mini_project | [templates/exercise_types/mini_project.py](../../templates/exercise_types/mini_project.py) |
| blank_page | [templates/exercise_types/blank_page.py](../../templates/exercise_types/blank_page.py) |

---

### Phase Summary

| Phase | Cluster | Exercises | Files | New Templates |
|:-----:|---------|-----------|:-----:|---------------|
| 1 | Basic Definition + H1 | 1-2, H1 | 3 | fill_blanks, write_code, complete_function, apprentice |
| 2 | Parameters | 3-5 | 3 | code_ordering |
| 3 | Return Values + H2 | 6-8, H2 | 4 | decode_error, spot_difference |
| 4 | Return vs Print + H3 | 9-10, H3 | 3 | which_is_better, add_error_handling, rescue |
| 5 | Default Params + H4 | 11-12, H4 | 3 | fix_style, simplify_code, upgrade |
| 6 | Scope + H5, H6 | 13, H5, H6 | 3 | competition, inheritance |
| 7 | Lists + H7, H8 | H7, H8 | 2 | *(none)* |
| 8 | Capstone | H9 | 1 | mini_project, blank_page |
| **Total** | | **22** | **22** | |

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every exercise contains at least one `{{placeholder}}`
- [ ] NO concepts from later modules used (no while/random/dicts/try-except)
- [ ] All 9 learning objectives covered
- [ ] Progressive difficulty (1 to 5)
- [ ] Hybrid ratio within 40-55%

### Format Requirements

- [ ] All functions use `pass` placeholder
- [ ] Instructions use `# YOUR CODE HERE` marker
- [ ] Each file has `main()` that calls all exercises
- [ ] PEP 8 compliant
- [ ] Follows templates from `templates/exercise_types/`

### Curriculum Compliance

| Concept | Used In |
|---------|---------|
| def syntax | Exercises 1, 2, H1 |
| parameters | Exercises 3, 4, 5 |
| return values | Exercises 6, 7, 8, H2 |
| return vs print | Exercises 9, 10, H3 |
| default parameters | Exercises 11, 12, H4 |
| local scope | Exercise 13, H5, H6 |
| functions with lists | H7, H8 |
| design/integration | H9 |

---

## 8. Implementation Notes

### Key Constraints

1. **No while loops** - Students can only use for loops
2. **No try/except** - Error handling via if-statement validation only
3. **No random** - Cannot use random module yet
4. **No global keyword** - Teach good practices, avoid global state
5. **No *args/**kwargs** - Too advanced for this level

### Pedagogical Considerations

**Why functions are challenging:**
- Abstraction is a conceptual leap
- Parameters vs arguments confusion
- Return vs print is the #1 beginner mistake
- Scope is invisible and counterintuitive
- When to create a function is a design skill

**Building mental models:**
- Functions as "machines" that take input and produce output
- Parameters as "slots" that receive values
- Return as "sending back" a value vs print as "showing" a value
- Scope as "boxes inside boxes"

**The return vs print problem:**
```python
def add(a, b):
    print(a + b)  # WRONG - returns None

result = add(2, 3)  # result is None!
```

This is covered explicitly in Cluster D and multiple hybrids.

### Common Bugs to Include

1. **Forgetting return:** Function prints but doesn't return
2. **Using print instead of return:** Then wondering why result is None
3. **Forgetting to call:** Referencing function without parentheses
4. **Parameter mismatch:** Wrong number of arguments
5. **Scope confusion:** Trying to access local variable outside function
6. **Mutating list parameter:** Surprising side effects
7. **Forgetting colon:** `def greet(name)` missing `:`

### Function Patterns to Cover

| Pattern | Purpose | Exercise Coverage |
|---------|---------|-------------------|
| `def greet():` | No params, no return | Phase 1 |
| `def greet(name):` | With parameter | Phase 2 |
| `def add(a, b):` | Multiple params | Phase 2 |
| `def add(a, b): return a + b` | With return | Phase 3 |
| `def greet(name="World"):` | Default param | Phase 5 |
| `def process(items):` | List parameter | Phase 7 |

### Placeholder Usage Ideas

- `{{hero}}` as function parameter for character name
- `{{spell1}}`, `{{spell2}}` as function names (cast_spell, calculate_power)
- `{{school}}` grading functions
- `{{item}}` inventory management functions
- `{{creature}}` stat calculation functions
- `{{mentor}}` providing function signatures to complete

### Arc Selection Rationale

| Arc | Count | Why Selected |
|-----|:-----:|--------------|
| **Apprentice** | 2 | Perfect for learning new syntax with scaffolding |
| **Rescue** | 2 | Error interpretation and validation are key function skills |
| **Upgrade** | 2 | Refactoring to functions is a core learning outcome |
| **Competition** | 1 | Comparing function designs teaches good practices |
| **Inheritance** | 1 | Working with existing function libraries is realistic |
| **Mini Project** | 1 | Capstone requires function design from scratch |

### Arcs NOT Used (and why)

| Arc | Why Not |
|-----|---------|
| Rivalry | Requires bug_hunt which isn't available for functions |
| Mystery | Requires output_prediction which isn't available |

---

## 9. Concept-Specific Teaching Notes

### Basic Function Definition (Cluster A)

- Start with functions that just print
- Emphasize the `def` keyword
- Show that calling requires parentheses: `greet()` not `greet`
- Indentation defines the body

### Parameters (Cluster B)

- Parameters are "named slots" for incoming data
- Arguments are the actual values passed
- Order matters for positional parameters
- Multiple parameters separated by commas

### Return Values (Cluster C)

- `return` sends a value back to the caller
- Without `return`, function returns `None`
- `return` immediately exits the function
- Return value can be stored in a variable

### Return vs Print (Cluster D)

**This is the most critical concept to emphasize.**

- `print()` shows text to the user - for humans
- `return` sends data back to the program - for code
- A function can do both, but they serve different purposes
- Test: "Can I use this result in a calculation?"

### Default Parameters (Cluster E)

- Provide a value that's used if caller doesn't pass one
- `def greet(name="World"):`
- Default parameters must come after required ones
- Useful for optional configuration

### Local Scope (Cluster F)

- Variables created inside a function are local
- They disappear when the function ends
- Parameters are also local variables
- Cannot access local variables from outside
- This prevents accidental interference between functions

### Functions with Lists (Cluster G)

- Lists passed to functions can be modified in place
- This is because lists are mutable
- Surprising for beginners: function can change your list!
- If you don't want modification, pass a copy

### Function Design (Cluster H)

- One function should do one thing
- Name should describe what it does
- Parameters for input, return for output
- If a function is too long, break it into helpers
- Good functions are reusable

---
