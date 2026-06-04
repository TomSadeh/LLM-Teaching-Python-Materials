# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# ## פרויקט גמר: עצבי ובני מערכת ניהול מלאה עבור {{school}}
# ## תוך שימוש בעקרונות תכנות מונחה עצמים. תרגיל זה משלב את כל מושגי יחידה 9.
#
# מושגי תכנות: עיצוב מחלקות, ירושה, קומפוזיציה, אנקפסולציה
#
# ## חלק 1: צמיחה - עצבי את היררכיית המחלקות הבסיסית
# {{CONTEXT_PHASE_1}}
#
# עצבי את המחלקות הבסיסיות של המערכת.
#
# מחלקת בסיס: `Person`
#     - `name` (מחרוזת)
#     - `age` (מספר שלם)
#     - `id_number` (מזהה ייחודי)
#     - `get_info()` -> מחזירה מחרוזת מידע מעוצבת
#     - `__str__` -> מחזירה שם ותפקיד
#
# תת-מחלקה: `Student(Person)`
#     - `house` (מחרוזת, למשל `"{{house}}"`)
#     - `year` (מספר שלם, 1-7)
#     - `grades` (מילון: מקצוע -> ציון)
#     - `add_grade(subject, grade)`
#     - `get_average()` -> ממוצע כל הציונים
#     - `promote()` -> מעלה שנה (מקסימום 7)
#     - דרסי את `get_info()` כך שתכלול בית ושנה
#
# תת-מחלקה: `Teacher(Person)`
#     - `subject` (מחרוזת, המקצוע שמלמדת)
#     - `years_experience` (מספר שלם)
#     - `students` (רשימת אובייקטי `Student` שמלמדת)
#     - `add_student(student)`
#     - `grade_student(student, grade)`
#     - `get_class_average()` -> ממוצע ציוני כל התלמידות במקצוע
#     - דרסי את `get_info()` כך שתכלול את המקצוע
#
# בדיקה:
#     student = Student("{{hero}}", 11, "S001", "{{house}}", 1)
#     teacher = Teacher("{{mentor}}", 45, "T001", "{{spell1}}", 20)
#     teacher.add_student(student)
#     teacher.grade_student(student, 95)
#     print(student.get_info())
#     print(teacher.get_info())

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - ממשי ניהול קורסים
# {{CONTEXT_PHASE_2}}
#
# צרי מחלקות לניהול קורסים ורישום תלמידות.
#
# class Course:
#     """קורס המוצע ב-{{school}}."""
#
#     def __init__(self, name, teacher, max_students=30):
#         self.name = name
#         self.teacher = teacher  # אובייקט Teacher
#         self.max_students = max_students
#         self.enrolled_students = []  # רשימת אובייקטי Student
#         self.schedule = {}  # יום -> שעה
#
#     def enroll_student(self, student):
#         """רישום תלמידה אם הקורס לא מלא ואם היא עוד לא רשומה."""
#         # החזירי True אם נרשמה, False אחרת
#         pass
#
#     def drop_student(self, student):
#         """הסירי תלמידה מהקורס."""
#         pass
#
#     def set_schedule(self, day, time):
#         """קבעי מתי הקורס מתקיים."""
#         pass
#
#     def get_roster(self):
#         """החזירי רשימת שמות התלמידות הרשומות."""
#         pass
#
#     def is_full(self):
#         """בדקי אם הקורס מלא."""
#         pass
#
#     def __str__(self):
#         """החזירי סיכום הקורס."""
#         pass
#
# בדיקה:
#     teacher = Teacher("{{mentor}}", 45, "T001", "{{spell1}}", 20)
#     course = Course("{{spell1}} 101", teacher, max_students=5)
#     student1 = Student("{{hero}}", 11, "S001", "{{house}}", 1)
#     student2 = Student("{{heroine}}", 11, "S002", "{{house}}", 1)
#     course.enroll_student(student1)
#     course.enroll_student(student2)
#     print(course)
#     print(f"Roster: {course.get_roster()}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - הוסיפי ירושה להתמחות
# {{CONTEXT_PHASE_3}}
#
# צרי תת-מחלקות מתמחות לסוגים שונים של אנשים וקורסים.
#
# class Prefect(Student):
#     """תלמידה עם אחריות מנהיגותית."""
#
#     def __init__(self, name, age, id_number, house, year):
#         super().__init__(name, age, id_number, house, year)
#         self.duties = []  # רשימת תפקידים
#         self.points_awarded = 0  # נקודות שניתנו לבית
#
#     def assign_duty(self, duty):
#         """הוסיפי תפקיד לאחריות הפרפקטית."""
#         pass
#
#     def award_points(self, amount, reason):
#         """הענקי נקודות לבית. עקבי אחר הסך הכולל."""
#         # הדפיסי: "[name] awards [amount] points to [house]: [reason]"
#         pass
#
#     def get_info(self):
#         """דרסי כך שתכלול סטטוס פרפקטית."""
#         pass
#
# class HeadTeacher(Teacher):
#     """מורה שעומדת בראש מחלקה."""
#
#     def __init__(self, name, age, id_number, subject, years_experience, department):
#         super().__init__(name, age, id_number, subject, years_experience)
#         self.department = department
#         self.department_teachers = []
#
#     def add_department_teacher(self, teacher):
#         """הוסיפי מורה למחלקה."""
#         pass
#
#     def get_department_stats(self):
#         """החזירי סיכום המחלקה."""
#         pass
#
# class AdvancedCourse(Course):
#     """קורס עם דרישות קדם."""
#
#     def __init__(self, name, teacher, max_students, prerequisites):
#         super().__init__(name, teacher, max_students)
#         self.prerequisites = prerequisites  # רשימת שמות קורסים
#
#     def check_prerequisites(self, student):
#         """בדקי אם התלמידה השלימה את כל דרישות הקדם."""
#         # הניחי שלתלמידה יש רשימת completed_courses
#         pass
#
#     def enroll_student(self, student):
#         """דרסי כדי לבדוק דרישות קדם תחילה."""
#         pass
#
# בדיקה:
#     prefect = Prefect("{{hero}}", 16, "S001", "{{house}}", 5)
#     prefect.assign_duty("Night patrol")
#     prefect.award_points(10, "Helping first years")
#     print(prefect.get_info())

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: שיפור - ודאי איכות קוד
# {{CONTEXT_PHASE_4}}
#
# סקרי ושפרי את הקוד לאיכות גבוהה.
#
# עברי על המחלקות שלך וודאי:
#
# 1. שמות:
#    - כל שמות המחלקות הם PascalCase
#    - כל שמות המתודות והתכונות הם snake_case
#    - השמות ברורים ותיאוריים
#
# 2. תיעוד:
#    - לכל מחלקה יש docstring המסביר את מטרתה
#    - לכל מתודה יש docstring עם Args ו-Returns
#    - לוגיקה מורכבת מלווה בהערות
#
# 3. אנקפסולציה:
#    - גישה לנתונים ושינוים דרך מתודות כשמתאים
#    - פעולות לא חוקיות מטופלות בצורה נאותה
#    - מתודות מאמתות את הקלטים שלהן
#
# 4. טיפול בשגיאות:
#    - מה קורה אם מנסים להירשם לקורס מלא?
#    - מה אם מנסים לתת ציון לתלמידה שלא בכיתה?
#    - מה אם מנסים לקדם תלמידת שנה 7?
#
# הוסיפי ולידציה וטיפול בשגיאות למחלקות שלך.
#
# דוגמה לשיפורים:
#
# def enroll_student(self, student):
#     """רישום תלמידה לקורס זה.
#
#     Args:
#         student: אובייקט Student לרישום
#
#     Returns:
#         bool: True אם נרשמה בהצלחה
#
#     Raises:
#         ValueError: אם student הוא None או כבר רשומה
#     """
#     if student is None:
#         raise ValueError("Cannot enroll None as student")
#     if student in self.enrolled_students:
#         return False  # Already enrolled
#     if self.is_full():
#         return False  # Course full
#     self.enrolled_students.append(student)
#     return True

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 5: בעלות - הרחיבי עם תכונה משלך
# {{CONTEXT_MASTERY_INTRO}}
# {{CONTEXT_MASTERY_NARRATIVE}}
#
# הוסיפי תכונה משלך למערכת הניהול.
#
# הוסיפי תכונה משמעותית לבחירתך. רעיונות:
#
# 1. מערכת נקודות הבתים:
#    - עקבי אחר נקודות לכל בית
#    - מורות ופרפקטיות יכולות להעניק/להפחית נקודות
#    - הצגי את הדירוג הנוכחי
#
# 2. מערכת אירועים:
#    - צרי אירועים (משחק קווידיץ', משתה, מבחן)
#    - תלמידות ומורות יכולות להשתתף
#    - עקבי אחר ההשתתפות
#
# 3. שיפור מערכת הציונים:
#    - עקבי אחר ציונים לאורך זמן
#    - חשבי ממוצע כולל (GPA)
#    - צרי תעודות
#
# 4. מערכת לוח זמנים:
#    - גלי התנגשויות בלוח הזמנים
#    - צרי מערכות שעות לתלמידות
#    - הזמנת חדרים
#
# 5. מערכת ספרייה:
#    - ספרים שניתן להשאיל
#    - תאריכי החזרה וקנסות איחור
#    - מדור שמור לתלמידות מתקדמות
#
# דרישות לתכונה שלך:
# - לפחות מחלקה חדשה אחת
# - חייבת לתקשר עם המחלקות הקיימות (`Person`, `Course` וכד')
# - כללי בדיקות מקיפות
# - תעדי את החלטות העיצוב שלך
#
# הדגימי את התכונה שלך בפעולה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("{{school}} Management System - Capstone Project")
print("=" * 60)
print()

print(">>> PART 1: Core Class Hierarchy")
print("(Design Person, Student, Teacher)")
part1_core_classes()
print()

print(">>> PART 2: Course Management")
print("(Implement enrollment and scheduling)")
part2_course_management()
print()

print(">>> PART 3: Specialization")
print("(Add Prefect, HeadTeacher, AdvancedCourse)")
part3_specialization()
print()

print(">>> PART 4: Code Quality")
print("(Add validation, error handling, documentation)")
part4_code_quality()
print()

print(">>> PART 5: Your Feature")
print("(Extend the system with your own idea)")
part5_extend_system()

print()
print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("Congratulations on completing the OOP module!")
print("=" * 60)
