# שיעור: יסודות פייתון

> **מודול**: module_0_basics
> **חלקים**: 6 (חלק 0-5)
> **רמת קושי**: 1-2
> **משך כולל**: 20-30 דקות

---

## סקירה

מודול התכנות הראשון. מבסס מיומנויות יסוד וגישה של ניסוי וטעייה.

---

## מטרות למידה

בסיום המודול, התלמיד/ה יוכל/תוכל:

1. להשתמש ב-`print()` להצגת טקסט על המסך
2. ליצור משתנים לאחסון טקסט ומספרים
3. לבצע פעולות חשבון בסיסיות (+, -, *, /)
4. לקבל קלט מהמשתמש עם `input()` ולהמיר טיפוסים עם `int()`
5. לשלב משתנים וטקסט באמצעות f-strings

---

## חלקים

| חלק | נושא | משך | מושג מרכזי |
|-----|------|-----|------------|
| 0 | ברוכים הבאים לתכנות | 2-3 דק׳ | גישה, ציפיות |
| 1 | Hello World עם print() | 3-5 דק׳ | `print()`, מחרוזות |
| 2 | משתנים | 3-5 דק׳ | השמה, שימוש במשתנים |
| 3 | פעולות חשבון | 3-5 דק׳ | אופרטורים, מספרים שלמים |
| 4 | קלט מהמשתמש | 3-5 דק׳ | `input()`, `int()` |
| 5 | מחברים הכל יחד | 5-7 דק׳ | f-strings, שילוב מיומנויות |

---

## מהלך התרגילים

### דפוס התקדמות
כל חלק עוקב אחר: **צפייה ← תרגול ← יצירה ← דיבאג**

ראו [learning-science.md](../../references/pedagogy/learning-science.md) לרציונל.

### רצף תרגילים

| חלק | צפייה | תרגול | יצירה | דיבאג |
|-----|-------|-------|-------|-------|
| 1 | `output_prediction/ex1_print_basics` | - | `write_code/ex1_hello` | - |
| 2 | (חלק מ-ex1_print_basics) | `fill_blanks/ex1_variables` | `write_code/ex2_variables` | `spot_difference/ex1_variable_errors` |
| 3 | `output_prediction/ex2_arithmetic` | `code_ordering/ex1_program_flow` | `write_code/ex3_calculator` | `decode_error/ex1_string_errors` |
| 4 | (הדגמה חיה) | `fill_blanks/ex2_input` | `write_code/ex5_input` | `decode_error/ex2_input_errors` |
| 5 | `match_output/ex1_string_output` | `complete_function/ex1_format_output` | `write_code/ex4_strings`, `ex6_fstrings` | `bug_hunt/ex1_basics_bugs` |

### תרגילי סיכום

| אחרי חלק | תרגיל היברידי |
|----------|---------------|
| חלק 2 | `hybrid/exercise_1_apprentice_variables` |
| חלק 5 | `hybrid/exercise_2_apprentice_program` (סיכום מודול) |

---

## סיכום מושגים מרכזיים

| מושג | מוצג ב- | הסבר |
|------|---------|------|
| `print()` | חלק 1 | הצגת פלט |
| מחרוזת | חלק 1 | טקסט במרכאות |
| משתנה | חלק 2 | אחסון עם שם |
| השמה (`=`) | חלק 2 | שמירת ערך |
| מספר שלם | חלק 3 | מספר ללא נקודה עשרונית |
| אופרטורים | חלק 3 | `+`, `-`, `*`, `/` |
| `input()` | חלק 4 | קבלת טקסט מהמשתמש |
| `int()` | חלק 4 | המרה למספר |
| f-string | חלק 5 | עיצוב עם `f"{}"` |

---

## תפיסות שגויות נפוצות

| תפיסה שגויה | המציאות | חלק |
|-------------|---------|-----|
| שכחת מרכאות סביב מחרוזות | בלי מרכאות, פייתון מחפש משתנה | 1 |
| `print("name")` מציג ערך משתנה | מרכאות הופכות לטקסט מילולי | 2 |
| `input()` מחזיר מספרים | תמיד מחזיר מחרוזת, צריך `int()` | 4 |
| `=` משווה ערכים | `=` משים ערך, `==` משווה (בהמשך) | 2 |

---

## הפניות

- [learning-science.md](../../references/pedagogy/learning-science.md)
- [common-struggles.md](../../references/pedagogy/common-struggles.md)
- [exercise-types.md](../../references/pedagogy/exercise-types.md)
