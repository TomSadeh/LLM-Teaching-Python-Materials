# Lesson: Using Modules - Part 2: The Random Module (Review)

> **Module**: module_8_modules
> **Part**: 2 of 6
> **Difficulty**: 3
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Confidently use the random module functions they've seen before

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `random.randint(a, b)` | Returns a random integer between a and b (inclusive) |
| `random.choice(list)` | Returns a random item from a list |
| `random.shuffle(list)` | Randomly reorders items in a list (modifies the list directly) |

---

## Lesson Content

### Building on Part 1

Now that we understand import syntax, let's practice with a module students have seen before - the random module. This is a good warm-up before learning new modules.

### Review of Random Functions

```python
import random

# Random integer between 1 and 10
number = random.randint(1, 10)

# Random choice from a list
spells = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
chosen = random.choice(spells)

# Shuffle a list in place
cards = ["A", "2", "3", "4", "5"]
random.shuffle(cards)  # cards is now shuffled
```

### Quick Confidence Check

Before moving on, make sure the student can:
- Write an import statement
- Use the module.function() syntax
- Explain what each random function does

### Watch For

- Forgetting that `shuffle()` modifies the list directly and returns None
- Confusing `randint` (inclusive) with `range` (exclusive end)

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_2_random_review | Confidence builder - uses familiar random functions with import syntax |

---

## Checkpoint

Ask: "If you want to pick a random character from a list of heroes, which function would you use?"
Expected: `random.choice(heroes_list)`

---

## If the Student Struggles

- **If unsure about random functions**: Focus on `randint` and `choice` - these are the most commonly used
- **If struggling with syntax**: Write out the pattern: `import module` then `module.function(arguments)`
