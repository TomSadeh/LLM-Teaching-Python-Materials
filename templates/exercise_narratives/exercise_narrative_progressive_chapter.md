# Exercise Narrative Template: Progressive Chapter

**Usage:** 28% of exercises (most common)
**Best For:** Multi-task exercises where story unfolds in chapters/sections
**Sections:** 2-5 depending on exercise size
**Pattern:** Opening → Chapter 1 → Chapter 2 → Chapter 3+ → Closing

---

## Template Structure

### Opening
```python
"""
{{EXERCISE_TITLE}}

{{EXERCISE_OPENING}}
Welcome to {{narrative_location}}! In this exercise, you'll {{exercise_goal}}.

This is a {{exercise_scope}} project that will teach you:
- {{learning_objective_1}}
- {{learning_objective_2}}
- {{learning_objective_3}}

{{exercise_hook}}

Let's begin!
"""
```

### Chapter 1 (Foundation)
```python
# ═══════════════════════════════════════════════════════════
# {{CHAPTER_1_TITLE}}
# ═══════════════════════════════════════════════════════════

{{CHAPTER_1_INTRO}}
# First, we need to {{chapter_1_goal}}.
# {{chapter_1_context}}

# Tasks 1-N go here (using task-level templates)
```

### Chapter 2 (Building)
```python
# ═══════════════════════════════════════════════════════════
# {{CHAPTER_2_TITLE}}
# ═══════════════════════════════════════════════════════════

{{CHAPTER_2_TRANSITION}}
# Great! Now that {{chapter_1_accomplishment}}, let's {{chapter_2_goal}}.
# {{chapter_2_context}}

# Tasks N+1 to M go here (using task-level templates)
```

### Chapter 3 (Enhancing) - Optional
```python
# ═══════════════════════════════════════════════════════════
# {{CHAPTER_3_TITLE}}
# ═══════════════════════════════════════════════════════════

{{CHAPTER_3_TRANSITION}}
# Excellent progress! With {{chapter_2_accomplishment}} complete,
# it's time to {{chapter_3_goal}}.
# {{chapter_3_context}}

# Tasks M+1 to P go here (using task-level templates)
```

### Chapter 4 (Advanced) - Optional for large exercises
```python
# ═══════════════════════════════════════════════════════════
# {{CHAPTER_4_TITLE}}
# ═══════════════════════════════════════════════════════════

{{CHAPTER_4_TRANSITION}}
# Almost there! Now let's {{chapter_4_goal}}.
# {{chapter_4_context}}

# Tasks P+1 to Q go here (using task-level templates)
```

### Closing
```python
# ═══════════════════════════════════════════════════════════
# {{EXERCISE_COMPLETION_TITLE}}
# ═══════════════════════════════════════════════════════════

{{EXERCISE_CLOSING}}
# Congratulations! You've completed {{exercise_completion_summary}}.
#
# You now know how to:
# - {{skill_learned_1}}
# - {{skill_learned_2}}
# - {{skill_learned_3}}
#
# {{celebration_message}}

def main():
    """Run all exercises to test your implementation."""
    # Call all exercise functions here
    pass

if __name__ == "__main__":
    main()
```

---

## Placeholder Definitions

### Opening Placeholders

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{EXERCISE_TITLE}}` | Exercise name | "RPG Battle System" |
| `{{EXERCISE_OPENING}}` | Opening hook | "The kingdom is under attack..." |
| `{{narrative_location}}` | Where the story takes place | "the Magical Academy" |
| `{{exercise_goal}}` | What student will build | "create a complete spell-casting system" |
| `{{exercise_scope}}` | Size indicator | "multi-part", "comprehensive", "advanced" |
| `{{learning_objective_N}}` | What they'll learn | "How to use dictionaries for data" |
| `{{exercise_hook}}` | Engaging question/challenge | "Can you master the ancient arts?" |

### Chapter Placeholders

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{CHAPTER_N_TITLE}}` | Chapter heading | "Chapter 1: Creating Spells" |
| `{{CHAPTER_N_INTRO}}` | Chapter introduction | "First, we need to create spell data structures" |
| `{{chapter_N_goal}}` | What to accomplish | "create the basic spell structure" |
| `{{chapter_N_context}}` | Additional context | "Spells have name, power, and type" |
| `{{CHAPTER_N_TRANSITION}}` | Transition from previous | "Great! Now that spells exist..." |
| `{{chapter_N_accomplishment}}` | What was just done | "you've created spell structures" |

### Closing Placeholders

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{EXERCISE_COMPLETION_TITLE}}` | Closing header | "Quest Complete!" |
| `{{EXERCISE_CLOSING}}` | Closing narrative | "The kingdom is safe thanks to you!" |
| `{{exercise_completion_summary}}` | What was built | "a complete spell-casting system" |
| `{{skill_learned_N}}` | Skills acquired | "Create and manipulate spell dictionaries" |
| `{{celebration_message}}` | Congratulations | "You're now a certified wizard!" |

---

## Sectioning Guidelines

### Small Exercise (2-5 tasks)
```
Opening
Chapter 1: All tasks
Closing
```

### Medium Exercise (6-12 tasks)
```
Opening
Chapter 1: Tasks 1-4 (Foundation)
Chapter 2: Tasks 5-8 (Building)
Chapter 3: Tasks 9-12 (Enhancement)
Closing
```

### Large Exercise (13-20 tasks)
```
Opening
Chapter 1: Tasks 1-5 (Foundation)
Chapter 2: Tasks 6-10 (Building)
Chapter 3: Tasks 11-15 (Enhancement)
Chapter 4: Tasks 16-20 (Advanced)
Closing
```

### Very Large Exercise (21+ tasks)
```
Opening
Chapter 1: Tasks 1-6 (Foundation)
Chapter 2: Tasks 7-12 (Building)
Chapter 3: Tasks 13-18 (Enhancement)
Chapter 4: Tasks 19-24 (Advanced)
Chapter 5: Tasks 25+ (Mastery)
Closing
```

---

## Theme Examples

### dumblecode (Harry Potter)

```python
"""
The Sorting Hat System

Welcome to Hogwarts! In this exercise, you'll create the famous
Sorting Hat system that assigns students to houses.

This is a comprehensive project that will teach you:
- How to use dictionaries for student data
- Working with nested data structures
- Implementing decision-making logic

Can you recreate the magic that has sorted thousands of students?

Let's begin!
"""

# ═══════════════════════════════════════════════════════════
# Chapter 1: Student Records
# ═══════════════════════════════════════════════════════════

# First, we need to create a system to store student information.
# Each student has a name, age, and personality traits.

# [Tasks 1-4: Create student dictionaries]

# ═══════════════════════════════════════════════════════════
# Chapter 2: House Characteristics
# ═══════════════════════════════════════════════════════════

# Great! Now that we can store student data, let's define
# the four houses and their values.
# Remember: Bravery, Cunning, Wisdom, and Loyalty!

# [Tasks 5-8: Create house definitions]

# ═══════════════════════════════════════════════════════════
# Chapter 3: The Sorting Algorithm
# ═══════════════════════════════════════════════════════════

# Excellent progress! With students and houses defined,
# it's time to implement the sorting logic.
# The Hat considers each student's traits carefully...

# [Tasks 9-12: Implement sorting logic]

# ═══════════════════════════════════════════════════════════
# Quest Complete!
# ═══════════════════════════════════════════════════════════

# Congratulations! You've created a complete Sorting Hat system.
#
# You now know how to:
# - Create and manipulate student records with dictionaries
# - Work with nested data structures for houses
# - Implement complex decision-making algorithms
#
# The Sorting Hat is pleased with your work! ⚡
```

### chirthon (Percy Jackson / Greek Mythology)

```python
"""
Quest for the Golden Fleece

Welcome to Camp Half-Blood! In this exercise, you'll build
a quest management system for demigods.

This is a multi-part project that will teach you:
- How to track quest objectives with dictionaries
- Managing hero stats and abilities
- Implementing challenge resolution

Can you help the demigods complete their dangerous quest?

Let's begin!
"""

# ═══════════════════════════════════════════════════════════
# Chapter 1: Hero Profiles
# ═══════════════════════════════════════════════════════════

# First, we need to create profiles for our brave demigods.
# Each hero has unique powers inherited from their godly parent.

# [Tasks 1-4: Create hero dictionaries]

# ═══════════════════════════════════════════════════════════
# Chapter 2: Quest Objectives
# ═══════════════════════════════════════════════════════════

# Great! Now that our heroes are ready, let's define the quest.
# The Golden Fleece awaits, but many challenges stand in the way!

# [Tasks 5-8: Create quest structure]

# ═══════════════════════════════════════════════════════════
# Chapter 3: Challenge Resolution
# ═══════════════════════════════════════════════════════════

# Excellent progress! With heroes and quests defined,
# it's time to face the challenges.
# Will your heroes succeed or fall to the monsters?

# [Tasks 9-12: Implement challenge system]

# ═══════════════════════════════════════════════════════════
# Quest Complete!
# ═══════════════════════════════════════════════════════════

# Congratulations! You've built a complete quest system.
#
# You now know how to:
# - Track hero abilities with dictionaries
# - Manage complex quest structures
# - Resolve challenges programmatically
#
# The Oracle smiles upon your success! 🏛️
```

### pyfire (KOTLC / Keeper of the Lost Cities)

```python
"""
The Ability Registry

Welcome to Foxfire Academy! In this exercise, you'll create
the Ability Registry that tracks special talents.

This is an advanced project that will teach you:
- How to catalog abilities with dictionaries
- Tracking ability manifestation and strength
- Managing ability restrictions and requirements

Can you build the system that identifies every unique talent?

Let's begin!
"""

# ═══════════════════════════════════════════════════════════
# Chapter 1: Ability Definitions
# ═══════════════════════════════════════════════════════════

# First, we need to define all known abilities in the Lost Cities.
# Each ability has a name, rarity level, and manifestation age.

# [Tasks 1-4: Create ability dictionaries]

# ═══════════════════════════════════════════════════════════
# Chapter 2: Registry System
# ═══════════════════════════════════════════════════════════

# Great! Now that abilities are defined, let's create the registry.
# The system must track who has which abilities and their strength!

# [Tasks 5-8: Build registry structure]

# ═══════════════════════════════════════════════════════════
# Chapter 3: Ability Matching
# ═══════════════════════════════════════════════════════════

# Excellent progress! With the registry complete,
# it's time to implement ability matching and validation.
# Some abilities are extremely rare!

# [Tasks 9-12: Implement matching logic]

# ═══════════════════════════════════════════════════════════
# Achievement Unlocked!
# ═══════════════════════════════════════════════════════════

# Congratulations! You've created the complete Ability Registry.
#
# You now know how to:
# - Catalog complex data with nested dictionaries
# - Implement validation and matching systems
# - Track hierarchical relationships in data
#
# The Council is impressed with your technical prowess! ✨
```

---

## Usage Guidelines

### When to Use This Template

✅ **Use Progressive Chapter when:**
- Exercise has 6+ tasks
- Clear progression from simple to complex
- Story can be divided into logical chapters
- Each section builds on previous sections

❌ **Don't use Progressive Chapter when:**
- Exercise is very short (2-3 tasks)
- Tasks are independent (no progression)
- Better fit for Tutorial Walkthrough (example-based)
- Better fit for Challenge Quest (game-like)

### Choosing Number of Chapters

| Tasks | Chapters | Division Strategy |
|-------|----------|-------------------|
| 2-5 | 1 | Single chapter, opening + closing |
| 6-9 | 2-3 | Foundation + Building (+ Enhancement) |
| 10-15 | 3 | Foundation + Building + Enhancement |
| 16-20 | 3-4 | Foundation + Building + Enhancement + Advanced |
| 21-30 | 4-5 | Add Mastery chapter |
| 30+ | 5 | Consider splitting exercise |

### Chapter Naming Conventions

**Generic (Works anywhere):**
- Chapter 1, Chapter 2, Chapter 3
- Part 1, Part 2, Part 3
- Section 1, Section 2, Section 3

**Thematic (Theme-specific):**
- **dumblecode:** Year 1, Year 2, Year 3 / Lesson 1, 2, 3
- **chirthon:** Quest Phase 1, 2, 3 / Trial 1, 2, 3
- **compile-games:** Arena Round 1, 2, 3 / Training Day 1, 2, 3
- **pyfire:** Level 1, 2, 3 / Ability Tier 1, 2, 3
- **pymentor:** Module 1, 2, 3 / Stage 1, 2, 3

---

## Integration with Task Templates

Each task within a chapter uses appropriate task-level template:

```python
# ═══════════════════════════════════════════════════════════
# Chapter 1: Spell Creation
# ═══════════════════════════════════════════════════════════

# First, we need to create basic spell structures.
# Each spell has a name, element, and power level.

# Task 1: Using template_2_incremental_builder
def create_spell(name, element, power):
    """
    {{CONTEXT_FUNCTION_DESCRIPTION}}
    Create a spell dictionary with the given attributes.

    Args:
        name: {{name_description}}
        element: {{element_description}}
        power: {{power_description}}

    Returns:
        Dictionary representing a spell
    """
    pass

# Task 2: Using template_2_incremental_builder
def get_spell_info(spell):
    """
    {{CONTEXT_FUNCTION_DESCRIPTION}}
    Return a formatted string describing the spell.
    """
    pass
```

---

## Customization Points

### Tone Adjustments

**Formal/Academic:**
```python
# Chapter 1: Foundational Concepts
# In this section, we establish the core data structures...
```

**Friendly/Encouraging:**
```python
# Chapter 1: Let's Get Started!
# Ready to build something awesome? Let's create...
```

**Dramatic/Story-Driven:**
```python
# Chapter 1: The Journey Begins
# As dawn breaks over the kingdom, you must...
```

### Visual Separators

**Minimal:**
```python
# --- Chapter 1: Title ---
```

**Standard:**
```python
# ═══════════════════════════════════════════════════════════
# Chapter 1: Title
# ═══════════════════════════════════════════════════════════
```

**Decorative (theme-specific):**
```python
# ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
# Chapter 1: Spell Basics
# ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
```

---

## Template Metadata

```yaml
template_id: exercise_narrative_progressive_chapter
version: 1.0
created: 2026-02-01
usage_percentage: 28%
best_for: Multi-task exercises with clear progression
min_tasks: 6
typical_tasks: 8-15
max_tasks: 30
sections: 2-5
combines_with:
  - template_2_incremental_builder (most common)
  - template_6_specification_implementer
  - template_9_world_builder
  - template_13_decision_tree
themes:
  - dumblecode
  - chirthon
  - compile-games
  - pyfire
  - pymentor
```

---

**Status:** ✅ Ready for use
**Next:** Test on pilot exercise
**Recommended Pilot:** `exercise_9_rpg_battle.py` (21 tasks, tutorial_guide archetype)
