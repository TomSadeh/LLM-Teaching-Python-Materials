# Lesson: Games (While Loops & Random) - Part 1: While Loop Basics

> **Module**: module_4_games
> **Part**: 1 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Variables and input/output
- [ ] if/elif/else statements
- [ ] Lists and for loops
- [ ] Basic comparison operators

---

## Learning Objective

By the end of this part, the student will be able to:

- Use `while` loops for indefinite repetition (looping until a condition changes)

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `while` loop | Repeats as long as a condition is True (unlike `for` which repeats a set number of times) |
| Loop condition | The boolean expression that controls whether the loop continues or stops |
| Infinite loop | A loop that never stops because the condition is always True |

---

## Lesson Content

### Getting Started

Compare `while` to `for`:
- `for` loop: "Do this exactly N times"
- `while` loop: "Do this while something is true"

Simple countdown example:
```python
count = 5
while count > 0:
    print(count)
    count = count - 1
print("Blastoff!")
```

Key point: The condition is checked *before* each iteration. If it starts False, the loop body never runs.

### Example: Keep Asking

A common pattern is asking for input until valid:
```python
answer = ""
while answer != "yes":
    answer = input("Are you ready? ")
print("Let's go!")
```

### Watch For

- **Infinite loops**: Forgetting to update the variable that's in the condition
- **Off-by-one errors**: Loop runs one too many or too few times
- **Never entering the loop**: Condition is False from the start

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| (conceptual) | This phase focuses on understanding while loops before moving to games |

---

## Checkpoint

Ask: "What happens if the while condition is never False?"
Expected: The loop runs forever (infinite loop)

---

## If the Student Struggles

- **If creating infinite loops**: Add print statements to show what's happening each iteration
- **If confused about while vs for**: "for = known number of times; while = until something happens"

---

## Real-World Connection

> "Every game you play has a game loop running - Minecraft checks your inputs, updates the world, and redraws the screen many times per second, all in a while loop."

---

## Notes for the LLM Teacher

- This is foundational - ensure students understand while before adding random and games
- Use simple counting examples first before introducing game concepts
- Infinite loops can freeze the environment - teach Ctrl+C early
- Let students make the infinite loop mistake once so they understand why updating the condition matters
