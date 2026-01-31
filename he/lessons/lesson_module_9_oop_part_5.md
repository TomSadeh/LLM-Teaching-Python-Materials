# שיעור: תכנות מונחה עצמים - חלק 5: חיבור הכל

> **מודול**: module_9_oop
> **חלק**: 5 מתוך 5
> **רמת קושי**: 3
> **משך**: 6-8 דקות

---

## מטרת למידה

בסוף חלק זה, התלמיד יוכל:

- ליצור מחלקות שלמות עם `__init__` ושיטות מרובות, ולהבין איך אובייקטים שומרים מצב

---

## מושגי מפתח

| מושג | הסבר במשפט אחד |
|------|----------------|
| מצב (State) | הערכים הנוכחיים של תכונות האובייקט ברגע נתון |
| אינטראקציה בין אובייקטים | אובייקטים יכולים לעבוד ביחד, לקרוא לשיטות אחד של השני |

---

## תוכן השיעור

### בניה על חלק 4

אנחנו יודעים את כל החלקים. עכשיו בואו נבנה מחלקות שלמות ושימושיות.

### מחלקת Character שלמה

```python
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.is_alive = True

    def attack(self, target):
        if self.is_alive:
            damage = self.strength
            print(f"{self.name} attacks {target.name} for {damage} damage!")
            target.take_damage(damage)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} has {self.health} health remaining.")
        if self.health <= 0:
            self.is_alive = False
            print(f"{self.name} has been defeated!")

    def heal(self, amount):
        if self.is_alive:
            self.health += amount
            print(f"{self.name} heals for {amount}. Health: {self.health}")

    def status(self):
        status = "alive" if self.is_alive else "defeated"
        print(f"{self.name}: {self.health} HP, {status}")
```

### אובייקטים מתקשרים

```python
hero = Character("{{hero}}", 100, 25)
villain = Character("{{villain}}", 80, 30)

hero.attack(villain)    # הגיבור תוקף את הנבל
villain.attack(hero)    # הנבל מגיב

hero.status()
villain.status()
```

### אובייקטים שומרים מצב

הכוח של OOP: אובייקטים זוכרים את המצב שלהם בין קריאות לשיטות:

```python
# כל קריאה משנה את מצב האובייקט
hero.take_damage(20)    # health עכשיו 80
hero.take_damage(15)    # health עכשיו 65
hero.heal(10)           # health עכשיו 75
```

### מופעים מרובים, מצב עצמאי

```python
hero = Character("{{hero}}", 100, 20)
friend = Character("{{friend}}", 80, 15)

hero.take_damage(30)    # health של hero: 70
friend.take_damage(10)  # health של friend: 70

# יש להם ערכי health נפרדים!
```

### לשים לב ל

- **בלבול בין רמת-מחלקה לרמת-מופע**: לכל אובייקט יש תכונות משלו
- **אובייקטים משפיעים אחד על השני בטעות**: לוודא שתלמידים מבינים איזה אובייקט משתנה
- **שכחה להשתמש ב-self בשיטות**: לחזור על זה אם הם עדיין עושים את הטעות הזו

---

## תרגולים

| תרגיל | הערות |
|-------|-------|
| exercise_4_character | מחלקת דמות שלמה - דוגמה בסגנון RPG |
| exercise_5_pet_sim | שינויי מצב - אובייקט אינטראקטיבי |
| exercise_7_bank_account | שיטות מרובות, אימות - מודל מהעולם האמיתי |
| exercise_8_text_adventure | אובייקטים מתקשרים - יישום מורכב |
| exercise_9_game_objects | מחלקות מרובות - פרויקט מלא |

---

## נקודת בדיקה

לשאול: "מתי היית משתמש במחלקה במקום סתם במילון?"
צפוי: כשרוצים לאגד נתונים עם התנהגות/פונקציות שפועלות על הנתונים האלה, וכשאובייקטים צריכים לשמור ולשנות מצב לאורך זמן

---

## אם התלמיד מתקשה

- **אם אינטראקציה בין אובייקטים מבלבלת**: לעבור על כל קריאה לשיטה צעד אחר צעד, להראות מה משתנה
- **אם שינויי מצב לא ברורים**: להדפיס ערכי תכונות אחרי כל פעולה כדי להראות איך הם משתנים
- **אם שוכח תחביר**: לספק תבנית מינימלית שהם יכולים להעתיק ולשנות

---

## רעיונות להרחבה

לתלמידים שמסיימים מוקדם או רוצים אתגר נוסף:

- ליצור משחק טקסט פשוט עם מחלקות Player ו-Enemy
- לבנות חיית מחמד וירטואלית שיש לה צרכים (רעב, אושר) שמשתנים לאורך זמן
- לעשות מחלקת Card ולבנות משחק קלפים פשוט

---

## הערות למורה LLM

- זו שיאו של שיעור ה-OOP - לוודא שכל המושגים הקודמים יציבים לפני דוגמאות מורכבות
- לא להציג ירושה בשיעור הזה - להתמקד ביסודות
- ההקשר של דמות/RPG עובד טוב כי תלמידים מבינים סטטיסטיקות ופעולות
- לעודד תלמידים להתנסות ביצירת מחלקות משלהם
- `self` הוא המושג הכי קשה - אם הם עדיין מתקשים, לחזור על זה שוב
- לשקול לא להשתמש במונח "בנאי" - פשוט לקרוא לזה "שיטת ה-init"
