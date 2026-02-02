# Plan: Module 1 - Turtle Loops

Recreation plan for module_1_turtle_loops using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_1_turtle_loops |
| **Topic** | For loops and turtle graphics |
| **Prerequisites** | module_0_basics |
| **Target Hybrid Ratio** | 10-20% |

### Learning Objectives

By the end of this module, students will be able to:

1. Use basic turtle commands (forward, backward, right, left)
2. Write `for` loops with `range()` to repeat actions
3. Use `range()` with 1, 2, and 3 arguments
4. Create geometric shapes using loops
5. Trace loop execution and predict output
6. Debug visual programs using turtle feedback

### Curriculum Constraints

| Available Concepts | NOT Available (later modules) |
|--------------------|-------------------------------|
| **From Module 0:** | |
| print(), variables | if/elif/else |
| strings, concatenation | lists, indexing |
| integers, floats | functions (def) |
| input(), type conversion | dictionaries |
| f-strings | while loops |
| math: +, -, *, /, //, %, ** | random module |
| **New in Module 1:** | classes, methods |
| for loops | try/except |
| range(stop) | nested loops (advanced) |
| range(start, stop) | |
| range(start, stop, step) | |
| turtle.forward(), .backward() | |
| turtle.right(), .left() | |
| turtle.penup(), .pendown() | |
| turtle.color(), .pensize() | |

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types for Module 1 (see "module_1_turtle_loops" section) |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE.md](WRITING_GUIDE.md) | Format standards |
| [common-struggles.md](../../references/pedagogy/common-struggles.md) | Loop mental model challenges |

**Note:** Phase-specific templates are listed in each implementation phase below.

---

## 2. Exercise Distribution

### Available Exercise Types (7 total)

| Category | Types |
|----------|-------|
| **Core** | write_code |
| **Reading** | output_prediction, code_tracing, match_output |
| **Scaffolded** | fill_blanks, code_ordering |
| **Debugging** | bug_hunt |

### Target Distribution

| Type | Count | Rationale |
|------|:-----:|-----------|
| write_code | 6 | Core practice for each concept cluster |
| output_prediction | 2 | Build mental model of loop execution |
| code_tracing | 2 | Track variables through iterations |
| match_output | 1 | Pattern recognition for loop output |
| fill_blanks | 2 | Syntax reinforcement for loop structure |
| code_ordering | 1 | Understand loop flow and turtle sequence |
| bug_hunt | 2 | Visual debugging with turtle feedback |
| **hybrid** | 2 | Multi-part narrative exercises |
| **TOTAL** | **18** | |

### Hybrid Ratio Calculation

- Total exercises: 18
- Hybrid exercises: 2
- Ratio: **11%** (within 10-20% target)

---

## 3. Exercise Inventory

### Concept Progression

Exercises are organized into concept clusters, progressing from simple to complex.

| Cluster | Concepts | Difficulty |
|---------|----------|:----------:|
| A | Turtle basics (commands without loops) | 1 |
| B | For loop introduction (range with 1 arg) | 2 |
| C | Range variations (2-arg and 3-arg) | 3 |
| D | Shape patterns (loops + turtle) | 3-4 |
| E | Loop control patterns | 4 |
| F | Integration | 5 |

### Isolated Exercises

#### Cluster A: Turtle Basics (Difficulty 1)

| # | Type | Concept Focus |
|---|------|---------------|
| 1 | output_prediction | Predict turtle position after commands |
| 2 | write_code | Write basic turtle movement sequences |

#### Cluster B: For Loop Introduction (Difficulty 2)

| # | Type | Concept Focus |
|---|------|---------------|
| 3 | fill_blanks | For loop and range() syntax |
| 4 | code_ordering | Order statements to draw a shape with loop |
| 5 | write_code | Use for loop to repeat turtle commands |

#### Cluster C: Range Variations (Difficulty 3)

| # | Type | Concept Focus |
|---|------|---------------|
| 6 | output_prediction | Predict range() output with different arguments |
| 7 | code_tracing | Trace loop variable values through iterations |
| 8 | write_code | Use range(start, stop) and range(start, stop, step) |

#### Cluster D: Shape Patterns (Difficulty 3-4)

| # | Type | Concept Focus |
|---|------|---------------|
| 9 | match_output | Match code to shape output |
| 10 | write_code | Draw regular polygons using loops |
| 11 | write_code | Draw patterns with calculated angles |

#### Cluster E: Loop Control Patterns (Difficulty 4)

| # | Type | Concept Focus |
|---|------|---------------|
| 12 | fill_blanks | Loop with accumulator pattern |
| 13 | code_tracing | Trace accumulator values |
| 14 | write_code | Build patterns with changing values |

#### Cluster F: Integration (Difficulty 5)

| # | Type | Concept Focus |
|---|------|---------------|
| 15 | bug_hunt | Fix bugs in turtle loop programs |
| 16 | bug_hunt | Debug a multi-step drawing program |

### Hybrid Exercises

#### Hybrid 1: The Apprentice - Learning Loops

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | output_prediction | Study how a loop draws |
| 2 | GUIDANCE | fill_blanks | Complete a similar loop |
| 3 | GROWTH | write_code | Create your own loop drawing |

**Placement:** After Cluster C (range variations), before shapes
**Difficulty:** 3

#### Hybrid 2: The Mystery - Strange Shapes

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | output_prediction | Observe unexpected output |
| 2 | INVESTIGATION | code_tracing | Trace to find the cause |
| 3 | IMPROVEMENT | bug_hunt | Fix the issue |

**Placement:** End of module, as integration
**Difficulty:** 4-5

---

## 4. Difficulty Progression Map

```
Difficulty:  1 -----> 2 -----> 3 -----> 4 -----> 5
             |       |        |        |        |
Exercises:   1,2     3,4,5    6,7,8    12,13,14 15,16
                              H1       9,10,11  H2
```

H1 = Hybrid 1, H2 = Hybrid 2

---

## 5. File Structure

```
exercises/
└── module_1_turtle_loops/
    ├── output_prediction/
    │   ├── exercise_1_turtle_position.py
    │   └── exercise_2_range_output.py
    ├── write_code/
    │   ├── exercise_1_turtle_basics.py
    │   ├── exercise_2_first_loop.py
    │   ├── exercise_3_range_variations.py
    │   ├── exercise_4_polygons.py
    │   ├── exercise_5_pattern_angles.py
    │   └── exercise_6_changing_values.py
    ├── fill_blanks/
    │   ├── exercise_1_loop_syntax.py
    │   └── exercise_2_accumulator.py
    ├── code_ordering/
    │   └── exercise_1_shape_sequence.py
    ├── code_tracing/
    │   ├── exercise_1_loop_variables.py
    │   └── exercise_2_accumulator_trace.py
    ├── match_output/
    │   └── exercise_1_code_to_shape.py
    ├── bug_hunt/
    │   ├── exercise_1_loop_bugs.py
    │   └── exercise_2_drawing_bugs.py
    └── hybrid/
        ├── exercise_1_apprentice_loops.py
        └── exercise_2_mystery_shapes.py
```

---

## 6. Implementation Phases

Implementation is organized into 6 phases following the concept progression.

**After completing each phase:** Mark it with COMPLETE below the phase header.

### Phase 1: Turtle Basics (Cluster A)

**Exercises:** 1, 2
**Difficulty:** 1
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| 1 | output_prediction | `output_prediction/exercise_1_turtle_position.py` |
| 2 | write_code | `write_code/exercise_1_turtle_basics.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| output_prediction | [templates/exercise_types/output_prediction.py](../../templates/exercise_types/output_prediction.py) |
| write_code | [templates/exercise_types/write_code.py](../../templates/exercise_types/write_code.py) |

---

### Phase 2: For Loop Introduction (Cluster B)

**Exercises:** 3, 4, 5
**Difficulty:** 2
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 3 | fill_blanks | `fill_blanks/exercise_1_loop_syntax.py` |
| 4 | code_ordering | `code_ordering/exercise_1_shape_sequence.py` |
| 5 | write_code | `write_code/exercise_2_first_loop.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| fill_blanks | [templates/exercise_types/fill_blanks.py](../../templates/exercise_types/fill_blanks.py) |
| code_ordering | [templates/exercise_types/code_ordering.py](../../templates/exercise_types/code_ordering.py) |

---

### Phase 3: Range Variations + Hybrid 1 (Cluster C)

**Exercises:** 6, 7, 8, Hybrid 1
**Difficulty:** 3
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 6 | output_prediction | `output_prediction/exercise_2_range_output.py` |
| 7 | code_tracing | `code_tracing/exercise_1_loop_variables.py` |
| 8 | write_code | `write_code/exercise_3_range_variations.py` |
| H1 | hybrid (apprentice) | `hybrid/exercise_1_apprentice_loops.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| code_tracing | [templates/exercise_types/code_tracing.py](../../templates/exercise_types/code_tracing.py) |
| hybrid_arcs README | [templates/hybrid_arcs/README.md](../../templates/hybrid_arcs/README.md) |
| apprentice arc | [templates/hybrid_arcs/apprentice.md](../../templates/hybrid_arcs/apprentice.md) |

---

### Phase 4: Shape Patterns (Cluster D)

**Exercises:** 9, 10, 11
**Difficulty:** 3-4
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 9 | match_output | `match_output/exercise_1_code_to_shape.py` |
| 10 | write_code | `write_code/exercise_4_polygons.py` |
| 11 | write_code | `write_code/exercise_5_pattern_angles.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| match_output | [templates/exercise_types/match_output.py](../../templates/exercise_types/match_output.py) |

---

### Phase 5: Loop Control Patterns (Cluster E)

**Exercises:** 12, 13, 14
**Difficulty:** 4
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 12 | fill_blanks | `fill_blanks/exercise_2_accumulator.py` |
| 13 | code_tracing | `code_tracing/exercise_2_accumulator_trace.py` |
| 14 | write_code | `write_code/exercise_6_changing_values.py` |

**Read Before This Phase:**

*(All templates already read in previous phases)*

---

### Phase 6: Integration + Hybrid 2 (Cluster F)

**Exercises:** 15, 16, Hybrid 2
**Difficulty:** 5
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 15 | bug_hunt | `bug_hunt/exercise_1_loop_bugs.py` |
| 16 | bug_hunt | `bug_hunt/exercise_2_drawing_bugs.py` |
| H2 | hybrid (mystery) | `hybrid/exercise_2_mystery_shapes.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| bug_hunt | [templates/exercise_types/bug_hunt.py](../../templates/exercise_types/bug_hunt.py) |
| mystery arc | [templates/hybrid_arcs/mystery.md](../../templates/hybrid_arcs/mystery.md) |

---

### Phase Summary

| Phase | Cluster | Exercises | Files | New Templates |
|:-----:|---------|-----------|:-----:|---------------|
| 1 | Turtle basics | 1-2 | 2 | output_prediction, write_code |
| 2 | For loops | 3-5 | 3 | fill_blanks, code_ordering |
| 3 | Range + H1 | 6-8, H1 | 4 | code_tracing, hybrid_arcs |
| 4 | Shapes | 9-11 | 3 | match_output |
| 5 | Loop patterns | 12-14 | 3 | *(none)* |
| 6 | Integration + H2 | 15-16, H2 | 3 | bug_hunt |
| **Total** | | **18** | **18** | |

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every exercise contains at least one `{{placeholder}}`
- [ ] NO concepts from later modules used (no if/while/functions/lists)
- [ ] All 6 learning objectives covered
- [ ] Progressive difficulty (1 to 5)
- [ ] Hybrid ratio within 10-20%

### Format Requirements

- [ ] All functions use `pass` placeholder
- [ ] Instructions use `# YOUR CODE HERE` marker
- [ ] Each file has `main()` that calls all exercises
- [ ] PEP 8 compliant
- [ ] Follows templates from `templates/exercise_types/`

### Curriculum Compliance

| Concept | Used In |
|---------|---------|
| turtle commands | Exercises 1, 2 (+ most others) |
| for loops | Exercises 3, 4, 5, Hybrid 1 |
| range() variations | Exercises 6, 7, 8 |
| shape patterns | Exercises 9, 10, 11 |
| loop control | Exercises 12, 13, 14 |
| integration | Exercises 15, 16, Hybrid 2 |

---

## 8. Implementation Notes

### Key Constraints

1. **No conditionals** - Cannot use if/elif/else
2. **No while loops** - Only for loops
3. **No functions defined by student** - They use turtle functions, not define their own
4. **No lists** - Cannot store values in lists
5. **No nested loops** - Keep to single-level loops (nested loops are advanced)

### Pedagogical Considerations

**Why turtle for loops?**
- Visual feedback makes abstract loop concept concrete
- Students see each iteration draw something
- Errors are visible (wrong shape = wrong code)
- Motivating - students create art

**Loop mental model building:**
- Start with fixed repetitions (range(4) for a square)
- Progress to range(start, stop) for numbered sequences
- End with range(start, stop, step) for skipping

**Tracing emphasis:**
- code_tracing exercises build loop mental models
- Track loop variable AND accumulated state
- Predict before running is key

### Turtle Setup Note

Exercises should include necessary turtle setup:
```python
import turtle

t = turtle.Turtle()
# Exercise code here
turtle.done()
```

Or use a `setup_turtle()` helper if pattern is repetitive.

### Common Pitfalls to Avoid

- Using `if` statements (not available yet)
- Using `while` loops (not until module 4/5)
- Using lists (not until module 3)
- Assuming functions are defined (complete_function not available in this module)
- Nested loops (too advanced for this level)

### Placeholder Usage Ideas

- `{{hero}}` draws shapes for `{{school}}`
- `{{creature}}` paths to trace
- `{{location}}` to map out
- `{{spell1}}`/`{{spell2}}` as loop iterations

---

## 9. Notes on Hybrid Arc Selection

### Why The Apprentice for Hybrid 1?

- **Module-appropriate:** Apprentice arc uses output_prediction, fill_blanks, write_code - all available in Module 1
- **Matches learning stage:** Students are new to loops, need scaffolded progression
- **Natural flow:** Observe master's loop → practice with guidance → create independently

### Why The Mystery for Hybrid 2?

- **Module-appropriate:** Mystery uses output_prediction, code_tracing, bug_hunt - all available
- **Engages debugging:** Turtle visual feedback makes "mystery" compelling
- **Integration exercise:** Combines all Module 1 skills in investigation narrative

### Arcs NOT Used (and why)

| Arc | Why Not |
|-----|---------|
| Rivalry | Requires bug_hunt + write_code combo that's better for later modules |
| Inheritance | Better when students have more concepts to "inherit" |
| Rescue | Requires decode_error + simplify_code (not available) |
| Upgrade | Requires which_is_better + simplify_code (not available) |
| Competition | Requires which_is_better (not available) |

---
