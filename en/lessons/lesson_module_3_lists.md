# Lesson: Lists

> **Module**: module_3_lists
> **Difficulty**: 2
> **Duration**: 25-30 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Variables and basic data types
- [ ] `for` loops with `range()`
- [ ] `if/else` statements

---

## Learning Objectives

By the end of this lesson, the student will be able to:

1. Create a list with multiple items
2. Access items by index (including negative indices)
3. Modify, add, and remove items from a list
4. Loop through a list using `for item in list`
5. Use common list methods: `append()`, `remove()`, `len()`

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| List | An ordered collection of items stored in a single variable |
| Index | The position of an item in a list, starting at 0 |
| `append()` | Adds an item to the end of a list |
| `len()` | Returns how many items are in a list |
| Iteration | Going through each item in a list one by one |

---

## Common Misconceptions

1. **Indexing starts at 1**: Trying to access the first item with `list[1]`
   **Reality**: Python lists start at index 0, so first item is `list[0]`

2. **Modifying while iterating**: Removing items from a list while looping through it
   **Reality**: This causes skipped items or errors; loop over a copy instead

3. **Confusing append() and extend()**: Using `append([1,2,3])` when they want to add 1, 2, 3 separately
   **Reality**: `append` adds one item (which could be a list); `extend` adds each item

4. **Thinking lists can only hold one type**: Believing all items must be the same type
   **Reality**: Python lists can mix types, though it's often clearer not to

---

## Teaching Sequence

### Phase 1: Creating and accessing lists
- Create a simple list: `fruits = ["apple", "banana", "cherry"]`
- Access by index: `fruits[0]` → "apple"
- Introduce negative indexing: `fruits[-1]` → last item
- Watch for: off-by-one errors, index out of range

### Phase 2: Modifying lists
- Change an item: `fruits[1] = "blueberry"`
- Add with `append()`: `fruits.append("date")`
- Remove with `remove()`: `fruits.remove("apple")`
- Watch for: trying to access removed items, append syntax errors

### Phase 3: Looping through lists
- `for fruit in fruits:` - cleaner than using range
- When you need the index too: `for i, fruit in enumerate(fruits):`
- Building a new list from an old one
- Watch for: modifying the list while looping

### Phase 4: List operations
- `len(fruits)` - how many items
- `"apple" in fruits` - checking membership
- Slicing basics: `fruits[1:3]`
- Watch for: confusing len() with last index

### Phase 5: Practical applications
- Todo list that grows and shrinks
- Random selection from a list
- Combining lists with conditions
- Watch for: forgetting to import random for choice()

---

## Exercises Mapping

| Exercise | Concepts covered | Notes |
|----------|------------------|-------|
| exercise_1_favorites | Creating lists, accessing items | Start with familiar data |
| exercise_2_loop_list | for-in loop | Basic iteration |
| exercise_3_magic_8ball | random.choice(), lists | Fun application |
| exercise_4_todo_list | append, remove, display | Practical project |
| exercise_5_search | `in` operator, conditions | Finding items |
| exercise_6_name_picker | random.choice, lists | Random selection |
| exercise_7_playlist | Multiple operations | Combined practice |
| exercise_8_high_scores | Sorting, comparing | Advanced list ops |
| exercise_9_inventory | Nested operations | Complex list management |

---

## Checkpoints

### After Phase 1 (creating/accessing)
Ask: "If `colors = ['red', 'blue', 'green']`, what is `colors[1]`?"
Expected: "blue" (not "red")

### After Phase 2 (modifying)
Ask: "How do you add 'purple' to the end of the colors list?"
Expected: `colors.append('purple')`

### After Phase 3 (looping)
Ask: "Write a loop that prints each color in the list."
Expected: `for color in colors: print(color)`

### End of Lesson
Ask: "How would you check if 'yellow' is in the colors list?"
Expected: `if 'yellow' in colors:` or `'yellow' in colors`

---

## If the Student Struggles

- **If struggling with indexing**: Draw boxes with numbers underneath; use finger counting from 0
- **If struggling with loops**: Trace through manually, writing out each value of the loop variable
- **If struggling with methods**: Emphasize the dot syntax - the list "knows" how to append to itself
- **If getting index errors**: Add `print(len(list))` to show the actual size

---

## Extension Ideas

For students who finish early or want more challenge:

- Build a simple shopping list app with add/remove/display
- Create a "name generator" that combines random first and last names from lists
- Implement a basic voting system that counts items

---

## Real-World Connection

> "Spotify playlists, Instagram followers, and Minecraft inventories are all lists - collections of items you can add to, remove from, and scroll through."

---

## Notes for the LLM Teacher

- Zero-based indexing is counterintuitive - use visual aids and repetition
- The `for item in list` pattern is more Pythonic than `for i in range(len(list))`
- Lists are mutable - this is important for understanding later concepts
- Random selection from lists is highly engaging - use it early for motivation
