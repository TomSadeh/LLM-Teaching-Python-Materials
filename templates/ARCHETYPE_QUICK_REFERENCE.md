# Archetype Quick Reference

Use this guide when creating new exercises to select the best narrative archetype.

## The 10 Archetypes

| # | Name | Use When Teaching | Core Action | Engagement Hook |
|---|------|-------------------|-------------|-----------------|
| 1 | **Random Assignment** | `random.choice()`, lists | "Sort me!" | Surprise + Identity |
| 2 | **Inventory Management** | Dictionaries, CRUD ops | "Collect items" | Growth + Collection |
| 3 | **Character Creation** | Dicts/classes, attributes | "Define yourself" | Personalization |
| 4 | **Challenge/Attempt** | Conditionals, comparisons | "Try to succeed" | Risk + Reward |
| 5 | **Knowledge Check** | Functions, comparisons | "Test knowledge" | Mastery + Score |
| 6 | **Progression Tracking** | Variables, thresholds | "Level up" | Advancement |
| 7 | **Relationship Mapping** | Nested dicts/lists | "Who knows who" | Discovery |
| 8 | **Decision Tree** | Nested conditionals | "Choose path" | Agency + Branching |
| 9 | **Collection Building** | Lists, `.append()` | "Build collection" | Personal taste |
| 10 | **Resource Exchange** | Multiple variables | "Buy/trade" | Economics |

---

## Quick Selection by Module

### Module 0 (Basics)
- **Character Creation**: Define variables with different types
- **Collection Building**: Create first list of favorites

### Module 1 (Loops)
- **Collection Building**: Loop to add items
- **Progression Tracking**: Loop to increment stats

### Module 2 (Conditionals)
- **Challenge/Attempt**: If/elif/else for success levels
- **Knowledge Check**: Quiz with scoring
- **Decision Tree**: Choose your adventure

### Module 3 (Lists)
- **Random Assignment**: Sorting Hat pattern
- **Collection Building**: Build and display lists
- **Knowledge Check**: Random quiz questions

### Module 4 (While Loops)
- **Decision Tree**: Adventure game
- **Challenge/Attempt**: Guess until correct
- **Progression Tracking**: Track attempts/score

### Module 5 (Functions)
- **Knowledge Check**: Question-asking function
- **Challenge/Attempt**: Function returns success/fail
- **Inventory Management**: Functions for add/remove

### Module 7 (Dictionaries)
- **Inventory Management**: Items with quantities
- **Character Creation**: Character profiles
- **Relationship Mapping**: Nested connections
- **Resource Exchange**: Shop system

### Module 8 (Modules)
- **Character Creation**: Import character templates
- **Random Assignment**: Use random module
- **Progression Tracking**: Import stats system

### Module 9 (OOP)
- **Character Creation**: Classes and instances
- **Challenge/Attempt**: Method interactions
- **Inventory Management**: Class-based inventory
- **Progression Tracking**: Level-up methods

---

## Quick Templates

### Template: Random Assignment

```python
def random_assignment_exercise():
    """{{hero}} gets sorted into a {{house}}!"""
    import random

    categories = ["category1", "category2", "category3", "category4"]
    subject = input("Enter name: ")

    print(f"Analyzing {subject}...")
    choice = random.choice(categories)
    print(f"Result: {choice}!")
```

**Placeholders:** `{{house}}`, `{{hero}}`, `{{school}}`

---

### Template: Inventory Management

```python
def inventory_exercise():
    """Manage {{hero}}'s items"""
    inventory = {"{{item}}": 1}

    def add_item(item, qty):
        inventory[item] = inventory.get(item, 0) + qty

    def remove_item(item, qty):
        if item in inventory:
            inventory[item] -= qty
            if inventory[item] <= 0:
                del inventory[item]

    def display():
        for item, qty in inventory.items():
            print(f"{item}: {qty}")
```

**Placeholders:** `{{hero}}`, `{{item}}`, `{{pet}}`

---

### Template: Character Creation

```python
def character_creation_exercise():
    """Create a profile for {{hero}}"""
    character = {
        "name": "{{hero}}",
        "affiliation": "{{house}}",
        "level": 1,
        "health": 100
    }

    print(f"=== {character['name']} ===")
    print(f"House: {character['affiliation']}")
    print(f"Level: {character['level']}")
```

**Placeholders:** `{{hero}}`, `{{house}}`, `{{school}}`, `{{item}}`

---

### Template: Challenge/Attempt

```python
def challenge_exercise():
    """Face the {{creature}}!"""
    skill = int(input("Your skill (1-20): "))
    difficulty = 15

    if skill >= difficulty:
        print("Success! You overcame the challenge!")
    elif skill >= difficulty - 5:
        print("Partial success!")
    else:
        print("Failed! Try again.")
```

**Placeholders:** `{{creature}}`, `{{hero}}`, `{{spell1}}`

---

### Template: Knowledge Check

```python
def quiz_exercise():
    """Book trivia quiz!"""
    score = 0

    def ask(question, answer):
        nonlocal score
        if input(question + " ").lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Answer: {answer}")

    ask("Who is {{hero}}'s mentor?", "{{mentor}}")
    ask("What {{house}} is {{hero}} in?", "{{house}}")

    print(f"Score: {score}/2")
```

**Placeholders:** Any theme variables for questions

---

### Template: Progression Tracking

```python
def level_up_exercise():
    """{{hero}} gains experience!"""
    character = {"name": "{{hero}}", "level": 1, "xp": 0}

    def gain_xp(amount):
        character["xp"] += amount
        if character["xp"] >= 100:
            character["level"] += 1
            character["xp"] -= 100
            print(f"⭐ Level {character['level']}!")

    gain_xp(60)
    gain_xp(50)  # Triggers level up
```

**Placeholders:** `{{hero}}`, `{{heroine}}`

---

### Template: Relationship Mapping

```python
def relationship_exercise():
    """Who knows {{hero}}?"""
    friends = {
        "{{hero}}": ["{{friend}}", "{{heroine}}"],
        "{{heroine}}": ["{{hero}}", "{{mentor}}"],
        "{{friend}}": ["{{hero}}"]
    }

    def get_friends(person):
        return friends.get(person, [])

    def mutual_friends(p1, p2):
        return set(get_friends(p1)) & set(get_friends(p2))
```

**Placeholders:** `{{hero}}`, `{{heroine}}`, `{{friend}}`, `{{mentor}}`

---

### Template: Decision Tree

```python
def adventure_exercise():
    """Explore {{location}}!"""
    print("You enter {{location}}...")
    print("1. Go left")
    print("2. Go right")

    choice = input("Choice: ")

    if choice == "1":
        print("You find a {{item}}!")
        print("1. Take it")
        print("2. Leave it")
        choice2 = input("Choice: ")
        # Nested decision...
    else:
        print("You encounter a {{creature}}!")
```

**Placeholders:** `{{location}}`, `{{item}}`, `{{creature}}`, `{{spell1}}`

---

### Template: Collection Building

```python
def collection_exercise():
    """Build your favorite {{hero}} list!"""
    favorites = []

    while True:
        item = input("Add favorite (or 'done'): ")
        if item == 'done':
            break
        favorites.append(item)

    print("\nYour favorites:")
    for i, item in enumerate(favorites, 1):
        print(f"{i}. {item}")
```

**Placeholders:** Any as examples (`{{hero}}`, `{{heroine}}`)

---

### Template: Resource Exchange

```python
def shop_exercise():
    """Visit the {{school}} shop!"""
    gold = 100
    inventory = {}

    shop = {
        "{{item}}": 50,
        "potion": 20
    }

    def buy(item):
        nonlocal gold
        price = shop[item]
        if gold >= price:
            gold -= price
            inventory[item] = inventory.get(item, 0) + 1
            print(f"Bought {item}!")
        else:
            print("Not enough gold!")
```

**Placeholders:** `{{school}}`, `{{item}}`, `{{pet}}`

---

## Combination Patterns

### Inventory + Shop (Advanced)
- Archetype 2 + Archetype 10
- Best for: Module 7, Module 9
- Example: RPG Inventory with shop system

### Character + Challenge (Combat)
- Archetype 3 + Archetype 4
- Best for: Module 9 (OOP)
- Example: Characters battle with stats

### Decision + Challenge (Adventure)
- Archetype 8 + Archetype 4
- Best for: Module 2, Module 4
- Example: Choose path, face challenges

### Collection + Random (Personalized)
- Archetype 9 + Archetype 1
- Best for: Module 3
- Example: Build list, pick random from it

---

## Archetype Checklist

Before writing an exercise, verify:

- [ ] Archetype matches programming concept being taught
- [ ] Core action feels natural (not forced)
- [ ] Student has agency (makes choices/builds something)
- [ ] Immediate feedback on actions
- [ ] Works with AND without fantasy theme
- [ ] Progressive complexity (simple → advanced)
- [ ] Uses 2-4 placeholders (not all 15)

---

## Anti-Pattern Warning Signs

🚫 **Avoid these:**

1. **Theme without purpose**
   - Bad: "Make a list called wizard_names" (just list practice)
   - Fix: Use Collection Building or Random Assignment

2. **No clear action**
   - Bad: "Here are some variables about characters"
   - Fix: What does student DO with them?

3. **Passive observation**
   - Bad: Code that prints facts
   - Fix: Student creates/modifies/chooses

4. **Arbitrary numbers/conditions**
   - Bad: "If x > 73.5"
   - Fix: Use meaningful thresholds (health, score, level)

5. **Disconnected placeholders**
   - Bad: Using all 15 placeholders randomly
   - Fix: Pick 2-4 that fit the archetype

---

## FAQ

**Q: Can I mix archetypes?**
A: Yes! Best exercises combine 2-3 (e.g., Character Creation + Challenge/Attempt)

**Q: What if my concept doesn't fit an archetype?**
A: Check if you're teaching the RIGHT concept. Most concepts map to archetypes.

**Q: How do I choose placeholders?**
A: Match archetype's "Required Placeholders" section in main doc.

**Q: Should every exercise use an archetype?**
A: For write_code exercises: YES. For reading exercises: Less critical.

**Q: What if I'm teaching something technical (imports, syntax)?**
A: Use lightest archetype (Character Creation) or skip for pure syntax.

---

## See Also

- [NARRATIVE_ARCHETYPES.md](../docs/NARRATIVE_ARCHETYPES.md) - Full archetype documentation
- [TEMPLATE.md](../TEMPLATE.md) - Available placeholders
- [WRITING_GUIDE_EXERCISES.md](../docs/WRITING_GUIDE_EXERCISES.md) - Exercise writing standards
- [WRITING_GUIDE_LESSONS.md](../docs/WRITING_GUIDE_LESSONS.md) - Lesson writing standards
