# Exercise 1: Write From Scratch - Data Processor
#
# These exercises give you minimal guidance. Read the docstring,
# understand what's needed, and implement it yourself.
#
# Theme: Processing data for {{school}}'s administration


# ============================================================
# CHALLENGE A: EASY - Create Student Record
# ============================================================

def create_student(name, house, year=1):
    """
    Create a student record dictionary.

    Args:
        name: Student's name
        house: Student's house
        year: Year of study (default 1)

    Returns:
        dict: Student record with keys: name, house, year, grades

    Examples:
        >>> create_student("{{hero}}", "{{house}}")
        {'name': '{{hero}}', 'house': '{{house}}', 'year': 1, 'grades': {}}
        >>> create_student("{{heroine}}", "{{house}}", 3)
        {'name': '{{heroine}}', 'house': '{{house}}', 'year': 3, 'grades': {}}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE B: EASY - Get Value Safely
# ============================================================

def safe_get(data, key, default=None):
    """
    Get a value from a dictionary with a default if missing.

    Args:
        data: Dictionary to get from
        key: Key to look up
        default: Value to return if key not found

    Returns:
        The value for key, or default if not found

    Examples:
        >>> safe_get({"a": 1}, "a")
        1
        >>> safe_get({"a": 1}, "b")
        None
        >>> safe_get({"a": 1}, "b", 0)
        0
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE C: MEDIUM - Add Grade
# ============================================================

def add_grade(student, subject, score):
    """
    Add a grade to a student's record.

    Args:
        student: Student dict (from create_student)
        subject: Subject name
        score: Grade score

    Returns:
        The updated student dict

    Examples:
        >>> s = create_student("{{hero}}", "{{house}}")
        >>> add_grade(s, "Potions", 85)
        >>> s['grades']
        {'Potions': 85}
        >>> add_grade(s, "Charms", 92)
        >>> s['grades']
        {'Potions': 85, 'Charms': 92}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE D: MEDIUM - Calculate GPA
# ============================================================

def calculate_gpa(student):
    """
    Calculate average grade for a student.

    Args:
        student: Student dict with grades

    Returns:
        float: Average of all grades, or 0.0 if no grades

    Examples:
        >>> s = create_student("{{hero}}", "{{house}}")
        >>> calculate_gpa(s)
        0.0
        >>> add_grade(s, "Potions", 80)
        >>> add_grade(s, "Charms", 90)
        >>> calculate_gpa(s)
        85.0
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE E: MEDIUM - Count by House
# ============================================================

def count_by_house(students):
    """
    Count students in each house.

    Args:
        students: List of student dicts

    Returns:
        dict: House name -> count of students

    Examples:
        >>> students = [
        ...     create_student("{{hero}}", "{{house}}"),
        ...     create_student("{{heroine}}", "{{house}}"),
        ...     create_student("{{friend}}", "Ravenclaw")
        ... ]
        >>> count_by_house(students)
        {'{{house}}': 2, 'Ravenclaw': 1}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE F: HARD - Group by House
# ============================================================

def group_by_house(students):
    """
    Group students by their house.

    Args:
        students: List of student dicts

    Returns:
        dict: House name -> list of student names

    Examples:
        >>> students = [
        ...     create_student("{{hero}}", "{{house}}"),
        ...     create_student("{{heroine}}", "{{house}}"),
        ...     create_student("{{friend}}", "Ravenclaw")
        ... ]
        >>> group_by_house(students)
        {'{{house}}': ['{{hero}}', '{{heroine}}'], 'Ravenclaw': ['{{friend}}']}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE G: HARD - Find Top Students
# ============================================================

def find_top_students(students, n=3):
    """
    Find the top n students by GPA.

    Args:
        students: List of student dicts (with grades)
        n: Number of top students to return

    Returns:
        list: Top n students sorted by GPA (highest first)
              Each item is (name, gpa) tuple

    Examples:
        >>> students = [
        ...     {'name': 'A', 'grades': {'Math': 90}},
        ...     {'name': 'B', 'grades': {'Math': 70}},
        ...     {'name': 'C', 'grades': {'Math': 85}}
        ... ]
        >>> find_top_students(students, 2)
        [('A', 90.0), ('C', 85.0)]
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE H: HARD - Merge Records
# ============================================================

def merge_records(record1, record2):
    """
    Merge two student records, preferring record2 for conflicts.

    Args:
        record1: First student dict
        record2: Second student dict (values take priority)

    Returns:
        dict: Merged record

    Examples:
        >>> r1 = {'name': '{{hero}}', 'year': 1, 'house': '{{house}}'}
        >>> r2 = {'year': 2, 'pet': '{{pet}}'}
        >>> merge_records(r1, r2)
        {'name': '{{hero}}', 'year': 2, 'house': '{{house}}', 'pet': '{{pet}}'}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE I: EXPERT - Nested Update
# ============================================================

def nested_update(data, path, value):
    """
    Update a nested dictionary value using a dot-separated path.

    Args:
        data: Dictionary to update (modified in place)
        path: Dot-separated path like "a.b.c"
        value: Value to set at the path

    Returns:
        The updated dictionary

    Examples:
        >>> d = {'a': {'b': {'c': 1}}}
        >>> nested_update(d, 'a.b.c', 2)
        {'a': {'b': {'c': 2}}}
        >>> d = {'a': 1}
        >>> nested_update(d, 'b.c', 3)
        {'a': 1, 'b': {'c': 3}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Hint: Split the path and traverse/create nested dicts
    pass


# ============================================================
# TESTS
# ============================================================

def run_tests():
    """Test all functions."""
    print("Testing Data Processor functions...\n")

    # Test create_student
    print("A: create_student")
    s = create_student("{{hero}}", "{{house}}")
    assert s["name"] == "{{hero}}"
    assert s["house"] == "{{house}}"
    assert s["year"] == 1
    assert s["grades"] == {}
    print("   ✓ Passed!\n")

    # Test safe_get
    print("B: safe_get")
    assert safe_get({"a": 1}, "a") == 1
    assert safe_get({"a": 1}, "b") is None
    assert safe_get({"a": 1}, "b", 0) == 0
    print("   ✓ Passed!\n")

    # Test add_grade
    print("C: add_grade")
    s = create_student("{{hero}}", "{{house}}")
    add_grade(s, "Potions", 85)
    assert s["grades"]["Potions"] == 85
    print("   ✓ Passed!\n")

    # Test calculate_gpa
    print("D: calculate_gpa")
    s = create_student("{{hero}}", "{{house}}")
    assert calculate_gpa(s) == 0.0
    add_grade(s, "Potions", 80)
    add_grade(s, "Charms", 90)
    assert calculate_gpa(s) == 85.0
    print("   ✓ Passed!\n")

    # Test count_by_house
    print("E: count_by_house")
    students = [
        create_student("A", "{{house}}"),
        create_student("B", "{{house}}"),
        create_student("C", "Ravenclaw")
    ]
    counts = count_by_house(students)
    assert counts["{{house}}"] == 2
    assert counts["Ravenclaw"] == 1
    print("   ✓ Passed!\n")

    # Test group_by_house
    print("F: group_by_house")
    groups = group_by_house(students)
    assert "A" in groups["{{house}}"]
    assert "C" in groups["Ravenclaw"]
    print("   ✓ Passed!\n")

    # Test merge_records
    print("H: merge_records")
    r1 = {"name": "{{hero}}", "year": 1}
    r2 = {"year": 2, "pet": "{{pet}}"}
    merged = merge_records(r1, r2)
    assert merged["name"] == "{{hero}}"
    assert merged["year"] == 2
    assert merged["pet"] == "{{pet}}"
    print("   ✓ Passed!\n")

    print("=" * 40)
    print("All tests passed! 🎉")


def main():
    print("=== Data Processor Challenges ===")
    print()
    print("Implement each function based on its docstring.")
    print("When ready, uncomment run_tests() to check your work.")
    print()

    # Uncomment to run tests:
    # run_tests()


main()
