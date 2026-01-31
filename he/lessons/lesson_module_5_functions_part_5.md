# שיעור: פונקציות - חלק 5: בנייה עם פונקציות

> **מודול**: module_5_functions
> **חלק**: 5 מתוך 5
> **רמת קושי**: 3
> **משך**: 6-8 דקות

---

## מטרת למידה

בסוף חלק זה, התלמיד יוכל:

- לארגן קוד לפונקציות מרובות שעובדות יחד לבניית תוכניות גדולות יותר

---

## מושגי מפתח

| מושג | הסבר במשפט אחד |
|------|----------------|
| פונקציות עזר (Helper functions) | פונקציות קטנות שעושות משימה ספציפית אחת, משמשות פונקציות אחרות |
| טווח (Scope) | היכן משתנה קיים - מקומי (בתוך פונקציה) או גלובלי (מחוץ) |
| הרכבת פונקציות (Function composition) | בניית התנהגות מורכבת על ידי שילוב פונקציות פשוטות יותר |

---

## תוכן השיעור

### בנייה על חלקים 1-4

עכשיו שאנחנו יודעים איך להגדיר פונקציות, להוסיף פרמטרים ולהחזיר ערכים, בואו נראה איך פונקציות עובדות יחד בתוכניות אמיתיות.

### פונקציות שקוראות לפונקציות אחרות

```python
def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def draw_house(t):
    # הבית משתמש בפונקציית הריבוע!
    draw_square(t, 100)  # גוף
    t.forward(100)
    t.right(30)
    t.forward(80)        # צד גג 1
    t.right(120)
    t.forward(80)        # צד גג 2
```

הפונקציה `draw_house` משתמשת ב-`draw_square` - בניית התנהגות מורכבת מחתיכות פשוטות יותר!

### פירוק בעיות

כשמתמודדים עם משימה מורכבת, לחשוב אילו פונקציות קטנות צריך:

```python
# משימה: ליצור מערכת ניקוד למשחק

# פונקציות קטנות וממוקדות
def calculate_bonus(level):
    return level * 10

def calculate_penalty(mistakes):
    return mistakes * 5

def calculate_score(base_points, level, mistakes):
    bonus = calculate_bonus(level)
    penalty = calculate_penalty(mistakes)
    return base_points + bonus - penalty

# להשתמש בהן יחד
final_score = calculate_score(100, 5, 2)
print(f"Your score: {final_score}")  # 100 + 50 - 10 = 140
```

### הבנת טווח (Scope)

משתנים בתוך פונקציות הם "מקומיים" - הם קיימים רק בתוך הפונקציה הזו:

```python
def my_function():
    secret = "{{password}}"  # זה קיים רק בתוך my_function
    print(secret)

my_function()
print(secret)  # שגיאה! 'secret' לא מוגדר מחוץ לפונקציה
```

לחשוב על פונקציות כחדרים נפרדים - משתנים בפנים לא נראים מבחוץ.

### דוגמה מלאה

```python
# כלי ניתוח טקסט

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    count = 0
    for char in text:
        if char in ".!?":
            count += 1
    return count

def analyze_text(text):
    word_count = count_words(text)
    sentence_count = count_sentences(text)

    if sentence_count > 0:
        avg_words = word_count / sentence_count
    else:
        avg_words = 0

    return {
        "words": word_count,
        "sentences": sentence_count,
        "average_words_per_sentence": avg_words
    }

# שימוש בפונקציה הראשית
story = "{{hero}} went to {{school}}. It was amazing! The {{creature}} was there too."
results = analyze_text(story)
print(results)
```

### לשים לב ל

- **בלבול טווח**: לצפות שמשתנים מפונקציה אחת יהיו זמינים באחרת
- **לא לפרק בעיות**: לכתוב פונקציה ענקית אחת במקום כמה קטנות
- **תלויות מעגליות**: פונקציה A קוראת ל-B שקוראת ל-A (יכול לגרום ללולאות אינסופיות)

---

## תרגילי תרגול

| תרגיל | הערות |
|-------|-------|
| exercise_3_helper_functions | פירוק משימות לפונקציות מרובות שמשתפות פעולה |
| exercise_7_text_tools | כלי מניפולציית מחרוזות שעובדים יחד |
| exercise_8_game_functions | לוגיקת משחק מאורגנת בפונקציות |
| exercise_9_turtle_scene | פרויקט אינטגרציה שמשלב פונקציות ציור מרובות |

---

## נקודת בדיקה

לשאול: "למה להשתמש בפונקציות במקום פשוט לכתוב את כל הקוד בסדר?"
צפוי: שימוש חוזר (לכתוב פעם אחת, להשתמש הרבה פעמים), ארגון (יותר קל להבין), יותר קל לתקן באגים (בעיות מבודדות), יותר קל לבדוק (אפשר לבדוק כל פונקציה בנפרד)

---

## אם התלמיד מתקשה

- **אם בעיות טווח**: לדמיין פונקציות כחדרים נפרדים - משתנים בפנים לא נראים מבחוץ
- **אם לא רואה את התועלת**: לבקש מהם לשנות תוכנית ארוכה בלי פונקציות לעומת עם פונקציות - הם יראו שפונקציות קלות יותר
- **אם פונקציות נהיות מורכבות מדי**: להחיל את הכלל "פונקציה אחת, עבודה אחת" - אם פונקציה עושה יותר מדי דברים, לפצל אותה
