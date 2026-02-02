# Exercise 1: Fix the Style - Class Style
#
# This code WORKS but has terrible class style! Fix the issues:
# - Incorrect naming conventions for classes
# - Missing or poor docstrings
# - Public attributes that should be managed
# - Poor method organization
# - Inconsistent __str__ / __repr__
#
# Theme: Character classes for {{school}} adventure game


# ============================================================
# STYLE FIX A: Class Naming
# ============================================================

class wizard_character:
    """ORIGINAL - Wrong naming convention for class"""
    def __init__(self, name):
        self.name = name


class SPELL_BOOK:
    """ORIGINAL - Wrong naming convention (not a constant)"""
    def __init__(self):
        self.spells = []


# ✏️ FIX THE STYLE ✏️
# Classes should use CapitalizedWords (PascalCase)

class WizardCharacter:
    """A wizard character in the game."""
    def __init__(self, name):
        # Your fixed code here
        pass


class SpellBook:
    """A collection of spells."""
    def __init__(self):
        # Your fixed code here
        pass


# ============================================================
# STYLE FIX B: Missing Docstrings
# ============================================================

class original_b:
    def __init__(self, n, h, p):
        self.n = n
        self.h = h
        self.p = p

    def a(self, x):
        self.p = self.p + x

    def t(self, d):
        self.h = self.h - d


class Character:
    # ✏️ FIX THE STYLE ✏️
    # - Add class docstring
    # - Add method docstrings
    # - Rename attributes to be descriptive
    # - Rename methods to be descriptive
    # What are n, h, p? What do a() and t() do?

    def __init__(self, name, health, power):
        """Initialize a character with name, health, and power."""
        pass

    def add_power(self, amount):
        """Add power points to the character."""
        pass

    def take_damage(self, damage):
        """Reduce health by damage amount."""
        pass


# ============================================================
# STYLE FIX C: Method Organization
# ============================================================

class original_c:
    """ORIGINAL - Methods in random order"""

    def cast_spell(self, spell):
        print(f"Casting {spell}")

    def __init__(self, name):
        self.name = name
        self.health = 100

    def __str__(self):
        return self.name

    def heal(self, amount):
        self.health += amount

    def get_health(self):
        return self.health


class OrganizedCharacter:
    # ✏️ FIX THE STYLE ✏️
    # Organize methods in standard order:
    # 1. __init__ first
    # 2. __str__, __repr__ next (dunder methods)
    # 3. Properties/getters
    # 4. Regular methods (alphabetically or by purpose)

    """A well-organized character class."""

    # Write methods in proper order here
    pass


# ============================================================
# STYLE FIX D: String Representation
# ============================================================

class original_d:
    """ORIGINAL - Inconsistent/missing string methods"""

    def __init__(self, name, spell_type, power):
        self.name = name
        self.spell_type = spell_type
        self.power = power

    def __str__(self):
        return self.name  # Too little info

    # No __repr__ at all!


class Spell:
    # ✏️ FIX THE STYLE ✏️
    # Add proper __str__ and __repr__:
    # - __str__ should be human-readable
    # - __repr__ should be unambiguous, ideally reproducible

    """A magical spell with name, type, and power level."""

    def __init__(self, name, spell_type, power):
        pass

    def __str__(self):
        # Human-readable: "Fireball (fire) - Power: 50"
        pass

    def __repr__(self):
        # Unambiguous: "Spell('Fireball', 'fire', 50)"
        pass


# ============================================================
# STYLE FIX E: Attribute Access
# ============================================================

class original_e:
    """ORIGINAL - Direct attribute manipulation"""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.gold = 0

    # Anyone can do: character.health = -999 (bad!)
    # Anyone can do: character.gold = 1000000 (cheating!)


class ProtectedCharacter:
    # ✏️ FIX THE STYLE ✏️
    # Use properties or methods to control attribute access.
    # Prevent invalid values like negative health.

    """A character with protected attributes."""

    def __init__(self, name):
        self.name = name
        self._health = 100  # "Private" by convention
        self._max_health = 100
        self._gold = 0

    @property
    def health(self):
        """Get current health."""
        pass

    @health.setter
    def health(self, value):
        """Set health, clamped to valid range."""
        # Ensure health stays between 0 and max_health
        pass

    def add_gold(self, amount):
        """Add gold (must be positive)."""
        # Only allow adding positive amounts
        pass

    @property
    def gold(self):
        """Get current gold."""
        pass


# ============================================================
# STYLE FIX F: Complete Class Cleanup
# ============================================================

class orig:
    """ORIGINAL - Everything wrong at once"""
    def m(self,s):
        self.s.append(s)
    def __init__(self,n):
        self.n=n
        self.s=[]
        self.hp=100
    def __str__(self):return self.n
    def atk(self,t):t.hp=t.hp-10


class Hero:
    # ✏️ FIX THE STYLE ✏️
    # Complete cleanup needed:
    # - Class docstring
    # - Proper __init__ (first, with spacing)
    # - Descriptive attribute names
    # - Method docstrings
    # - Descriptive method names
    # - Proper spacing throughout
    # - Good __str__ and __repr__

    """A hero character for the adventure game."""

    def __init__(self, name):
        """Initialize hero with name, empty spell list, and full health."""
        pass

    def __str__(self):
        """Return human-readable string."""
        pass

    def __repr__(self):
        """Return unambiguous representation."""
        pass

    def learn_spell(self, spell_name):
        """Add a spell to the hero's known spells."""
        pass

    def attack(self, target):
        """Attack another character, dealing damage."""
        pass


def main():
    print("=== Style Fix A: Class Naming ===")
    bad_wizard = wizard_character("{{hero}}")
    print(f"Bad style: {bad_wizard.name}")
    # good_wizard = WizardCharacter("{{hero}}")
    # print(f"Good style: {good_wizard.name}")

    print("\n=== Style Fix B: Docstrings ===")
    bad_char = original_b("{{hero}}", 100, 50)
    bad_char.a(10)  # What does this do?
    bad_char.t(25)  # What does this do?
    print(f"n={bad_char.n}, h={bad_char.h}, p={bad_char.p}")  # Confusing!

    print("\n=== Style Fix D: String Representation ===")
    spell = original_d("{{spell1}}", "fire", 50)
    print(f"str: {str(spell)}")
    print(f"repr: {repr(spell)}")  # Not helpful!

    print("\n=== Test your fixed classes! ===")
    print("Uncomment the test code in main() to verify your fixes.")


main()
