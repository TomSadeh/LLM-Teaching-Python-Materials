# Exercise 1: Write From Scratch - Mini App
#
# Build a complete mini application from scratch.
# You're given only the specifications - the implementation is up to you!
#
# Theme: {{hero}}'s Personal Assistant App


# ============================================================
# THE CHALLENGE: Build a Task Manager
# ============================================================
#
# Create a simple task manager with these features:
# 1. Add tasks
# 2. View all tasks
# 3. Mark tasks complete
# 4. Remove completed tasks
# 5. Save/load tasks (bonus)
#
# You need to implement ALL the functions below.
# The main() function shows how they should work together.


def create_task_manager():
    """
    Create and return a new empty task manager.

    Returns:
        dict: A task manager with structure:
            {
                "tasks": [],  # List of task dicts
                "next_id": 1  # ID to assign to next task
            }

    Each task should have:
        - id: unique number
        - description: what to do
        - completed: True/False
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def add_task(manager, description):
    """
    Add a new task to the manager.

    Args:
        manager: The task manager dict
        description: What the task is

    Returns:
        int: The ID of the newly created task

    Example:
        >>> tm = create_task_manager()
        >>> add_task(tm, "Learn Python")
        1
        >>> add_task(tm, "Practice spells")
        2
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_all_tasks(manager):
    """
    Get all tasks from the manager.

    Args:
        manager: The task manager dict

    Returns:
        list: List of all task dicts

    Example:
        >>> tm = create_task_manager()
        >>> add_task(tm, "Task 1")
        >>> get_all_tasks(tm)
        [{'id': 1, 'description': 'Task 1', 'completed': False}]
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_pending_tasks(manager):
    """
    Get only incomplete tasks.

    Args:
        manager: The task manager dict

    Returns:
        list: List of task dicts where completed is False
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_completed_tasks(manager):
    """
    Get only completed tasks.

    Args:
        manager: The task manager dict

    Returns:
        list: List of task dicts where completed is True
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def complete_task(manager, task_id):
    """
    Mark a task as completed.

    Args:
        manager: The task manager dict
        task_id: ID of task to complete

    Returns:
        bool: True if task was found and completed, False otherwise

    Example:
        >>> tm = create_task_manager()
        >>> add_task(tm, "Learn Python")
        >>> complete_task(tm, 1)
        True
        >>> complete_task(tm, 999)  # Doesn't exist
        False
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def remove_task(manager, task_id):
    """
    Remove a task by ID.

    Args:
        manager: The task manager dict
        task_id: ID of task to remove

    Returns:
        bool: True if task was found and removed, False otherwise
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def clear_completed(manager):
    """
    Remove all completed tasks.

    Args:
        manager: The task manager dict

    Returns:
        int: Number of tasks removed
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def format_task(task):
    """
    Format a task for display.

    Args:
        task: A task dict

    Returns:
        str: Formatted string like "[X] 1. Description" or "[ ] 1. Description"

    Example:
        >>> format_task({'id': 1, 'description': 'Test', 'completed': True})
        '[X] 1. Test'
        >>> format_task({'id': 2, 'description': 'Test', 'completed': False})
        '[ ] 2. Test'
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def display_tasks(manager, show_completed=True):
    """
    Display all tasks nicely formatted.

    Args:
        manager: The task manager dict
        show_completed: If False, only show pending tasks

    Prints tasks in format:
        === Your Tasks ===
        [ ] 1. First task
        [X] 2. Completed task
        ==================
        Pending: 1 | Completed: 1
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# BONUS CHALLENGES (Optional)
# ============================================================

def save_tasks(manager, filename):
    """
    Save tasks to a JSON file.

    Args:
        manager: The task manager dict
        filename: Path to save to

    Returns:
        bool: True if saved successfully
    """
    # ✏️ BONUS: YOUR CODE HERE ✏️
    pass


def load_tasks(filename):
    """
    Load tasks from a JSON file.

    Args:
        filename: Path to load from

    Returns:
        dict: The loaded task manager, or new empty one if file doesn't exist
    """
    # ✏️ BONUS: YOUR CODE HERE ✏️
    pass


# ============================================================
# INTERACTIVE MODE
# ============================================================

def run_interactive():
    """Run the task manager interactively."""
    print("=" * 40)
    print(f"  {{hero}}'s Task Manager")
    print("=" * 40)

    manager = create_task_manager()

    while True:
        print("\nOptions:")
        print("  1. Add task")
        print("  2. View all tasks")
        print("  3. Complete a task")
        print("  4. Remove a task")
        print("  5. Clear completed")
        print("  6. Quit")

        choice = input("\nChoice (1-6): ").strip()

        if choice == "1":
            desc = input("Task description: ").strip()
            if desc:
                task_id = add_task(manager, desc)
                print(f"Added task #{task_id}")

        elif choice == "2":
            display_tasks(manager)

        elif choice == "3":
            display_tasks(manager)
            try:
                task_id = int(input("Task ID to complete: "))
                if complete_task(manager, task_id):
                    print("Task completed!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a number.")

        elif choice == "4":
            display_tasks(manager)
            try:
                task_id = int(input("Task ID to remove: "))
                if remove_task(manager, task_id):
                    print("Task removed!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a number.")

        elif choice == "5":
            count = clear_completed(manager)
            print(f"Removed {count} completed task(s).")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try 1-6.")


# ============================================================
# TESTS
# ============================================================

def run_tests():
    """Test all task manager functions."""
    print("Testing Task Manager...\n")

    # Test create_task_manager
    print("Testing create_task_manager...")
    tm = create_task_manager()
    assert "tasks" in tm, "Manager should have 'tasks' key"
    assert "next_id" in tm, "Manager should have 'next_id' key"
    assert tm["tasks"] == [], "Tasks should start empty"
    print("   ✓ Passed!\n")

    # Test add_task
    print("Testing add_task...")
    id1 = add_task(tm, "Learn Python")
    id2 = add_task(tm, "Practice spells")
    assert id1 == 1, "First task should have ID 1"
    assert id2 == 2, "Second task should have ID 2"
    assert len(tm["tasks"]) == 2, "Should have 2 tasks"
    print("   ✓ Passed!\n")

    # Test get_all_tasks
    print("Testing get_all_tasks...")
    tasks = get_all_tasks(tm)
    assert len(tasks) == 2, "Should return all tasks"
    print("   ✓ Passed!\n")

    # Test complete_task
    print("Testing complete_task...")
    assert complete_task(tm, 1) == True, "Should complete existing task"
    assert complete_task(tm, 999) == False, "Should return False for missing task"
    assert tm["tasks"][0]["completed"] == True, "Task should be marked complete"
    print("   ✓ Passed!\n")

    # Test get_pending_tasks and get_completed_tasks
    print("Testing get_pending_tasks and get_completed_tasks...")
    pending = get_pending_tasks(tm)
    completed = get_completed_tasks(tm)
    assert len(pending) == 1, "Should have 1 pending task"
    assert len(completed) == 1, "Should have 1 completed task"
    print("   ✓ Passed!\n")

    # Test remove_task
    print("Testing remove_task...")
    assert remove_task(tm, 2) == True, "Should remove existing task"
    assert len(tm["tasks"]) == 1, "Should have 1 task left"
    print("   ✓ Passed!\n")

    # Test clear_completed
    print("Testing clear_completed...")
    add_task(tm, "Another task")
    complete_task(tm, 1)
    count = clear_completed(tm)
    assert count == 1, "Should clear 1 completed task"
    print("   ✓ Passed!\n")

    print("=" * 40)
    print("All tests passed! 🎉")


def main():
    print("=== {{hero}}'s Task Manager ===")
    print()
    print("First, implement all the functions above.")
    print("Then uncomment one of the lines below:")
    print()

    # Uncomment to run tests:
    # run_tests()

    # Uncomment to run interactively:
    # run_interactive()


main()
