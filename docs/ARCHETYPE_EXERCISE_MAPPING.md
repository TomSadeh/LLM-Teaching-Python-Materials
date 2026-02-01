# Exercise-to-Archetype Mapping & Opportunities

This document maps existing exercises to their narrative archetypes and identifies opportunities for improvement.

---

## Module 2: Decisions (Conditionals)

### Current Exercises

| Exercise | Type | Archetype | Score | Notes |
|----------|------|-----------|:-----:|-------|
| `exercise_1_password.py` | write_code | **Challenge/Attempt** | 7/9 | Simple password check |
| `exercise_2_grades.py` | write_code | **Progression Tracking** | ? | Grade → Letter conversion |
| `exercise_3_number_game.py` | write_code | **Challenge/Attempt** | ? | Guess too high/low |
| `exercise_4_quiz.py` | write_code | **Knowledge Check** | ? | Book trivia |
| `exercise_5_age_checker.py` | write_code | **Challenge/Attempt** | ? | Threshold checking |
| `exercise_6_calculator.py` | write_code | None | ? | Pure utility |
| `exercise_7_time_greeter.py` | write_code | None | ? | Time-based message |
| `exercise_8_even_odd.py` | write_code | None | ? | Pure math |
| `exercise_9_leap_year.py` | write_code | None | ? | Pure algorithm |

### Archetype Distribution
- Challenge/Attempt: 3
- Knowledge Check: 1
- Progression Tracking: 1
- No Archetype: 4

### Opportunities

**High Priority:**
1. **Add Decision Tree exercise**
   - Replace or enhance calculator with "Choose Your Adventure"
   - Teaches nested if/elif/else naturally
   - High engagement archetype missing from module

2. **Enhance password exercise**
   - Current: Single password check
   - Enhanced: Multiple security levels, hints, retry count
   - Better use of Challenge/Attempt pattern

3. **Convert time_greeter to Character Creation**
   - Instead of generic time greetings
   - Create character profile that changes based on time (energy level, mood)
   - Adds narrative context to time checking

---

## Module 3: Lists

### Current Exercises

| Exercise | Type | Archetype | Score | Notes |
|----------|------|-----------|:-----:|-------|
| `exercise_1_favorites.py` | write_code | **Collection Building** | ? | Basic list creation |
| `exercise_2_loop_list.py` | write_code | **Collection Building** | ? | Iterate and print |
| `exercise_3_magic_8ball.py` | write_code | **Random Assignment** | 8/9 | Sorting Hat variation |
| `exercise_4_madlibs.py` | write_code | **Collection Building** | ? | Build word list, use in story |
| `exercise_5_todo_list.py` | write_code | **Inventory Management** | ? | Add/remove tasks |
| `exercise_6_name_picker.py` | write_code | **Random Assignment** | 8/9 | Choose random name |
| `exercise_7_shopping_total.py` | write_code | None | ? | Sum list of numbers |
| `exercise_8_playlist_shuffler.py` | write_code | **Collection Building** | ? | Music list |
| `exercise_9_word_collector.py` | write_code | **Collection Building** | ? | Build word list |

### Archetype Distribution
- Collection Building: 5
- Random Assignment: 2
- Inventory Management: 1
- No Archetype: 1

### Opportunities

**High Priority:**
1. **Add Knowledge Check with random.choice()**
   - Pull random question from list of questions
   - Combines lists + random in meaningful way
   - Example: "Quiz Master" that randomizes question order

2. **Convert shopping_total to Resource Exchange**
   - Instead of just summing prices
   - Add budget checking, can you afford all items?
   - More meaningful math context

3. **Enhance todo_list**
   - Current: Basic add/remove
   - Enhanced: Priority levels, mark complete/incomplete
   - Bridges to Module 7 dictionaries

**Medium Priority:**
4. **Add Relationship Mapping (simple)**
   - Character → list of friends
   - Teach lists as dictionary values (preview Module 7)
   - Example: "Who are {{hero}}'s friends?"

---

## Module 4: While Loops & Games

### Current Exercises

| Exercise | Type | Archetype | Score | Notes |
|----------|------|-----------|:-----:|-------|
| `exercise_1_guess_number.py` | write_code | **Challenge/Attempt** | ? | Classic number game |
| `exercise_2_rock_paper_scissors.py` | write_code | **Challenge/Attempt** | ? | Play until quit |
| `exercise_3_dice_game.py` | write_code | **Challenge/Attempt** | ? | Dice rolling |
| `exercise_4_your_game.py` | write_code | Various | ? | Student choice |
| `exercise_5_coin_flip_streak.py` | write_code | **Progression Tracking** | ? | Track streak |
| `exercise_6_higher_lower.py` | write_code | **Challenge/Attempt** | ? | Card game |
| `exercise_7_trivia.py` | write_code | **Knowledge Check** | ? | Loop until wrong |
| `exercise_8_word_scramble.py` | write_code | **Challenge/Attempt** | ? | Unscramble words |
| `exercise_9_adventure.py` | write_code | **Decision Tree** | ? | Text adventure |

### Archetype Distribution
- Challenge/Attempt: 5
- Decision Tree: 1
- Knowledge Check: 1
- Progression Tracking: 1

### Opportunities

**High Priority:**
1. **Enhance adventure.py**
   - Current: Open-ended structure
   - Provide clearer Decision Tree template
   - Add state tracking (inventory, health)

2. **Add Inventory Management game**
   - Collect items during gameplay
   - Use items to solve puzzles
   - Combines Challenge + Inventory patterns

3. **Convert trivia to Knowledge Check with score**
   - Track total correct answers
   - Progressive difficulty
   - "Achievement unlocked" at milestones

**Medium Priority:**
4. **Add Resource Exchange**
   - Gambling/betting game with gold
   - Teaches variable updates in loop
   - "Casino" or "Market Trading" game

---

## Module 7: Dictionaries

### Current Exercises

| Exercise | Type | Archetype | Score | Notes |
|----------|------|-----------|:-----:|-------|
| `exercise_1_spellbook.py` | write_code | **Character Creation** | ? | Define spell dicts |
| `exercise_2_character_stats.py` | write_code | **Character Creation** | ? | Hero profiles |
| `exercise_3_loop_dictionaries.py` | write_code | None | ? | Iteration practice |
| `exercise_4_nested_data.py` | write_code | **Relationship Mapping** | ? | Nested structures |
| `exercise_5_dict_methods.py` | write_code | None | ? | .get(), .setdefault() |
| `exercise_6_quiz_game.py` | write_code | **Knowledge Check** | ? | Question: Answer dict |
| `exercise_7_secret_codes.py` | write_code | None | ? | Cipher dictionary |
| `exercise_8_rpg_inventory.py` | write_code | **Inventory Management** | 9/9 | Full CRUD + shop |
| `exercise_9_contact_book.py` | write_code | **Inventory Management** | ? | Contacts CRUD |

### Archetype Distribution
- Inventory Management: 2
- Character Creation: 2
- Knowledge Check: 1
- Relationship Mapping: 1
- No Archetype: 3

### Opportunities

**High Priority:**
1. **Enhance nested_data.py with Relationship Mapping**
   - Current: Just show nested structure
   - Enhanced: Query relationships, find mutual connections
   - Example: "{{hero}}'s friends who are also in {{house}}"

2. **Convert secret_codes to Resource Exchange**
   - Buy/unlock cipher keys with points
   - Each cipher costs different amounts
   - Combines dicts + resource management

3. **Add Progression Tracking**
   - Track character stats that level up
   - XP → level with dict tracking
   - Missing archetype in this module

**Medium Priority:**
4. **Enhance loop_dictionaries**
   - Not just iteration practice
   - Use Collection Building: build a dictionary through user input
   - "Create Your Spellbook" by adding spells

5. **Add Decision Tree with dict state**
   - Adventure where choices update a character dict
   - Player.health, player.inventory change with choices
   - Combines Module 2 concept with Module 7 data

---

## Module 9: OOP

### Current Exercises

| Exercise | Type | Archetype | Score | Notes |
|----------|------|-----------|:-----:|-------|
| `exercise_1_first_class.py` | write_code | **Character Creation** | ? | Basic class |
| `exercise_2_init_method.py` | write_code | **Character Creation** | ? | Constructor |
| `exercise_3_methods.py` | write_code | **Character Creation** | ? | Behavior |
| `exercise_4_str_repr.py` | write_code | None | ? | String representation |
| `exercise_5_interaction.py` | write_code | **Challenge/Attempt** | 8/9 | Objects interact |
| `exercise_6_inheritance.py` | write_code | **Character Creation** | 8/9 | Wizard subclass |
| `exercise_7_composition.py` | write_code | **Relationship Mapping** | ? | Has-a relationship |
| `exercise_8_text_adventure.py` | complete_function | **Decision Tree** | ? | Room navigation |
| `exercise_9_rpg_battle.py` | complete_function | **Challenge/Attempt** | ? | Combat system |

### Archetype Distribution
- Character Creation: 4
- Challenge/Attempt: 2
- Decision Tree: 1
- Relationship Mapping: 1
- No Archetype: 1

### Opportunities

**High Priority:**
1. **Add Inventory Management as class**
   - Missing from OOP module
   - Natural fit: Inventory class with methods
   - Could replace or enhance str_repr exercise

2. **Enhance composition with Relationship Mapping**
   - Current: Basic has-a relationship
   - Enhanced: Team class with member management
   - Query team relationships, find synergies

3. **Add Progression Tracking class**
   - Character class with experience system
   - Encapsulates level-up logic
   - Natural OOP pattern

**Medium Priority:**
4. **Combine Challenge/Attempt + Progression**
   - Each battle gives XP
   - Character levels up during combat
   - More realistic RPG simulation

---

## Cross-Module Archetype Summary

### Archetype Usage Heat Map

| Archetype | Mod 2 | Mod 3 | Mod 4 | Mod 7 | Mod 9 | Total | Target |
|-----------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:------:|
| Random Assignment | 0 | 2 | 0 | 0 | 0 | 2 | 4 |
| Inventory Management | 0 | 1 | 0 | 2 | 0 | 3 | 6 |
| Character Creation | 0 | 0 | 0 | 2 | 4 | 6 | 8 |
| Challenge/Attempt | 3 | 0 | 5 | 0 | 2 | 10 | 12 |
| Knowledge Check | 1 | 0 | 1 | 1 | 0 | 3 | 6 |
| Progression Tracking | 1 | 0 | 1 | 0 | 0 | 2 | 5 |
| Relationship Mapping | 0 | 0 | 0 | 1 | 1 | 2 | 5 |
| Decision Tree | 0 | 0 | 1 | 0 | 1 | 2 | 5 |
| Collection Building | 0 | 5 | 0 | 0 | 0 | 5 | 6 |
| Resource Exchange | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| **No Archetype** | 4 | 1 | 0 | 3 | 1 | 9 | 0 |

### Critical Gaps

1. **Resource Exchange: 0 exercises**
   - Should appear in: Module 7 (shop), Module 9 (trading)
   - Replace non-archetype exercises

2. **Relationship Mapping: 2 exercises**
   - Natural fit for: Module 7 (nested dicts)
   - Underutilized powerful pattern

3. **Decision Tree: 2 exercises**
   - Should appear in: Module 2 (if/elif/else)
   - High engagement, low usage

4. **Progression Tracking: 2 exercises**
   - Should appear in: Module 7, Module 9
   - Perfect for teaching state changes

5. **No Archetype: 9 exercises**
   - Candidates for enhancement or replacement
   - Pure syntax exercises could use narrative wrapper

---

## Recommended Additions

### Module 2 (Add 2 exercises)
1. **Decision Tree: "The {{location}} Quest"**
   - Replace calculator with narrative adventure
   - Nested if/elif/else with story
   - 3 levels deep, multiple endings

2. **Character Creation: "The Profile Builder"**
   - Input character attributes
   - Use if/else to determine character type
   - Display formatted character card

### Module 3 (Add 1 exercise)
1. **Knowledge Check: "Random Quiz Master"**
   - List of questions and answers
   - Use random.choice() to select question
   - Score tracking

### Module 4 (Add 1 exercise)
1. **Resource Exchange: "The Trading Game"**
   - Start with gold
   - Buy/sell items in loop
   - Win when you reach target gold

### Module 7 (Add 3 exercises)
1. **Progression Tracking: "The Leveling System"**
   - Character dict with XP
   - Add XP, check for level up
   - Update stats on level up

2. **Relationship Mapping: "The Social Network"**
   - Nested dict of character → friends
   - Query mutual friends
   - Find who knows who

3. **Resource Exchange: "The Magic Shop"**
   - Enhanced shop with affordability checks
   - Sell items back for gold
   - Inventory + budget management

### Module 9 (Add 2 exercises)
1. **Inventory Management: "The Inventory Class"**
   - Class-based inventory system
   - Methods for add/remove/display
   - Integration with character class

2. **Progression Tracking: "The Experience System"**
   - Character class with XP methods
   - Automatic level up
   - Stat increases on level

---

## Archetype Quality Indicators

### High-Quality Archetype Implementation

**Indicators:**
- ✅ Natural mapping (operation = action)
- ✅ Immediate feedback on every action
- ✅ Student has agency/choice
- ✅ Progressive complexity (simple → advanced)
- ✅ Theme-agnostic core
- ✅ Multiple placeholders used meaningfully
- ✅ Clear success/failure states

**Example: `exercise_8_rpg_inventory.py` (9/9)**
- ✅ add_item = real collection action
- ✅ Shows inventory after each action
- ✅ Student chooses what to buy/use
- ✅ Starts simple (display), adds complexity (shop)
- ✅ Works as "backpack" without fantasy
- ✅ Uses {{item}}, {{spell1}}, {{hero}}
- ✅ Clear: item added or not enough gold

### Low-Quality Archetype Implementation

**Indicators:**
- ❌ Forced theme (doesn't match operation)
- ❌ No feedback or delayed feedback
- ❌ Passive (student just observes)
- ❌ All complexity at once
- ❌ Only works with fantasy theme
- ❌ Placeholder spam (all 15 used)
- ❌ Unclear what success means

**Example: Hypothetical bad "wizard" exercise**
- ❌ "Make a list called wand_types" (forced theme)
- ❌ Just creates list, no use of it (no feedback)
- ❌ Hardcoded list, no input (passive)
- ❌ Tries to teach indexing, slicing, methods at once
- ❌ "Wand types" has no non-fantasy equivalent
- ❌ Mentions {{hero}}, {{school}}, {{spell1}}, {{wand}}...
- ❌ No clear goal or outcome

---

## Exercise Enhancement Checklist

When revising an exercise without an archetype:

1. **Identify core programming concept**
   - What syntax/structure is being taught?

2. **Select matching archetype**
   - Check "Quick Selection by Module" table

3. **Map operation to action**
   - What real-world action matches the code operation?

4. **Choose 2-4 placeholders**
   - Use archetype's "Required Placeholders"

5. **Add theme-agnostic version**
   - Ensure it works for pymentor theme

6. **Test progression**
   - Does it build from simple to complex?

7. **Verify engagement**
   - Does student have agency?
   - Is there immediate feedback?

---

## See Also

- [NARRATIVE_ARCHETYPES.md](NARRATIVE_ARCHETYPES.md) - Full archetype documentation
- [ARCHETYPE_QUICK_REFERENCE.md](../templates/ARCHETYPE_QUICK_REFERENCE.md) - Quick templates
- [CATALOG.md](CATALOG.md) - All exercises and modules
- [WRITING_GUIDE.md](WRITING_GUIDE.md) - Exercise standards
