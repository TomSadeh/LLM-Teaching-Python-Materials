# Companion Repo Handoff: Required Changes

This document describes what changes need to be made in the `LLM-Teaching-Python-Materials` companion repository to work with the updated sync system in maya-chat.

## Summary of Changes in maya-chat

The sync system has been updated to be more robust:

1. **Module metadata is now stored in the database** instead of a local JSON file
2. **Lessons are now included in the sync button** (previously only exercises/prompts)
3. **All content comes from the companion repo** - no local config files that can get stale

## Required File: `exercises_config.json`

The companion repo must have an `exercises_config.json` at the root with this structure:

```json
{
  "version": "1.0.0",
  "modules": {
    "module_0_basics": {
      "name_en": "Python Basics",
      "name_he": "יסודות פייתון",
      "description_en": "Print, variables, input",
      "description_he": "הדפסה, משתנים, קלט",
      "topic_id": "basics.print",
      "difficulty": 1,
      "order_index": 0
    },
    "module_1_turtle_loops": {
      "name_en": "Turtle Graphics & Loops",
      "name_he": "גרפיקת צב ולולאות",
      "description_en": "Drawing with turtle, for loops",
      "description_he": "ציור עם צב, לולאות for",
      "topic_id": "turtle.basics",
      "difficulty": 1,
      "order_index": 1
    },
    "module_2_decisions": {
      "name_en": "Decisions",
      "name_he": "החלטות",
      "description_en": "If/else conditions",
      "description_he": "תנאים if/else",
      "topic_id": "conditions.if",
      "difficulty": 2,
      "order_index": 2
    },
    "module_3_lists": {
      "name_en": "Lists",
      "name_he": "רשימות",
      "description_en": "Lists and iteration",
      "description_he": "רשימות ואיטרציה",
      "topic_id": "lists.basics",
      "difficulty": 2,
      "order_index": 3
    },
    "module_4_games": {
      "name_en": "Game Logic",
      "name_he": "לוגיקת משחקים",
      "description_en": "While loops, game logic",
      "description_he": "לולאות while, לוגיקת משחקים",
      "topic_id": "loops.while",
      "difficulty": 2,
      "order_index": 4
    },
    "module_5_functions": {
      "name_en": "Functions",
      "name_he": "פונקציות",
      "description_en": "Defining and using functions",
      "description_he": "הגדרה ושימוש בפונקציות",
      "topic_id": "functions.basics",
      "difficulty": 3,
      "order_index": 5
    },
    "module_6_final_project": {
      "name_en": "Final Projects",
      "name_he": "פרויקטים מסכמים",
      "description_en": "Putting it all together",
      "description_he": "שילוב הכל יחד",
      "topic_id": "projects.final",
      "difficulty": 3,
      "order_index": 6
    },
    "module_7_dictionaries": {
      "name_en": "Dictionaries",
      "name_he": "מילונים",
      "description_en": "Key-value data structures",
      "description_he": "מבני נתונים מפתח-ערך",
      "topic_id": "dictionaries.basics",
      "difficulty": 2,
      "order_index": 7
    },
    "module_8_modules": {
      "name_en": "Standard Library",
      "name_he": "ספריות סטנדרטיות",
      "description_en": "Using Python modules",
      "description_he": "שימוש במודולים של פייתון",
      "topic_id": "modules.stdlib",
      "difficulty": 3,
      "order_index": 8
    },
    "module_9_oop": {
      "name_en": "Object-Oriented Programming",
      "name_he": "תכנות מונחה עצמים",
      "description_en": "Classes and objects",
      "description_he": "מחלקות ואובייקטים",
      "topic_id": "oop.basics",
      "difficulty": 3,
      "order_index": 9
    },
    "free_practice": {
      "name_en": "Free Practice",
      "name_he": "תרגול חופשי",
      "description_en": "Open-ended practice",
      "description_he": "תרגול פתוח",
      "topic_id": "practice.free",
      "difficulty": 1,
      "order_index": -1
    }
  }
}
```

### Field Descriptions

| Field | Required | Description |
|-------|----------|-------------|
| `name_en` | Yes | English display name for the module |
| `name_he` | Yes | Hebrew display name for the module |
| `description_en` | No | English description |
| `description_he` | No | Hebrew description |
| `topic_id` | No | Associated topic ID (e.g., "basics.print") |
| `difficulty` | No | 1-3 difficulty level (default: 1) |
| `order_index` | No | Sort order for display (default: 0) |

## How the Sync Works

1. On startup, maya-chat checks for companion repo at `../LLM-Teaching-Python-Materials`
2. If found, it syncs in this order:
   - **Config** (`exercises_config.json`) → `modules` table in DB
   - **Lessons** (`lessons.json`) → `lessons` table in DB
   - **Exercises** (`raw_exercises/*/exercises.json`) → `exercises` table in DB

3. The frontend then fetches module display names from `/api/exercises/modules-config`, which reads from the database

## Checklist for Companion Repo

- [ ] Create `exercises_config.json` at repo root with all modules
- [ ] Ensure all module IDs match what's used in lessons and exercises
- [ ] Include both Hebrew and English names for every module
- [ ] Set correct `order_index` for proper sorting in the UI
- [ ] Bump the `version` field when making changes

## Testing the Sync

After making changes in the companion repo:

1. Restart the maya-chat backend (or use the sync button)
2. Check logs for: `Local modules sync: X added, Y updated`
3. Verify the lesson picker shows Hebrew module names
4. Verify exercises are grouped correctly by module

## Database Table: `modules`

The sync creates/updates this table in `content.db`:

```sql
CREATE TABLE modules (
    id TEXT PRIMARY KEY,           -- e.g., "module_0_basics"
    name_en TEXT NOT NULL,
    name_he TEXT NOT NULL,
    description_en TEXT,
    description_he TEXT,
    topic_id TEXT,
    difficulty INTEGER DEFAULT 1,
    order_index INTEGER DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```
