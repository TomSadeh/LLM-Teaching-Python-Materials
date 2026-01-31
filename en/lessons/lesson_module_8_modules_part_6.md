# Lesson: Using Modules - Part 6: Exploring Modules

> **Module**: module_8_modules
> **Part**: 6 of 6
> **Difficulty**: 3
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Explore new modules using `dir()`, `help()`, and documentation

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `dir(module)` | Lists all names (functions, variables) available in a module |
| `help(module.function)` | Shows documentation for a specific function |
| Documentation | Official guides at docs.python.org for all standard library modules |

---

## Lesson Content

### Building on Part 5

You've now learned several modules. But Python has hundreds more! Let's learn how to explore and discover new modules on your own.

### Using dir() to See What's Available

```python
import string

# See everything in the string module
print(dir(string))
# ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'digits', ...]

# Useful constants in string module
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)         # 0123456789
```

### Using help() for Details

```python
import random

# Get help on a specific function
help(random.choice)
# Shows: choice(seq) - Return a random element from the non-empty sequence seq.
```

### Reading Documentation

The official Python documentation at **docs.python.org** has detailed information about every module:
- What functions are available
- What arguments they take
- Examples of how to use them

### Exploring a New Module: string

```python
import string
import random

# Create a random password using string module constants
letters = string.ascii_letters  # All letters
digits = string.digits          # All numbers
all_chars = letters + digits

password = ""
for i in range(8):
    password += random.choice(all_chars)
print(f"Generated password: {password}")
```

### Watch For

- Information overload from `dir()` - many items start with `_` and are internal
- Filter out internal items: `[x for x in dir(module) if not x.startswith('_')]`

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_6_string_utils | Use the string module for text processing |
| exercise_8_random_generator | Advanced random - create passwords and tokens |
| exercise_9_mini_project | Integration project using multiple modules together |

---

## Checkpoint

Ask: "How would you find out what functions are in a module you've never used before?"
Expected: `dir(module)`, documentation, or `help(module)`

---

## If the Student Struggles

- **If overwhelmed by dir() output**: Focus on items that don't start with underscore, and look for names that sound useful
- **If help() output is confusing**: Just read the first line - it usually gives a simple summary
- **If unsure how to explore**: Start with a specific goal ("I want to generate a random password") and search for relevant functions
