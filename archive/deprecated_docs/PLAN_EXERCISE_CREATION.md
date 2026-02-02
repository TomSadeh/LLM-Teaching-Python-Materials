# Exercise Creation Plan

This document outlines the plan for creating exercises from the 14 exercise type templates.

---

## Phase 0: Migration (FIRST)

Before creating new exercises, migrate existing exercises to the new structure.

### Task: Move Existing Exercises to `write_code/` Subdirectories

```bash
# For each module:
mkdir exercises/module_X_topic/write_code/
mv exercises/module_X_topic/exercise_*.py exercises/module_X_topic/write_code/
```

### Modules to Migrate
- [x] module_0_basics (18 exercises)
- [x] module_1_turtle_loops (10 exercises)
- [x] module_2_decisions (9 exercises)
- [x] module_3_lists (9 exercises)
- [x] module_4_games (9 exercises)
- [x] module_5_functions (9 exercises)
- [x] module_6_final_project (3 exercises)
- [x] module_7_dictionaries (9 exercises)
- [x] module_8_modules (9 exercises)
- [x] module_9_oop (9 exercises)

**Total: 94 exercises migrated to `write_code/` subdirectories**

### Update Scripts
- [x] Update `scripts/convert_exercises.py` to scan subdirectories
- [x] Added `exercise_type` field to exercise metadata
- [x] Added `exercise_types` list to module metadata
- [ ] Update any other scripts that reference exercise paths

---

## Overview

### Exercise Types by Category

| Category | Types | Purpose |
|----------|-------|---------|
| **Reading** | output_prediction, code_tracing, match_output | Understand existing code |
| **Scaffolded Writing** | fill_blanks, code_ordering, complete_function | Guided code writing |
| **Improvement** | fix_style, simplify_code, add_error_handling | Make code better |
| **Analysis** | which_is_better, spot_difference | Compare and judge |
| **Debugging** | decode_error, bug_hunt | Find and fix problems |
| **Free Writing** | blank_page | Independent implementation |

---

## Phase 1: Foundation Exercises (Priority: HIGH)

Create exercises that support **every module** - these are the most versatile types.

### 1.1 Bug Hunt (1 per module)
- **Why first**: Engaging narrative format, covers all difficulty levels
- **Target**: 10 exercises (one per module)
- **Naming**: `exercise_bug_hunt_[module].py`

### 1.2 Decode the Error (1 per module)
- **Why early**: Essential debugging skill, universally needed
- **Target**: 10 exercises (one per module)
- **Naming**: `exercise_decode_error_[module].py`

### 1.3 Output Prediction (Basics + Loops + Decisions)
- **Why early**: Fundamental mental execution skill
- **Target**: 3 exercises
- **Naming**: `exercise_output_prediction_[topic].py`

---

## Phase 2: Scaffolded Practice (Priority: HIGH)

Create exercises that help students practice with support.

### 2.1 Fill in the Blanks (Basics + Loops + Functions)
- **Target**: 3 exercises
- **Focus**: Keywords, operators, method names

### 2.2 Code Ordering (Basics + Loops + Functions)
- **Target**: 3 exercises
- **Focus**: Program flow, dependencies

### 2.3 Complete the Function (Functions + Lists + Dicts)
- **Target**: 3 exercises
- **Focus**: Implementation patterns

---

## Phase 3: Code Quality (Priority: MEDIUM)

Create exercises focused on writing better code.

### 3.1 Fix the Style (Basics + Functions + OOP)
- **Target**: 3 exercises
- **Focus**: PEP 8, naming, formatting

### 3.2 Simplify This (Lists + Functions + Dicts)
- **Target**: 3 exercises
- **Focus**: Pythonic idioms

### 3.3 Add Error Handling (Functions + Games + Modules)
- **Target**: 3 exercises
- **Focus**: Try/except patterns

---

## Phase 4: Critical Thinking (Priority: MEDIUM)

Create exercises for analysis and comparison.

### 4.1 Which is Better? (Lists + Functions + Dicts + OOP)
- **Target**: 4 exercises
- **Focus**: Trade-offs, judgment

### 4.2 Spot the Difference (Basics + Lists + Functions)
- **Target**: 3 exercises
- **Focus**: Subtle behavior differences

### 4.3 Code Tracing (Loops + Decisions + Lists)
- **Target**: 3 exercises
- **Focus**: Variable tracking tables

### 4.4 Match the Output (Basics + Loops + Lists)
- **Target**: 3 exercises
- **Focus**: Quick pattern matching

---

## Phase 5: Independence (Priority: LOWER)

Create exercises for advanced independent practice.

### 5.1 Write From Scratch (Functions + Dicts + OOP)
- **Target**: 3 exercises with 5-10 challenges each
- **Focus**: Full implementation from docstrings
- **Difficulty progression**: Easy → Expert within each exercise

---

## File Structure

Each module contains subdirectories for each exercise type:

```
exercises/
├── module_0_basics/
│   ├── write_code/                        # Traditional exercises (existing)
│   │   ├── exercise_1_hello_world.py
│   │   ├── exercise_2_variables.py
│   │   └── exercise_3_input_output.py
│   │
│   ├── bug_hunt/                          # Debugging with stories
│   │   ├── exercise_1_print_bugs.py
│   │   ├── exercise_2_variable_bugs.py
│   │   └── exercise_3_string_bugs.py
│   │
│   ├── decode_error/                      # Error message interpretation
│   │   ├── exercise_1_syntax_errors.py
│   │   ├── exercise_2_name_errors.py
│   │   └── exercise_3_type_errors.py
│   │
│   ├── output_prediction/                 # Mental execution
│   │   ├── exercise_1_print_statements.py
│   │   └── exercise_2_variables.py
│   │
│   ├── fill_blanks/                       # Syntax recall
│   │   └── exercise_1_basics.py
│   │
│   ├── code_ordering/                     # Program flow
│   │   └── exercise_1_sequences.py
│   │
│   ├── spot_difference/                   # Subtle changes
│   │   └── exercise_1_operators.py
│   │
│   └── fix_style/                         # PEP 8 practice
│       └── exercise_1_naming.py
│
├── module_1_turtle_loops/
│   ├── write_code/
│   ├── bug_hunt/
│   ├── decode_error/
│   ├── output_prediction/
│   ├── code_tracing/                      # Variable tracking
│   ├── fill_blanks/
│   ├── code_ordering/
│   └── match_output/
│
├── module_5_functions/
│   ├── write_code/
│   ├── bug_hunt/
│   ├── decode_error/
│   ├── complete_function/                 # Finish partial functions
│   ├── blank_page/                        # Docstrings only
│   ├── simplify_code/                     # Pythonic idioms
│   ├── add_error_handling/                # Try/except
│   └── which_is_better/                   # Trade-off analysis
│
└── ... (other modules follow same pattern)
```

### Type Directories by Module

Not all types apply to all modules. Here's the mapping:

| Module | Types Available |
|--------|-----------------|
| module_0_basics | write_code, bug_hunt, decode_error, output_prediction, fill_blanks, code_ordering, spot_difference, fix_style |
| module_1_turtle_loops | write_code, bug_hunt, decode_error, output_prediction, code_tracing, fill_blanks, code_ordering, match_output |
| module_2_decisions | write_code, bug_hunt, decode_error, output_prediction, code_tracing, fill_blanks, spot_difference |
| module_3_lists | write_code, bug_hunt, decode_error, output_prediction, code_tracing, match_output, spot_difference, simplify_code, which_is_better |
| module_4_games | write_code, bug_hunt, decode_error, add_error_handling |
| module_5_functions | write_code, bug_hunt, decode_error, complete_function, blank_page, simplify_code, add_error_handling, which_is_better, fix_style |
| module_6_final_project | write_code, blank_page |
| module_7_dictionaries | write_code, bug_hunt, decode_error, complete_function, blank_page, simplify_code, which_is_better |
| module_8_modules | write_code, bug_hunt, add_error_handling |
| module_9_oop | write_code, bug_hunt, decode_error, complete_function, blank_page, fix_style, which_is_better |

---

## Creation Guidelines

### For Each Exercise

1. **Create the type directory** if it doesn't exist:
   ```bash
   mkdir -p exercises/module_X_topic/[type]/
   ```

2. **Read the template header** - understand purpose, structure, guidelines

3. **Create the exercise file**:
   ```bash
   exercises/module_X_topic/[type]/exercise_N_topic.py
   ```

4. **Choose concepts** from the template's concept lists

5. **Create 4-8 challenges** per exercise, progressing in difficulty

6. **Use {{placeholders}}** for all theme references

7. **Add Hebrew translations** to `exercises_config.json` or converter script

8. **Test the exercise** runs without errors (where applicable)

### Difficulty Distribution Per Exercise

- **Easy**: 2-3 challenges (confidence builders)
- **Medium**: 2-3 challenges (core practice)
- **Hard**: 1-2 challenges (stretch goals)

### Theming Guidelines

Always use placeholders - never hardcode theme references:

```python
# ✓ CORRECT
hero = "{{hero}}"
print(f"{hero} casts {{spell1}}!")

# ✗ WRONG
hero = "Harry"
print(f"{hero} casts Lumos!")
```

---

## Integration with Existing System

### 1. Update exercises_config.json

Add new exercise type metadata:

```json
{
  "exercise_types": {
    "bug_hunt": {
      "name": "Bug Hunt",
      "name_he": "ציד באגים",
      "category": "debugging"
    }
  }
}
```

### 2. Update convert_exercises.py

Add title translations for new exercises:

```python
TITLE_HE_MAP = {
    # ...existing...
    "exercise_bug_hunt_basics": "ציד באגים - יסודות",
    "exercise_decode_error_basics": "פענוח שגיאות - יסודות",
    # ...etc...
}
```

### 3. Run Conversion

After creating exercises:

```bash
python scripts/convert_exercises.py
```

---

## Estimated Effort

| Phase | Exercises | Est. Hours | Priority |
|-------|-----------|------------|----------|
| Phase 1 | 23 | 15-20 | HIGH |
| Phase 2 | 9 | 8-12 | HIGH |
| Phase 3 | 9 | 8-12 | MEDIUM |
| Phase 4 | 13 | 10-15 | MEDIUM |
| Phase 5 | 3 | 5-8 | LOWER |
| **Total** | **57** | **46-67** | - |

---

## Quality Checklist

Before committing each exercise:

- [ ] All challenges use `{{placeholders}}` for theme content
- [ ] ✏️ markers clearly show where students write code
- [ ] Difficulty progresses from easy to hard
- [ ] Code follows PEP 8 conventions
- [ ] Hebrew title added to converter/config
- [ ] Exercise runs without syntax errors
- [ ] main() function calls all challenges appropriately
- [ ] Template structure is followed (header, challenges, main)

---

## Success Metrics

After completion, the exercise library should:

1. **Cover all modules** with at least 2 new exercise types each
2. **Span all categories** (reading, writing, improvement, analysis, debugging)
3. **Support all difficulty levels** (1, 2, 3) within each type
4. **Be fully themed** with no hardcoded references
5. **Be bilingual** with Hebrew translations for all titles
