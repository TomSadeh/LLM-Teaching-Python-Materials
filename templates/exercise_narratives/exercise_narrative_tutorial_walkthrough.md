# Exercise Narrative Template: Tutorial Walkthrough

**Usage:** 26% of exercises
**Best For:** Example-driven learning where students follow along and practice
**Pattern:** Setup → Example 1 → Try It 1 → Example 2 → Try It 2 → Practice

---

## Template Structure

### Opening
```python
"""
{{EXERCISE_TITLE}}

{{TUTORIAL_OPENING}}
Let's learn {{concept}} by {{learning_method}}.

In this tutorial, you'll:
1. See examples of {{skill_1}}
2. Try it yourself with guidance
3. Practice independently

Follow along and learn by doing!
"""
```

### Example Section
```python
# ─────────────────────────────────────────────────────────────
# {{EXAMPLE_1_TITLE}} - Creating Your First Spell
# ─────────────────────────────────────────────────────────────

{{EXAMPLE_1_INTRO}}
# Here's an example of how to create a spell dictionary.
# Pay attention to the structure and keys used.

def example_1_create_spell():
    """
    {{CONTEXT_EXAMPLE_DESCRIPTION}}
    Example: Creating a basic fire spell

    This demonstrates: Dictionary creation with required keys
    """
    spell = {
        "name": "{{spell_1}}",
        "element": "{{element_fire}}",
        "power": 50
    }
    return spell

# Study this example carefully before moving on!
```

### Try It Section
```python
# ─────────────────────────────────────────────────────────────
# {{TRY_IT_1_TITLE}} - Your Turn!
# ─────────────────────────────────────────────────────────────

{{TRY_IT_1_INTRO}}
# Now you try! Create a spell similar to the example above.
# Use a different element and choose your own power level.

def create_ice_spell():
    """
    {{CONTEXT_FUNCTION_DESCRIPTION}}
    Create an ice spell dictionary.

    Follow the pattern from example_1.
    """
    pass  # ✏️ Your code here
```

### Practice Section
```python
# ─────────────────────────────────────────────────────────────
# {{PRACTICE_TITLE}} - Independent Practice
# ─────────────────────────────────────────────────────────────

{{PRACTICE_INTRO}}
# Great work! Now practice what you've learned on your own.
# These tasks combine everything from the examples.

# Create multiple spells and a spellbook system!
```

### Closing
```python
{{TUTORIAL_CLOSING}}
# Excellent! You've completed the tutorial.
#
# You learned:
# - {{learning_1}}
# - {{learning_2}}
# - {{learning_3}}
#
# {{encouragement}}
```

---

## Placeholder Definitions

### Tutorial Placeholders

| Placeholder | Example |
|-------------|---------|
| `{{TUTORIAL_OPENING}}` | "Welcome to the Dictionary Tutorial!" |
| `{{concept}}` | "dictionaries" |
| `{{learning_method}}` | "building a spellbook" |
| `{{skill_1}}` | "creating dictionary entries" |

### Example Placeholders

| Placeholder | Example |
|-------------|---------|
| `{{EXAMPLE_N_TITLE}}` | "Example 1: Basic Spell Creation" |
| `{{EXAMPLE_N_INTRO}}` | "Here's how to create a spell..." |
| `{{CONTEXT_EXAMPLE_DESCRIPTION}}` | "This shows the basic spell structure" |
| `{{example_demonstrates}}` | "dictionary key-value pairs" |

### Try It Placeholders

| Placeholder | Example |
|-------------|---------|
| `{{TRY_IT_N_TITLE}}` | "Try It 1: Create Your Own Spell" |
| `{{TRY_IT_N_INTRO}}` | "Now you try!" |
| `{{guidance_hint}}` | "Remember to include name, element, and power" |

---

## Theme Examples

### dumblecode (Harry Potter)
```python
"""
The Spellbook Tutorial

Welcome to {{narrative_location}}! Professor {{mentor}} will teach you
how to create and manage spell dictionaries.

In this tutorial, you'll:
1. See examples of spell creation
2. Try creating your own spells
3. Build a complete spellbook

Follow along and master the magical arts!
"""

# Example 1: The Basic Spell
def example_1_create_lumos():
    spell = {
        "name": "Lumos",
        "type": "Light",
        "power": 30
    }
    return spell

# Try It 1: Create Nox
def create_nox():
    """Create the counter-spell to Lumos."""
    pass
```

### chirthon (Percy Jackson)
```python
"""
The Hero's Abilities Tutorial

Welcome to {{narrative_location}}! {{mentor}} will guide you through
creating hero ability dictionaries.

In this tutorial, you'll:
1. See examples of godly powers
2. Try creating demigod abilities
3. Build a complete powers registry

Follow along and harness divine power!
"""

# Example 1: Zeus's Lightning
def example_1_lightning_bolt():
    ability = {
        "name": "Lightning Bolt",
        "god": "Zeus",
        "power": 100
    }
    return ability

# Try It 1: Poseidon's Trident
def create_tidal_wave():
    """Create Poseidon's water-based ability."""
    pass
```

---

## Structure Guidelines

### Small Tutorial (4-6 tasks)
```
Opening
Example 1 (Task 1)
Try It 1 (Task 2)
Example 2 (Task 3)
Try It 2 (Task 4)
Practice (Tasks 5-6)
Closing
```

### Standard Tutorial (7-10 tasks)
```
Opening
Example 1 (Task 1)
Try It 1 (Task 2)
Example 2 (Task 3)
Try It 2 (Task 4)
Example 3 (Task 5)
Try It 3 (Task 6)
Practice (Tasks 7-10)
Closing
```

### Large Tutorial (11+ tasks)
```
Opening
Example 1 (Task 1)
Try It 1 (Tasks 2-3)
Example 2 (Task 4)
Try It 2 (Tasks 5-6)
Example 3 (Task 7)
Try It 3 (Tasks 8-9)
Example 4 (Task 10)
Practice (Tasks 11+)
Closing
```

---

## When to Use

✅ **Use Tutorial Walkthrough when:**
- Teaching new concepts for the first time
- Students benefit from seeing examples
- Gradual scaffold from guided to independent
- Exercise types: write_code, complete_function (with examples)

❌ **Don't use when:**
- No examples provided (use Progressive Chapter)
- Heavy debugging focus (use Mystery Investigation)
- Competitive/game-like (use Challenge Quest)
- Pure OOP entity building (use World Builder)

---

## Integration with Task Templates

```python
# Example section uses completed example code
def example_1_spell():
    # Full working example
    return {"name": "Fireball", "power": 50}

# Try It uses template_2_incremental_builder
def create_your_spell():
    """{{CONTEXT_FUNCTION_DESCRIPTION}}"""
    pass  # Student implements

# Practice uses template_6_specification_implementer
def advanced_spellbook():
    """
    {{CONTEXT_FUNCTION_DESCRIPTION}}
    Build a complete spellbook system.

    Args: ...
    Returns: ...
    """
    pass
```

---

**Status:** ✅ Ready for use
**Combines With:** template_2_incremental_builder, template_6_specification_implementer
