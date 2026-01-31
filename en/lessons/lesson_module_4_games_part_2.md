# Lesson: Games (While Loops & Random) - Part 2: Random Numbers

> **Module**: module_4_games
> **Part**: 2 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Generate random numbers using `random.randint()`

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `import random` | Loads the random module so we can use its functions |
| `random.randint(a, b)` | Returns a random integer between a and b, inclusive |

---

## Lesson Content

### Building on Part 1

Now that we know how to loop "until something happens," we need something unpredictable to happen. That's where random numbers come in - they make games exciting because you can't predict the outcome!

### New Material

First, we need to import the random module:
```python
import random
```

Then we can generate random numbers:
```python
import random

number = random.randint(1, 10)
print(number)  # Could be 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10
```

Key point: `randint` includes both endpoints! This is different from `range()`.

Run the same code multiple times - you'll get different results each time!

### Dice Example

```python
import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print(f"You rolled: {die1} and {die2}")
print(f"Total: {die1 + die2}")
```

### Watch For

- **Forgetting `import random`**: Must be at the top of the file
- **Wrong syntax**: It's `random.randint()`, not just `randint()`
- **Off-by-one thinking**: `randint(1, 10)` DOES include 10

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_3_dice | Simple dice rolling with random numbers and accumulating scores |

---

## Checkpoint

Ask: "What do you need at the top of your file to use random?"
Expected: `import random`

---

## If the Student Struggles

- **If not getting randomness**: Explain that `randint` is truly random - can't predict it
- **If confused about range vs randint**: `range(1, 10)` excludes 10, but `randint(1, 10)` includes it
- **If forgetting the import**: The error message will say "name 'random' is not defined" - this means you need to import it
