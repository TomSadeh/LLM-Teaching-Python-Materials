# Lesson: Object-Oriented Programming

> **Module**: module_9_oop
> **Difficulty**: 3
> **Duration**: 35-40 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Functions - defining, parameters, return values
- [ ] Dictionaries - key-value pairs
- [ ] All previous concepts: variables, loops, conditions

---

## Learning Objectives

By the end of this lesson, the student will be able to:

1. Define a class with `class` keyword
2. Create instances (objects) of a class
3. Use `__init__` to set up object attributes
4. Define methods that operate on object data
5. Understand the difference between a class and an instance

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Class | A blueprint/template for creating objects with shared structure |
| Object/Instance | A specific thing created from a class blueprint |
| `self` | The reference to the current object, used inside methods |
| `__init__` | Special method that runs when creating a new object (constructor) |
| Method | A function that belongs to a class and operates on object data |

---

## Common Misconceptions

1. **Forgetting self**: Leaving `self` out of method definitions
   **Reality**: Every method's first parameter must be `self`

2. **Class vs instance confusion**: Trying to use attributes on the class itself
   **Reality**: Must create an instance first, then access attributes on it

3. **Not calling __init__**: Writing `MyClass` instead of `MyClass()`
   **Reality**: Need parentheses to actually create an instance

4. **self.x vs x**: Using just `x` instead of `self.x` for attributes
   **Reality**: Without `self.`, Python looks for a local variable, not an attribute

---

## Teaching Sequence

### Phase 1: Why classes?
- Start with a dictionary representing a character
- Show the problem: functions that take the dict as parameter
- Introduce the idea: bundling data AND functions together
- Watch for: making the motivation clear before the syntax

### Phase 2: Creating a simple class
- Define a class with just attributes
- Create instances
- Access attributes with dot notation
- Watch for: missing parentheses when creating instances

### Phase 3: The __init__ method
- Set up attributes when object is created
- Parameters become `self.attribute`
- Different instances can have different values
- Watch for: not storing parameters as self.something

### Phase 4: Adding methods
- Methods are functions inside a class
- Always take `self` as first parameter
- Can access and modify `self.attribute`
- Watch for: forgetting self in method definition

### Phase 5: Putting it together
- A complete class with init and multiple methods
- Create multiple instances that interact
- Show how objects can store state that changes
- Watch for: confusing class-level vs instance-level

---

## Exercises Mapping

| Exercise | Concepts covered | Notes |
|----------|------------------|-------|
| exercise_1_first_class | Class definition, instances | Simplest possible class |
| exercise_2_init | __init__ method | Setting up objects |
| exercise_3_methods | Adding methods | Object behavior |
| exercise_4_character | Complete character class | RPG-style example |
| exercise_5_pet_sim | State changes | Interactive object |
| exercise_6_counter | Simple class with state | Practical example |
| exercise_7_bank_account | Multiple methods, validation | Real-world model |
| exercise_8_text_adventure | Objects interacting | Complex application |
| exercise_9_game_objects | Multiple classes | Full project |

---

## Checkpoints

### After Phase 2 (basic class)
Ask: "What's the difference between a class and an object?"
Expected: A class is the blueprint/template, an object is a specific instance made from it

### After Phase 3 (__init__)
Ask: "What is `__init__` for?"
Expected: It runs when you create a new object and sets up its initial values

### After Phase 4 (methods)
Ask: "Why do methods always have `self` as the first parameter?"
Expected: So the method knows which object it's working with

### End of Lesson
Ask: "When would you use a class instead of just a dictionary?"
Expected: When you want to bundle data with behavior/functions that operate on that data

---

## If the Student Struggles

- **If self is confusing**: Explain it as "this object right here" - like saying your own name
- **If class vs instance is unclear**: Use tangible examples - "Dog" is the class, "my dog Fluffy" is an instance
- **If __init__ is mysterious**: Call it "the setup function" that runs automatically
- **If forgetting syntax**: Provide a minimal template they can copy and modify

---

## Extension Ideas

For students who finish early or want more challenge:

- Create a simple text-based game with Player and Enemy classes
- Build a virtual pet that has needs (hunger, happiness) that change over time
- Make a Card class and build a simple card game

---

## Real-World Connection

> "In Minecraft, every entity - players, zombies, pigs - is an object made from a class. They all have health and position (attributes) and can move and take damage (methods). OOP is how games organize thousands of entities."

---

## Notes for the LLM Teacher

- OOP is a big conceptual leap - be patient and use lots of analogies
- Start with the "why" before the "how" - classes solve real problems
- The character/RPG context works well since students understand stats and actions
- Don't introduce inheritance in the first lesson - focus on the basics
- `self` is the hardest concept - use it consistently and explain every time at first
- If students are comfortable, you can mention that methods are just functions with self, and attributes are just variables attached to an object
- Consider not using the term "constructor" - just call it "the init method"
