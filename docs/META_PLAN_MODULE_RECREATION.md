# Meta-Plan: Module Recreation Strategy

Systematic approach for recreating all exercise modules using the universal template system. We plan these modules first, one by one, and save the plan to docs/plans dir.

---

## Goals

- 100% theme-agnostic content (no hardcoded theme references)
- Diverse exercise types per module (not just write_code)
- Proper narrative structure (exercise-level + task-level templates)
- Progressive difficulty within each module
- Curriculum-appropriate concepts (strict progression)
- Hybrid exercises combining multiple types with narrative arcs
- NO EXAMPLES IN THE PLANS. We don't want to constrain the implementor, we have templates for this.

---

## Progress Tracking

| Order | Module | Planned | Implemented | Validated | Status |
|:-----:|--------|:-------:|:-----------:|:---------:|--------|
| 1 | module_0_basics | 20 | 20 | Yes | **Complete** |
| 2 | module_1_turtle_loops | 18 | 18 | No | **Implemented** |
| 3 | module_2_decisions | 19 | 19 | No | **Implemented** |
| 4 | module_3_lists | 23 | 24 | No | **Implemented** |
| 5 | module_4_functions | 22 | 0 | No | **Planned** |
| 6 | module_5_games | 18 | 0 | No | **Planned** |
| 7 | module_6_final_project | 4 | 4 | No | **Implemented** |
| 8 | module_7_dicts | - | 0 | No | Pending |
| 9 | module_8_modules | - | 0 | No | Pending |
| 10 | module_9_oop | - | 0 | No | Pending |
| 11 | module_10_mega_project | - | 0 | No | Pending |

### Plan Links

| Module | Plan Document |
|--------|---------------|
| module_0_basics | [PLAN_MODULE_0_BASICS.md](plans/PLAN_MODULE_0_BASICS.md) |
| module_1_turtle_loops | [PLAN_MODULE_1_TURTLE_LOOPS.md](plans/PLAN_MODULE_1_TURTLE_LOOPS.md) |
| module_2_decisions | [PLAN_MODULE_2_DECISIONS.md](plans/PLAN_MODULE_2_DECISIONS.md) |
| module_3_lists | [PLAN_MODULE_3_LISTS.md](plans/PLAN_MODULE_3_LISTS.md) |
| module_4_functions | [PLAN_MODULE_4_FUNCTIONS.md](plans/PLAN_MODULE_4_FUNCTIONS.md) |
| module_5_games | [PLAN_MODULE_5_GAMES.md](plans/PLAN_MODULE_5_GAMES.md) |
| module_6_final_project | [PLAN_MODULE_6_FINAL_PROJECT.md](plans/PLAN_MODULE_6_FINAL_PROJECT.md) |

---

## Curriculum Progression

**CRITICAL:** Each module can ONLY use concepts from that module or earlier.

| Module | New Concepts | Cumulative |
|--------|--------------|------------|
| **0_basics** | print, variables, strings, numbers, input, f-strings, math | basics only |
| **1_turtle** | for loops, range(), turtle | + loops |
| **2_decisions** | if/elif/else, comparisons, and/or/not | + conditionals |
| **3_lists** | lists, indexing, slicing, list methods | + lists |
| **4_functions** | def, parameters, return, scope | + functions |
| **5_games** | while loops, random, game loops | + while/random |
| **6_mid_project** | Integration of modules 0-5 | checkpoint |
| **7_dicts** | dictionaries, keys/values, .get(), nested | + dicts |
| **8_modules** | import, standard library | + stdlib |
| **9_oop** | classes, __init__, methods, inheritance | + OOP |
| **10_mega_project** | Full integration | capstone |

---

## Hybrid Exercises

Multi-part exercises that combine 2-4 exercise types with a narrative arc.

### Why Hybrids?

| Isolated | Hybrid |
|----------|--------|
| "Fix this bug" | "Build a system, encounter bugs, fix them" |
| Tests one skill | Tests skill integration |
| 5-10 minutes | 20-45 minutes |

### Hybrid Ratio by Module

| Module | Hybrid Ratio | Rationale |
|--------|:------------:|-----------|
| 0-1 | 10-20% | First exposure, need focused practice |
| 2-3 | 25-35% | Branching logic benefits from integration |
| 4-5 | 45-55% | Functions/games enable larger projects |
| 6, 10 | 100% | Integration checkpoints |
| 7-9 | 60-70% | Complex data needs real context |

### Common Hybrid Patterns

**Read -> Build -> Debug** (early modules)
- Part 1: Predict output / trace execution
- Part 2: Add a new feature
- Part 3: Find and fix bugs

**Spec -> Implement -> Compare** (with functions)
- Part 1: Implement from signatures
- Part 2: Use functions to build feature
- Part 3: Compare design approaches
- Part 4: Create your own

**Design -> Build -> Test -> Ship** (advanced)
- Part 1: Analyze requirements
- Part 2: Implement the system
- Part 3: Debug failing tests
- Part 4: Refactor for quality

---

## Plan Template

Each module plan should include:

### 1. Overview
- Module ID and topic
- Prerequisites
- Learning objectives
- Curriculum constraints (available/unavailable concepts)

### 2. Exercise Distribution
- Isolated exercises by type
- Hybrid exercises with type combinations
- Hybrid ratio calculation

### 3. Exercise Inventory
- Concept focus for each exercise
- Difficulty progression
- Narrative template selection

### 4. Quality Checklist
- At least one {{placeholder}} per file
- ONLY uses concepts available at this curriculum point
- Progressive difficulty
- Appropriate hybrid ratio

---

## Planning Process

1. **Gather Context**
   - Review `EXERCISE_TYPE_MODULE_MAPPING.md` for valid types
   - Check `TEMPLATE.md` for available placeholders
   - Confirm curriculum constraints from this document

2. **Design Isolated Exercises**
   - Map concepts to exercise types
   - Ensure all module concepts are covered
   - Order from simple to complex

3. **Design Hybrid Exercises**
   - Choose pattern appropriate for module level
   - Select meaningful type combinations
   - Design narrative arc

4. **Validate**
   - No concepts from later modules
   - All new concepts covered
   - Progressive difficulty clear
   - Target hybrid ratio met

---

## Deliverables

For each module:
1. Plan document: `docs/plans/PLAN_MODULE_N_TOPIC.md`
2. Exercise inventory with metadata
3. Curriculum compliance verification
4. Difficulty progression map

---

## References

| Document | Purpose |
|----------|---------|
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Format and style rules |
| [TEMPLATE.md](../TEMPLATE.md) | Placeholder reference |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types per module |
| [hybrid_arcs/README.md](../templates/hybrid_arcs/README.md) | Narrative arc definitions |
