# %% [markdown]
# {{CONTEXT_FIX_STYLE_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תתקני קוד שעובד אבל מפר את מוסכמות השמות של OOP
# ואת שיטות העבודה הטובות. סגנון טוב הופך את הקוד לקריא
# ועוזר לאחרים להבין את עיצובי הכיתות שלך.
#
# ## {{STYLE_1_TITLE}}
# {{CONTEXT_STYLE_1_NARRATIVE}}
#
#
# ORIGINAL - This code works but has style issues

# %%
class character:  # Wrong! Classes should be PascalCase
    def __init__(self, n, hp, pwr):  # Bad parameter names
        self.n = n  # Unclear attribute name
        self.hp = hp
        self.Pwr = pwr  # Inconsistent naming

    def Damage(self, amt):  # Methods should be snake_case
        self.hp = self.hp - amt

    def GetInfo(self):  # Should be snake_case
        return self.n + " has " + str(self.hp) + " HP"  # Use f-string

# %% [markdown]
# {{CONTEXT_STYLE_FIX_1}}
#
# שכתבי את הכיתה עם המוסכמות הנכונות:
# - שם כיתה: `PascalCase` (‏`Character`)
# - שמות מתודות: `snake_case` (‏`take_damage`, `get_info`)
# - שמות תכונות: `snake_case`, ברורים (‏`name`, `health`, `power`)
# - השתמשי ב-`f-strings` לעיצוב מחרוזות
#
# כתבי את הגרסה המתוקנת שלך למטה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{STYLE_2_TITLE}}
# {{CONTEXT_STYLE_2_NARRATIVE}}
#
#
# ORIGINAL - Mixed naming conventions and poor structure

# %%
class INVENTORY:  # Wrong! Not PascalCase
    def __init__(self, ownerName):  # camelCase, should be snake_case
        self.ownerName = ownerName
        self.ItemList = []  # Wrong case, unclear purpose
        self.g = 0  # What is g?

    def ADD(self, item):  # All caps is wrong
        self.ItemList.append(item)

    def addGold(self, amount):  # camelCase, inconsistent with ADD
        self.g = self.g + amount

    def Display(self):
        print(self.ownerName)
        print(self.ItemList)
        print(self.g)

# %% [markdown]
# {{CONTEXT_STYLE_FIX_2}}
#
# תקני:
# 1. שם הכיתה ל-`PascalCase`
# 2. את כל התכונות ל-`snake_case` עם שמות ברורים
# 3. את כל המתודות ל-`snake_case`
# 4. היי עקבית לאורך כל הקוד
#
# כתבי את הגרסה המתוקנת שלך למטה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{STYLE_3_TITLE}}
# {{CONTEXT_STYLE_3_NARRATIVE}}
#
#
# ORIGINAL - Missing docstrings and unclear code

# %%
class e:  # Single letter name!
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def f(self, x):
        self.b = self.b - x
        if self.b < 0:
            self.b = 0

    def g(self, x):
        if self.c >= x:
            self.c = self.c - x
            return True
        return False

    def h(self):
        return self.a + " B:" + str(self.b) + " C:" + str(self.c)

# %% [markdown]
# {{CONTEXT_STYLE_FIX_3}}
#
# נראה שמדובר בישות משחק עם בריאות (`b`) ומאנה (`c`).
#
# תקני:
# 1. תני לכיתה שם משמעותי (‏`Entity`, `Character` וכו')
# 2. שנני את כל שמות התכונות לשמות ברורים
# 3. שנני את כל שמות המתודות לשמות ברורים (‏`take_damage`, `use_mana`, `get_status`)
# 4. הוסיפי `docstrings` לכיתה ולמתודות
#
# כתבי את הגרסה המתוקנת שלך למטה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{STYLE_4_TITLE}}
# {{CONTEXT_STYLE_4_NARRATIVE}}
#
#
# ORIGINAL - Inheritance with style issues

# %%
class baseUnit:  # Should be PascalCase
    def __init__(self, NAME, HP):  # ALL CAPS parameters
        self.NAME = NAME
        self.HP = HP

# %%
class warrior_unit(baseUnit):  # Should be PascalCase
    def __init__(self, NAME, HP, str):  # str shadows built-in!
        super().__init__(NAME, HP)
        self.str = str  # shadows built-in str()

    def ATTACK(self):  # ALL CAPS method
        return self.str

# %%
class MageUnit(baseUnit):  # Inconsistent with warrior_unit
    def __init__(self, NAME, HP, mp, magic_power):
        super().__init__(NAME, HP)
        self.mp = mp  # Inconsistent (not all caps like HP)
        self.magic_power = magic_power

    def cast(self):
        if self.mp >= 10:
            self.mp -= 10
            return self.magic_power
        return 0

# %% [markdown]
# {{CONTEXT_STYLE_FIX_4}}
#
# תקני:
# 1. את כל שמות הכיתות ל-`PascalCase` (‏`BaseUnit`, `WarriorUnit`, `MageUnit`)
# 2. את כל התכונות ל-`snake_case`
# 3. את כל המתודות ל-`snake_case`
# 4. אל תסתירי פונקציות מובנות (‏`str` ← `strength`)
# 5. היי עקבית בכל ההיררכיה
#
# כתבי את הגרסה המתוקנת שלך למטה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_FIX_STYLE_INTRO}}")
print("=" * 50)

print("\n=== {{STYLE_1_TITLE}} ===")
print("Original (poor style):")
c = character("{{hero}}", 100, 25)
c.Damage(30)
print(c.GetInfo())
print("\nFixed (your version):")
fixed_1()

print("\n=== {{STYLE_2_TITLE}} ===")
print("Original (poor style):")
inv = INVENTORY("{{hero}}")
inv.ADD("{{item}}")
inv.addGold(50)
inv.Display()
print("\nFixed (your version):")
fixed_2()

print("\n=== {{STYLE_3_TITLE}} ===")
print("Original (poor style):")
entity = e("{{hero}}", 100, 50)
entity.f(30)
entity.g(20)
print(entity.h())
print("\nFixed (your version):")
fixed_3()

print("\n=== {{STYLE_4_TITLE}} ===")
print("Original (poor style):")
warrior = warrior_unit("{{hero}}", 100, 25)
mage = MageUnit("{{heroine}}", 80, 50, 30)
print(f"Warrior attack: {warrior.ATTACK()}")
print(f"Mage cast: {mage.cast()}")
print("\nFixed (your version):")
fixed_4()

print("\n" + "=" * 50)
print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")
