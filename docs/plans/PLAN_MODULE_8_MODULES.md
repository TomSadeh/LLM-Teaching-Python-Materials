# Plan: Module 8 - Modules, Standard Library, and File I/O

Recreation plan for module_8_modules using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_8_modules |
| **Topic** | Python imports, standard library, file I/O (JSON/CSV) |
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
10. Read and write text files using context managers (`with open()`)
11. Save and load structured data with `json` module
12. Read and write tabular data with `csv` module
13. Handle file-related errors (FileNotFoundError, JSONDecodeError)

### Curriculum Constraints

| Available Concepts | NOT Available (later modules) |
|--------------------|-------------------------------|
| **From Modules 0-7:** | |
| print(), variables, strings, numbers | classes, objects, custom methods |
| input(), type conversion, f-strings | third-party packages (pip) |
| for loops, range(), turtle | async/await |
| if/elif/else, comparisons, boolean ops | decorators |
| lists, indexing, slicing, list methods | generators |
| functions (def, parameters, return) | |
| while loops, break, continue | |
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
| **File I/O (NEW):** | |
| `with open(file, mode) as f:` | |
| `f.read()`, `f.write()`, `f.readlines()` | |
| `json.load()`, `json.dump()`, `json.loads()`, `json.dumps()` | |
| `csv.reader()`, `csv.writer()`, `csv.DictReader()`, `csv.DictWriter()` | |
| FileNotFoundError, JSONDecodeError | |

### Why File I/O Belongs Here

| Reason | Explanation |
|--------|-------------|
| **json and csv ARE stdlib modules** | Natural extension of "modules and standard library" |
| **Enables real projects** | Module 10 mega project needs data persistence |
| **Error handling synergy** | File errors pair well with add_error_handling type |
| **Dict integration** | JSON works directly with dicts (learned in module 7) |
| **Practical skill** | Every real program needs to save/load data |

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types for Module 8 |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Exercise format standards |

---

## 2. Exercise Distribution

### Available Exercise Types (4 total)

| Category | Types |
|----------|-------|
| **Core** | write_code |
| **Improvement** | add_error_handling |
| **Debugging** | decode_error (NEW - file errors enable this) |
| **Scaffolded** | complete_function |

**Why more types now:** File I/O introduces common, predictable errors (FileNotFoundError, JSONDecodeError, csv formatting issues) that make `decode_error` pedagogically valuable. The `complete_function` type helps scaffold file handling patterns.

### Target Distribution

| Type | Count | Rationale |
|------|:-----:|-----------|
| write_code | 8 | Core stdlib exploration, file operations, module creation |
| add_error_handling | 4 | Import safety, file error handling |
| decode_error | 3 | File-related error interpretation |
| complete_function | 2 | Scaffold file handling patterns |
| **hybrid** | 10 | Multi-part projects (59% of total) |
| **TOTAL** | **27** | |

### Hybrid Ratio Calculation

- Total exercises: 27
- Hybrid exercises: 10
- Isolated exercises: 17
- Ratio: **59%** (meets 60-70% target, rounded)

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
| **H** | **File I/O basics (text files)** | **2-3** |
| **I** | **JSON for structured data** | **3-4** |
| **J** | **CSV for tabular data** | **3-4** |
| K | Full integration projects | 4-5 |

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

#### Cluster H: File I/O Basics (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 9 | write_code | Read and write text files with `with open()` |
| 10 | complete_function | Complete file reading/writing patterns |
| 11 | decode_error | Interpret FileNotFoundError and PermissionError |

#### Cluster I: JSON Module (Difficulty 3-4)

| # | Type | Concept Focus |
|---|------|---------------|
| 12 | write_code | Save and load dicts/lists with json.dump/load |
| 13 | decode_error | Interpret JSONDecodeError (malformed JSON) |
| 14 | add_error_handling | Safe JSON loading with fallback defaults |

#### Cluster J: CSV Module (Difficulty 3-4)

| # | Type | Concept Focus |
|---|------|---------------|
| 15 | write_code | Read and write CSV files with csv module |
| 16 | complete_function | Complete CSV processing functions |
| 17 | decode_error | Handle CSV formatting issues |

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
**Arc:** Apprentice (simplified - GUIDANCE -> GROWTH -> GROWTH)

#### Hybrid 2: The Math Toolkit

**Story:** Build a complete math utilities module for the {{school}}.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Implement basic math helper functions |
| 2 | GROWTH | write_code | Add advanced calculations (distance, area) |
| 3 | IMPROVEMENT | add_error_handling | Handle invalid inputs gracefully |

**Placement:** After Cluster B (math module)
**Difficulty:** 2-3
**Arc:** Custom (BUILD -> EXTEND -> HARDEN)

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

**Placement:** After Cluster D (extended random)
**Difficulty:** 2-3
**Arc:** Custom (BUILD -> BUILD -> BUILD)

#### Hybrid 5: Password and Code Generator

**Story:** {{hero}} needs secure passwords and codes using string constants.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Use string.ascii_letters and digits |
| 2 | GROWTH | write_code | Combine modules (string + random) |
| 3 | IMPROVEMENT | add_error_handling | Validate password requirements |

**Placement:** After Cluster E (string module)
**Difficulty:** 2-3
**Arc:** Custom (BUILD -> COMBINE -> HARDEN)

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
**Arc:** Inheritance (adapted - DISCOVERY -> OWNERSHIP -> GROWTH -> OWNERSHIP)

#### Hybrid 7: The Data Keeper (NEW - File I/O)

**Story:** {{hero}} needs to save and load progress in {{school}}.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Save data to a text file |
| 2 | GROWTH | write_code | Load data from a text file |
| 3 | INVESTIGATION | decode_error | Understand file errors |
| 4 | IMPROVEMENT | add_error_handling | Handle missing files gracefully |

**Placement:** Cluster H (file I/O basics)
**Difficulty:** 2-3
**Arc:** Custom (BUILD -> BUILD -> UNDERSTAND -> HARDEN)

#### Hybrid 8: The Settings Manager (NEW - JSON)

**Story:** Build a configuration system that persists between sessions.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Save settings dict to JSON file |
| 2 | GROWTH | write_code | Load settings with defaults for missing keys |
| 3 | INVESTIGATION | decode_error | Handle corrupted JSON files |
| 4 | GROWTH | write_code | Build complete settings manager |

**Placement:** Cluster I (JSON module)
**Difficulty:** 3-4
**Arc:** Custom (BUILD -> BUILD -> INVESTIGATE -> INTEGRATE)

#### Hybrid 9: The Records Keeper (NEW - CSV)

**Story:** {{school}} needs to track {{creature}} sightings in a spreadsheet format.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Write records to CSV |
| 2 | GROWTH | write_code | Read and display CSV data |
| 3 | GROWTH | complete_function | Add search and filter functions |
| 4 | GROWTH | write_code | Generate reports from CSV data |

**Placement:** Cluster J (CSV module)
**Difficulty:** 3-4
**Arc:** Custom (BUILD -> BUILD -> SCAFFOLD -> EXTEND)

#### Hybrid 10: The {{school}} Data System (Capstone)

**Story:** Build a complete data management system using all learned modules.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Design data structure (dicts for entities) |
| 2 | GROWTH | write_code | Implement CRUD operations |
| 3 | GROWTH | write_code | Add JSON persistence (save/load) |
| 4 | GROWTH | write_code | Add CSV export for reports |
| 5 | IMPROVEMENT | add_error_handling | Production-ready error handling |

**Placement:** End of module (capstone)
**Difficulty:** 5
**Arc:** Custom (DESIGN -> BUILD -> PERSIST -> EXPORT -> HARDEN)

---

## 4. Difficulty Progression Map

```
Difficulty:  1 -----> 2 -----> 3 -----> 4 -----> 5
             |       |        |        |        |
Exercises:   1,2     3,4,5,6  7,8      12,13,14 H10
             H1      9,10,11  15,16,17 H6,H8,H9
                     H2,H3    H7
                     H4,H5
```

H1-H10 = Hybrid exercises

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
    │   ├── exercise_6_string_constants.py
    │   ├── exercise_7_file_basics.py
    │   └── exercise_8_json_basics.py
    ├── complete_function/
    │   ├── exercise_1_file_patterns.py
    │   └── exercise_2_csv_processing.py
    ├── decode_error/
    │   ├── exercise_1_file_errors.py
    │   ├── exercise_2_json_errors.py
    │   └── exercise_3_csv_errors.py
    ├── add_error_handling/
    │   ├── exercise_1_import_not_found.py
    │   ├── exercise_2_missing_attribute.py
    │   ├── exercise_3_file_not_found.py
    │   └── exercise_4_json_fallback.py
    └── hybrid/
        ├── exercise_1_import_journey.py
        ├── exercise_2_math_toolkit.py
        ├── exercise_3_time_keeper.py
        ├── exercise_4_random_adventures.py
        ├── exercise_5_password_generator.py
        ├── exercise_6_create_module.py
        ├── exercise_7_data_keeper.py
        ├── exercise_8_settings_manager.py
        ├── exercise_9_records_keeper.py
        └── exercise_10_school_data_system.py
```

---

## 6. Implementation Phases

Implementation is organized into 6 phases following the concept progression.

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

### Phase 2: Time, Randomness, and Strings (Clusters C, D, E)

**Exercises:** 4, 5, 6, Hybrid 3, Hybrid 4, Hybrid 5
**Difficulty:** 2-3
**Estimated Files:** 6

| # | Type | File |
|---|------|------|
| 4 | write_code | `write_code/exercise_4_datetime_basics.py` |
| 5 | write_code | `write_code/exercise_5_random_extended.py` |
| 6 | write_code | `write_code/exercise_6_string_constants.py` |
| H3 | hybrid | `hybrid/exercise_3_time_keeper.py` |
| H4 | hybrid | `hybrid/exercise_4_random_adventures.py` |
| H5 | hybrid | `hybrid/exercise_5_password_generator.py` |

---

### Phase 3: Custom Modules and Import Errors (Clusters F, G)

**Exercises:** 7, 8, Hybrid 6
**Difficulty:** 3-4
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 7 | add_error_handling | `add_error_handling/exercise_1_import_not_found.py` |
| 8 | add_error_handling | `add_error_handling/exercise_2_missing_attribute.py` |
| H6 | hybrid | `hybrid/exercise_6_create_module.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| add_error_handling | [templates/exercise_types/add_error_handling.py](../../templates/exercise_types/add_error_handling.py) |

---

### Phase 4: File I/O Basics (Cluster H)

**Exercises:** 9, 10, 11, Hybrid 7
**Difficulty:** 2-3
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 9 | write_code | `write_code/exercise_7_file_basics.py` |
| 10 | complete_function | `complete_function/exercise_1_file_patterns.py` |
| 11 | decode_error | `decode_error/exercise_1_file_errors.py` |
| H7 | hybrid | `hybrid/exercise_7_data_keeper.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| complete_function | [templates/exercise_types/complete_function.py](../../templates/exercise_types/complete_function.py) |
| decode_error | [templates/exercise_types/decode_error.py](../../templates/exercise_types/decode_error.py) |

---

### Phase 5: JSON and CSV (Clusters I, J)

**Exercises:** 12, 13, 14, 15, 16, 17, Hybrid 8, Hybrid 9
**Difficulty:** 3-4
**Estimated Files:** 8

| # | Type | File |
|---|------|------|
| 12 | write_code | `write_code/exercise_8_json_basics.py` |
| 13 | decode_error | `decode_error/exercise_2_json_errors.py` |
| 14 | add_error_handling | `add_error_handling/exercise_4_json_fallback.py` |
| 15 | write_code | `write_code/exercise_9_csv_basics.py` |
| 16 | complete_function | `complete_function/exercise_2_csv_processing.py` |
| 17 | decode_error | `decode_error/exercise_3_csv_errors.py` |
| H8 | hybrid | `hybrid/exercise_8_settings_manager.py` |
| H9 | hybrid | `hybrid/exercise_9_records_keeper.py` |

---

### Phase 6: Integration (Cluster K)

**Exercises:** Hybrid 10
**Difficulty:** 5
**Estimated Files:** 1

| # | Type | File |
|---|------|------|
| H10 | hybrid | `hybrid/exercise_10_school_data_system.py` |

---

### Phase Summary

| Phase | Cluster | Exercises | Files | New Templates |
|:-----:|---------|-----------|:-----:|---------------|
| 1 | Import Fundamentals | 1-3, H1, H2 | 5 | write_code |
| 2 | Time/Random/String | 4-6, H3-H5 | 6 | *(none)* |
| 3 | Custom Modules + Errors | 7-8, H6 | 3 | add_error_handling |
| 4 | File I/O Basics | 9-11, H7 | 4 | complete_function, decode_error |
| 5 | JSON and CSV | 12-17, H8, H9 | 8 | *(none)* |
| 6 | Integration | H10 | 1 | *(none)* |
| **Total** | | **27** | **27** | |

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every exercise contains at least one `{{placeholder}}`
- [ ] NO concepts from later modules used (no classes, third-party packages)
- [ ] All 13 learning objectives covered
- [ ] Progressive difficulty (1 to 5)
- [ ] Uses all 4 available exercise types appropriately

### Format Requirements

- [ ] All functions use `pass` placeholder
- [ ] Instructions use `# YOUR CODE HERE` marker
- [ ] Each file has `main()` that calls all exercises
- [ ] PEP 8 compliant
- [ ] Follows templates from `templates/exercise_types/`

### Curriculum Compliance

| Concept | Covered In |
|---------|------------|
| `import module` syntax | Exercises 1, H1 |
| `from module import` syntax | Exercises 2, H1 |
| `import as` aliases | Exercises 2, H1 |
| math module functions | Exercises 3, H2 |
| datetime basics | Exercises 4, H3 |
| random choice/shuffle/sample | Exercises 5, H4 |
| string module constants | Exercises 6, H5 |
| Creating custom modules | H6 |
| `__name__ == "__main__"` | H6 |
| ModuleNotFoundError handling | Exercises 7, H6 |
| AttributeError from imports | Exercise 8 |
| **File I/O with `with open()`** | Exercises 9, 10, 11, H7 |
| **json.load() / json.dump()** | Exercises 12, 13, 14, H8 |
| **csv.reader / csv.writer** | Exercises 15, 16, 17, H9 |
| **FileNotFoundError handling** | Exercises 11, 14, H7 |
| **JSONDecodeError handling** | Exercises 13, 14, H8 |
| **Full integration** | H10 |

---

## 8. Implementation Notes

### Key Constraints

1. **No classes** - Functions and modules only (classes come in module 9)
2. **No third-party packages** - Only standard library
3. **Students HAVE try/except** - Available from module 4 (games) for error handling
4. **Students HAVE dicts** - JSON works naturally with dict structures
5. **Context managers (`with`) are NEW** - Teach as the safe way to handle files

### Standard Library Modules to Teach

| Module | Functions/Constants | Teaching Priority |
|--------|---------------------|:-----------------:|
| **math** | sqrt, floor, ceil, pow, pi, e | High |
| **datetime** | date, datetime, timedelta | High |
| **random** | choice, shuffle, sample (extend from module 5) | High |
| **string** | ascii_letters, digits, punctuation | Medium |
| **json** | load, dump, loads, dumps | High |
| **csv** | reader, writer, DictReader, DictWriter | High |

### File I/O Concepts to Teach

| Concept | Priority | Notes |
|---------|:--------:|-------|
| `with open(file, mode) as f:` | High | Always use context manager |
| File modes: 'r', 'w', 'a' | High | Read, write, append |
| `f.read()`, `f.write()` | High | Basic operations |
| `f.readlines()` | Medium | For line-by-line processing |
| `json.dump(data, f)` | High | Save dict/list to file |
| `json.load(f)` | High | Load dict/list from file |
| `csv.reader(f)` | High | Read rows as lists |
| `csv.writer(f)` | High | Write rows as lists |
| `csv.DictReader(f)` | Medium | Read rows as dicts |
| `csv.DictWriter(f, fieldnames)` | Medium | Write dicts as rows |

### Modules NOT to Teach (Too Advanced)

| Module | Reason |
|--------|--------|
| os, sys | System-level operations |
| pathlib | Path manipulation (keep it simple with strings) |
| collections | Counter/defaultdict - could confuse dict learning |
| re (regex) | Too complex for this level |
| pickle | Security concerns, binary format |

### Common File Errors to Cover

| Error | When It Occurs | Teaching Approach |
|-------|----------------|-------------------|
| FileNotFoundError | File doesn't exist when reading | decode_error, add_error_handling |
| PermissionError | No access rights | decode_error (brief mention) |
| JSONDecodeError | Malformed JSON content | decode_error, add_error_handling |
| csv format issues | Wrong delimiter, missing fields | decode_error |

### Pedagogical Considerations

**Why file I/O is challenging:**

- Context managers (`with`) are new syntax
- File modes are easy to confuse
- Path handling can be tricky
- Error handling is essential (files may not exist)
- JSON/CSV formats have specific requirements

**Building mental models:**

- `with open() as f:` = "borrow the file, return it when done"
- File modes: 'r' = reading glasses, 'w' = writing pen (erases!), 'a' = adding to a list
- JSON = "Python dicts/lists saved as text"
- CSV = "spreadsheet saved as text"

### Placeholder Usage Ideas

- `{{hero}}` profile saved to JSON
- `{{school}}` settings/configuration file
- `{{creature}}` sightings logged to CSV
- `{{item}}` inventory persisted between sessions
- `{{location}}` data exported to reports
- `{{spell1}}`, `{{spell2}}` in a custom module
- `{{mentor}}` provides save/load guidance

---

## 9. Concept-Specific Teaching Notes

### Import Syntax (Cluster A)

**Three main forms:**
```python
import math           # Access with math.sqrt()
from math import sqrt # Access directly as sqrt()
import math as m      # Access with m.sqrt()
```

### Context Managers (Cluster H) - NEW

**The `with` statement:**
```python
# Always use with for files - it handles closing automatically
with open("data.txt", "r") as f:
    content = f.read()
# File is automatically closed here, even if errors occur
```

**Why `with` matters:**
- Automatically closes the file
- Works even if an error occurs
- Cleaner than try/finally
- The "Pythonic" way

### JSON Module (Cluster I) - NEW

**Saving data:**
```python
import json

data = {"name": "{{hero}}", "level": 5, "items": ["sword", "shield"]}

with open("save.json", "w") as f:
    json.dump(data, f, indent=2)  # indent for readability
```

**Loading data:**
```python
with open("save.json", "r") as f:
    data = json.load(f)
```

**JSON supports:** dicts, lists, strings, numbers, booleans, None
**JSON does NOT support:** sets, tuples (become lists), custom objects

### CSV Module (Cluster J) - NEW

**Writing CSV:**
```python
import csv

records = [
    ["name", "level", "house"],
    ["{{hero}}", 5, "{{house}}"],
    ["{{heroine}}", 6, "{{house}}"]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(records)
```

**Reading CSV:**
```python
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # Each row is a list
```

**DictReader/DictWriter** - More advanced, uses first row as keys

### Error Handling Patterns

**Safe file loading with fallback:**
```python
def load_settings(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"default": "settings"}
    except json.JSONDecodeError:
        print("Settings file corrupted, using defaults")
        return {"default": "settings"}
```

---

## 10. Arc Adaptations

With 4 exercise types, module 8 now has more arc flexibility:

| Standard Arc | Adaptation for Module 8 |
|--------------|------------------------|
| Rescue | write_code (broken) -> decode_error (understand) -> add_error_handling (fix) |
| Apprentice | write_code (guided) -> write_code (practice) -> write_code (independent) |
| Investigation | write_code (build) -> decode_error (investigate) -> add_error_handling (harden) |

### Custom Arcs for File I/O

**BUILD -> BUILD -> INVESTIGATE -> HARDEN:**
1. Build basic functionality (write_code)
2. Extend with more features (write_code)
3. Understand what can go wrong (decode_error)
4. Add defensive error handling (add_error_handling)

**BUILD -> SCAFFOLD -> EXTEND:**
1. Learn the pattern (write_code)
2. Practice with guidance (complete_function)
3. Build independently (write_code)

---

## 11. Comparison with Adjacent Modules

| Aspect | Module 7 (Dicts) | Module 8 (Modules) | Module 9 (OOP) |
|--------|------------------|-------------------|----------------|
| Exercise types | 7 | **4** | 5 |
| Total exercises | 20 | **27** | 20 |
| Hybrid count | 8 | **10** | 8 |
| Hybrid ratio | 57% | **59%** | 62% |
| Key challenge | Key-based mental model | Import/namespace + File I/O | Object orientation |
| Enables for next | Dict → JSON bridge | File I/O → Persistence | OOP → Full projects |

**Module 8's expanded scope:**
1. Standard library mastery (import patterns)
2. File I/O fundamentals (persistence)
3. JSON for structured data (builds on dicts)
4. CSV for tabular data (builds on lists)
5. Error handling patterns (production readiness)

---

## 12. Success Criteria

A successful module 8 implementation will:

1. **Teach import mastery** - Students can use all import variations confidently
2. **Build stdlib familiarity** - Students know when to reach for math, datetime, random, string
3. **Enable code organization** - Students can create and import their own modules
4. **Enable data persistence** - Students can save/load data with JSON and CSV
5. **Develop defensive coding** - Students handle file and import errors gracefully
6. **Prepare for OOP and mega project** - File I/O + modules = ready for real applications

### Measurable Outcomes

| Objective | How We'll Know |
|-----------|----------------|
| Can use imports | Exercises 1-2, H1 completed correctly |
| Knows stdlib | Exercises 3-6, H2-H5 show appropriate module use |
| Can create modules | H6 produces working custom module |
| Can persist data | H7, H8, H9 show working save/load |
| Handles errors | add_error_handling exercises show defensive patterns |

---

## 13. Transition Notes

### From Module 7 (Dicts)

Students arrive knowing:
- Dictionary creation and manipulation
- Nested data structures
- `.get()` for safe access
- When to use dicts vs lists

**Bridge concepts:**
- JSON is "dicts/lists saved to a file"
- CSV is "lists saved as spreadsheet rows"
- File paths are just strings

### To Module 9 (OOP)

Students should leave ready to:
- Organize code across multiple files
- Persist object state (save/load objects as dicts/JSON)
- Handle errors gracefully
- Work with structured data formats

**OOP prep:**
- Namespaces prepare for class scope
- Module organization prepares for class organization
- JSON persistence will work with object `__dict__`

### To Module 10 (Mega Project)

With module 8 complete, students can:
- Build multi-file projects (custom modules)
- Save and load game state (JSON)
- Export reports and data (CSV)
- Handle all common errors
- Use the full standard library

This is the foundation for a **real** mega project with persistence and proper architecture.
