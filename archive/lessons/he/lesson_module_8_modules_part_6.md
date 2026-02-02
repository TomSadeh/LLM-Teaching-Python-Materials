# שיעור: שימוש במודולים - חלק 6: חקירת מודולים

> **מודול**: module_8_modules
> **חלק**: 6 מתוך 6
> **רמת קושי**: 3
> **משך**: 5-6 דקות

---

## מטרת למידה

בסוף חלק זה, התלמיד יוכל:

- לחקור מודולים חדשים באמצעות `dir()`, `help()` ותיעוד

---

## מושגי מפתח

| מושג | הסבר במשפט אחד |
|------|----------------|
| `dir(module)` | מציג את כל השמות (פונקציות, משתנים) הזמינים במודול |
| `help(module.function)` | מציג תיעוד לפונקציה ספציפית |
| תיעוד | מדריכים רשמיים ב-docs.python.org לכל מודולי הספרייה הסטנדרטית |

---

## תוכן השיעור

### בהמשך לחלק 5

עכשיו למדתם כמה מודולים. אבל לפייתון יש עוד מאות! בואו נלמד איך לחקור ולגלות מודולים חדשים בעצמכם.

### שימוש ב-dir() לראות מה זמין

```python
import string

# לראות הכל במודול string
print(dir(string))
# ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'digits', ...]

# קבועים שימושיים במודול string
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)         # 0123456789
```

### שימוש ב-help() לפרטים

```python
import random

# לקבל עזרה על פונקציה ספציפית
help(random.choice)
# מראה: choice(seq) - Return a random element from the non-empty sequence seq.
```

### קריאת תיעוד

התיעוד הרשמי של פייתון ב-**docs.python.org** מכיל מידע מפורט על כל מודול:
- אילו פונקציות זמינות
- אילו ארגומנטים הן מקבלות
- דוגמאות איך להשתמש בהן

### חקירת מודול חדש: string

```python
import string
import random

# יצירת סיסמה אקראית באמצעות קבועי מודול string
letters = string.ascii_letters  # כל האותיות
digits = string.digits          # כל המספרים
all_chars = letters + digits

password = ""
for i in range(8):
    password += random.choice(all_chars)
print(f"סיסמה שנוצרה: {password}")
```

### לשים לב ל

- עומס מידע מ-`dir()` - הרבה פריטים מתחילים ב-`_` והם פנימיים
- לסנן פריטים פנימיים: `[x for x in dir(module) if not x.startswith('_')]`

---

## תרגילי תרגול

| תרגיל | הערות |
|-------|-------|
| exercise_6_string_utils | שימוש במודול string לעיבוד טקסט |
| exercise_8_random_generator | random מתקדם - יצירת סיסמאות וטוקנים |
| exercise_9_mini_project | פרויקט אינטגרציה שמשתמש במספר מודולים יחד |

---

## נקודת בדיקה

לשאול: "איך היית מגלה אילו פונקציות יש במודול שמעולם לא השתמשת בו?"
צפוי: `dir(module)`, תיעוד, או `help(module)`

---

## אם התלמיד מתקשה

- **אם מוצף מפלט dir()**: להתמקד בפריטים שלא מתחילים בקו תחתון, ולחפש שמות שנשמעים שימושיים
- **אם פלט help() מבלבל**: רק לקרוא את השורה הראשונה - היא בדרך כלל נותנת סיכום פשוט
- **אם לא בטוח איך לחקור**: להתחיל עם מטרה ספציפית ("אני רוצה ליצור סיסמה אקראית") ולחפש פונקציות רלוונטיות
