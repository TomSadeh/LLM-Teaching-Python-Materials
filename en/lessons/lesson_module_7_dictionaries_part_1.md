# Lesson: Dictionaries - Part 1: What's a Dictionary?

> **Module**: module_7_dictionaries
> **Part**: 1 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Variables and basic data types
- [ ] Lists and how to access items by index
- [ ] Loops (for and while)
- [ ] Functions (helpful but not required)

---

## Learning Objective

By the end of this part, the student will be able to:

- Create a dictionary with key-value pairs and access values using keys

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Dictionary | A collection of key-value pairs, like a real dictionary (word -> definition) |
| Key | The unique identifier used to look up a value (like a word) |
| Value | The data stored at a key (like a definition) |
| Key-value pair | A single entry: `"name": "Maya"` |

---

## Lesson Content

### Getting Started

Introduce dictionaries by contrasting them with lists:
- **Lists** use numeric indices (0, 1, 2) to access items
- **Dictionaries** use meaningful keys ("name", "age", "house") to access items

Think of a real dictionary: you look up a **word** (the key) to find its **definition** (the value).

### Creating a Dictionary

```python
# A simple character dictionary
character = {"name": "{{hero}}", "age": 11}

# An empty dictionary
empty_dict = {}
```

### Accessing Values

Use square brackets with the key name:

```python
character = {"name": "{{hero}}", "age": 11}
print(character["name"])  # Output: {{hero}}
print(character["age"])   # Output: 11
```

### Watch For

- **Using list syntax**: Students may try `character[0]` instead of `character["name"]`
- **Forgetting quotes**: String keys need quotes: `character["name"]` not `character[name]`
- **KeyError**: Accessing a key that doesn't exist causes an error

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_1_spellbook | Introduction to key-value pairs with spell names and effects |
| exercise_2_character_stats | Practice accessing and reading values from a dictionary |

---

## Checkpoint

Ask: "If I have `pet = {'name': 'Fluffy', 'type': 'cat'}`, how do I get 'Fluffy'?"
Expected: `pet['name']` or `pet.get('name')`

---

## If the Student Struggles

- **If confused about keys vs indices**: Use a real dictionary analogy - you look up words, not page numbers. Ask: "In a real dictionary, do you look up 'page 47' or do you look up 'python'?"
- **If getting KeyError on access**: Remind them that the key must exist and be spelled exactly right, including capitalization

---

## Real-World Connection

> "Every user profile on any website is a dictionary - your username, email, profile picture, and settings are all stored as key-value pairs."

---

## Notes for the LLM Teacher

- Dictionaries feel very different from lists - take time with the mental model shift
- The real dictionary analogy (word -> definition) is very effective
- Keep examples simple in this phase - just creation and reading, no modifications yet
- RPG character stats make an excellent, engaging example context
