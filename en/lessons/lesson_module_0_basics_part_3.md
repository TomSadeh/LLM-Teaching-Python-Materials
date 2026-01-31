# Lesson: Python Basics - Part 3: Math Operations

> **Module**: module_0_basics
> **Part**: 3 of 5
> **Difficulty**: 1
> **Duration**: 3-5 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Perform basic math operations (+, -, *, /)

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Integer | A whole number without decimals (42) |
| Operators | Symbols for math: `+` add, `-` subtract, `*` multiply, `/` divide |

---

## Lesson Content

### Building on Part 2

We can store numbers in variables. Now let's do math with them!

### New Material

Show basic math operations:
```python
print(2 + 3)   # Addition: 5
print(10 - 4)  # Subtraction: 6
print(3 * 5)   # Multiplication: 15
print(10 / 2)  # Division: 5.0
```

Combine with variables:
```python
age = 12
next_year = age + 1
print(next_year)  # 13
```

You can do math directly in print:
```python
print(5 + 3)  # 8
```

### Watch For

- **Trying to do math on strings**: `"5" + 3` causes an error
- **Using `x` for multiplication**: Python uses `*`, not `x`
- **Division always gives decimals**: `10 / 2` gives `5.0`, not `5`

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_03_math | Numeric calculations with operators |

---

## Checkpoint

Ask: "What's the difference between 5 and '5'?"
Expected: 5 is a number you can do math with, '5' is text

---

## If the Student Struggles

- **If confused about operators**: Write them out: `*` means multiply, `/` means divide
- **If trying to do math on strings**: Show the error and explain that `"5"` is text, not a number
