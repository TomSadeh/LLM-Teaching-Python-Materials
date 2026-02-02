# Lesson: Using Modules

> **Module**: module_8_modules
> **Difficulty**: 3
> **Duration**: 30-35 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Functions - defining and calling
- [ ] Basic data types: strings, numbers, lists, dictionaries
- [ ] Control flow: loops and conditionals

---

## Learning Objectives

By the end of this lesson, the student will be able to:

1. Import built-in modules using `import` and `from ... import`
2. Use the `datetime` module to work with dates and times
3. Use the `math` module for advanced mathematical operations
4. Use the `json` module to save and load data
5. Explore new modules using `dir()` and documentation

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

## Common Misconceptions

1. **Forgetting to import**: Trying to use a module function without importing first
   **Reality**: Must import at the top of the file before using

2. **Import syntax confusion**: Mixing up `import X` vs `from X import Y`
   **Reality**: `import X` → use `X.function()`, `from X import Y` → use `Y()` directly

3. **Thinking modules need installation**: Assuming all modules need pip install
   **Reality**: Standard library modules are already available

4. **Reusing module names**: Creating a file called `random.py` and breaking imports
   **Reality**: Don't name your files after built-in modules

---

## Teaching Sequence

### Phase 1: What are modules?
- Explain: pre-written code you can use in your programs
- Compare to importing functions like borrowing tools
- Show the two import styles and when to use each
- Watch for: putting import statements in the middle of code

### Phase 2: The random module (review)
- They've seen this before - quick review
- `random.randint()`, `random.choice()`, `random.shuffle()`
- Good warm-up before new modules
- Watch for: confidence check before moving on

### Phase 3: The datetime module
- `datetime.datetime.now()` - current date and time
- Formatting dates with `.strftime()`
- Calculating time differences
- Watch for: the double datetime (datetime.datetime)

### Phase 4: The math module
- `math.sqrt()`, `math.pow()`, `math.floor()`, `math.ceil()`
- Constants: `math.pi`, `math.e`
- When to use math vs built-in operators
- Watch for: confusing with basic operators

### Phase 5: The json module
- Saving data: `json.dump()` and `json.dumps()`
- Loading data: `json.load()` and `json.loads()`
- Practical use: saving game state, configuration
- Watch for: file handling basics (open, close)

### Phase 6: Exploring modules
- `dir(module)` - see what's available
- Getting help: `help(module.function)`
- Reading documentation
- Watch for: information overload

---

## Exercises Mapping

| Exercise | Concepts covered | Notes |
|----------|------------------|-------|
| exercise_1_datetime | Current time, formatting | Practical date handling |
| exercise_2_random_review | random module recap | Confidence builder |
| exercise_3_math_tools | math functions | Calculator extensions |
| exercise_4_json_save | Saving data to file | Data persistence |
| exercise_5_json_load | Loading data from file | Data retrieval |
| exercise_6_string_utils | String module | Text processing |
| exercise_7_time_calculator | datetime arithmetic | Time differences |
| exercise_8_random_generator | Advanced random | Passwords, tokens |
| exercise_9_mini_project | Multiple modules | Integration |

---

## Checkpoints

### After Phase 1 (imports)
Ask: "What's the difference between `import math` and `from math import sqrt`?"
Expected: With `import math` you use `math.sqrt()`, with `from` you use `sqrt()` directly

### After Phase 3 (datetime)
Ask: "How do you get the current date and time?"
Expected: `datetime.datetime.now()` or `from datetime import datetime` then `datetime.now()`

### After Phase 5 (json)
Ask: "What module would you use to save a dictionary to a file?"
Expected: json

### End of Lesson
Ask: "How would you find out what functions are in a module?"
Expected: `dir(module)`, documentation, or `help(module)`

---

## If the Student Struggles

- **If confused about import styles**: Stick with `import X` and always use `X.function()` for consistency
- **If overwhelmed by options**: Focus on one module at a time, master it, then move on
- **If JSON is confusing**: Start with `json.dumps()` (to string) before file operations
- **If datetime is complex**: Use `datetime.date.today()` for simpler date-only operations first

---

## Extension Ideas

For students who finish early or want more challenge:

- Build a countdown timer to a future date
- Create a password generator using multiple modules
- Make a simple data logger that saves timestamped entries to JSON

---

## Real-World Connection

> "Every real application uses modules - websites use datetime for timestamps, games use random for enemy spawning, and apps use json to save your settings and progress."

---

## Notes for the LLM Teacher

- Modules are where Python's power really shows - emphasize the "standing on shoulders of giants" aspect
- Don't try to cover too many modules - depth over breadth
- The json module is particularly practical for saving game state - students often love this
- Encourage exploration with `dir()` - learning to explore is a meta-skill
- If time is short, prioritize datetime and json over math (they've seen random already)
