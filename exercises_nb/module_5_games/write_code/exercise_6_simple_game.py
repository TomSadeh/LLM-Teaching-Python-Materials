# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# נושא: בניית משחק שלם ופשוט
# רמת קושי: 4-5
#
# שלבי את כל מה שלמדת כדי לבנות משחק שלם שאפשר לשחק בו,
# עם לולאות, `random`, בדיקת קלט ומצב!

# %%
import random

# %% [markdown]
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# בני את מנגנוני הליבה של המשחק.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# בני את מערכת הלחימה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# בני את פעולות השחקנית.

# %%
print(f"\n{{{{hero}}}} attacks {{{{villain}}}}!")
return attack(player, enemy)

# %% [markdown]
#
# הדפיסי הודעת הגנה
# החזירי 3 (בונוס הגנה זמני)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# בני את לולאת הלחימה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("\n" + "=" * 50)
print(f"   BATTLE: {{{{hero}}}} vs {enemy['name']}")
print("=" * 50)

defending = False

# %% [markdown]
#
# כל עוד שניהם בחיים:
# 1. הצגי סטטוס
# 2. הרצי סיבוב לחימה, קבלי את מצב ההגנה החדש
# 3. בדקי אם הקרב הסתיים
#
# אחרי הלולאה: הכריזי על המנצחת, החזירי תוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# בני את המשחק השלם.

# %%
print("=" * 50)
print("   ARENA CHAMPION")
print(f"   A {{{{school}}}} Adventure")
print("=" * 50)
print()
print(f"{{{{hero}}}} enters {{{{location}}}} to face {{{{villain}}}}!")
print("Victory means glory. Defeat means... starting over.")
print()

# %%
introduction()

playing = True
while playing:
    print("\n--- Creating your champion ---")
    name = input("Enter your champion's name: ").strip()
    if not name:
        name = "{{hero}}"

    player = create_character(name)
    print(f"\n{name} enters the arena!")
    print(f"HP: {player['hp']} | Attack: {player['attack']} | Defense: {player['defense']}")

    # ✏️ YOUR CODE HERE ✏️
    #
    # Create three enemies with increasing difficulty:
    # enemies = [
    #     create_enemy("{{creature}}", 1),
    #     create_enemy("{{villain}}'s Minion", 2),
    #     create_enemy("{{villain}}", 3)
    # ]
    #
    # Battle loop:
    # For each enemy:
    #   1. Print "Battle X of 3"
    #   2. Run battle
    #   3. If lost, print game over, break
    #   4. If won and not last battle, restore 10 HP
    #
    # If completed all battles: Victory message!
    #
    # Ask to play again
    pass

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
print("Testing character creation:")
# player = create_character("Test")
# print(f"Player: {player}")
# enemy = create_enemy("Goblin", 2)
# print(f"Enemy: {enemy}")

print("\n=== {{PHASE_2_TITLE}} ===")
print("Testing combat:")
# player = create_character("Test")
# enemy = create_enemy("Target", 1)
# damage = attack(player, enemy)
# print(f"Enemy HP: {enemy['hp']}")

print("\n=== {{PHASE_3_TITLE}} ===")
print("Testing player actions:")
# (test individual actions)

print("\n=== {{PHASE_4_TITLE}} ===")
print("Testing battle:")
# player = create_character("Champion")
# enemy = create_enemy("Challenger", 1)
# result = battle(player, enemy)
# print(f"Player won: {result}")

print("\n=== {{PHASE_5_TITLE}} ===")
print("Launch full game:")
# play_game()

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
