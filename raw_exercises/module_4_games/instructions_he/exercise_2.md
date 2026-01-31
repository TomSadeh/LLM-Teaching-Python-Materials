# תרגיל 2: אבן, נייר, מספריים ✊✋✌️

## המשימה שלך
השלימי את הפונקציה שקובעת מי ניצח!

## הכללים
- אבן (rock) מנצחת מספריים (scissors)
- מספריים (scissors) מנצחות נייר (paper)
- נייר (paper) מנצח אבן (rock)
- אותו דבר = תיקו

## מה להחזיר
- `"tie"` אם שניהם בחרו אותו דבר
- `"player"` אם השחקן ניצח
- `"computer"` אם המחשב ניצח

## רמז
בדקי תיקו קודם, ואז בדקי את כל המקרים שהשחקן מנצח:
```python
if player == computer:
    return "tie"

if player == "rock" and computer == "scissors":
    return "player"

# add more...
```

## בונוס
הוסיפי לולאה כדי לשחק כמה סיבובים ולספור נקודות!

## הקוד שלך
פתחי את `exercise_2_rock_paper_scissors.py` ומלאי את `get_winner`
