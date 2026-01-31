# תרגילים 4-6: קלט ופלט

## תרגיל 4: קבלת קלט
`input()` מחכה שהמשתמש יקליד משהו:

```python
name = input("What is your name, young wizard? ")
print("Welcome to Hogwarts, " + name)
```

**חשוב לזכור:**
- `input()` תמיד מחזיר מחרוזת (str)
- גם אם המשתמש הקליד מספר!

## תרגיל 5: קלט + מתמטיקה
כדי לעשות חשבון עם קלט, צריך להמיר למספר:

```python
# כמה שנים עד שסופי פוסטר יכולה להירשם לפוקספייר?
age_text = input("How old are you? ")
age = int(age_text)         # המרה למספר שלם
years_left = 13 - age       # אלפים מתחילים בגיל 13!
print(years_left)

# או בשורה אחת:
district = int(input("Which district are you from? "))
```

**סוגי המרה:**
- `int()` - למספר שלם (12 מחוזות, 4 בתים בהוגוורטס)
- `float()` - למספר עשרוני (3.14)
- `str()` - למחרוזת

## תרגיל 6: חיבור מחרוזות (Mad Libs!)
אפשר לחבר מחרוזות עם `+` כדי ליצור סיפורים:

```python
first = "Expecto"
second = "Patronum"
spell = first + " " + second
print(spell)  # Expecto Patronum

hero = input("Choose a hero: ")
print(hero + " saved the day!")
```

**טיפ:**
אם רוצים לחבר מחרוזת עם מספר:
```python
district = 12
print("Katniss is from District " + str(district))
```

**דוגמאות לתרגיל:**
- הארי פוטר: "Welcome to Hogwarts, " + name
- משחקי הרעב: name + " from District " + str(district)
- פרסי ג'קסון: "The child of " + god + " has arrived at Camp Half-Blood!"
- שומרת הערים האבודות: ability + " is a rare ability!"
