# שיעור: שימוש במודולים - חלק 5: מודול JSON

> **מודול**: module_8_modules
> **חלק**: 5 מתוך 6
> **רמת קושי**: 3
> **משך**: 5-6 דקות

---

## מטרת למידה

בסוף חלק זה, התלמיד יוכל:

- להשתמש במודול json לשמירה וטעינת נתונים

---

## מושגי מפתח

| מושג | הסבר במשפט אחד |
|------|----------------|
| JSON | פורמט טקסט לאחסון נתונים (JavaScript Object Notation) |
| `json.dumps(data)` | ממיר נתוני פייתון למחרוזת JSON ("dump string") |
| `json.loads(string)` | ממיר מחרוזת JSON בחזרה לנתוני פייתון ("load string") |
| `json.dump(data, file)` | כותב נתוני פייתון לקובץ כ-JSON |
| `json.load(file)` | קורא JSON מקובץ לנתוני פייתון |

---

## תוכן השיעור

### בהמשך לחלק 4

למדנו math - עכשיו בואו נלמד משהו מאוד מעשי: שמירת נתונים! מודול json מאפשר לנו לשמור נתוני פייתון (מילונים, רשימות) לקבצים.

### המרה מ/ל מחרוזות JSON

```python
import json

# מילון פייתון
character = {
    "name": "{{hero}}",
    "level": 5,
    "spells": ["{{spell1}}", "{{spell2}}"]
}

# המרה למחרוזת JSON
json_string = json.dumps(character)
print(json_string)  # {"name": "{{hero}}", "level": 5, "spells": [...]}

# המרה בחזרה לפייתון
data = json.loads(json_string)
print(data["name"])  # {{hero}}
```

### שמירה לקובץ

```python
import json

game_state = {
    "player": "{{hero}}",
    "score": 100,
    "items": ["{{item}}", "potion"]
}

# שמירה לקובץ
with open("save_game.json", "w") as file:
    json.dump(game_state, file)
```

### טעינה מקובץ

```python
import json

# טעינה מקובץ
with open("save_game.json", "r") as file:
    loaded_data = json.load(file)

print(f"ברוך שובך, {loaded_data['player']}!")
print(f"הניקוד שלך: {loaded_data['score']}")
```

### טריק זיכרון: s = string (מחרוזת)

- `dumps` / `loads` = עובדים עם **מחרוזות** (s)
- `dump` / `load` = עובדים עם קבצים (בלי s)

### לשים לב ל

- בלבול בין `dump`/`dumps` ו-`load`/`loads`
- יסודות טיפול בקבצים: שימוש ב-`with open()` ומצב נכון ("w" לכתיבה, "r" לקריאה)

---

## תרגילי תרגול

| תרגיל | הערות |
|-------|-------|
| exercise_4_json_save | שמירת נתונים לקובץ JSON |
| exercise_5_json_load | טעינת נתונים מקובץ JSON |

---

## נקודת בדיקה

לשאול: "באיזה מודול היית משתמש כדי לשמור מילון לקובץ?"
צפוי: json

---

## אם התלמיד מתקשה

- **אם JSON מבלבל**: להתחיל עם `json.dumps()` (למחרוזת) כדי לראות את הפלט, לפני פעולות קובץ
- **אם טיפול בקבצים לא ברור**: להתמקד בתבנית `with open()` - היא מטפלת בפתיחה וסגירה אוטומטית
