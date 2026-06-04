# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגילה רב-שלבית שבה את יורשת מערכת רישום קיימת,
# מבינה איך היא עובדת, מרחיבה אותה ומתקנת בעיות.
#
# מושגי תכנות: מילונים, זוגות מפתח-ערך, `KeyError`, `.get()`
#
# חלק 1: גילוי - הבנת מערכת הרישום שירשת
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{mentor}} השאיר מאחור את מערכת הרישום הזו. לפני שתוכלי להשתמש בה,
# את צריכה להבין איך היא עובדת.
#
# למדי את הקוד שלמטה ועקבי אחר הרצת הביצוע שלו.

# %%
registry = {
    "{{spell1}}": {"power": 10, "type": "basic"},
    "{{spell2}}": {"power": 25, "type": "intermediate"}
}

ability_name = "{{spell1}}"
ability_data = registry[ability_name]
power = ability_data["power"]
print(f"{ability_name}: power {power}")

# %% [markdown]
# ## מלאי את טבלת המעקב
#
# עקבי אחר הערכים של המשתנים בכל שלב.
#
# | שלב | ability_name | ability_data                  | power | פלט |
# |-----|--------------|-------------------------------|-------|-----|
# | 0   | -            | -                             | -     |     |
# | 1   | "{{spell1}}" | -                             | -     |     |
# | 2   |              |                               | -     |     |
# | 3   |              |                               |       |     |
# | 4   |              |                               |       |     |
#
# כתבי את הטבלה המלאה שלך כהערות למטה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 2: בעלות - הרחבת מערכת הרישום
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# עכשיו הפכי את מערכת הרישום לשלך על ידי הוספת ערכים חדשים
# ופונקציה לחיפוש יכולות.
#
# 1. צרי מילון עם 2 היכולות המקוריות:
#    - `"{{spell1}}"`: power 10, type `"basic"`
#    - `"{{spell2}}"`: power 25, type `"intermediate"`
#
# 2. הוסיפי עוד 2 יכולות מעיצובך:
#    - `"{{spell3}}"`: power 50, type `"advanced"`
#    - `"{{spell4}}"`: power 15, type `"utility"`
#
# 3. החזירי את מערכת הרישום

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. בדקי אם `ability_name` קיים במערכת הרישום
#    > רמז: השתמשי ב-`if ability_name in registry:`
#
# 2. אם הוא קיים, הדפיסי: `"[name]: power [X], type [Y]"`
#
# 3. אם לא נמצא, הדפיסי: `"[name] not found in registry"`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 3: חקירה - איתור באגים במערכת הרישום
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# מישהו דיווח על באגים בקוד הרישום הזה. מצאי ותקני אותם!
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "registry.py", line 12, in <module>
#     total_power = total_power + registry[name]["power"]
# KeyError: '{{creature}}'

# %%
requested = ["{{spell1}}", "{{spell2}}", "{{creature}}"]
total_power = 0

for name in requested:
    # BUG: Doesn't check if name exists in registry!
    total_power = total_power + registry[name]["power"]

return total_power

# %% [markdown]
# השגיאה התרחשה כי: _______________
#
# תקני את הקוד כך שהוא:
# 1. מוסיף power רק עבור יכולות שקיימות במערכת הרישום
# 2. מדפיס אזהרה עבור יכולות שלא נמצאו
# 3. מחזיר את סך ה-power של היכולות שנמצאו
#
# > רמז: בדקי אם כל שם קיים לפני שאת ניגשת אליו

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_DISCOVERY_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Understanding the inherited registry...")
print("(Study code_to_trace() and complete trace_the_registry())")
print()
# Uncomment to verify your trace:
# code_to_trace()

print()
print(">>> PART 2: Extending the registry...")
print("(Implement create_extended_registry() and lookup_ability())")
print()
# Uncomment to test:
# registry = create_extended_registry()
# print(f"Registry has {len(registry)} abilities")
# lookup_ability(registry, "{{spell1}}")
# lookup_ability(registry, "{{spell3}}")
# lookup_ability(registry, "unknown")

print()
print(">>> PART 3: Fixing the bugs...")
print("(Implement fixed_power_calculator())")
print()
# Uncomment to test:
# registry = create_extended_registry()
# total = fixed_power_calculator(registry)
# print(f"Total power of found abilities: {total}")

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
