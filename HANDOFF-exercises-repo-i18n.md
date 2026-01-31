# Exercises Repository i18n Handoff

> **Status: COMPLETE** - All i18n support has been implemented.

This document describes the changes needed in the **LLM-Teaching-Python-Materials** repository to support multi-language content.

## Overview

The maya-chat app now supports multiple languages (Hebrew and English). The exercises repository needs to provide translations for:

1. **Module names** (currently only `name_he`)
2. **Exercise titles** (currently only `title_he`)
3. **Exercise descriptions** (currently only `description_he`)

## Required Changes

### 1. Update `exercises_config.json`

Add English names to each module:

```json
{
  "modules": {
    "module_0_basics": {
      "topic_id": "basics.print",
      "difficulty": 1,
      "name_he": "יסודות",
      "name_en": "Basics"
    },
    "module_1_turtle_loops": {
      "topic_id": "loops.for",
      "difficulty": 1,
      "name_he": "צב ולולאות",
      "name_en": "Turtle & Loops"
    },
    "module_2_decisions": {
      "topic_id": "control.if",
      "difficulty": 2,
      "name_he": "תנאים והחלטות",
      "name_en": "Conditions & Decisions"
    },
    "module_3_lists": {
      "topic_id": "collections.lists",
      "difficulty": 2,
      "name_he": "רשימות",
      "name_en": "Lists"
    },
    "module_4_games": {
      "topic_id": "loops.while",
      "difficulty": 2,
      "name_he": "משחקים",
      "name_en": "Games"
    },
    "module_5_functions": {
      "topic_id": "functions.basic",
      "difficulty": 3,
      "name_he": "פונקציות",
      "name_en": "Functions"
    },
    "module_6_final_project": {
      "topic_id": "project.final",
      "difficulty": 3,
      "name_he": "פרויקט מסכם",
      "name_en": "Final Project"
    }
  },
  "title_translations": {
    "hello": {
      "he": "שלום עולם",
      "en": "Hello World"
    },
    "variables": {
      "he": "משתנים",
      "en": "Variables"
    }
    // ... etc for all titles
  }
}
```

### 2. Update Exercise JSON Format

Each exercise should have both Hebrew and English fields:

**Current format:**
```json
{
  "id": "module_0_basics.exercise_01_hello",
  "title": "module_0_basics/exercise_01_hello.py",
  "title_he": "שלום עולם",
  "description_he": "יסודות: שלום עולם\n\nExercise 1: Hello World and Print"
}
```

**New format:**
```json
{
  "id": "module_0_basics.exercise_01_hello",
  "title": "module_0_basics/exercise_01_hello.py",
  "title_he": "שלום עולם",
  "title_en": "Hello World",
  "description_he": "יסודות: שלום עולם\n\nתרגיל 1: הדפסה ושלום עולם",
  "description_en": "Basics: Hello World\n\nExercise 1: Hello World and Print"
}
```

### 3. Version File Update

Update `version.json` to indicate i18n support:

```json
{
  "exercises": "2.0.0",
  "prompts": "1.0.5",
  "i18n_supported": true,
  "languages": ["he", "en"]
}
```

## Migration Strategy

### Phase 1: Backward Compatible
Add `_en` fields alongside existing `_he` fields. The app will fall back to Hebrew if English is missing.

### Phase 2: Full Translation
Translate all content to English. The app already handles missing translations gracefully.

## App-Side Integration

The maya-chat app:
- Stores language preference in `settingsStore` (`language: 'he' | 'en'`)
- Falls back to Hebrew if translation is missing
- Uses `languageConfig` for RTL/LTR direction

### How the App Will Use This

```typescript
// In ExercisePanel or similar
const { language } = useTranslation();
const moduleName = module[`name_${language}`] || module.name_he;
const exerciseTitle = exercise[`title_${language}`] || exercise.title_he;
```

## Testing

After updating the exercises repo:
1. Run sync in the app
2. Switch language to English in settings
3. Verify module names and exercise titles display in English
4. Switch back to Hebrew to verify nothing broke

## Files to Update in LLM-Teaching-Python-Materials

### ✅ COMPLETED
1. `exercises_config.json` - Created with full i18n support:
   - 10 modules with `name_he`/`name_en` and descriptions
   - 90+ title translations (he/en)
   - Topic translations (17 topics)
   - Difficulty level translations
   - UI labels in both languages

2. `raw_exercises/*/exercises.json` - Added `title_en`, `description_en` to all 94 exercises
   - Updated `scripts/convert_exercises.py` with `MODULE_NAMES_EN` and `TITLE_EN_MAP`
   - Regenerated all module exercise JSON files

3. `version.json` - Bumped to version 2.0.0 with i18n metadata:
   - `i18n_supported: true`
   - `languages: ["he", "en"]`

## Notes

- The exercise **starter_code** and **solution_code** remain in English (Python code)
- Theme-specific content (sync messages, etc.) is handled in maya-chat's `he.json`/`en.json`
- Hints could optionally be translated but are lower priority
