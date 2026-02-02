# Theme Creator Guide

Create custom themes for Maya Chat Python exercises. Your theme transforms coding lessons into adventures in your chosen world.

---

## Quick Start

1. Copy `_TEMPLATE.json` to `your_theme_name.json`
2. Fill in the required fields (marked below)
3. Add your theme to the theme registry
4. Test with a few exercises

---

## Theme File Structure

Each theme is a single JSON file with these sections:

```
your_theme.json
├── Metadata (theme_id, name, description)
├── Layer 1: Entity Names (characters, places, items)
├── Layer 2: Universal Blocks (voice and framing)
├── Layer 2: Context Blocks (narrative sentences)
├── Layer 2: Indexed Blocks (multi-part content)
├── Layer 3: Framework Concepts (world structure)
└── Hybrid Blocks (multi-part exercises)
```

---

## Required vs Optional Fields

### Required (exercises won't work without these)

| Field | Example | Why Required |
|-------|---------|--------------|
| `theme_id` | `"space_explorers"` | Unique identifier |
| `theme_name` | `"Space Explorers"` | Display name |
| `hero` | `["Captain Nova"]` | Main character references |
| `heroine` | `["Engineer Luna"]` | Main character references |
| `school` | `["Starship Academy"]` | Primary setting |
| `mentor` | `["Admiral Chen"]` | Teacher figure |

### Recommended (significantly improve experience)

| Field | Purpose |
|-------|---------|
| `ROLE_TITLE` | What students are called |
| `COMPONENT_SINGULAR` | What they're building |
| `OPENING_FLAVOR` | Sets the mood |
| `CELEBRATION` | Reward message |
| Layer 2 context blocks | Rich narratives |

### Optional (enhance specific exercise types)

- Indexed blocks (PHASE_N, CASE_N, etc.)
- Hybrid exercise blocks
- Layer 3 framework concepts

---

## Layer 1: Entity Names

Simple noun replacements. Use arrays for variety (random selection).

```json
"layer_1_entities": {
  "hero": ["Alex StarPilot", "Jordan Cosmos", "Sam Nebula"],
  "school": ["Starship Academy"],
  "item": ["laser cutter", "gravity wrench", "plasma torch"]
}
```

**Tips:**
- 3-5 options per entity creates nice variety
- Keep names consistent with your genre
- `spell1-4` can be any abilities (not just magic)

---

## Layer 2: Universal Blocks

Voice and framing that applies everywhere.

```json
"layer_2_universal": {
  "ROLE_TITLE": "Cadet",
  "MENTOR_TITLE": "Commander",
  "WORKSPACE": "engineering bay",
  "COMPONENT_SINGULAR": "system module",
  "TASK_VERB": "construct",
  "SUCCESS_WORD": "Mission accomplished",
  "CELEBRATION": "Systems online! You've earned your engineering badge!",
  "OPENING_FLAVOR": "Your workstation is powered up. The starship awaits your expertise!"
}
```

---

## Layer 2: Context Blocks

Full sentences that provide narrative depth. Organized by purpose:

### Introduction Blocks
Set the scene for different exercise types.

```json
"introduction": {
  "CONTEXT_INTRO": "Welcome aboard the Starship Academy training deck!",
  "CONTEXT_INVESTIGATION_INTRO": "Alert! Multiple ship systems are reporting errors!",
  "CONTEXT_PROJECT_INTRO": "Your engineering team needs a new navigation module."
}
```

### Task Blocks
Tell students what to do.

```json
"tasks": {
  "CONTEXT_STUDENT_TASK": "Build the module following the specifications below.",
  "CONTEXT_INVESTIGATION_MISSION": "Diagnose each system failure and restore operations."
}
```

### Completion Blocks
Celebrate success.

```json
"completion": {
  "CONTEXT_ROLE_COMPLETE": "Outstanding work, Cadet! The Captain is impressed.",
  "CONTEXT_VERIFICATION_COMPLETE": "All systems verified. Ship is ready for launch!"
}
```

---

## Layer 2: Indexed Blocks

For exercises with multiple parts. Replace `N` with numbers 1-5.

```json
"phases": {
  "PHASE_1_TITLE": "Phase 1: Power Core",
  "CONTEXT_PHASE_1": "Every starship needs a power source. Initialize the reactor.",

  "PHASE_2_TITLE": "Phase 2: Life Support",
  "CONTEXT_PHASE_2": "With power online, activate the oxygen systems.",

  "PHASE_3_TITLE": "Phase 3: Navigation",
  "CONTEXT_PHASE_3": "Now add the star charts and plotting computer."
}
```

---

## Layer 3: Framework Concepts

Define how your universe works (used in meta-descriptions).

```json
"layer_3_framework": {
  "INSTITUTION_TYPE": "starship training vessel",
  "ABILITY_TYPE": "engineering",
  "PRACTITIONER_SINGULAR": "cadet",
  "RANKING_SYSTEM": "officer ranks",
  "CHALLENGE_TYPE": "system malfunctions"
}
```

---

## Genre Examples

### Fantasy
```json
{
  "hero": ["Aldric the Bold"],
  "school": ["Silvermist Academy"],
  "ROLE_TITLE": "Apprentice",
  "COMPONENT_SINGULAR": "spell",
  "TASK_VERB": "cast",
  "CONTEXT_INTRO": "Welcome, young apprentice, to the halls of Silvermist!"
}
```

### Sports
```json
{
  "hero": ["Marcus Johnson"],
  "school": ["Elite Sports Academy"],
  "ROLE_TITLE": "Rookie",
  "COMPONENT_SINGULAR": "play",
  "TASK_VERB": "execute",
  "CONTEXT_INTRO": "Welcome to training camp, rookie! Time to prove yourself."
}
```

### Detective/Mystery
```json
{
  "hero": ["Detective Morgan"],
  "school": ["City Precinct Academy"],
  "ROLE_TITLE": "Detective",
  "COMPONENT_SINGULAR": "case file",
  "TASK_VERB": "investigate",
  "CONTEXT_INTRO": "A new case has landed on your desk, Detective."
}
```

### Professional Coding
```json
{
  "hero": ["the developer"],
  "school": ["Tech Corp"],
  "ROLE_TITLE": "Developer",
  "COMPONENT_SINGULAR": "feature",
  "TASK_VERB": "implement",
  "CONTEXT_INTRO": "Let's build this step by step."
}
```

---

## Testing Your Theme

1. **Minimal test**: Ensure required fields render correctly
2. **Exercise type test**: Try one exercise from each type
3. **Narrative flow test**: Read through a full exercise - does it make sense?
4. **Edge cases**: Check exercises with multiple parts (phases, cases)

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Single string instead of array | Use `["value"]` not `"value"` for entities |
| Missing required field | Check hero, heroine, school, mentor |
| Inconsistent tone | Read all context blocks together |
| Too many exclamation points | Keep energy consistent |
| Theme-specific Python references | Keep code examples generic |

---

## Placeholder Reference

### In Exercises, Use:
```python
name = "{{hero}}"           # Becomes "Alex StarPilot"
print("{{CONTEXT_INTRO}}")  # Becomes "Welcome aboard..."
```

### Available Placeholders:

**Characters:** `hero`, `heroine`, `friend`, `mentor`, `villain`

**Places:** `school`, `house`, `location`, `place`

**Abilities:** `spell1`, `spell2`, `spell3`, `spell4`

**Items:** `creature`, `pet`, `item`, `transport`

**Groups:** `group`, `exclamation`, `greeting`, `password`

**All CONTEXT_* blocks** from the template

---

## Need Help?

- Check existing themes in `theme_mappings/` for examples
- See `_TEMPLATE.json` for complete placeholder list
- Read `docs/NARRATIVE_SYSTEM.md` for template details
