# Module 4: Simple Games

## What You'll Learn
- The game loop - keep playing until done
- `while` loops for repeating until a condition
- Combining everything: loops, if/else, lists, random
- Building complete games!

## Lessons

### Lesson 1: The while Loop
A `while` loop keeps going as long as something is true:

```python
lives = 3
while lives > 0:
    print("You have", lives, "lives left")
    lives = lives - 1
print("Game over!")
```

### Lesson 2: Game Loop Pattern
Most games follow this pattern:

```python
playing = True
while playing:
    # 1. Show something to the player
    # 2. Get player input
    # 3. Check what happened
    # 4. Maybe set playing = False to end
```

### Lesson 3: Breaking Out
Use `break` to exit a loop immediately:

```python
while True:
    answer = input("Continue? (y/n): ")
    if answer == "n":
        break
    print("Let's keep going!")
```

### Lesson 4: Keeping Score
Track points with a variable:

```python
score = 0
# player does something good
score = score + 10
print("Score:", score)
```

---

## Exercises
1. `exercise_1_guess_number.py` - Guess the number (with hints!)
2. `exercise_2_rock_paper_scissors.py` - Classic game vs computer
3. `exercise_3_dice_game.py` - Roll dice and try your luck
4. `exercise_4_your_game.py` - Create your own game!

## Tips
- Test your game by playing it yourself
- Think about what could go wrong (bad input, etc.)
- Add fun messages to make it more exciting!
