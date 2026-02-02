# Lesson: Lists - Part 1: Creating and Accessing Lists

> **Module**: module_3_lists
> **Part**: 1 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Variables and basic data types
- [ ] `for` loops with `range()`
- [ ] `if/else` statements

---

## Learning Objective

By the end of this part, the student will be able to:

- Create a list with multiple items and access items by index (including negative indices)

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| List | An ordered collection of items stored in a single variable |
| Index | The position of an item in a list, starting at 0 |
| Negative Index | Counting from the end of the list, where -1 is the last item |

---

## Lesson Content

### Getting Started

A list is like a container that holds multiple items in order. Instead of creating separate variables for each item, you can store them all in one place.

```python
# Creating a list with square brackets
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = ["hello", 42, True]  # Lists can hold different types
```

### Accessing Items by Index

Each item has a position number called an index. Python starts counting from 0, not 1.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # "apple" - first item
print(fruits[1])  # "banana" - second item
print(fruits[2])  # "cherry" - third item
```

### Negative Indexing

Use negative numbers to count from the end:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])  # "cherry" - last item
print(fruits[-2])  # "banana" - second to last
```

### Watch For

- **Off-by-one errors**: Remember that index 0 is the first item, not index 1
- **Index out of range**: Accessing `fruits[3]` when the list only has 3 items (indices 0, 1, 2)

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_1_favorites | Create lists with familiar data and access items by index |

---

## Checkpoint

Ask: "If `colors = ['red', 'blue', 'green']`, what is `colors[1]`?"
Expected: "blue" (not "red")

---

## If the Student Struggles

- **If struggling with indexing**: Draw boxes with numbers underneath; use finger counting starting from 0
- **If getting index errors**: Add `print(len(list))` to show the actual size

---

## Real-World Connection

> "Spotify playlists, Instagram followers, and Minecraft inventories are all lists - collections of items stored in a specific order that you can access by position."

---

## Notes for the LLM Teacher

- Zero-based indexing is counterintuitive - use visual aids and repetition
- Have the student predict what index will give them before running code
- Negative indexing is a Python convenience that many find helpful once understood
