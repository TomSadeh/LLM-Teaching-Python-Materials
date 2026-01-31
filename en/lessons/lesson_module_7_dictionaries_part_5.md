# Lesson: Dictionaries - Part 5: Real-World Structures

> **Module**: module_7_dictionaries
> **Part**: 5 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Use dictionaries to represent real-world data including nested structures

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Nested dictionary | A dictionary inside another dictionary, for complex data |
| Data modeling | Choosing the right structure (dict vs list) for your data |

---

## Lesson Content

### Building on Part 4

We can now create, modify, access safely, and loop through dictionaries. Now let's see how they're used in real applications.

### Character Stats (RPG Style)

Dictionaries are perfect for game character data:

```python
player = {
    "name": "{{hero}}",
    "level": 5,
    "health": 100,
    "inventory": ["wand", "potion", "{{item}}"],
    "skills": {"attack": 15, "defense": 10, "magic": 20}
}
```

### Nested Dictionaries

A dictionary can contain other dictionaries:

```python
school = {
    "{{house}}": {
        "points": 350,
        "head": "{{mentor}}",
        "members": ["{{hero}}", "{{friend}}"]
    },
    "Slytherin": {
        "points": 320,
        "head": "{{villain}}",
        "members": ["{{creature}}", "Pansy"]
    }
}

# Access nested data:
print(school["{{house}}"]["points"])  # 350
print(school["{{house}}"]["members"][0])  # {{hero}}
```

### When to Use Dict vs List

| Use a **List** when... | Use a **Dictionary** when... |
|------------------------|------------------------------|
| Order matters | You need to look up by name/key |
| Items are similar | Each item has a unique identifier |
| You access by position | Items have multiple properties |

```python
# List: ordered collection of similar items
spells = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]

# Dictionary: named properties of one thing
character = {"name": "{{hero}}", "age": 11, "house": "{{house}}"}
```

### Simple Database Pattern

Store multiple records using a list of dictionaries:

```python
contacts = [
    {"name": "{{hero}}", "phone": "555-1234"},
    {"name": "{{friend}}", "phone": "555-5678"},
    {"name": "{{mentor}}", "phone": "555-9999"}
]

# Find a contact:
for contact in contacts:
    if contact["name"] == "{{hero}}":
        print(contact["phone"])
```

### Watch For

- **Over-nesting**: Too many levels of nesting becomes hard to read and maintain
- **Mixing up access patterns**: Remember: dict uses keys `["key"]`, list uses indices `[0]`

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_6_contact_book | Build a mini database with multiple entries |
| exercise_7_nested_data | Work with dictionaries inside dictionaries |
| exercise_8_game_state | Manage complex game save data |
| exercise_9_quiz_data | Combine all dictionary concepts in a full application |

---

## Checkpoint

Ask: "When would you use a dictionary instead of a list?"
Expected: When you want to look up data by a name/key rather than by position. For example, storing character stats where you want to access by "health" or "attack" rather than remembering that health is at index 0.

---

## If the Student Struggles

- **If confused about nesting**: Start with simple examples. Draw it out: the outer dictionary contains inner dictionaries, like folders containing files.
- **If unsure when to use dicts vs lists**: Ask "Do you care about order, or do you want to look things up by name?" Order = list, lookup by name = dict.
- **If overwhelmed by complexity**: Suggest breaking complex structures into smaller pieces first, then combining them.
