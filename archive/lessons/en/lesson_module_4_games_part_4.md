# Lesson: Games (While Loops & Random) - Part 4: Game State and Scoring

> **Module**: module_4_games
> **Part**: 4 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Track game state using variables (score, attempts, lives)

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| State variable | A variable that tracks something across multiple iterations (like score or attempts) |
| Attempt counter | Counting how many tries the player has used |
| Score system | Awarding points based on performance |

---

## Lesson Content

### Building on Part 3

Our guessing game works, but there's no scoring! Let's add state tracking to make it more engaging.

### New Material

Adding an attempt counter:
```python
import random

secret = random.randint(1, 10)
attempts = 0  # Track how many guesses

while True:
    guess = int(input("Guess (1-10): "))
    attempts = attempts + 1

    if guess == secret:
        print(f"Correct! It took you {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
```

Limiting guesses (adding difficulty):
```python
import random

secret = random.randint(1, 10)
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    guess = int(input("Guess: "))
    attempts = attempts + 1

    if guess == secret:
        print("You win!")
        break
    else:
        remaining = max_attempts - attempts
        print(f"Wrong! {remaining} guesses left.")

if guess != secret:
    print(f"Game over! The number was {secret}")
```

### Watch For

- **Resetting score inside the loop**: State variables should be initialized BEFORE the loop
- **Forgetting to increment**: `attempts = attempts + 1` must be inside the loop
- **Off-by-one in limit**: Use `<` vs `<=` correctly for the right number of attempts

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_7_trivia | Quiz game with scoring, lists, and conditionals |

---

## Checkpoint

Ask: "Where should you initialize a score variable - before the loop or inside it?"
Expected: Before the loop (so it doesn't reset to 0 each iteration)

---

## If the Student Struggles

- **If score keeps resetting**: Check that `score = 0` is before the while loop, not inside it
- **If attempts count is wrong**: Add a print statement to show the count each iteration to debug
- **If game ends too early/late**: Check the loop condition and when you increment the counter
