# Plan: Module 7 - Dictionaries

Recreation plan for module_7_dicts using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_7_dicts |
| **Topic** | Dictionaries, keys/values, .get(), nested structures |
| **Prerequisites** | module_0_basics through module_5_games (including module_6_mid_project) |
| **Target Hybrid Ratio** | 60-70% |

### Learning Objectives

By the end of this module, students will be able to:

1. Create and initialize dictionaries with key-value pairs
2. Access values using bracket notation and `.get()` method
3. Add, modify, and delete dictionary entries
4. Use dictionary methods (`.keys()`, `.values()`, `.items()`)
5. Iterate over dictionaries with for loops
6. Recognize when to use dictionaries vs lists
7. Work with nested dictionaries
8. Apply dictionaries to real-world problems (counting, grouping, lookup tables)

### Curriculum Constraints

| Available Concepts | NOT Available (later modules) |
|--------------------|-------------------------------|
| **From Modules 0-5:** | |
| print(), variables, strings, numbers | classes, objects, methods on custom types |
| input(), type conversion, f-strings | file I/O |
| for loops, range() | try/except (for type errors) |
| if/elif/else, comparisons, boolean ops | imports beyond random |
| lists, indexing, slicing, list methods | |
| functions (def, parameters, return) | |
| while loops, break, continue | |
| import random | |
| **New in Module 7:** | |
| dict literals `{key: value}` | |
| dict() constructor | |
| Bracket access `d[key]` | |
| `.get(key)` and `.get(key, default)` | |
| `.keys()`, `.values()`, `.items()` | |
| `in` operator with dicts | |
| Nested dictionaries | |
| Dict comprehensions (introduce late) | |

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types for Module 7 |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Exercise format standards |
| [common-struggles.md](../../references/pedagogy/common-struggles.md) | Dict mental models |

---

## 2. Exercise Distribution

### Available Exercise Types (7 total)

| Category | Types |
|----------|-------|
| **Core** | write_code, complete_function, blank_page |
| **Reading** | code_tracing |
| **Improvement** | simplify_code |
| **Analysis** | which_is_better |
| **Debugging** | decode_error |

**Note:** Unlike module 5 (games) which had only 3 types, module 7 has 7 diverse types enabling richer hybrid combinations. Notably, `bug_hunt` is NOT available for this module—debugging is handled through `decode_error` which focuses on understanding error messages.

### Target Distribution

| Type | Count | Rationale |
|------|:-----:|-----------|
| write_code | 3 | Core dict operations and patterns |
| complete_function | 2 | Guided dict function implementation |
| code_tracing | 2 | Track dict state through modifications |
| simplify_code | 1 | Replace verbose patterns with dict elegance |
| which_is_better | 1 | Dict vs list decision-making |
| decode_error | 2 | KeyError and TypeError understanding |
| blank_page | 1 | Independent dict project |
| **hybrid** | 8 | Multi-part dict projects (57% of total) |
| **TOTAL** | **20** | |

### Hybrid Ratio Calculation

- Total exercises: 20
- Hybrid exercises: 8
- Ratio: **57%** (slightly below 60% target, justified below)

**Rationale:** With 7 exercise types, we prioritize giving students exposure to each type in isolation before combining them in hybrids. The 12 isolated exercises ensure solid foundations with each type, while 8 substantial hybrids provide integration practice. Each hybrid is a multi-part project rather than a simple 2-part combination.

---

## 3. Exercise Inventory

### Concept Progression

Exercises are organized into concept clusters, progressing from simple to complex.

| Cluster | Concepts | Difficulty |
|---------|----------|:----------:|
| A | Basic dict creation and access | 1-2 |
| B | Dict modification and methods | 2-3 |
| C | Dict iteration patterns | 2-3 |
| D | Dict vs list decisions | 3 |
| E | Nested dictionaries | 3-4 |
| F | Real-world dict applications | 4-5 |

### Isolated Exercises

#### Cluster A: Basic Dict Creation and Access (Difficulty 1-2)

| # | Type | Concept Focus |
|---|------|---------------|
| 1 | write_code | Create dicts with literal syntax; access values by key |
| 2 | decode_error | Understand KeyError when accessing missing keys |
| 3 | code_tracing | Trace dict creation and basic access operations |

#### Cluster B: Dict Modification and Methods (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 4 | write_code | Add, update, and delete dict entries |
| 5 | complete_function | Complete functions using `.get()` with defaults |
| 6 | code_tracing | Trace dict mutations through a sequence of operations |

#### Cluster C: Dict Iteration (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 7 | write_code | Iterate with `.keys()`, `.values()`, `.items()` |
| 8 | complete_function | Complete a function that processes dict items |

#### Cluster D: Dict vs List (Difficulty 3)

| # | Type | Concept Focus |
|---|------|---------------|
| 9 | which_is_better | Compare dict lookup vs list search approaches |
| 10 | simplify_code | Replace if/elif chains with dict-based dispatch |

#### Cluster E: Nested Dictionaries (Difficulty 3-4)

| # | Type | Concept Focus |
|---|------|---------------|
| 11 | decode_error | Understand TypeError/KeyError in nested access |

#### Cluster F: Real-World Applications (Difficulty 4-5)

| # | Type | Concept Focus |
|---|------|---------------|
| 12 | blank_page | Build a complete dict-based system from docstring only |

### Hybrid Exercises

#### Hybrid 1: The Inheritance - The Spell Registry

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | code_tracing | Understand an inherited dict-based registry |
| 2 | OWNERSHIP | write_code | Add new entries and lookup functionality |
| 3 | INVESTIGATION | decode_error | Debug KeyError in the inherited code |

**Placement:** After Cluster A (basic access)
**Difficulty:** 2
**Arc:** Inheritance

#### Hybrid 2: The Rescue - The Broken Inventory

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | decode_error | Diagnose KeyError crashing the inventory |
| 2 | INVESTIGATION | code_tracing | Trace to find where keys go missing |
| 3 | IMPROVEMENT | simplify_code | Replace fragile code with `.get()` pattern |

**Placement:** After Cluster B (modification and methods)
**Difficulty:** 2-3
**Arc:** Rescue

#### Hybrid 3: The Competition - Lookup Showdown

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | EVALUATION | which_is_better | Compare list search vs dict lookup |
| 2 | GROWTH | write_code | Implement the superior dict-based approach |
| 3 | EVALUATION | which_is_better | Reflect on when each approach is best |

**Placement:** After Cluster D (dict vs list)
**Difficulty:** 3
**Arc:** Competition

#### Hybrid 4: The Upgrade - The Messy Counter

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | EVALUATION | which_is_better | Evaluate verbose counting code |
| 2 | DISCOVERY | code_tracing | Trace how the counter works |
| 3 | IMPROVEMENT | simplify_code | Refactor using dict patterns |

**Placement:** After Cluster C (iteration)
**Difficulty:** 3
**Arc:** Upgrade

#### Hybrid 5: The Inheritance - The Nested Config

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | code_tracing | Trace nested dict access patterns |
| 2 | OWNERSHIP | write_code | Add nested configuration options |
| 3 | INVESTIGATION | decode_error | Debug nested KeyError chains |

**Placement:** After Cluster E (nested dicts)
**Difficulty:** 3-4
**Arc:** Inheritance

#### Hybrid 6: The Rescue - The Crashed Leaderboard

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | decode_error | Diagnose why leaderboard crashes |
| 2 | INVESTIGATION | code_tracing | Trace the score update logic |
| 3 | IMPROVEMENT | write_code | Rebuild with robust dict patterns |
| 4 | GROWTH | complete_function | Add new leaderboard features |

**Placement:** Cluster F (real-world applications)
**Difficulty:** 4
**Arc:** Rescue (extended)

#### Hybrid 7: The Competition - Data Structure Duel

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | EVALUATION | which_is_better | Compare complex list vs dict structures |
| 2 | GROWTH | write_code | Build a dict-based solution |
| 3 | GROWTH | complete_function | Extend with advanced operations |
| 4 | EVALUATION | which_is_better | Final reflection on trade-offs |

**Placement:** Cluster F (real-world applications)
**Difficulty:** 4-5
**Arc:** Competition (extended)

#### Hybrid 8: Mini Project - Build Your Data System

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | code_tracing | Study a model data system |
| 2 | GROWTH | write_code | Design your dict structure |
| 3 | GROWTH | complete_function | Implement core operations |
| 4 | OWNERSHIP | blank_page | Add a feature of your own design |

**Placement:** End of module, as capstone
**Difficulty:** 5
**Arc:** Custom (Study -> Design -> Implement -> Create)

---

## 4. Difficulty Progression Map

```
Difficulty:  1 -----> 2 -----> 3 -----> 4 -----> 5
             |       |        |        |        |
Exercises:   1       2,3      4,5,6    11       12
                     H1       7,8      H5,H6    H7,H8
                              9,10
                              H2,H3,H4
```

H1-H8 = Hybrid exercises

---

## 5. File Structure

```
exercises/
└── module_7_dicts/
    ├── write_code/
    │   ├── exercise_1_dict_basics.py
    │   ├── exercise_2_dict_modification.py
    │   └── exercise_3_dict_iteration.py
    ├── complete_function/
    │   ├── exercise_1_get_with_default.py
    │   └── exercise_2_process_items.py
    ├── code_tracing/
    │   ├── exercise_1_basic_operations.py
    │   └── exercise_2_mutations.py
    ├── simplify_code/
    │   └── exercise_1_dict_dispatch.py
    ├── which_is_better/
    │   └── exercise_1_dict_vs_list.py
    ├── decode_error/
    │   ├── exercise_1_key_error.py
    │   └── exercise_2_nested_error.py
    ├── blank_page/
    │   └── exercise_1_dict_system.py
    └── hybrid/
        ├── exercise_1_inheritance_spell_registry.py
        ├── exercise_2_rescue_broken_inventory.py
        ├── exercise_3_competition_lookup_showdown.py
        ├── exercise_4_upgrade_messy_counter.py
        ├── exercise_5_inheritance_nested_config.py
        ├── exercise_6_rescue_crashed_leaderboard.py
        ├── exercise_7_competition_data_duel.py
        └── exercise_8_project_data_system.py
```

---

## 6. Implementation Phases

Implementation is organized into 6 phases following the concept progression.

**After completing each phase:** Mark it with a checkmark below the phase header.

### Phase 1: Basic Dict Creation and Access (Cluster A)

**Exercises:** 1, 2, 3, Hybrid 1
**Difficulty:** 1-2
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 1 | write_code | `write_code/exercise_1_dict_basics.py` |
| 2 | decode_error | `decode_error/exercise_1_key_error.py` |
| 3 | code_tracing | `code_tracing/exercise_1_basic_operations.py` |
| H1 | hybrid (inheritance) | `hybrid/exercise_1_inheritance_spell_registry.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| write_code | [templates/exercise_types/write_code.py](../../templates/exercise_types/write_code.py) |
| decode_error | [templates/exercise_types/decode_error.py](../../templates/exercise_types/decode_error.py) |
| code_tracing | [templates/exercise_types/code_tracing.py](../../templates/exercise_types/code_tracing.py) |
| inheritance arc | [templates/hybrid_arcs/README.md](../../templates/hybrid_arcs/README.md) |

---

### Phase 2: Dict Modification and Methods + Hybrid 2 (Cluster B)

**Exercises:** 4, 5, 6, Hybrid 2
**Difficulty:** 2-3
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 4 | write_code | `write_code/exercise_2_dict_modification.py` |
| 5 | complete_function | `complete_function/exercise_1_get_with_default.py` |
| 6 | code_tracing | `code_tracing/exercise_2_mutations.py` |
| H2 | hybrid (rescue) | `hybrid/exercise_2_rescue_broken_inventory.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| complete_function | [templates/exercise_types/complete_function.py](../../templates/exercise_types/complete_function.py) |
| simplify_code | [templates/exercise_types/simplify_code.py](../../templates/exercise_types/simplify_code.py) |
| rescue arc | [templates/hybrid_arcs/README.md](../../templates/hybrid_arcs/README.md) |

---

### Phase 3: Dict Iteration + Hybrids 3, 4 (Clusters C, D)

**Exercises:** 7, 8, 9, 10, Hybrid 3, Hybrid 4
**Difficulty:** 2-3
**Estimated Files:** 6

| # | Type | File |
|---|------|------|
| 7 | write_code | `write_code/exercise_3_dict_iteration.py` |
| 8 | complete_function | `complete_function/exercise_2_process_items.py` |
| 9 | which_is_better | `which_is_better/exercise_1_dict_vs_list.py` |
| 10 | simplify_code | `simplify_code/exercise_1_dict_dispatch.py` |
| H3 | hybrid (competition) | `hybrid/exercise_3_competition_lookup_showdown.py` |
| H4 | hybrid (upgrade) | `hybrid/exercise_4_upgrade_messy_counter.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| which_is_better | [templates/exercise_types/which_is_better.py](../../templates/exercise_types/which_is_better.py) |
| competition arc | [templates/hybrid_arcs/README.md](../../templates/hybrid_arcs/README.md) |
| upgrade arc | [templates/hybrid_arcs/README.md](../../templates/hybrid_arcs/README.md) |

---

### Phase 4: Nested Dictionaries + Hybrid 5 (Cluster E)

**Exercises:** 11, Hybrid 5
**Difficulty:** 3-4
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| 11 | decode_error | `decode_error/exercise_2_nested_error.py` |
| H5 | hybrid (inheritance) | `hybrid/exercise_5_inheritance_nested_config.py` |

**Read Before This Phase:**

*(All templates already read in previous phases)*

---

### Phase 5: Real-World Applications + Hybrids 6, 7 (Cluster F)

**Exercises:** Hybrid 6, Hybrid 7
**Difficulty:** 4-5
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| H6 | hybrid (rescue) | `hybrid/exercise_6_rescue_crashed_leaderboard.py` |
| H7 | hybrid (competition) | `hybrid/exercise_7_competition_data_duel.py` |

**Read Before This Phase:**

*(All templates already read in previous phases)*

---

### Phase 6: Capstone + Blank Page (Cluster F continued)

**Exercises:** 12, Hybrid 8
**Difficulty:** 5
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| 12 | blank_page | `blank_page/exercise_1_dict_system.py` |
| H8 | hybrid (project) | `hybrid/exercise_8_project_data_system.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| blank_page | [templates/exercise_types/blank_page.py](../../templates/exercise_types/blank_page.py) |

---

### Phase Summary

| Phase | Cluster | Exercises | Files | New Templates |
|:-----:|---------|-----------|:-----:|---------------|
| 1 | Basic Access | 1-3, H1 | 4 | write_code, decode_error, code_tracing, inheritance arc |
| 2 | Modification + H2 | 4-6, H2 | 4 | complete_function, simplify_code, rescue arc |
| 3 | Iteration + H3, H4 | 7-10, H3, H4 | 6 | which_is_better, competition arc, upgrade arc |
| 4 | Nested + H5 | 11, H5 | 2 | *(none)* |
| 5 | Applications + H6, H7 | H6, H7 | 2 | *(none)* |
| 6 | Capstone | 12, H8 | 2 | blank_page |
| **Total** | | **20** | **20** | |

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every exercise contains at least one `{{placeholder}}`
- [ ] NO concepts from later modules used (no classes/file I/O/try-except for type conversion)
- [ ] All 8 learning objectives covered
- [ ] Progressive difficulty (1 to 5)
- [ ] Hybrid exercises use available types only (no bug_hunt)

### Format Requirements

- [ ] All functions use `pass` placeholder
- [ ] Instructions use `# YOUR CODE HERE` marker
- [ ] Each file has `main()` that calls all exercises
- [ ] PEP 8 compliant
- [ ] Follows templates from `templates/exercise_types/`

### Curriculum Compliance

| Concept | Used In |
|---------|---------|
| dict literals | Exercises 1, 3, H1 |
| bracket access | Exercises 1, 2, 3, H1 |
| .get() method | Exercises 5, H2 |
| dict modification | Exercises 4, 6, H2 |
| .keys(), .values(), .items() | Exercises 7, 8, H4 |
| dict vs list | Exercises 9, 10, H3 |
| nested dicts | Exercises 11, H5 |
| real-world applications | Exercises 12, H6, H7, H8 |

---

## 8. Implementation Notes

### Key Constraints

1. **No try/except for KeyError** - Use `.get()` or `in` operator for safe access
2. **No classes** - Dicts are standalone data structures
3. **No file I/O** - Data is defined in code
4. **Students HAVE functions** - Can define and use helper functions
5. **Students HAVE while loops** - Can combine with dict operations for interactive programs

### Pedagogical Considerations

**Why dictionaries are challenging:**
- Key vs index conceptual shift (names vs positions)
- Mutable nature causes unexpected side effects
- KeyError is a new error type to understand
- Nested access chains can be confusing
- Knowing when dict vs list is appropriate

**Building mental models:**
- Dictionary = "lookup table" or "address book"
- Keys are unique identifiers (like names)
- Values are the data (like phone numbers)
- `.get()` = "safe lookup with fallback"
- `.items()` = "walk through all pairs"

**Common Dict Patterns to Teach:**
1. Counting/frequency: `counts[item] = counts.get(item, 0) + 1`
2. Grouping: `groups[key].append(item)` (with setdefault or defaultdict alternative)
3. Lookup table: Replace if/elif chains with dict
4. Configuration: Nested dicts for settings
5. Memoization: Cache function results (advanced)

### Common Errors for decode_error Exercises

1. **KeyError:** Accessing a key that doesn't exist
2. **TypeError:** Using unhashable type as key (list)
3. **TypeError:** Trying to index dict with integer like a list
4. **AttributeError:** Calling list methods on dict or vice versa
5. **Nested KeyError:** Missing intermediate key in chain

### Dict Patterns to Cover

| Pattern | Description | Exercise Coverage |
|---------|-------------|-------------------|
| Creation | `{key: value}` syntax | Phase 1 |
| Safe access | `.get(key, default)` | Phase 2 |
| Iteration | `.items()` for loops | Phase 3 |
| Counting | Frequency counting | Phase 3, H4 |
| Dispatch | Replace conditionals | Phase 3 |
| Nesting | Multi-level dicts | Phase 4 |
| CRUD | Create/Read/Update/Delete | Phase 2, H6 |

### Placeholder Usage Ideas

- `{{hero}}` stats dictionary (health, strength, magic)
- `{{creature}}` encyclopedia with attributes
- `{{item}}` inventory with quantities
- `{{spell1}}`, `{{spell2}}` in spell registry
- `{{location}}` with nested room data
- `{{school}}` student/grade records
- `{{mentor}}` and `{{hero}}` relationship scores
- `{{villain}}` weakness lookup table

### Arc Selection Rationale

| Arc | Count | Why Selected |
|-----|:-----:|--------------|
| **Inheritance** | 2 | Perfect for "inherited data structures" - understand then extend |
| **Rescue** | 2 | Debugging dict errors is crucial skill |
| **Competition** | 2 | Dict vs list comparison is key learning |
| **Upgrade** | 1 | Replace verbose code with dict elegance |
| **Project** | 1 | Capstone: design your own system |

### Arcs NOT Used (and why)

| Arc | Why Not |
|-----|---------|
| Rivalry | Requires bug_hunt (not available for module 7) |
| Mystery | Requires output_prediction (not available) |
| Apprentice | Requires fill_blanks (not available) |

---

## 9. Concept-Specific Teaching Notes

### Basic Dict Creation (Cluster A)

- Start with analogy: "phone book", "student roster"
- Keys must be unique (like IDs)
- Values can be anything (including other dicts!)
- Order is preserved in modern Python (3.7+)

### Safe Access with .get() (Cluster B)

- Bracket access crashes on missing key
- `.get()` returns None (or custom default)
- Pattern: `value = d.get(key, default_value)`
- Use case: counting, configuration fallbacks

### Dict Iteration (Cluster C)

- `.keys()` - iterate over keys only
- `.values()` - iterate over values only
- `.items()` - iterate over (key, value) pairs
- Pattern: `for key, value in d.items():`

### Dict vs List Decision (Cluster D)

| Use Dict When | Use List When |
|---------------|---------------|
| Need fast lookup by name | Need ordered sequence |
| Data has natural identifiers | Data is positional |
| Need O(1) access | Need to iterate in order |
| Heterogeneous attributes | Homogeneous collection |

### Nested Dictionaries (Cluster E)

- Think of it as "dict of dicts"
- Access: `d[outer_key][inner_key]`
- Safe nested access: check outer key first, or use `.get()` chains
- Use case: game characters, configuration files, JSON data

### Real-World Applications (Cluster F)

| Application | Dict Structure |
|-------------|----------------|
| Inventory | `{item_name: quantity}` |
| Leaderboard | `{player_name: score}` |
| Character stats | `{stat_name: value}` |
| Word frequency | `{word: count}` |
| Settings | `{category: {option: value}}` |
| Spell book | `{spell_name: {power: N, cost: M}}` |

---

## 10. Comparison with Module 5 (Games)

| Aspect | Module 5 (Games) | Module 7 (Dicts) |
|--------|------------------|------------------|
| Exercise types | 3 | 7 |
| Total exercises | 18 | 20 |
| Hybrid count | 6 | 8 |
| Hybrid ratio | 33% | 57% |
| Primary arcs | Rivalry, Rescue | Inheritance, Rescue, Competition, Upgrade |
| Key challenge | While loop control | Key-based access mental model |

The higher hybrid ratio for module 7 reflects that:
1. More exercise types enable richer combinations
2. Dict concepts benefit from integrated, real-world contexts
3. Students are more experienced at this point in curriculum
