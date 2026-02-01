# Quick Start: Creating a New Theme

**Goal**: Create a new theme in 10 minutes

---

## Step 1: Copy the Template (30 seconds)

```bash
cd theme_mappings
cp professional_coding.json my_theme.json
```

Why professional_coding? It's the **minimal theme** - easiest to customize.

---

## Step 2: Fill in Basic Info (2 minutes)

Open `my_theme.json` and update:

```json
{
  "theme_id": "restaurant_chef",
  "theme_name": "Restaurant Chef Training",
  "description": "Cooking and restaurant management theme",
  "narrative_variables": {
    ...
  }
}
```

---

## Step 3: Fill Core Variables (5 minutes)

These 10 variables cover 90% of narratives:

```json
"ROLE_TITLE": "Chef",
"WORKSPACE": "kitchen",

"PROJECT_TYPE": "signature menu",
"PROJECT_SCALE": "award-winning",
"GOAL": "michelin star",

"COMPONENT_SINGULAR": "recipe",
"COMPONENT_PLURAL": "recipes",
"TASK_VERB": "prepare",
"TASK_NOUN": "dish",

"SECTION_ICON": "🍳"
```

**Think**: What role does the learner play? What are they building?

---

## Step 4: Fill Feedback Variables (2 minutes)

How does your theme celebrate success?

```json
"SUCCESS_WORD": "Excellent",
"CELEBRATION": "Service complete! Diners are delighted!",
"PROGRESS_UNIT": "course"
```

---

## Step 5: Fill Flavor Text (1 minute)

Add personality:

```json
"OPENING_FLAVOR": "Your chef's knife is sharp and the kitchen awaits!",
"TRANSITION_WORD": "Next",
"CLOSING_FLAVOR": "Your culinary skills have earned rave reviews!"
```

---

## Step 6: Test It! (30 seconds)

```bash
cd ..
python scripts/validate_themes.py
```

Look for:
```
[OK] Loaded theme: Restaurant Chef Training
[OK] Coherent narrative generated
```

---

## Done! ✅

Your theme now works with ALL 6 exercise narrative templates:
- Progressive Chapter
- Tutorial Walkthrough
- Challenge Quest
- Mystery Investigation
- World Builder
- Spec Implementation

---

## Optional: Advanced Variables

For specific templates, add these if needed:

### For Investigation Templates
```json
"EVIDENCE_NOUN": "ingredient",
"SOLVE_VERB": "perfect"
```

### For Builder Templates
```json
"ENTITY_NOUN": "dish",
"ENTITY_NOUN_PLURAL": "dishes",
"SYSTEM_NOUN": "menu system"
```

### For Spec Templates
```json
"CLIENT": "Restaurant Owner",
"DELIVERABLE": "tasting menu",
"DELIVERABLE_TITLE": "Menu Complete"
```

---

## Examples

### Restaurant Theme (Cooking)
- **Role**: Chef
- **Project**: signature menu
- **Components**: recipes
- **Celebration**: "Service excellent!"

### Space Exploration (Sci-Fi)
- **Role**: Astronaut
- **Project**: space mission
- **Components**: protocols
- **Celebration**: "Mission successful!"

### Fashion Design
- **Role**: Designer
- **Project**: fashion collection
- **Components**: outfits
- **Celebration**: "Runway ready!"

### Marine Biology
- **Role**: Marine Biologist
- **Project**: coral reef study
- **Components**: observations
- **Celebration**: "Discovery complete!"

---

## The 20-Variable Checklist

Make sure you fill all these:

**Role & Context** (4):
- [ ] ROLE_TITLE
- [ ] ROLE_TITLE_PLURAL
- [ ] MENTOR_TITLE
- [ ] WORKSPACE

**Project & Scope** (3):
- [ ] PROJECT_TYPE
- [ ] PROJECT_SCALE
- [ ] GOAL

**Components & Tasks** (4):
- [ ] COMPONENT_SINGULAR
- [ ] COMPONENT_PLURAL
- [ ] TASK_VERB
- [ ] TASK_NOUN

**Progress & Feedback** (4):
- [ ] SECTION_ICON
- [ ] SUCCESS_WORD
- [ ] CELEBRATION
- [ ] PROGRESS_UNIT

**Narrative Flavor** (3):
- [ ] OPENING_FLAVOR
- [ ] TRANSITION_WORD
- [ ] CLOSING_FLAVOR

**Optional Advanced** (6):
- [ ] EVIDENCE_NOUN
- [ ] SOLVE_VERB
- [ ] ENTITY_NOUN
- [ ] ENTITY_NOUN_PLURAL
- [ ] SYSTEM_NOUN
- [ ] CLIENT
- [ ] DELIVERABLE
- [ ] DELIVERABLE_TITLE

---

## Tips for Good Themes

### DO:
✅ Keep ROLE_TITLE to 1-2 words (Chef, not "Professional Chef")
✅ Make variables internally consistent (all military OR all cooking)
✅ Test phrases out loud: "prepare your recipe" vs "execute your dish"
✅ Match formality: formal mentor → formal celebration

### DON'T:
❌ Mix metaphors (wizard-coach in a kitchen)
❌ Use overly long values (keep it punchy)
✅ Change placeholder names (system expects exact names)
❌ Add new variables (templates won't recognize them)

---

## Testing Your Theme

### Quick Test
```bash
python scripts/validate_themes.py
```

### What to Look For
1. `[OK] Loaded theme` - File is valid JSON
2. `[OK] Coherent narrative generated` - All placeholders filled
3. Read the sample openings - Do they make sense?

### Common Issues

**"Unfilled placeholders detected"**
→ You're missing a required variable. Check the checklist above.

**"Opening too short or missing"**
→ Template can't find your theme file. Check file location and JSON syntax.

**Narrative sounds weird**
→ Variables might not fit together. Read it out loud and adjust.

---

## Where Your Theme Is Used

Once created, your theme will automatically work in:

1. **Exercise Openings**
   - "Welcome, {ROLE_TITLE}!"
   - Sets the stage

2. **Section Transitions**
   - "Great! Now let's continue to..."
   - Maintains flow

3. **Task Descriptions**
   - "Build {COMPONENT_PLURAL}"
   - Contextualizes work

4. **Celebrations**
   - "{CELEBRATION}"
   - Rewards progress

5. **Closings**
   - "Your {PROJECT_TYPE} is complete!"
   - Provides closure

---

## Need Inspiration?

Look at existing themes:

- **Minimal**: `professional_coding.json` - Plain, no metaphors
- **Maximal**: `fantasy_magic.json` - Full metaphorical language
- **Balanced**: `soccer_academy.json` - Metaphors but grounded

Copy what works for you!

---

## Ready to Create?

1. Copy `professional_coding.json`
2. Fill 20 variables
3. Run validation
4. **Done!**

Your theme now works with 6 narrative templates and can be used for all Python exercises.

**Time needed**: ~10 minutes
**Difficulty**: Easy (just fill a JSON file)
**Result**: Professional-quality themed learning experience
