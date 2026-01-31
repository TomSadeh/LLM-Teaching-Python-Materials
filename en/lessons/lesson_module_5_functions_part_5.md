# Lesson: Functions - Part 5: Building with Functions

> **Module**: module_5_functions
> **Part**: 5 of 5
> **Difficulty**: 3
> **Duration**: 6-8 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Organize code into multiple functions that work together to build larger programs

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Helper functions | Small functions that do one specific task, used by other functions |
| Scope | Where a variable exists - local (inside function) or global (outside) |
| Function composition | Building complex behavior by combining simpler functions |

---

## Lesson Content

### Building on Parts 1-4

Now that we know how to define functions, add parameters, and return values, let's see how functions work together in real programs.

### Functions Calling Other Functions

```python
def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def draw_house(t):
    # The house uses the square function!
    draw_square(t, 100)  # Body
    t.forward(100)
    t.right(30)
    t.forward(80)        # Roof side 1
    t.right(120)
    t.forward(80)        # Roof side 2
```

The `draw_house` function uses `draw_square` - building complex behavior from simpler pieces!

### Breaking Down Problems

When facing a complex task, think about what smaller functions you need:

```python
# Task: Create a game score system

# Small, focused functions
def calculate_bonus(level):
    return level * 10

def calculate_penalty(mistakes):
    return mistakes * 5

def calculate_score(base_points, level, mistakes):
    bonus = calculate_bonus(level)
    penalty = calculate_penalty(mistakes)
    return base_points + bonus - penalty

# Use them together
final_score = calculate_score(100, 5, 2)
print(f"Your score: {final_score}")  # 100 + 50 - 10 = 140
```

### Understanding Scope

Variables inside functions are "local" - they only exist inside that function:

```python
def my_function():
    secret = "{{password}}"  # This only exists inside my_function
    print(secret)

my_function()
print(secret)  # Error! 'secret' is not defined outside the function
```

Think of functions as separate rooms - variables inside can't be seen from outside.

### A Complete Example

```python
# Text analysis tool

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    count = 0
    for char in text:
        if char in ".!?":
            count += 1
    return count

def analyze_text(text):
    word_count = count_words(text)
    sentence_count = count_sentences(text)

    if sentence_count > 0:
        avg_words = word_count / sentence_count
    else:
        avg_words = 0

    return {
        "words": word_count,
        "sentences": sentence_count,
        "average_words_per_sentence": avg_words
    }

# Use the main function
story = "{{hero}} went to {{school}}. It was amazing! The {{creature}} was there too."
results = analyze_text(story)
print(results)
```

### Watch For

- **Scope confusion**: Expecting variables from one function to be available in another
- **Not breaking down problems**: Writing one giant function instead of several small ones
- **Circular dependencies**: Function A calling B which calls A (can cause infinite loops)

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_3_helper_functions | Breaking tasks into multiple cooperating functions |
| exercise_7_text_tools | String manipulation utilities that work together |
| exercise_8_game_functions | Game logic organized into functions |
| exercise_9_turtle_scene | Integration project combining multiple drawing functions |

---

## Checkpoint

Ask: "Why would you use functions instead of just writing all the code in order?"
Expected: Reusability (write once, use many times), organization (easier to understand), easier to fix bugs (problems are isolated), easier to test (can test each function separately)

---

## If the Student Struggles

- **If scope issues**: Visualize functions as separate rooms - variables inside can't be seen from outside
- **If not seeing the benefit**: Have them modify a long program without functions vs with functions - they'll see functions are easier
- **If functions getting too complex**: Apply the "one function, one job" rule - if a function does too many things, split it
