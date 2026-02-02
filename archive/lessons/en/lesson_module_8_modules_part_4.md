# Lesson: Using Modules - Part 4: The Math Module

> **Module**: module_8_modules
> **Part**: 4 of 6
> **Difficulty**: 3
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Use the math module for advanced mathematical operations

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `math.sqrt(x)` | Returns the square root of x |
| `math.pow(x, y)` | Returns x raised to the power y |
| `math.floor(x)` | Rounds down to the nearest integer |
| `math.ceil(x)` | Rounds up to the nearest integer |
| `math.pi` | The mathematical constant pi (3.14159...) |

---

## Lesson Content

### Building on Part 3

We've learned datetime - now let's explore math. The math module provides mathematical functions beyond basic operators.

### Common Math Functions

```python
import math

# Square root
print(math.sqrt(16))    # 4.0
print(math.sqrt(2))     # 1.4142...

# Powers (alternative to **)
print(math.pow(2, 3))   # 8.0

# Rounding
print(math.floor(3.7))  # 3 (always rounds down)
print(math.ceil(3.2))   # 4 (always rounds up)
print(round(3.5))       # 4 (built-in, rounds to nearest)
```

### Mathematical Constants

```python
import math

print(math.pi)   # 3.141592653589793
print(math.e)    # 2.718281828459045

# Calculate circle area
radius = 5
area = math.pi * radius ** 2
```

### When to Use math vs Built-in Operators

| Operation | Built-in | math module |
|-----------|----------|-------------|
| Power | `2 ** 3` | `math.pow(2, 3)` |
| Absolute value | `abs(-5)` | `math.fabs(-5)` |
| Square root | `x ** 0.5` | `math.sqrt(x)` |

Use math module for: clarity, special functions (sqrt, floor, ceil), constants (pi, e)

### Watch For

- Confusing `math.pow()` with the `**` operator (both work, but `**` is often simpler)
- Forgetting that floor/ceil return integers conceptually but float type in Python 2 (int in Python 3)

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_3_math_tools | Calculator extensions using math functions |

---

## Checkpoint

Ask: "What's the difference between `math.floor(3.9)` and `math.ceil(3.1)`?"
Expected: `floor(3.9)` returns 3 (rounds down), `ceil(3.1)` returns 4 (rounds up)

---

## If the Student Struggles

- **If confused about when to use math**: Focus on `sqrt`, `floor`, `ceil`, and `pi` - these are the most practical
- **If mixing up floor/ceil**: Floor = "down to the floor", Ceil = "up to the ceiling"
