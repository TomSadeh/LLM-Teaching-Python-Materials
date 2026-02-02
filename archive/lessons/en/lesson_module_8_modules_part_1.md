# Lesson: Using Modules - Part 1: What are Modules?

> **Module**: module_8_modules
> **Part**: 1 of 6
> **Difficulty**: 3
> **Duration**: 5-6 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Functions - defining and calling
- [ ] Basic data types: strings, numbers, lists, dictionaries
- [ ] Control flow: loops and conditionals

---

## Learning Objective

By the end of this part, the student will be able to:

- Import built-in modules using `import` and `from ... import` syntax

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Module | A file containing Python code (functions, variables) that can be imported |
| `import` | Brings a module into your program so you can use its contents |
| `from X import Y` | Imports only specific items from a module |
| Standard library | Modules that come built-in with Python (no installation needed) |
| Namespace | The "container" for a module's functions, accessed with `module.function()` |

---

## Lesson Content

### Getting Started

Explain that modules are pre-written code you can use in your programs - like borrowing tools from a toolbox instead of building them yourself.

Python comes with many built-in modules in its "standard library" - no installation needed!

### Two Ways to Import

**Method 1: Import the whole module**
```python
import math
result = math.sqrt(16)  # Use module_name.function()
```

**Method 2: Import specific items**
```python
from math import sqrt
result = sqrt(16)  # Use function directly
```

### When to Use Each Style

- Use `import module` when you need many things from a module, or want clarity about where functions come from
- Use `from module import item` when you only need one or two specific things

### Watch For

- Students putting import statements in the middle of code (imports should go at the top)
- Creating files with the same name as built-in modules (e.g., naming a file `random.py`)
- Forgetting to import before using a module function

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| (conceptual) | This part introduces syntax - practice comes with specific modules in following parts |

---

## Checkpoint

Ask: "What's the difference between `import math` and `from math import sqrt`?"
Expected: With `import math` you use `math.sqrt()`, with `from` you use `sqrt()` directly

---

## If the Student Struggles

- **If confused about import styles**: Stick with `import X` and always use `X.function()` for consistency - it's clearer where each function comes from

---

## Real-World Connection

> "Every real application uses modules - websites use datetime for timestamps, games use random for enemy spawning, and apps use json to save your settings and progress."

---

## Notes for the LLM Teacher

- This is the conceptual foundation - make sure students understand WHY we use modules before diving into specific ones
- The toolbox analogy works well: "Why build a hammer when you can borrow one?"
- Emphasize that standard library modules are already installed - common misconception that everything needs pip install
