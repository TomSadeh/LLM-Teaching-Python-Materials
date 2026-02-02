# Lesson: Python Basics - Part 2: Variables

> **Module**: module_0_basics
> **Part**: 2 of 5
> **Difficulty**: 1
> **Duration**: 3-5 minutes

---

## Prerequisites

### Concepts
- [ ] `print()` function
- [ ] Strings (text in quotes)

### Exercises Completed
- [ ] `output_prediction/exercise_1_print_basics` (Part 1)
- [ ] `write_code/exercise_1_hello` (Part 1)

---

## Learning Objective

- **Create variables to store and reuse values**

---

## Key Concepts

| Concept | Explanation |
|---------|-------------|
| Variable | Named container that stores a value (labeled box analogy) |
| Assignment | Using `=` to put a value into a variable |
| Using variables | Write variable name without quotes to get its value |

---

## Lesson Flow

### Phase 1: OBSERVE
Show variable assignment and usage.

**Exercise**: `output_prediction/exercise_1_print_basics` (challenge_c touches variables)

Key observations:
- `name = "Maya"` creates a variable
- `print(name)` shows the value, not the word "name"
- `print("name")` shows the literal word "name"

### Phase 2: PRACTICE
Scaffolded variable creation.

**Exercise**: `fill_blanks/exercise_1_variables`

Student fills in assignment operators and variable names.

### Phase 3: CREATE
Independent variable usage.

**Exercise**: `write_code/exercise_2_variables`

Student creates their own variables and prints them.

### Phase 4: DEBUG
Spot common variable errors.

**Exercise**: `spot_difference/exercise_1_variable_errors`

---

## Exercise Sequence

| Order | Exercise | Type | Phase |
|-------|----------|------|-------|
| 1 | `output_prediction/exercise_1_print_basics` | Predict | OBSERVE |
| 2 | `fill_blanks/exercise_1_variables` | Fill | PRACTICE |
| 3 | `write_code/exercise_2_variables` | Write | CREATE |
| 4 | `spot_difference/exercise_1_variable_errors` | Spot | DEBUG |

### Capstone
**Hybrid**: `hybrid/exercise_1_apprentice_variables`

Assign after main exercises to consolidate variables + strings.

---

## Checkpoint

**Ask**: If I write `name = "Maya"`, what does `print(name)` show?

**Expected**: Maya (without quotes) - the value, not the variable name

---

## Common Mistakes

| Mistake | Example | Hint Strategy |
|---------|---------|---------------|
| Quotes around variable | `print("name")` | Do you want the word or what's inside the box? |
| Missing quotes on value | `name = Maya` | How does Python know Maya is text, not a variable? |
| Typo in variable name | `print(nmae)` | Check spelling - does it match exactly? |
| Case mismatch | `Name` vs `name` | Python sees these as different - which one did you create? |

---

## If Student Struggles

| Signal | Response |
|--------|----------|
| Confused about quotes | Side by side: `print(name)` vs `print("name")` - run both |
| Doesn't understand assignment | Use box analogy: `=` puts something in the box |
| Variable not defined error | Where did you create the variable? Is it spelled the same? |

---

## References

- [learning-science.md](../../references/pedagogy/learning-science.md) - Cognitive Load (one concept at a time)
- [common-struggles.md](../../references/pedagogy/common-struggles.md) - Variable Confusion
