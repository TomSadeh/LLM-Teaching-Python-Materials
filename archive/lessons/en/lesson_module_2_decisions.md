# Lesson: Decisions (if/elif/else)

> **Module**: module_2_decisions
> **Difficulty**: 2
> **Duration**: 25-30 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Variables and basic data types (strings, integers)
- [ ] Using `input()` to get user data
- [ ] Basic comparison concepts (bigger, smaller, equal)

---

## Learning Objectives

By the end of this lesson, the student will be able to:

1. Write `if` statements to execute code conditionally
2. Use `else` to provide an alternative when the condition is false
3. Use `elif` to check multiple conditions in sequence
4. Combine conditions with `and`, `or`, and `not`
5. Nest conditional statements when needed

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `if` | Runs the indented code only when the condition is True |
| `else` | Runs when the `if` condition is False - the "otherwise" |
| `elif` | Short for "else if" - checks another condition if previous ones were False |
| Comparison operators | `==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=` |
| Boolean | A value that's either `True` or `False` |

---

## Common Misconceptions

1. **Using `=` instead of `==`**: Writing `if x = 5:` instead of `if x == 5:`
   **Reality**: `=` assigns values, `==` compares them

2. **Multiple `if` vs `elif`**: Using multiple `if` statements instead of `elif`
   **Reality**: Multiple `if`s all get checked; `elif` stops after first match

3. **Forgetting the colon**: Writing `if x == 5` without the `:`
   **Reality**: Python requires a colon after the condition

4. **Indentation after if**: Not indenting the code that should run conditionally
   **Reality**: Indentation tells Python what's "inside" the if block

---

## Teaching Sequence

### Phase 1: Simple if statement
- Start with the simplest case: `if condition:`
- Use a concrete example: checking if a password matches
- Show what happens when condition is True vs False
- Watch for: missing colon, no indentation, = vs ==

### Phase 2: Adding else
- Introduce the "otherwise" concept
- Show if-else as two paths: one or the other runs
- Watch for: indentation of else at wrong level

### Phase 3: Multiple conditions with elif
- Build a grading system: A, B, C, D, F
- Show how `elif` checks in order and stops at first match
- Compare to multiple `if` statements (all get checked)
- Watch for: wrong order of conditions (checking < 60 before < 70)

### Phase 4: Combining conditions
- `and`: both must be true
- `or`: at least one must be true
- `not`: flips True to False and vice versa
- Watch for: using English "and" instead of Python `and`

### Phase 5: Nested conditions
- An if inside another if
- When to nest vs when to use `and`
- Watch for: excessive nesting (usually can be simplified)

---

## Exercises Mapping

| Exercise | Concepts covered | Notes |
|----------|------------------|-------|
| exercise_1_password | Simple if-else | Classic "access granted/denied" |
| exercise_2_grades | elif chain | Multiple conditions in sequence |
| exercise_3_number_game | Comparison operators | Greater than, less than |
| exercise_4_quiz | Multiple if statements | Each question independent |
| exercise_5_age_checker | Compound conditions (and/or) | Age ranges |
| exercise_6_menu | elif for choices | User menu selection |
| exercise_7_calculator | elif + input | Combining with earlier concepts |
| exercise_8_adventure | Nested if | Branching story |
| exercise_9_validation | Multiple conditions | Input validation |

---

## Checkpoints

### After Phase 1 (if)
Ask: "What's the difference between `=` and `==`?"
Expected: `=` puts a value in a variable, `==` checks if two things are equal

### After Phase 2 (else)
Ask: "If the `if` condition is True, does the `else` block run?"
Expected: No, only one of them runs

### After Phase 3 (elif)
Ask: "In a grade checker, why should we check for A (≥90) before B (≥80)?"
Expected: Because if someone has 95, both conditions are true, but we want the first match

### End of Lesson
Ask: "How would you check if a number is between 10 and 20?"
Expected: `if number >= 10 and number <= 20:` or `if 10 <= number <= 20:`

---

## If the Student Struggles

- **If struggling with conditions**: Use real-world analogies - "if it's raining, take an umbrella"
- **If struggling with elif order**: Draw a flowchart showing the decision path
- **If struggling with and/or**: Use truth tables with simple examples
- **If getting unexpected results**: Add print statements to debug which branch runs

---

## Extension Ideas

For students who finish early or want more challenge:

- Build a simple text adventure with multiple decision points
- Create a "20 questions" style guessing game
- Make a chatbot that responds differently based on keywords

---

## Real-World Connection

> "Every app makes decisions constantly - Instagram decides whether to show you a notification, games decide if you won or lost, and websites check if your password is correct."

---

## Notes for the LLM Teacher

- The `= vs ==` confusion is very common - address it explicitly and multiple times
- Use interactive examples where students predict the output before running
- Build complexity gradually: if → if-else → if-elif-else → if-elif-elif-else
- Encourage students to trace through code manually before running it
