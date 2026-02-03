# Theme Placeholder Audit - Handoff Document

## Problem Statement

Exercises contain hardcoded fantasy/RPG-specific terms that don't work across all themes (e.g., "cave", "traps", "mana", "sword", "dungeon"). A soccer or professional coding theme would render these narratives nonsensical.

## What Was Completed

### New Placeholders Added to All 6 Themes

**Rivalry/Narrative Blocks:**
| Placeholder | Purpose |
|-------------|---------|
| `{{CONTEXT_SETBACK_INTRO}}` | Opening for setback/defeat scenario |
| `{{CONTEXT_SETBACK_NARRATIVE}}` | Story explaining the defeat |
| `{{CONTEXT_CONFRONTATION_INTRO}}` | Opening for final confrontation |
| `{{CONTEXT_CONFRONTATION_NARRATIVE}}` | Climactic showdown narrative |

**Dangers & Conditions:**
| Placeholder | Purpose | Example Values |
|-------------|---------|----------------|
| `{{obstacle}}` | Things that block progress | trap, force field, error |
| `{{danger_location}}` | Risky places to enter | dark cave, danger zone, untested code |
| `{{harmful_status}}` | Negative conditions | poisoned, injured, flagged |
| `{{busy_activity}}` | Activities preventing rest | in combat, on mission, processing |

**Game Stats & Actions:**
| Placeholder | Purpose | Example Values |
|-------------|---------|----------------|
| `{{primary_stat}}` | Main resource | health, stamina, progress |
| `{{secondary_stat}}` | Secondary resource | mana, energy, resources |
| `{{retreat_action}}` | Escape action | flee, retreat, cancel |
| `{{basic_action}}` | Simple action | basic attack, defend, try again |

### Exercises Already Fixed

| File | Changes Made |
|------|--------------|
| `module_2_decisions/bug_hunt/exercise_1_boolean_bugs.py` | cave/traps → `{{danger_location}}`/`{{obstacle}}`, poison/combat → `{{harmful_status}}`/`{{busy_activity}}` |
| `module_2_decisions/bug_hunt/exercise_3_nested_bugs.py` | health/mana → generic `primary`/`secondary` variables with stat placeholders |
| `module_2_decisions/write_code/exercise_5_boolean_operators.py` | battle/mana → generic terms with placeholders |
| `module_2_decisions/code_tracing/exercise_3_boolean_trace.py` | dungeon → `{{danger_location}}`, potion → `{{item}}` |
| `module_2_decisions/hybrid/exercise_3_mystery_boolean.py` | sword/bow/arrows → generic `has_primary`/`has_backup`/`has_supplies` |
| `module_2_decisions/hybrid/exercise_4_rivalry_challenge.py` | health/mana → stat placeholders, Retreat → `{{retreat_action}}` |
| `module_5_games/hybrid/exercise_1_rivalry_showdown.py` | Uses new CONTEXT_SETBACK/CONFRONTATION placeholders |

### Documentation Updated

- `theme_mappings/_TEMPLATE.json` - All new placeholder definitions
- `TEMPLATE.md` - New sections for Dangers & Conditions, Game Stats & Actions, Rivalry/Showdown Blocks

---

## Remaining Work

### High Priority - Fantasy-Specific Terms Still Present

Run this search to find remaining issues:
```bash
grep -rn --include="*.py" -E "\b(cave|trap|poison|mana|combat|battle|flee|dungeon|sword|shield|potion|knight|dragon|castle|wizard|magic)\b" exercises/
```

### Known Files Needing Review

Based on the audit, these files likely have issues:

**module_0_basics:**
- `complete_function/exercise_1_format_output.py` - Uses "Knight", "HP"
- `hybrid/exercise_2_apprentice_program.py` - Uses "Wizard", "Combat Rating", "Magic Power"

**module_2_decisions:**
- `code_tracing/exercise_1_if_else_trace.py` - "drinks potion"

**module_3_lists:**
- Multiple files use "potion", "key", "map", "coin" as list data - **These are ACCEPTABLE** as generic item examples for teaching list operations

**module_6_final_project:**
- `hybrid/exercise_1_character_system.py` - "Simulate battle"
- `hybrid/exercise_3_collection_manager.py` - "potion" in examples
- `hybrid/exercise_4_text_adventure.py` - "Finding a potion"

---

## How to Fix an Exercise

### Step 1: Identify the Problem
Look for:
- Fantasy terms in comments/docstrings (narrative context)
- Fantasy terms in print statements
- Fantasy-specific variable names (less critical, but rename if obvious like `mana`)

### Step 2: Choose Replacement Strategy

**For narrative text (comments, print statements):**
- Use existing placeholders: `{{hero}}`, `{{villain}}`, `{{item}}`, `{{location}}`, etc.
- Use new placeholders: `{{danger_location}}`, `{{obstacle}}`, `{{primary_stat}}`, etc.

**For variable names:**
- Use generic programming terms: `value`, `score`, `stat_value`, `resource`
- Or generic game terms: `primary`, `secondary`, `is_busy`, `is_harmed`
- Keep them readable and educational

**For list data ("potion", "key", "map"):**
- These are generally ACCEPTABLE as they're teaching data structures
- Only replace if used in narrative context

### Step 3: Apply Consistent Patterns

**Pattern for stat-based logic:**
```python
# Before (fantasy-specific)
if health < 30 and mana < 20:
    print("{{hero}} flees!")

# After (theme-agnostic)
if primary < 30 and secondary < 20:
    print("{{hero}} must {{retreat_action}}!")
```

**Pattern for danger/location checks:**
```python
# Before
print("{{hero}} enters the cave!")

# After
print("{{hero}} enters {{danger_location}}!")
```

---

## Testing Changes

After making changes:
1. Verify placeholders are valid by checking against `theme_mappings/_TEMPLATE.json`
2. Run the audit script: `python scripts/audit_all_themes.py exercises/`
3. Test with multiple themes mentally to ensure it reads naturally

---

## Files Reference

| File | Purpose |
|------|---------|
| `theme_mappings/_TEMPLATE.json` | Full placeholder reference |
| `TEMPLATE.md` | Quick placeholder guide |
| `themes/*.json` | Theme-specific values for each placeholder |

---

## Notes

- "potion", "key", "map", "coin" as list items are fine - they're just example data
- Variable names don't need placeholders (can't have `{{}}` in Python identifiers)
- Focus on fixing narrative/display text, not code structure
- Some generic terms like "level", "score", "gold" work across most themes
