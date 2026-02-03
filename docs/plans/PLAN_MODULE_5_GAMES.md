# Plan: Module 5 - Games

Recreation plan for module_5_games using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_5_games |
| **Topic** | While loops, random module, game loops |
| **Prerequisites** | module_0_basics through module_4_functions |
| **Target Hybrid Ratio** | 45-55% |

### Learning Objectives

By the end of this module, students will be able to:

1. Use `while` loops for indefinite iteration
2. Write correct loop conditions to control when loops exit
3. Use `break` and `continue` for loop control
4. Import and use the `random` module (`randint`, `choice`, `random`)
5. Implement input validation loops (keep asking until valid)
6. Build game loops with win/lose/quit conditions
7. Combine all previous concepts into interactive programs
8. Handle user input robustly with error checking

### Curriculum Constraints

| Available Concepts | NOT Available (later modules) |
|--------------------|-------------------------------|
| **From Modules 0-4:** | |
| print(), variables, strings, numbers | dictionaries |
| input(), type conversion, f-strings | classes, methods |
| for loops, range() | file I/O |
| if/elif/else, comparisons, boolean ops | try/except (for type errors) |
| lists, indexing, slicing, list methods | |
| functions (def, parameters, return) | |
| **New in Module 5:** | |
| while loops | |
| break, continue | |
| import random | |
| random.randint(a, b) | |
| random.choice(sequence) | |
| random.random() | |
| Game loop patterns | |

**Note on error handling:** `add_error_handling` exercises should use while loops with if-statement validation, not try/except. Example: checking if input is a valid choice, not catching ValueError.

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types for Module 5 (see "module_4_games" section*) |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Exercise format standards |
| [common-struggles.md](../../references/pedagogy/common-struggles.md) | Loop mental models |

*Note: The exercise type mapping document uses different numbering. Our module_5_games corresponds to their "module_4_games" section.

---

## 2. Exercise Distribution

### Available Exercise Types (3 total)

| Category | Types |
|----------|-------|
| **Core** | write_code |
| **Improvement** | add_error_handling |
| **Debugging** | bug_hunt |

**Important:** Module 5 has the fewest exercise types (tied with Module 2). This is intentional - game development is highly creative and benefits from focused write_code practice with bug_hunt for debugging skills. The limited types actually work well because games are inherently engaging and provide their own feedback loops.

### Target Distribution

| Type | Count | Rationale |
|------|:-----:|-----------|
| write_code | 6 | Core practice for while loops and game logic |
| bug_hunt | 4 | Find common loop and game bugs |
| add_error_handling | 2 | Input validation is crucial for games |
| **hybrid** | 6 | Multi-part game projects (46% of total) |
| **TOTAL** | **18** | |

### Hybrid Ratio Calculation

- Total exercises: 18
- Hybrid exercises: 6
- Ratio: **33%** (below 45-55% target, but see rationale below)

**Rationale for lower hybrid ratio:** With only 3 exercise types available, achieving 45%+ hybrids while maintaining variety is challenging. However, each hybrid exercise in this module is a substantial mini-game project, making them more substantial than typical hybrids. The effective "weight" of practice is higher.

---

## 3. Exercise Inventory

### Concept Progression

Exercises are organized into concept clusters, progressing from simple to complex.

| Cluster | Concepts | Difficulty |
|---------|----------|:----------:|
| A | Basic while loops | 1-2 |
| B | Loop control (break, continue) | 2-3 |
| C | Random module basics | 2-3 |
| D | Input validation loops | 3 |
| E | Game loops | 3-4 |
| F | Complete games | 4-5 |

### Isolated Exercises

#### Cluster A: Basic While Loops (Difficulty 1-2)

| # | Type | Concept Focus |
|---|------|---------------|
| 1 | write_code | Write while loops with counter variables |
| 2 | bug_hunt | Find infinite loop bugs |

#### Cluster B: Loop Control (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 3 | write_code | Use break to exit loops early |
| 4 | write_code | Use continue to skip iterations |
| 5 | bug_hunt | Find break/continue placement bugs |

#### Cluster C: Random Module (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 6 | write_code | Use random.randint() and random.choice() |
| 7 | bug_hunt | Find random usage bugs (off-by-one in ranges) |

#### Cluster D: Input Validation (Difficulty 3)

| # | Type | Concept Focus |
|---|------|---------------|
| 8 | add_error_handling | Add validation loops for user input |
| 9 | write_code | Build robust input functions |

#### Cluster E: Game Loops (Difficulty 3-4)

| # | Type | Concept Focus |
|---|------|---------------|
| 10 | bug_hunt | Find game logic bugs |
| 11 | add_error_handling | Handle invalid game commands gracefully |

#### Cluster F: Complete Games (Difficulty 4-5)

| # | Type | Concept Focus |
|---|------|---------------|
| 12 | write_code | Build a complete simple game |

### Hybrid Exercises

#### Hybrid 1: The Rivalry - Loop Duel

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | bug_hunt | Fix broken loop code |
| 2 | GROWTH | write_code | Build better while loop |
| 3 | CONFRONTATION | write_code | Create a loop-based challenge |

**Placement:** After Cluster B (loop control)
**Difficulty:** 2-3
**Arc:** Rivalry

#### Hybrid 2: The Rescue - The Stuck Game

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | bug_hunt | Find why the game freezes (infinite loop) |
| 2 | INVESTIGATION | bug_hunt | Locate all the loop bugs |
| 3 | IMPROVEMENT | add_error_handling | Add input validation to prevent future issues |

**Placement:** After Cluster D (input validation)
**Difficulty:** 3
**Arc:** Rescue (adapted for available types)

#### Hybrid 3: The Rivalry - Number Guessing Game

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | bug_hunt | Fix a broken guessing game |
| 2 | GROWTH | write_code | Build core guessing logic |
| 3 | CONFRONTATION | write_code | Add hints (higher/lower) and guess counting |

**Placement:** After Cluster C (random module)
**Difficulty:** 3
**Arc:** Rivalry

#### Hybrid 4: The Rivalry - Rock Paper Scissors

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | bug_hunt | Fix buggy RPS logic |
| 2 | GROWTH | write_code | Build working RPS round |
| 3 | CONFRONTATION | write_code | Add play-again loop and score tracking |

**Placement:** After Cluster E (game loops)
**Difficulty:** 3-4
**Arc:** Rivalry

#### Hybrid 5: The Rescue - The Broken Adventure

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | SETBACK | bug_hunt | Find bugs in text adventure |
| 2 | INVESTIGATION | bug_hunt | Debug the navigation/command parsing |
| 3 | IMPROVEMENT | add_error_handling | Add robust command handling |
| 4 | GROWTH | write_code | Extend with new locations/features |

**Placement:** Cluster F (complete games)
**Difficulty:** 4-5
**Arc:** Rescue (extended)

#### Hybrid 6: Mini Project - Build Your Game

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Design and implement core game loop |
| 2 | GROWTH | write_code | Add win/lose conditions |
| 3 | IMPROVEMENT | add_error_handling | Make it crash-proof |
| 4 | GROWTH | write_code | Add features (score, replay, difficulty) |

**Placement:** End of module, as capstone
**Difficulty:** 5
**Arc:** Custom (Build -> Enhance -> Polish -> Extend)

---

## 4. Difficulty Progression Map

```
Difficulty:  1 -----> 2 -----> 3 -----> 4 -----> 5
             |       |        |        |        |
Exercises:   1       2,3,4    8,9      10,11    12
                     5,6,7    H2,H3    H4       H5,H6
                     H1
```

H1-H6 = Hybrid exercises

---

## 5. File Structure

```
exercises/
└── module_5_games/
    ├── write_code/
    │   ├── exercise_1_basic_while.py
    │   ├── exercise_2_break_loops.py
    │   ├── exercise_3_continue_loops.py
    │   ├── exercise_4_random_basics.py
    │   ├── exercise_5_input_functions.py
    │   └── exercise_6_simple_game.py
    ├── bug_hunt/
    │   ├── exercise_1_infinite_loops.py
    │   ├── exercise_2_break_continue.py
    │   ├── exercise_3_random_bugs.py
    │   └── exercise_4_game_logic.py
    ├── add_error_handling/
    │   ├── exercise_1_input_validation.py
    │   └── exercise_2_game_commands.py
    └── hybrid/
        ├── exercise_1_rivalry_loop_duel.py
        ├── exercise_2_rescue_stuck_game.py
        ├── exercise_3_rivalry_guessing.py
        ├── exercise_4_rivalry_rps.py
        ├── exercise_5_rescue_adventure.py
        └── exercise_6_project_your_game.py
```

---

## 6. Implementation Phases

Implementation is organized into 6 phases following the concept progression.

**After completing each phase:** Mark it with a checkmark below the phase header.

### Phase 1: Basic While Loops (Cluster A)

**Exercises:** 1, 2
**Difficulty:** 1-2
**Estimated Files:** 2

| # | Type | File |
|---|------|------|
| 1 | write_code | `write_code/exercise_1_basic_while.py` |
| 2 | bug_hunt | `bug_hunt/exercise_1_infinite_loops.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| write_code | [templates/exercise_types/write_code.py](../../templates/exercise_types/write_code.py) |
| bug_hunt | [templates/exercise_types/bug_hunt.py](../../templates/exercise_types/bug_hunt.py) |
| hybrid_arcs README | [templates/hybrid_arcs/README.md](../../templates/hybrid_arcs/README.md) |

---

### Phase 2: Loop Control + Hybrid 1 (Cluster B)

**Exercises:** 3, 4, 5, Hybrid 1
**Difficulty:** 2-3
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 3 | write_code | `write_code/exercise_2_break_loops.py` |
| 4 | write_code | `write_code/exercise_3_continue_loops.py` |
| 5 | bug_hunt | `bug_hunt/exercise_2_break_continue.py` |
| H1 | hybrid (rivalry) | `hybrid/exercise_1_rivalry_loop_duel.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| rivalry arc | [templates/hybrid_arcs/rivalry.md](../../templates/hybrid_arcs/rivalry.md) |

---

### Phase 3: Random Module + Hybrid 3 (Cluster C)

**Exercises:** 6, 7, Hybrid 3
**Difficulty:** 2-3
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 6 | write_code | `write_code/exercise_4_random_basics.py` |
| 7 | bug_hunt | `bug_hunt/exercise_3_random_bugs.py` |
| H3 | hybrid (rivalry) | `hybrid/exercise_3_rivalry_guessing.py` |

**Read Before This Phase:**

*(All templates already read in previous phases)*

---

### Phase 4: Input Validation + Hybrid 2 (Cluster D)

**Exercises:** 8, 9, Hybrid 2
**Difficulty:** 3
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 8 | add_error_handling | `add_error_handling/exercise_1_input_validation.py` |
| 9 | write_code | `write_code/exercise_5_input_functions.py` |
| H2 | hybrid (rescue) | `hybrid/exercise_2_rescue_stuck_game.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| add_error_handling | [templates/exercise_types/add_error_handling.py](../../templates/exercise_types/add_error_handling.py) |
| rescue arc | [templates/hybrid_arcs/rescue.md](../../templates/hybrid_arcs/rescue.md) |

---

### Phase 5: Game Loops + Hybrid 4 (Cluster E)

**Exercises:** 10, 11, Hybrid 4
**Difficulty:** 3-4
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 10 | bug_hunt | `bug_hunt/exercise_4_game_logic.py` |
| 11 | add_error_handling | `add_error_handling/exercise_2_game_commands.py` |
| H4 | hybrid (rivalry) | `hybrid/exercise_4_rivalry_rps.py` |

**Read Before This Phase:**

*(All templates already read in previous phases)*

---

### Phase 6: Complete Games + Hybrids 5, 6 (Cluster F)

**Exercises:** 12, Hybrid 5, Hybrid 6
**Difficulty:** 4-5
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 12 | write_code | `write_code/exercise_6_simple_game.py` |
| H5 | hybrid (rescue) | `hybrid/exercise_5_rescue_adventure.py` |
| H6 | hybrid (project) | `hybrid/exercise_6_project_your_game.py` |

**Read Before This Phase:**

*(All templates already read in previous phases)*

---

### Phase Summary

| Phase | Cluster | Exercises | Files | New Templates |
|:-----:|---------|-----------|:-----:|---------------|
| 1 | Basic While | 1-2 | 2 | write_code, bug_hunt |
| 2 | Loop Control + H1 | 3-5, H1 | 4 | rivalry arc |
| 3 | Random + H3 | 6-7, H3 | 3 | *(none)* |
| 4 | Input Validation + H2 | 8-9, H2 | 3 | add_error_handling, rescue arc |
| 5 | Game Loops + H4 | 10-11, H4 | 3 | *(none)* |
| 6 | Complete Games + H5, H6 | 12, H5, H6 | 3 | *(none)* |
| **Total** | | **18** | **18** | |

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every exercise contains at least one `{{placeholder}}`
- [ ] NO concepts from later modules used (no dicts/classes/try-except for type errors)
- [ ] All 8 learning objectives covered
- [ ] Progressive difficulty (1 to 5)
- [ ] Hybrid exercises are substantial game projects

### Format Requirements

- [ ] All functions use `pass` placeholder
- [ ] Instructions use `# YOUR CODE HERE` marker
- [ ] Each file has `main()` that calls all exercises
- [ ] PEP 8 compliant
- [ ] Follows templates from `templates/exercise_types/`

### Curriculum Compliance

| Concept | Used In |
|---------|---------|
| basic while | Exercises 1, 2 |
| break | Exercises 3, 5, H1 |
| continue | Exercises 4, 5, H1 |
| random module | Exercises 6, 7, H3, H4 |
| input validation | Exercises 8, 9, H2 |
| game loops | Exercises 10, 11, H4 |
| complete games | Exercise 12, H5, H6 |

---

## 8. Implementation Notes

### Key Constraints

1. **No try/except for type conversion** - Use while loops with string checking instead
2. **No dictionaries** - Use if/elif chains for command handling
3. **No classes** - Games must use functions and global state carefully
4. **Students HAVE functions** - This is the first module where students can define their own functions

### Pedagogical Considerations

**Why while loops are challenging:**
- Infinite loops are easy to create accidentally
- Loop condition must eventually become False
- Off-by-one in loop termination
- Forgetting to update loop variable
- break/continue flow can be confusing

**Building mental models:**
- "While" = "keep going as long as"
- Loop condition checked BEFORE each iteration
- break = "emergency exit"
- continue = "skip to next iteration"

**Game development motivation:**
- Games provide intrinsic feedback (did it work?)
- Natural context for loops (game loop, play again)
- Randomness makes games replayable
- Students are excited to show friends

### Common Bugs to Include in bug_hunt

1. **Infinite loops:** Forgetting to update counter or condition
2. **Off-by-one:** `while count < 10` vs `while count <= 10`
3. **Wrong comparison:** `while x = 5` instead of `while x == 5`
4. **break in wrong place:** Breaking before necessary action
5. **Missing break:** Loop never exits
6. **Random range errors:** `randint(1, 6)` is inclusive on both ends
7. **Game state bugs:** Not resetting between rounds
8. **Input never validated:** Accepting invalid input

### Game Patterns to Cover

| Pattern | Description | Exercise Coverage |
|---------|-------------|-------------------|
| Counter loop | `while count < limit:` | Phase 1 |
| Sentinel loop | `while input != "quit":` | Phase 2 |
| Validation loop | `while not valid:` | Phase 4 |
| Game loop | `while playing:` with win/lose | Phase 5-6 |
| Play again | `while play_again == "yes":` | Phase 6 |

### Input Validation Pattern (No try/except)

Since try/except isn't available yet, input validation should use string methods:

```python
# Validate numeric input without try/except
user_input = input("Enter a number 1-10: ")
while not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 10:
    print("Invalid! Please enter a number between 1 and 10.")
    user_input = input("Enter a number 1-10: ")
number = int(user_input)
```

### Placeholder Usage Ideas

- `{{hero}}` playing games against `{{villain}}`
- `{{creature}}` guessing games (guess the creature's number)
- `{{item}}` collection games
- `{{spell1}}`, `{{spell2}}` as game commands
- `{{location}}` exploration in text adventure
- `{{school}}` tournament brackets
- `{{exclamation}}` for win/lose messages

### Arc Selection Rationale

| Arc | Count | Why Selected |
|-----|:-----:|--------------|
| **Rivalry** | 3 | Perfect for games - defeat, train, triumph |
| **Rescue** | 2 | Debug broken games, make them robust |
| **Project** | 1 | Capstone: build your own game |

### Arcs NOT Used (and why)

| Arc | Why Not |
|-----|---------|
| Apprentice | Requires fill_blanks/complete_function (not available) |
| Mystery | Requires output_prediction/code_tracing (not available) |
| Upgrade | Requires which_is_better/simplify_code (not available) |
| Competition | Requires which_is_better (not available) |
| Inheritance | Requires code_tracing (not available) |

**Note:** The limited arc options are offset by the inherently engaging nature of game development. Each hybrid is essentially a mini-game project.

---

## 9. Concept-Specific Teaching Notes

### Basic While Loops (Cluster A)

- Contrast with for loops: "for = known count, while = unknown count"
- Always ask: "What makes this loop stop?"
- Start with simple counters before complex conditions
- Visualize with print statements inside loop

### Loop Control (Cluster B)

- `break` exits the loop immediately
- `continue` skips to the next iteration
- Both only affect the innermost loop
- Use sparingly - often a sign of redesign needed

### Random Module (Cluster C)

- `import random` at top of file
- `random.randint(a, b)` includes both endpoints!
- `random.choice(list)` picks one item
- `random.random()` gives float 0.0 to 1.0

**Common confusion:** `randint(1, 6)` can return 6 (unlike range!)

### Input Validation (Cluster D)

- Pattern: ask, validate, loop if bad, proceed if good
- Give clear error messages
- Don't let bad input crash the program
- Use `.lower()` for case-insensitive comparison

### Game Loops (Cluster E)

- Outer loop: "play again?"
- Inner loop: single game session
- Track state: score, turns, game over conditions
- Handle all possible inputs

### Complete Games (Cluster F)

- Plan before coding: what are the rules?
- Start with minimal viable game
- Add features incrementally
- Test after each addition

### Classic Games to Build

| Game | Key Concepts | Difficulty |
|------|--------------|:----------:|
| Number Guessing | while, random, comparison | 2-3 |
| Rock Paper Scissors | random.choice, conditionals | 3 |
| Word Guessing (Hangman) | while, string ops, lists | 4 |
| Text Adventure | while, commands, state | 4-5 |
| Dice Games | random, scoring, rounds | 3-4 |

---
