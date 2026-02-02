# Narrative Archetype Visual Guide

Quick visual reference for selecting and implementing narrative archetypes in exercises.

---

## The 10 Archetypes at a Glance

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         NARRATIVE ARCHETYPES                             │
│                     (Universal Reusable Patterns)                        │
└─────────────────────────────────────────────────────────────────────────┘

1. RANDOM ASSIGNMENT                    Icon: 🎩
   ┌─────────────────────────────────────────────┐
   │ Input → Random Selection → Assignment       │
   │ "Who/what are you?" → Categorize            │
   │ Example: Sorting Hat, House Assignment      │
   │ Teaches: random.choice(), lists             │
   └─────────────────────────────────────────────┘

2. INVENTORY MANAGEMENT                 Icon: 🎒
   ┌─────────────────────────────────────────────┐
   │ Collection → Add/Remove/Use → Update        │
   │ "Manage your items"                         │
   │ Example: RPG Inventory, Backpack            │
   │ Teaches: Dictionaries, CRUD operations      │
   └─────────────────────────────────────────────┘

3. CHARACTER CREATION                   Icon: 👤
   ┌─────────────────────────────────────────────┐
   │ Attributes → Define → Display Profile       │
   │ "Create your character"                     │
   │ Example: Hero Profile, Character Sheet      │
   │ Teaches: Dicts/classes, data types          │
   └─────────────────────────────────────────────┘

4. CHALLENGE/ATTEMPT                    Icon: ⚔️
   ┌─────────────────────────────────────────────┐
   │ Task → Attempt → Success/Failure            │
   │ "Can you overcome this?"                    │
   │ Example: Face creature, Pass test           │
   │ Teaches: Conditionals, comparisons          │
   └─────────────────────────────────────────────┘

5. KNOWLEDGE CHECK                      Icon: 📝
   ┌─────────────────────────────────────────────┐
   │ Questions → Answer → Score                  │
   │ "Test your knowledge"                       │
   │ Example: Trivia Quiz, Flashcards            │
   │ Teaches: Functions, string comparison       │
   └─────────────────────────────────────────────┘

6. PROGRESSION TRACKING                 Icon: ⭐
   ┌─────────────────────────────────────────────┐
   │ Points → Threshold → Level Up               │
   │ "Grow stronger"                             │
   │ Example: Experience System, Achievements    │
   │ Teaches: Variables, thresholds, math        │
   └─────────────────────────────────────────────┘

7. RELATIONSHIP MAPPING                 Icon: 🔗
   ┌─────────────────────────────────────────────┐
   │ Entities → Connections → Query              │
   │ "Who knows who?"                            │
   │ Example: Friend Network, Alliances          │
   │ Teaches: Nested dicts, graph concepts       │
   └─────────────────────────────────────────────┘

8. DECISION TREE                        Icon: 🌳
   ┌─────────────────────────────────────────────┐
   │ Choice → Branch → Choice → Outcome          │
   │ "Choose your path"                          │
   │ Example: Text Adventure, Story Branches     │
   │ Teaches: Nested conditionals, state         │
   └─────────────────────────────────────────────┘

9. COLLECTION BUILDING                  Icon: 📚
   ┌─────────────────────────────────────────────┐
   │ Empty → Add Items → Display Collection      │
   │ "Build your list"                           │
   │ Example: Favorites, Playlist, Wishlist      │
   │ Teaches: Lists, .append(), iteration        │
   └─────────────────────────────────────────────┘

10. RESOURCE EXCHANGE                   Icon: 💰
    ┌─────────────────────────────────────────────┐
    │ Resources → Trade → Update Both Sides       │
    │ "Buy and sell"                              │
    │ Example: Shop, Trading, Budget              │
    │ Teaches: Multiple variables, validation     │
    └─────────────────────────────────────────────┘
```

---

## Archetype Selection Flowchart

```
START: What programming concept are you teaching?
  │
  ├─ Lists
  │   ├─ random.choice() → [1] RANDOM ASSIGNMENT
  │   ├─ .append() → [9] COLLECTION BUILDING
  │   └─ Iteration → [5] KNOWLEDGE CHECK (random questions)
  │
  ├─ Dictionaries
  │   ├─ Key-value basics → [3] CHARACTER CREATION
  │   ├─ CRUD operations → [2] INVENTORY MANAGEMENT
  │   ├─ Nested dicts → [7] RELATIONSHIP MAPPING
  │   └─ Multiple dicts → [10] RESOURCE EXCHANGE
  │
  ├─ Conditionals
  │   ├─ if/else → [4] CHALLENGE/ATTEMPT
  │   ├─ Nested if → [8] DECISION TREE
  │   └─ Thresholds → [6] PROGRESSION TRACKING
  │
  ├─ Functions
  │   ├─ Return values → [5] KNOWLEDGE CHECK
  │   ├─ Parameters → [2] INVENTORY MANAGEMENT (functions)
  │   └─ Multiple functions → [4] CHALLENGE/ATTEMPT (helpers)
  │
  ├─ Classes (OOP)
  │   ├─ Basic class → [3] CHARACTER CREATION
  │   ├─ Methods → [4] CHALLENGE/ATTEMPT (interactions)
  │   ├─ Inheritance → [3] CHARACTER CREATION (subclasses)
  │   └─ Composition → [7] RELATIONSHIP MAPPING (has-a)
  │
  └─ Loops
      ├─ while True → [8] DECISION TREE (game loop)
      ├─ Counter → [6] PROGRESSION TRACKING
      └─ Accumulator → [9] COLLECTION BUILDING
```

---

## Archetype Combination Matrix

Common and effective combinations:

```
┌────────────────┬────────────────┬──────────────────────────────────┐
│  Archetype 1   │  Archetype 2   │         Result Pattern           │
├────────────────┼────────────────┼──────────────────────────────────┤
│ Character (3)  │ Challenge (4)  │ Hero faces obstacle with stats   │
│ Inventory (2)  │ Exchange (10)  │ RPG Inventory with shop system   │
│ Decision (8)   │ Challenge (4)  │ Adventure with skill checks      │
│ Collection (9) │ Random (1)     │ Build list, pick random item     │
│ Character (3)  │ Progression (6)│ Character with leveling system   │
│ Relationship(7)│ Character (3)  │ Social network of characters     │
│ Decision (8)   │ Inventory (2)  │ Adventure with item collection   │
│ Knowledge (5)  │ Progression (6)│ Quiz that unlocks levels         │
│ Challenge (4)  │ Progression (6)│ Combat that gives experience     │
│ Inventory (2)  │ Challenge (4)  │ Use items to overcome obstacles  │
└────────────────┴────────────────┴──────────────────────────────────┘
```

---

## Placeholder Mapping by Archetype

What placeholders each archetype typically needs:

```
ARCHETYPE                REQUIRED          OPTIONAL           AVOID
─────────────────────────────────────────────────────────────────────
1. Random Assignment     {{house}} (x4)    {{hero}}           {{spell1}}
                         OR categories      {{school}}

2. Inventory Management  {{item}}          {{spell1}}         {{villain}}
                         {{pet}}           {{hero}}
                         generic items

3. Character Creation    {{hero}}          {{item}}           {{spell4}}
                         {{heroine}}       {{pet}}
                         {{house}}
                         {{school}}

4. Challenge/Attempt     {{hero}}          {{item}}           {{password}}
                         {{creature}}      {{spell1}}
                         {{villain}}

5. Knowledge Check       ANY (for Q's)     {{exclamation}}    None
                         {{hero}}
                         {{house}}

6. Progression Tracking  {{hero}}          {{spell1}}         {{location}}
                         {{heroine}}       (for effects)

7. Relationship Mapping  {{hero}}          {{group}}          {{item}}
                         {{heroine}}       {{house}}
                         {{friend}}
                         {{mentor}}

8. Decision Tree         {{location}}      {{hero}}           Generic
                         {{place}}         {{item}}
                         {{school}}        {{spell1}}

9. Collection Building   ANY (examples)    {{exclamation}}    Complex
                         {{hero}}                             ones
                         {{spell1}}

10. Resource Exchange    {{item}}          {{mentor}}         {{password}}
                         {{pet}}           (as merchant)
                         "gold"
```

---

## Difficulty Progression

How to scale archetype complexity:

```
BEGINNER (Modules 0-2)
══════════════════════════════════════════════════════════════════
[3] Character Creation
    Level 1: Hardcoded character dict, print values
    Level 2: Input for some values
    Level 3: Validate input, format display

[9] Collection Building
    Level 1: Pre-filled list, print it
    Level 2: Add items from input
    Level 3: Add + display with enumeration

[5] Knowledge Check
    Level 1: Single question, check answer
    Level 2: Multiple questions, track score
    Level 3: Score + feedback messages


INTERMEDIATE (Modules 3-5)
══════════════════════════════════════════════════════════════════
[2] Inventory Management
    Level 1: Display inventory
    Level 2: Add/remove items
    Level 3: Add/remove/use with effects
    Level 4: Full CRUD + shop system

[4] Challenge/Attempt
    Level 1: Simple pass/fail check
    Level 2: Pass/partial/fail (elif)
    Level 3: Random chance + skill
    Level 4: Multiple rounds, track wins

[8] Decision Tree
    Level 1: 1 choice, 2 outcomes
    Level 2: 2 levels deep
    Level 3: 3+ levels, multiple branches
    Level 4: With state tracking (inventory, health)


ADVANCED (Modules 6-9)
══════════════════════════════════════════════════════════════════
[7] Relationship Mapping
    Level 1: Simple person → friends list
    Level 2: Query who is friends with who
    Level 3: Mutual friends, degree of separation
    Level 4: Complex networks with attributes

[10] Resource Exchange
    Level 1: Fixed price, buy only
    Level 2: Buy + sell
    Level 3: Dynamic pricing
    Level 4: Multi-resource trading

[6] Progression Tracking
    Level 1: Add points
    Level 2: Level up at threshold
    Level 3: Multiple stats, exponential growth
    Level 4: Prestige system, skill trees
```

---

## Anti-Pattern Warning Signs

```
🚫 RED FLAGS - Avoid these patterns:

┌─────────────────────────────────────────────────────────────┐
│ SYMPTOM              │ PROBLEM          │ FIX               │
├──────────────────────┼──────────────────┼───────────────────┤
│ "Create a list       │ No purpose       │ Use Collection    │
│  called X"           │                  │ Building pattern  │
├──────────────────────┼──────────────────┼───────────────────┤
│ Code just prints     │ Passive          │ Add user input    │
│ facts                │                  │ or choices        │
├──────────────────────┼──────────────────┼───────────────────┤
│ "If x > 73.5"        │ Arbitrary        │ Use meaningful    │
│                      │ number           │ thresholds        │
├──────────────────────┼──────────────────┼───────────────────┤
│ Uses all 15          │ Placeholder      │ Pick 2-4 that     │
│ placeholders         │ spam             │ fit archetype     │
├──────────────────────┼──────────────────┼───────────────────┤
│ Theme only works     │ Not theme-       │ Add pymentor      │
│ with fantasy         │ agnostic         │ version           │
├──────────────────────┼──────────────────┼───────────────────┤
│ No clear success/    │ No feedback      │ Add clear         │
│ failure              │                  │ outcomes          │
├──────────────────────┼──────────────────┼───────────────────┤
│ Student can't        │ No agency        │ Add choices or    │
│ make choices         │                  │ customization     │
└──────────────────────┴──────────────────┴───────────────────┘
```

---

## Quick Templates (Copy-Paste Ready)

### Template 1: Random Assignment

```python
# {{hero}} gets sorted into {{house}}!
import random

def assign_category():
    categories = ["{{house}}", "{{house}}", "{{house}}", "{{house}}"]
    name = input("Enter your name: ")

    print(f"Analyzing {name}...")
    print("Interesting... very interesting...")

    result = random.choice(categories)
    print(f"You belong in {result}!")
```

### Template 2: Inventory Management

```python
# {{hero}}'s Inventory System
def manage_inventory():
    inventory = {"{{item}}": 1, "gold": 50}

    def display():
        print("=== INVENTORY ===")
        for item, qty in inventory.items():
            print(f"{item}: {qty}")

    def add_item(item, qty):
        inventory[item] = inventory.get(item, 0) + qty

    def use_item(item):
        if item in inventory:
            inventory[item] -= 1
            if inventory[item] <= 0:
                del inventory[item]
            print(f"Used {item}!")
```

### Template 3: Character Creation

```python
# Create {{hero}}'s Profile
def create_character():
    character = {
        "name": "{{hero}}",
        "house": "{{house}}",
        "level": 1,
        "health": 100
    }

    print(f"=== {character['name']} ===")
    print(f"House: {character['house']}")
    print(f"Level: {character['level']}")
    print(f"Health: {character['health']}")
```

### Template 4: Challenge/Attempt

```python
# Face the {{creature}}!
def attempt_challenge():
    skill = int(input("Your skill (1-20): "))
    difficulty = 15

    if skill >= difficulty:
        print("Success! You overcame the {{creature}}!")
    elif skill >= difficulty - 5:
        print("Partial success! You barely made it!")
    else:
        print("Failed! The {{creature}} was too strong!")
```

### Template 5: Knowledge Check

```python
# {{school}} Trivia Quiz
def quiz():
    score = 0

    answer = input("Who is {{hero}}'s mentor? ")
    if answer.lower() == "{{mentor}}".lower():
        print("Correct!")
        score += 1

    answer = input("What {{house}} is {{hero}} in? ")
    if answer.lower() == "{{house}}".lower():
        print("Correct!")
        score += 1

    print(f"Score: {score}/2")
```

---

## Success Checklist

Before submitting an exercise with an archetype:

```
ARCHETYPE QUALITY CHECKLIST
═══════════════════════════════════════════════════════════════

Structure
  ☐ Archetype selected matches programming concept
  ☐ Core action is natural and meaningful
  ☐ Follows archetype's narrative flow

Engagement
  ☐ Student has agency (makes choices/builds something)
  ☐ Immediate feedback after actions
  ☐ Clear success/failure or completion states

Implementation
  ☐ Uses 2-4 placeholders (not all 15)
  ☐ Placeholders match archetype requirements
  ☐ Works with AND without fantasy theme
  ☐ Progressive complexity (simple → advanced)

Code Quality
  ☐ Follows PEP 8
  ☐ Meaningful variable names
  ☐ Clear comments with ✏️ markers
  ☐ Functions use `pass` placeholder

Testing
  ☐ Tested in fantasy theme
  ☐ Tested in pymentor theme
  ☐ Clear what student should do
  ☐ Example output makes sense
```

---

## Resources

- **Full Documentation:** [NARRATIVE_ARCHETYPES.md](NARRATIVE_ARCHETYPES.md)
- **Quick Reference:** [ARCHETYPE_QUICK_REFERENCE.md](../templates/ARCHETYPE_QUICK_REFERENCE.md)
- **Placeholder List:** [TEMPLATE.md](../TEMPLATE.md)
- **Writing Guide:** [WRITING_GUIDE.md](WRITING_GUIDE.md)
