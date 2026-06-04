# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# זוהי תרגילה רב-חלקית שבה את מרחיבה את מערכת המשחק של {{school}}
# עם פיצ'רים של אקראיות מתקדמים. תשתמשי ב-`choice()`, ב-`shuffle()`,
# וב-`sample()` כדי ליצור מכניקות משחק מעניינות.
#
# מושגי תכנות: מודול `random`, מכניקות משחק, עבודה עם רשימות
# רמת קושי: 2-3

# %%
import random

# %% [markdown]
# ## חלק 1: צמיחה - בחירה אקראית עם `choice()`
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# השתמשי ב-`random.choice()` כדי לבחור פריטים אקראיים מתוך אוספים.
#
# 1. צרי רשימות של אפשרויות:
#    `creatures = ["{{creature}}", "guardian", "wanderer", "spirit"]`
#    `actions = ["approaches", "appears", "emerges", "awaits"]`
#    `locations = ["{{location}}", "the path", "the shadows", "ahead"]`
# 2. השתמשי ב-`random.choice()` כדי לבחור מכל רשימה
# 3. בני והחזירי משפט:
#    `f"A {creature} {action} from {location}!"`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. צרי רשימה ממושקלת:
#    `outcomes = ["success"] * 3 + ["partial"] * 2 + ["failure"] * 1`
#    כך מתקבל: 50% הצלחה, 33% חלקי, 17% כישלון
# 2. השתמשי ב-`random.choice(outcomes)`
# 3. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. צרי מאגרי פרסים לכל דרגה:
#    `common = ["gold coins", "health potion", "basic scroll"]`
#    `rare = ["{{item}}", "enchanted gem", "silver key"]`
#    `legendary = ["ancient artifact", "{{spell3}}", "master key"]`
# 2. בחרי את המאגר המתאים לפי הדרגה
# 3. השתמשי ב-`random.choice()` על המאגר שבחרת
# 4. החזירי את הפרס

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - ערבוב עם `shuffle()`
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# השתמשי ב-`random.shuffle()` כדי לערבב סדר לגיימפליי הוגן.
#
# 1. צרי עותק: `deck = items.copy()` או `list(items)`
#    (הפונקציה `shuffle` משנה את הרשימה במקום - לא נרצה לשנות את המקור)
# 2. ערבבי את העותק: `random.shuffle(deck)`
# 3. החזירי את החפיסה המעורבבת

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי ב-`create_shuffled_deck` כדי לקבל סדר אקראי

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# החזירי עותק מעורבב של `challenges`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - דגימה עם `sample()`
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# השתמשי ב-`random.sample()` לבחירות בסגנון הגרלה.
#
# 1. ודאי שה-`count` לא גדול מגודל ה-`pool`:
#    `if count > len(pool):`
#    `    count = len(pool)`
# 2. השתמשי ב-`random.sample(pool, count)`
# 3. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי ב-`draw_items` כדי לבחור חברות צוות

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. צרי מספרי משתתפות: `range(1, participant_count + 1)`
# 2. השתמשי ב-`random.sample()` לבחירת הזוכות
# 3. מיינ את הזוכות: `sorted(winners)`
# 4. החזירי את הרשימה הממוינת

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("Random Adventures in {{school}}")
print("=" * 60)
print()

print(">>> PART 1: Random Selection")
print("-" * 40)
print("Generating random encounters...")
# Uncomment to test:
# for i in range(3):
#     print(f"  {get_random_encounter()}")
# print()
# print("Testing outcomes:")
# for i in range(5):
#     print(f"  Attempt {i+1}: {random_event_outcome()}")
# print()
# print("Reward tiers:")
# print(f"  Common: {select_reward('common')}")
# print(f"  Rare: {select_reward('rare')}")
# print(f"  Legendary: {select_reward('legendary')}")
print()

print(">>> PART 2: Shuffling")
print("-" * 40)
# Uncomment to test:
# players = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]
# print(f"Original order: {players}")
# turn_order = determine_turn_order(players)
# print(f"Turn order: {turn_order}")
# print(f"Original unchanged: {players}")
print()

print(">>> PART 3: Sampling")
print("-" * 40)
# Uncomment to test:
# rewards = ["gold", "gem", "key", "scroll", "potion", "armor", "weapon"]
# drawn = draw_items(rewards, 3)
# print(f"Drew 3 items: {drawn}")
# print()
# all_chars = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}", "ally1", "ally2"]
# team = generate_quest_team(all_chars, 3)
# print(f"Quest team: {team}")
# print()
# winners = lucky_draw(100, 5)
# print(f"Lucky draw winners (from 100): {winners}")
print()

print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("=" * 60)
