# Lesson: Lists - Part 4: List Operations

> **Module**: module_3_lists
> **Part**: 4 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Use `len()`, the `in` operator, and slicing to work with lists

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `len()` | Returns how many items are in a list |
| `in` operator | Checks if an item exists in a list (returns True or False) |
| Slicing | Extracts a portion of a list using `[start:end]` |

---

## Lesson Content

### Building on Part 3

Now that you can loop through lists, let's learn some powerful operations for checking and extracting data from lists.

### Getting the Length with len()

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # 3

# Useful for loops and conditions
if len(fruits) > 0:
    print("The list is not empty")
```

### Checking Membership with in

The `in` operator returns True or False:

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)   # True
print("mango" in fruits)    # False

# Commonly used with if statements
if "apple" in fruits:
    print("We have apples!")
```

### Slicing Lists

Get a portion of a list with `[start:end]`:

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])   # [1, 2, 3] - from index 1 up to (not including) 4
print(numbers[:3])    # [0, 1, 2] - from start to index 3
print(numbers[3:])    # [3, 4, 5] - from index 3 to end
print(numbers[-2:])   # [4, 5] - last 2 items
```

### Watch For

- **Confusing len() with last index**: If `len(fruits)` is 3, the last index is 2
- **Slice end is exclusive**: `[1:4]` gives indices 1, 2, 3 (not 4)

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_5_search | Practice using the `in` operator with conditions |

---

## Checkpoint

Ask: "How would you check if 'yellow' is in the colors list?"
Expected: `if 'yellow' in colors:` or `'yellow' in colors`

---

## If the Student Struggles

- **If struggling with len()**: Draw the list and count boxes, then show len() gives the same answer
- **If confused about slicing**: Think of it as "from this position up to but not including that position"
