# Lesson: Lists - Part 2: Modifying Lists

> **Module**: module_3_lists
> **Part**: 2 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Modify, add, and remove items from a list using assignment, `append()`, and `remove()`

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `append()` | Adds an item to the end of a list |
| `remove()` | Removes the first occurrence of a specific item from a list |
| Mutable | Lists can be changed after they are created |

---

## Lesson Content

### Building on Part 1

Now that you can create lists and access items, let's learn how to change them. Lists are mutable, meaning you can modify them after creation.

### Changing an Item

Use the index to replace an item:

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Replace "banana"
print(fruits)  # ["apple", "blueberry", "cherry"]
```

### Adding Items with append()

The `append()` method adds an item to the end:

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]

fruits.append("date")
print(fruits)  # ["apple", "banana", "cherry", "date"]
```

### Removing Items with remove()

The `remove()` method removes the first matching item:

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # ["apple", "cherry"]
```

### Watch For

- **Trying to access removed items**: After removing, indices shift down
- **Syntax errors with append**: It's `fruits.append("item")`, not `fruits.append = "item"`
- **remove() on missing item**: Causes an error if the item isn't in the list

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_4_todo_list | Build a practical todo list with append, remove, and display |

---

## Checkpoint

Ask: "How do you add 'purple' to the end of the colors list?"
Expected: `colors.append('purple')`

---

## If the Student Struggles

- **If struggling with methods**: Emphasize the dot syntax - the list "knows" how to append to itself
- **If confused about append vs assignment**: Show that `fruits[0] = x` changes existing, `fruits.append(x)` adds new
