# שיעור: שימוש במודולים - חלק 3: מודול Datetime

> **מודול**: module_8_modules
> **חלק**: 3 מתוך 6
> **רמת קושי**: 3
> **משך**: 5-6 דקות

---

## מטרת למידה

בסוף חלק זה, התלמיד יוכל:

- להשתמש במודול datetime לעבודה עם תאריכים וזמנים

---

## מושגי מפתח

| מושג | הסבר במשפט אחד |
|------|----------------|
| `datetime.datetime.now()` | מחזיר את התאריך והזמן הנוכחיים |
| `datetime.date.today()` | מחזיר רק את התאריך של היום (פשוט יותר מ-datetime) |
| `.strftime()` | מעצב אובייקט datetime למחרוזת קריאה |
| `timedelta` | מייצג משך זמן (הפרש בין שני תאריכים/זמנים) |

---

## תוכן השיעור

### בהמשך לחלק 2

תרגלנו עם random - עכשיו בואו נלמד מודול חדש לגמרי. מודול datetime עוזר לנו לעבוד עם תאריכים וזמנים.

### קבלת התאריך והזמן הנוכחיים

```python
import datetime

# תאריך וזמן נוכחיים
now = datetime.datetime.now()
print(now)  # 2024-01-15 14:30:45.123456

# רק התאריך של היום (פשוט יותר)
today = datetime.date.today()
print(today)  # 2024-01-15
```

### עיצוב תאריכים

משתמשים ב-`.strftime()` ליצירת מחרוזות תאריך יפות:

```python
import datetime

now = datetime.datetime.now()

# קודי פורמט נפוצים:
# %Y = שנה (2024)
# %m = חודש (01-12)
# %d = יום (01-31)
# %H = שעה (00-23)
# %M = דקה (00-59)

formatted = now.strftime("%Y-%m-%d")  # "2024-01-15"
nice = now.strftime("%B %d, %Y")      # "January 15, 2024"
```

### חישוב הפרשי זמן

```python
import datetime

today = datetime.date.today()
birthday = datetime.date(2024, 12, 25)  # שנה, חודש, יום

days_until = birthday - today
print(f"ימים עד יום ההולדת: {days_until.days}")
```

### לשים לב ל

- ה-datetime הכפול: `datetime.datetime` (שם המודול זהה לשם המחלקה)
- אלטרנטיבה: `from datetime import datetime` ואז רק להשתמש ב-`datetime.now()`

---

## תרגילי תרגול

| תרגיל | הערות |
|-------|-------|
| exercise_1_datetime | טיפול מעשי בתאריכים - קבלה ועיצוב של הזמן הנוכחי |
| exercise_7_time_calculator | חישוב הפרשי זמן בין תאריכים |

---

## נקודת בדיקה

לשאול: "איך מקבלים את התאריך והזמן הנוכחיים?"
צפוי: `datetime.datetime.now()` או `from datetime import datetime` ואז `datetime.now()`

---

## אם התלמיד מתקשה

- **אם datetime.datetime מבלבל**: להשתמש ב-`from datetime import datetime` כדי לפשט, או להתחיל עם `datetime.date.today()` לפעולות עם תאריך בלבד
- **אם קודי strftime מציפים**: להתחיל רק עם `%Y-%m-%d` - הם יכולים לחפש אחרים לפי הצורך
