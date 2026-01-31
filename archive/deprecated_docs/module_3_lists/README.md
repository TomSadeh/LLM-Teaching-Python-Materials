# Module 3: Lists - Collecting Things

## What You'll Learn
- Creating lists to store multiple items
- Getting items from a list
- Looping through lists
- Adding and removing items
- Picking random items (for games!)

## Lessons

### Lesson 1: Creating Lists
A list holds multiple items in order:

```python
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True]
```

### Lesson 2: Getting Items (Indexing)
Each item has a position number (starting from 0!):

```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # orange
```

### Lesson 3: Looping Through Lists
Use a for loop to go through each item:

```python
colors = ["red", "green", "blue"]
for color in colors:
    print(color)
```

### Lesson 4: Changing Lists
Add and remove items:

```python
pets = ["dog", "cat"]
pets.append("hamster")     # Add to end: ["dog", "cat", "hamster"]
pets.remove("cat")         # Remove item: ["dog", "hamster"]
print(len(pets))           # Length: 2
```

### Lesson 5: Random Choices
Pick random items from a list:

```python
import random

answers = ["Yes", "No", "Maybe"]
chosen = random.choice(answers)
print(chosen)
```

---

## Exercises
1. `exercise_1_favorites.py` - Make and print a list
2. `exercise_2_loop_list.py` - Loop through items
3. `exercise_3_magic_8ball.py` - Random answer generator
4. `exercise_4_madlibs.py` - Silly story generator!

## Tips
- Lists start counting at 0, not 1!
- `len(my_list)` gives you how many items
- `random.choice(my_list)` picks one randomly
