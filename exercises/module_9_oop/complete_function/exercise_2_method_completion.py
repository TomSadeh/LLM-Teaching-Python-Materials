"""
{{CONTEXT_COMPLETE_FUNCTION_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll complete methods that operate on object state.
The class structure is provided - you write the method bodies.
"""


# ============================================================
# {{FUNCTION_1_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_1_NARRATIVE}}


class HealthTracker:
    """Tracks health for a character at {{school}}."""

    def __init__(self, name, max_health):
        """Initialize with full health."""
        self.name = name
        self.max_health = max_health
        self.current_health = max_health

    def take_damage(self, amount):
        """
        Reduce health by the damage amount.

        Args:
            amount: Damage to take (positive integer)

        The health should not go below 0.

        Examples:
            >>> tracker = HealthTracker("{{hero}}", 100)
            >>> tracker.take_damage(30)
            >>> tracker.current_health
            70
            >>> tracker.take_damage(200)
            >>> tracker.current_health
            0
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_1}}
        #
        # Subtract amount from self.current_health
        # Make sure health doesn't go below 0
        # Hint: Use max(0, result) or an if statement

        pass

    def heal(self, amount):
        """
        Restore health by the healing amount.

        Args:
            amount: Health to restore (positive integer)

        The health should not exceed max_health.

        Examples:
            >>> tracker = HealthTracker("{{hero}}", 100)
            >>> tracker.current_health = 50
            >>> tracker.heal(30)
            >>> tracker.current_health
            80
            >>> tracker.heal(50)
            >>> tracker.current_health
            100
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_2}}
        #
        # Add amount to self.current_health
        # Make sure health doesn't exceed self.max_health
        # Hint: Use min(self.max_health, result) or an if statement

        pass

    def is_alive(self):
        """
        Check if the character is still alive.

        Returns:
            bool: True if current_health > 0, False otherwise

        Examples:
            >>> tracker = HealthTracker("{{hero}}", 100)
            >>> tracker.is_alive()
            True
            >>> tracker.current_health = 0
            >>> tracker.is_alive()
            False
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_3}}
        #
        # Return True if health is above 0

        pass


# ============================================================
# {{FUNCTION_2_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_2_NARRATIVE}}


class ScoreKeeper:
    """Keeps track of points and achievements."""

    def __init__(self, player_name):
        """Initialize with zero points."""
        self.player_name = player_name
        self.score = 0
        self.high_score = 0
        self.achievements = []

    def add_points(self, points):
        """
        Add points to the score.

        Args:
            points: Points to add (positive integer)

        Also updates high_score if the new score is higher.

        Examples:
            >>> keeper = ScoreKeeper("{{hero}}")
            >>> keeper.add_points(50)
            >>> keeper.score
            50
            >>> keeper.high_score
            50
            >>> keeper.add_points(30)
            >>> keeper.score
            80
            >>> keeper.high_score
            80
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_1}}
        #
        # Add points to self.score
        # Update self.high_score if score is now higher

        pass

    def unlock_achievement(self, achievement_name):
        """
        Unlock a new achievement if not already unlocked.

        Args:
            achievement_name: Name of the achievement

        Returns:
            bool: True if newly unlocked, False if already had it

        Examples:
            >>> keeper = ScoreKeeper("{{hero}}")
            >>> keeper.unlock_achievement("First Victory")
            True
            >>> keeper.achievements
            ['First Victory']
            >>> keeper.unlock_achievement("First Victory")
            False
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_2}}
        #
        # Check if achievement_name is already in self.achievements
        # If not, add it and return True
        # If already there, return False

        pass

    def reset_score(self):
        """
        Reset the current score to 0.

        The high_score is NOT reset - it persists across resets.

        Examples:
            >>> keeper = ScoreKeeper("{{hero}}")
            >>> keeper.add_points(100)
            >>> keeper.reset_score()
            >>> keeper.score
            0
            >>> keeper.high_score
            100
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_3}}
        #
        # Set self.score to 0 (but leave high_score alone)

        pass


# ============================================================
# {{FUNCTION_3_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_3_NARRATIVE}}


class ItemStack:
    """A stack of identical items in an inventory."""

    def __init__(self, item_name, quantity=1, max_stack=99):
        """Initialize an item stack."""
        self.item_name = item_name
        self.quantity = quantity
        self.max_stack = max_stack

    def add(self, amount):
        """
        Add items to the stack.

        Args:
            amount: Number of items to add

        Returns:
            int: The number of items that couldn't fit (overflow)

        Examples:
            >>> stack = ItemStack("{{item}}", 50, max_stack=99)
            >>> stack.add(30)
            0
            >>> stack.quantity
            80
            >>> stack.add(30)
            11
            >>> stack.quantity
            99
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_1}}
        #
        # Calculate how many items would fit
        # Add what fits, return the overflow
        # total = self.quantity + amount
        # If total > max_stack: overflow = total - max_stack

        pass

    def remove(self, amount):
        """
        Remove items from the stack.

        Args:
            amount: Number of items to remove

        Returns:
            int: The number of items actually removed

        Examples:
            >>> stack = ItemStack("{{item}}", 50)
            >>> stack.remove(30)
            30
            >>> stack.quantity
            20
            >>> stack.remove(50)
            20
            >>> stack.quantity
            0
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_2}}
        #
        # Can only remove up to what's available
        # Actually removed = min(amount, self.quantity)
        # Subtract from quantity, return amount removed

        pass

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if quantity is 0

        Examples:
            >>> stack = ItemStack("{{item}}", 5)
            >>> stack.is_empty()
            False
            >>> stack.remove(5)
            5
            >>> stack.is_empty()
            True
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_3}}

        pass


def main():
    print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
    print("=" * 50)

    print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
    tracker = HealthTracker("{{hero}}", 100)
    print(f"Starting health: {tracker.current_health}")
    tracker.take_damage(30)
    print(f"After 30 damage: {tracker.current_health}")
    tracker.heal(20)
    print(f"After 20 healing: {tracker.current_health}")
    print(f"Is alive: {tracker.is_alive()}")

    print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
    keeper = ScoreKeeper("{{heroine}}")
    keeper.add_points(100)
    print(f"Score: {keeper.score}, High: {keeper.high_score}")
    print(f"New achievement: {keeper.unlock_achievement('First Win')}")
    print(f"Duplicate: {keeper.unlock_achievement('First Win')}")
    keeper.reset_score()
    print(f"After reset - Score: {keeper.score}, High: {keeper.high_score}")

    print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
    stack = ItemStack("{{item}}", 50, max_stack=99)
    overflow = stack.add(60)
    print(f"Added 60, overflow: {overflow}, quantity: {stack.quantity}")
    removed = stack.remove(40)
    print(f"Removed {removed}, quantity: {stack.quantity}")
    print(f"Is empty: {stack.is_empty()}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
