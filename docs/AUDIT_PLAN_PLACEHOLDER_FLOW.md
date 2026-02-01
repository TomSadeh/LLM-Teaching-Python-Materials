# Audit Plan: Placeholder Flow and Logical Progression

Improving narrative coherence and learning progression through better placeholder usage.

---

## Overview

**Goal:** Transform exercises from isolated programming tasks into engaging, themed narratives with logical progression.

**Why This Matters:**
- **Engagement:** Students stay motivated when exercises tell a story
- **Memory:** Context aids retention (the "Baker-baker paradox")
- **Transfer:** Narrative scenarios help students see real-world applications

**Scope:** All 145 exercises across 10 modules

---

## What is "Flow"?

Flow is the narrative and logical connection between exercises that creates:

1. **Story Coherence** - Placeholders create a mini-narrative
2. **Concept Progression** - Each exercise builds on previous ones
3. **Theme Consistency** - Fantasy elements support, not distract from, learning

### Example: Poor Flow vs. Good Flow

#### ❌ Poor Flow (module_0_basics)

```python
# Exercise 1
print("{{hero}}")

# Exercise 2
age = 25
print(age)

# Exercise 3
print("{{villain}}")

# Exercise 4
x = 10
y = 20
print(x + y)
```

**Problems:**
- No narrative connection
- Placeholders appear randomly
- No clear progression
- Breaks immersion with generic examples

#### ✅ Good Flow (module_0_basics)

```python
# Exercise 1: Arrival
print("{{hero}} arrives at {{school}}")

# Exercise 2: Age requirement
hero_age = 11
print(f"{{hero}} is {hero_age} years old")

# Exercise 3: House assignment
print("{{hero}} is sorted into {{house}}")

# Exercise 4: First class
wand_length = 11
spell_power = 9
total_power = wand_length + spell_power
print(f"{{hero}}'s magical power: {total_power}")
```

**Strengths:**
- Clear narrative: arrival → sorting → learning
- Placeholders create story
- Numbers have context (age, power)
- Each exercise builds conceptually

---

## Audit Framework

### Dimension 1: Narrative Coherence (Story)

**Question:** Do the placeholders tell a story?

**Rating Scale:**
- **0 - No Narrative:** Random placeholders or none
- **1 - Weak Narrative:** Some connection but disjointed
- **2 - Clear Narrative:** Exercises flow as a story
- **3 - Excellent Narrative:** Engaging mini-adventure

**Evaluation Criteria:**
- [ ] Placeholders introduce characters/setting
- [ ] Story progresses logically
- [ ] Has beginning, middle, end
- [ ] Placeholders support the narrative

### Dimension 2: Concept Progression (Learning)

**Question:** Do exercises build on each other programmatically?

**Rating Scale:**
- **0 - Disconnected:** No conceptual relationship
- **1 - Loose Connection:** Same topic, different examples
- **2 - Clear Progression:** Each adds one new element
- **3 - Scaffolded:** Perfect learning staircase

**Evaluation Criteria:**
- [ ] Intro → Practice → Challenge structure
- [ ] New concepts introduced one at a time
- [ ] Previous concepts reinforced
- [ ] Difficulty increases gradually

### Dimension 3: Theme Integration (Immersion)

**Question:** Do placeholders enhance or distract from learning?

**Rating Scale:**
- **0 - Breaks Immersion:** Placeholders feel forced
- **1 - Neutral:** Placeholders present but not meaningful
- **2 - Supports Theme:** Placeholders feel natural
- **3 - Enhances Learning:** Theme aids understanding

**Evaluation Criteria:**
- [ ] Placeholders fit the exercise context
- [ ] Fantasy elements don't obscure concepts
- [ ] Theme makes examples more memorable
- [ ] Consistent within exercise set

---

## Module-Specific Flow Patterns

Each module should have a signature narrative pattern that fits its learning objectives.

### module_0_basics: First Day Journey

**Narrative Arc:** Arrival → Orientation → First Lessons → Achievement

**Placeholder Pattern:**
```
Intro: {{hero}}, {{school}}
Rising: {{house}}, {{mentor}}, {{friend}}
Practice: {{item}}, {{spell1}}
Closure: {{greeting}}, {{exclamation}}
```

**Example Flow:**
1. Hello World → `{{hero}}` arrives at `{{school}}`
2. Variables → Name tags for `{{hero}}` and `{{friend}}`
3. Math → Calculate `{{item}}` cost at `{{place}}`
4. Input → Ask for `{{password}}` to enter `{{house}}`
5. Project → Create greeting card with `{{greeting}}`

**Success Criteria:**
- [ ] Student feels like they're following a character
- [ ] Each exercise is a "scene" in the story
- [ ] Programming concepts tied to story events

---

### module_1_turtle_loops: Art and Magic

**Narrative Arc:** Learning spells → Practice → Create masterpiece

**Placeholder Pattern:**
```
Intro: {{spell1}} (simple)
Build: {{spell2}}, {{spell3}}
Combine: {{creature}}, {{location}}
Master: {{house}} colors, {{school}} emblem
```

**Example Flow:**
1. Intro → Draw with `{{spell1}}` (single shape)
2. Patterns → Use `{{spell2}}` (repeated patterns)
3. Colors → `{{house}}` colored designs
4. Challenge → Draw `{{creature}}` or `{{school}}` scene
5. Project → Create `{{location}}` landscape

**Success Criteria:**
- [ ] Each "spell" = a programming technique
- [ ] Visual progression visible
- [ ] Theme makes drawing meaningful (not random)

---

### module_2_decisions: Choices and Consequences

**Narrative Arc:** Facing challenges → Making choices → Outcomes

**Placeholder Pattern:**
```
Setup: {{villain}} threat or {{location}} challenge
Choice: Use {{spell1}} or {{spell2}}?
Outcome: Success with {{exclamation}} or retry
Alliance: {{friend}}, {{heroine}}, {{group}}
```

**Example Flow:**
1. Password Check → Guess `{{password}}` to enter `{{house}}`
2. Ability Test → If power > X, learn `{{spell1}}`
3. Character Quiz → Multiple questions determine trait
4. Battle Choice → Choose `{{spell1}}`, `{{spell2}}`, or `{{spell3}}`
5. Adventure → Navigate `{{location}}` with branching paths

**Success Criteria:**
- [ ] Conditions feel like meaningful choices
- [ ] Outcomes have narrative weight
- [ ] Booleans = yes/no story decisions

---

### module_3_lists: Teams and Collections

**Narrative Arc:** Forming groups → Training together → Mission

**Placeholder Pattern:**
```
Solo: {{hero}}
Pair: {{hero}}, {{friend}}
Team: {{hero}}, {{friend}}, {{heroine}}
Organization: {{group}}
Inventory: {{item}}, {{spell1}}, {{spell2}}
```

**Example Flow:**
1. Roster → List of `{{group}}` members
2. Inventory → `{{hero}}`'s collection of `{{item}}`s
3. Spellbook → Add/remove `{{spell1}}`, `{{spell2}}`
4. Quest Party → Manage team for `{{location}}` adventure
5. Score Tracker → Track `{{group}}` achievements

**Success Criteria:**
- [ ] Lists = collections of related items
- [ ] Operations have story meaning (add = recruit)
- [ ] Iteration = checking each team member

---

### module_4_games: Adventures and Challenges

**Narrative Arc:** Quest begins → Obstacles → Victory/Defeat

**Placeholder Pattern:**
```
Hero: {{hero}}
Antagonist: {{villain}}
Challenge: {{location}}, {{creature}}
Tools: {{spell1}}, {{spell2}}, {{item}}
Outcome: {{exclamation}}
```

**Example Flow:**
1. Number Guess → `{{mentor}}` tests `{{hero}}`
2. Battle → `{{hero}}` vs `{{villain}}` with `{{spell1}}`
3. Dice → Roll for `{{creature}}` encounter at `{{location}}`
4. Streak → Count wins in `{{group}}` tournament
5. Adventure → Complex quest with multiple mechanics

**Success Criteria:**
- [ ] While loop = ongoing challenge
- [ ] Conditions = win/lose states
- [ ] Random = unpredictable outcomes
- [ ] Variables = game state (score, lives)

---

### module_5_functions: Mastering Spells

**Narrative Arc:** Learn basics → Create variations → Combine powers

**Placeholder Pattern:**
```
Simple: {{spell1}} (one effect)
Parameters: {{spell2}} (customizable)
Returns: {{spell3}} (produces result)
Composition: Combine multiple spells
```

**Example Flow:**
1. First Spell → `cast_spell1()` prints effect
2. Customizable → `cast_spell(name, power)` with parameters
3. Calculation → `calculate_power(spell, wand)` returns number
4. Validation → `is_valid_house(name)` checks `{{house}}`
5. Complex → Combine functions for `{{creature}}` encounter

**Success Criteria:**
- [ ] Functions = spells (reusable magic)
- [ ] Parameters = customization
- [ ] Returns = producing something
- [ ] Abstraction makes sense

---

### module_6_final_project: Epic Quests

**Narrative Arc:** Full adventure from start to finish

**Placeholder Pattern:**
```
Use ALL placeholders naturally:
{{hero}} leads {{group}} to {{location}}
Faces {{villain}} using {{spell1}}, {{spell2}}, {{spell3}}
With {{friend}}, {{heroine}}, guidance from {{mentor}}
```

**Example Flow:**
1. Calculator → `{{place}}` shop calculator
2. Card Generator → Create `{{greeting}}` cards for `{{house}}`
3. Scene → Full `{{location}}` adventure
4. (Open-ended templates)

**Success Criteria:**
- [ ] Integrates concepts from all modules
- [ ] Rich narrative with many placeholders
- [ ] Feels like a "final exam" adventure

---

### module_7_dictionaries: Profiles and Data

**Narrative Arc:** Recording information → Looking up data → Analysis

**Placeholder Pattern:**
```
Single: {{hero}} profile
Multiple: {{hero}}, {{friend}}, {{heroine}} data
Nested: {{school}} with {{house}} members
Lookup: {{spell1}} effects, {{item}} properties
```

**Example Flow:**
1. Character Card → `{{hero}}` name, age, `{{house}}`
2. Spellbook → Map `{{spell1}}` to effect
3. Roster → `{{group}}` members with roles
4. Inventory → Track `{{item}}` quantities
5. Database → Complex `{{school}}` records

**Success Criteria:**
- [ ] Dicts = profiles/records
- [ ] Keys = attributes (name, house)
- [ ] Values = data
- [ ] Nested = hierarchical (school → house → student)

---

### module_8_modules: Expanding Powers

**Narrative Arc:** Learn library → Import tools → Create own

**Placeholder Pattern:**
```
Built-in: random ({{spell1}} unpredictability)
Time: Track quest duration
Math: Calculate {{spell1}} power precisely
Custom: Create {{school}} module
```

**Example Flow:**
1. Random → `{{spell1}}` has random effects
2. Time → Track how long `{{hero}}` takes
3. Math → Precise `{{creature}}` calculations
4. JSON → Save `{{hero}}` profile
5. Custom → Create `{{school}}.py` module

**Success Criteria:**
- [ ] Modules = tool libraries
- [ ] Import = gaining new abilities
- [ ] Creating module = teaching others

---

### module_9_oop: Creating Characters

**Narrative Arc:** Define type → Create instances → Interactions

**Placeholder Pattern:**
```
Class: Character, Spell, Creature
Instances: {{hero}}, {{villain}}, {{friend}}
Attributes: name={{hero}}, house={{house}}
Methods: cast_spell(), learn(), battle()
```

**Example Flow:**
1. First Class → Character with name
2. Init → Character({{hero}}, {{house}})
3. Methods → .cast_spell(), .learn_spell()
4. Repr → Display `{{hero}}` info
5. Interaction → `{{hero}}` battles `{{villain}}`
6. Inheritance → Student inherits from Character
7. Composition → Character has Spellbook

**Success Criteria:**
- [ ] Classes = types of things
- [ ] Objects = specific characters
- [ ] Methods = what they can do
- [ ] Inheritance/composition clear

---

## Audit Process

### Step 1: Module Overview (15 min per module)

For each module:

1. **List all exercises** in order
2. **Extract current placeholders** used
3. **Identify current flow** (if any)
4. **Rate** on 3 dimensions (0-3 scale each)

**Output:** Scoring matrix

| Module | Exercises | Narrative | Progression | Integration | Total |
|--------|-----------|-----------|-------------|-------------|-------|
| module_0 | 23 | 1 | 2 | 1 | 4/9 |
| module_1 | 11 | 2 | 2 | 2 | 6/9 |
| ... | ... | ... | ... | ... | ... |

---

### Step 2: Deep Dive (1-2 hours per module)

For modules scoring <6/9:

1. **Map current flow**
   - Create visual diagram of exercise connections
   - Note where flow breaks

2. **Identify issues**
   - Where does narrative disconnect?
   - Where do concepts jump?
   - Where do placeholders feel forced?

3. **Design improved flow**
   - Sketch ideal narrative arc
   - Map concepts to story beats
   - Select appropriate placeholders

4. **Document changes**
   - List specific edits per exercise
   - Note which exercises might need reordering
   - Identify exercises that need heavy revision

---

### Step 3: Cross-Module Coherence (2 hours)

Check that modules connect:

1. **Does module_1 build on module_0?**
   - Same characters continue?
   - Story advances?

2. **Progressive mastery**
   - Early modules: Simple scenarios
   - Middle modules: Challenges
   - Late modules: Complex adventures

3. **Callback opportunities**
   - Can later modules reference earlier achievements?
   - E.g., module_9 creates a `{{hero}}` class from module_0

---

## Documentation Template

For each module needing improvement:

```markdown
# Flow Improvement: module_X_topic

## Current State

**Narrative Rating:** X/3
**Progression Rating:** X/3
**Integration Rating:** X/3

**Current Flow:** [Brief description]

**Issues:**
1. [Specific problem 1]
2. [Specific problem 2]
...

## Proposed Flow

**Narrative Arc:** [Beginning → Middle → End]

**Placeholder Pattern:**
```
[List key placeholders and when they appear]
```

**Concept Progression:**
1. [Exercise 1: Concept A]
2. [Exercise 2: Concept A + B]
3. [Exercise 3: Concept A + B + C]
...

## Changes Required

### Exercise 1: exercise_name.py
**Current:** [What it does now]
**Change:** [What to modify]
**Placeholders:** [Add/change which ones]

### Exercise 2: exercise_name.py
...

## Expected Improvement

**New Ratings:** Narrative X/3, Progression X/3, Integration X/3
**Benefits:**
- [Benefit 1]
- [Benefit 2]
```

---

## Success Criteria

### Quantitative Goals
- [ ] All modules score ≥6/9 total
- [ ] No module scores 0 on any dimension
- [ ] 80% of exercises have clear narrative connection

### Qualitative Goals
- [ ] Reading exercises in order tells a story
- [ ] Placeholders feel natural, not forced
- [ ] Story supports learning, not distracts
- [ ] Students can anticipate what comes next

---

## Priority Matrix

| Module | Current Score | Issues | Priority | Effort |
|--------|--------------|--------|----------|--------|
| module_0_basics | 4/9 | Random placeholders | HIGH | Medium |
| module_1_turtle_loops | 6/9 | Okay but could improve | MEDIUM | Low |
| module_2_decisions | 5/9 | Disconnected exercises | HIGH | Medium |
| module_3_lists | 4/9 | No clear narrative | HIGH | Medium |
| module_4_games | 7/9 | Already good | LOW | Low |
| module_5_functions | 5/9 | Placeholder inconsistency | MEDIUM | Medium |
| module_6_final_project | 3/9 | Generic templates | HIGH | High |
| module_7_dictionaries | 4/9 | No story arc | HIGH | Medium |
| module_8_modules | 5/9 | Abstract examples | MEDIUM | Medium |
| module_9_oop | 6/9 | Good foundation | MEDIUM | Low |

**Priority HIGH:** modules 0, 2, 3, 6, 7 (focus first)
**Priority MEDIUM:** modules 1, 5, 8, 9 (next)
**Priority LOW:** module 4 (polish only)

---

## Timeline

### Week 1: Assessment
- Day 1-2: Score all modules
- Day 3-4: Deep dive on HIGH priority modules
- Day 5: Documentation and prioritization

### Week 2-3: Design
- Design improved flows for each HIGH priority module
- Document specific changes needed
- Create mockups/examples

### Week 4+: Implementation
- Revise exercises according to design
- Test flow by reading through sequentially
- Update documentation

---

## Validation

### Self-Check
After implementing improvements, verify:
- [ ] Read all exercises in order - does it flow?
- [ ] Check placeholders - do they tell a story?
- [ ] Review concepts - do they build logically?
- [ ] Test with theme toggle - works in all themes?

### User Testing (if possible)
- [ ] Have student work through module
- [ ] Note where they get confused
- [ ] Ask if story made sense
- [ ] Measure engagement (completed exercises)

---

## Output Documents

Create in `docs/audits/flow/`:

1. `FLOW_SCORES.md` - Ratings for all modules
2. `FLOW_MODULE_0_IMPROVEMENTS.md` - Detailed changes
3. `FLOW_MODULE_2_IMPROVEMENTS.md` - Detailed changes
4. `FLOW_MODULE_3_IMPROVEMENTS.md` - Detailed changes
5. `FLOW_MODULE_6_IMPROVEMENTS.md` - Detailed changes
6. `FLOW_MODULE_7_IMPROVEMENTS.md` - Detailed changes
7. `FLOW_CROSS_MODULE.md` - Inter-module connections
