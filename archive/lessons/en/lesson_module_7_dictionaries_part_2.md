# Lesson: Dictionaries - Part 2: Modifying Dictionaries

> **Module**: module_7_dictionaries
> **Part**: 2 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Add new key-value pairs, modify existing values, and remove entries from a dictionary

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Adding entries | Assign a value to a new key: `dict["new_key"] = value` |
| Modifying entries | Assign a new value to an existing key: `dict["existing_key"] = new_value` |
| Removing entries | Use `del dict["key"]` to remove a key-value pair |

---

## Lesson Content

### Building on Part 1

In Part 1, we learned to create dictionaries and read values. Now we'll learn to change them - adding new data, updating existing values, and removing entries.

### Adding New Key-Value Pairs

Simply assign to a key that doesn't exist yet:

```python
character = {"name": "{{hero}}", "age": 11}
character["house"] = "{{house}}"
print(character)
# Output: {'name': '{{hero}}', 'age': 11, 'house': '{{house}}'}
```

### Modifying Existing Values

Assign a new value to an existing key:

```python
character = {"name": "{{hero}}", "age": 11}
character["age"] = 12  # Birthday!
print(character["age"])  # Output: 12
```

### Removing Entries

Use `del` to remove a key-value pair:

```python
character = {"name": "{{hero}}", "age": 11, "temporary_item": "map"}
del character["temporary_item"]
print(character)
# Output: {'name': '{{hero}}', 'age': 11}
```

### Watch For

- **Trying to use append()**: Students may try `character.append()` - that's for lists! For dictionaries, just assign to a new key
- **Modifying vs adding confusion**: The syntax is the same - Python creates a new key if it doesn't exist, or updates if it does

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_3_inventory | Practice adding, modifying, and removing items from a dictionary |

---

## Checkpoint

Ask: "How do I add a new key 'color' with value 'orange' to the pet dictionary?"
Expected: `pet['color'] = 'orange'`

---

## If the Student Struggles

- **If trying to use append()**: Explain that append() is for lists (adding to the end). Dictionaries don't have "an end" - they have keys. Show: `dict["new_key"] = value`
- **If confused about add vs modify**: Point out that Python handles both cases automatically. If the key exists, it updates. If not, it creates.
