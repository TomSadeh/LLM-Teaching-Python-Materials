# Theme System Architecture

This document explains how the three-layer universal theme system works across fantasy, sci-fi, and plain coding themes.

## Overview

The theme system uses **placeholder variables** (`{{variable}}`) in exercises that get replaced at runtime with theme-specific values. This allows the same exercise to work in any setting - a magical academy, a starship, or a plain coding environment.

**Key principle:** The Python code is identical. Only the narrative context changes.

## Three-Layer Architecture

| Layer | Purpose | Example |
|-------|---------|---------|
| **Layer 1** | Entity names (nouns) | `{{hero}}` → "Harry Potter" / "Captain Nova" |
| **Layer 2** | Context blocks (sentences) | `{{CONTEXT_INTRO}}` → "Welcome to Hogwarts!" |
| **Layer 3** | Framework concepts | `{{ABILITY_TYPE}}` → "magic" / "engineering" |

### Layer 1: Entity Names

Simple noun replacements. Used throughout exercise code.

```python
name = "{{hero}}"      # → "Harry Potter" / "Captain Nova" / "Alex"
school = "{{school}}"  # → "Hogwarts" / "Starship Academy" / "Code Academy"
```

### Layer 2: Context Blocks

Full sentences that provide narrative framing. Used for introductions, instructions, and feedback.

```python
# {{CONTEXT_INTRO}}
# → "Welcome to Hogwarts! Your magical education continues..."
# → "Welcome aboard, Cadet! All crew must complete training..."
# → "Let's build this step by step."
```

### Layer 3: Framework Concepts

Structural terms that define how the universe works. Used sparingly in meta-descriptions.

```python
# As a {{PRACTITIONER_SINGULAR}}, you'll learn {{ABILITY_TYPE}}
# → "As a wizard, you'll learn magic"
# → "As an engineer, you'll learn engineering"
```

---

## Theme Categories

### Commercial Themes (Open License)

These themes use free-to-commercialize IP and ship with the app:

| Theme ID | Setting | License | Description |
|----------|---------|---------|-------------|
| `dnd-srd` | D&D Fantasy | CC-BY-4.0 | Classic fantasy with adventurers, dungeons, magic |
| `cepheus` | Space Opera | OGL | Sci-fi exploration, ships, technology |
| `pymentor` | Plain | N/A | No fantasy/sci-fi, just programming concepts |

### Test-Only Themes (Proprietary IP)

These themes are for internal testing and generalization validation only:

| Theme ID | Setting | IP Owner | Purpose |
|----------|---------|----------|---------|
| `dumblecode` | Harry Potter | Warner Bros | Validate fantasy patterns |
| `chirthon` | Percy Jackson | Disney | Validate mythology patterns |
| `compile-games` | Hunger Games | Lionsgate | Validate dystopian patterns |
| `pyfire` | Keeper of Lost Cities | Simon & Schuster | Validate school patterns |

---

## Theme File Structure

Theme definitions live in `theme_mappings/`:

```
theme_mappings/
├── _TEMPLATE.json              # Complete placeholder reference
├── _EXAMPLE_fantasy_complete.json  # Full example theme
├── THEME_CREATOR_GUIDE.md      # Documentation for theme creators
├── fantasy_magic.json          # Fantasy theme
├── scifi_engineering.json      # Sci-fi theme
├── professional_coding.json    # Plain coding theme
└── [other themes].json
```

Each theme file contains all three layers:

```json
{
  "theme_id": "fantasy_magic",
  "theme_name": "Fantasy Magic Academy",

  "layer_1_entities": {
    "hero": ["Harry Potter", "Ron Weasley"],
    "school": ["Hogwarts"],
    ...
  },

  "layer_2_universal": {
    "ROLE_TITLE": "Wizard",
    "COMPONENT_SINGULAR": "spell",
    ...
  },

  "layer_2_context_blocks": {
    "introduction": {
      "CONTEXT_INTRO": "Welcome to {{school}}!",
      ...
    }
  },

  "layer_3_framework": {
    "ABILITY_TYPE": "magic",
    ...
  }
}
```

---

## Layer 1 Placeholder Reference

### Character Roles

| Placeholder | Fantasy | Sci-Fi | Plain |
|-------------|---------|--------|-------|
| `{{hero}}` | the fighter | the pilot | the programmer |
| `{{heroine}}` | the wizard | the scientist | the engineer |
| `{{friend}}` | party member | crewmate | coding buddy |
| `{{mentor}}` | archmage | captain | instructor |
| `{{villain}}` | dragon | pirate lord | bugs |

### Locations

| Placeholder | Fantasy | Sci-Fi | Plain |
|-------------|---------|--------|-------|
| `{{school}}` | Adventurers Guild | Naval Academy | Code Academy |
| `{{house}}` | Fighters Guild | Scout Service | the lab |
| `{{location}}` | the dungeon | the cargo bay | the IDE |
| `{{place}}` | Waterdeep | starport | GitHub |

### Abilities

| Placeholder | Fantasy | Sci-Fi | Plain |
|-------------|---------|--------|-------|
| `{{spell1}}` | Light | sensor scan | coding |
| `{{spell2}}` | Fireball | weapons lock | debugging |
| `{{spell3}}` | Teleport | hyperspace jump | problem solving |
| `{{spell4}}` | Levitate | auto-pilot | refactoring |

### Objects

| Placeholder | Fantasy | Sci-Fi | Plain |
|-------------|---------|--------|-------|
| `{{creature}}` | owlbear | space squid | robot |
| `{{pet}}` | wizard's familiar | ship's cat | helpful robot |
| `{{item}}` | healing potion | datapad | keyboard |
| `{{transport}}` | griffon | scout ship | the internet |

### Phrases

| Placeholder | Fantasy | Sci-Fi | Plain |
|-------------|---------|--------|-------|
| `{{group}}` | adventuring party | the crew | dev team |
| `{{exclamation}}` | By the gods! | By the stars! | Eureka! |
| `{{greeting}}` | Welcome, adventurer | Welcome aboard | Welcome |
| `{{password}}` | friend | alpha-one | password |

---

## Layer 2 Context Block Reference

### Introduction Blocks

| Placeholder | Purpose |
|-------------|---------|
| `{{CONTEXT_INTRO}}` | Generic exercise opening |
| `{{CONTEXT_PROJECT_INTRO}}` | Incremental builder exercises |
| `{{CONTEXT_INVESTIGATION_INTRO}}` | Bug hunt / debugging exercises |
| `{{CONTEXT_PREDICTION_INTRO}}` | Output prediction exercises |
| `{{CONTEXT_COMPARISON_INTRO}}` | Comparison exercises |

### Task Blocks

| Placeholder | Purpose |
|-------------|---------|
| `{{CONTEXT_STUDENT_TASK}}` | What the student needs to do |
| `{{CONTEXT_SUCCESS_CRITERIA}}` | How to know they succeeded |
| `{{CONTEXT_IMPLEMENTATION_GUIDANCE}}` | Tips for implementation |

### Completion Blocks

| Placeholder | Purpose |
|-------------|---------|
| `{{CONTEXT_ROLE_COMPLETE}}` | Closing message |
| `{{CONTEXT_FINAL_ASSEMBLY}}` | Builder exercise completion |
| `{{CONTEXT_VERIFICATION_COMPLETE}}` | Prediction verification done |

See [_TEMPLATE.json](../theme_mappings/_TEMPLATE.json) for the complete list.

---

## Example: Same Exercise, Different Themes

### Template (with placeholders)

```python
"""
{{CONTEXT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

def exercise_inventory():
    """Manage {{hero}}'s inventory."""
    inventory = {}

    def add_item(item, quantity):
        inventory[item] = inventory.get(item, 0) + quantity
        print(f"Added {quantity} {item}.")

    def use_item(item):
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
            print(f"{{hero}} used {item}! {{exclamation}}")
        else:
            print(f"No {item} available.")

    add_item("{{item}}", 3)
    use_item("{{item}}")

    print("{{CONTEXT_ROLE_COMPLETE}}")
```

### Rendered in Fantasy Theme

```python
"""
Welcome to the Adventurers Guild! Your training continues today.
You'll learn to manage character inventories using dictionaries.
"""

def exercise_inventory():
    """Manage the fighter's inventory."""
    # ... same code ...
    print(f"the fighter used healing potion! By the gods!")
    # ...
    print("Excellent work, adventurer! Your inventory management skills grow!")
```

### Rendered in Sci-Fi Theme

```python
"""
Welcome aboard, Cadet! All crew must complete supply management training.
You'll learn to track ship supplies using data structures.
"""

def exercise_inventory():
    """Manage the pilot's inventory."""
    # ... same code ...
    print(f"the pilot used datapad! By the stars!")
    # ...
    print("Systems confirmed, Cadet! Supply protocols validated!")
```

### Rendered in Plain Theme

```python
"""
Let's learn about dictionary operations.
You'll learn to manage data using Python dictionaries.
"""

def exercise_inventory():
    """Manage the programmer's inventory."""
    # ... same code ...
    print(f"the programmer used keyboard! Eureka!")
    # ...
    print("Great work! Dictionary operations complete.")
```

**The Python logic is identical. Only the narrative changes.**

---

## Design Principles

### 1. Theme-Agnostic Exercises

Every exercise is based on universal patterns that work regardless of theme:
- Inventory management works for potions, ship cargo, or data structures
- Character creation works for adventurers, crew members, or user profiles
- Bug hunting works for spell malfunctions, system errors, or code bugs

### 2. Semantic Placeholders

Placeholders map to **roles**, not specific objects:
- `{{item}}` = useful object (potion, datapad, tool)
- `{{transport}}` = means of travel (griffon, ship, internet)
- `{{spell1}}` = basic action/ability (Light, sensor scan, print statement)

### 3. Multiple Options for Variety

Each theme provides arrays of options:
```json
"hero": ["Harry Potter", "Ron Weasley", "Neville Longbottom"]
```
The system randomly picks one to keep content fresh.

### 4. Graceful Fallback

If a student disables themed content, all exercises fall back to `pymentor` (plain) theme automatically.

---

## Adding New Themes

1. **Copy the template:**
   ```bash
   cp theme_mappings/_TEMPLATE.json theme_mappings/my_theme.json
   ```

2. **Fill in required fields:**
   - `theme_id`, `theme_name`, `description`
   - Layer 1 entities (hero, school, etc.)
   - Layer 2 context blocks (CONTEXT_INTRO, etc.)

3. **Test with multiple exercises:**
   Verify the theme reads naturally across different exercise types.

See [THEME_CREATOR_GUIDE.md](../theme_mappings/THEME_CREATOR_GUIDE.md) for detailed instructions.

---

## Testing Themes

### Validation Script

```bash
# Check for hardcoded theme references
python scripts/audit_all_themes.py

# Test placeholder replacement
python scripts/apply_theme_placeholders.py --theme my_theme --check
```

### Cross-Theme Testing Strategy

1. **Primary test**: D&D SRD (commercial fantasy)
2. **Secondary test**: Cepheus (commercial sci-fi)
3. **Fallback test**: PyMentor (plain)
4. **Validation tests**: Proprietary themes (for pattern validation only)

---

## Architecture Benefits

1. **Content reuse**: Write once, works in any theme
2. **Easy localization**: Theme variables can be translated
3. **Legal safety**: Clear separation between free and proprietary IP
4. **Testing flexibility**: Validate with familiar IP, ship with open IP
5. **Student choice**: Let students pick their preferred setting
6. **Theme creator ecosystem**: Anyone can create new themes with just JSON

---

## Quick Links

| Resource | Location |
|----------|----------|
| Complete placeholder list | [theme_mappings/_TEMPLATE.json](../theme_mappings/_TEMPLATE.json) |
| Example theme | [theme_mappings/_EXAMPLE_fantasy_complete.json](../theme_mappings/_EXAMPLE_fantasy_complete.json) |
| Theme creator guide | [theme_mappings/THEME_CREATOR_GUIDE.md](../theme_mappings/THEME_CREATOR_GUIDE.md) |
| Narrative templates | [NARRATIVE_SYSTEM.md](NARRATIVE_SYSTEM.md) |
| Writing exercises | [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) |
| Writing lessons | [WRITING_GUIDE_LESSONS.md](WRITING_GUIDE_LESSONS.md) |
