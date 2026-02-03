# Plan: Module 6 - Final Project

Recreation plan for module_6_final_project using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_6_final_project |
| **Topic** | Integration checkpoint - combining all concepts from modules 0-5 |
| **Prerequisites** | module_0_basics through module_5_games |
| **Target Hybrid Ratio** | 100% (integration checkpoint) |

### Learning Objectives

By the end of this module, students will be able to:

1. Combine multiple programming concepts (variables, loops, conditionals, lists, functions, while loops) in a single project
2. Design and implement a complete program from requirements
3. Structure code using functions for organization and reuse
4. Handle user input with validation loops
5. Use randomness for dynamic behavior
6. Demonstrate mastery of all concepts learned so far

### Curriculum Constraints

| Available Concepts | NOT Available (later modules) |
|--------------------|-------------------------------|
| **From Module 0:** | |
| print(), variables, strings, numbers | dictionaries |
| input(), type conversion, f-strings | classes, methods |
| math: +, -, *, /, //, %, ** | file I/O |
| **From Module 1:** | try/except (for type errors) |
| for loops, range() | import (except turtle, random) |
| turtle graphics | |
| **From Module 2:** | |
| if/elif/else, comparisons | |
| and, or, not | |
| **From Module 3:** | |
| lists, indexing, slicing | |
| list methods | |
| len(), in operator | |
| **From Module 4:** | |
| while loops, break, continue | |
| random module | |
| **From Module 5:** | |
| def, parameters, return | |
| default parameters | |
| local scope | |

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types for Module 6 |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Exercise format standards |

---

## 2. Exercise Distribution

### Available Exercise Types (3 total)

| Category | Types |
|----------|-------|
| **Core** | write_code, mini_project, blank_page |

**Note:** Module 6 has limited exercise types by design. As an integration checkpoint, the focus is on substantial projects that combine all prior concepts, not on introducing new exercise formats.

### Target Distribution

| Type | Count | Rationale |
|------|:-----:|-----------|
| **hybrid (mini_project)** | 4 | Multi-part integration projects |
| **TOTAL** | **4** | |

### Hybrid Ratio Calculation

- Total exercises: 4
- Hybrid exercises: 4
- Ratio: **100%** (matches integration checkpoint target)

**Rationale:** This is a checkpoint module. Every exercise is a substantial multi-part project that requires students to integrate concepts from all previous modules. Quality over quantity.

---

## 3. Exercise Inventory

### Project Themes

Each project focuses on a different combination of concepts while requiring integration of all skills.

| Project | Primary Focus | Key Concepts Combined |
|---------|---------------|----------------------|
| 1 | Character/Profile System | lists, functions, loops, input |
| 2 | Interactive Quiz Game | while loops, random, functions, lists |
| 3 | Collection Manager | lists, functions, input validation, menus |
| 4 | Adventure Game | while loops, conditionals, functions, lists, random |

### Hybrid Exercises

#### Hybrid 1: Character Profile System

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | write_code | Design data structure for characters |
| 2 | GROWTH | write_code | Build functions to create and display profiles |
| 3 | GROWTH | write_code | Add functions to modify character stats |
| 4 | OWNERSHIP | write_code | Create a menu-driven interface |

**Difficulty:** 3-4
**Arc:** Custom (Design -> Build -> Extend -> Polish)
**Concepts integrated:** lists, functions, for loops, conditionals, input, f-strings

#### Hybrid 2: Quiz Game

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Build question/answer data structures |
| 2 | GROWTH | write_code | Create functions to ask questions and check answers |
| 3 | GROWTH | write_code | Add scoring and feedback |
| 4 | OWNERSHIP | write_code | Add random question order and play-again loop |

**Difficulty:** 3-4
**Arc:** Custom (Build -> Enhance -> Polish -> Extend)
**Concepts integrated:** lists, functions, while loops, random, conditionals, input

#### Hybrid 3: Collection Manager

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | blank_page | Design core functions from docstrings |
| 2 | GROWTH | write_code | Implement add/remove/list operations |
| 3 | GROWTH | write_code | Add search and filter functions |
| 4 | OWNERSHIP | write_code | Build complete menu interface with validation |

**Difficulty:** 4
**Arc:** Custom (Design -> Build -> Extend -> Integrate)
**Concepts integrated:** lists, functions, while loops, conditionals, input validation

#### Hybrid 4: Text Adventure

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | blank_page | Design game functions from specifications |
| 2 | GROWTH | write_code | Implement core game mechanics |
| 3 | GROWTH | write_code | Add inventory and status tracking |
| 4 | OWNERSHIP | write_code | Complete the adventure with multiple paths |

**Difficulty:** 5
**Arc:** Custom (Design -> Build -> Extend -> Complete)
**Concepts integrated:** ALL concepts from modules 0-5

---

## 4. Difficulty Progression Map

```
Difficulty:  3 -----> 4 -----> 5
             |        |        |
Projects:    H1       H3       H4
             H2
```

H1-H4 = Hybrid projects

---

## 5. File Structure

```
exercises/
└── module_6_final_project/
    └── hybrid/
        ├── exercise_1_character_system.py
        ├── exercise_2_quiz_game.py
        ├── exercise_3_collection_manager.py
        └── exercise_4_text_adventure.py
```

---

## 6. Implementation Phases

Implementation is organized into 2 phases.

### Phase 1: Foundation Projects (H1, H2)

**Exercises:** Hybrid 1, Hybrid 2
**Difficulty:** 3-4
**Files:** 2

| # | Type | File |
|---|------|------|
| H1 | hybrid (mini_project) | `hybrid/exercise_1_character_system.py` |
| H2 | hybrid (mini_project) | `hybrid/exercise_2_quiz_game.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| write_code | [templates/exercise_types/write_code.py](../../templates/exercise_types/write_code.py) |
| blank_page | [templates/exercise_types/blank_page.py](../../templates/exercise_types/blank_page.py) |
| hybrid_arcs README | [templates/hybrid_arcs/README.md](../../templates/hybrid_arcs/README.md) |

---

### Phase 2: Advanced Projects (H3, H4)

**Exercises:** Hybrid 3, Hybrid 4
**Difficulty:** 4-5
**Files:** 2

| # | Type | File |
|---|------|------|
| H3 | hybrid (mini_project) | `hybrid/exercise_3_collection_manager.py` |
| H4 | hybrid (mini_project) | `hybrid/exercise_4_text_adventure.py` |

---

### Phase Summary

| Phase | Projects | Files | Difficulty |
|:-----:|----------|:-----:|:----------:|
| 1 | H1, H2 | 2 | 3-4 |
| 2 | H3, H4 | 2 | 4-5 |
| **Total** | **4** | **4** | |

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every exercise contains at least one `{{placeholder}}`
- [ ] NO concepts from later modules used (no dicts/classes/try-except/file I/O)
- [ ] All 6 learning objectives covered
- [ ] Progressive difficulty (3 to 5)
- [ ] 100% hybrid ratio achieved

### Format Requirements

- [ ] All functions use `pass` placeholder
- [ ] Instructions use `# YOUR CODE HERE` marker
- [ ] Each file has `main()` that calls all exercises
- [ ] PEP 8 compliant
- [ ] Follows templates from `templates/exercise_types/`

### Curriculum Compliance

| Concept | Used In |
|---------|---------|
| variables, print, f-strings | All projects |
| for loops | H1, H2, H3 |
| while loops | H2, H3, H4 |
| if/elif/else | All projects |
| lists | All projects |
| functions | All projects |
| random | H2, H4 |
| input validation | H3, H4 |

---

## 8. Implementation Notes

### Key Constraints

1. **No dictionaries** - Use lists of lists or parallel lists
2. **No try/except** - Use while loops with string validation
3. **No classes** - Structure with functions only
4. **No file I/O** - All data is temporary within session

### Pedagogical Considerations

**Why a final project module:**
- Students need to see how concepts work together
- Integration is harder than isolated practice
- Real programs combine many concepts
- Builds confidence before moving to advanced topics

**Project design principles:**
- Start with clear requirements
- Build incrementally (each part adds value)
- Functions should have single responsibilities
- User experience matters (clear prompts, feedback)

### Placeholder Usage Ideas

- `{{hero}}`, `{{heroine}}` as character names in profile system
- `{{school}}` quiz questions about the themed world
- `{{item}}`, `{{creature}}` for collection manager items
- `{{location}}`, `{{spell1}}` for text adventure
- `{{villain}}` as antagonist in adventure game
- `{{exclamation}}` for success/failure messages

### Project Complexity Guidelines

| Project | Lines of Code (estimated) | Functions (estimated) |
|---------|:-------------------------:|:---------------------:|
| H1 Character System | 80-120 | 5-7 |
| H2 Quiz Game | 100-150 | 6-8 |
| H3 Collection Manager | 120-180 | 8-10 |
| H4 Text Adventure | 150-250 | 10-15 |

### Integration Points to Emphasize

Each project should clearly demonstrate:
1. **Data storage:** Using lists appropriately
2. **Modularity:** Breaking code into functions
3. **User interaction:** Input with validation
4. **Control flow:** Loops and conditionals working together
5. **Code reuse:** Calling functions from other functions

---
