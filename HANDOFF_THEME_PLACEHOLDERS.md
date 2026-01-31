# Theme Placeholders System - Handoff Document

## Overview

This document describes the dynamic theming system for exercises. The `{{placeholder}}` syntax is replaced at runtime with theme-specific values (Harry Potter characters for dumblecode theme, Percy Jackson for chirthon, etc.)

## Current Status: Complete

### What's Been Done

1. **Created `replacements.json`** (v1.1.0)
   - Data-driven replacement patterns (no hardcoded values in code)
   - 362 total replacement patterns
   - Verified against `maya-chat/CLAUDE_HE.md` reference

2. **Updated `scripts/apply_theme_placeholders.py`**
   - Reads patterns from `replacements.json`
   - Supports `--raw` flag to process raw `.py` files
   - Supports `--all` flag for both raw files and exercises.json
   - Smart handling of short words (≤5 chars) to avoid partial replacements

3. **Updated 14 raw exercise files** with `{{placeholder}}` syntax

4. **Regenerated `exercises.json`** (v1.2.0) with `theme_support: true`

5. **Verification completed**: 0 hardcoded book references in Python exercise files

6. **Archived deprecated documentation** (Phase 2 - Jan 2026)
   - Moved all `README.md`, `README_HE.md`, `README_HE.html` from module folders
   - Moved all `instructions_he/` folders
   - Archived to `archive/deprecated_docs/` preserving module structure
   - 48 files total (7 English READMEs + 14 Hebrew READMEs + 27 instruction files)

7. **Updated theme_variables.json to use arrays** (Phase 3 - Jan 2026)
   - Both repos now use array format for variety
   - `maya-chat/data/theme_variables.json` - runtime source
   - `LLM-Teaching-Python-Materials/theme_variables.json` - repo copy

8. **Backend loads from JSON file** (Jan 2026)
   - `maya-chat/backend/services/theme_variables.py` now loads from `data/theme_variables.json`
   - No more hardcoded values in Python code
   - Includes `reload_theme_variables()` for hot-reload capability

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| `replacements.json` | `LLM-Teaching-Python-Materials/` | Pattern definitions for conversion |
| `apply_theme_placeholders.py` | `LLM-Teaching-Python-Materials/scripts/` | Replacement script |
| `exercises.json` | `LLM-Teaching-Python-Materials/` | Generated exercises with placeholders |
| `theme_variables.json` | `LLM-Teaching-Python-Materials/` | Runtime theme values (array format) |
| `theme_variables.json` | `maya-chat/data/` | Runtime theme values (backend source) |
| `theme_variables.py` | `maya-chat/backend/services/` | Backend replacement logic (loads from JSON) |
| `CLAUDE_HE.md` | `maya-chat/` | Authoritative reference for book terms |
| `archive/deprecated_docs/` | `LLM-Teaching-Python-Materials/` | Archived README and instruction files |

---

## How To Run

```bash
cd LLM-Teaching-Python-Materials

# Update raw .py files with placeholders
python scripts/apply_theme_placeholders.py --raw

# Regenerate exercises.json from raw files
python scripts/convert_exercises.py raw_exercises

# Update exercises.json version manually after regeneration:
# Change "version": "1.0.0" to "version": "1.2.0"
# Add "theme_support": true
```

---

## How Placeholders Work

### Available Placeholders

| Placeholder | Description | Example (dumblecode) |
|-------------|-------------|---------------------|
| `{{hero}}` | Male protagonist | Harry Potter |
| `{{heroine}}` | Female protagonist | Hermione Granger |
| `{{friend}}` | Sidekick/ally | Ron Weasley |
| `{{mentor}}` | Teacher/guide | Dumbledore |
| `{{villain}}` | Antagonist | Voldemort |
| `{{school}}` | Main institution | Hogwarts |
| `{{house}}` | Sub-group | Gryffindor |
| `{{location}}` | Adventure place | the Forbidden Forest |
| `{{place}}` | Famous location | Diagon Alley |
| `{{spell1}}` | Basic ability | Lumos |
| `{{spell2}}` | Combat ability | Expelliarmus |
| `{{spell3}}` | Advanced ability | Expecto Patronum |
| `{{spell4}}` | Utility ability | Wingardium Leviosa |
| `{{creature}}` | Magical creature | hippogriff |
| `{{pet}}` | Character's pet | Hedwig the owl |
| `{{item}}` | Special object | wand |
| `{{group}}` | Organization | Dumbledore's Army |
| `{{exclamation}}` | Themed phrase | By Merlin's beard! |
| `{{greeting}}` | Welcome message | Welcome to Hogwarts! |
| `{{password}}` | Secret code | Caput Draconis |

### Runtime Replacement

The backend (`maya-chat/backend/services/theme_variables.py`) replaces placeholders when:
1. Fetching current exercise (`/api/exercises/current`)
2. Loading exercise to editor (`/api/exercises/{id}/load`)

The frontend passes the current theme from `useThemeStore`.

### Array Support

Each placeholder maps to an **array of values** for variety:
```json
"dumblecode": {
  "hero": ["Harry Potter", "Ron Weasley", "Neville Longbottom"],
  "heroine": ["Hermione Granger", "Luna Lovegood", "Ginny Weasley"],
  ...
}
```

The backend randomly selects from the array, with `consistent=True` ensuring the same placeholder gets the same value throughout a single exercise.

---

## Testing Checklist

- [x] Backend starts without errors
- [x] Sync pulls exercises (not duplicates) - check `source_id` matching
- [x] Exercise panel shows themed content
- [x] Loading exercise to editor applies theme
- [x] Changing theme changes displayed exercise content
- [x] All exercises render properly (no broken `{{` syntax)
- [x] Backend loads theme variables from JSON file
- [x] Multiple values per placeholder provide variety

---

## Reference Files

- **Authoritative source:** `maya-chat/CLAUDE_HE.md` - Contains verified Hebrew and English names from all 4 book series
- **Pattern definitions:** `LLM-Teaching-Python-Materials/replacements.json`
- **Runtime values:** `maya-chat/data/theme_variables.json`

When adding new terms, always verify spelling against CLAUDE_HE.md first.
