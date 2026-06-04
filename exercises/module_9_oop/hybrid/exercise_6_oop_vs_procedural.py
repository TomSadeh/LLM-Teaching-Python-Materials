# %% [markdown]
# {{CONTEXT_COMPARISON_INTRO}}
#
# זוהי תרגיל רב-חלקי שבו נחקרי מתי כדאי להשתמש ב-OOP ומתי בגישה פרוצדורלית.
# תשווי בין מימושים שונים, תמירי בין סגנונות,
# ותעצבי מערכת משלך עם הנמקה.
#
# מושגי תכנות: OOP מול פרוצדורלי, החלטות עיצוב, שיפוץ קוד
#
# ## חלק 1: הערכה - השוואה בין גישת המילון לגישת המחלקה
# {{CONTEXT_COMPARISON_DECISION}}
#
# למערכת הרישומים של {{school}} יש שני מימושים.
#
#
# ## גרסה א: מבוססת מילון (פרוצדורלית)

# %%
return {
    "name": name,
    "house": house,
    "year": year,
    "grades": {},
    "attendance": 0
}

# %%
student["grades"][subject] = grade

# %%
student["attendance"] += 1

# %%
grades = student["grades"].values()
if not grades:
    return 0
return sum(grades) / len(grades)

# %%
student["year"] += 1

# %% [markdown]
# ## גרסה ב: מבוססת מחלקה (OOP)

# %%
class Student:
    """A student at {{school}}."""

    def __init__(self, name, house, year):
        self.name = name
        self.house = house
        self.year = year
        self.grades = {}
        self.attendance = 0

    def add_grade(self, subject, grade):
        """Add a grade for a subject."""
        self.grades[subject] = grade

    def record_attendance(self):
        """Increment attendance count."""
        self.attendance += 1

    def get_average_grade(self):
        """Calculate average grade."""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def promote(self):
        """Promote to next year."""
        self.year += 1

# %% [markdown]
# נסי את שתי הגרסאות:
#
#     # גרסת המילון
#     s1 = create_student_dict("{{hero}}", "{{house}}", 1)
#     add_grade_dict(s1, "{{spell1}}", 90)
#     add_grade_dict(s1, "{{spell2}}", 85)
#     record_attendance_dict(s1)
#     print(f"Dict avg: {get_average_grade_dict(s1)}")
#
#     # גרסת המחלקה
#     s2 = Student("{{hero}}", "{{house}}", 1)
#     s2.add_grade("{{spell1}}", 90)
#     s2.add_grade("{{spell2}}", 85)
#     s2.record_attendance()
#     print(f"Class avg: {s2.get_average_grade()}")
#
# כתבי את ההשוואה שלך:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
analysis = """
Comparison:

Dict version calling style:
    add_grade_dict(student, subject, grade)

Class version calling style:
    student.add_grade(subject, grade)

Which is more intuitive?
-

Which is easier to get wrong (e.g., pass wrong data)?
-

Which would be easier to extend with new features?
-
"""
return analysis

# %% [markdown]
# ## חלק 2: צמיחה - המרת קוד פרוצדורלי ל-OOP
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# המירי את מערכת המלאי הפרוצדורלית הזו ל-OOP.
#
#
# ## הגרסה הפרוצדורלית להמרה

# %%
return {"name": name, "max_slots": max_slots, "items": [], "gold": 0}

# %%
if len(inventory["items"]) < inventory["max_slots"]:
    inventory["items"].append({"name": item_name, "value": item_value})
    return True
return False

# %%
for i, item in enumerate(inventory["items"]):
    if item["name"] == item_name:
        inventory["items"].pop(i)
        return True
return False

# %%
total = inventory["gold"]
for item in inventory["items"]:
    total += item["value"]
return total

# %%
print(f"=== {inventory['name']}'s Inventory ===")
print(f"Slots: {len(inventory['items'])}/{inventory['max_slots']}")
for item in inventory["items"]:
    print(f"  - {item['name']} ({item['value']} gold)")
print(f"Gold: {inventory['gold']}")
print(f"Total value: {get_total_value(inventory)}")

# %% [markdown]
# צרי מחלקת `Inventory` ומחלקת `Item` שמשחזרות את הפונקציונליות הזו.
#
# class Item:
#     def __init__(self, name, value):
#         pass
#
# class Inventory:
#     def __init__(self, owner_name, max_slots):
#         pass
#
#     def add_item(self, item):
#         pass
#
#     def remove_item(self, item_name):
#         pass
#
#     def get_total_value(self):
#         pass
#
#     def __str__(self):
#         pass
#
# נסי את ההמרה שלך:
#     inv = Inventory("{{hero}}", 5)
#     inv.add_item(Item("{{item}}", 100))
#     inv.add_item(Item("{{spell1}}", 50))
#     inv.gold = 200
#     print(inv)
#     print(f"Total value: {inv.get_total_value()}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: בעלות - עצבי מערכת משלך
# {{CONTEXT_MASTERY_INTRO}}
# {{CONTEXT_MASTERY_NARRATIVE}}
#
# עצבי מערכת מעקב אחרי משימות. את בוחרת את הגישה!
#
# דרישות למערכת מעקב משימות:
# - מעקב אחרי שם המשימה, תיאור וסטטוס (פעילה / הושלמה)
# - מעקב אחרי פרסים (נקודות ניסיון, זהב, פריטים)
# - תמיכה בכמה יעדים לכל משימה
# - מעקב אחרי התקדמות בכל יעד
# - סימון המשימה כהושלמה כשכל היעדים הושגו
#
# החלטה: תשתמשי ב-OOP או בגישה פרוצדורלית?
#
# אם OOP, שימי לב למחלקות האלה:
# - `Quest` (name, description, status, objectives, rewards)
# - `Objective` (description, current_progress, target_progress)
# - `QuestLog` (אוסף משימות, סינון לפעילות / שהושלמו)
#
# אם פרוצדורלי, שימי לב לפונקציות האלה:
# - `create_quest`, `add_objective`, `update_progress`
# - `check_completion`, `get_active_quests` וכו'
#
# מימשי את הגישה שבחרת והנמיקי את ההחלטה שלך:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
justification = """
I chose: ??? (OOP / Procedural)

Reasons:
1.
2.
3.

This approach is better for this problem because:
-
"""

# Your implementation here:
pass

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_COMPARISON_INTRO}}")
print("OOP vs Procedural Design")
print("=" * 60)
print()

print(">>> PART 1: Compare Dict vs Class")
print()

# Dict version
s_dict = create_student_dict("{{hero}}", "{{house}}", 1)
add_grade_dict(s_dict, "{{spell1}}", 90)
add_grade_dict(s_dict, "{{spell2}}", 85)
print(f"Dict approach - Avg grade: {get_average_grade_dict(s_dict)}")

# Class version
s_class = Student("{{hero}}", "{{house}}", 1)
s_class.add_grade("{{spell1}}", 90)
s_class.add_grade("{{spell2}}", 85)
print(f"Class approach - Avg grade: {s_class.get_average_grade()}")

print()
print("Your analysis:")
print(part1_compare())
print()

print(">>> PART 2: Convert Procedural to OOP")
print()
print("Procedural version:")
inv = create_inventory("{{hero}}", 5)
add_item(inv, "{{item}}", 100)
add_item(inv, "{{spell1}}", 50)
inv["gold"] = 200
display_inventory(inv)
print()
print("Convert to OOP:")
part2_convert_to_oop()
print()

print(">>> PART 3: Design Your Own Quest System")
print("(Choose OOP or procedural and justify)")
part3_design_system()

print()
print("=" * 60)
print("{{CONTEXT_EVALUATION_COMPLETE}}")
print("=" * 60)
