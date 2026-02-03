# Plan: Module 8 - Modules and Standard Library

Recreation plan for module_8_modules using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_8_modules |
| **Topic** | Python imports, standard library, creating modules |
| **Prerequisites** | module_0_basics through module_7_dicts |
| **Target Hybrid Ratio** | 60-70% |

### Learning Objectives

By the end of this module, students will be able to:

1. Use different import syntax variations (`import X`, `from X import Y`, `import X as Y`)
2. Avoid naming conflicts by understanding namespaces
3. Use the `math` module for mathematical operations
4. Work with `datetime` for dates and times
5. Extend `random` usage beyond basic games
6. Use `string` module constants
7. Handle import-related errors gracefully
8. Create and import custom modules
9. Understand the `__name__ == "__main__"` pattern
10. Read documentation to learn new modules

### Curriculum Constraints

| Available Concepts | NOT Available (later modules) |
|--------------------|-------------------------------|
| **From Modules 0-7:** | |
| print(), variables, strings, numbers | classes, objects, custom methods |
| input(), type conversion, f-strings | file I/O (open/read/write) |
| for loops, range(), turtle | third-party packages (pip) |
| if/elif/else, comparisons, boolean ops | async/await |
| lists, indexing, slicing, list methods | decorators |
| functions (def, parameters, return) | generators |
| while loops, break, continue | context managers (with) |
| import random (basic) | |
| dictionaries, .get(), nested dicts | |
| **New in Module 8:** | |
| `import module` | |
| `from module import name` | |
| `from module import name as alias` | |
| `import module as alias` | |
| Standard library: math, datetime, string | |
| Extended random: choice, shuffle, sample | |
| Creating .py modules | |
| `__name__ == "__main__"` | |
| ModuleNotFoundError, ImportError | |

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types for Module 8 |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Exercise format standards |

---

## 2. Exercise Distribution

### Available Exercise Types (2 total)

| Category | Types |
|----------|-------|
| **Core** | write_code |
| **Improvement** | add_error_handling |

**Critical constraint:** Module 8 has only 2 available exercise types. This limits hybrid diversity significantly. We compensate by:

1. Creating multi-part write_code exercises with progressive complexity
2. Using add_error_handling to teach defensive import practices
3. Designing longer narrative arcs within the write_code type
4. Including "study and extend" patterns within write_code

### Target Distribution

| Type | Count | Rationale |
|------|:-----:|-----------|
| write_code | 6 | Core stdlib exploration and module creation |
| add_error_handling | 3 | Import safety and defensive programming |
| **hybrid** | 9 | Multi-part projects (60% of total) |
| **TOTAL** | **18** | |

### Hybrid Ratio Calculation

- Total exercises: 18
- Hybrid exercises: 9
- Ratio: **60%** (meets 60-70% target)

**Note:** With only 2 exercise types, hybrids combine write_code and add_error_handling in various sequences, or use multi-part write_code with progressive complexity.

---

## 3. Exercise Inventory

### Concept Progression

Exercises are organized into concept clusters, progressing from simple to complex.

| Cluster | Concepts | Difficulty |
|---------|----------|:----------:|
| A | Import syntax basics | 1-2 |
| B | math module | 2 |
| C | datetime module | 2-3 |
| D | Extended random | 2-3 |
| E | string module and utilities | 2-3 |
| F | Custom modules | 3-4 |
| G | Import error handling | 3-4 |
| H | Module integration projects | 4-5 |

### Isolated Exercises

#### Cluster A: Import Syntax Basics (Difficulty 1-2)

| # | Type | Concept Focus |
|---|------|---------------|
| 1 | write_code | Basic `import module` and accessing with dot notation |
| 2 | write_code | `from module import name` for direct access |

#### Cluster B: math Module (Difficulty 2)

| # | Type | Concept Focus |
|---|------|---------------|
| 3 | write_code | Math functions: sqrt, floor, ceil, pow, fabs |

#### Cluster C: datetime Module (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 4 | write_code | Creating dates, formatting, basic arithmetic |

#### Cluster D: Extended random (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 5 | write_code | choice, shuffle, sample beyond basic randint |

#### Cluster E: string Module (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 6 | write_code | string.ascii_letters, digits, punctuation constants |

#### Cluster G: Import Error Handling (Difficulty 3-4)

| # | Type | Concept Focus |
|---|------|---------------|
| 7 | add_error_handling | Handle ModuleNotFoundError gracefully |
| 8 | add_error_handling | Handle missing attributes in modules |
| 9 | add_error_handling | Provide fallback behavior when imports fail |

### Hybrid Exercises

#### Hybrid 1: Import Fundamentals Journey

**Story:** Learn all import variations by building a character stat calculator.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GUIDANCE | write_code | Use `import math` with dot notation |
| 2 | GROWTH | write_code | Refactor with `from math import` |
| 3 | GROWTH | write_code | Add aliases to avoid naming conflicts |

**Placement:** After Cluster A (import basics)
**Difficulty:** 1-2
**Arc:** Apprentice (simplified - GUIDANCE → GROWTH → GROWTH)

#### Hybrid 2: The Math Toolkit

**Story:** Build a complete math utilities module for the {{school}}.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Implement basic math helper functions |
| 2 | GROWTH | write_code | Add advanced calculations (distance, area) |
| 3 | IMPROVEMENT | add_error_handling | Handle invalid inputs gracefully |

**Placement:** After Cluster B (math module)
**Difficulty:** 2-3
**Arc:** Custom (BUILD → EXTEND → HARDEN)

#### Hybrid 3: The Time Keeper

**Story:** {{mentor}} needs a scheduling system using datetime.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Create and format dates |
| 2 | GROWTH | write_code | Calculate time differences and deadlines |
| 3 | GROWTH | write_code | Build a complete event scheduler |

**Placement:** After Cluster C (datetime module)
**Difficulty:** 2-3
**Arc:** Custom (BUILD progressively)

#### Hybrid 4: Random Adventures Extended

**Story:** Expand the {{school}} game with advanced random features.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Use choice() for random selection |
| 2 | GROWTH | write_code | Use shuffle() for deck/card mechanics |
| 3 | GROWTH | write_code | Use sample() for lottery/drawing mechanics |
| 4 | IMPROVEMENT | add_error_handling | Handle empty lists and invalid ranges |

**Placement:** After Cluster D (extended random)
**Difficulty:** 2-3
**Arc:** Custom (BUILD → BUILD → BUILD → HARDEN)

#### Hybrid 5: Password and Code Generator

**Story:** {{hero}} needs secure passwords and codes using string constants.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Use string.ascii_letters and digits |
| 2 | GROWTH | write_code | Combine modules (string + random) |
| 3 | IMPROVEMENT | add_error_handling | Validate password requirements |

**Placement:** After Cluster E (string module)
**Difficulty:** 2-3
**Arc:** Custom (BUILD → COMBINE → HARDEN)

#### Hybrid 6: Create Your Own Module

**Story:** Build a reusable module for {{school}} operations.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | write_code | Understand module structure |
| 2 | OWNERSHIP | write_code | Create a custom module with functions |
| 3 | GROWTH | write_code | Add `__name__ == "__main__"` pattern |
| 4 | OWNERSHIP | write_code | Import and use your module |

**Placement:** Cluster F (custom modules)
**Difficulty:** 3-4
**Arc:** Inheritance (adapted - DISCOVERY → OWNERSHIP → GROWTH → OWNERSHIP)

#### Hybrid 7: The Resilient Importer

**Story:** Make code that survives missing modules.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | write_code | Code that crashes on missing import |
| 2 | INVESTIGATION | write_code | Understand the error |
| 3 | IMPROVEMENT | add_error_handling | Add try/except with fallback |
| 4 | GROWTH | add_error_handling | Create optional feature detection |

**Placement:** Cluster G (error handling)
**Difficulty:** 3-4
**Arc:** Rescue (adapted - SETBACK → INVESTIGATION → IMPROVEMENT → GROWTH)

#### Hybrid 8: The Module Mashup

**Story:** Combine multiple modules for a complex application.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Use math + random together |
| 2 | GROWTH | write_code | Add datetime for timestamps |
| 3 | GROWTH | write_code | Add string for formatting |
| 4 | IMPROVEMENT | add_error_handling | Handle all edge cases |

**Placement:** Cluster H (integration)
**Difficulty:** 4
**Arc:** Custom (PROGRESSIVE BUILD → HARDEN)

#### Hybrid 9: The {{school}} Management System

**Story:** Capstone project using all learned modules.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Design module structure |
| 2 | GROWTH | write_code | Implement core features with stdlib |
| 3 | GROWTH | write_code | Add reporting with datetime/math |
| 4 | IMPROVEMENT | add_error_handling | Production-ready error handling |
| 5 | OWNERSHIP | write_code | Add your own custom feature |

**Placement:** End of module (capstone)
**Difficulty:** 5
**Arc:** Custom (DESIGN → BUILD → EXTEND → HARDEN → CREATE)

---

## 4. Difficulty Progression Map

```
Difficulty:  1 -----> 2 -----> 3 -----> 4 -----> 5
             |       |        |        |        |
Exercises:   1,2     3,4,5,6  7,8,9    H6,H7,H8 H9
             H1      H2,H3
                     H4,H5
```

H1-H9 = Hybrid exercises

---

## 5. File Structure

```
exercises/
└── module_8_modules/
    ├── write_code/
    │   ├── exercise_1_import_basics.py
    │   ├── exercise_2_from_import.py
    │   ├── exercise_3_math_functions.py
    │   ├── exercise_4_datetime_basics.py
    │   ├── exercise_5_random_extended.py
    │   └── exercise_6_string_constants.py
    ├── add_error_handling/
    │   ├── exercise_1_import_not_found.py
    │   ├── exercise_2_missing_attribute.py
    │   └── exercise_3_fallback_imports.py
    └── hybrid/
        ├── exercise_1_import_journey.py
        ├── exercise_2_math_toolkit.py
        ├── exercise_3_time_keeper.py
        ├── exercise_4_random_adventures.py
        ├── exercise_5_password_generator.py
        ├── exercise_6_create_module.py
        ├── exercise_7_resilient_importer.py
        ├── exercise_8_module_mashup.py
        └── exercise_9_school_management.py
```

---

## 6. Implementation Phases

Implementation is organized into 5 phases following the concept progression.

### Phase 1: Import Fundamentals (Clusters A, B)

**Exercises:** 1, 2, 3, Hybrid 1, Hybrid 2
**Difficulty:** 1-2
**Estimated Files:** 5

| # | Type | File |
|---|------|------|
| 1 | write_code | `write_code/exercise_1_import_basics.py` |
| 2 | write_code | `write_code/exercise_2_from_import.py` |
| 3 | write_code | `write_code/exercise_3_math_functions.py` |
| H1 | hybrid | `hybrid/exercise_1_import_journey.py` |
| H2 | hybrid | `hybrid/exercise_2_math_toolkit.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| write_code | [templates/exercise_types/write_code.py](../../templates/exercise_types/write_code.py) |

---

### Phase 2: Time and Randomness (Clusters C, D)

**Exercises:** 4, 5, Hybrid 3, Hybrid 4
**Difficulty:** 2-3
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 4 | write_code | `write_code/exercise_4_datetime_basics.py` |
| 5 | write_code | `write_code/exercise_5_random_extended.py` |
| H3 | hybrid | `hybrid/exercise_3_time_keeper.py` |
| H4 | hybrid | `hybrid/exercise_4_random_adventures.py` |

---

### Phase 3: String Utilities and Combinations (Cluster E)

**Exercises:** 6, Hybrid 5
**Difficulty:** 2-3
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| 6 | write_code | `write_code/exercise_6_string_constants.py` |
| H5 | hybrid | `hybrid/exercise_5_password_generator.py` |

---

### Phase 4: Custom Modules and Error Handling (Clusters F, G)

**Exercises:** 7, 8, 9, Hybrid 6, Hybrid 7
**Difficulty:** 3-4
**Estimated Files:** 5

| # | Type | File |
|---|------|------|
| 7 | add_error_handling | `add_error_handling/exercise_1_import_not_found.py` |
| 8 | add_error_handling | `add_error_handling/exercise_2_missing_attribute.py` |
| 9 | add_error_handling | `add_error_handling/exercise_3_fallback_imports.py` |
| H6 | hybrid | `hybrid/exercise_6_create_module.py` |
| H7 | hybrid | `hybrid/exercise_7_resilient_importer.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| add_error_handling | [templates/exercise_types/add_error_handling.py](../../templates/exercise_types/add_error_handling.py) |

---

### Phase 5: Integration Projects (Cluster H)

**Exercises:** Hybrid 8, Hybrid 9
**Difficulty:** 4-5
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| H8 | hybrid | `hybrid/exercise_8_module_mashup.py` |
| H9 | hybrid | `hybrid/exercise_9_school_management.py` |

---

### Phase Summary

| Phase | Cluster | Exercises | Files | New Templates |
|:-----:|---------|-----------|:-----:|---------------|
| 1 | Import Fundamentals | 1-3, H1, H2 | 5 | write_code |
| 2 | Time and Randomness | 4-5, H3, H4 | 4 | *(none)* |
| 3 | String Utilities | 6, H5 | 2 | *(none)* |
| 4 | Custom Modules + Errors | 7-9, H6, H7 | 5 | add_error_handling |
| 5 | Integration | H8, H9 | 2 | *(none)* |
| **Total** | | **18** | **18** | |

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every exercise contains at least one `{{placeholder}}`
- [ ] NO concepts from later modules used (no classes, file I/O, third-party packages)
- [ ] All 10 learning objectives covered
- [ ] Progressive difficulty (1 to 5)
- [ ] Only uses write_code and add_error_handling types

### Format Requirements

- [ ] All functions use `pass` placeholder
- [ ] Instructions use `# YOUR CODE HERE` marker
- [ ] Each file has `main()` that calls all exercises
- [ ] PEP 8 compliant
- [ ] Follows templates from `templates/exercise_types/`

### Curriculum Compliance

| Concept | Used In |
|---------|---------|
| `import module` syntax | Exercises 1, H1 |
| `from module import` syntax | Exercises 2, H1 |
| `import as` aliases | Exercises 2, H1 |
| math module functions | Exercises 3, H2 |
| datetime basics | Exercises 4, H3 |
| random choice/shuffle/sample | Exercises 5, H4 |
| string module constants | Exercises 6, H5 |
| Creating custom modules | H6 |
| `__name__ == "__main__"` | H6 |
| ModuleNotFoundError handling | Exercises 7, H7 |
| AttributeError from imports | Exercise 8 |
| Fallback imports | Exercises 9, H7 |
| Multi-module integration | H8, H9 |

---

## 8. Implementation Notes

### Key Constraints

1. **No file I/O** - Cannot read/write files, only in-memory operations
2. **No third-party packages** - Only standard library
3. **No classes** - Functions and modules only
4. **Students HAVE try/except** - Available from module 4 (games) for error handling
5. **Students HAVE dicts** - Can use for complex data structures

### Standard Library Modules to Teach

| Module | Functions/Constants | Teaching Priority |
|--------|---------------------|:-----------------:|
| **math** | sqrt, floor, ceil, pow, pi, e | High |
| **datetime** | date, datetime, timedelta | High |
| **random** | choice, shuffle, sample (extend from module 5) | High |
| **string** | ascii_letters, digits, punctuation | Medium |

### Modules NOT to Teach (Too Advanced)

| Module | Reason |
|--------|--------|
| os, sys | File system operations |
| json | Requires file I/O context |
| collections | Counter/defaultdict - could confuse dict learning |
| re (regex) | Too complex |
| pathlib | File path manipulation |

### Pedagogical Considerations

**Why modules are challenging:**

- Namespace concept is abstract
- Multiple import syntaxes cause confusion
- Understanding what "module" means
- The `__name__` pattern is non-intuitive
- Finding and reading documentation

**Building mental models:**

- Module = "toolbox" containing related tools
- `import math` = "bring the whole toolbox"
- `from math import sqrt` = "take just the sqrt tool"
- `as` = "give it a nickname"
- `__name__` = "am I the main program or being used as a tool?"

### Common Errors for add_error_handling Exercises

1. **ModuleNotFoundError:** Importing a module that doesn't exist
2. **ImportError:** Importing a name that doesn't exist in the module
3. **AttributeError:** Accessing an attribute that doesn't exist
4. **TypeError:** Using imported function incorrectly

### Placeholder Usage Ideas

- `{{hero}}` stat calculations using math module
- `{{school}}` event scheduling with datetime
- `{{creature}}` random encounters with extended random
- `{{password}}` generation using string constants
- `{{spell1}}`, `{{spell2}}` in a custom magic module
- `{{mentor}}` teaches import patterns
- `{{item}}` inventory with module-based utilities
- `{{location}}` scheduling system

---

## 9. Concept-Specific Teaching Notes

### Import Syntax (Cluster A)

**Three main forms:**
```python
import math           # Access with math.sqrt()
from math import sqrt # Access directly as sqrt()
import math as m      # Access with m.sqrt()
```

**Key points:**
- Dot notation prevents naming conflicts
- `from` imports can shadow local names
- Aliases help with long module names

### math Module (Cluster B)

| Function | What It Does | Example |
|----------|--------------|---------|
| `sqrt(x)` | Square root | `sqrt(16)` → 4.0 |
| `floor(x)` | Round down | `floor(3.7)` → 3 |
| `ceil(x)` | Round up | `ceil(3.2)` → 4 |
| `pow(x, y)` | x to the power y | `pow(2, 3)` → 8.0 |
| `pi` | 3.14159... | `pi * r**2` |

### datetime Module (Cluster C)

**Core classes:**
- `date` - just date (year, month, day)
- `datetime` - date and time
- `timedelta` - duration/difference

**Common patterns:**
```python
from datetime import date, timedelta
today = date.today()
week_later = today + timedelta(days=7)
```

### Extended random (Cluster D)

Building on module 5's `randint` and `random`:

| Function | What It Does |
|----------|--------------|
| `choice(seq)` | Pick one random element |
| `shuffle(list)` | Reorder list in-place |
| `sample(seq, k)` | Pick k unique elements |

### string Module (Cluster E)

**Useful constants:**
```python
import string
string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits         # '0123456789'
string.punctuation    # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```

### Custom Modules (Cluster F)

**Creating a module:**
1. Create a `.py` file with functions
2. Import it from another file
3. Use `__name__ == "__main__"` for runnable modules

**The `__name__` pattern:**
```python
if __name__ == "__main__":
    # Only runs when this file is run directly
    # Not when imported as a module
    test_functions()
```

### Error Handling (Cluster G)

**Defensive import pattern:**
```python
try:
    import some_module
except ModuleNotFoundError:
    # Provide fallback or warning
    some_module = None
```

**Feature detection:**
```python
if some_module is not None:
    # Use the module
else:
    # Use alternative approach
```

---

## 10. Arc Adaptations

Since module 8 only has 2 exercise types, standard arcs need adaptation:

| Standard Arc | Adaptation for Module 8 |
|--------------|------------------------|
| Rescue | write_code (broken) → write_code (understand) → add_error_handling |
| Apprentice | write_code (guided) → write_code (practice) → write_code (independent) |
| Competition | Not feasible (needs which_is_better) |
| Inheritance | write_code (study) → write_code (own) → add_error_handling (fix) |

### Custom Arcs for Module 8

**BUILD → EXTEND → HARDEN:**
1. Build basic functionality (write_code)
2. Add more features (write_code)
3. Add error handling (add_error_handling)

**PROGRESSIVE BUILD:**
1. Start simple (write_code)
2. Add complexity (write_code)
3. Integrate multiple parts (write_code)
4. Production-ready (add_error_handling)

---

## 11. Comparison with Adjacent Modules

| Aspect | Module 7 (Dicts) | Module 8 (Modules) | Module 9 (OOP) |
|--------|------------------|-------------------|----------------|
| Exercise types | 7 | **2** | 5 |
| Total exercises | 20 | 18 | TBD |
| Hybrid count | 8 | 9 | TBD |
| Hybrid ratio | 57% | 60% | TBD |
| Key challenge | Key-based mental model | Import/namespace concepts | Object orientation |
| Arc diversity | High | Low (constrained) | Medium |

**Note:** Module 8's constraint of only 2 exercise types is compensated by:
1. Longer multi-part hybrids (4-5 parts instead of 3)
2. Progressive complexity within write_code sequences
3. Meaningful integration with add_error_handling for production readiness

---

## 12. Success Criteria

A successful module 8 implementation will:

1. **Teach import mastery** - Students can use all import variations confidently
2. **Build stdlib familiarity** - Students know when to reach for math, datetime, random, string
3. **Enable code organization** - Students can create and import their own modules
4. **Develop defensive coding** - Students handle import failures gracefully
5. **Prepare for OOP** - Namespace understanding prepares for class concepts in module 9
