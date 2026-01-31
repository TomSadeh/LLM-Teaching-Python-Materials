# Lesson: Lists - Part 3: Looping Through Lists

> **Module**: module_3_lists
> **Part**: 3 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Loop through a list using `for item in list` to process each item

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Iteration | Going through each item in a list one by one |
| for-in loop | A cleaner way to loop through lists than using range() |
| enumerate() | A way to get both the index and item when looping |

---

## Lesson Content

### Building on Part 2

You've learned to create, access, and modify lists. Now let's process every item in a list automatically using loops.

### The for-in Loop

This is the cleanest way to loop through a list:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

The variable `fruit` takes on each value in the list, one at a time.

### When You Need the Index Too

Use `enumerate()` to get both the position and the item:

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
```

### Building a New List from an Old One

```python
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(doubled)  # [2, 4, 6, 8, 10]
```

### Watch For

- **Modifying the list while looping**: This causes skipped items or errors; work with a copy instead
- **Using range(len(list)) unnecessarily**: `for item in list` is cleaner and more Pythonic

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_2_loop_list | Practice basic iteration through lists |

---

## Checkpoint

Ask: "Write a loop that prints each color in the list."
Expected: `for color in colors: print(color)`

---

## If the Student Struggles

- **If struggling with loops**: Trace through manually, writing out each value of the loop variable
- **If confused about the loop variable**: Explain that it's a temporary variable that changes each iteration
