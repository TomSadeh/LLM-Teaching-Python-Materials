# Lesson: Using Modules - Part 5: The JSON Module

> **Module**: module_8_modules
> **Part**: 5 of 6
> **Difficulty**: 3
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Use the json module to save and load data

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| JSON | A text format for storing data (JavaScript Object Notation) |
| `json.dumps(data)` | Converts Python data to a JSON string ("dump string") |
| `json.loads(string)` | Converts a JSON string back to Python data ("load string") |
| `json.dump(data, file)` | Writes Python data to a file as JSON |
| `json.load(file)` | Reads JSON from a file into Python data |

---

## Lesson Content

### Building on Part 4

We've learned math - now let's learn something very practical: saving data! The json module lets us save Python data (dictionaries, lists) to files.

### Converting to/from JSON Strings

```python
import json

# Python dictionary
character = {
    "name": "{{hero}}",
    "level": 5,
    "spells": ["{{spell1}}", "{{spell2}}"]
}

# Convert to JSON string
json_string = json.dumps(character)
print(json_string)  # {"name": "{{hero}}", "level": 5, "spells": [...]}

# Convert back to Python
data = json.loads(json_string)
print(data["name"])  # {{hero}}
```

### Saving to a File

```python
import json

game_state = {
    "player": "{{hero}}",
    "score": 100,
    "items": ["{{item}}", "potion"]
}

# Save to file
with open("save_game.json", "w") as file:
    json.dump(game_state, file)
```

### Loading from a File

```python
import json

# Load from file
with open("save_game.json", "r") as file:
    loaded_data = json.load(file)

print(f"Welcome back, {loaded_data['player']}!")
print(f"Your score: {loaded_data['score']}")
```

### Memory Trick: s = string

- `dumps` / `loads` = work with **s**trings
- `dump` / `load` = work with files (no s)

### Watch For

- Confusing `dump`/`dumps` and `load`/`loads`
- File handling basics: using `with open()` and correct mode ("w" for write, "r" for read)

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_4_json_save | Save data to a JSON file |
| exercise_5_json_load | Load data from a JSON file |

---

## Checkpoint

Ask: "What module would you use to save a dictionary to a file?"
Expected: json

---

## If the Student Struggles

- **If JSON is confusing**: Start with `json.dumps()` (to string) to see the output, before file operations
- **If file handling is unclear**: Focus on the `with open()` pattern - it handles opening and closing automatically
