"""
{{CONTEXT_PROJECT_INTRO}}

CAPSTONE PROJECT: Design and build a complete management system for {{school}}
using OOP principles. This exercise integrates all Module 9 concepts.

Programming concepts: class design, inheritance, composition, encapsulation
"""


# ============================================================
# PART 1: Growth - Design the Core Class Hierarchy
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# Design the foundational classes for the system.


def part1_core_classes():
    # ✏️ DESIGN THE CORE CLASSES ✏️
    #
    # Base class: Person
    #     - name (string)
    #     - age (integer)
    #     - id_number (unique identifier)
    #     - get_info() -> returns formatted info string
    #     - __str__ -> returns name and role
    #
    # Subclass: Student(Person)
    #     - house (string, e.g., "{{house}}")
    #     - year (integer, 1-7)
    #     - grades (dict: subject -> grade)
    #     - add_grade(subject, grade)
    #     - get_average() -> average of all grades
    #     - promote() -> increment year (max 7)
    #     - Override get_info() to include house and year
    #
    # Subclass: Teacher(Person)
    #     - subject (string, what they teach)
    #     - years_experience (integer)
    #     - students (list of Student objects they teach)
    #     - add_student(student)
    #     - grade_student(student, grade)
    #     - get_class_average() -> average of all students' grades in subject
    #     - Override get_info() to include subject
    #
    # Test:
    #     student = Student("{{hero}}", 11, "S001", "{{house}}", 1)
    #     teacher = Teacher("{{mentor}}", 45, "T001", "{{spell1}}", 20)
    #     teacher.add_student(student)
    #     teacher.grade_student(student, 95)
    #     print(student.get_info())
    #     print(teacher.get_info())

    pass


# ============================================================
# PART 2: Growth - Implement Course Management
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# Create classes to manage courses and enrollment.


def part2_course_management():
    # ✏️ IMPLEMENT COURSE MANAGEMENT ✏️
    #
    # class Course:
    #     """A course offered at {{school}}."""
    #
    #     def __init__(self, name, teacher, max_students=30):
    #         self.name = name
    #         self.teacher = teacher  # Teacher object
    #         self.max_students = max_students
    #         self.enrolled_students = []  # List of Student objects
    #         self.schedule = {}  # day -> time
    #
    #     def enroll_student(self, student):
    #         """Add student if not full and not already enrolled."""
    #         # Return True if enrolled, False otherwise
    #         pass
    #
    #     def drop_student(self, student):
    #         """Remove student from course."""
    #         pass
    #
    #     def set_schedule(self, day, time):
    #         """Set when the course meets."""
    #         pass
    #
    #     def get_roster(self):
    #         """Return list of enrolled student names."""
    #         pass
    #
    #     def is_full(self):
    #         """Check if course is at capacity."""
    #         pass
    #
    #     def __str__(self):
    #         """Return course summary."""
    #         pass
    #
    # Test:
    #     teacher = Teacher("{{mentor}}", 45, "T001", "{{spell1}}", 20)
    #     course = Course("{{spell1}} 101", teacher, max_students=5)
    #     student1 = Student("{{hero}}", 11, "S001", "{{house}}", 1)
    #     student2 = Student("{{heroine}}", 11, "S002", "{{house}}", 1)
    #     course.enroll_student(student1)
    #     course.enroll_student(student2)
    #     print(course)
    #     print(f"Roster: {course.get_roster()}")

    pass


# ============================================================
# PART 3: Growth - Add Inheritance for Specialization
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# Create specialized subclasses for different types of people and courses.


def part3_specialization():
    # ✏️ ADD SPECIALIZED SUBCLASSES ✏️
    #
    # class Prefect(Student):
    #     """A student with leadership responsibilities."""
    #
    #     def __init__(self, name, age, id_number, house, year):
    #         super().__init__(name, age, id_number, house, year)
    #         self.duties = []  # List of duty assignments
    #         self.points_awarded = 0  # Points given to house
    #
    #     def assign_duty(self, duty):
    #         """Add a duty to the prefect's responsibilities."""
    #         pass
    #
    #     def award_points(self, amount, reason):
    #         """Award points to house. Track total awarded."""
    #         # Print: "[name] awards [amount] points to [house]: [reason]"
    #         pass
    #
    #     def get_info(self):
    #         """Override to include prefect status."""
    #         pass
    #
    # class HeadTeacher(Teacher):
    #     """A teacher who heads a department."""
    #
    #     def __init__(self, name, age, id_number, subject, years_experience, department):
    #         super().__init__(name, age, id_number, subject, years_experience)
    #         self.department = department
    #         self.department_teachers = []
    #
    #     def add_department_teacher(self, teacher):
    #         """Add a teacher to the department."""
    #         pass
    #
    #     def get_department_stats(self):
    #         """Return department summary."""
    #         pass
    #
    # class AdvancedCourse(Course):
    #     """A course with prerequisites."""
    #
    #     def __init__(self, name, teacher, max_students, prerequisites):
    #         super().__init__(name, teacher, max_students)
    #         self.prerequisites = prerequisites  # List of course names
    #
    #     def check_prerequisites(self, student):
    #         """Check if student has completed all prerequisites."""
    #         # Assume student has completed_courses list
    #         pass
    #
    #     def enroll_student(self, student):
    #         """Override to check prerequisites first."""
    #         pass
    #
    # Test:
    #     prefect = Prefect("{{hero}}", 16, "S001", "{{house}}", 5)
    #     prefect.assign_duty("Night patrol")
    #     prefect.award_points(10, "Helping first years")
    #     print(prefect.get_info())

    pass


# ============================================================
# PART 4: Improvement - Ensure Code Quality
# ============================================================
# {{CONTEXT_PHASE_4}}
#
# Review and improve the code for production quality.


def part4_code_quality():
    # ✏️ CODE QUALITY REVIEW ✏️
    #
    # Review your classes and ensure:
    #
    # 1. NAMING:
    #    - All class names are PascalCase
    #    - All methods and attributes are snake_case
    #    - Names are descriptive and clear
    #
    # 2. DOCUMENTATION:
    #    - Every class has a docstring explaining its purpose
    #    - Every method has a docstring with Args and Returns
    #    - Complex logic has inline comments
    #
    # 3. ENCAPSULATION:
    #    - Data is accessed/modified through methods when appropriate
    #    - Invalid operations are handled gracefully
    #    - Methods validate their inputs
    #
    # 4. ERROR HANDLING:
    #    - What happens if you try to enroll in a full course?
    #    - What if you try to grade a student not in your class?
    #    - What if you promote a 7th year student?
    #
    # Add input validation and error handling to your classes.
    #
    # Example improvements:
    #
    # def enroll_student(self, student):
    #     """Enroll a student in this course.
    #
    #     Args:
    #         student: Student object to enroll
    #
    #     Returns:
    #         bool: True if enrolled successfully
    #
    #     Raises:
    #         ValueError: If student is None or already enrolled
    #     """
    #     if student is None:
    #         raise ValueError("Cannot enroll None as student")
    #     if student in self.enrolled_students:
    #         return False  # Already enrolled
    #     if self.is_full():
    #         return False  # Course full
    #     self.enrolled_students.append(student)
    #     return True

    pass


# ============================================================
# PART 5: Ownership - Extend With Your Own Feature
# ============================================================
# {{CONTEXT_MASTERY_INTRO}}
# {{CONTEXT_MASTERY_NARRATIVE}}
#
# Add your own feature to the management system.


def part5_extend_system():
    # ✏️ EXTEND THE SYSTEM ✏️
    #
    # Add a significant feature of your choice. Ideas:
    #
    # 1. House Points System:
    #    - Track points for each house
    #    - Teachers and prefects can award/deduct points
    #    - Get current standings
    #
    # 2. Event System:
    #    - Create events (quidditch match, feast, exam)
    #    - Students/teachers can attend
    #    - Track participation
    #
    # 3. Grading System Enhancement:
    #    - Track grades over time
    #    - Calculate GPA
    #    - Generate report cards
    #
    # 4. Scheduling System:
    #    - Detect schedule conflicts
    #    - Generate student timetables
    #    - Room booking
    #
    # 5. Library System:
    #    - Books that can be borrowed
    #    - Due dates and late fees
    #    - Reserved section for advanced students
    #
    # Requirements for your feature:
    # - At least 1 new class
    # - Must interact with existing classes (Person, Course, etc.)
    # - Include comprehensive testing
    # - Document your design decisions
    #
    # Demonstrate your feature in action:

    pass


# ============================================================
# MAIN
# ============================================================

def main():
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


if __name__ == "__main__":
    main()
