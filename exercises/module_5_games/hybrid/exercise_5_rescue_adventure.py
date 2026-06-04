# %% [markdown]
# {{CONTEXT_SETBACK_INTRO}}
#
# זוהי תרגיל בכמה חלקים שבו את מצילה משחק הרפתקאות טקסטואלי.
# תמצאי באגים, תתקני ניווט, תוסיפי טיפול בשגיאות ואז תרחיבי את המשחק!
#
# מושגי תכנות: לולאות `while`, מילונים (הצצה ראשונה), פירוש פקודות, מצב משחק
#
# חלק 1: ההרפתקה השבורה
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# למשחק ההרפתקאות של {{friend}} יש באגים קריטיים.
# שחקנים נתקעים והמשחק קורס!
#
# באגים למציאה: 3
#
#
# עולם המשחק (מפושט — ללא מילונים, נשתמש ברשימות מקבילות)

# %%
ROOM_NAMES = ["entrance", "hallway", "treasure_room", "exit"]

# %%
ROOM_DESCRIPTIONS = [
    "You are at the entrance of {{location}}.",
    "A long hallway stretches before you.",
    "{{exclamation}} A treasure chest gleams!",
    "The exit! Fresh air awaits."
]

# %% [markdown]
# ## חיבורים: אינדקס = חדר המוצא, ערך = [צפון, דרום, מזרח, מערב] או 1- אם חסום

# %%
ROOM_CONNECTIONS = [
    [-1, -1, 1, -1],   # entrance: east to hallway
    [2, -1, 3, 0],     # hallway: north to treasure, east to exit, west to entrance
    [-1, 1, -1, -1],   # treasure: south to hallway
    [-1, -1, -1, 1]    # exit: west to hallway
]

# %%
return ROOM_DESCRIPTIONS[room_index]  # BUG 1: Crashes if index out of range

# %%
# BUG 2: Direction indices are wrong!
direction_index = {
    "north": 2,  # Should be 0
    "south": 0,  # Should be 1
    "east": 3,   # Should be 2
    "west": 1    # Should be 3
}

if direction not in direction_index:
    return current_room

idx = direction_index[direction]
next_room = ROOM_CONNECTIONS[current_room][idx]

# BUG 3: Returns -1 instead of current_room when blocked!
return next_room  # Should check if -1 and return current_room

# %%
current_room = 0
print("=== {{school}} Adventure ===")
print(buggy_get_room_description(current_room))

while current_room != 3:  # Exit is room 3
    command = input("\n> ").lower().strip()

    if command in ["north", "south", "east", "west"]:
        new_room = buggy_move(current_room, command)
        if new_room == current_room:
            print("You can't go that way.")
        else:
            current_room = new_room
            print(buggy_get_room_description(current_room))
    elif command == "look":
        print(buggy_get_room_description(current_room))
    elif command == "quit":
        break
    else:
        print("Unknown command.")

print("\nThanks for playing!")

# %% [markdown]
# תקני את הבאג!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# תקני את הבאגים!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 2: תיקון הניווט
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# במערכת התנועה יש באגים עדינים יותר.
# מצאי ותקני את בעיות הניווט האלה.

# %%
# BUG 1: No stripping of extra spaces
# BUG 2: Doesn't extract direction from "go north"
parts = command_string.split()
if len(parts) == 1:
    return parts[0]
return None  # Fails on "go north"

# %% [markdown]
# תקני את הבאגים!
#
# 1. הסירי רווחים מיותרים והמירי לאותיות קטנות
# 2. פצלי לחלקים
# 3. אם יש חלק אחד והוא כיוון — החזירי אותו
# 4. אם יש שני חלקים והראשון הוא `go` — החזירי את השני אם הוא כיוון תקין
# 5. אחרת החזירי `None`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
if room_index == 2:  # Treasure room
    if has_treasure:  # BUG: Logic inverted! Should be "not has_treasure"
        return False
    print("You found the treasure!")
    return True
return has_treasure

# %% [markdown]
# תקני את הבאג!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 3: הוספת טיפול בשגיאות
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# הפכי את ההרפתקה לעמידה בפני קריסות!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# הוסיפי טיפול בשגיאות!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# משתנים:
# - `current_room` = חדר ההתחלה
# - `has_treasure` = `False`
# - `playing` = `True`
#
# כל עוד `playing` הוא `True`:
# 1. הציגי את תיאור החדר הנוכחי
# 2. הציגי את הפקודות: `north`/`south`/`east`/`west`/`look`/`inventory`/`quit`
# 3. קבלי קלט
# 4. עבדי על הפקודה:
#    - כיוונים: הזזה והצגת משוב
#    - `look`: הצגת תיאור
#    - `inventory`: הצגה אם יש אוצר
#    - `quit`: הגדירי `playing = False`
# 5. בדקי אם נמצא אוצר
# 6. בדקי תנאי ניצחון (בחדר היציאה עם האוצר)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 4: הרחבת ההרפתקה
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# הוסיפי תכונות חדשות כדי לשפר את ההרפתקה!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
import random

# %% [markdown]
# כתבי את הקוד שלך כאן!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
import random

print("=" * 50)
print(f"   {{{{school}}}} ADVENTURE")
print("   Enhanced Edition")
print("=" * 50)
print()
print(f"{{{{hero}}}} seeks treasure in {{{{location}}}}!")
print("Find the treasure and escape!")
print()

# %% [markdown]
# לולאת המשחק:
# 1. התחילי בכניסה (חדר 0)
# 2. עקבי אחרי: `current_room`, `has_treasure`, `score`, `hp`
# 3. בכל חדר:
#    - בדקי אם יש מפגש עם אויב
#    - אם יש אויב — הפעילי קרב
#    - אם הובסת — סיום משחק
# 4. תנועה ואיסוף אוצר
# 5. ניצחון: הגיעי ליציאה עם האוצר
# 6. עקבי אחרי שיאים
# 7. אפשרות לשחק שוב

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## ראשי

# %%
print("=" * 60)
print("{{CONTEXT_SETBACK_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Fix the broken adventure...")
print("(DON'T RUN buggy_adventure - it has issues!)")
print("(Implement fixed_get_room_description and fixed_move)")
print()
# Test fixes:
# print(fixed_get_room_description(0))  # Should work
# print(fixed_get_room_description(99))  # Should say "Invalid room"
# print(fixed_move(0, "east"))  # Should return 1 (hallway)
# print(fixed_move(0, "north"))  # Should return 0 (blocked)

print()
print(">>> PART 2: Debug navigation...")
print("(Implement fixed_parse_command and fixed_check_item)")
print()
# Test:
# print(fixed_parse_command("  go  north  "))  # Should return "north"
# print(fixed_parse_command("east"))  # Should return "east"

print()
print(">>> PART 3: Add error handling...")
print("(Implement safe functions and robust_adventure_loop)")
print()
# robust_adventure_loop(0)

print()
print(">>> PART 4: Build the enhanced adventure...")
print("(Implement all enhancements)")
print()
# enhanced_adventure()

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
