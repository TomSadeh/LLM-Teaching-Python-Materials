"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to write instance methods - functions
inside classes that can read and modify the object's attributes using self.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a class with methods that READ attributes.
    #
    # Step 1: Define a class called `Character` with __init__ that takes:
    #         - self, name, health, max_health
    #         Store all as instance attributes.
    #
    # Step 2: Add a method called `get_status`:
    #         def get_status(self):
    #         It should return a string: "[name]: [health]/[max_health] HP"
    #
    # Step 3: Add a method called `is_healthy`:
    #         def is_healthy(self):
    #         It should return True if health > max_health / 2, else False
    #
    # Step 4: Create a character and test the methods:
    #         hero = Character("{{hero}}", 75, 100)
    #         print(hero.get_status())  # Should print status
    #         print(hero.is_healthy())  # Should print True
    #
    # Remember: Methods always have self as the first parameter!
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a class with methods that MODIFY attributes.
    #
    # Step 1: Define a class called `Counter` with __init__ that takes:
    #         - self, name, start_value=0
    #         Store as self.name and self.value
    #
    # Step 2: Add a method `increment` that increases value by 1:
    #         def increment(self):
    #             self.value += 1
    #
    # Step 3: Add a method `add` that takes an amount parameter:
    #         def add(self, amount):
    #         It should add the amount to self.value
    #
    # Step 4: Add a method `reset` that sets value back to 0
    #
    # Step 5: Test your counter:
    #         counter = Counter("{{spell1}} uses")
    #         counter.increment()
    #         counter.add(5)
    #         print(f"{counter.name}: {counter.value}")  # Should be 6
    #         counter.reset()
    #         print(f"After reset: {counter.value}")  # Should be 0
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a class where methods return values AND modify state.
    #
    # Step 1: Define a class called `Wallet` with __init__ that takes:
    #         - self, owner, initial_gold=0
    #         Store as self.owner and self.gold
    #
    # Step 2: Add a method `deposit` that takes an amount:
    #         - Add amount to self.gold
    #         - Return the new total
    #
    # Step 3: Add a method `withdraw` that takes an amount:
    #         - If amount > self.gold, print "Not enough gold!" and return 0
    #         - Otherwise, subtract amount from self.gold and return amount
    #
    # Step 4: Add a method `check_balance` that returns self.gold
    #
    # Step 5: Test the wallet:
    #         wallet = Wallet("{{hero}}", 50)
    #         print(f"Deposited, new balance: {wallet.deposit(30)}")  # 80
    #         print(f"Withdrew: {wallet.withdraw(20)}")  # 20
    #         print(f"Balance: {wallet.check_balance()}")  # 60
    #         wallet.withdraw(100)  # Should print "Not enough gold!"
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    exercise_a()

    print("\n=== {{PHASE_2_TITLE}} ===")
    exercise_b()

    print("\n=== {{PHASE_3_TITLE}} ===")
    exercise_c()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
