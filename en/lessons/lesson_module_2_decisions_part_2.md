# Lesson: Decisions (if/elif/else) - Part 2: Adding else

> **Module**: module_2_decisions
> **Part**: 2 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Use `else` to provide an alternative when the condition is false

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `else` | Runs when the `if` condition is False - the "otherwise" |

---

## Lesson Content

### Building on Part 1
- In Part 1, we wrote code that runs only when a condition is True
- But what if we want something to happen when it's False?

### New Material
- Introduce the "otherwise" concept with `else`
- Show if-else as two paths: one or the other runs, never both

```python
password = input("Enter password: ")
if password == "{{password}}":
    print("Access granted!")
else:
    print("Access denied!")
```

### The Structure
1. The `if` statement with its condition and colon
2. Indented code for when True
3. The keyword `else` followed by a colon (no condition!)
4. Indented code for when False

### Watch For
- **Indentation of else at wrong level**: `else` must align with its `if`
- **Adding a condition to else**: `else` doesn't take a condition - it catches everything that wasn't True
- **Forgetting the colon after else**: Just like `if`, `else` needs a `:`

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_1_password | Extend the password checker to print "Access denied" when wrong |

---

## Checkpoint

Ask: "If the `if` condition is True, does the `else` block run?"
Expected: No, only one of them runs - either the if block or the else block

---

## If the Student Struggles

- **If confused about when else runs**: Draw two paths - "if password correct, go left; otherwise, go right"
- **If getting indentation errors**: Make sure else aligns with if, and both have their own indented blocks
