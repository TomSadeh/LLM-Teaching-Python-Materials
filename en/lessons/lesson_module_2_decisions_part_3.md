# Lesson: Decisions (if/elif/else) - Part 3: Multiple Conditions with elif

> **Module**: module_2_decisions
> **Part**: 3 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Use `elif` to check multiple conditions in sequence

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `elif` | Short for "else if" - checks another condition if previous ones were False |

---

## Lesson Content

### Building on Part 2
- With if-else, we have two paths: True or False
- What if we need more than two options?

### New Material
- Build a grading system: A, B, C, D, F
- Show how `elif` checks in order and stops at first match

```python
score = int(input("Enter score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

### Why Order Matters
- `elif` checks conditions in order
- It stops at the first True condition
- If someone has 95: both `>= 90` and `>= 80` are True, but we only want "A"

### Multiple if vs elif
```python
# WRONG: Multiple if (all get checked)
if score >= 90:
    print("A")
if score >= 80:  # This also runs for score 95!
    print("B")

# CORRECT: elif (stops at first match)
if score >= 90:
    print("A")
elif score >= 80:  # This doesn't run for score 95
    print("B")
```

### Watch For
- **Wrong order of conditions**: Checking `>= 60` before `>= 90` would give everyone a D
- **Using multiple if instead of elif**: All `if` statements get checked; `elif` stops at first match

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_2_grades | Build a grade calculator with multiple elif |
| exercise_6_menu | Use elif for user menu selection |

---

## Checkpoint

Ask: "In a grade checker, why should we check for A (>=90) before B (>=80)?"
Expected: Because if someone has 95, both conditions are true, but we want the first match

---

## If the Student Struggles

- **If struggling with elif order**: Draw a flowchart showing the decision path
- **If using multiple if instead of elif**: Show side-by-side comparison of the output
