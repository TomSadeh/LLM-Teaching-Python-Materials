# Exercise Narrative Architecture

**Date:** 2026-02-01
**Status:** 📊 Analysis Complete - Design Phase

---

## Executive Summary

Analysis of all 145 exercises reveals a **predominantly hybrid architecture** where:
- **100% are multi-task exercises** (average 8.6 tasks per exercise)
- **72% exhibit progressive narrative patterns** (104 exercises)
- **58% have rich narrative complexity** (84 exercises)
- **43% narrative-to-code ratio** on average

**Key Insight:** We need **exercise-level narrative templates** that wrap around task-level templates, creating a cohesive story across multiple tasks.

---

## Current State

### Task Structure

| Metric | Value | Insight |
|--------|-------|---------|
| Multi-task exercises | 145 (100%) | No single-task exercises exist |
| Average tasks/exercise | 8.6 | Substantial scope per exercise |
| Exercises with 10+ tasks | ~65 (45%) | Complex multi-part exercises |
| Exercises with 20+ tasks | ~15 (10%) | Very large exercises |

**Conclusion:** Exercises are inherently multi-task learning experiences, not isolated code snippets.

### Narrative Complexity Distribution

| Complexity | Count | % | Characteristics |
|------------|-------|---|-----------------|
| **Rich** | 84 | 58% | Multiple narrative elements, story progression |
| **Moderate** | 28 | 19% | Some story elements, basic progression |
| **Simple** | 33 | 23% | Minimal narrative, mostly technical |
| **None** | 0 | 0% | No purely technical exercises |

**Conclusion:** All exercises have narrative elements; most are story-rich.

### Story Archetypes Found

| Archetype | Count | % | Description |
|-----------|-------|---|-------------|
| **Mixed Narrative** | 41 | 28% | Blend of multiple narrative patterns |
| **Tutorial Guide** | 38 | 26% | "Follow along" with examples |
| **Challenge/Competition** | 37 | 26% | Game-like challenges |
| **Quest/Mission** | 13 | 9% | Goal-oriented tasks |
| **Mystery/Investigation** | 9 | 6% | Debug/discover patterns |
| **Progressive Build** | 3 | 2% | Explicit phase-based building |
| **World Exploration** | 2 | 1% | Discover a world/system |
| **Technical Only** | 2 | 1% | Minimal narrative |

**Conclusion:** Diverse narrative approaches, with mixed/tutorial/challenge dominating.

### Narrative Patterns

| Pattern | Count | % | Description |
|---------|-------|---|-------------|
| **Progressive narrative** | 99 | 68% | Story evolves between tasks |
| **Has closing** | 38 | 26% | Conclusion/wrap-up |
| **Quest structure** | 9 | 6% | Explicit mission/goal |
| **Progression phases** | 3 | 2% | Phase 1, 2, 3 markers |
| **Challenge escalation** | 3 | 2% | Difficulty increases with story |
| **World building** | 3 | 2% | Establishes a setting |

**Conclusion:** Most exercises tell a progressive story across tasks.

### Hybrid Exercise Patterns

**Definition:** Exercises that combine:
- Multiple tasks (10+)
- Progressive narrative (story evolves)
- Rich complexity

**Count:** 104 exercises (72%)

**Pattern:** Large exercises (20+ tasks) typically exhibit:
- World exploration or system-building arcs
- Progressive chapter narrative structure
- Tutorial guide for skill building exercises

---

## The Problem

### What We Have Now

**Task-Level Templates** (15 templates)
- Template for individual function/task within exercise
- Example: `template_2_incremental_builder`
- Works for **one task at a time**

### What We Need

**Exercise-Level Narrative Templates**
- Wrap around multiple tasks
- Provide cohesive story across exercise
- Connect tasks with narrative progression

### Current Gap

```
┌─────────────────────────────────────────┐
│  Exercise: RPG Battle (21 tasks)        │
├─────────────────────────────────────────┤
│  Task 1: Create Character class         │  <- template_2_incremental_builder
│  Task 2: Add health attribute           │  <- template_2_incremental_builder
│  Task 3: Implement attack method        │  <- template_2_incremental_builder
│  ...                                     │
│  Task 21: Battle simulation             │  <- template_2_incremental_builder
└─────────────────────────────────────────┘
     ↑
     Missing: Overall narrative wrapper!
```

**What's Missing:**
- Opening: "You're creating an RPG battle system..."
- Progression: "Now that you have characters, let's add combat..."
- Transitions: "With attacks working, let's add defense..."
- Closure: "You've built a complete battle system!"

---

## Proposed Solution: Two-Level Template System

### Level 1: Exercise-Level Narrative Templates

Provide overall story structure:

```python
# Exercise Narrative Template Example

{{EXERCISE_OPENING}}
# Opening narrative introducing the whole exercise
# Example: "You're building a magical RPG battle system..."

{{SECTION_1_INTRO}}
# Introduction to first section of tasks
# Example: "First, let's create character classes..."

# Tasks 1-5 go here (using task-level templates)

{{SECTION_2_INTRO}}
# Transition and introduction to next section
# Example: "Now that characters exist, let's add combat..."

# Tasks 6-12 go here

{{SECTION_3_INTRO}}
# Another progression
# Example: "With basic combat working, let's add special abilities..."

# Tasks 13-21 go here

{{EXERCISE_CLOSING}}
# Wrap-up and conclusion
# Example: "Congratulations! You've built a complete battle system..."
```

### Level 2: Task-Level Templates (Existing)

Handle individual tasks within sections:
- `template_2_incremental_builder` - Build step-by-step
- `template_4_forensic_debugger` - Debug errors
- `template_6_specification_implementer` - Build to spec
- etc.

---

## Exercise Narrative Template Archetypes

Based on audit, here are proposed exercise-level narrative archetypes:

### 1. **Progressive Chapter**

**Structure:** Story unfolds in chapters/sections
**Usage:** 41% of exercises (mixed narrative)
**Pattern:**
```
Opening → Chapter 1 → Chapter 2 → Chapter 3 → Closing
```

**Example:**
```
Opening: "Welcome to the magical academy..."
Chapter 1: "Your first lesson: Basic spells"
  - Task 1-3: Create spell functions
Chapter 2: "Advancing your skills"
  - Task 4-7: Add spell effects
Chapter 3: "Master level magic"
  - Task 8-10: Combine spells
Closing: "You're now a certified wizard!"
```

### 2. **Tutorial Walkthrough**

**Structure:** Follow-along with examples
**Usage:** 26% of exercises
**Pattern:**
```
Setup → Example 1 → Try It 1 → Example 2 → Try It 2 → Practice
```

**Example:**
```
Setup: "Let's learn dictionaries by building a spellbook"
Example 1: "Here's how to create a spell entry..."
Try It 1: Create your own spell entry
Example 2: "Now let's look up spells..."
Try It 2: Implement spell lookup
Practice: Build complete spellbook
```

### 3. **Challenge Quest**

**Structure:** Game-like progression with challenges
**Usage:** 26% of exercises
**Pattern:**
```
Challenge Intro → Level 1 → Level 2 → Level 3 → Victory
```

**Example:**
```
Challenge: "Can you build a working calculator?"
Level 1: Basic operations (+, -)
Level 2: Advanced operations (*, /)
Level 3: Special features (powers, roots)
Victory: "Calculator complete! Here's your score..."
```

### 4. **Mystery Investigation**

**Structure:** Discover/debug through investigation
**Usage:** 6% of exercises
**Pattern:**
```
Mystery Setup → Clue 1 → Clue 2 → Clue 3 → Solution
```

**Example:**
```
Mystery: "Something's wrong with this code..."
Clue 1: The error message says...
Clue 2: Looking at line 10...
Clue 3: The variable type is...
Solution: Fix the bug!
```

### 5. **World Builder**

**Structure:** Build a world/system piece by piece
**Usage:** 2% of exercises (but important for OOP)
**Pattern:**
```
World Intro → Entities → Interactions → Systems → Complete World
```

**Example:**
```
World: "Let's create a fantasy kingdom"
Entities: Create characters, items, locations
Interactions: Characters can trade items
Systems: Economy, combat, quests
Complete: Your kingdom is alive!
```

### 6. **Spec Implementation**

**Structure:** Build to detailed specifications
**Usage:** Implicit in many complete_function exercises
**Pattern:**
```
Requirements → Feature 1 → Feature 2 → Feature 3 → Testing
```

**Example:**
```
Requirements: "Build a contact book with these features..."
Feature 1: Add contacts
Feature 2: Search contacts
Feature 3: Delete contacts
Testing: Verify all features work
```

---

## Implementation Strategy

### Phase 1: Create Exercise Narrative Templates

For each archetype above, create template file:

```
templates/structure_patterns/
├── exercise_narrative_progressive_chapter.md
├── exercise_narrative_tutorial_walkthrough.md
├── exercise_narrative_challenge_quest.md
├── exercise_narrative_mystery_investigation.md
├── exercise_narrative_world_builder.md
└── exercise_narrative_spec_implementation.md
```

Each template contains:
- `{{EXERCISE_OPENING}}` - Overall introduction
- `{{SECTION_N_INTRO}}` - Section introductions (1-5 sections typical)
- `{{SECTION_N_TRANSITION}}` - Transitions between sections
- `{{EXERCISE_CLOSING}}` - Wrap-up and conclusion

### Phase 2: Map Exercises to Narrative Templates

Update conversion script to identify:
1. Which exercise narrative template fits
2. How many sections the exercise has
3. Where to place section breaks

### Phase 3: Combine with Task Templates

Final structure:

```python
# Using: exercise_narrative_progressive_chapter
# + task template_2_incremental_builder for each task

{{EXERCISE_OPENING}}
"""
{{narrative_world}}'s magical academy needs a spell system.
You'll build it step by step.
"""

{{SECTION_1_INTRO}}
# Chapter 1: Basic Spell Structure

def create_spell():
    """
    {{CONTEXT_FUNCTION_DESCRIPTION}}
    Create a spell dictionary.
    """
    pass  # Using template_2_incremental_builder

{{SECTION_2_INTRO}}
# Chapter 2: Spell Effects

def cast_spell():
    """
    {{CONTEXT_FUNCTION_DESCRIPTION}}
    Cast a spell and apply its effect.
    """
    pass  # Using template_2_incremental_builder

{{EXERCISE_CLOSING}}
"""
Congratulations! You've built a complete spell system.
"""
```

---

## Sectioning Strategy

### How to Divide Exercises into Sections

Based on audit findings:

**Small Exercises (1-5 tasks):**
- Single section with opening/closing
- No section breaks needed

**Medium Exercises (6-12 tasks):**
- 2-3 sections
- Section break every 3-5 tasks
- Group by related functionality

**Large Exercises (13-20 tasks):**
- 3-4 sections
- Section break every 4-6 tasks
- Clear progression: Setup → Build → Enhance → Complete

**Very Large Exercises (21+ tasks):**
- 4-5 sections
- Section break every 5-7 tasks
- May need mini-conclusions within sections

### Section Break Heuristics

Identify natural breaks:
1. **Functionality change** - Moving from creation to manipulation
2. **Concept progression** - From basic to advanced
3. **Phase markers** - Explicit "Phase 1", "Phase 2" comments
4. **Class changes** - When switching between classes in OOP
5. **Exercise type change** - Moving from write to debug

---

## Structure Examples

### Example 1: Large Exercise (21 tasks) - Progressive Chapter

```
Exercise Narrative: Progressive Chapter

Opening: "Build an RPG battle system"

Section 1 (Tasks 1-5): Character Creation
- Create Character class
- Add attributes (health, attack, defense)
- Implement __init__ and __str__

Section 2 (Tasks 6-12): Combat System
- Implement attack method
- Add defense calculation
- Handle damage
- Check if character is alive

Section 3 (Tasks 13-17): Special Abilities
- Add special attack
- Implement mana system
- Create ability effects

Section 4 (Tasks 18-21): Battle Simulation
- Create battle loop
- Handle turn-based combat
- Determine winner

Closing: "Complete battle system ready!"
```

### Example 2: Medium Exercise (7 tasks) - Tutorial Walkthrough

```
Exercise Narrative: Tutorial Walkthrough

Opening: "Learn dictionaries by building a {{item}} collection"

Section 1 (Tasks 1-3): Basic Dictionary Operations
- Example: Create item dictionary
- Try it: Add your own entry
- Try it: Look up item by name

Section 2 (Tasks 4-7): Advanced Operations
- Example: Update item properties
- Try it: Remove an item
- Try it: List all items
- Practice: Build complete collection

Closing: "You've mastered dictionaries!"
```

---

## Benefits of Two-Level System

### 1. **Pedagogical Clarity**
- Students understand where they are in the learning journey
- Clear progression from simple to complex
- Motivation through story

### 2. **Theme Flexibility**
- Exercise narrative separate from task details
- Easy to retheme entire exercise
- Maintain pedagogical structure across themes

### 3. **Cognitive Load Management**
- Large exercises broken into digestible sections
- Natural pause points for reflection
- Reduced overwhelm

### 4. **Reusability**
- Exercise narratives can wrap different task combinations
- Task templates remain focused and simple
- Mix and match as needed

---

## Implementation Checklist

### Phase 1: Template Creation
- [ ] Create 6 exercise narrative template files
- [ ] Define placeholder structure for each
- [ ] Document usage guidelines

### Phase 2: Conversion Script Enhancement
- [ ] Add exercise narrative detection to `convert_to_templates.py`
- [ ] Identify section break points
- [ ] Match exercises to narrative templates
- [ ] Generate exercise-level context blocks

### Phase 3: Pilot Conversion
- [ ] Select 5 representative exercises
- [ ] Apply two-level template system
- [ ] Test with one theme
- [ ] Validate pedagogical flow

### Phase 4: Full Conversion
- [ ] Convert all 145 exercises
- [ ] Define context blocks for all themes
- [ ] Test across all 5 themes
- [ ] Validate narrative coherence

---

## Next Steps

### Immediate Actions

1. **Review this analysis** with team
2. **Select pilot exercises** for two-level system
3. **Create first exercise narrative template** (Progressive Chapter)
4. **Test on 1 exercise** end-to-end

### Questions to Resolve

1. **Section naming:** Use "Chapter", "Section", "Part", or "Phase"?
2. **Transition style:** Explicit prompts or subtle narrative flow?
3. **Closing frequency:** Every section or just at end?
4. **Mixed task types:** How to narrative between complete_function and debug tasks?

---

## Appendix: Statistics

### Narrative Locations Found

| Location | Count | % |
|----------|-------|---|
| Function docstrings | ~145 | 100% |
| Narrative comments | ~120 | 83% |
| Exercise descriptions | ~100 | 69% |
| Between functions | ~80 | 55% |
| Phase markers | ~3 | 2% |

### Average Exercise Profile

- **Tasks:** 8.6
- **Lines of code:** ~250
- **Narrative lines:** ~107
- **Narrative ratio:** 43%
- **Sections needed:** 2-3

---

**Status:** 📊 Analysis Complete
**Recommendation:** Proceed with two-level template system
**Priority:** High - Will significantly improve conversion quality
**Estimated Effort:** 12-16 hours for full implementation
