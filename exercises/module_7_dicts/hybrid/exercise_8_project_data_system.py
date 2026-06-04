# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זהו פרויקט הסיום של מודול 7. תלמדי מערכת לדוגמה,
# תעצבי מבנה משלך, תממשי פעולות, ותוסיפי פיצ'ר מיוחד משלך.
#
# מושגי תכנות: כל מושגי המילונים ממודול 7
#
# ## חלק 1: גילוי - לימוד המערכת לדוגמה
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# לימדי את מערכת ההישגים הזו כדי להבין איך היא עובדת.

# %%
MODEL_ACHIEVEMENTS = {
    "achievements": {
        "first_steps": {
            "name": "First Steps",
            "description": "Complete the tutorial",
            "points": 10,
            "category": "progress"
        },
        "collector": {
            "name": "Collector",
            "description": "Collect 100 items",
            "points": 25,
            "category": "collection"
        },
        "master": {
            "name": "Master",
            "description": "Reach level 50",
            "points": 100,
            "category": "progress"
        }
    },
    "players": {
        "{{hero}}": {
            "unlocked": ["first_steps"],
            "total_points": 10
        },
        "{{heroine}}": {
            "unlocked": ["first_steps", "collector"],
            "total_points": 35
        }
    }
}

# %%
system = MODEL_ACHIEVEMENTS

# Get all achievement IDs
achievement_ids = list(system["achievements"].keys())

# Get a specific achievement's details
collector_details = system["achievements"]["collector"]

# Check what {{hero}} has unlocked
hero_unlocked = system["players"]["{{hero}}"]["unlocked"]

# Get {{hero}}'s points
hero_points = system["players"]["{{hero}}"]["total_points"]

print(f"All achievements: {achievement_ids}")
print(f"Collector details: {collector_details}")
print(f"{{{{hero}}}} unlocked: {hero_unlocked}")
print(f"{{{{hero}}}} points: {hero_points}")

# %% [markdown]
# מלאי את טבלת המעקב הזו:
#
# | נתון                    | נתיב הגישה                                     |
# |-------------------------|------------------------------------------------|
# | השם "Master"            | MODEL_ACHIEVEMENTS["achievements"]["master"]["name"] |
# | נקודות ה-Collector      | MODEL_ACHIEVEMENTS[?][?][?]                   |
# | הנקודות של {{heroine}}  | MODEL_ACHIEVEMENTS[?][?][?]                   |
# | האם {{hero}} היא master? | "master" in MODEL_ACHIEVEMENTS[?][?][?]      |
#
# כמה רמות עמוק הגישה העמוקה ביותר?

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - עיצוב מבנה משלך
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# עצבי וצרי מערכת נתונים משלך באמצעות מילונים.
#
# עצבי קווסטים משלך! היי יצירתית עם שמות ותיאורים.
# השתמשי ב-`{{placeholders}}` לתוכן ערכותי.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - מימוש פעולות בסיסיות
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# ממשי פעולות CRUD עבור מערכת הקווסטים שלך.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: בעלות - הוסיפי פיצ'ר משלך
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# עצבי וממשי פיצ'ר חדש לפי בחירתך!
#
# היי יצירתית! זה הפיצ'ר שלך.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## DEMONSTRATION

# %%
print("=== Creating Quest System ===")
system = create_quest_system()

if system is None:
    print("Please implement create_quest_system() first!")
    return

print(f"Quests: {list(system['quests'].keys())}")
print(f"Players: {list(system['players'].keys())}")
print()

print("=== Adding New Content ===")
# Add a new quest
add_quest(system, "secret", "Secret Mission",
          "Find the hidden {{item}}", 50, "hard")
print(f"Added secret quest: {'secret' in system['quests']}")

# Add a new player
add_player(system, "{{friend}}")
print(f"Added {{{{friend}}}}: {'{{friend}}' in system['players']}")
print()

print("=== Quest Operations ===")
# Start a quest
if start_quest(system, "{{friend}}", "secret"):
    print("{{friend}} started the secret quest!")

# Complete a quest
reward = complete_quest(system, "{{friend}}", "secret")
print(f"{{{{friend}}}} completed quest, earned {reward} points!")
print()

print("=== Player Stats ===")
stats = get_player_stats(system, "{{friend}}")
if stats:
    print(f"{{{{friend}}}} stats: {stats}")

available = get_available_quests(system, "{{friend}}")
print(f"Available quests for {{{{friend}}}}: {available}")
print()

print("=== Your Custom Feature ===")
# Call your custom feature here
# result = your_custom_feature(system, ...)
# print(f"Custom feature result: {result}")
print("(Implement and demonstrate your custom feature!)")

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_DISCOVERY_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Study the model system...")
print()
study_model()
print()
print("(Complete trace_model_access())")
print()

print(">>> PART 2: Design your quest system...")
print("(Implement create_quest_system())")
print()

print(">>> PART 3: Implement operations...")
print("(Implement add_quest, add_player, start_quest, complete_quest,")
print(" get_player_stats, get_available_quests)")
print()

print(">>> PART 4: Add your custom feature...")
print("(Design and implement your_custom_feature())")
print()

# Uncomment to demonstrate:
# demonstrate_system()

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print()
print("Congratulations! You've mastered dictionaries!")
print("=" * 60)
