# שיעור: החלטות (if/elif/else) - חלק 4: שילוב תנאים

> **מודול**: module_2_decisions
> **חלק**: 4 מתוך 5
> **רמת קושי**: 2
> **משך**: 5-6 דקות

---

## מטרת למידה

בסוף חלק זה, התלמיד יוכל:

- לשלב תנאים עם `and`, `or`, ו-`not`

---

## מושגי מפתח

| מושג | הסבר במשפט אחד |
|------|----------------|
| `and` | שני התנאים חייבים להיות True כדי שהכל יהיה True |
| `or` | לפחות תנאי אחד חייב להיות True כדי שהכל יהיה True |
| `not` | הופך True ל-False ו-False ל-True |

---

## תוכן השיעור

### בהמשך לחלק 3
- לפעמים תנאי בודד לא מספיק
- מה אם אנחנו צריכים לבדוק מספר דברים בו-זמנית?

### חומר חדש

#### שימוש ב-`and` - שניהם חייבים להיות True
```python
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if age >= 13 and has_ticket == "yes":
    print("Welcome to the movie!")
else:
    print("Sorry, you can't enter.")
```

#### שימוש ב-`or` - לפחות אחד חייב להיות True
```python
day = input("What day is it? ")

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")
```

#### שימוש ב-`not` - הפיכת התנאי
```python
is_raining = False

if not is_raining:
    print("Let's go outside!")
```

### שילוב מספר אופרטורים
```python
# בדיקה אם גיל בין 13 ל-19 (נער/ה)
age = int(input("Enter age: "))
if age >= 13 and age <= 19:
    print("You're a teenager!")

# פייתון גם מאפשר תחביר נקי יותר:
if 13 <= age <= 19:
    print("You're a teenager!")
```

### לשים לב ל
- **לשכוח ש-`and` דורש ששניהם יהיו True**: אם אחד מהם False, הכל False
- **שימוש במילים באנגלית במקום מילות מפתח של פייתון**: חובה להשתמש ב-`and`, `or`, `not` באותיות קטנות

---

## תרגילי תרגול

| תרגיל | הערות |
|-------|-------|
| exercise_5_age_checker | תרגול שילוב תנאים לטווחי גילאים |
| exercise_9_validation | שימוש בתנאים מרובים לאימות קלט |

---

## נקודת בדיקה

לשאול: "איך היית בודק אם מספר נמצא בין 10 ל-20?"
צפוי: `if number >= 10 and number <= 20:` או `if 10 <= number <= 20:`

---

## אם התלמיד מתקשה

- **אם מתקשה עם and/or**: להשתמש בטבלאות אמת עם דוגמאות פשוטות
- **אם מבולבל מתי להשתמש ב-and לעומת or**: "and" = שניהם חייבים להיות אמיתיים (מחמיר יותר), "or" = אחד מהם יכול להיות אמיתי (מקל יותר)
