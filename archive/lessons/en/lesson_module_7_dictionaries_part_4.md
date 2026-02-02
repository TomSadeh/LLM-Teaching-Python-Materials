# Lesson: Dictionaries - Part 4: Looping Through Dictionaries

> **Module**: module_7_dictionaries
> **Part**: 4 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Loop through dictionary keys, values, or both using `.keys()`, `.values()`, and `.items()`

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `.keys()` | Returns all the keys in the dictionary |
| `.values()` | Returns all the values in the dictionary |
| `.items()` | Returns all key-value pairs as tuples |

---

## Lesson Content

### Building on Part 3

We know how to access individual values and handle missing keys. Now let's learn to process all entries in a dictionary using loops.

### Looping Through Keys

By default, looping through a dictionary gives you the keys:

```python
character = {"name": "{{hero}}", "age": 11, "house": "{{house}}"}

for key in character:
    print(key)
# Output:
# name
# age
# house
```

This is the same as using `.keys()`:

```python
for key in character.keys():
    print(key)
```

### Looping Through Values

Use `.values()` to get just the values:

```python
character = {"name": "{{hero}}", "age": 11, "house": "{{house}}"}

for value in character.values():
    print(value)
# Output:
# {{hero}}
# 11
# {{house}}
```

### Looping Through Both (Key-Value Pairs)

Use `.items()` to get both keys and values:

```python
character = {"name": "{{hero}}", "age": 11, "house": "{{house}}"}

for key, value in character.items():
    print(f"{key}: {value}")
# Output:
# name: {{hero}}
# age: 11
# house: {{house}}
```

### Understanding `.items()`

The `.items()` method returns pairs (tuples). The `for key, value` syntax unpacks each pair:

```python
# This is what .items() returns:
print(list(character.items()))
# [('name', '{{hero}}'), ('age', 11), ('house', '{{house}}')]
```

### Watch For

- **Trying to unpack in a regular loop**: `for key, value in character:` won't work - need `.items()`
- **Forgetting which method to use**: keys() for keys, values() for values, items() for both

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_4_word_counter | Build a dictionary by looping through data and counting occurrences |

---

## Checkpoint

Ask: "How do I print both the keys and values of a dictionary?"
Expected: `for key, value in dict.items():` then print them

---

## If the Student Struggles

- **If confused about .items()**: Show the output of `.items()` - it's a list of tuples. Each tuple has (key, value).
- **If the loop only prints keys**: They're probably using `for x in dict:` instead of `for k, v in dict.items():`
