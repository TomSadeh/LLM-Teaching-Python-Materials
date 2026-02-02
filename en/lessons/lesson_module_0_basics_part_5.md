# Lesson: Python Basics - Part 5: Putting It Together

> **Module**: module_0_basics
> **Part**: 5 of 5
> **Difficulty**: 2
> **Duration**: 5-7 minutes

---

## Prerequisites

### Concepts
- [ ] `print()` and strings
- [ ] Variables and assignment
- [ ] Math operations
- [ ] `input()` and `int()`

### Exercises Completed
- [ ] `fill_blanks/exercise_2_input` (Part 4)
- [ ] `write_code/exercise_5_input` (Part 4)

---

## Learning Objective

- **Combine variables, input, and output using f-strings**

---

## Key Concepts

| Concept | Explanation |
|---------|-------------|
| f-string | Format string: `f"Hello, {name}!"` - variables inside `{}` |
| Concatenation | Joining strings with `+`: `"Hello, " + name` |
| String formatting | Making output readable and combined |

---

## Lesson Flow

### Phase 1: OBSERVE
Show different ways to combine text and variables.

**Exercise**: `match_output/exercise_1_string_output`

Key observations:
- `+` requires all strings (must convert numbers)
- Comma in `print()` adds spaces automatically
- f-strings are cleanest: `f"Value: {x}"`

### Phase 2: PRACTICE
Complete a formatting function.

**Exercise**: `complete_function/exercise_1_format_output`

Student completes f-string formatting in function context.

### Phase 3: CREATE
Build complete programs.

**Exercises**:
- `write_code/exercise_4_strings`
- `write_code/exercise_6_fstrings`

Student creates programs combining all Module 0 skills.

### Phase 4: DEBUG
Find bugs across all basics.

**Exercise**: `bug_hunt/exercise_1_basics_bugs`

Comprehensive debugging covering print, variables, math, input, strings.

---

## Exercise Sequence

| Order | Exercise | Type | Phase |
|-------|----------|------|-------|
| 1 | `match_output/exercise_1_string_output` | Match | OBSERVE |
| 2 | `complete_function/exercise_1_format_output` | Complete | PRACTICE |
| 3 | `write_code/exercise_4_strings` | Write | CREATE |
| 4 | `write_code/exercise_6_fstrings` | Write | CREATE |
| 5 | `bug_hunt/exercise_1_basics_bugs` | Hunt | DEBUG |

### Module Capstone
**Hybrid**: `hybrid/exercise_2_apprentice_program`

Complete character creator program using all Module 0 concepts.

---

## Checkpoint

**Ask**: What are three ways to print a variable's value with text around it?

**Expected**:
1. Comma: `print("Score:", score)`
2. Concatenation: `print("Score: " + str(score))`
3. f-string: `print(f"Score: {score}")`

---

## Common Mistakes

| Mistake | Example | Hint Strategy |
|---------|---------|---------------|
| Missing `f` prefix | `"Hello {name}"` | What makes a string an f-string? |
| Wrong braces | `f"Hello, (name)"` | What brackets go around variables in f-strings? |
| Concat number | `"Score: " + score` | Can you add text and number directly? |
| Quotes inside f-string | `f"Say "hi""` | Use different quote types inside and outside |

---

## If Student Struggles

| Signal | Response |
|--------|----------|
| f-string syntax | Start simple: `f"{name}"` then add text around it |
| TypeError on concat | Use `str()` to convert, or switch to f-string |
| Overwhelmed | Pick one method (f-strings) and stick with it |

---

## Module Wrap-up

After completing Part 5 and the capstone hybrid:

**Skills acquired**:
- Display output with `print()`
- Store values in variables
- Perform math calculations
- Get user input
- Format strings with f-strings

**Ready for**: Module 1 (Turtle graphics and loops)

---

## References

- [learning-science.md](../../references/pedagogy/learning-science.md) - Transfer of Learning
- [common-struggles.md](../../references/pedagogy/common-struggles.md) - Debugging Mindset
