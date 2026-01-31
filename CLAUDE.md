# Claude Code Guidelines for LLM Teaching Python Materials

This repository contains Python exercises for teaching beginners. The exercises are consumed by Maya Chat, a teaching app with dynamic theming support.

## Core Principles

### 1. No Hardcoded Theme References

**Never use hardcoded book/character references.** Always use `{{placeholder}}` syntax that gets replaced at runtime.

```python
# WRONG - Hardcoded references
hero = "Harry Potter"
school = "Hogwarts"
spell = "Expecto Patronum"

# CORRECT - Use placeholders
hero = "{{hero}}"
school = "{{school}}"
spell = "{{spell3}}"
```

Available placeholders (see `theme_variables.json` for values):
- `{{hero}}`, `{{heroine}}` - Protagonists
- `{{friend}}`, `{{mentor}}`, `{{villain}}` - Supporting characters
- `{{school}}`, `{{house}}`, `{{group}}` - Institutions
- `{{location}}`, `{{place}}` - Settings
- `{{spell1}}` to `{{spell4}}` - Abilities (basic to advanced)
- `{{creature}}`, `{{pet}}`, `{{item}}` - Objects
- `{{exclamation}}`, `{{greeting}}`, `{{password}}` - Phrases

### 2. Teach Proper Python

**No shortcuts or corner-cutting.** We are teaching real programming skills.

- Use proper Python conventions (PEP 8)
- Explain trade-offs between different approaches when relevant
- Don't oversimplify to the point of teaching bad habits
- Use meaningful variable names, not single letters (except for conventional uses like `i` in loops)

```python
# WRONG - Oversimplified
x = input()
print(x*2)

# CORRECT - Proper teaching
user_input = input("Enter a number: ")
number = int(user_input)  # Explain: input() returns a string
result = number * 2
print(f"Double of {number} is {result}")
```

### 3. Progressive Complexity

Exercises within a module should build on each other:
- Start with the simplest form of a concept
- Each exercise introduces one new element
- Later exercises combine concepts from earlier ones
- Final exercises in a module are integrative projects

### 4. Explain Pros and Cons

When multiple approaches exist, guide students to understand why one might be preferred:

```python
# In comments, explain the trade-off:
# Method 1: Using a for loop (clear, explicit)
# Method 2: Using list comprehension (concise, Pythonic)
# For beginners, we start with for loops for clarity
```

## File Structure

### Module Naming
```
raw_exercises/
├── module_0_basics/          # Difficulty 1
├── module_1_turtle_loops/    # Difficulty 1
├── module_2_decisions/       # Difficulty 2
├── module_3_lists/           # Difficulty 2
├── module_4_games/           # Difficulty 2
├── module_5_functions/       # Difficulty 3
├── module_6_final_project/   # Difficulty 3
├── module_7_dictionaries/    # Difficulty 2
├── module_8_modules/         # Difficulty 3
└── module_9_oop/             # Difficulty 3
```

### Exercise File Naming
- Pattern: `exercise_N_descriptive_name.py`
- Use underscores, lowercase
- Number exercises sequentially within a module

### Exercise File Structure

```python
# Exercise N: Title Here
#
# Optional: Multi-line description of the concept being taught


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Clear instructions for what to do
    # Include hints when helpful
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Next task in progression
    pass


# Optional: Include a complete example for reference
class ExampleClass:
    """Example to study - shows the complete pattern"""
    pass


def main():
    print("=== Exercise A: Description ===")
    exercise_a()

    print("\n=== Exercise B: Description ===")
    exercise_b()


main()
```

## Writing Guidelines

### Exercise Comments

Use the ✏️ emoji to mark where students should write code:
```python
def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Instructions go here
    pass
```

### Hint Format
```python
# Hint: Use dictionary["key"] to access values
# Hint: Remember that range(5) gives 0,1,2,3,4
```

### Example Values
When providing example values, use placeholders:
```python
# Create a character like "{{hero}}" or "{{heroine}}"
# Use a spell like "{{spell1}}" or "{{spell2}}"
```

### Difficulty Progression

| Level | Concepts | Example Topics |
|-------|----------|----------------|
| 1 | Single concept, no nesting | print, variables, simple loops |
| 2 | Combining concepts, conditions | if/else, lists, while loops |
| 3 | Abstraction, design patterns | functions, modules, OOP |

## Regenerating JSON Files

After adding or modifying exercises:

```bash
python scripts/convert_exercises.py
```

This single command:
- Reads all `.py` files from `raw_exercises/module_*/`
- Writes `exercises.json` to each module directory
- Updates `manifest.json` with the module list
- Updates `version.json`

### Adding a New Module

1. Create the directory: `raw_exercises/module_N_topic/`
2. Update `scripts/convert_exercises.py`:
   - Add to `MODULE_TO_TOPIC`
   - Add to `MODULE_TO_DIFFICULTY`
   - Add to `MODULE_NAMES_HE`
   - Add Hebrew titles for exercises to `TITLE_HE_MAP`
3. Run `python scripts/convert_exercises.py`

## Manifest File

The `manifest.json` file lists all available modules for remote sync:

```json
{
  "version": "1.3.0",
  "modules": [
    "module_0_basics",
    "module_1_turtle_loops",
    ...
  ]
}
```

The sync system uses this to discover which modules to fetch. Each module listed must have a corresponding `raw_exercises/<module>/exercises.json` file.

## Quality Checklist

Before committing exercises:

- [ ] No hardcoded theme references (grep for character names)
- [ ] All exercises use `pass` placeholder
- [ ] Instructions use ✏️ marker
- [ ] `main()` function calls all exercises
- [ ] Hebrew translations added to `convert_exercises.py`
- [ ] Exercises progress in difficulty within module
- [ ] Code follows PEP 8 conventions
- [ ] Comments explain "why", not just "what"

## Anti-Patterns to Avoid

### Don't Over-Engineer
```python
# WRONG - Too much abstraction for a beginner exercise
class ExerciseValidator:
    def __init__(self, validator_func):
        self.validate = validator_func

# CORRECT - Direct and clear
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer
```

### Don't Hide Complexity
```python
# WRONG - Magic that hides what's happening
from our_helper import do_everything
do_everything()

# CORRECT - Show the steps
user_input = input("Enter text: ")
words = user_input.split()
count = len(words)
print(f"Word count: {count}")
```

### Don't Skip Error Handling When It Matters
```python
# For input validation, show proper handling:
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
```

### Don't Use Features Before Teaching Them
If a module is about lists, don't use list comprehensions before they're introduced. Build concepts incrementally.

## Theme Testing

To verify no hardcoded references exist:
```bash
python scripts/apply_theme_placeholders.py --raw --check
```

See `HANDOFF_THEME_PLACEHOLDERS.md` for the complete placeholder system documentation.
