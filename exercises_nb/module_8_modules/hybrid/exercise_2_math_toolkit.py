# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# בתרגיל הזה תבני מודול שלם של פונקציות עזר מתמטיות עבור {{school}}.
# תממשי פונקציות בסיסיות, תרחיבי אותן עם יכולות נוספות, ותוסיפי טיפול בשגיאות.
#
# מושגי תכנות: מודול `math`, עיצוב פונקציות, טיפול בשגיאות
# רמת קושי: 2-3

# %%
import math

# %% [markdown]
# ## חלק 1: צמיחה - פונקציות עזר מתמטיות בסיסיות
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# בני פונקציות עזר מתמטיות בסיסיות.
#
# 1. השתמשי ב-`math.pi` ובנוסחה: `area = pi * radius^2`
# 2. החזירי את השטח שחישבת
#
# > רמז: `radius**2` או `math.pow(radius, 2)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# 1. השתמשי במשפט פיתגורס: `c = sqrt(a^2 + b^2)`
# 2. החזירי את התוצאה
#
# > רמז: `math.sqrt(a**2 + b**2)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# 1. בדקי את הפרמטר `direction`
# 2. אם `"up"` - השתמשי ב-`math.ceil()`
# 3. אם `"down"` - השתמשי ב-`math.floor()`
# 4. אם `"nearest"` - השתמשי ב-`round()` (מובנה)
# 5. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - חישובים מתקדמים
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# הוסיפי פעולות מתמטיות מתוחכמות יותר.
#
# 1. חשבי את ההפרשים: `dx = x2 - x1`, `dy = y2 - y1`
# 2. הפעילי את נוסחת המרחק: `sqrt(dx^2 + dy^2)`
# 3. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# > רמז: האלכסון הוא בדיוק היתר של הרוחב והגובה!
# > את יכולה לעשות שימוש חוזר ב-`calculate_hypotenuse()` או לחשב ישירות

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# 1. חשבי `math.pow(base, exponent)` והמירי ל-`int`
# 2. אם `modulo` סופק, החזירי `result % modulo`
# 3. אחרת, החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: שיפור - טיפול בשגיאות
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# הוסיפי טיפול בשגיאות עבור קלט לא תקין.
#
# 1. בדקי אם `radius` הוא מספר (שלם או עשרוני)
#    השתמשי ב: `isinstance(radius, (int, float))`
# 2. אם זה לא מספר, הדפיסי `"Error: radius must be a number"`
#    והחזירי `None`
# 3. בדקי אם `radius` שלילי
# 4. אם שלילי, הדפיסי `"Error: radius cannot be negative"`
#    והחזירי `None`
# 5. חשבי והחזירי את השטח

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# 1. בדקי אם `value` הוא מספר
# 2. בדקי אם `value` שלילי (לא ניתן לחשב שורש של מספר שלילי)
# 3. אם תקין, החזירי `math.sqrt(value)`
# 4. אם לא תקין, הדפיסי שגיאה מתאימה והחזירי `None`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# 1. בדקי אם גם `a` וגם `b` הם מספרים
# 2. בדקי אם `b` הוא אפס
# 3. אם תקין, החזירי `a / b`
# 4. טפלי בשגיאות בצורה מתאימה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## ראשי

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("Math Toolkit for {{school}}")
print("=" * 60)
print()

print(">>> PART 1: Basic Math Helpers")
print("-" * 40)
# Uncomment to test after implementing:
# print(f"Circle area (r=5): {calculate_circle_area(5)}")
# print(f"Hypotenuse (3,4): {calculate_hypotenuse(3, 4)}")
# print(f"Round 3.7 up: {round_to_precision(3.7, 'up')}")
# print(f"Round 3.7 down: {round_to_precision(3.7, 'down')}")
# print(f"Round 3.7 nearest: {round_to_precision(3.7, 'nearest')}")
print()

print(">>> PART 2: Advanced Calculations")
print("-" * 40)
# Uncomment to test:
# print(f"Distance (0,0) to (3,4): {calculate_distance(0, 0, 3, 4)}")
# print(f"Rectangle diagonal 3x4: {calculate_rectangle_diagonal(3, 4)}")
# print(f"2^10: {power_with_modulo(2, 10)}")
# print(f"2^10 mod 100: {power_with_modulo(2, 10, 100)}")
print()

print(">>> PART 3: Safe Functions with Error Handling")
print("-" * 40)
# Uncomment to test:
# print(f"Safe circle area (5): {safe_circle_area(5)}")
# print(f"Safe circle area (-5): {safe_circle_area(-5)}")
# print(f"Safe sqrt (16): {safe_square_root(16)}")
# print(f"Safe sqrt (-16): {safe_square_root(-16)}")
# print(f"Safe divide (10, 2): {safe_divide(10, 2)}")
# print(f"Safe divide (10, 0): {safe_divide(10, 0)}")
print()

print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("=" * 60)
