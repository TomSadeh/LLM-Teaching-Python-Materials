<div dir="rtl">

# מודול 3: רשימות - לאסוף דברים

## מה תלמדי
- ליצור רשימות כדי לאחסן הרבה פריטים (כמו רשימת הגיבורים האהובים!)
- לקחת פריטים מרשימה
- לעבור על רשימה בלולאה
- להוסיף ולהסיר פריטים
- לבחור פריטים אקראיים (למשחקים!)

## שיעורים

### שיעור 1: יצירת רשימות
רשימה מחזיקה הרבה פריטים בסדר:

```python
# בתים בהוגוורטס
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# הכישרונות של סופי פוסטר
abilities = ["Telepath", "Inflictor", "Polyglot", "Teleporter", "Enhancer"]

# מחוזות במשחקי הרעב
districts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

### שיעור 2: גישה לפריטים (אינדקס)
לכל פריט יש מספר מיקום (מתחיל מ-0!):

```python
heroes = ["Percy", "Annabeth", "Grover"]
print(heroes[0])   # Percy - הראשון
print(heroes[1])   # Annabeth - השנייה
print(heroes[-1])  # Grover - האחרון!
```

### שיעור 3: לעבור על רשימה בלולאה
השתמשי בלולאת for כדי לעבור על כל פריט:

```python
tributes = ["Katniss", "Peeta", "Rue", "Finnick"]
for tribute in tributes:
    print("May the odds be ever in your favor, " + tribute + "!")
```

### שיעור 4: לשנות רשימות
להוסיף ולהסיר פריטים:

```python
team_valiant = ["Sophie", "Fitz", "Biana"]
team_valiant.append("Keefe")    # הוסיפי: ["Sophie", "Fitz", "Biana", "Keefe"]
team_valiant.remove("Fitz")     # הסירי
print(len(team_valiant))        # אורך: 3
```

### שיעור 5: בחירות אקראיות (כובע המיון!)
לבחור פריטים אקראיים מרשימה:

```python
import random

# כובע המיון!
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
chosen = random.choice(houses)
print("Better be... " + chosen + "!")
```

---

## תרגילים
1. `exercise_1_favorites.py` - רשימת הגיבורים האהובים! 📚
2. `exercise_2_loop_list.py` - עברי על פריטים בלולאה
3. `exercise_3_magic_8ball.py` - כובע המיון! 🎩
4. `exercise_4_madlibs.py` - יוצר סיפורי פנטזיה! ✨

## דוגמאות לרשימות
- **הארי פוטר:** בתים, לחשים, דמויות
- **פרסי ג'קסון:** אלים, מפלצות, מחנאים
- **משחקי הרעב:** מחוזות, נשק, שבטים
- **שומרת הערים האבודות:** כישרונות, שדונים, חברי צוות

## טיפים
- רשימות מתחילות לספור מ-0, לא מ-1!
- `len(my_list)` נותן כמה פריטים יש
- `random.choice(my_list)` בוחר אחד באקראי

</div>
