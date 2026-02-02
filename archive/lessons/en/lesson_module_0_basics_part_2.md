# Lesson: Python Basics - Part 2: Variables

> **Module**: module_0_basics
> **Part**: 2 of 5
> **Difficulty**: 1
> **Duration**: 3-5 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Create variables to store text and numbers

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Variable | A named container that stores a value (like a labeled box) |
| Assignment | Using `=` to put a value into a variable |

---

## Lesson Content

### Building on Part 1

We learned how to print text directly. Now we'll store values so we can use them multiple times.

### New Material

Introduce the "labeled box" analogy - a variable is like a box with a name on it:

```python
name = "Maya"
print(name)
```

Key points:
- `name` is the variable (the box's label)
- `"Maya"` is the value (what's inside the box)
- `=` puts the value into the variable (assignment)

Show that when using a variable, we don't use quotes:
```python
name = "Maya"
print(name)    # Prints: Maya
print("name")  # Prints: name (the word, not the value!)
```

Variables can store numbers too:
```python
age = 12
print(age)
```

### Watch For

- **Quotes around variable names**: `print("name")` prints the word, not the value
- **Typos in variable names**: `print(nmae)` when the variable is `name`
- **Case sensitivity**: `Name` and `name` are different variables

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_02_variables | Introduces storing values in variables |

---

## Checkpoint

Ask: "If I write name = 'Maya', what does print(name) show?"
Expected: Maya (without quotes)

---

## If the Student Struggles

- **If confused about variables**: Use physical props analogy - sticky notes on boxes
- **If putting quotes around variables**: Show side by side: `print(name)` vs `print("name")`
