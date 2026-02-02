# Theme Placeholder Reference

Use `{{placeholder}}` syntax in exercises. Values are replaced at runtime based on the user's selected theme.

For the complete placeholder list with descriptions, see [theme_mappings/_TEMPLATE.json](theme_mappings/_TEMPLATE.json).

---

## Three-Layer System Overview

| Layer | Purpose | Example |
|-------|---------|---------|
| **Layer 1** | Entity names (nouns) | `{{hero}}` → "Harry Potter" |
| **Layer 2** | Context blocks (sentences) | `{{CONTEXT_INTRO}}` → "Welcome to Hogwarts!" |
| **Layer 3** | Framework concepts (structure) | `{{ABILITY_TYPE}}` → "magic" |

---

## Layer 1: Entity Names

Simple noun replacements. Arrays in theme files allow random selection for variety.

### Characters

| Placeholder | Description | Fantasy | Sci-Fi | Plain |
|-------------|-------------|---------|--------|-------|
| `{{hero}}` | Male protagonist | Harry Potter | Captain Nova | Alex |
| `{{heroine}}` | Female protagonist | Hermione Granger | Engineer Luna | Sam |
| `{{friend}}` | Supporting character | Ron Weasley | Crewmate Chen | teammate |
| `{{mentor}}` | Teacher/guide | Dumbledore | Admiral Chen | instructor |
| `{{villain}}` | Antagonist | Voldemort | Pirate Lord | bugs |

### Places

| Placeholder | Description | Fantasy | Sci-Fi | Plain |
|-------------|-------------|---------|--------|-------|
| `{{school}}` | Main institution | Hogwarts | Starship Academy | Code Academy |
| `{{house}}` | Sub-group/division | Gryffindor | Engineering Deck | Team Alpha |
| `{{location}}` | Specific place | the Great Hall | the Bridge | the workspace |
| `{{place}}` | Named destination | Diagon Alley | the Starport | the office |

### Abilities

| Placeholder | Description | Fantasy | Sci-Fi | Plain |
|-------------|-------------|---------|--------|-------|
| `{{spell1}}` | Basic ability | Lumos | sensor scan | print statement |
| `{{spell2}}` | Intermediate ability | Expelliarmus | weapons lock | for loop |
| `{{spell3}}` | Advanced ability | Expecto Patronum | hyperspace jump | recursion |
| `{{spell4}}` | Utility ability | Wingardium Leviosa | auto-pilot | debugging |

### Objects

| Placeholder | Description | Fantasy | Sci-Fi | Plain |
|-------------|-------------|---------|--------|-------|
| `{{creature}}` | Entity type | hippogriff | alien creature | data structure |
| `{{pet}}` | Companion | Hedwig the owl | ship's cat | helper function |
| `{{item}}` | Tool/object | wand | datapad | keyboard |
| `{{transport}}` | Vehicle | Nimbus 2000 | shuttle craft | internet |

### Phrases

| Placeholder | Description | Fantasy | Sci-Fi | Plain |
|-------------|-------------|---------|--------|-------|
| `{{group}}` | Organization | Dumbledore's Army | the crew | the dev team |
| `{{exclamation}}` | Themed expression | By Merlin's beard! | By the stars! | Eureka! |
| `{{greeting}}` | Welcome message | Welcome to Hogwarts | Welcome aboard | Welcome |
| `{{password}}` | Secret phrase | Caput Draconis | clearance code | password123 |

---

## Layer 2: Context Blocks

Full sentences that provide narrative framing. Use for introductions, instructions, and completion messages.

### Introduction Blocks

| Placeholder | Use For |
|-------------|---------|
| `{{CONTEXT_INTRO}}` | Generic exercise opening |
| `{{CONTEXT_PROJECT_INTRO}}` | Incremental builder exercises |
| `{{CONTEXT_ROLE_INTRO}}` | Role assignment exercises |
| `{{CONTEXT_INVESTIGATION_INTRO}}` | Bug hunt / decode error exercises |
| `{{CONTEXT_PREDICTION_INTRO}}` | Output prediction exercises |
| `{{CONTEXT_COMPARISON_INTRO}}` | Which-is-better exercises |

### Learning Blocks

| Placeholder | Use For |
|-------------|---------|
| `{{CONTEXT_LEARNING_OBJECTIVE}}` | What the student will learn |
| `{{CONTEXT_STUDENT_TASK}}` | What the student needs to do |
| `{{CONTEXT_SUCCESS_CRITERIA}}` | How to know they succeeded |

### Guidance Blocks

| Placeholder | Use For |
|-------------|---------|
| `{{CONTEXT_IMPLEMENTATION_GUIDANCE}}` | Tips for writing code |
| `{{CONTEXT_ANALYSIS_PROMPT}}` | How to analyze tradeoffs |
| `{{CONTEXT_DECISION_GUIDANCE}}` | Criteria for decisions |

### Completion Blocks

| Placeholder | Use For |
|-------------|---------|
| `{{CONTEXT_ROLE_COMPLETE}}` | Closing message for role exercises |
| `{{CONTEXT_FINAL_ASSEMBLY}}` | Closing message for builder exercises |
| `{{CONTEXT_VERIFICATION_COMPLETE}}` | Closing message for prediction exercises |

### Indexed Blocks (N = 1-5)

For multi-part exercises, replace `N` with the part number.

| Pattern | Use For |
|---------|---------|
| `{{PHASE_N_TITLE}}` | Incremental builder phase titles |
| `{{CONTEXT_PHASE_N}}` | Incremental builder phase narratives |
| `{{CASE_N_TITLE}}` | Bug hunt case titles |
| `{{CONTEXT_CASE_N_NARRATIVE}}` | Bug hunt case stories |
| `{{CHALLENGE_N_TITLE}}` | Prediction challenge titles |
| `{{APPROACH_N_NAME}}` | Comparison approach names |

---

## Layer 3: Framework Concepts

Structural terms for meta-descriptions. Use sparingly.

| Placeholder | Description | Fantasy | Sci-Fi | Plain |
|-------------|-------------|---------|--------|-------|
| `{{ROLE_TITLE}}` | Student role | Wizard | Engineer | Developer |
| `{{MENTOR_TITLE}}` | Teacher title | Professor | Commander | Instructor |
| `{{COMPONENT_SINGULAR}}` | What they build | spell | module | feature |
| `{{TASK_VERB}}` | Action verb | cast | construct | implement |
| `{{ABILITY_TYPE}}` | Type of skill | magic | engineering | coding |
| `{{PRACTITIONER_SINGULAR}}` | Practitioner | wizard | engineer | developer |

---

## Usage Examples

### Basic Entity Usage

```python
# Create a profile for {{hero}}
name = "{{hero}}"
skill = "{{spell1}}"
print(f"{name} learned {skill}!")
```

### Context Block Usage

```python
"""
{{CONTEXT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

# {{CONTEXT_STUDENT_TASK}}
def exercise():
    # ✏️ YOUR CODE HERE ✏️
    pass
```

### Indexed Block Usage

```python
# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}

def exercise_a():
    pass

# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}

def exercise_b():
    pass
```

---

## Theme Files

Theme values are defined in `theme_mappings/*.json`:

| File | Description |
|------|-------------|
| `_TEMPLATE.json` | Complete placeholder reference |
| `_EXAMPLE_fantasy_complete.json` | Full fantasy theme example |
| `fantasy_magic.json` | Harry Potter-style magic |
| `scifi_engineering.json` | Space/technology theme |
| `professional_coding.json` | Plain coding, no metaphors |

---

## Guidelines

1. **Use placeholders consistently** - If you mention `{{hero}}` once, use `{{hero}}` throughout
2. **Match context to exercise type** - Use `{{CONTEXT_INVESTIGATION_*}}` for bug hunts, not write_code
3. **Don't overuse** - A few well-placed placeholders are better than placeholder soup
4. **Test with multiple themes** - Verify exercises read naturally in fantasy, sci-fi, and plain modes

---

## Quick Links

- Full template: [theme_mappings/_TEMPLATE.json](theme_mappings/_TEMPLATE.json)
- Writing guide: [docs/WRITING_GUIDE.md](docs/WRITING_GUIDE.md)
- Theme creation: [theme_mappings/THEME_CREATOR_GUIDE.md](theme_mappings/THEME_CREATOR_GUIDE.md)
- Narrative system: [docs/NARRATIVE_SYSTEM.md](docs/NARRATIVE_SYSTEM.md)
