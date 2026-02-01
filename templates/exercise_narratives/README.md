# Exercise Narrative Templates

**Purpose:** Exercise-level narrative templates that wrap around task-level templates to create cohesive multi-task learning experiences.

**Status:** ✅ All 6 templates created and tested

---

## Overview

Based on analysis of 145 exercises, we discovered that **100% are multi-task exercises** (average 8.6 tasks) with **72% exhibiting progressive narrative patterns**. These templates provide the overall story structure that connects multiple coding tasks into a unified learning experience.

---

## Available Templates

### 1. Progressive Chapter (28% of exercises)

**File:** `exercise_narrative_progressive_chapter.py`
**Best For:** Multi-task exercises with clear progression
**Pattern:** Opening → Chapter 1 → Chapter 2 → Chapter 3+ → Closing

**Structure Example (21 tasks):**
```
Opening
Chapter 1: Foundation (Tasks 1-4)
Chapter 2: Building (Tasks 5-8)
Chapter 3: Enhancement (Tasks 9-12)
Chapter 4: Advanced (Tasks 13-16)
Chapter 5: Mastery (Tasks 17-21)
Closing
```

**Theme Examples:**
- dumblecode: Year 1, Year 2, Year 3...
- chirthon: Quest Phase 1, 2, 3...
- compile-games: Training Day 1, 2, 3...

---

### 2. Tutorial Walkthrough (26% of exercises)

**File:** `exercise_narrative_tutorial_walkthrough.py`
**Best For:** Example-driven learning with practice
**Pattern:** Setup → Example 1 → Try It 1 → Example 2 → Try It 2 → Practice

**Structure Example (8 tasks):**
```
Opening
Example 1 (Task 1)
Try It 1 (Task 2)
Example 2 (Task 3)
Try It 2 (Task 4)
Example 3 (Task 5)
Try It 3 (Task 6)
Practice (Tasks 7-8)
Closing
```

**Use When:** Teaching new concepts through worked examples

---

### 3. Challenge Quest (26% of exercises)

**File:** `exercise_narrative_challenge_quest.py`
**Best For:** Game-like, competitive exercises
**Pattern:** Challenge Intro → Level 1 → Level 2 → Level 3 → Victory

**Structure Example (12 tasks):**
```
Opening (Challenge briefing)
Level 1 ⭐: Tasks 1-3 (Easy, 100 pts)
Level 2 ⭐⭐: Tasks 4-6 (Medium, 200 pts)
Level 3 ⭐⭐⭐: Tasks 7-9 (Hard, 300 pts)
Level 4 ⭐⭐⭐⭐: Tasks 10-12 (Expert, 500 pts)
Victory (Score & achievements)
```

**Use When:** Motivation through gamification, progressive difficulty

---

### 4. Mystery Investigation (6% of exercises)

**File:** `exercise_narrative_mystery_investigation.py`
**Best For:** Debug exercises, error decoding
**Pattern:** Mystery Setup → Clue 1 → Clue 2 → Clue 3 → Solution

**Structure Example (7 tasks):**
```
Opening (Mystery introduced)
Clue 1: The Error Message (Task 1)
Clue 2: The Variable Trail (Task 2)
Clue 3: The Logic Path (Task 3)
Clue 4: The Data Structure (Task 4)
Clue 5: The Function Call (Task 5)
Clue 6: The Type Mismatch (Task 6)
Solution: Case Solved! (Task 7)
Closing
```

**Use When:** Debug exercises, decode_error, bug_hunt

---

### 5. World Builder (2% of exercises)

**File:** `exercise_narrative_world_builder.py`
**Best For:** OOP exercises, entity systems
**Pattern:** World Intro → Entities → Interactions → Systems → Complete World

**Structure Example (15 tasks):**
```
Opening (World introduction)
🏛️ Entities: Tasks 1-6 (40%)
🔗 Interactions: Tasks 7-12 (40%)
⚙️ Systems: Tasks 13-15 (20%)
Closing (World complete)
```

**Use When:** Module 9 OOP, simulation exercises, class-based systems

---

### 6. Spec Implementation (~18% of exercises)

**File:** `exercise_narrative_spec_implementation.py`
**Best For:** Complete_function with detailed specifications
**Pattern:** Requirements → Feature 1 → Feature 2 → Feature 3 → Testing

**Structure Example (10 tasks):**
```
Opening (Project specifications)
Feature 1 🔴 HIGH: Task 1
Feature 2 🔴 HIGH: Task 2
Feature 3 🔴 HIGH: Task 3
Feature 4 🟡 MEDIUM: Task 4
Feature 5 🟡 MEDIUM: Task 5
Feature 6 🟡 MEDIUM: Task 6
Feature 7 🟢 LOW: Task 7
Testing (Tasks 8-10)
Closing (Project delivery)
```

**Use When:** Complete_function exercises with Args/Returns specifications

---

## Usage

### Programmatic Usage

```python
from exercise_narrative_progressive_chapter import generate_exercise_structure

structure = generate_exercise_structure(
    exercise_title="RPG Battle System",
    task_count=21,
    theme='dumblecode'
)

print(f"Sections: {structure['section_count']}")
for section in structure['sections']:
    print(f"  {section['title']}: Tasks {section['task_range']}")
```

### Integration with Task Templates

```python
# Exercise-level template
exercise_template = 'exercise_narrative_progressive_chapter'

# Task-level templates for each task
task_templates = [
    'template_2_incremental_builder',  # Tasks 1-5
    'template_6_specification_implementer',  # Tasks 6-10
    'template_9_world_builder',  # Tasks 11-15
]

# Generated exercise combines both levels
```

---

## Template Metadata

| Template | Usage | Min Tasks | Typical Tasks | Max Tasks |
|----------|-------|-----------|---------------|-----------|
| Progressive Chapter | 28% | 6 | 8-15 | 30 |
| Tutorial Walkthrough | 26% | 4 | 6-10 | 15 |
| Challenge Quest | 26% | 3 | 6-12 | 20 |
| Mystery Investigation | 6% | 3 | 5-8 | 12 |
| World Builder | 2% | 6 | 10-20 | 30 |
| Spec Implementation | 18% | 4 | 6-12 | 20 |

---

## Theme Support

All templates support all 5 themes:

### dumblecode (Harry Potter)
- Progressive: Years 1-5
- Challenge: House Points
- World: Magical Kingdom
- Celebration: ⚡

### chirthon (Percy Jackson)
- Progressive: Quest Phases
- Challenge: Divine Trials
- World: Mythological Realm
- Celebration: 🏛️

### compile-games (Hunger Games)
- Progressive: Training Days
- Challenge: Arena Rounds
- World: Panem Districts
- Celebration: 🏹

### pyfire (KOTLC)
- Progressive: Ability Levels
- Challenge: Ability Mastery
- World: Lost Cities
- Celebration: ✨

### pymentor (Generic)
- Progressive: Modules
- Challenge: Achievements
- World: System Architecture
- Celebration: 💻

---

## Placeholder System

Each template uses placeholders that get filled per theme:

**Exercise-level placeholders:**
- `{{EXERCISE_OPENING}}` - Opening narrative
- `{{CHAPTER_N_TITLE}}` - Chapter/section titles
- `{{CHAPTER_N_INTRO}}` - Section introductions
- `{{EXERCISE_CLOSING}}` - Wrap-up narrative

**Theme placeholders (within narratives):**
- `{{narrative_world}}` - The world name
- `{{narrative_location}}` - Specific location
- `{{hero}}`, `{{mentor}}`, `{{villain}}` - Characters
- `{{house_1}}`, `{{faction}}` - Groups

**Task-level placeholders (existing system):**
- `{{CONTEXT_FUNCTION_DESCRIPTION}}` - What function does
- `{{CONTEXT_NARRATIVE}}` - Task-specific story

---

## Selection Guidelines

### By Exercise Type

| Exercise Type | Best Template | Alternative |
|---------------|---------------|-------------|
| write_code | Progressive Chapter | Challenge Quest |
| complete_function | Spec Implementation | Progressive Chapter |
| decode_error | Mystery Investigation | Progressive Chapter |
| bug_hunt | Mystery Investigation | Challenge Quest |
| which_is_better | Tutorial Walkthrough | Progressive Chapter |
| output_prediction | Tutorial Walkthrough | Mystery Investigation |
| blank_page | Progressive Chapter | World Builder |
| fix_style | Spec Implementation | Mystery Investigation |

### By Task Count

| Tasks | Best Template | Why |
|-------|---------------|-----|
| 2-5 | Tutorial Walkthrough | Compact, example-driven |
| 6-9 | Progressive Chapter | Natural sections |
| 10-15 | Progressive Chapter | Clear progression |
| 16-20 | Challenge Quest | Maintains motivation |
| 21+ | Progressive Chapter | Multiple chapters |

### By Module

| Module | Best Template | Why |
|--------|---------------|-----|
| Module 0-1 | Tutorial Walkthrough | Foundational learning |
| Module 2-4 | Challenge Quest | Game-like motivation |
| Module 5-8 | Progressive Chapter | Building complexity |
| Module 9 (OOP) | World Builder | Entity-based thinking |

---

## Testing

All templates have been tested with sample task counts:

```bash
cd templates/exercise_narratives
python exercise_narrative_progressive_chapter.py
python exercise_narrative_tutorial_walkthrough.py
python exercise_narrative_challenge_quest.py
python exercise_narrative_mystery_investigation.py
python exercise_narrative_world_builder.py
python exercise_narrative_spec_implementation.py
```

**Results:**
- ✅ Progressive Chapter: 21 tasks → 5 chapters
- ✅ Tutorial: 8 tasks → 3 examples + 3 try-its + 2 practice
- ✅ Challenge: 12 tasks → 4 levels with points
- ✅ Mystery: 7 tasks → 6 clues + 1 solution
- ✅ World Builder: 15 tasks → entities + interactions + systems
- ✅ Spec: 10 tasks → 7 features + 3 testing

---

## Next Steps

### Immediate
1. Integrate with conversion script (`convert_to_templates.py`)
2. Test on pilot exercise (e.g., `exercise_9_rpg_battle.py`)
3. Generate full exercise with two-level templates

### Short Term
4. Map all 145 exercises to appropriate narrative templates
5. Define narrative content for all themes
6. Validate pedagogical flow

### Long Term
7. Create markdown documentation templates
8. Build theme-specific narrative libraries
9. Automate exercise generation from templates

---

## Files

```
templates/exercise_narratives/
├── README.md (this file)
├── exercise_narrative_progressive_chapter.py
├── exercise_narrative_progressive_chapter.md
├── exercise_narrative_tutorial_walkthrough.py
├── exercise_narrative_challenge_quest.py
├── exercise_narrative_mystery_investigation.py
├── exercise_narrative_world_builder.py
└── exercise_narrative_spec_implementation.py
```

---

**Status:** ✅ Complete
**Created:** 2026-02-01
**Next Milestone:** Integration with conversion system
