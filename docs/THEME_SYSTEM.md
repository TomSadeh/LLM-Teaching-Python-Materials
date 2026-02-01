# Theme System Architecture

This document explains how the universal theme system works across fantasy, sci-fi, and plain themes.

## Overview

The theme system uses **placeholder variables** (`{{variable}}`) in exercises that get replaced at runtime with theme-specific values. This allows the same exercise to work in Harry Potter's Hogwarts, a D&D dungeon, a spaceship, or a plain coding context.

## Theme Categories

### Commercial Themes (Open License)
These themes use free-to-commercialize IP and ship with the app:

| Theme ID | Setting | License | Description |
|----------|---------|---------|-------------|
| `dnd-srd` | D&D Fantasy | CC-BY-4.0 | Classic fantasy with adventurers, dungeons, magic |
| `cepheus` | Space Opera | OGL | Sci-fi exploration, ships, technology levels |
| `pymentor` | Plain | N/A | No fantasy/sci-fi, just programming concepts |

### Test-Only Themes (Proprietary IP)
These themes are for internal testing and generalization validation only:

| Theme ID | Setting | IP Owner | Purpose |
|----------|---------|----------|---------|
| `dumblecode` | Harry Potter | Warner Bros | Validate fantasy patterns |
| `chirthon` | Percy Jackson | Disney | Validate mythology patterns |
| `compile-games` | Hunger Games | Lionsgate | Validate dystopian patterns |
| `pyfire` | Keeper of Lost Cities | Simon & Schuster | Validate telepathy/school patterns |

## Universal Placeholder System

### Character Roles

| Placeholder | Fantasy Example | Sci-Fi Example | Plain Example |
|-------------|-----------------|----------------|---------------|
| `{{hero}}` | the fighter | the pilot | the programmer |
| `{{heroine}}` | the wizard | the scientist | the engineer |
| `{{friend}}` | party member | crewmate | coding buddy |
| `{{mentor}}` | archmage | captain | instructor |
| `{{villain}}` | dragon | pirate lord | bugs |

### Location Categories

| Placeholder | Fantasy Example | Sci-Fi Example | Plain Example |
|-------------|-----------------|----------------|---------------|
| `{{school}}` | Adventurers Guild | Naval Academy | Code Academy |
| `{{house}}` | Fighters Guild | Scout Service | the lab |
| `{{location}}` | the dungeon | the cargo bay | the IDE |
| `{{place}}` | Waterdeep | starport | GitHub |

### Action/Ability Categories

| Placeholder | Fantasy Example | Sci-Fi Example | Plain Example |
|-------------|-----------------|----------------|---------------|
| `{{spell1}}` | Light | sensor scan | coding |
| `{{spell2}}` | Fireball | weapons lock | debugging |
| `{{spell3}}` | Teleport | hyperspace jump | problem solving |
| `{{spell4}}` | Levitate | auto-pilot | refactoring |

### Object Categories

| Placeholder | Fantasy Example | Sci-Fi Example | Plain Example |
|-------------|-----------------|----------------|---------------|
| `{{creature}}` | owlbear | space squid | robot |
| `{{pet}}` | wizard's familiar | ship's cat | helpful robot |
| `{{item}}` | healing potion | datapad | keyboard |
| `{{transport}}` | griffon | scout ship | the internet |

### Narrative Elements

| Placeholder | Fantasy Example | Sci-Fi Example | Plain Example |
|-------------|-----------------|----------------|---------------|
| `{{group}}` | adventuring party | the crew | dev team |
| `{{exclamation}}` | By the gods! | By the stars! | Eureka! |
| `{{greeting}}` | Welcome, adventurer | Welcome aboard | Welcome to coding |
| `{{password}}` | friend | alpha-one | python |

## Example Exercise Across Themes

### Template (with placeholders)
```python
def exercise_inventory():
    """Manage {{hero}}'s inventory."""
    inventory = {}

    def add_item(item, quantity):
        inventory[item] = inventory.get(item, 0) + quantity
        print(f"Added {quantity} {item} to inventory.")

    def use_item(item):
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
            print(f"{{hero}} used {item}! {{exclamation}}")
        else:
            print(f"No {item} available.")

    # Example usage
    add_item("{{item}}", 3)
    use_item("{{item}}")
```

### Rendered in D&D Theme (`dnd-srd`)
```python
def exercise_inventory():
    """Manage the fighter's inventory."""
    inventory = {}

    def add_item(item, quantity):
        inventory[item] = inventory.get(item, 0) + quantity
        print(f"Added {quantity} {item} to inventory.")

    def use_item(item):
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
            print(f"the fighter used {item}! By the gods!")
        else:
            print(f"No {item} available.")

    # Example usage
    add_item("healing potion", 3)
    use_item("healing potion")
```

### Rendered in Cepheus Theme (`cepheus`)
```python
def exercise_inventory():
    """Manage the pilot's inventory."""
    inventory = {}

    def add_item(item, quantity):
        inventory[item] = inventory.get(item, 0) + quantity
        print(f"Added {quantity} {item} to inventory.")

    def use_item(item):
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
            print(f"the pilot used {item}! By the stars!")
        else:
            print(f"No {item} available.")

    # Example usage
    add_item("datapad", 3)
    use_item("datapad")
```

### Rendered in Plain Theme (`pymentor`)
```python
def exercise_inventory():
    """Manage the programmer's inventory."""
    inventory = {}

    def add_item(item, quantity):
        inventory[item] = inventory.get(item, 0) + quantity
        print(f"Added {quantity} {item} to inventory.")

    def use_item(item):
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
            print(f"the programmer used {item}! Eureka!")
        else:
            print(f"No {item} available.")

    # Example usage
    add_item("keyboard", 3)
    use_item("keyboard")
```

## Design Principles

### 1. Theme-Agnostic Archetypes
Every exercise is based on a **universal narrative archetype** (see `NARRATIVE_ARCHETYPES.md`) that works regardless of theme:
- Inventory Management works for potions, ship cargo, or supplies
- Random Assignment works for houses, crew positions, or teams
- Character Creation works for adventurers, officers, or profiles

### 2. Semantic Consistency
Placeholders map to **semantic roles**, not specific objects:
- `{{item}}` = useful object (potion, datapad, tool)
- `{{transport}}` = means of travel (griffon, ship, internet)
- `{{spell1}}` = basic action/ability

### 3. Multiple Options Per Theme
Each theme provides **arrays of options** for variety:
```json
"hero": ["the fighter", "the ranger", "the paladin", "the monk", "the barbarian"]
```
The system randomly picks one to keep content fresh.

### 4. Fallback to Plain
If a student disables fantasy themes, all exercises fall back to `pymentor` (plain) theme automatically.

## Testing Themes

### Validation Script
```bash
# Check for hardcoded theme references
python scripts/apply_theme_placeholders.py --raw --check

# Convert existing exercises to use placeholders
python scripts/convert_to_templates.py --all --dry-run
```

### Cross-Theme Testing Strategy
1. **Primary test**: D&D SRD (commercial fantasy)
2. **Secondary test**: Cepheus (commercial sci-fi)
3. **Fallback test**: PyMentor (plain)
4. **Validation tests**: Proprietary themes (Harry Potter, Percy Jackson, etc.)

This ensures exercises work in:
- ✅ Fantasy settings
- ✅ Sci-fi settings
- ✅ No-theme settings
- ✅ Various narrative styles

## Adding New Themes

To add a new theme:

1. **Add to `theme_variables.json`:**
```json
"new-theme-id": {
  "hero": [...],
  "heroine": [...],
  // ... all 23 placeholders
}
```

2. **Update `TEMPLATE.md`** with theme description

3. **Test with validation script:**
```bash
python scripts/apply_theme_placeholders.py --theme new-theme-id --check
```

4. **Mark as commercial or test-only** in documentation

## Theme Distribution Strategy

### For Maya Chat (Educational App)
**Ship these themes:**
- `dnd-srd` (fantasy)
- `cepheus` (sci-fi)
- `pymentor` (plain)

**Keep internal only:**
- `dumblecode`, `chirthon`, `compile-games`, `pyfire` (proprietary IP)

### For Other Projects
Can safely ship any theme using:
- D&D SRD 5.1/5.2 (CC-BY-4.0)
- Cepheus Engine (OGL)
- Public domain IP (Wizard of Oz, Alice in Wonderland, etc.)

## Architecture Benefits

1. **Content reuse**: Write once, works in any theme
2. **Easy localization**: Theme variables can be translated
3. **Legal safety**: Clear separation between free and proprietary IP
4. **Testing flexibility**: Validate with familiar IP, ship with open IP
5. **Student choice**: Let students pick their preferred setting

## Next Steps

1. ✅ Add D&D SRD theme (completed)
2. ✅ Add Cepheus Engine theme (completed)
3. 🔲 Update maya-chat app to load new themes
4. 🔲 Create theme prompt files in `prompts/themes/`
5. 🔲 Test all exercises in new themes
6. 🔲 Remove hardcoded references from legacy exercises
