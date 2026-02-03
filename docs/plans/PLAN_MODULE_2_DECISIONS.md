# Plan: Module 2 - Decisions

Recreation plan for module_2_decisions using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_2_decisions |
| **Topic** | Conditionals and Boolean logic |
| **Prerequisites** | module_0_basics, module_1_turtle_loops |
| **Target Hybrid Ratio** | 25-35% |

### Learning Objectives

By the end of this module, students will be able to:

1. Use `if` statements to execute code conditionally
2. Use `if/else` for two-branch decisions
3. Use `if/elif/else` for multi-branch decisions
4. Apply comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
5. Combine conditions using `and`, `or`, `not`
6. Trace conditional execution paths through code
7. Debug conditional logic errors

### Curriculum Constraints

| Available Concepts | NOT Available (later modules) |
|--------------------|-------------------------------|
| **From Module 0:** | |
| print(), variables | lists, indexing |
| strings, concatenation | functions (def) |
| integers, floats | dictionaries |
| input(), type conversion | while loops |
| f-strings | try/except |
| math: +, -, *, /, //, %, ** | random module |
| **From Module 1:** | classes, methods |
| for loops | import (except turtle) |
| range(stop), range(start, stop), range(start, stop, step) | |
| turtle graphics | |
| **New in Module 2:** | |
| if statements | |
| if/else | |
| if/elif/else | |
| == != < > <= >= | |
| and, or, not | |
| True, False | |

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types for Module 2 (see "module_2_decisions" section) |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Exercise format standards |
| [common-struggles.md](../../references/pedagogy/common-struggles.md) | Boolean logic challenges |

**Note:** Phase-specific templates are listed in each implementation phase below.

---

## 2. Exercise Distribution

### Available Exercise Types (4 total)

| Category | Types |
|----------|-------|
| **Core** | write_code |
| **Reading** | output_prediction, code_tracing |
| **Debugging** | bug_hunt |

**Important:** Module 2 has the fewest exercise types of any module. This is intentional - conditionals are conceptually dense and benefit from focused practice on these four core activities.

### Target Distribution

| Type | Count | Rationale |
|------|:-----:|-----------|
| write_code | 6 | Core practice for each conditional pattern |
| output_prediction | 3 | Build mental model of branching execution |
| code_tracing | 3 | Track variable values through conditional paths |
| bug_hunt | 3 | Find common conditional logic errors |
| **hybrid** | 4 | Multi-part narrative exercises (25-35% target) |
| **TOTAL** | **19** | |

### Hybrid Ratio Calculation

- Total exercises: 19
- Hybrid exercises: 4
- Ratio: **21%** (edges toward 25-35% target range)

Note: With only 4 exercise types available, achieving a higher hybrid ratio is challenging while maintaining variety. The 21% ratio represents a reasonable balance.

---

## 3. Exercise Inventory

### Concept Progression

Exercises are organized into concept clusters, progressing from simple to complex.

| Cluster | Concepts | Difficulty |
|---------|----------|:----------:|
| A | Simple if statements | 1 |
| B | if/else (two branches) | 2 |
| C | Comparison operators | 2-3 |
| D | if/elif/else (multi-branch) | 3 |
| E | Boolean operators (and/or/not) | 4 |
| F | Integration | 5 |

### Isolated Exercises

#### Cluster A: Simple if Statements (Difficulty 1)

| # | Type | Concept Focus |
|---|------|---------------|
| 1 | output_prediction | Predict if code with `if` will execute |
| 2 | write_code | Write simple if statements |

#### Cluster B: if/else (Difficulty 2)

| # | Type | Concept Focus |
|---|------|---------------|
| 3 | output_prediction | Predict which branch executes |
| 4 | code_tracing | Trace variable values through if/else |
| 5 | write_code | Write if/else for binary decisions |

#### Cluster C: Comparison Operators (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 6 | output_prediction | Predict comparison results |
| 7 | write_code | Use various comparison operators |

#### Cluster D: if/elif/else (Difficulty 3)

| # | Type | Concept Focus |
|---|------|---------------|
| 8 | code_tracing | Trace through multi-branch conditionals |
| 9 | write_code | Write if/elif/else chains |

#### Cluster E: Boolean Operators (Difficulty 4)

| # | Type | Concept Focus |
|---|------|---------------|
| 10 | code_tracing | Trace compound conditions with and/or/not |
| 11 | write_code | Combine conditions with boolean operators |
| 12 | bug_hunt | Find errors in boolean expressions |

#### Cluster F: Integration (Difficulty 5)

| # | Type | Concept Focus |
|---|------|---------------|
| 13 | bug_hunt | Fix bugs across all conditional concepts |
| 14 | bug_hunt | Debug a program with nested conditionals |
| 15 | write_code | Combine loops and conditionals |

### Hybrid Exercises

#### Hybrid 1: The Mystery - Unexpected Branch

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | output_prediction | Observe unexpected conditional behavior |
| 2 | INVESTIGATION | code_tracing | Trace to find which branch executed |
| 3 | IMPROVEMENT | bug_hunt | Fix the conditional logic |

**Placement:** After Cluster B (if/else), as first integration
**Difficulty:** 2-3
**Arc:** Mystery

#### Hybrid 2: The Inheritance - The Sorting System

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | code_tracing | Understand inherited conditional code |
| 2 | OWNERSHIP | write_code | Add a new branch to the system |
| 3 | INVESTIGATION | bug_hunt | Find and fix a hidden edge case |

**Placement:** After Cluster D (if/elif/else)
**Difficulty:** 3-4
**Arc:** Inheritance

#### Hybrid 3: The Mystery - Boolean Confusion

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | output_prediction | Observe confusing boolean behavior |
| 2 | INVESTIGATION | code_tracing | Trace and/or/not evaluation |
| 3 | IMPROVEMENT | bug_hunt | Fix the boolean expression |

**Placement:** After Cluster E (boolean operators)
**Difficulty:** 4
**Arc:** Mystery

#### Hybrid 4: The Rivalry - Conditional Challenge

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | bug_hunt | Analyze failed conditional code |
| 2 | GROWTH | write_code | Build improved conditional logic |
| 3 | CONFRONTATION | write_code | Create a complete decision system |

**Placement:** End of module, as capstone
**Difficulty:** 5
**Arc:** Rivalry

---

## 4. Difficulty Progression Map

```
Difficulty:  1 -----> 2 -----> 3 -----> 4 -----> 5
             |       |        |        |        |
Exercises:   1,2     3,4,5    6,7      10,11,12 13,14,15
                     H1       8,9      H3       H4
                              H2
```

H1 = Hybrid 1, H2 = Hybrid 2, H3 = Hybrid 3, H4 = Hybrid 4

---

## 5. File Structure

```
exercises/
└── module_2_decisions/
    ├── output_prediction/
    │   ├── exercise_1_simple_if.py
    │   ├── exercise_2_if_else_branches.py
    │   └── exercise_3_comparisons.py
    ├── write_code/
    │   ├── exercise_1_simple_if.py
    │   ├── exercise_2_if_else.py
    │   ├── exercise_3_comparisons.py
    │   ├── exercise_4_elif_chains.py
    │   ├── exercise_5_boolean_operators.py
    │   └── exercise_6_loops_and_conditions.py
    ├── code_tracing/
    │   ├── exercise_1_if_else_trace.py
    │   ├── exercise_2_elif_trace.py
    │   └── exercise_3_boolean_trace.py
    ├── bug_hunt/
    │   ├── exercise_1_boolean_bugs.py
    │   ├── exercise_2_conditional_bugs.py
    │   └── exercise_3_nested_bugs.py
    └── hybrid/
        ├── exercise_1_mystery_branch.py
        ├── exercise_2_inheritance_sorting.py
        ├── exercise_3_mystery_boolean.py
        └── exercise_4_rivalry_challenge.py
```

---

## 6. Implementation Phases

Implementation is organized into 6 phases following the concept progression.

**After completing each phase:** Mark it with ✅ COMPLETE below the phase header.

### Phase 1: Simple if Statements (Cluster A)

**Exercises:** 1, 2
**Difficulty:** 1
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| 1 | output_prediction | `output_prediction/exercise_1_simple_if.py` |
| 2 | write_code | `write_code/exercise_1_simple_if.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| output_prediction | [templates/exercise_types/output_prediction.py](../../templates/exercise_types/output_prediction.py) |
| write_code | [templates/exercise_types/write_code.py](../../templates/exercise_types/write_code.py) |

---

### Phase 2: if/else + Hybrid 1 (Cluster B)

**Exercises:** 3, 4, 5, Hybrid 1
**Difficulty:** 2
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 3 | output_prediction | `output_prediction/exercise_2_if_else_branches.py` |
| 4 | code_tracing | `code_tracing/exercise_1_if_else_trace.py` |
| 5 | write_code | `write_code/exercise_2_if_else.py` |
| H1 | hybrid (mystery) | `hybrid/exercise_1_mystery_branch.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| code_tracing | [templates/exercise_types/code_tracing.py](../../templates/exercise_types/code_tracing.py) |
| hybrid_arcs README | [templates/hybrid_arcs/README.md](../../templates/hybrid_arcs/README.md) |
| mystery arc | [templates/hybrid_arcs/mystery.md](../../templates/hybrid_arcs/mystery.md) |

---

### Phase 3: Comparison Operators (Cluster C)

**Exercises:** 6, 7
**Difficulty:** 2-3
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| 6 | output_prediction | `output_prediction/exercise_3_comparisons.py` |
| 7 | write_code | `write_code/exercise_3_comparisons.py` |

**Read Before This Phase:**

*(All templates already read in previous phases)*

---

### Phase 4: if/elif/else + Hybrid 2 (Cluster D)

**Exercises:** 8, 9, Hybrid 2
**Difficulty:** 3
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 8 | code_tracing | `code_tracing/exercise_2_elif_trace.py` |
| 9 | write_code | `write_code/exercise_4_elif_chains.py` |
| H2 | hybrid (inheritance) | `hybrid/exercise_2_inheritance_sorting.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| inheritance arc | [templates/hybrid_arcs/inheritance.md](../../templates/hybrid_arcs/inheritance.md) |

---

### Phase 5: Boolean Operators + Hybrid 3 (Cluster E)

**Exercises:** 10, 11, 12, Hybrid 3
**Difficulty:** 4
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 10 | code_tracing | `code_tracing/exercise_3_boolean_trace.py` |
| 11 | write_code | `write_code/exercise_5_boolean_operators.py` |
| 12 | bug_hunt | `bug_hunt/exercise_1_boolean_bugs.py` |
| H3 | hybrid (mystery) | `hybrid/exercise_3_mystery_boolean.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| bug_hunt | [templates/exercise_types/bug_hunt.py](../../templates/exercise_types/bug_hunt.py) |

---

### Phase 6: Integration + Hybrid 4 (Cluster F)

**Exercises:** 13, 14, 15, Hybrid 4
**Difficulty:** 5
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 13 | bug_hunt | `bug_hunt/exercise_2_conditional_bugs.py` |
| 14 | bug_hunt | `bug_hunt/exercise_3_nested_bugs.py` |
| 15 | write_code | `write_code/exercise_6_loops_and_conditions.py` |
| H4 | hybrid (rivalry) | `hybrid/exercise_4_rivalry_challenge.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| rivalry arc | [templates/hybrid_arcs/rivalry.md](../../templates/hybrid_arcs/rivalry.md) |

---

### Phase Summary

| Phase | Cluster | Exercises | Files | New Templates |
|:-----:|---------|-----------|:-----:|---------------|
| 1 | Simple if | 1-2 | 2 | output_prediction, write_code |
| 2 | if/else + H1 | 3-5, H1 | 4 | code_tracing, mystery arc |
| 3 | Comparisons | 6-7 | 2 | *(none)* |
| 4 | elif + H2 | 8-9, H2 | 3 | inheritance arc |
| 5 | Boolean + H3 | 10-12, H3 | 4 | bug_hunt |
| 6 | Integration + H4 | 13-15, H4 | 4 | rivalry arc |
| **Total** | | **19** | **19** | |

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every exercise contains at least one `{{placeholder}}`
- [ ] NO concepts from later modules used (no lists/functions/while/dicts)
- [ ] All 7 learning objectives covered
- [ ] Progressive difficulty (1 to 5)
- [ ] Hybrid ratio within 21-35%

### Format Requirements

- [ ] All functions use `pass` placeholder
- [ ] Instructions use `# ✏️ YOUR CODE HERE ✏️` marker
- [ ] Each file has `main()` that calls all exercises
- [ ] PEP 8 compliant
- [ ] Follows templates from `templates/exercise_types/`

### Curriculum Compliance

| Concept | Used In |
|---------|---------|
| simple if | Exercises 1, 2 |
| if/else | Exercises 3, 4, 5, Hybrid 1 |
| comparisons | Exercises 6, 7 |
| if/elif/else | Exercises 8, 9, Hybrid 2 |
| and/or/not | Exercises 10, 11, 12, Hybrid 3 |
| integration | Exercises 13, 14, 15, Hybrid 4 |

---

## 8. Implementation Notes

### Key Constraints

1. **No lists** - Cannot use lists or indexing
2. **No functions defined by student** - Use conditional logic without custom functions
3. **No while loops** - Only for loops from Module 1
4. **No try/except** - Error handling comes in Module 5
5. **No random** - Deterministic conditionals only (random comes in Module 5)

### Pedagogical Considerations

**Why conditionals are challenging:**
- Multiple execution paths to track mentally
- Boolean logic (especially `and`/`or`) requires formal reasoning
- Common confusion: `=` vs `==`
- Edge cases with comparisons (off-by-one with `<` vs `<=`)
- Nested conditionals multiply complexity

**Building mental models:**
- Start with simple yes/no conditions
- Progress to either/or (if/else)
- Then multiple choices (if/elif/else)
- Finally compound conditions (and/or/not)

**Tracing emphasis:**
- code_tracing exercises are critical for conditionals
- Students must predict which branch executes
- Track variable values BEFORE and AFTER conditionals

### Common Bugs to Include in bug_hunt

1. **Assignment vs comparison:** `if x = 5:` instead of `if x == 5:`
2. **Off-by-one in comparisons:** `< 10` when should be `<= 10`
3. **Boolean operator confusion:** `and` when should be `or`
4. **Negation errors:** `not x > 5` vs `x <= 5`
5. **Missing colons:** `if x == 5` (no colon)
6. **Unreachable code:** elif after a catch-all else
7. **Wrong operator order:** `5 < x < 10` works but `5 > x > 10` is confusing

### Combining Loops and Conditionals

Exercise 15 and Hybrid 4 should combine for loops with conditionals:
- Count items meeting a condition
- Find first/last item matching criteria
- Conditional actions inside loops

This prepares students for lists module where they'll iterate AND filter.

### Placeholder Usage Ideas

- `{{hero}}` making decisions
- `{{school}}` sorting students into `{{house}}`
- `{{item}}` quality checks (pass/fail)
- `{{spell1}}` vs `{{spell2}}` comparison
- `{{villain}}` detection (conditional guards)
- `{{location}}` access control (password checks)

### Arc Selection Rationale

| Arc | Why Selected |
|-----|--------------|
| **Mystery** (x2) | Perfect for conditionals - "why did this branch execute?" |
| **Inheritance** | Extends existing conditional logic - adds new branch |
| **Rivalry** | Capstone arc - defeat bugs then build better code |

### Arcs NOT Used (and why)

| Arc | Why Not |
|-----|---------|
| Apprentice | Requires fill_blanks or complete_function (not available) |
| Rescue | Requires decode_error and simplify_code (not available) |
| Upgrade | Requires which_is_better and simplify_code (not available) |
| Competition | Requires which_is_better (not available) |

---

## 9. Concept-Specific Teaching Notes

### Simple if (Cluster A)

- Introduce the basic pattern: `if condition:`
- Use simple True/False conditions first
- Progress to variable comparisons
- Emphasize indentation matters

### if/else (Cluster B)

- Two mutually exclusive outcomes
- "Either this happens OR that happens"
- No overlap between branches

### Comparison Operators (Cluster C)

- `==` and `!=` for equality
- `<`, `>`, `<=`, `>=` for ordering
- Emphasize difference between `=` (assignment) and `==` (comparison)
- Show edge cases: is 5 < 5? (no), is 5 <= 5? (yes)

### if/elif/else (Cluster D)

- Multiple mutually exclusive options
- Only ONE branch executes
- Order matters! First match wins
- `else` is the catch-all

### Boolean Operators (Cluster E)

- `and`: both must be True
- `or`: at least one must be True
- `not`: inverts True/False
- Operator precedence: `not` > `and` > `or`
- Encourage parentheses for clarity

### Integration (Cluster F)

- Loops with conditionals inside
- Counting/finding patterns
- Nested conditionals (carefully - can get complex)
- Prepare for lists module

---
