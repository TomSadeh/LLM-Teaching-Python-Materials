# LLM Teaching Python Materials

Teaching materials for Maya's Magic Coding Chat - Python exercises and LLM prompt fragments.

## Purpose

This repository serves as a remote content source for the Maya Chat teaching app. The app can sync exercises and prompt updates from this repo using its remote sync API.

## Structure

```
├── version.json           # Version tracking for sync
├── manifest.json          # Lists all modules for remote discovery
├── exercises_config.json  # Module metadata and i18n translations
├── prompts.json           # LLM prompt fragments (for remote sync)
├── exercises/         # Per-module exercises with their own exercises.json
│   ├── module_0_basics/
│   ├── module_1_turtle_loops/
│   ├── module_2_decisions/
│   ├── module_3_lists/
│   ├── module_4_games/
│   ├── module_5_functions/
│   ├── module_6_mid_project/
│   ├── module_7_dictionaries/
│   ├── module_8_modules/
│   └── module_9_oop/
└── scripts/
    ├── convert_exercises.py        # Regenerate exercises.json from raw files
    ├── convert_to_templates.py     # Convert exercises to universal template system
    └── build_lessons_json.py       # Build lessons.json from lesson files
```

## Modules

| Module | Topic | Difficulty | Exercises |
|--------|-------|------------|-----------|
| module_0_basics | Print, variables, input | 1 | 18 |
| module_1_turtle_loops | Turtle graphics, for loops | 1 | 10 |
| module_2_decisions | If/else conditions | 2 | 9 |
| module_3_lists | Lists and iteration | 2 | 9 |
| module_4_games | While loops, game logic | 2 | 9 |
| module_5_functions | Functions | 3 | 9 |
| module_6_mid_project | Mid projects | 3 | 3 |
| module_7_dictionaries | Dictionaries | 2 | 9 |
| module_8_modules | Standard library modules | 3 | 9 |
| module_9_oop | Object-oriented programming | 3 | 9 |

**Total: 94 exercises**

## Syncing to Maya Chat

Configure the app to sync from this repo:

```bash
# Set the remote source (use raw GitHub URL)
curl -X PUT http://localhost:8765/api/sync/remote/config \
  -H "Content-Type: application/json" \
  -d '{
    "source_type": "github",
    "source_url": "https://raw.githubusercontent.com/TomSadeh/LLM-Teaching-Python-Materials/main"
  }'

# Check for updates
curl -X POST http://localhost:8765/api/sync/remote/check

# Pull updates
curl -X POST http://localhost:8765/api/sync/remote/pull
```

## Exercise JSON Format

Each exercise in `exercises.json` has this structure:

```json
{
  "id": "module_0_basics.exercise_01_hello",
  "topic_id": "basics.print",
  "title": "Hello",
  "title_he": "שלום עולם",
  "description_he": "יסודות: שלום עולם\n\nExercise 1: Hello World and Print",
  "difficulty": 1,
  "starter_code": "# Exercise 1: Hello World...",
  "solution_code": null,
  "hints": [],
  "tags": "module_0_basics",
  "source_file": "module_0_basics/exercise_01_hello.py"
}
```

## Prompt Fragments

Add prompt fragments to `prompts.json` to inject additional teaching instructions:

```json
{
  "version": "1.0.0",
  "prompts": [
    {
      "id": "custom-rule",
      "name": "Custom Teaching Rule",
      "content": "# Additional instruction for the LLM...",
      "priority": 50,
      "is_active": true
    }
  ]
}
```

## Regenerating exercises.json

If you modify the raw exercise files:

```bash
python scripts/convert_exercises.py exercises
```

Then update the version in `version.json` and commit.

## Converting to Universal Templates

To convert exercises from hardcoded themes to universal template system:

```bash
# Analyze a single exercise
python scripts/convert_to_templates.py --input exercises/module_7_dictionaries/complete_function/exercise_1.py --dry-run

# Convert an entire module
python scripts/convert_to_templates.py --module 7 --dry-run --report-dir conversion_reports

# Analyze all exercises
python scripts/convert_to_templates.py --all --dry-run --report-dir conversion_reports
```

The conversion script:
- Matches exercises to appropriate narrative templates
- Detects hardcoded theme references (Harry Potter, etc.)
- Extracts narrative context for templatization
- Generates JSON reports with conversion analysis
- Supports batch processing across all 145 exercises

See `docs/CONVERSION_SCRIPT_FINAL.md` for complete documentation.

## Language

- Exercise comments and descriptions: Hebrew
- Code and variable names: English
- Target audience: Hebrew-speaking students learning Python
