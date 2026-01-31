# תרגיל 4: חידון ספרים! 📚

## המשימה שלך
צרי משחק חידון על הספרים האהובים עליך!

## שלב 1: השלימי את ask_question
הפונקציה צריכה:
1. להדפיס את השאלה
2. לקבל תשובה מהמשתמש
3. לבדוק אם התשובה נכונה
4. להחזיר `True` אם נכון, `False` אם לא

## שלב 2: הוסיפי שאלות מהספרים!
ב-`run_quiz`, הוסיפי לפחות 5 שאלות משלך!

## רעיונות לשאלות

**הארי פוטר:**
```python
if ask_question("What house is Harry in?", "Gryffindor"):
    score = score + 1
if ask_question("What is Hermione's cat called?", "Crookshanks"):
    score = score + 1
```

**פרסי ג'קסון:**
```python
if ask_question("Who is Percy's father?", "Poseidon"):
    score = score + 1
if ask_question("What is the name of Percy's sword?", "Riptide"):
    score = score + 1
```

**משחקי הרעב:**
```python
if ask_question("What district is Katniss from?", "12"):
    score = score + 1
if ask_question("What is Katniss's sister's name?", "Prim"):
    score = score + 1
```

**שומרת הערים האבודות:**
```python
if ask_question("What is Sophie Foster's main ability?", "Telepath"):
    score = score + 1
if ask_question("What school do elves attend?", "Foxfire"):
    score = score + 1
```

## בונוס
- הוסיפי הודעה בסוף לפי הציון!
- ערבבי שאלות מכל הספרים!

## הקוד שלך
פתחי את `exercise_4_quiz.py` והשלימי את שתי הפונקציות
