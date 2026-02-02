# Handoff: New Module Structure (v3.0)

This document explains the new exercise organization system.

---

## Directory Structure

```
raw_exercises_new/
└── module_0_basics/
    ├── exercises.json           # Module manifest (NEW)
    ├── hints.json              # Hints per exercise (TODO)
    ├── output_prediction/
    │   ├── exercise_1_print_basics.py
    │   └── exercise_2_arithmetic.py
    ├── write_code/
    │   ├── exercise_1_hello.py
    │   ├── exercise_2_variables.py
    │   ├── exercise_3_calculator.py
    │   ├── exercise_4_strings.py
    │   ├── exercise_5_input.py
    │   └── exercise_6_fstrings.py
    ├── fill_blanks/
    │   ├── exercise_1_variables.py
    │   └── exercise_2_input.py
    ├── spot_difference/
    │   └── exercise_1_variable_errors.py
    ├── code_ordering/
    │   └── exercise_1_program_flow.py
    ├── match_output/
    │   └── exercise_1_string_output.py
    ├── decode_error/
    │   ├── exercise_1_string_errors.py
    │   └── exercise_2_input_errors.py
    ├── complete_function/
    │   └── exercise_1_format_output.py
    ├── bug_hunt/
    │   └── exercise_1_basics_bugs.py
    ├── fix_style/
    │   └── exercise_1_naming.py
    └── hybrid/
        ├── exercise_1_apprentice_variables.py
        └── exercise_2_apprentice_program.py
```

---

## Key Files

### 1. `exercises_config.json` (Root Level)

Global configuration for the entire curriculum.

```json
{
  "version": "3.0.0",
  "modules": {
    "module_0_basics": {
      "order_index": 0,
      "difficulty": 1,
      "topic_id": "basics.print",
      "name_en": "Basics",
      "name_he": "יסודות",
      "description_en": "...",
      "description_he": "..."
    }
  },
  "exercise_types": { ... },
  "categories": { ... },
  "i18n": { ... }
}
```

**Purpose:** Defines modules, exercise types, categories, and translations.

---

### 2. `exercises.json` (Per Module)

Each module has its own manifest at `raw_exercises_new/{module}/exercises.json`.

```json
{
  "version": "3.0.0",
  "theme_support": true,
  "module": "module_0_basics",
  "count": 20,
  "exercise_types": ["bug_hunt", "code_ordering", ...],
  "exercises": [
    {
      "id": "module_0_basics.output_prediction.exercise_1_print_basics",
      "exercise_type": "output_prediction",
      "category": "reading",
      "title_en": "Print Basics",
      "title_he": "יסודות הדפסה",
      "difficulty": 1,
      "order_index": 1,
      "concepts": ["print() function", "string literals"],
      "source_file": "output_prediction/exercise_1_print_basics.py"
    }
  ]
}
```

**Purpose:** Lists all exercises in the module with metadata for the app.

---

### 3. `hints.json` (Per Module - TODO)

Will contain hints for each exercise:

```json
{
  "module_0_basics.output_prediction.exercise_1_print_basics": {
    "hints": [
      "Look at what's inside the quotes",
      "Remember: print() displays exactly what you tell it"
    ]
  }
}
```

---

## Exercise Types

| Type | Category | Description |
|------|----------|-------------|
| `output_prediction` | reading | Predict what code prints |
| `match_output` | reading | Match code to output |
| `fill_blanks` | scaffolded_writing | Complete code with blanks |
| `code_ordering` | scaffolded_writing | Arrange scrambled lines |
| `complete_function` | scaffolded_writing | Finish function bodies |
| `spot_difference` | analysis | Find differences in similar code |
| `decode_error` | debugging | Interpret error messages |
| `bug_hunt` | debugging | Find and fix bugs |
| `fix_style` | improvement | Improve code style |
| `write_code` | free_writing | Write code from scratch |
| `hybrid` | integration | Multi-part narrative exercises |

---

## Exercise ID Format

```
{module}.{exercise_type}.{filename_without_extension}
```

Examples:
- `module_0_basics.output_prediction.exercise_1_print_basics`
- `module_0_basics.hybrid.exercise_1_apprentice_variables`

---

## Difficulty Scale

| Level | Name (EN) | Name (HE) | Description |
|-------|-----------|-----------|-------------|
| 1 | Easy | קל | Single concept, obvious |
| 2 | Medium | בינוני | Combines 2 concepts |
| 3 | Challenging | מאתגר | Multiple steps |
| 4 | Hard | קשה | Requires synthesis |
| 5 | Advanced | מתקדם | Integration/capstone |

---

## Theme Support

All exercises use `{{placeholder}}` syntax for theming:

- `{{hero}}` - Main character name
- `{{school}}` - Location name
- `{{item}}` - Object name
- `{{greeting}}` - Greeting message

Theme mappings are in `theme_mappings/*.json`.

---

## Hybrid Exercises

Hybrid exercises combine multiple exercise types in a narrative arc.

### Arc: The Apprentice

| Part | Beat | Exercise Type |
|------|------|---------------|
| 1 | DISCOVERY | output_prediction |
| 2 | GUIDANCE | fill_blanks / complete_function |
| 3 | GROWTH | write_code |

Hybrid exercises have extra fields:
```json
{
  "arc": "apprentice",
  "parts": ["DISCOVERY", "GUIDANCE", "GROWTH"]
}
```

---

## App Integration

The app should:

1. Load `exercises_config.json` for global config
2. Load `{module}/exercises.json` for exercise list
3. Load `{module}/{source_file}` for starter code
4. Load `{module}/hints.json` for hints (when available)
5. Apply theme from selected `theme_mappings/*.json`

---

## Migration Notes

### From Old Structure
- Old exercises are in `archive/raw_exercises_old/`
- New exercises are in `raw_exercises_new/`
- The old `convert_exercises.py` script is being replaced

### What's New
1. Per-module `exercises.json` manifest
2. Simplified `exercises_config.json`
3. Exercise types organized into subdirectories
4. Hybrid exercises for multi-part narratives
5. Separate hints file (TODO)

---

## Next Steps

1. [ ] Create `hints.json` for module_0_basics
2. [ ] Update app to read new structure
3. [ ] Migrate remaining modules
4. [ ] Update convert script if needed
