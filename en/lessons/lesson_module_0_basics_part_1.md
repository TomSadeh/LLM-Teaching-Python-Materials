# Lesson: Python Basics - Part 1: Hello World with print()

> **Module**: module_0_basics
> **Part**: 1 of 5
> **Difficulty**: 1
> **Duration**: 3-5 minutes

---

## Prerequisites

### Concepts
- [ ] None - first coding lesson

### Exercises Completed
- [ ] Part 0 conversation completed

---

## Learning Objective

- **Use `print()` to display text on the screen**

---

## Key Concepts

| Concept | Explanation |
|---------|-------------|
| `print()` | Function that displays text/values on screen |
| String | Text data, written in quotes (`"hello"` or `'hello'`) |
| Function call | Using parentheses to run a function: `print("Hi")` |

---

## Lesson Flow

### Phase 1: OBSERVE
Show simplest working code first.

**Exercise**: `output_prediction/exercise_1_print_basics`

Student predicts output, then runs to verify. Key observations:
- Text appears exactly as written
- Quotes define the text boundaries
- Each `print()` creates a new line

### Phase 2: PRACTICE
Not applicable for Part 1 - `print()` is simple enough to move directly to CREATE.

### Phase 3: CREATE
First independent code.

**Exercise**: `write_code/exercise_1_hello`

Student writes their own print statements. This is their first success moment.

### Phase 4: DEBUG (optional)
Introduce error reading early.

**Exercise**: `decode_error/exercise_1_syntax_errors` (if exists) or skip for Part 1

---

## Exercise Sequence

| Order | Exercise | Type | Phase |
|-------|----------|------|-------|
| 1 | `output_prediction/exercise_1_print_basics` | Predict | OBSERVE |
| 2 | `write_code/exercise_1_hello` | Write | CREATE |

---

## Checkpoint

**Ask**: What happens if you write `print(hello)` without quotes?

**Expected**: Python looks for a variable named `hello` and gives an error (NameError)

---

## Common Mistakes

| Mistake | Example | Hint Strategy |
|---------|---------|---------------|
| Missing quotes | `print(hello)` | What's different between text and a name Python should look up? |
| Mismatched quotes | `print("hello')` | Look at the beginning and end - do they match? |
| Missing parentheses | `print "hello"` | How do we tell Python to run a function? |
| Wrong parentheses | `print["hello"]` | What shape of brackets did we use in the example? |

---

## If Student Struggles

| Signal | Response |
|--------|----------|
| Forgets quotes | Compare `"Maya"` (text) vs `Maya` (variable name) |
| Confused by parentheses | Parentheses mean "do this action" |
| Typo in `print` | Check spelling letter by letter |

---

## Notes

- This is the first code - prioritize success over comprehension
- Run code after every small change to build experimental habit
- Keep examples trivial: `print("Hi")` is enough

---

## References

- [learning-science.md](../../references/pedagogy/learning-science.md) - Worked Examples Effect
- [common-struggles.md](../../references/pedagogy/common-struggles.md) - Syntax Errors
