# Lesson: Python Basics - Part 3: Math Operations

> **Module**: module_0_basics
> **Part**: 3 of 5
> **Difficulty**: 1
> **Duration**: 3-5 minutes

---

## Prerequisites

### Concepts
- [ ] Variables and assignment
- [ ] `print()` function

### Exercises Completed
- [ ] `fill_blanks/exercise_1_variables` (Part 2)
- [ ] `write_code/exercise_2_variables` (Part 2)

---

## Learning Objective

- **Perform basic math operations and store results in variables**

---

## Key Concepts

| Concept | Explanation |
|---------|-------------|
| Integer | Whole number without quotes: `42` |
| Operators | `+` add, `-` subtract, `*` multiply, `/` divide |
| Expressions | Math that Python calculates: `10 + 5` becomes `15` |

---

## Lesson Flow

### Phase 1: OBSERVE
Show math in action.

**Exercise**: `output_prediction/exercise_2_arithmetic`

Key observations:
- Numbers don't need quotes
- Python calculates expressions before printing
- Results can be stored in variables

### Phase 2: PRACTICE
Order matters in programs.

**Exercise**: `code_ordering/exercise_1_program_flow`

Student arranges lines in correct sequence - must assign before use.

### Phase 3: CREATE
Build a calculator.

**Exercise**: `write_code/exercise_3_calculator`

Student creates variables with numbers, performs operations, prints results.

### Phase 4: DEBUG
Type errors with numbers and strings.

**Exercise**: `decode_error/exercise_1_string_errors` (covers string + number errors)

---

## Exercise Sequence

| Order | Exercise | Type | Phase |
|-------|----------|------|-------|
| 1 | `output_prediction/exercise_2_arithmetic` | Predict | OBSERVE |
| 2 | `code_ordering/exercise_1_program_flow` | Order | PRACTICE |
| 3 | `write_code/exercise_3_calculator` | Write | CREATE |
| 4 | `decode_error/exercise_1_string_errors` | Decode | DEBUG |

---

## Checkpoint

**Ask**: What's the difference between `"5"` and `5`?

**Expected**: `"5"` is text (string), `5` is a number (integer). You can do math with numbers but not with text.

---

## Common Mistakes

| Mistake | Example | Hint Strategy |
|---------|---------|---------------|
| Quotes around numbers | `age = "12"` then `age + 1` | Is 12 text or a number here? |
| Wrong operator | Using `x` instead of `*` | What symbol does Python use for multiply? |
| Integer division surprise | `5 / 2` gives `2.5` | Division always gives decimal in Python 3 |
| Order of operations | `2 + 3 * 4` | Does Python follow math rules? (yes - PEMDAS) |

---

## If Student Struggles

| Signal | Response |
|--------|----------|
| TypeError with + | Check what types you're adding - both numbers? |
| Confused by results | Break into steps: what's `3 * 4`? Now add 2 |
| Float confusion | `/` gives decimals, `//` gives whole numbers (mention briefly) |

---

## References

- [common-struggles.md](../../references/pedagogy/common-struggles.md) - Variable Confusion (types)
