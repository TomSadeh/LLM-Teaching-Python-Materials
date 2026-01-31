# Lesson: Dictionaries

> **Module**: module_7_dictionaries
> **Difficulty**: 2
> **Duration**: 25-30 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Variables and basic data types
- [ ] Lists and how to access items by index
- [ ] Loops (for and while)
- [ ] Functions (helpful but not required)

---

## Learning Objectives

By the end of this lesson, the student will be able to:

1. Create a dictionary with key-value pairs
2. Access, add, and modify values using keys
3. Loop through dictionary keys, values, or both
4. Use dictionaries to represent real-world data (characters, items, etc.)
5. Handle missing keys with `.get()` or conditionals

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Dictionary | A collection of key-value pairs, like a real dictionary (word → definition) |
| Key | The unique identifier used to look up a value (like a word) |
| Value | The data stored at a key (like a definition) |
| Key-value pair | A single entry: `"name": "Maya"` |
| `.get()` method | Safely retrieves a value, returning None (or a default) if key doesn't exist |

---

## Common Misconceptions

1. **Using indices instead of keys**: Trying `my_dict[0]` to get the first item
   **Reality**: Dictionaries use keys, not numeric positions

2. **KeyError panic**: Not knowing what to do when accessing a non-existent key
   **Reality**: Use `if key in dict:` or `.get()` to handle missing keys

3. **Mutable keys**: Trying to use a list as a dictionary key
   **Reality**: Keys must be immutable (strings, numbers, tuples - not lists)

4. **Order confusion**: Assuming dictionaries have no order
   **Reality**: Since Python 3.7, dictionaries maintain insertion order

---

## Teaching Sequence

### Phase 1: What's a dictionary?
- Contrast with lists: index (0,1,2) vs meaningful keys ("name", "age")
- Create a simple dictionary: `character = {"name": "{{hero}}", "age": 11}`
- Access values: `character["name"]`
- Watch for: using list syntax, forgetting quotes on string keys

### Phase 2: Modifying dictionaries
- Add new key-value pairs: `character["house"] = "{{house}}"`
- Change existing values: `character["age"] = 12`
- Remove pairs: `del character["age"]`
- Watch for: trying to "append" (that's for lists)

### Phase 3: Checking and safe access
- Check if key exists: `if "name" in character:`
- Safe access with `.get()`: `character.get("pet", "no pet")`
- Handle missing keys gracefully
- Watch for: forgetting the `in` check before access

### Phase 4: Looping through dictionaries
- Keys: `for key in character:`
- Values: `for value in character.values():`
- Both: `for key, value in character.items():`
- Watch for: trying to unpack in a regular for loop

### Phase 5: Real-world structures
- Character stats, inventory systems, simple databases
- Nested dictionaries (dictionary inside dictionary)
- When to use dict vs list
- Watch for: over-nesting, complexity

---

## Exercises Mapping

| Exercise | Concepts covered | Notes |
|----------|------------------|-------|
| exercise_1_spellbook | Basic dict creation | Key-value introduction |
| exercise_2_character_stats | Accessing/modifying values | RPG-style stats |
| exercise_3_inventory | Adding/removing items | Dynamic dictionaries |
| exercise_4_word_counter | Building dicts from data | Processing input |
| exercise_5_translator | Dictionary lookup | Practical application |
| exercise_6_contact_book | Multiple entries | Mini database |
| exercise_7_nested_data | Nested dictionaries | Complex structures |
| exercise_8_game_state | State management | Game save data |
| exercise_9_quiz_data | Combining concepts | Full application |

---

## Checkpoints

### After Phase 1 (creation/access)
Ask: "If I have `pet = {'name': 'Fluffy', 'type': 'cat'}`, how do I get 'Fluffy'?"
Expected: `pet['name']` or `pet.get('name')`

### After Phase 2 (modifying)
Ask: "How do I add a new key 'color' with value 'orange' to the pet dictionary?"
Expected: `pet['color'] = 'orange'`

### After Phase 4 (looping)
Ask: "How do I print both the keys and values of a dictionary?"
Expected: `for key, value in dict.items():` then print them

### End of Lesson
Ask: "When would you use a dictionary instead of a list?"
Expected: When you want to look up data by a name/key rather than by position

---

## If the Student Struggles

- **If confused about keys vs indices**: Use a real dictionary analogy - you look up words, not page numbers
- **If getting KeyError**: Always demonstrate checking with `in` before accessing
- **If confused about .items()**: Show the output of `.items()` - it's a list of tuples
- **If unsure when to use dicts**: Ask "Do you care about order, or do you want to look things up by name?"

---

## Extension Ideas

For students who finish early or want more challenge:

- Build a simple phone book with add/remove/search
- Create a character creation wizard that stores choices in a dict
- Make a translation dictionary between two languages

---

## Real-World Connection

> "Every user profile on any website is a dictionary - your username, email, profile picture, and settings are all stored as key-value pairs."

---

## Notes for the LLM Teacher

- Dictionaries feel very different from lists - take time with the mental model shift
- The real dictionary analogy (word → definition) is very effective
- RPG character stats make an excellent, engaging example context
- Emphasize when to use dicts vs lists - this is a design decision students will make often
- Nested dicts can be confusing - only introduce if the student is comfortable with basic dicts
