# Hybrid Exercise Narrative Arcs

How to compose multi-part exercises using generic emotional beats.

---

## Overview

Hybrid exercises combine 2-4 exercise types into a single file with a **narrative arc**. The narrative is equally important as the exercise combination.

### The Four Components

```
Hybrid Exercise = Narrative Arc + Exercise Types + Theme + Task Instructions
```

| Component | What It Defines | Where It Lives |
|-----------|-----------------|----------------|
| **Narrative Arc** | Emotional journey structure | This document |
| **Exercise Types** | Pedagogical activities | Exercise file structure |
| **Theme** | World-specific content (Layers 1-3) | `theme_mappings/*.json` |
| **Task Instructions** | Universal mechanical instructions (Layer 4) | `theme_mappings/*.json` |

---

## Layer 4: Task Instructions

Task instructions are **universal mechanical instructions** that don't change with theme. They tell the student what to DO, separate from the narrative context.

### Why Layer 4?

| Layer | Content | Themed? |
|-------|---------|---------|
| 1 | Entity names | Yes |
| 2 | Context blocks (narrative) | Yes |
| 3 | Framework concepts | Yes |
| **4** | **Task instructions** | **No** |

**Narrative** (Layer 2): *"Elena's spell-casting code had critical flaws..."*
**Instruction** (Layer 4): *"Find and fix the 3 bugs in the code below."*

The instruction is identical in fantasy, sci-fi, or soccer themes.

### Task Instruction Blocks

```
{{TASK_BUG_HUNT_N}}        → "Find and fix the N bugs in the code below."
{{TASK_IMPLEMENT}}         → "Implement the function according to the docstring."
{{TASK_PREDICT_OUTPUT}}    → "Predict what this code will print before running it."
{{TASK_COMPARE}}           → "Compare these two approaches. Which is better and why?"
{{TASK_TRACE}}             → "Trace through the code and track the variable values."
{{TASK_COMPLETE_FUNCTION}} → "Complete the function based on the signature and docstring."
{{TASK_TRAINING_LOOP}}     → "Build a loop that continues until the user quits."
```

### Usage in Templates

```python
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# {{TASK_BUG_HUNT_3}}
```

Renders (Fantasy):
```python
# Elena's spell-casting code from the last duel had critical flaws.
#
# Find and fix the 3 bugs in the code below.
```

Renders (Soccer):
```python
# Yael's penalty routine had flaws that Marco exploited.
#
# Find and fix the 3 bugs in the code below.
```

---

## Emotional Beats

Narrative arcs are composed from **generic emotional beats**. Each beat represents a stage in the learner's emotional journey.

### Beat Catalog

| Beat | Emotion | Description |
|------|---------|-------------|
| **SETBACK** | Defeat, failure | Something went wrong; must analyze and recover |
| **DISCOVERY** | Curiosity, understanding | Finding and comprehending something new |
| **INVESTIGATION** | Analysis, tracing | Looking deeper, following the trail |
| **GROWTH** | Determination, learning | Building strength, practicing, improving |
| **CONFRONTATION** | Challenge, tension | Facing the test, the showdown |
| **TRIUMPH** | Victory, mastery | Success, completion, pride |
| **EVALUATION** | Judgment, comparison | Weighing options, deciding between approaches |
| **OWNERSHIP** | Responsibility, agency | Taking control, making it yours |
| **GUIDANCE** | Support, scaffolding | Being taught, following expert lead |
| **IMPROVEMENT** | Refinement, polish | Making something better than before |

---

## Context Blocks for Beats

Each emotional beat has corresponding Layer 2 context blocks:

### Block Naming Pattern

```
{{CONTEXT_{BEAT}_INTRO}}      # Opening for this beat
{{CONTEXT_{BEAT}_NARRATIVE}}  # Story/instructions for this beat
{{CONTEXT_{BEAT}_COMPLETE}}   # Closing for this beat (optional)
```

### Full Block List

| Beat | Intro Block | Narrative Block | Complete Block |
|------|-------------|-----------------|----------------|
| SETBACK | `{{CONTEXT_SETBACK_INTRO}}` | `{{CONTEXT_SETBACK_NARRATIVE}}` | - |
| DISCOVERY | `{{CONTEXT_DISCOVERY_INTRO}}` | `{{CONTEXT_DISCOVERY_NARRATIVE}}` | - |
| INVESTIGATION | `{{CONTEXT_INVESTIGATION_INTRO}}` | `{{CONTEXT_INVESTIGATION_NARRATIVE}}` | - |
| GROWTH | `{{CONTEXT_GROWTH_INTRO}}` | `{{CONTEXT_GROWTH_NARRATIVE}}` | - |
| CONFRONTATION | `{{CONTEXT_CONFRONTATION_INTRO}}` | `{{CONTEXT_CONFRONTATION_NARRATIVE}}` | - |
| TRIUMPH | - | - | `{{CONTEXT_TRIUMPH_COMPLETE}}` |
| EVALUATION | `{{CONTEXT_EVALUATION_INTRO}}` | `{{CONTEXT_EVALUATION_NARRATIVE}}` | - |
| OWNERSHIP | `{{CONTEXT_OWNERSHIP_INTRO}}` | `{{CONTEXT_OWNERSHIP_NARRATIVE}}` | - |
| GUIDANCE | `{{CONTEXT_GUIDANCE_INTRO}}` | `{{CONTEXT_GUIDANCE_NARRATIVE}}` | - |
| IMPROVEMENT | `{{CONTEXT_IMPROVEMENT_INTRO}}` | `{{CONTEXT_IMPROVEMENT_NARRATIVE}}` | - |

---

## Narrative Arcs

### Arc 1: The Rivalry

**Emotional journey:** Humiliation → Determination → Triumph

**Story:** Defeated by a rival, train hard, face them again and win.

| Part | Beat | Exercise Type | Purpose |
|------|------|---------------|---------|
| 1 | SETBACK | bug_hunt | Analyze the defeat, find what went wrong |
| 2 | GROWTH | write_code | Build new abilities, practice |
| 3 | CONFRONTATION | write_code | Face the rival, prove mastery |
| Close | TRIUMPH | - | Victory message |

**Context blocks used:**
```
{{CONTEXT_SETBACK_INTRO}}
{{CONTEXT_SETBACK_NARRATIVE}}
{{CONTEXT_GROWTH_INTRO}}
{{CONTEXT_GROWTH_NARRATIVE}}
{{CONTEXT_CONFRONTATION_INTRO}}
{{CONTEXT_CONFRONTATION_NARRATIVE}}
{{CONTEXT_TRIUMPH_COMPLETE}}
```

---

### Arc 2: The Inheritance

**Emotional journey:** Curiosity → Understanding → Ownership → Pride

**Story:** Inherit code from someone who left, understand it, make it yours.

| Part | Beat | Exercise Type | Purpose |
|------|------|---------------|---------|
| 1 | DISCOVERY | code_tracing, output_prediction | Understand the inherited system |
| 2 | OWNERSHIP | write_code | Add your own feature |
| 3 | INVESTIGATION | bug_hunt | Find and fix hidden issues |
| Close | TRIUMPH | - | The system is now yours |

**Context blocks used:**
```
{{CONTEXT_DISCOVERY_INTRO}}
{{CONTEXT_DISCOVERY_NARRATIVE}}
{{CONTEXT_OWNERSHIP_INTRO}}
{{CONTEXT_OWNERSHIP_NARRATIVE}}
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_NARRATIVE}}
{{CONTEXT_TRIUMPH_COMPLETE}}
```

---

### Arc 3: The Rescue

**Emotional journey:** Urgency → Investigation → Relief → Improvement

**Story:** Something is broken, people depend on you, fix it and make it better.

| Part | Beat | Exercise Type | Purpose |
|------|------|---------------|---------|
| 1 | SETBACK | decode_error | Understand the crisis |
| 2 | INVESTIGATION | bug_hunt | Find and fix the problem |
| 3 | IMPROVEMENT | simplify_code, add_error_handling | Prevent future failures |
| Close | TRIUMPH | - | System saved and improved |

**Context blocks used:**
```
{{CONTEXT_SETBACK_INTRO}}
{{CONTEXT_SETBACK_NARRATIVE}}
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_NARRATIVE}}
{{CONTEXT_IMPROVEMENT_INTRO}}
{{CONTEXT_IMPROVEMENT_NARRATIVE}}
{{CONTEXT_TRIUMPH_COMPLETE}}
```

---

### Arc 4: The Apprentice

**Emotional journey:** Observation → Imitation → Independence → Mastery

**Story:** Learn from a master, practice with guidance, then create independently.

| Part | Beat | Exercise Type | Purpose |
|------|------|---------------|---------|
| 1 | DISCOVERY | output_prediction | Study the master's work |
| 2 | GUIDANCE | fill_blanks, complete_function | Practice with scaffolding |
| 3 | GROWTH | write_code | Create your own version |
| Close | TRIUMPH | - | You have surpassed the teacher |

**Context blocks used:**
```
{{CONTEXT_DISCOVERY_INTRO}}
{{CONTEXT_DISCOVERY_NARRATIVE}}
{{CONTEXT_GUIDANCE_INTRO}}
{{CONTEXT_GUIDANCE_NARRATIVE}}
{{CONTEXT_GROWTH_INTRO}}
{{CONTEXT_GROWTH_NARRATIVE}}
{{CONTEXT_TRIUMPH_COMPLETE}}
```

---

### Arc 5: The Mystery

**Emotional journey:** Surprise → Investigation → Discovery → Resolution

**Story:** Code does something unexpected, investigate why, fix it.

| Part | Beat | Exercise Type | Purpose |
|------|------|---------------|---------|
| 1 | DISCOVERY | output_prediction (with twist) | Observe unexpected behavior |
| 2 | INVESTIGATION | code_tracing | Trace to find the cause |
| 3 | IMPROVEMENT | bug_hunt | Fix the issue |
| Close | TRIUMPH | - | Mystery solved |

**Context blocks used:**
```
{{CONTEXT_DISCOVERY_INTRO}}
{{CONTEXT_DISCOVERY_NARRATIVE}}
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_NARRATIVE}}
{{CONTEXT_IMPROVEMENT_INTRO}}
{{CONTEXT_IMPROVEMENT_NARRATIVE}}
{{CONTEXT_TRIUMPH_COMPLETE}}
```

---

### Arc 6: The Upgrade

**Emotional journey:** Dissatisfaction → Understanding → Improvement → Satisfaction

**Story:** Working but ugly code needs to be cleaned up.

| Part | Beat | Exercise Type | Purpose |
|------|------|---------------|---------|
| 1 | EVALUATION | which_is_better, spot_difference | See what's wrong |
| 2 | DISCOVERY | output_prediction | Understand what it does |
| 3 | IMPROVEMENT | simplify_code | Make it better |
| Close | TRIUMPH | - | Clean, elegant code |

**Context blocks used:**
```
{{CONTEXT_EVALUATION_INTRO}}
{{CONTEXT_EVALUATION_NARRATIVE}}
{{CONTEXT_DISCOVERY_INTRO}}
{{CONTEXT_DISCOVERY_NARRATIVE}}
{{CONTEXT_IMPROVEMENT_INTRO}}
{{CONTEXT_IMPROVEMENT_NARRATIVE}}
{{CONTEXT_TRIUMPH_COMPLETE}}
```

---

### Arc 7: The Competition

**Emotional journey:** Evaluation → Judgment → Ambition → Creation

**Story:** Two solutions exist, evaluate them, then build your own better one.

| Part | Beat | Exercise Type | Purpose |
|------|------|---------------|---------|
| 1 | EVALUATION | which_is_better | Compare existing approaches |
| 2 | GROWTH | write_code | Build your own approach |
| 3 | EVALUATION | which_is_better (reflection) | Compare yours to the best |
| Close | TRIUMPH | - | Your solution stands strong |

**Context blocks used:**
```
{{CONTEXT_EVALUATION_INTRO}}
{{CONTEXT_EVALUATION_NARRATIVE}}
{{CONTEXT_GROWTH_INTRO}}
{{CONTEXT_GROWTH_NARRATIVE}}
{{CONTEXT_TRIUMPH_COMPLETE}}
```

---

## Arc Selection Guide

| Choose This Arc | When You Want Students To... |
|-----------------|------------------------------|
| **Rivalry** | Experience defeat, train, and triumph |
| **Inheritance** | Take ownership of existing code |
| **Rescue** | Feel urgency and save something broken |
| **Apprentice** | Learn progressively with scaffolding |
| **Mystery** | Investigate unexpected behavior |
| **Upgrade** | Refactor and improve code quality |
| **Competition** | Evaluate and surpass existing solutions |

---

## Module Compatibility

Not all arcs work well in all modules. Consider what exercise types are available:

| Arc | Requires | Best For Modules |
|-----|----------|------------------|
| Rivalry | bug_hunt, write_code | 3, 4, 5, 7 |
| Inheritance | code_tracing/output_prediction, write_code, bug_hunt | 3, 4, 5, 7 |
| Rescue | decode_error, bug_hunt, simplify_code/add_error_handling | 5, 7, 8 |
| Apprentice | output_prediction, fill_blanks/complete_function, write_code | 0, 1, 3, 5 |
| Mystery | output_prediction, code_tracing, bug_hunt | 1, 2, 3, 4 |
| Upgrade | which_is_better, output_prediction, simplify_code | 3, 5, 7 |
| Competition | which_is_better, write_code | 3, 5, 7, 9 |

---

## File Structure for Hybrid Exercises

Hybrid exercises live in a dedicated directory:

```
raw_exercises/
└── module_N_topic/
    └── hybrid/
        └── exercise_1_arc_name.py
```

### Naming Convention

```
exercise_{number}_{arc}_{theme_hint}.py
```

Examples:
- `exercise_1_rivalry_game_loop.py`
- `exercise_2_inheritance_data_system.py`
- `exercise_1_apprentice_list_basics.py`

---

## Writing Hybrid Exercises

### Template Structure

```python
"""
{{CONTEXT_{ARC}_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""

# ============================================================
# PART 1: {Beat Name}
# ============================================================
# {{CONTEXT_{BEAT1}_INTRO}}
# {{CONTEXT_{BEAT1}_NARRATIVE}}

# [Exercise type 1 content here]


# ============================================================
# PART 2: {Beat Name}
# ============================================================
# {{CONTEXT_{BEAT2}_INTRO}}
# {{CONTEXT_{BEAT2}_NARRATIVE}}

# [Exercise type 2 content here]


# ============================================================
# PART 3: {Beat Name}
# ============================================================
# {{CONTEXT_{BEAT3}_INTRO}}
# {{CONTEXT_{BEAT3}_NARRATIVE}}

# [Exercise type 3 content here]


def main():
    # Run all parts
    pass


if __name__ == "__main__":
    main()
    print()
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
```

---

## Theme File Additions

When using hybrid exercises, theme files must include the emotional beat blocks.

### Required Additions to `theme_mappings/*.json`

```json
{
  "layer_2_context_blocks": {
    "emotional_beats": {
      "CONTEXT_SETBACK_INTRO": "...",
      "CONTEXT_SETBACK_NARRATIVE": "...",
      "CONTEXT_DISCOVERY_INTRO": "...",
      "CONTEXT_DISCOVERY_NARRATIVE": "...",
      "CONTEXT_INVESTIGATION_INTRO": "...",
      "CONTEXT_INVESTIGATION_NARRATIVE": "...",
      "CONTEXT_GROWTH_INTRO": "...",
      "CONTEXT_GROWTH_NARRATIVE": "...",
      "CONTEXT_CONFRONTATION_INTRO": "...",
      "CONTEXT_CONFRONTATION_NARRATIVE": "...",
      "CONTEXT_EVALUATION_INTRO": "...",
      "CONTEXT_EVALUATION_NARRATIVE": "...",
      "CONTEXT_OWNERSHIP_INTRO": "...",
      "CONTEXT_OWNERSHIP_NARRATIVE": "...",
      "CONTEXT_GUIDANCE_INTRO": "...",
      "CONTEXT_GUIDANCE_NARRATIVE": "...",
      "CONTEXT_IMPROVEMENT_INTRO": "...",
      "CONTEXT_IMPROVEMENT_NARRATIVE": "...",
      "CONTEXT_TRIUMPH_COMPLETE": "..."
    }
  }
}
```

---

## Example Theme Values

### Fantasy Theme

```json
"CONTEXT_SETBACK_INTRO": "{{villain}} has bested {{hero}} in combat. Every defeat teaches a lesson.",
"CONTEXT_SETBACK_NARRATIVE": "Examine {{hero}}'s failed spell. What went wrong in the incantation?",
"CONTEXT_GROWTH_INTRO": "{{hero}} retreats to the training grounds. New abilities must be mastered.",
"CONTEXT_GROWTH_NARRATIVE": "Learn this technique. {{mentor}} believes it will turn the tide.",
"CONTEXT_CONFRONTATION_INTRO": "The final duel. {{hero}} faces {{villain}} in {{location}}.",
"CONTEXT_CONFRONTATION_NARRATIVE": "Channel everything you've learned. Cast the winning spell.",
"CONTEXT_TRIUMPH_COMPLETE": "{{exclamation}} {{hero}} has defeated {{villain}}! {{school}} celebrates!"
```

### Sci-Fi Theme

```json
"CONTEXT_SETBACK_INTRO": "{{villain}}'s fleet destroyed {{hero}}'s prototype. Time to analyze the failure.",
"CONTEXT_SETBACK_NARRATIVE": "Review the failed system logs. Identify the critical malfunction.",
"CONTEXT_GROWTH_INTRO": "Back at {{school}}, {{hero}} develops countermeasures.",
"CONTEXT_GROWTH_NARRATIVE": "Engineer this new module. It could be the tactical advantage needed.",
"CONTEXT_CONFRONTATION_INTRO": "The fleets meet at {{location}}. This battle decides everything.",
"CONTEXT_CONFRONTATION_NARRATIVE": "Deploy your systems. Execute the winning strategy.",
"CONTEXT_TRIUMPH_COMPLETE": "{{exclamation}} {{villain}}'s fleet is disabled! {{hero}} has saved {{school}}!"
```

### Professional/Plain Theme

```json
"CONTEXT_SETBACK_INTRO": "The previous implementation failed code review. Let's understand why.",
"CONTEXT_SETBACK_NARRATIVE": "Examine the rejected code. Identify the issues.",
"CONTEXT_GROWTH_INTRO": "Time to develop a better approach.",
"CONTEXT_GROWTH_NARRATIVE": "Implement this improved solution using what you've learned.",
"CONTEXT_CONFRONTATION_INTRO": "Final implementation. Make it production-ready.",
"CONTEXT_CONFRONTATION_NARRATIVE": "Write the complete solution. This is your submission.",
"CONTEXT_TRIUMPH_COMPLETE": "Excellent work! Your code passed all reviews and is ready for deployment."
```

---

## Quick Reference

| Need | See |
|------|-----|
| Available beats | [Beat Catalog](#beat-catalog) |
| Arc structures | [Narrative Arcs](#narrative-arcs) |
| Module compatibility | [Module Compatibility](#module-compatibility) |
| File structure | [File Structure for Hybrid Exercises](#file-structure-for-hybrid-exercises) |
| Theme additions | [Theme File Additions](#theme-file-additions) |
