# שיעור: תכנות מונחה עצמים - חלק 4: הוספת שיטות

> **מודול**: module_9_oop
> **חלק**: 4 מתוך 5
> **רמת קושי**: 3
> **משך**: 6-8 דקות

---

## מטרת למידה

בסוף חלק זה, התלמיד יוכל:

- להגדיר שיטות שפועלות על נתוני האובייקט ולהבין למה `self` נחוץ

---

## מושגי מפתח

| מושג | הסבר במשפט אחד |
|------|----------------|
| שיטה (Method) | פונקציה ששייכת למחלקה ויכולה לגשת לנתוני האובייקט |
| `self` בשיטות | מאפשר לשיטה לגשת ולשנות את האובייקט הספציפי שעליו היא נקראה |

---

## תוכן השיעור

### בניה על חלק 3

אנחנו יכולים ליצור אובייקטים עם תכונות. עכשיו בואו נוסיף התנהגות - דברים שהאובייקט יכול לעשות.

### שיטות הן פונקציות בתוך מחלקות

```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        print(f"I am {self.name}!")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! Health: {self.health}")
```

### קריאה לשיטות

משתמשים בתחביר הנקודה, בדיוק כמו לתכונות:

```python
hero = Character("{{hero}}", 100)
hero.introduce()           # מדפיס: I am {{hero}}!
hero.take_damage(20)       # מדפיס: {{hero}} takes 20 damage! Health: 80
```

### למה self נדרש

כל שיטה צריכה `self` כפרמטר הראשון שלה:

```python
def introduce(self):       # self נדרש!
    print(f"I am {self.name}!")  # self.name ניגש לשם של האובייקט הזה

# כשקוראים:
hero.introduce()
# פייתון אוטומטית מעביר את hero בתור self
```

חשבו על `self` כאומר לשיטה "עם איזה אובייקט את עובדת?"

### שיטות יכולות לשנות מצב

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

counter = Counter()
counter.increment()
counter.increment()
print(counter.get_count())  # מדפיס: 2
```

### לשים לב ל

- **שכחת self בהגדרה**: `def introduce():` לא יעבוד
- **אי שימוש ב-self לגישה לתכונות**: `print(name)` מחפש משתנה מקומי, לא `self.name`
- **שכחה לקרוא עם סוגריים**: `hero.introduce` לעומת `hero.introduce()`

---

## תרגולים

| תרגיל | הערות |
|-------|-------|
| exercise_3_methods | הוספת שיטות למחלקה |
| exercise_6_counter | מחלקה פשוטה עם מצב - דוגמה מעשית |

---

## נקודת בדיקה

לשאול: "למה לשיטות תמיד יש `self` כפרמטר ראשון?"
צפוי: כדי שהשיטה תדע עם איזה אובייקט היא עובדת - היא יכולה לגשת לתכונות של האובייקט הזה

---

## אם התלמיד מתקשה

- **אם שוכח self**: לגרום להם תמיד לכתוב `self` קודם, ואז להוסיף פרמטרים אחרים
- **אם self.x לעומת x מבלבל**: להסביר ש-`self.name` זה "השם ששמור על האובייקט הזה" בעוד ש-`name` לבד מחפש משתנה מקומי
- **אם שיטות לעומת פונקציות לא ברור**: שיטות הן פונקציות ש"שייכות" לאובייקט ויכולות לגשת לנתונים שלו
