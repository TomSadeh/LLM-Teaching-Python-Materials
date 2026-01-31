# Lesson: Dictionaries - Part 3: Checking and Safe Access

> **Module**: module_7_dictionaries
> **Part**: 3 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Handle missing keys gracefully using `in` checks and the `.get()` method

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `in` operator | Check if a key exists: `if "name" in my_dict:` |
| `.get()` method | Safely retrieves a value, returning None (or a default) if key doesn't exist |
| KeyError | The error Python raises when you try to access a key that doesn't exist |

---

## Lesson Content

### Building on Part 2

We can now create, read, and modify dictionaries. But what happens when we try to access a key that doesn't exist? Let's learn to handle that safely.

### The KeyError Problem

```python
character = {"name": "{{hero}}", "age": 11}
print(character["pet"])  # KeyError! The key "pet" doesn't exist
```

### Checking with `in`

Before accessing, check if the key exists:

```python
character = {"name": "{{hero}}", "age": 11}

if "pet" in character:
    print(character["pet"])
else:
    print("No pet found")
# Output: No pet found
```

### Safe Access with `.get()`

The `.get()` method returns `None` if the key doesn't exist (no error):

```python
character = {"name": "{{hero}}", "age": 11}

pet = character.get("pet")
print(pet)  # Output: None

# You can also provide a default value:
pet = character.get("pet", "no pet")
print(pet)  # Output: no pet
```

### Comparing the Two Approaches

```python
# Method 1: Check with 'in' first (good for doing something different)
if "spell" in wizard:
    cast_spell(wizard["spell"])
else:
    print("No spell equipped!")

# Method 2: Use .get() with default (good for simple defaults)
spell = wizard.get("spell", "{{spell1}}")
cast_spell(spell)
```

### Watch For

- **Forgetting the `in` check**: Students may access keys directly and get KeyError
- **Confusing `.get()` parameters**: The second parameter is the default, not something else

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_5_translator | Practice dictionary lookup with handling of missing keys |

---

## Checkpoint

Ask: "What's the difference between `dict['key']` and `dict.get('key')`?"
Expected: `dict['key']` raises KeyError if the key doesn't exist, while `dict.get('key')` returns None (or a default value you specify)

---

## If the Student Struggles

- **If getting KeyError**: Always demonstrate checking with `in` before accessing, or switch to using `.get()`
- **If confused about when to use which**: Use `in` when you need different logic for present/missing keys. Use `.get()` when you just want a default value.
