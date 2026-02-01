# Universal Narrative Template System v2.0

**Purpose:** Genre-agnostic narrative templates that work for fantasy, sci-fi, sports, music, business, or any other domain.

**Key Innovation:** Uses three-layer placeholders (entity names + context blocks + framework concepts) to generate appropriate narratives for any genre.

---

## Table of Contents

1. [Template Architecture](#template-architecture)
2. [15 Universal Narrative Templates](#15-universal-narrative-templates)
3. [Context Block Library](#context-block-library)
4. [Implementation Examples](#implementation-examples)
5. [Migration Guide](#migration-guide)

---

## Template Architecture

### Three-Layer System

**Layer 1: Entity Names** (existing)
- `{{hero}}`, `{{item}}`, `{{school}}`, `{{mentor}}`
- Simple string replacements

**Layer 2: Narrative Context Blocks** (NEW)
- `{{CONTEXT_INTRO}}`, `{{CONTEXT_ACTION}}`, `{{CONTEXT_RESULT}}`
- Full sentences or paragraphs that swap by genre
- Provides narrative flavor while keeping code structure identical

**Layer 3: Framework Concepts** (NEW)
- `{{INSTITUTION_TYPE}}`, `{{CATEGORY_SYSTEM}}`, `{{ABILITY_TYPE}}`
- Structural elements that define universe rules
- Used in documentation and meta-descriptions

---

## 15 Universal Narrative Templates

Based on the pattern analysis, here are 15 universal templates that work across all genres:

---

### Template 1: The Tutorial Guide

**Purpose:** Teach a new concept by showing complete example first, then asking student to replicate.

**Structure:**
```python
# {{CONTEXT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}

# EXAMPLE: {{EXAMPLE_TITLE}}
# {{CONTEXT_EXAMPLE_NARRATIVE}}

def example_function():
    """Complete working example to study."""
    # Implementation here
    pass

# ✏️ YOUR TURN ✏️
# {{CONTEXT_STUDENT_TASK}}
# {{CONTEXT_SUCCESS_CRITERIA}}

def student_function():
    """{{TASK_DESCRIPTION}}"""
    pass
```

**Context Blocks Needed:**
- `{{CONTEXT_INTRO}}`: Opening that places student in learning situation
- `{{CONTEXT_LEARNING_OBJECTIVE}}`: What they'll learn
- `{{CONTEXT_EXAMPLE_NARRATIVE}}`: Story explaining the example
- `{{CONTEXT_STUDENT_TASK}}`: Instructions for replication
- `{{CONTEXT_SUCCESS_CRITERIA}}`: How to know they succeeded

**Example Values by Genre:**

**Fantasy (dumblecode):**
```
CONTEXT_INTRO: "Welcome to your first day at {{school}}! Before you can cast your own spells, you must study the masters."
CONTEXT_LEARNING_OBJECTIVE: "You'll learn how to structure spell formulas using dictionaries."
CONTEXT_EXAMPLE_NARRATIVE: "Here's how {{mentor}} teaches {{spell1}} to first-years:"
CONTEXT_STUDENT_TASK: "Now craft your own spell using the same pattern."
CONTEXT_SUCCESS_CRITERIA: "Your spell should have name, power, and effect properties."
```

**Sci-fi (starfleet):**
```
CONTEXT_INTRO: "Welcome aboard {{school}}, Cadet! All crew must complete systems training before their first shift."
CONTEXT_LEARNING_OBJECTIVE: "You'll learn how to structure ship system protocols using data records."
CONTEXT_EXAMPLE_NARRATIVE: "Here's how the Engineering Chief configures the {{item_1}} system:"
CONTEXT_STUDENT_TASK: "Now configure your assigned system using the same protocol structure."
CONTEXT_SUCCESS_CRITERIA: "Your system config should have designation, power_draw, and status fields."
```

**Sports (academy):**
```
CONTEXT_INTRO: "Welcome to {{school}}, rookie! Before you hit the field, you need to understand the playbook."
CONTEXT_LEARNING_OBJECTIVE: "You'll learn how to structure play formations using game plans."
CONTEXT_EXAMPLE_NARRATIVE: "Here's how Coach {{mentor}} diagrams the {{ability_1}} play:"
CONTEXT_STUDENT_TASK: "Now design your own play using the same structure."
CONTEXT_SUCCESS_CRITERIA: "Your play should have name, formation, and objective fields."
```

---

### Template 2: The Incremental Builder

**Purpose:** Build a complex system one feature at a time across multiple sub-exercises.

**Structure:**
```python
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_INCREMENTAL_NARRATIVE}}

# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}

def exercise_a():
    """{{PHASE_1_DESCRIPTION}}"""
    # ✏️ YOUR CODE HERE ✏️
    pass

# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}

def exercise_b():
    """{{PHASE_2_DESCRIPTION}}"""
    # ✏️ YOUR CODE HERE ✏️
    pass

# ... continue for phases 3-5 ...

# ============================================================
# {{CONTEXT_INTEGRATION}}
# ============================================================

def main():
    """{{CONTEXT_FINAL_ASSEMBLY}}"""
    exercise_a()
    exercise_b()
    # etc.
```

**Context Blocks Needed:**
- `{{CONTEXT_PROJECT_INTRO}}`: Overall project framing
- `{{CONTEXT_INCREMENTAL_NARRATIVE}}`: Why building piece by piece
- `{{CONTEXT_PHASE_N}}`: What each phase accomplishes
- `{{CONTEXT_INTEGRATION}}`: How pieces fit together
- `{{CONTEXT_FINAL_ASSEMBLY}}`: The completed system description

**Example Values by Genre:**

**Fantasy:**
```
CONTEXT_PROJECT_INTRO: "Your first assignment at {{school}}: create your personal spellbook."
CONTEXT_INCREMENTAL_NARRATIVE: "Like all great {{practitioner_plural}}, you'll start simple and expand your grimoire over time."
PHASE_1_TITLE: "Step 1: The Foundation Spell"
CONTEXT_PHASE_1: "Every spellbook begins with a basic spell. Create a dictionary to store your first spell's properties."
PHASE_2_TITLE: "Step 2: Reading Your Spells"
CONTEXT_PHASE_2: "Now that your spell exists, practice accessing its power level and effects."
CONTEXT_INTEGRATION: "The Complete Grimoire"
CONTEXT_FINAL_ASSEMBLY: "Run all exercises to see your spellbook come to life!"
```

**Music (conservatory):**
```
CONTEXT_PROJECT_INTRO: "Welcome to {{school}} Composition Class! Today you'll build your first digital music catalog."
CONTEXT_INCREMENTAL_NARRATIVE: "Like all great composers, you'll organize your works methodically."
PHASE_1_TITLE: "Movement 1: Define Your First Piece"
CONTEXT_PHASE_1: "Every catalog starts with a single composition. Create a record for your first piece with title, tempo, and key signature."
PHASE_2_TITLE: "Movement 2: Reading Your Catalog"
CONTEXT_PHASE_2: "Now that your piece is recorded, practice accessing its tempo and other properties."
CONTEXT_INTEGRATION: "The Complete Portfolio"
CONTEXT_FINAL_ASSEMBLY: "Run all movements to hear your catalog in action!"
```

---

### Template 3: The Role Assignment

**Purpose:** Place student in specific role with responsibilities.

**Structure:**
```python
"""
{{CONTEXT_ROLE_INTRO}}
{{CONTEXT_ROLE_RESPONSIBILITIES}}
{{CONTEXT_ROLE_CHALLENGE}}
"""

# {{CONTEXT_SITUATION_SETUP}}

def role_task_1():
    """{{TASK_1_DESCRIPTION}}"""
    # {{CONTEXT_TASK_1_GUIDANCE}}
    # ✏️ YOUR CODE HERE ✏️
    pass

def role_task_2():
    """{{TASK_2_DESCRIPTION}}"""
    # {{CONTEXT_TASK_2_GUIDANCE}}
    # ✏️ YOUR CODE HERE ✏️
    pass

def main():
    print("{{CONTEXT_ROLE_START}}")
    print("=" * 50)

    role_task_1()
    role_task_2()

    print("=" * 50)
    print("{{CONTEXT_ROLE_COMPLETE}}")
```

**Context Blocks Needed:**
- `{{CONTEXT_ROLE_INTRO}}`: Who the student is in this scenario
- `{{CONTEXT_ROLE_RESPONSIBILITIES}}`: What their job entails
- `{{CONTEXT_ROLE_CHALLENGE}}`: The problem they need to solve
- `{{CONTEXT_SITUATION_SETUP}}`: Current situation
- `{{CONTEXT_ROLE_START}}`: Opening message when exercise begins
- `{{CONTEXT_ROLE_COMPLETE}}`: Closing message when finished

**Example Values by Genre:**

**Fantasy:**
```
CONTEXT_ROLE_INTRO: "You are the new Inventory Keeper at {{school}}."
CONTEXT_ROLE_RESPONSIBILITIES: "Your job is to track all magical items, supplies, and equipment used by students and staff."
CONTEXT_ROLE_CHALLENGE: "The previous keeper's records are in chaos! You must organize everything using proper data structures."
CONTEXT_SITUATION_SETUP: "It's the morning of September 1st. Hundreds of students are arriving today, and they're all asking for their supplies!"
CONTEXT_ROLE_START: "{{hero}}'s INVENTORY MANAGEMENT SYSTEM"
CONTEXT_ROLE_COMPLETE: "Excellent work, Inventory Keeper! The supplies are organized and ready for distribution."
```

**Business (startup):**
```
CONTEXT_ROLE_INTRO: "You are the new Product Manager at {{school}} (a fast-growing tech startup)."
CONTEXT_ROLE_RESPONSIBILITIES: "Your job is to track all product features, user requests, and development priorities."
CONTEXT_ROLE_CHALLENGE: "The previous PM's backlog is a mess! You must organize everything using proper data structures."
CONTEXT_SITUATION_SETUP: "It's Monday morning. Your team sprint starts today, and everyone's asking what to build next!"
CONTEXT_ROLE_START: "{{hero}}'s PRODUCT BACKLOG SYSTEM"
CONTEXT_ROLE_COMPLETE: "Great work, PM! The backlog is prioritized and the team knows what to build."
```

---

### Template 4: The Forensic Debugger

**Purpose:** Debug broken code by investigating error messages and tracing execution.

**Structure:**
```python
"""
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_MISSION}}
"""

# ============================================================
# {{CASE_1_TITLE}}
# ============================================================
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# ERROR MESSAGE:
# {{ERROR_MESSAGE_1}}
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

def case_1_buggy():
    """{{CASE_1_DESCRIPTION}}"""
    # 🐛 BUG: {{BUG_1_HINT}}
    # Buggy code here
    pass

# ✏️ FIX THE CODE ✏️
def case_1_fixed():
    """{{CASE_1_FIX_DESCRIPTION}}"""
    pass

# ... repeat for cases 2-N ...
```

**Context Blocks Needed:**
- `{{CONTEXT_INVESTIGATION_INTRO}}`: Framing as investigation/debugging
- `{{CONTEXT_INVESTIGATION_MISSION}}`: What needs to be fixed
- `{{CONTEXT_CASE_N_NARRATIVE}}`: Story behind each bug
- `{{CONTEXT_INVESTIGATION_PROMPT_N}}`: Questions to guide debugging

**Example Values by Genre:**

**Fantasy:**
```
CONTEXT_INVESTIGATION_INTRO: "Oh no! Several spells at {{school}} have been sabotaged!"
CONTEXT_INVESTIGATION_MISSION: "As a member of the Spell Debugging Squad, you must identify what went wrong and restore each spell to working order."
CASE_1_TITLE: "Case #1: The Levitation Malfunction"
CONTEXT_CASE_1_NARRATIVE: "{{friend_1}} tried to levitate their books, but the spell crashed instead of lifting anything."
ERROR_MESSAGE_1: "KeyError: 'target'"
CONTEXT_INVESTIGATION_PROMPT_1: "Examine the spell code. What's missing from the spell dictionary? How can you fix it?"
BUG_1_HINT: "The spell is trying to access a key that doesn't exist"
```

**Sci-fi:**
```
CONTEXT_INVESTIGATION_INTRO: "ALERT! Multiple ship systems aboard {{school}} are malfunctioning!"
CONTEXT_INVESTIGATION_MISSION: "As a Systems Diagnostics Engineer, you must identify the errors in each module and restore normal operations."
CASE_1_TITLE: "Incident #1: Life Support Data Corruption"
CONTEXT_CASE_1_NARRATIVE: "{{friend_1}} tried to query oxygen levels, but the system returned a fatal error instead."
ERROR_MESSAGE_1: "KeyError: 'oxygen_level'"
CONTEXT_INVESTIGATION_PROMPT_1: "Examine the sensor data structure. What field is the system looking for? Why isn't it there?"
BUG_1_HINT: "The data record is missing a required field"
```

---

### Template 5: The Comparison Analyst

**Purpose:** Compare two approaches and analyze tradeoffs.

**Structure:**
```python
"""
{{CONTEXT_COMPARISON_INTRO}}
{{CONTEXT_COMPARISON_DECISION}}
"""

# ============================================================
# {{APPROACH_1_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_1_NARRATIVE}}

def approach_1_example():
    """{{APPROACH_1_DESCRIPTION}}"""
    # Implementation of approach 1
    pass

# ============================================================
# {{APPROACH_2_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_2_NARRATIVE}}

def approach_2_example():
    """{{APPROACH_2_DESCRIPTION}}"""
    # Implementation of approach 2
    pass

# ============================================================
# ✏️ YOUR ANALYSIS ✏️
# ============================================================
# {{CONTEXT_ANALYSIS_PROMPT}}
#
# Questions to consider:
# 1. {{ANALYSIS_QUESTION_1}}
# 2. {{ANALYSIS_QUESTION_2}}
# 3. {{ANALYSIS_QUESTION_3}}
#
# Which approach do you prefer and why?
# {{CONTEXT_DECISION_GUIDANCE}}
```

**Context Blocks Needed:**
- `{{CONTEXT_COMPARISON_INTRO}}`: Why comparison matters
- `{{CONTEXT_COMPARISON_DECISION}}`: What decision needs to be made
- `{{CONTEXT_APPROACH_N_NARRATIVE}}`: Story explaining each approach
- `{{CONTEXT_ANALYSIS_PROMPT}}`: How to think about tradeoffs
- `{{CONTEXT_DECISION_GUIDANCE}}`: Criteria for good decision

**Example Values by Genre:**

**Fantasy:**
```
CONTEXT_COMPARISON_INTRO: "{{mentor}} has challenged your class to optimize spell storage."
CONTEXT_COMPARISON_DECISION: "Two senior students have proposed different spellbook structures. Which is better?"
APPROACH_1_NAME: "Approach A: The Flat Grimoire"
CONTEXT_APPROACH_1_NARRATIVE: "{{friend_1}} prefers keeping all spell data in a single-level dictionary with simple keys."
APPROACH_2_NAME: "Approach B: The Nested Tome"
CONTEXT_APPROACH_2_NARRATIVE: "{{friend_2}} argues that grouping related spell properties in nested dictionaries is clearer."
CONTEXT_ANALYSIS_PROMPT: "As an apprentice spellcrafter, you must evaluate both approaches and defend your choice."
ANALYSIS_QUESTION_1: "Which structure makes it easier to access a spell's power level?"
ANALYSIS_QUESTION_2: "Which structure makes it easier to add new spell properties later?"
ANALYSIS_QUESTION_3: "Which structure is more readable for other wizards reviewing your spellbook?"
CONTEXT_DECISION_GUIDANCE: "Consider: simplicity vs. organization, performance vs. maintainability, current needs vs. future growth."
```

**Business:**
```
CONTEXT_COMPARISON_INTRO: "Your product team at {{school}} needs to choose how to structure customer data."
CONTEXT_COMPARISON_DECISION: "Two engineers have proposed different database schemas. Which should the team adopt?"
APPROACH_1_NAME: "Proposal A: The Flat Schema"
CONTEXT_APPROACH_1_NARRATIVE: "{{friend_1}} (Senior Engineer) prefers a simple table with all customer fields at the top level."
APPROACH_2_NAME: "Proposal B: The Normalized Schema"
CONTEXT_APPROACH_2_NARRATIVE: "{{friend_2}} (Lead Architect) argues for separating customer info, preferences, and history into related tables."
CONTEXT_ANALYSIS_PROMPT: "As the Product Manager, you must evaluate both proposals and make a recommendation to the CTO."
ANALYSIS_QUESTION_1: "Which schema makes it faster to query a customer's email address?"
ANALYSIS_QUESTION_2: "Which schema makes it easier to add new types of customer preferences?"
ANALYSIS_QUESTION_3: "Which schema will scale better as we grow from 1K to 1M customers?"
CONTEXT_DECISION_GUIDANCE: "Consider: query performance, schema flexibility, data integrity, team familiarity with each approach."
```

---

### Template 6: The Specification Implementer

**Purpose:** Implement functionality from comprehensive specifications (like real-world development).

**Structure:**
```python
"""
{{CONTEXT_SPEC_INTRO}}
{{CONTEXT_SPEC_SOURCE}}
"""

# ============================================================
# SPECIFICATION: {{COMPONENT_NAME}}
# ============================================================
# {{CONTEXT_SPEC_NARRATIVE}}
#
# Requirements:
# {{REQUIREMENT_1}}
# {{REQUIREMENT_2}}
# {{REQUIREMENT_3}}
#
# {{CONTEXT_SPEC_CONSTRAINTS}}

def implement_spec():
    """
    {{SPEC_SUMMARY}}

    Args:
        {{ARG_SPEC}}

    Returns:
        {{RETURN_SPEC}}

    Examples:
        {{EXAMPLE_1}}
        {{EXAMPLE_2}}

    {{CONTEXT_IMPLEMENTATION_GUIDANCE}}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass
```

**Context Blocks Needed:**
- `{{CONTEXT_SPEC_INTRO}}`: Why specifications matter
- `{{CONTEXT_SPEC_SOURCE}}`: Who wrote the spec and why
- `{{CONTEXT_SPEC_NARRATIVE}}`: Story context for the component
- `{{CONTEXT_SPEC_CONSTRAINTS}}`: Any limitations or considerations
- `{{CONTEXT_IMPLEMENTATION_GUIDANCE}}`: Tips for implementation

**Example Values by Genre:**

**Fantasy:**
```
CONTEXT_SPEC_INTRO: "Professional spellcrafters at {{school}} never start coding without a proper spell specification."
CONTEXT_SPEC_SOURCE: "{{mentor}} has written the requirements for a new defensive spell. Your job is to implement it according to spec."
COMPONENT_NAME: "Shield Charm v2.0"
CONTEXT_SPEC_NARRATIVE: "The old Shield Charm is outdated. We need a new version that can protect against multiple threat types."
REQUIREMENT_1: "- Must accept a list of threat types to block (e.g., ['fire', 'ice', 'lightning'])"
REQUIREMENT_2: "- Must return True if shield successfully forms, False if invalid threat types provided"
REQUIREMENT_3: "- Must store the shield's strength as a number from 1-10 based on caster's power level"
CONTEXT_SPEC_CONSTRAINTS: "Note: Shield cannot block more than 5 threat types at once (magical limit)."
CONTEXT_IMPLEMENTATION_GUIDANCE: "Start by validating inputs, then create the shield data structure, then return success/failure."
```

**Sci-fi:**
```
CONTEXT_SPEC_INTRO: "Professional engineers aboard {{school}} always work from detailed system specifications."
CONTEXT_SPEC_SOURCE: "The Chief Engineer has written the requirements for a new sensor module. Your job is to implement it according to spec."
COMPONENT_NAME: "Multi-Spectrum Scanner v3.1"
CONTEXT_SPEC_NARRATIVE: "The old scanner only detects basic anomalies. We need an upgraded version that can track multiple signal types."
REQUIREMENT_1: "- Must accept a list of signal frequencies to monitor (e.g., ['radio', 'infrared', 'subspace'])"
REQUIREMENT_2: "- Must return True if scanner calibration succeeds, False if invalid frequencies provided"
REQUIREMENT_3: "- Must store the scanner's sensitivity as a number from 1-10 based on power allocation"
CONTEXT_SPEC_CONSTRAINTS: "Note: Scanner cannot monitor more than 5 frequencies simultaneously (hardware limit)."
CONTEXT_IMPLEMENTATION_GUIDANCE: "Start by validating inputs, then configure the scanner parameters, then return calibration status."
```

---

### Template 7: The Prediction Challenger

**Purpose:** Test understanding by predicting code output before running.

**Structure:**
```python
"""
{{CONTEXT_PREDICTION_INTRO}}
{{CONTEXT_PREDICTION_PURPOSE}}
"""

# ============================================================
# {{CHALLENGE_1_TITLE}}
# ============================================================
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}
#
# ✏️ YOUR PREDICTION ✏️
# What will this code print? Write your answer below BEFORE running it:
#
# Predicted output:
# {{PREDICTION_PLACEHOLDER_1}}
#
# {{CONTEXT_PREDICTION_GUIDANCE_1}}

def challenge_1():
    """{{CHALLENGE_1_DESCRIPTION}}"""
    # Code to predict
    pass

# ... repeat for challenges 2-N ...

# ============================================================
# VERIFICATION
# ============================================================
# {{CONTEXT_VERIFICATION_PROMPT}}

def verify_predictions():
    """{{CONTEXT_VERIFICATION_NARRATIVE}}"""
    print("{{CONTEXT_VERIFICATION_START}}")
    challenge_1()
    # etc.
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")
```

**Context Blocks Needed:**
- `{{CONTEXT_PREDICTION_INTRO}}`: Why prediction matters
- `{{CONTEXT_PREDICTION_PURPOSE}}`: Skill being developed
- `{{CONTEXT_CHALLENGE_N_NARRATIVE}}`: Story context for each challenge
- `{{CONTEXT_PREDICTION_GUIDANCE_N}}`: Hints for thinking through it
- `{{CONTEXT_VERIFICATION_PROMPT}}`: Instructions for checking work
- `{{CONTEXT_VERIFICATION_START/COMPLETE}}`: Verification messages

**Example Values by Genre:**

**Fantasy:**
```
CONTEXT_PREDICTION_INTRO: "At {{school}}, advanced students learn to predict spell effects without casting them first."
CONTEXT_PREDICTION_PURPOSE: "This crucial skill prevents dangerous magical accidents. Today you'll practice predicting output without running the code."
CHALLENGE_1_TITLE: "Challenge 1: The Levitation Sequence"
CONTEXT_CHALLENGE_1_NARRATIVE: "{{friend_1}} has written a spell that levitates three objects in sequence. What will the enchantment announce?"
PREDICTION_PLACEHOLDER_1: "# Line 1:\n# Line 2:\n# Line 3:"
CONTEXT_PREDICTION_GUIDANCE_1: "Read the code line by line. What does each print statement output? Are there any surprises in variable values?"
CONTEXT_VERIFICATION_PROMPT: "Once you've written all your predictions, uncomment the verify function to see actual results."
CONTEXT_VERIFICATION_START: "=== ACTUAL SPELL EFFECTS ==="
CONTEXT_VERIFICATION_NARRATIVE: "Compare your predictions with the actual spell outputs. How accurate were you?"
CONTEXT_VERIFICATION_COMPLETE: "=== VERIFICATION COMPLETE ===="
```

**Sports:**
```
CONTEXT_PREDICTION_INTRO: "At {{school}}, pro-level athletes learn to visualize plays before executing them."
CONTEXT_PREDICTION_PURPOSE: "This crucial skill improves reaction time and decision-making. Today you'll practice predicting outcomes without running the code."
CHALLENGE_1_TITLE: "Play 1: The Triple Option"
CONTEXT_CHALLENGE_1_NARRATIVE: "Coach {{mentor}} has diagrammed a play that involves three possible routes. What will the announcer say as each route is called?"
PREDICTION_PLACEHOLDER_1: "# Call 1:\n# Call 2:\n# Call 3:"
CONTEXT_PREDICTION_GUIDANCE_1: "Read the playbook line by line. What does each announcement output? Are there any trick plays?"
CONTEXT_VERIFICATION_PROMPT: "Once you've written all your predictions, run the verification to see actual play calls."
CONTEXT_VERIFICATION_START: "=== ACTUAL PLAY EXECUTION ==="
CONTEXT_VERIFICATION_NARRATIVE: "Compare your predictions with the actual play calls. How accurate was your game sense?"
CONTEXT_VERIFICATION_COMPLETE: "=== PLAY REVIEW COMPLETE ===="
```

---

### Template 8: The Progressive Unlocking

**Purpose:** Build confidence with gated content that students activate when ready.

**Structure:**
```python
"""
{{CONTEXT_UNLOCKING_INTRO}}
{{CONTEXT_UNLOCKING_PROGRESSION}}
"""

# ============================================================
# {{STAGE_1_TITLE}} - AVAILABLE NOW
# ============================================================
# {{CONTEXT_STAGE_1_NARRATIVE}}

def stage_1():
    """{{STAGE_1_DESCRIPTION}}"""
    # ✏️ YOUR CODE HERE ✏️
    pass

# ============================================================
# {{STAGE_2_TITLE}} - UNLOCK AFTER STAGE 1
# ============================================================
# {{CONTEXT_STAGE_2_NARRATIVE}}
# {{CONTEXT_UNLOCK_INSTRUCTION_2}}

# def stage_2():
#     """{{STAGE_2_DESCRIPTION}}"""
#     # ✏️ YOUR CODE HERE ✏️
#     pass

# ... repeat for stages 3-N, all commented ...

def main():
    print("{{CONTEXT_PROGRESSION_START}}")

    stage_1()

    # {{CONTEXT_UNLOCK_REMINDER}}
    # stage_2()  # Uncomment when ready
    # stage_3()  # Uncomment when ready

    print("{{CONTEXT_PROGRESSION_STATUS}}")
```

**Context Blocks Needed:**
- `{{CONTEXT_UNLOCKING_INTRO}}`: Why progressive unlocking
- `{{CONTEXT_UNLOCKING_PROGRESSION}}`: Overall journey description
- `{{CONTEXT_STAGE_N_NARRATIVE}}`: What each stage unlocks
- `{{CONTEXT_UNLOCK_INSTRUCTION_N}}`: How to activate next stage
- `{{CONTEXT_UNLOCK_REMINDER}}`: Reminder about progression
- `{{CONTEXT_PROGRESSION_STATUS}}`: Current progress message

**Example Values by Genre:**

**Fantasy:**
```
CONTEXT_UNLOCKING_INTRO: "At {{school}}, advanced magic is taught in stages. You must master each level before unlocking the next."
CONTEXT_UNLOCKING_PROGRESSION: "This spellbook contains three increasingly powerful enchantments. Start with the basics and unlock more as you grow stronger."
STAGE_1_TITLE: "Level 1: Apprentice Spell"
CONTEXT_STAGE_1_NARRATIVE: "Every wizard begins here. This simple spell is safe for beginners."
STAGE_2_TITLE: "Level 2: Journeyman Spell [LOCKED]"
CONTEXT_STAGE_2_NARRATIVE: "This intermediate spell requires understanding from Level 1. Once you've completed the apprentice spell, you may attempt this."
CONTEXT_UNLOCK_INSTRUCTION_2: "To unlock: Uncomment the stage_2() function and its call in main()"
CONTEXT_UNLOCK_REMINDER: "# Uncomment stages as you complete previous ones!"
CONTEXT_PROGRESSION_START: "=== {{school}} SPELL PROGRESSION SYSTEM ==="
CONTEXT_PROGRESSION_STATUS: "Check which stages you've completed. Unlock the next when ready!"
```

**Music:**
```
CONTEXT_UNLOCKING_INTRO: "At {{school}} Conservatory, advanced techniques are taught in progressive stages. Master each level before moving forward."
CONTEXT_UNLOCKING_PROGRESSION: "This lesson contains three increasingly complex compositions. Start with fundamentals and unlock more as your skills develop."
STAGE_1_TITLE: "Movement 1: Basic Melody"
CONTEXT_STAGE_1_NARRATIVE: "Every composer begins here. This simple melody teaches core principles."
STAGE_2_TITLE: "Movement 2: Harmony [LOCKED]"
CONTEXT_STAGE_2_NARRATIVE: "This intermediate piece adds harmonic complexity. Once you've mastered the basic melody, you may attempt harmony."
CONTEXT_UNLOCK_INSTRUCTION_2: "To unlock: Uncomment the stage_2() function and its call in main()"
CONTEXT_UNLOCK_REMINDER: "# Uncomment movements as you complete previous ones!"
CONTEXT_PROGRESSION_START: "=== {{school}} COMPOSITION PROGRESSION SYSTEM ==="
CONTEXT_PROGRESSION_STATUS: "Review which movements you've completed. Unlock the next when ready!"
```

---

### Template 9: The World Builder

**Purpose:** Create interconnected systems where objects/entities interact.

**Structure:**
```python
"""
{{CONTEXT_WORLD_INTRO}}
{{CONTEXT_WORLD_VISION}}
"""

# ============================================================
# {{ENTITY_TYPE_1}} - {{ENTITY_TYPE_1_DESCRIPTION}}
# ============================================================
# {{CONTEXT_ENTITY_1_NARRATIVE}}

def create_entity_1():
    """{{ENTITY_1_CREATION_DESCRIPTION}}"""
    entity = {
        # ✏️ YOUR CODE HERE ✏️
    }
    return entity

# ============================================================
# {{ENTITY_TYPE_2}} - {{ENTITY_TYPE_2_DESCRIPTION}}
# ============================================================
# {{CONTEXT_ENTITY_2_NARRATIVE}}

def create_entity_2():
    """{{ENTITY_2_CREATION_DESCRIPTION}}"""
    entity = {
        # ✏️ YOUR CODE HERE ✏️
    }
    return entity

# ============================================================
# {{INTERACTION_TITLE}}
# ============================================================
# {{CONTEXT_INTERACTION_NARRATIVE}}

def entities_interact(entity1, entity2):
    """{{INTERACTION_DESCRIPTION}}"""
    # ✏️ YOUR CODE HERE ✏️
    pass

def main():
    print("{{CONTEXT_WORLD_BUILDING_START}}")

    e1 = create_entity_1()
    e2 = create_entity_2()

    entities_interact(e1, e2)

    print("{{CONTEXT_WORLD_BUILDING_COMPLETE}}")
```

**Context Blocks Needed:**
- `{{CONTEXT_WORLD_INTRO}}`: The world being created
- `{{CONTEXT_WORLD_VISION}}`: What the complete system will do
- `{{CONTEXT_ENTITY_N_NARRATIVE}}`: Story behind each entity type
- `{{CONTEXT_INTERACTION_NARRATIVE}}`: How entities relate
- `{{CONTEXT_WORLD_BUILDING_START/COMPLETE}}`: Framing messages

**Example Values by Genre:**

**Fantasy:**
```
CONTEXT_WORLD_INTRO: "Welcome to {{school}}'s Advanced Magical Systems class!"
CONTEXT_WORLD_VISION: "Today you'll build an ecosystem where wizards, spells, and magical creatures interact. Your code will simulate real magical dynamics."
ENTITY_TYPE_1: "WIZARD"
ENTITY_TYPE_1_DESCRIPTION: "Spell Casters"
CONTEXT_ENTITY_1_NARRATIVE: "Wizards are the primary magic users in your world. Each wizard has a name, power level, and list of known spells."
ENTITY_1_CREATION_DESCRIPTION: "Create a dictionary representing a wizard with: name (str), power_level (int), known_spells (list)"
ENTITY_TYPE_2: "MAGICAL CREATURE"
ENTITY_TYPE_2_DESCRIPTION: "Companions and Challenges"
CONTEXT_ENTITY_2_NARRATIVE: "Magical creatures can be befriended or battled. Each has a name, type (dragon/phoenix/unicorn), and disposition toward wizards."
ENTITY_2_CREATION_DESCRIPTION: "Create a dictionary representing a magical creature with: name (str), creature_type (str), friendly (bool)"
INTERACTION_TITLE: "WIZARD-CREATURE INTERACTION"
CONTEXT_INTERACTION_NARRATIVE: "When a wizard encounters a creature, the outcome depends on both entities' properties. Friendly creatures may offer aid; hostile ones may attack."
INTERACTION_DESCRIPTION: "Determine interaction outcome based on wizard's power and creature's disposition"
CONTEXT_WORLD_BUILDING_START: "=== BUILDING YOUR MAGICAL ECOSYSTEM ==="
CONTEXT_WORLD_BUILDING_COMPLETE: "=== WORLD SIMULATION COMPLETE ==="
```

**Sci-fi:**
```
CONTEXT_WORLD_INTRO: "Welcome to {{school}}'s Advanced Systems Integration course!"
CONTEXT_WORLD_VISION: "Today you'll build a space station where crew, equipment, and AI systems interact. Your code will simulate real operational dynamics."
ENTITY_TYPE_1: "CREW MEMBER"
ENTITY_TYPE_1_DESCRIPTION: "Station Personnel"
CONTEXT_ENTITY_1_NARRATIVE: "Crew members are the human operators aboard your station. Each has a name, rank, and list of certifications."
ENTITY_1_CREATION_DESCRIPTION: "Create a dictionary representing a crew member with: name (str), rank (str), certifications (list)"
ENTITY_TYPE_2: "SHIP SYSTEM"
ENTITY_TYPE_2_DESCRIPTION: "Critical Infrastructure"
CONTEXT_ENTITY_2_NARRATIVE: "Ship systems keep the station operational. Each has a designation, system type (life-support/propulsion/sensors), and operational status."
ENTITY_2_CREATION_DESCRIPTION: "Create a dictionary representing a ship system with: designation (str), system_type (str), online (bool)"
INTERACTION_TITLE: "CREW-SYSTEM INTERACTION"
CONTEXT_INTERACTION_NARRATIVE: "When crew interacts with systems, success depends on certifications and system status. Certified crew can repair offline systems; uncertified crew cannot."
INTERACTION_DESCRIPTION: "Determine interaction outcome based on crew certifications and system type"
CONTEXT_WORLD_BUILDING_START: "=== BUILDING YOUR STATION ECOSYSTEM ==="
CONTEXT_WORLD_BUILDING_COMPLETE: "=== SIMULATION RUN COMPLETE ==="
```

---

### Template 10: The Quality Auditor

**Purpose:** Identify and fix style/quality issues in working code.

**Structure:**
```python
"""
{{CONTEXT_AUDIT_INTRO}}
{{CONTEXT_AUDIT_STANDARDS}}
"""

# ============================================================
# {{CODE_SAMPLE_TITLE}} - NEEDS IMPROVEMENT
# ============================================================
# {{CONTEXT_CODE_SAMPLE_NARRATIVE}}
#
# {{CONTEXT_ISSUES_FOUND}}
#
# Issues to fix:
# 1. {{ISSUE_1}}
# 2. {{ISSUE_2}}
# 3. {{ISSUE_3}}

def original_code():
    """{{ORIGINAL_CODE_DESCRIPTION}}"""
    # Working but poorly styled code
    pass

# ✏️ YOUR IMPROVED VERSION ✏️
# {{CONTEXT_IMPROVEMENT_GUIDANCE}}

def improved_code():
    """{{IMPROVED_CODE_DESCRIPTION}}"""
    pass
```

**Context Blocks Needed:**
- `{{CONTEXT_AUDIT_INTRO}}`: Why code quality matters
- `{{CONTEXT_AUDIT_STANDARDS}}`: What standards to apply
- `{{CONTEXT_CODE_SAMPLE_NARRATIVE}}`: Where this code came from
- `{{CONTEXT_ISSUES_FOUND}}`: Overview of problems
- `{{CONTEXT_IMPROVEMENT_GUIDANCE}}`: Tips for improvement

**Example Values by Genre:**

**Fantasy:**
```
CONTEXT_AUDIT_INTRO: "At {{school}}, even if a spell works, it may not be worthy of publication in the Grand Grimoire."
CONTEXT_AUDIT_STANDARDS: "All spells submitted to the library must follow the {{school}} Code Style Guide: clear naming, proper documentation, consistent formatting."
CODE_SAMPLE_TITLE: "Spell #347: Lightning Strike"
CONTEXT_CODE_SAMPLE_NARRATIVE: "A first-year student submitted this working spell, but {{mentor}} rejected it for poor style."
CONTEXT_ISSUES_FOUND: "The spell functions correctly but violates several style principles:"
ISSUE_1: "Variable name 'x' is not descriptive (should indicate it represents damage)"
ISSUE_2: "No docstring explaining what the spell does"
ISSUE_3: "Magic number '50' should be a named constant (BASE_LIGHTNING_DAMAGE)"
CONTEXT_IMPROVEMENT_GUIDANCE: "Rewrite the spell with clear variable names, a complete docstring, and named constants. The functionality should remain identical."
ORIGINAL_CODE_DESCRIPTION: "Working spell with style violations"
IMPROVED_CODE_DESCRIPTION: "Same spell, cleaned up to meet {{school}} standards"
```

**Business:**
```
CONTEXT_AUDIT_INTRO: "At {{school}} (tech startup), even if code passes tests, it may not pass code review."
CONTEXT_AUDIT_STANDARDS: "All code merged to main must follow the Engineering Team's Style Guide: clear naming, proper documentation, consistent formatting."
CODE_SAMPLE_TITLE: "Function #347: calculate_revenue"
CONTEXT_CODE_SAMPLE_NARRATIVE: "A junior engineer submitted this working function, but the tech lead rejected it for poor style."
CONTEXT_ISSUES_FOUND: "The function works correctly but violates several style principles:"
ISSUE_1: "Variable name 'x' is not descriptive (should indicate it represents monthly sales)"
ISSUE_2: "No docstring explaining what the function calculates"
ISSUE_3: "Magic number '0.15' should be a named constant (COMMISSION_RATE)"
CONTEXT_IMPROVEMENT_GUIDANCE: "Refactor the function with clear variable names, a complete docstring, and named constants. The functionality should remain identical."
ORIGINAL_CODE_DESCRIPTION: "Working function with style violations"
IMPROVED_CODE_DESCRIPTION: "Same function, refactored to meet team standards"
```

---

### Templates 11-15: Quick Reference

**Template 11: The Batch Processor**
- Pattern: Perform similar operation on multiple items
- Use case: Apply same function to list of entities
- Key blocks: `{{CONTEXT_BATCH_INTRO}}`, `{{CONTEXT_BATCH_ITEM_N}}`, `{{CONTEXT_BATCH_SUMMARY}}`

**Template 12: The Resource Exchange**
- Pattern: Trade/convert/exchange between entity types
- Use case: Currency exchange, item trading, resource conversion
- Key blocks: `{{CONTEXT_EXCHANGE_INTRO}}`, `{{CONTEXT_EXCHANGE_RATE}}`, `{{CONTEXT_EXCHANGE_RESULT}}`

**Template 13: The Decision Tree**
- Pattern: Branch through multiple conditional paths
- Use case: Dialog trees, RPG choice systems, classification
- Key blocks: `{{CONTEXT_DECISION_INTRO}}`, `{{CONTEXT_DECISION_POINT_N}}`, `{{CONTEXT_DECISION_OUTCOME}}`

**Template 14: The Collection Builder**
- Pattern: Accumulate items into growing collection
- Use case: Building inventory, gathering data, compiling results
- Key blocks: `{{CONTEXT_COLLECTION_INTRO}}`, `{{CONTEXT_COLLECTION_ADD}}`, `{{CONTEXT_COLLECTION_DISPLAY}}`

**Template 15: The Table Tracer**
- Pattern: Track variable state changes in structured format
- Use case: Code tracing exercises, debugging, state monitoring
- Key blocks: `{{CONTEXT_TRACE_INTRO}}`, `{{CONTEXT_TRACE_TABLE}}`, `{{CONTEXT_TRACE_VERIFICATION}}`

*(Full templates for 11-15 can be expanded if needed, but following same three-layer structure)*

---

## Context Block Library

### Complete List of Context Blocks

Here are all context blocks referenced in the templates above, organized by category:

#### Introduction & Framing
- `{{CONTEXT_INTRO}}` - Opening that places student in scenario
- `{{CONTEXT_PROJECT_INTRO}}` - Overall project framing
- `{{CONTEXT_ROLE_INTRO}}` - Who the student is
- `{{CONTEXT_WORLD_INTRO}}` - The world being created
- `{{CONTEXT_SPEC_INTRO}}` - Why specifications matter
- `{{CONTEXT_AUDIT_INTRO}}` - Why quality matters
- `{{CONTEXT_PREDICTION_INTRO}}` - Why prediction matters
- `{{CONTEXT_COMPARISON_INTRO}}` - Why comparison matters
- `{{CONTEXT_INVESTIGATION_INTRO}}` - Framing as investigation
- `{{CONTEXT_UNLOCKING_INTRO}}` - Why progressive unlocking

#### Learning Objectives
- `{{CONTEXT_LEARNING_OBJECTIVE}}` - What they'll learn
- `{{CONTEXT_PREDICTION_PURPOSE}}` - Skill being developed
- `{{CONTEXT_WORLD_VISION}}` - What complete system does

#### Narrative Context
- `{{CONTEXT_EXAMPLE_NARRATIVE}}` - Story explaining example
- `{{CONTEXT_PHASE_N}}` - What each phase accomplishes
- `{{CONTEXT_CASE_N_NARRATIVE}}` - Story behind each case
- `{{CONTEXT_APPROACH_N_NARRATIVE}}` - Story explaining approach
- `{{CONTEXT_SPEC_NARRATIVE}}` - Story context for component
- `{{CONTEXT_CHALLENGE_N_NARRATIVE}}` - Story for each challenge
- `{{CONTEXT_STAGE_N_NARRATIVE}}` - What each stage unlocks
- `{{CONTEXT_ENTITY_N_NARRATIVE}}` - Story behind entity type
- `{{CONTEXT_CODE_SAMPLE_NARRATIVE}}` - Where code came from
- `{{CONTEXT_INTERACTION_NARRATIVE}}` - How entities relate

#### Tasks & Instructions
- `{{CONTEXT_STUDENT_TASK}}` - Instructions for task
- `{{CONTEXT_ROLE_RESPONSIBILITIES}}` - Job description
- `{{CONTEXT_ROLE_CHALLENGE}}` - Problem to solve
- `{{CONTEXT_SITUATION_SETUP}}` - Current situation
- `{{CONTEXT_INVESTIGATION_MISSION}}` - What needs fixing
- `{{CONTEXT_COMPARISON_DECISION}}` - Decision to make
- `{{CONTEXT_SPEC_CONSTRAINTS}}` - Limitations
- `{{CONTEXT_UNLOCK_INSTRUCTION_N}}` - How to activate stage

#### Guidance & Support
- `{{CONTEXT_SUCCESS_CRITERIA}}` - How to know success
- `{{CONTEXT_IMPLEMENTATION_GUIDANCE}}` - Implementation tips
- `{{CONTEXT_PREDICTION_GUIDANCE_N}}` - Prediction hints
- `{{CONTEXT_ANALYSIS_PROMPT}}` - How to analyze
- `{{CONTEXT_DECISION_GUIDANCE}}` - Decision criteria
- `{{CONTEXT_INVESTIGATION_PROMPT_N}}` - Investigation questions
- `{{CONTEXT_IMPROVEMENT_GUIDANCE}}` - Improvement tips
- `{{CONTEXT_UNLOCK_REMINDER}}` - Progression reminder

#### Results & Completion
- `{{CONTEXT_INTEGRATION}}` - How pieces fit together
- `{{CONTEXT_FINAL_ASSEMBLY}}` - Complete system description
- `{{CONTEXT_ROLE_COMPLETE}}` - Closing message
- `{{CONTEXT_VERIFICATION_COMPLETE}}` - Verification done
- `{{CONTEXT_WORLD_BUILDING_COMPLETE}}` - World simulation done
- `{{CONTEXT_PROGRESSION_STATUS}}` - Current progress

#### Standards & Quality
- `{{CONTEXT_AUDIT_STANDARDS}}` - Quality standards
- `{{CONTEXT_ISSUES_FOUND}}` - Problem overview
- `{{CONTEXT_SPEC_SOURCE}}` - Who wrote spec

#### Analysis & Comparison
- `{{CONTEXT_INCREMENTAL_NARRATIVE}}` - Why building incrementally
- `{{CONTEXT_VERIFICATION_NARRATIVE}}` - How to verify
- `{{ANALYSIS_QUESTION_N}}` - Specific analysis questions

---

## Implementation Examples

### Example 1: Convert Existing Exercise Using Templates

**Before (module_7/code_tracing/exercise_1_trace_dict_updates.py):**
```python
"""
Code Tracing: Dictionary Updates
Track how dictionaries change line by line.
"""

def trace_example():
    spell = {"name": "Lumos", "power": 5}
    spell["learned"] = True
    spell["power"] = 10
    # etc.
```

**After (using Template 15: Table Tracer):**
```python
"""
{{CONTEXT_TRACE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

# ============================================================
# {{TRACE_SCENARIO_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_NARRATIVE}}
#
# ✏️ FILL IN THE TRACING TABLE ✏️
# {{CONTEXT_TRACE_TABLE}}
#
# | Line | Code | spell contents | Notes |
# |------|------|---------------|-------|
# | 1 | spell = {...} | {{TRACE_STEP_1}} | {{TRACE_NOTE_1}} |
# | 2 | spell["learned"] = True | {{TRACE_STEP_2}} | {{TRACE_NOTE_2}} |
# | 3 | spell["power"] = 10 | {{TRACE_STEP_3}} | {{TRACE_NOTE_3}} |

def trace_example():
    """{{TRACE_EXAMPLE_DESCRIPTION}}"""
    spell = {"name": "{{spell1}}", "power": 5}
    spell["learned"] = True
    spell["power"] = 10
    # etc.

# ============================================================
# VERIFICATION
# ============================================================
# {{CONTEXT_TRACE_VERIFICATION}}

def verify_trace():
    """{{CONTEXT_VERIFICATION_NARRATIVE}}"""
    print("{{CONTEXT_VERIFICATION_START}}")
    trace_example()
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")
```

**With fantasy theme (dumblecode):**
```
CONTEXT_TRACE_INTRO: "At {{school}}, advanced students learn to predict how spells evolve without casting them."
CONTEXT_LEARNING_OBJECTIVE: "You'll master tracking dictionary mutations line-by-line."
TRACE_SCENARIO_TITLE: "Scenario: Spell Power Upgrade"
CONTEXT_TRACE_NARRATIVE: "{{friend_1}} is upgrading the {{spell1}} spell. Track how the spell dictionary changes with each modification."
CONTEXT_TRACE_TABLE: "Fill in what the 'spell' dictionary contains after each line executes:"
TRACE_STEP_1: "{'name': 'Lumos', 'power': 5}"
TRACE_NOTE_1: "Initial spell creation"
TRACE_STEP_2: "{'name': 'Lumos', 'power': 5, 'learned': True}"
TRACE_NOTE_2: "Added learned status"
TRACE_STEP_3: "{'name': 'Lumos', 'power': 10, 'learned': True}"
TRACE_NOTE_3: "Upgraded power level"
```

**With sci-fi theme (starfleet):**
```
CONTEXT_TRACE_INTRO: "Aboard {{school}}, senior engineers learn to predict system state changes without running diagnostics."
CONTEXT_LEARNING_OBJECTIVE: "You'll master tracking data structure mutations line-by-line."
TRACE_SCENARIO_TITLE: "Scenario: Shield Power Upgrade"
CONTEXT_TRACE_NARRATIVE: "{{friend_1}} is upgrading the {{item_1}} shield system. Track how the system configuration changes with each command."
CONTEXT_TRACE_TABLE: "Fill in what the 'system' configuration contains after each line executes:"
TRACE_STEP_1: "{'designation': 'Forward Shields', 'power': 5}"
TRACE_NOTE_1: "Initial system configuration"
TRACE_STEP_2: "{'designation': 'Forward Shields', 'power': 5, 'online': True}"
TRACE_NOTE_2: "System brought online"
TRACE_STEP_3: "{'designation': 'Forward Shields', 'power': 10, 'online': True}"
TRACE_NOTE_3: "Power allocation increased"
```

**Note:** The exercise code is IDENTICAL. Only the context blocks change by theme!

---

### Example 2: Create New Exercise Using Templates

**Goal:** Create a new "bug hunt" exercise for Module 7 (Dictionaries) that works across all genres.

**Choose Template:** Template 4 (Forensic Debugger)

**Step 1: Define the Python concept**
- Teaching: Common dictionary errors (KeyError, TypeError, etc.)
- Exercise type: bug_hunt

**Step 2: Use template structure**
```python
"""
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_MISSION}}
"""

# ============================================================
# {{CASE_1_TITLE}}
# ============================================================
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# ERROR MESSAGE:
# KeyError: 'level'
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

def case_1_buggy():
    """Attempting to access non-existent key."""
    player = {"name": "{{hero}}", "health": 100}
    print(f"Player level: {player['level']}")  # 🐛 BUG!

# ✏️ FIX THE CODE ✏️
def case_1_fixed():
    """Fixed version using .get() or checking key existence."""
    pass
```

**Step 3: Define context blocks for all genres**

**Fantasy theme:**
```json
{
  "CONTEXT_INVESTIGATION_INTRO": "Alert! Several spells at {{school}} have been corrupted!",
  "CONTEXT_INVESTIGATION_MISSION": "As a member of the Spell Debugging Team, you must identify and fix each magical malfunction.",
  "CASE_1_TITLE": "Bug #1: The Missing Power Level",
  "CONTEXT_CASE_1_NARRATIVE": "{{friend_1}} tried to check their magical level, but the spell crashed with a mysterious error.",
  "CONTEXT_INVESTIGATION_PROMPT_1": "Examine the player dictionary. What key is the code trying to access? Does that key exist? How can you safely check?"
}
```

**Sci-fi theme:**
```json
{
  "CONTEXT_INVESTIGATION_INTRO": "Alert! Several systems aboard {{school}} have encountered runtime errors!",
  "CONTEXT_INVESTIGATION_MISSION": "As a Systems Diagnostics Engineer, you must identify and fix each software malfunction.",
  "CASE_1_TITLE": "Error #1: The Missing Rank Field",
  "CONTEXT_CASE_1_NARRATIVE": "{{friend_1}} tried to query their officer rank, but the system crashed with a data access error.",
  "CONTEXT_INVESTIGATION_PROMPT_1": "Examine the crew_member record. What field is the code trying to access? Does that field exist? How can you safely query?"
}
```

**Sports theme:**
```json
{
  "CONTEXT_INVESTIGATION_INTRO": "Alert! Several plays in the {{school}} playbook have coding errors!",
  "CONTEXT_INVESTIGATION_MISSION": "As the team's Analytics Engineer, you must debug each play simulation.",
  "CASE_1_TITLE": "Bug #1: The Missing Skill Rating",
  "CONTEXT_CASE_1_NARRATIVE": "{{friend_1}} tried to check their skill level, but the simulation crashed with a data error.",
  "CONTEXT_INVESTIGATION_PROMPT_1": "Examine the player stats. What field is the code trying to access? Does that field exist? How can you safely check?"
}
```

**Result:** ONE exercise file, works perfectly in fantasy/sci-fi/sports/music/business by just swapping context blocks!

---

## Migration Guide

### How to Convert Existing Exercises to Template System

**Step 1: Identify Current Narrative Pattern**

Read the exercise and determine which template(s) it matches:
- Does it show an example first? → Template 1 (Tutorial Guide)
- Does it build something incrementally? → Template 2 (Incremental Builder)
- Does it assign a role? → Template 3 (Role Assignment)
- Does it involve debugging? → Template 4 (Forensic Debugger)
- Does it compare approaches? → Template 5 (Comparison Analyst)
- Does it implement from spec? → Template 6 (Specification Implementer)
- Does it predict output? → Template 7 (Prediction Challenger)
- Does it unlock progressively? → Template 8 (Progressive Unlocking)
- Does it build interconnected systems? → Template 9 (World Builder)
- Does it fix style issues? → Template 10 (Quality Auditor)

**Step 2: Extract Existing Narrative Elements**

Identify what narrative content exists:
- Opening statements → becomes `{{CONTEXT_INTRO}}`
- Task descriptions → becomes `{{CONTEXT_STUDENT_TASK}}`
- Hints and guidance → becomes `{{CONTEXT_GUIDANCE}}`
- Completion messages → becomes `{{CONTEXT_COMPLETE}}`

**Step 3: Rewrite Using Template Structure**

Replace hardcoded narrative with context block placeholders.

**Step 4: Define Context Blocks for Each Theme**

Add entries to `theme_variables.json`:

```json
{
  "dumblecode": {
    "hero": "Harry",
    "CONTEXT_INTRO": "Fantasy version...",
    "CONTEXT_STUDENT_TASK": "Fantasy version...",
    // etc.
  },
  "starfleet": {
    "hero": "Ensign Chen",
    "CONTEXT_INTRO": "Sci-fi version...",
    "CONTEXT_STUDENT_TASK": "Sci-fi version...",
    // etc.
  }
}
```

**Step 5: Test Across Multiple Genres**

```bash
python scripts/convert_exercises.py --theme dumblecode
python scripts/convert_exercises.py --theme starfleet
python scripts/convert_exercises.py --theme sports-academy
```

Verify that:
- Each version tells a coherent story
- Technical content remains identical
- Instructions are clear in all versions
- No hardcoded references remain

---

### Priority Migration Order

**Phase 1: High-Impact Exercises** (Modules 7-9)
- Already have good placeholder coverage
- Most coherent narratives
- Will demonstrate template system value quickly

**Phase 2: Mid-Level Exercises** (Modules 3-6)
- Currently inconsistent narrative quality
- Would benefit most from template standardization

**Phase 3: Foundation Exercises** (Modules 0-2)
- Simplest exercises
- Can use simpler templates (Tutorial Guide, Incremental Builder)

**Phase 4: Create New Sci-Fi Theme**
- Test system with non-fantasy genre
- Validate that templates truly are universal

---

## Next Steps

1. **Extend theme_variables.json**
   - Add context block entries for dumblecode (existing theme)
   - Create complete starfleet theme (new sci-fi theme)

2. **Convert 3 Pilot Exercises**
   - Module 7, Exercise 1 (Incremental Builder)
   - Module 9, Exercise 8 (World Builder)
   - Module 7, Decode Error Exercise 1 (Forensic Debugger)

3. **Test Pilot Conversions**
   - Generate fantasy version
   - Generate sci-fi version
   - Compare narrative coherence

4. **Document Template Selection Guide**
   - When to use each template
   - How to combine templates
   - Common patterns for each module

5. **Create Remaining Templates**
   - Expand Templates 11-15 with full specifications
   - Add edge case templates as needed

---

## Benefits of Template System

✅ **True Genre Independence**: Works for fantasy, sci-fi, sports, music, business, history, etc.

✅ **Narrative Consistency**: Every exercise tells a proper story in every theme

✅ **Easy Theme Creation**: Just write context blocks for new theme, no code changes

✅ **Pedagogical Clarity**: Templates enforce good instructional design patterns

✅ **Maintainability**: Update template once, affects all exercises using it

✅ **Scalability**: Easy to add new exercises following established patterns

✅ **Quality Assurance**: Templates prevent "Sorting Hat problem" (theme-specific exercises)

---

**Document Status:** ✅ COMPLETE
**Next Action:** Begin extending theme_variables.json with context blocks
