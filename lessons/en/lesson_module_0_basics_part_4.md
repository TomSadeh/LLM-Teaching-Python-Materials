# Lesson: Python Basics - Part 4: User Input

> **Module**: module_0_basics
> **Part**: 4 of 5
> **Difficulty**: 2
> **Duration**: 3-5 minutes

---

## Prerequisites

### Concepts
- [ ] Variables and assignment
- [ ] Strings vs numbers
- [ ] Basic math operations

### Exercises Completed
- [ ] `output_prediction/exercise_2_arithmetic` (Part 3)
- [ ] `write_code/exercise_3_calculator` (Part 3)

---

## Learning Objective

- **Get user input with `input()` and use it in a program**

---

## Key Concepts

| Concept | Explanation |
|---------|-------------|
| `input()` | Function that waits for user to type, returns what they typed |
| Prompt | Text shown to user: `input("Enter name: ")` |
| String result | `input()` always returns a string, even if user types numbers |
| `int()` | Converts string to integer: `int("42")` becomes `42` |

---

## Lesson Flow

### Phase 1: OBSERVE
Show input in action.

Demonstrate live or use existing prediction exercise.

Key observations:
- Program pauses and waits for typing
- Whatever user types becomes the value
- `input()` result is always a string

### Phase 2: PRACTICE
Scaffolded input usage.

**Exercise**: `fill_blanks/exercise_2_input`

Student fills in prompts and variable names for input.

### Phase 3: CREATE
Interactive programs.

**Exercise**: `write_code/exercise_5_input`

Student creates program that asks for input and responds.

### Phase 4: DEBUG
Common input errors.

**Exercise**: `decode_error/exercise_2_input_errors`

Focus on: forgetting `int()`, type mismatches.

---

## Exercise Sequence

| Order | Exercise | Type | Phase |
|-------|----------|------|-------|
| 1 | (live demo or review) | Demo | OBSERVE |
| 2 | `fill_blanks/exercise_2_input` | Fill | PRACTICE |
| 3 | `write_code/exercise_5_input` | Write | CREATE |
| 4 | `decode_error/exercise_2_input_errors` | Decode | DEBUG |

---

## Checkpoint

**Ask**: Why do we need `int()` when adding numbers from input?

**Expected**: Because `input()` always gives us text (string), not a number. `int()` converts it.

---

## Common Mistakes

| Mistake | Example | Hint Strategy |
|---------|---------|---------------|
| Math on string input | `age = input(); age + 1` | What type does `input()` return? |
| Forgetting to store | `input("Name: ")` without `=` | Where does the answer go? |
| Empty prompt | `input()` with no message | How will user know what to type? |
| `int()` on non-number | `int("hello")` | What happens if user types letters? |

---

## If Student Struggles

| Signal | Response |
|--------|----------|
| TypeError on math | What type is the variable? Add `print(type(x))` to check |
| Program doesn't wait | Did you store the input in a variable? |
| Confused by int() | Two steps: 1) get text, 2) convert to number |

---

## Notes

- `input()` always returns string - this is the #1 gotcha
- Don't introduce `try/except` yet - keep it simple
- If user enters non-number for `int()`, program crashes - that's okay for now

---

## References

- [common-struggles.md](../../references/pedagogy/common-struggles.md) - Variable Confusion (types)
