# Lesson: Lists - Part 5: Practical Applications

> **Module**: module_3_lists
> **Part**: 5 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Apply list skills to build practical programs including random selection and list management

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `random.choice()` | Selects a random item from a list |
| Combined operations | Using multiple list skills together in one program |
| List management | Building applications that add, remove, and display list contents |

---

## Lesson Content

### Building on Parts 1-4

You now have all the building blocks: creating lists, accessing items, modifying lists, looping, and checking contents. Let's combine these skills into real programs.

### Random Selection from Lists

```python
import random

responses = ["Yes!", "No way", "Maybe", "Ask again later"]
answer = random.choice(responses)
print(answer)
```

### Combining Lists with Conditions

```python
scores = [85, 92, 78, 95, 88]
high_scores = []

for score in scores:
    if score >= 90:
        high_scores.append(score)

print(f"High scores: {high_scores}")  # [92, 95]
```

### Building an Interactive List App

```python
playlist = []

# Add songs
playlist.append("Song A")
playlist.append("Song B")
playlist.append("Song C")

# Display all
print("Your playlist:")
for i, song in enumerate(playlist):
    print(f"{i + 1}. {song}")

# Check and remove
if "Song B" in playlist:
    playlist.remove("Song B")
    print("Removed Song B")
```

### Watch For

- **Forgetting to import random**: Must have `import random` at the top
- **Empty list errors**: `random.choice([])` on an empty list causes an error

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_3_magic_8ball | Fun application using random.choice() |
| exercise_6_name_picker | Random selection from a list of names |
| exercise_7_playlist | Multiple list operations combined |
| exercise_8_high_scores | Sorting and comparing list items |
| exercise_9_inventory | Complex list management with nested operations |

---

## Checkpoint

Ask: "How would you pick a random item from a list called `options`?"
Expected: `random.choice(options)` (with `import random` at top)

---

## If the Student Struggles

- **If struggling with random**: Make sure they understand the import statement first
- **If overwhelmed by combining concepts**: Break the problem into smaller steps - first get the list working, then add the loop, then add conditions
