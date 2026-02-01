# Narrative Archetypes for Exercise Design

This document catalogs reusable narrative patterns identified from high-scoring exercises. Each archetype represents a **universal structure** that can be adapted across themes and programming concepts.

---

## Analysis Methodology

Examined exercises from top-performing modules:
- **Module 7** (Dictionaries): RPG Inventory - 9/9 narrative score
- **Module 3** (Lists): Sorting Hat, character lists - 8/9 score
- **Module 9** (OOP): Wizard inheritance - 8/9 score
- **Module 2** (Decisions): Password guard - 7/9 score

**Key finding:** Success comes from matching a **programming operation** to a **natural real-world action** that feels meaningful to the learner.

---

## The 10 Core Archetypes

### 1. RANDOM ASSIGNMENT
**"The Sorting Hat Pattern"**

**Universal Structure:**
- Player/object needs categorization
- System randomly assigns to a category
- Assignment feels meaningful (not arbitrary)

**Programming Concepts:**
- `random.choice()` from a list
- List indexing
- Print formatting

**Required Placeholders:**
- Categories: `{{house}}` (4 options) OR list of items/groups
- Subject: `{{hero}}`, user input, or item being sorted

**Narrative Flow:**
1. Introduce the selection ceremony/moment
2. Build anticipation ("Hmm, difficult...")
3. Make the selection
4. Reveal with impact

**Example Implementations:**

```python
# Theme-agnostic template
def random_assignment():
    """Assign an entity to a random category."""
    categories = [category1, category2, category3, category4]
    subject = input("Who/what is being assigned? ")

    print(f"Analyzing {subject}...")
    print("Interesting... very interesting...")

    choice = random.choice(categories)
    print(f"You belong in {choice}!")
```

**Cross-theme applications:**
- Fantasy: House sorting (Hogwarts, Camp Half-Blood, Districts)
- Real-world: Team assignment, role selection, random partner
- Abstract: Group categorization, cluster assignment

**Why it works:**
- Randomness creates surprise and replayability
- Assignment feels like an "official" moment
- Natural use of lists and random module

---

### 2. INVENTORY MANAGEMENT
**"The RPG Inventory Pattern"**

**Universal Structure:**
- Player has a collection of items with quantities
- Actions: add, remove, use, display
- Items have properties (type, quantity, effect)

**Programming Concepts:**
- Dictionary key-value pairs
- Dictionary methods (`.get()`, `.pop()`, `.setdefault()`)
- Conditional logic for item effects
- Iteration over dictionary

**Required Placeholders:**
- Items: `{{item}}`, `{{pet}}`, generic items
- Actions/effects: `{{spell1}}` for special effects
- Character: `{{hero}}` as inventory owner

**Narrative Flow:**
1. Display current inventory state
2. Perform action (add/remove/use)
3. Show consequences
4. Update and display new state

**Example Implementations:**

```python
# Theme-agnostic template
def inventory_system():
    """Manage a collection with quantities."""
    inventory = {}

    def add_item(item, quantity):
        inventory[item] = inventory.get(item, 0) + quantity

    def remove_item(item, quantity):
        if item in inventory:
            inventory[item] -= quantity
            if inventory[item] <= 0:
                del inventory[item]

    def use_item(item):
        if item in inventory:
            remove_item(item, 1)
            return get_item_effect(item)

    def display():
        for item, qty in inventory.items():
            print(f"{item}: {qty}")
```

**Cross-theme applications:**
- Fantasy: Spell components, magical items, potions
- Real-world: Shopping list, budget tracker, supplies
- Abstract: Resource management, stock tracking

**Why it works:**
- Mirrors real collection management
- Natural CRUD operations
- Immediate visual feedback
- Quantities make math meaningful

---

### 3. CHARACTER CREATION
**"The Character Sheet Pattern"**

**Universal Structure:**
- Define entity with multiple attributes
- Attributes have types (string, int, bool)
- Display formatted character information

**Programming Concepts:**
- Dictionary or class attributes
- Data types
- String formatting
- Structured data representation

**Required Placeholders:**
- Names: `{{hero}}`, `{{heroine}}`, `{{mentor}}`
- Locations: `{{school}}`, `{{house}}`
- Items: `{{item}}`, `{{pet}}`

**Narrative Flow:**
1. Initialize character template
2. Fill in attributes (hardcoded or input)
3. Display formatted character sheet
4. (Optional) Compare characters or modify attributes

**Example Implementations:**

```python
# Theme-agnostic template
def create_character():
    """Define an entity with structured attributes."""
    character = {
        "name": "",
        "affiliation": "",
        "level": 1,
        "health": 100,
        "special_ability": ""
    }

    # Display character card
    print(f"=== {character['name']} ===")
    print(f"Affiliation: {character['affiliation']}")
    print(f"Level: {character['level']}")
    print(f"Health: {character['health']}")
    print(f"Special: {character['special_ability']}")
```

**Cross-theme applications:**
- Fantasy: Wizard, hero, creature profiles
- Real-world: Contact info, profile cards, resume
- Abstract: Object specification, configuration

**Why it works:**
- Players love creating "their character"
- Natural introduction to structured data
- Multiple data types in one exercise
- Easy to visualize and verify

---

### 4. CHALLENGE/ATTEMPT
**"The Quest Pattern"**

**Universal Structure:**
- Player attempts a task
- Success/failure determined by conditions
- Different outcomes based on result

**Programming Concepts:**
- Conditionals (if/elif/else)
- Comparisons
- Boolean logic
- Random success/failure

**Required Placeholders:**
- Character: `{{hero}}`, user input
- Challenge: `{{creature}}`, `{{villain}}`, abstract challenge
- Success: `{{spell1}}`, special ability
- Location: `{{location}}`, `{{place}}`

**Narrative Flow:**
1. Present the challenge
2. Player makes choice or attempt
3. Evaluate conditions
4. Show outcome with consequences

**Example Implementations:**

```python
# Theme-agnostic template
def attempt_challenge():
    """Try to overcome an obstacle with conditions."""
    challenge_difficulty = 15
    player_skill = int(input("Enter your skill level (1-20): "))

    print("You face the challenge...")

    if player_skill >= challenge_difficulty:
        print("Success! You overcome the obstacle!")
    elif player_skill >= challenge_difficulty - 5:
        print("Partial success! It was difficult...")
    else:
        print("You fail. Try again later.")
```

**Cross-theme applications:**
- Fantasy: Spell casting, creature encounter, duel
- Real-world: Test taking, job interview, competition
- Abstract: Threshold checking, validation

**Why it works:**
- Clear success/failure provides immediate feedback
- Tension and stakes
- Natural use of conditionals
- Multiple difficulty levels teach elif

---

### 5. KNOWLEDGE CHECK
**"The Quiz Pattern"**

**Universal Structure:**
- Series of questions
- Check answers against correct values
- Track score
- Report results

**Programming Concepts:**
- String comparison
- Functions with return values
- Score accumulation
- Loops for multiple questions

**Required Placeholders:**
- Characters: `{{hero}}`, `{{heroine}}`, `{{mentor}}`
- Locations: `{{school}}`, `{{house}}`
- Items: `{{item}}`, `{{pet}}`
- Any theme-specific knowledge

**Narrative Flow:**
1. Welcome to quiz/test
2. For each question:
   - Ask question
   - Get answer
   - Check correctness
   - Update score
3. Report final score

**Example Implementations:**

```python
# Theme-agnostic template
def quiz_game():
    """Test knowledge with scored questions."""
    score = 0
    total = 0

    def ask(question, correct_answer):
        nonlocal score, total
        total += 1
        answer = input(question + " ")
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
            return True
        else:
            print(f"Wrong! The answer was {correct_answer}")
            return False

    # Ask questions
    ask("Question 1?", "answer1")
    ask("Question 2?", "answer2")

    print(f"Final score: {score}/{total}")
```

**Cross-theme applications:**
- Fantasy: Lore quiz, character knowledge, spell identification
- Real-world: Trivia game, study flashcards, exam
- Abstract: Data validation, pattern matching

**Why it works:**
- Immediate right/wrong feedback
- Score provides motivation
- Repeatable to improve
- Students can customize questions

---

### 6. PROGRESSION TRACKING
**"The Level-Up Pattern"**

**Universal Structure:**
- Character/entity has stats that grow
- Experience/points accumulate
- Thresholds trigger advancement
- Visual progress indicators

**Programming Concepts:**
- Numeric variables and updates
- Threshold conditionals
- Modulo for overflow (XP → level)
- State tracking

**Required Placeholders:**
- Character: `{{hero}}`, `{{heroine}}`
- Progression metric: level, rank, mastery
- Stats: health, power, skill

**Narrative Flow:**
1. Show current state
2. Gain experience/points
3. Check if threshold reached
4. Level up with fanfare
5. Display new state

**Example Implementations:**

```python
# Theme-agnostic template
def level_system():
    """Track progression and leveling."""
    character = {
        "name": "Player",
        "level": 1,
        "xp": 0,
        "xp_needed": 100
    }

    def gain_xp(amount):
        character["xp"] += amount
        print(f"+{amount} XP!")

        while character["xp"] >= character["xp_needed"]:
            character["xp"] -= character["xp_needed"]
            character["level"] += 1
            character["xp_needed"] = int(character["xp_needed"] * 1.5)
            print(f"⭐ LEVEL UP! Now level {character['level']}!")
```

**Cross-theme applications:**
- Fantasy: Wizard levels, skill mastery, rank advancement
- Real-world: Grade progression, achievement unlocking
- Abstract: Counter thresholds, state transitions

**Why it works:**
- Visual progress is motivating
- Math has immediate meaning
- Threshold logic is clear
- Loops naturally emerge for multiple level-ups

---

### 7. RELATIONSHIP MAPPING
**"The Social Network Pattern"**

**Universal Structure:**
- Entities have connections to other entities
- Relationships are defined and queried
- Bidirectional or directed connections

**Programming Concepts:**
- Nested dictionaries
- Lists as values
- Dictionary lookup
- Set operations for mutual connections

**Required Placeholders:**
- Characters: `{{hero}}`, `{{heroine}}`, `{{friend}}`, `{{mentor}}`
- Relationships: friends, family, allies, enemies
- Groups: `{{group}}`, `{{house}}`

**Narrative Flow:**
1. Define relationships
2. Query connections ("Who are X's friends?")
3. Find paths ("How are X and Y connected?")
4. Discover mutual connections

**Example Implementations:**

```python
# Theme-agnostic template
def relationship_map():
    """Map connections between entities."""
    relationships = {
        "character_a": ["character_b", "character_c"],
        "character_b": ["character_a", "character_d"],
        "character_c": ["character_a"],
        "character_d": ["character_b"]
    }

    def get_friends(character):
        return relationships.get(character, [])

    def mutual_friends(char1, char2):
        friends1 = set(get_friends(char1))
        friends2 = set(get_friends(char2))
        return friends1 & friends2
```

**Cross-theme applications:**
- Fantasy: Character alliances, house memberships
- Real-world: Social networks, org charts, family trees
- Abstract: Graph connections, network topology

**Why it works:**
- Mirrors real social understanding
- Natural use of nested structures
- Queries feel purposeful
- Set operations have clear meaning

---

### 8. DECISION TREE
**"The Choose Your Path Pattern"**

**Universal Structure:**
- Present situation with choices
- Each choice leads to new situation
- Branching paths with different endings
- Nested decisions

**Programming Concepts:**
- Nested conditionals
- Multiple elif branches
- Input validation
- State tracking through choices

**Required Placeholders:**
- Locations: `{{school}}`, `{{location}}`, `{{place}}`
- Characters: `{{hero}}`, `{{villain}}`, `{{mentor}}`
- Items: `{{item}}`, `{{spell1}}`
- Outcomes: `{{exclamation}}`

**Narrative Flow:**
1. Set scene
2. Present 2-4 choices
3. Get player input
4. Based on choice, go to next situation
5. Repeat 2-3 levels deep
6. End with outcome

**Example Implementations:**

```python
# Theme-agnostic template
def decision_tree():
    """Branch story based on player choices."""
    print("You enter the dark forest...")
    print("1. Follow the path")
    print("2. Go off-trail")
    print("3. Turn back")

    choice = input("What do you do? ")

    if choice == "1":
        print("The path leads to a clearing...")
        print("1. Investigate")
        print("2. Keep moving")
        choice2 = input("What now? ")

        if choice2 == "1":
            print("You find a treasure!")
        else:
            print("You continue safely.")

    elif choice == "2":
        print("You get lost!")

    else:
        print("You return home safely.")
```

**Cross-theme applications:**
- Fantasy: Adventure quest, dungeon exploration
- Real-world: Life choices, problem-solving scenarios
- Abstract: State machine, flowchart logic

**Why it works:**
- Agency creates engagement
- Clear cause-and-effect
- Natural nested conditionals
- Replayability to see other paths

---

### 9. COLLECTION BUILDING
**"The Favorites List Pattern"**

**Universal Structure:**
- Start with empty or small collection
- Add items one by one
- Display the collection
- Optional: sort, filter, or search

**Programming Concepts:**
- List initialization
- `.append()` method
- Loops for user input
- List indexing and slicing

**Required Placeholders:**
- Items collected: `{{hero}}`, `{{heroine}}`, `{{spell1}}`, generic items
- Collection name: favorites, wishlist, spellbook

**Narrative Flow:**
1. Initialize empty collection
2. Prompt for items to add
3. Add items to collection
4. Display collection
5. (Optional) Access specific items

**Example Implementations:**

```python
# Theme-agnostic template
def build_collection():
    """Create and display a collection."""
    collection = []

    print("Build your collection!")

    while True:
        item = input("Add item (or 'done'): ")
        if item.lower() == 'done':
            break
        collection.append(item)
        print(f"Added {item}!")

    print("\nYour collection:")
    for i, item in enumerate(collection, 1):
        print(f"{i}. {item}")
```

**Cross-theme applications:**
- Fantasy: Favorite characters, spell collection
- Real-world: Wishlist, todo list, playlist
- Abstract: Data accumulation, user input lists

**Why it works:**
- Personal investment in their list
- Clear before/after states
- Natural introduction to `.append()`
- Easy to verify correctness

---

### 10. RESOURCE EXCHANGE
**"The Shop/Trade Pattern"**

**Universal Structure:**
- Two parties exchange resources
- Check if exchange is valid
- Update both parties' inventories
- Handle insufficient resources

**Programming Concepts:**
- Multiple variable updates
- Conditional validation
- Subtraction and addition
- Dictionary updates for complex trades

**Required Placeholders:**
- Currency: gold, points, `{{item}}`
- Items: `{{pet}}`, potions, equipment
- Merchant: shopkeeper, `{{mentor}}`

**Narrative Flow:**
1. Display available items and prices
2. Player chooses what to buy/trade
3. Check if they can afford it
4. If yes: deduct cost, add item
5. If no: inform and return

**Example Implementations:**

```python
# Theme-agnostic template
def shop_system():
    """Buy and sell with resource checking."""
    inventory = {"gold": 100}
    shop = {
        "item1": 20,
        "item2": 50,
        "item3": 100
    }

    def buy(item):
        price = shop.get(item)
        if price is None:
            print("Item not found!")
        elif inventory["gold"] >= price:
            inventory["gold"] -= price
            inventory[item] = inventory.get(item, 0) + 1
            print(f"Bought {item}!")
        else:
            print("Not enough gold!")
```

**Cross-theme applications:**
- Fantasy: Magic shop, potion trading
- Real-world: Store, marketplace, budget management
- Abstract: Resource allocation, transaction processing

**Why it works:**
- Real-world relevance (shopping)
- Clear success/failure conditions
- Math has immediate purpose
- Multiple operations in sequence

---

## Archetype Selection Guide

### By Programming Concept

| Concept | Best Archetypes |
|---------|----------------|
| Lists | Random Assignment, Collection Building |
| Dictionaries | Inventory Management, Character Creation, Relationship Mapping |
| Conditionals | Challenge/Attempt, Decision Tree, Knowledge Check |
| Loops | Collection Building, Knowledge Check, Decision Tree |
| Functions | Knowledge Check, Inventory Management |
| OOP | Character Creation, Challenge/Attempt, Inventory Management |
| Random | Random Assignment, Challenge/Attempt |

### By Difficulty Level

**Beginner (Modules 0-2):**
- Knowledge Check
- Collection Building
- Character Creation (simple)
- Random Assignment

**Intermediate (Modules 3-5):**
- Inventory Management
- Challenge/Attempt
- Decision Tree
- Progression Tracking

**Advanced (Modules 6-9):**
- Relationship Mapping
- Resource Exchange
- All archetypes combined

### By Engagement Level

**High Replay Value:**
- Random Assignment
- Decision Tree
- Challenge/Attempt

**High Personalization:**
- Character Creation
- Collection Building
- Knowledge Check (custom questions)

**High Complexity:**
- Inventory Management
- Relationship Mapping
- Resource Exchange

---

## Combining Archetypes

Powerful exercises often combine 2-3 archetypes:

**Examples:**

1. **RPG Inventory (Module 7)**
   - Inventory Management + Resource Exchange
   - Add/remove items + shop system

2. **Sorting Hat (Module 3)**
   - Random Assignment + Character Creation
   - Assign house + display character info

3. **Adventure Game (Module 4)**
   - Decision Tree + Challenge/Attempt
   - Choose path + test success conditions

4. **Character Battle (Module 9)**
   - Character Creation + Challenge/Attempt + Progression Tracking
   - Define characters + combat system + level up

---

## Design Principles

### What Makes an Archetype Work

1. **Natural Mapping**
   - Programming operation feels like real-world action
   - Example: `.append()` = "add to collection" (not "append to array")

2. **Immediate Feedback**
   - Every action shows visible result
   - Example: After buying item, see updated inventory

3. **Clear Mental Model**
   - Student understands what should happen
   - Example: "Higher score wins" is clear

4. **Progressive Disclosure**
   - Simple version first, then add complexity
   - Example: Display inventory → Add items → Remove items → Use items with effects

5. **Theme-Agnostic Core**
   - Structure works with OR without fantasy theme
   - Example: Quiz works for book trivia OR math facts

### Anti-Patterns to Avoid

1. **Forced Theming**
   - Don't make exercise about theme when programming is unrelated
   - Bad: "Make a list called potion_ingredients but it's just list practice"
   - Good: "Track potion inventory with add/remove/use actions"

2. **Arbitrary Collections**
   - Collections should have purpose
   - Bad: "Make a list of 5 numbers"
   - Good: "Track daily scores to find your best"

3. **Meaningless Conditions**
   - If/else should match real decisions
   - Bad: "If number > 10 print 'big' else 'small'"
   - Good: "If health > 50 you can fight, else rest"

4. **Passive Learning**
   - Student should DO something, not just observe
   - Bad: Code that just prints facts
   - Good: Code where student makes choices

---

## Template Usage

Each archetype can be adapted by:

1. **Identify the core structure** from archetype description
2. **Map to programming concept** you're teaching
3. **Select appropriate placeholders** from TEMPLATE.md
4. **Add theme-agnostic version** for pymentor theme
5. **Test cross-theme** to ensure it works in all themes

**Example adaptation:**

```
Teaching: Dictionary .get() method
Archetype: Inventory Management
Structure: Check if item exists, return quantity or default
Placeholders: {{item}}, {{pet}}
Theme-agnostic: "backpack.get('notebook', 0)"
```

---

## Next Steps

1. **Audit existing exercises** against these archetypes
2. **Identify which archetypes are underused** in each module
3. **Create archetype-based templates** for rapid exercise creation
4. **Tag exercises** with their archetype in metadata
5. **Balance archetype distribution** across curriculum

---

## Appendix: Archetype Frequency Analysis

Based on current exercises:

| Archetype | Module 2 | Module 3 | Module 7 | Module 9 | Total |
|-----------|:--------:|:--------:|:--------:|:--------:|:-----:|
| Random Assignment | 0 | 2 | 0 | 0 | 2 |
| Inventory Management | 0 | 1 | 3 | 0 | 4 |
| Character Creation | 0 | 1 | 2 | 5 | 8 |
| Challenge/Attempt | 2 | 0 | 0 | 1 | 3 |
| Knowledge Check | 1 | 0 | 1 | 0 | 2 |
| Progression Tracking | 0 | 0 | 1 | 0 | 1 |
| Relationship Mapping | 0 | 0 | 0 | 0 | 0 |
| Decision Tree | 0 | 0 | 0 | 0 | 0 |
| Collection Building | 0 | 4 | 0 | 0 | 4 |
| Resource Exchange | 0 | 0 | 1 | 0 | 1 |

**Gaps identified:**
- Relationship Mapping: Not used yet (perfect for Module 7 nested dicts)
- Decision Tree: Not used in scaffolded exercises (Module 4 candidate)
- Progression Tracking: Underused (Module 7 or Module 9 candidate)
