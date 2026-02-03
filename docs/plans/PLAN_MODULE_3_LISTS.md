# Plan: Module 3 - Lists

Recreation plan for module_3_lists using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_3_lists |
| **Topic** | Lists, indexing, slicing, list methods |
| **Prerequisites** | module_0_basics, module_1_turtle_loops, module_2_decisions |
| **Target Hybrid Ratio** | 25-35% |

### Learning Objectives

By the end of this module, students will be able to:

1. Create lists with various element types (strings, numbers, mixed)
2. Access list elements using positive indexing
3. Access list elements using negative indexing
4. Modify list elements by index assignment
5. Use list methods: `append()`, `pop()`, `insert()`, `remove()`
6. Slice lists to extract sublists with `[start:stop:step]`
7. Iterate over lists with for loops
8. Understand mutability and aliasing (two names, same list)
9. Use list operations: `len()`, `in` operator, concatenation (`+`), repetition (`*`)

### Curriculum Constraints

| Available Concepts | NOT Available (later modules) |
|--------------------|-------------------------------|
| **From Module 0:** | |
| print(), variables | functions (def, return) |
| strings, concatenation | dictionaries |
| integers, floats | while loops |
| input(), type conversion | try/except |
| f-strings | random module |
| math: +, -, *, /, //, %, ** | classes, methods |
| **From Module 1:** | file I/O |
| for loops | |
| range(stop), range(start, stop), range(start, stop, step) | |
| turtle graphics | |
| **From Module 2:** | |
| if/elif/else | |
| == != < > <= >= | |
| and, or, not | |
| **New in Module 3:** | |
| list literals `[1, 2, 3]` | |
| indexing `list[0]`, `list[-1]` | |
| slicing `list[1:3]`, `list[::2]` | |
| list methods: append, pop, insert, remove | |
| len(), in operator | |
| list concatenation (+) and repetition (*) | |
| mutability, aliasing | |

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types for Module 3 (see "module_3_lists" section) |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Exercise format standards |
| [common-struggles.md](../../references/pedagogy/common-struggles.md) | Indexing off-by-one, mutability confusion |

**Note:** Phase-specific templates are listed in each implementation phase below.

---

## 2. Exercise Distribution

### Available Exercise Types (9 total)

| Category | Types |
|----------|-------|
| **Core** | write_code, complete_function |
| **Reading** | code_tracing, match_output |
| **Improvement** | simplify_code |
| **Analysis** | which_is_better, spot_difference |
| **Debugging** | decode_error, bug_hunt |

**Note:** Module 3 has significantly more exercise types than Module 2 (9 vs 4). This allows for greater variety and supports more hybrid arc options.

### Target Distribution

| Type | Count | Rationale |
|------|:-----:|-----------|
| write_code | 5 | Core practice for list operations |
| complete_function | 2 | Guided implementation of list functions |
| code_tracing | 3 | Track list state through modifications |
| match_output | 2 | Quick pattern recognition for list access |
| simplify_code | 1 | Refactor verbose list operations |
| which_is_better | 1 | Compare list approaches |
| spot_difference | 1 | Catch subtle indexing/slicing bugs |
| decode_error | 1 | Interpret IndexError messages |
| bug_hunt | 2 | Find common list bugs |
| **hybrid** | 5 | Multi-part narrative exercises (25% of total) |
| **TOTAL** | **23** | |

### Hybrid Ratio Calculation

- Total exercises: 23
- Hybrid exercises: 5
- Ratio: **22%** (at lower end of 25-35% target, but reasonable given concept density)

---

## 3. Exercise Inventory

### Concept Progression

Exercises are organized into concept clusters, progressing from simple to complex.

| Cluster | Concepts | Difficulty |
|---------|----------|:----------:|
| A | List creation and literals | 1 |
| B | Positive indexing | 2 |
| C | Negative indexing, element modification | 2-3 |
| D | List methods (append, pop, insert, remove) | 3 |
| E | Slicing | 3-4 |
| F | Iteration over lists | 3 |
| G | Mutability and aliasing | 4 |
| H | Integration (lists + loops + conditionals) | 5 |

### Isolated Exercises

#### Cluster A: List Creation (Difficulty 1)

| # | Type | Concept Focus |
|---|------|---------------|
| 1 | write_code | Create lists with different element types |
| 2 | match_output | Predict output of list creation and printing |

#### Cluster B: Positive Indexing (Difficulty 2)

| # | Type | Concept Focus |
|---|------|---------------|
| 3 | match_output | Match list access expressions to output |
| 4 | write_code | Access and use list elements by index |
| 5 | decode_error | Interpret IndexError for out-of-bounds access |

#### Cluster C: Negative Indexing and Modification (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 6 | code_tracing | Trace negative index access |
| 7 | write_code | Modify list elements by assignment |
| 8 | spot_difference | Find subtle indexing errors (off-by-one) |

#### Cluster D: List Methods (Difficulty 3)

| # | Type | Concept Focus |
|---|------|---------------|
| 9 | code_tracing | Trace list after append/pop/insert/remove |
| 10 | write_code | Use list methods to build and modify lists |
| 11 | bug_hunt | Find bugs in list method usage |

#### Cluster E: Slicing (Difficulty 3-4)

| # | Type | Concept Focus |
|---|------|---------------|
| 12 | code_tracing | Trace slicing operations |
| 13 | write_code | Extract sublists using slicing |
| 14 | complete_function | Complete function that uses slicing |

#### Cluster F: Iteration (Difficulty 3)

| # | Type | Concept Focus |
|---|------|---------------|
| 15 | write_code | Iterate over list elements with for loop |
| 16 | complete_function | Complete function that processes list items |

#### Cluster G: Mutability and Aliasing (Difficulty 4)

| # | Type | Concept Focus |
|---|------|---------------|
| 17 | which_is_better | Compare copy vs alias approaches |
| 18 | bug_hunt | Find aliasing bugs (unexpected mutations) |

### Hybrid Exercises

#### Hybrid 1: The Apprentice - List Foundations

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | match_output | Study how lists work |
| 2 | GUIDANCE | complete_function | Practice with scaffolding |
| 3 | GROWTH | write_code | Create list operations independently |

**Placement:** After Cluster B (positive indexing), as first integration
**Difficulty:** 2
**Arc:** Apprentice

#### Hybrid 2: The Mystery - The Vanishing Element

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | code_tracing | Observe unexpected list behavior |
| 2 | INVESTIGATION | code_tracing | Trace to find where element disappeared |
| 3 | IMPROVEMENT | bug_hunt | Fix the list modification bug |

**Placement:** After Cluster D (list methods)
**Difficulty:** 3
**Arc:** Mystery

#### Hybrid 3: The Inheritance - The Inventory System

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | code_tracing | Understand inherited list-based system |
| 2 | OWNERSHIP | write_code | Add new features to the system |
| 3 | INVESTIGATION | bug_hunt | Find and fix hidden edge cases |

**Placement:** After Cluster E (slicing)
**Difficulty:** 3-4
**Arc:** Inheritance

#### Hybrid 4: The Upgrade - Cleaner List Code

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | EVALUATION | which_is_better | Compare verbose vs elegant approaches |
| 2 | IMPROVEMENT | simplify_code | Refactor to use better list patterns |

**Placement:** After Cluster F (iteration)
**Difficulty:** 4
**Arc:** Upgrade (2-part variant)

#### Hybrid 5: The Rivalry - List Master Challenge

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | bug_hunt | Analyze failed list code |
| 2 | GROWTH | write_code | Build improved list operations |
| 3 | CONFRONTATION | write_code | Create a complete list-based system |

**Placement:** End of module, as capstone
**Difficulty:** 5
**Arc:** Rivalry

---

## 4. Difficulty Progression Map

```
Difficulty:  1 -----> 2 -----> 3 -----> 4 -----> 5
             |       |        |        |        |
Exercises:   1,2     3,4,5    9,10,11  17,18    H5
                     H1       6,7,8    H4
                              12,13,14
                              15,16
                              H2,H3
```

H1-H5 = Hybrid exercises

---

## 5. File Structure

```
exercises/
└── module_3_lists/
    ├── write_code/
    │   ├── exercise_1_list_creation.py
    │   ├── exercise_2_indexing_access.py
    │   ├── exercise_3_modify_elements.py
    │   ├── exercise_4_list_methods.py
    │   └── exercise_5_iteration.py
    ├── complete_function/
    │   ├── exercise_1_slicing_function.py
    │   └── exercise_2_list_processing.py
    ├── code_tracing/
    │   ├── exercise_1_negative_indexing.py
    │   ├── exercise_2_list_methods_trace.py
    │   └── exercise_3_slicing_trace.py
    ├── match_output/
    │   ├── exercise_1_list_basics.py
    │   └── exercise_2_indexing_patterns.py
    ├── simplify_code/
    │   └── exercise_1_list_operations.py
    ├── which_is_better/
    │   └── exercise_1_copy_vs_alias.py
    ├── spot_difference/
    │   └── exercise_1_indexing_errors.py
    ├── decode_error/
    │   └── exercise_1_index_errors.py
    ├── bug_hunt/
    │   ├── exercise_1_method_bugs.py
    │   └── exercise_2_aliasing_bugs.py
    └── hybrid/
        ├── exercise_1_apprentice_foundations.py
        ├── exercise_2_mystery_vanishing.py
        ├── exercise_3_inheritance_inventory.py
        ├── exercise_4_upgrade_cleaner.py
        └── exercise_5_rivalry_master.py
```

---

## 6. Implementation Phases

Implementation is organized into 8 phases following the concept progression.

**After completing each phase:** Mark it with a checkmark below the phase header.

### Phase 1: List Creation (Cluster A)

**Exercises:** 1, 2
**Difficulty:** 1
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| 1 | write_code | `write_code/exercise_1_list_creation.py` |
| 2 | match_output | `match_output/exercise_1_list_basics.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| write_code | [templates/exercise_types/write_code.py](../../templates/exercise_types/write_code.py) |
| match_output | [templates/exercise_types/match_output.py](../../templates/exercise_types/match_output.py) |

---

### Phase 2: Positive Indexing + Hybrid 1 (Cluster B)

**Exercises:** 3, 4, 5, Hybrid 1
**Difficulty:** 2
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 3 | match_output | `match_output/exercise_2_indexing_patterns.py` |
| 4 | write_code | `write_code/exercise_2_indexing_access.py` |
| 5 | decode_error | `decode_error/exercise_1_index_errors.py` |
| H1 | hybrid (apprentice) | `hybrid/exercise_1_apprentice_foundations.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| decode_error | [templates/exercise_types/decode_error.py](../../templates/exercise_types/decode_error.py) |
| complete_function | [templates/exercise_types/complete_function.py](../../templates/exercise_types/complete_function.py) |
| hybrid_arcs README | [templates/hybrid_arcs/README.md](../../templates/hybrid_arcs/README.md) |
| apprentice arc | [templates/hybrid_arcs/apprentice.md](../../templates/hybrid_arcs/apprentice.md) |

---

### Phase 3: Negative Indexing and Modification (Cluster C)

**Exercises:** 6, 7, 8
**Difficulty:** 2-3
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 6 | code_tracing | `code_tracing/exercise_1_negative_indexing.py` |
| 7 | write_code | `write_code/exercise_3_modify_elements.py` |
| 8 | spot_difference | `spot_difference/exercise_1_indexing_errors.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| code_tracing | [templates/exercise_types/code_tracing.py](../../templates/exercise_types/code_tracing.py) |
| spot_difference | [templates/exercise_types/spot_difference.py](../../templates/exercise_types/spot_difference.py) |

---

### Phase 4: List Methods + Hybrid 2 (Cluster D)

**Exercises:** 9, 10, 11, Hybrid 2
**Difficulty:** 3
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 9 | code_tracing | `code_tracing/exercise_2_list_methods_trace.py` |
| 10 | write_code | `write_code/exercise_4_list_methods.py` |
| 11 | bug_hunt | `bug_hunt/exercise_1_method_bugs.py` |
| H2 | hybrid (mystery) | `hybrid/exercise_2_mystery_vanishing.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| bug_hunt | [templates/exercise_types/bug_hunt.py](../../templates/exercise_types/bug_hunt.py) |
| mystery arc | [templates/hybrid_arcs/mystery.md](../../templates/hybrid_arcs/mystery.md) |

---

### Phase 5: Slicing + Hybrid 3 (Cluster E)

**Exercises:** 12, 13, 14, Hybrid 3
**Difficulty:** 3-4
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 12 | code_tracing | `code_tracing/exercise_3_slicing_trace.py` |
| 13 | write_code | `write_code/exercise_5_slicing.py` |
| 14 | complete_function | `complete_function/exercise_1_slicing_function.py` |
| H3 | hybrid (inheritance) | `hybrid/exercise_3_inheritance_inventory.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| inheritance arc | [templates/hybrid_arcs/inheritance.md](../../templates/hybrid_arcs/inheritance.md) |

---

### Phase 6: Iteration + Hybrid 4 (Cluster F)

**Exercises:** 15, 16, Hybrid 4
**Difficulty:** 3-4
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 15 | write_code | `write_code/exercise_5_iteration.py` |
| 16 | complete_function | `complete_function/exercise_2_list_processing.py` |
| H4 | hybrid (upgrade) | `hybrid/exercise_4_upgrade_cleaner.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| simplify_code | [templates/exercise_types/simplify_code.py](../../templates/exercise_types/simplify_code.py) |
| which_is_better | [templates/exercise_types/which_is_better.py](../../templates/exercise_types/which_is_better.py) |
| upgrade arc | [templates/hybrid_arcs/upgrade.md](../../templates/hybrid_arcs/upgrade.md) |

---

### Phase 7: Mutability and Aliasing (Cluster G)

**Exercises:** 17, 18
**Difficulty:** 4
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| 17 | which_is_better | `which_is_better/exercise_1_copy_vs_alias.py` |
| 18 | bug_hunt | `bug_hunt/exercise_2_aliasing_bugs.py` |

**Read Before This Phase:**

*(All templates already read in previous phases)*

---

### Phase 8: Integration + Hybrid 5 (Cluster H)

**Exercises:** Hybrid 5
**Difficulty:** 5
**Estimated Files:** 1

| # | Type | File |
|---|------|------|
| H5 | hybrid (rivalry) | `hybrid/exercise_5_rivalry_master.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| rivalry arc | [templates/hybrid_arcs/rivalry.md](../../templates/hybrid_arcs/rivalry.md) |

---

### Phase Summary

| Phase | Cluster | Exercises | Files | New Templates |
|:-----:|---------|-----------|:-----:|---------------|
| 1 | List Creation | 1-2 | 2 | write_code, match_output |
| 2 | Indexing + H1 | 3-5, H1 | 4 | decode_error, complete_function, apprentice arc |
| 3 | Negative/Modify | 6-8 | 3 | code_tracing, spot_difference |
| 4 | Methods + H2 | 9-11, H2 | 4 | bug_hunt, mystery arc |
| 5 | Slicing + H3 | 12-14, H3 | 4 | inheritance arc |
| 6 | Iteration + H4 | 15-16, H4 | 3 | simplify_code, which_is_better, upgrade arc |
| 7 | Mutability | 17-18 | 2 | *(none)* |
| 8 | Integration + H5 | H5 | 1 | rivalry arc |
| **Total** | | **23** | **23** | |

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every exercise contains at least one `{{placeholder}}`
- [ ] NO concepts from later modules used (no functions/while/dicts/try-except)
- [ ] All 9 learning objectives covered
- [ ] Progressive difficulty (1 to 5)
- [ ] Hybrid ratio within 20-35%

### Format Requirements

- [ ] All functions use `pass` placeholder
- [ ] Instructions use `# YOUR CODE HERE` marker
- [ ] Each file has `main()` that calls all exercises
- [ ] PEP 8 compliant
- [ ] Follows templates from `templates/exercise_types/`

### Curriculum Compliance

| Concept | Used In |
|---------|---------|
| list creation | Exercises 1, 2, H1 |
| positive indexing | Exercises 3, 4, 5, H1 |
| negative indexing | Exercise 6 |
| element modification | Exercises 7, 8 |
| list methods | Exercises 9, 10, 11, H2 |
| slicing | Exercises 12, 13, 14, H3 |
| iteration | Exercises 15, 16, H4 |
| mutability/aliasing | Exercises 17, 18 |
| integration | H5 |

---

## 8. Implementation Notes

### Key Constraints

1. **No functions defined by student** - Students use lists but cannot define functions (comes in Module 4)
2. **No while loops** - Only for loops available
3. **No try/except** - Cannot catch IndexError
4. **No random** - Cannot randomly select from lists
5. **No list comprehensions** - Typically taught with functions

### Pedagogical Considerations

**Why lists are challenging:**
- Zero-based indexing is counterintuitive ("first item is index 0")
- Slicing boundaries (start inclusive, stop exclusive)
- Mutability surprises (list changes in place)
- Aliasing confusion (two variables, same list)
- Off-by-one errors in loops over lists

**Building mental models:**
- Start with simple list literals
- Progress to single-element access
- Then modification and methods
- Slicing as "extracting a piece"
- Iteration as "visiting each item"
- Aliasing as "two names for one thing"

**Tracing emphasis:**
- code_tracing exercises are critical for lists
- Students must track list state after each operation
- Visualize memory (box diagrams)
- Show before/after for mutations

### Common Bugs to Include in bug_hunt

1. **Off-by-one indexing:** `list[len(list)]` instead of `list[len(list)-1]`
2. **Modifying while iterating:** Removing items during for loop causes skips
3. **Aliasing confusion:** `b = a` creates alias, not copy
4. **Wrong method:** Using `remove(index)` instead of `pop(index)`
5. **Slice boundary confusion:** `list[1:3]` gets items 1 and 2, not 1, 2, 3
6. **Forgetting mutability:** Expecting original list unchanged after passing to function
7. **Empty list access:** Accessing `list[0]` on empty list

### List Operations to Cover

| Operation | Category | Exercise Coverage |
|-----------|----------|-------------------|
| `[1, 2, 3]` | Creation | Phase 1 |
| `list[0]` | Access | Phase 2 |
| `list[-1]` | Negative index | Phase 3 |
| `list[0] = x` | Modification | Phase 3 |
| `list.append(x)` | Add to end | Phase 4 |
| `list.pop()` | Remove from end | Phase 4 |
| `list.insert(i, x)` | Insert at position | Phase 4 |
| `list.remove(x)` | Remove by value | Phase 4 |
| `list[1:3]` | Slicing | Phase 5 |
| `list[::2]` | Step slicing | Phase 5 |
| `for item in list:` | Iteration | Phase 6 |
| `len(list)` | Length | Throughout |
| `x in list` | Membership | Throughout |
| `list1 + list2` | Concatenation | Phase 1-2 |
| `list * 3` | Repetition | Phase 1-2 |

### Placeholder Usage Ideas

- `{{hero}}` managing inventory of `{{item}}`s
- `{{school}}` roster of students in `{{house}}`
- `{{group}}` membership list
- `{{creature}}` collection
- `{{spell1}}`, `{{spell2}}` in a spellbook list
- `{{location}}` as list of places to visit
- `{{friend}}` and `{{heroine}}` names in a party list

### Arc Selection Rationale

| Arc | Why Selected |
|-----|--------------|
| **Apprentice** | Perfect for early list learning - observe, practice with guidance, create |
| **Mystery** | Great for list mutations - "where did the element go?" |
| **Inheritance** | Take over existing list-based system - common real-world scenario |
| **Upgrade** | Refactor verbose list code - teaches elegant patterns |
| **Rivalry** | Capstone challenge - defeat bugs then build mastery |

### Arcs NOT Used (and why)

| Arc | Why Not |
|-----|---------|
| Rescue | Requires decode_error + simplify_code + add_error_handling (no add_error_handling available) |
| Competition | Similar to Upgrade; chose Upgrade for the simplify_code integration |

---

## 9. Concept-Specific Teaching Notes

### List Creation (Cluster A)

- Start with simple literals: `[1, 2, 3]`
- Show mixed types: `["name", 42, True]`
- Empty list: `[]`
- Emphasize square brackets (not parentheses)

### Positive Indexing (Cluster B)

- Index 0 is the first element
- Think of index as "offset from start"
- `len(list)` returns count, but last index is `len(list) - 1`
- IndexError when accessing beyond list

### Negative Indexing (Cluster C)

- `-1` is the last element
- Think of negative as "from the end"
- `-1` is more readable than `list[len(list)-1]`
- Works with slicing too

### List Methods (Cluster D)

- `append(x)` - add to end, no return value
- `pop()` - remove and return last item
- `pop(i)` - remove and return item at index i
- `insert(i, x)` - insert x at position i
- `remove(x)` - remove first occurrence of value x

**Common confusion:** `remove()` takes a value, `pop()` takes an index

### Slicing (Cluster E)

- `list[start:stop]` - items from start up to (but not including) stop
- `list[:3]` - first 3 items (indices 0, 1, 2)
- `list[3:]` - from index 3 to end
- `list[::2]` - every other item (step 2)
- `list[::-1]` - reversed copy

**Key insight:** Slicing creates a NEW list (copy)

### Iteration (Cluster F)

- `for item in list:` - visit each element
- `for i in range(len(list)):` - iterate by index
- Can combine with conditionals: `if item > 5:`
- Building new lists from loops

### Mutability and Aliasing (Cluster G)

- Lists are mutable (can change in place)
- `b = a` creates an alias (same list, two names)
- Changes through `b` affect `a` too
- To copy: `b = a.copy()` or `b = a[:]`
- Most surprising concept for beginners

---
