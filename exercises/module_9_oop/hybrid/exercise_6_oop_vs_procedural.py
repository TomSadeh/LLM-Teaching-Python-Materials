"""
{{CONTEXT_COMPARISON_INTRO}}

This is a multi-part exercise exploring when to use OOP vs procedural
approaches. You'll compare implementations, convert between styles,
and design your own system with justification.

Programming concepts: OOP vs procedural, design decisions, refactoring
"""


# ============================================================
# PART 1: Evaluation - Compare Dict-Based vs Class-Based
# ============================================================
# {{CONTEXT_COMPARISON_DECISION}}
#
# The {{school}} records system has two implementations.


# Version A: Dictionary-based (procedural)


def create_student_dict(name, house, year):
    """Create a student record as a dictionary."""
    return {
        "name": name,
        "house": house,
        "year": year,
        "grades": {},
        "attendance": 0
    }


def add_grade_dict(student, subject, grade):
    """Add a grade to a student dictionary."""
    student["grades"][subject] = grade


def record_attendance_dict(student):
    """Increment attendance for a student dictionary."""
    student["attendance"] += 1


def get_average_grade_dict(student):
    """Calculate average grade for a student dictionary."""
    grades = student["grades"].values()
    if not grades:
        return 0
    return sum(grades) / len(grades)


def promote_student_dict(student):
    """Promote student to next year."""
    student["year"] += 1


# Version B: Class-based (OOP)


class Student:
    """A student at {{school}}."""

    def __init__(self, name, house, year):
        self.name = name
        self.house = house
        self.year = year
        self.grades = {}
        self.attendance = 0

    def add_grade(self, subject, grade):
        """Add a grade for a subject."""
        self.grades[subject] = grade

    def record_attendance(self):
        """Increment attendance count."""
        self.attendance += 1

    def get_average_grade(self):
        """Calculate average grade."""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def promote(self):
        """Promote to next year."""
        self.year += 1


def part1_compare():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # Test both versions:
    #
    #     # Dict version
    #     s1 = create_student_dict("{{hero}}", "{{house}}", 1)
    #     add_grade_dict(s1, "{{spell1}}", 90)
    #     add_grade_dict(s1, "{{spell2}}", 85)
    #     record_attendance_dict(s1)
    #     print(f"Dict avg: {get_average_grade_dict(s1)}")
    #
    #     # Class version
    #     s2 = Student("{{hero}}", "{{house}}", 1)
    #     s2.add_grade("{{spell1}}", 90)
    #     s2.add_grade("{{spell2}}", 85)
    #     s2.record_attendance()
    #     print(f"Class avg: {s2.get_average_grade()}")
    #
    # Write your comparison:

    analysis = """
    Comparison:

    Dict version calling style:
        add_grade_dict(student, subject, grade)

    Class version calling style:
        student.add_grade(subject, grade)

    Which is more intuitive?
    -

    Which is easier to get wrong (e.g., pass wrong data)?
    -

    Which would be easier to extend with new features?
    -
    """
    return analysis


# ============================================================
# PART 2: Growth - Convert Procedural to OOP
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Convert this procedural inventory system to OOP.


# Procedural version to convert


def create_inventory(name, max_slots):
    return {"name": name, "max_slots": max_slots, "items": [], "gold": 0}


def add_item(inventory, item_name, item_value):
    if len(inventory["items"]) < inventory["max_slots"]:
        inventory["items"].append({"name": item_name, "value": item_value})
        return True
    return False


def remove_item(inventory, item_name):
    for i, item in enumerate(inventory["items"]):
        if item["name"] == item_name:
            inventory["items"].pop(i)
            return True
    return False


def get_total_value(inventory):
    total = inventory["gold"]
    for item in inventory["items"]:
        total += item["value"]
    return total


def display_inventory(inventory):
    print(f"=== {inventory['name']}'s Inventory ===")
    print(f"Slots: {len(inventory['items'])}/{inventory['max_slots']}")
    for item in inventory["items"]:
        print(f"  - {item['name']} ({item['value']} gold)")
    print(f"Gold: {inventory['gold']}")
    print(f"Total value: {get_total_value(inventory)}")


def part2_convert_to_oop():
    # ✏️ CONVERT TO OOP ✏️
    #
    # Create an Inventory class and Item class that replicate this functionality.
    #
    # class Item:
    #     def __init__(self, name, value):
    #         pass
    #
    # class Inventory:
    #     def __init__(self, owner_name, max_slots):
    #         pass
    #
    #     def add_item(self, item):
    #         pass
    #
    #     def remove_item(self, item_name):
    #         pass
    #
    #     def get_total_value(self):
    #         pass
    #
    #     def __str__(self):
    #         pass
    #
    # Test your conversion:
    #     inv = Inventory("{{hero}}", 5)
    #     inv.add_item(Item("{{item}}", 100))
    #     inv.add_item(Item("{{spell1}}", 50))
    #     inv.gold = 200
    #     print(inv)
    #     print(f"Total value: {inv.get_total_value()}")

    pass


# ============================================================
# PART 3: Ownership - Design Your Own System
# ============================================================
# {{CONTEXT_MASTERY_INTRO}}
# {{CONTEXT_MASTERY_NARRATIVE}}
#
# Design a quest tracking system. You choose the approach!


def part3_design_system():
    # ✏️ DESIGN YOUR OWN SYSTEM ✏️
    #
    # Requirements for Quest Tracking System:
    # - Track quest name, description, and status (active/completed)
    # - Track rewards (experience points, gold, items)
    # - Support multiple objectives per quest
    # - Track progress on each objective
    # - Mark quest complete when all objectives are done
    #
    # Decision: Will you use OOP or procedural?
    #
    # If OOP, consider these classes:
    # - Quest (name, description, status, objectives, rewards)
    # - Objective (description, current_progress, target_progress)
    # - QuestLog (collection of quests, active/completed filtering)
    #
    # If procedural, consider these functions:
    # - create_quest, add_objective, update_progress
    # - check_completion, get_active_quests, etc.
    #
    # Implement your chosen approach and justify your decision:

    justification = """
    I chose: ??? (OOP / Procedural)

    Reasons:
    1.
    2.
    3.

    This approach is better for this problem because:
    -
    """

    # Your implementation here:
    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_COMPARISON_INTRO}}")
    print("OOP vs Procedural Design")
    print("=" * 60)
    print()

    print(">>> PART 1: Compare Dict vs Class")
    print()

    # Dict version
    s_dict = create_student_dict("{{hero}}", "{{house}}", 1)
    add_grade_dict(s_dict, "{{spell1}}", 90)
    add_grade_dict(s_dict, "{{spell2}}", 85)
    print(f"Dict approach - Avg grade: {get_average_grade_dict(s_dict)}")

    # Class version
    s_class = Student("{{hero}}", "{{house}}", 1)
    s_class.add_grade("{{spell1}}", 90)
    s_class.add_grade("{{spell2}}", 85)
    print(f"Class approach - Avg grade: {s_class.get_average_grade()}")

    print()
    print("Your analysis:")
    print(part1_compare())
    print()

    print(">>> PART 2: Convert Procedural to OOP")
    print()
    print("Procedural version:")
    inv = create_inventory("{{hero}}", 5)
    add_item(inv, "{{item}}", 100)
    add_item(inv, "{{spell1}}", 50)
    inv["gold"] = 200
    display_inventory(inv)
    print()
    print("Convert to OOP:")
    part2_convert_to_oop()
    print()

    print(">>> PART 3: Design Your Own Quest System")
    print("(Choose OOP or procedural and justify)")
    part3_design_system()

    print()
    print("=" * 60)
    print("{{CONTEXT_EVALUATION_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
