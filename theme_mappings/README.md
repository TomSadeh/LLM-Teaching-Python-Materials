# Theme Mapping Files

**Purpose**: Enable theme creators to customize exercise narratives without modifying template code.

## What Are Theme Mappings?

Theme mapping files are JSON configurations that fill universal exercise narrative templates with theme-specific language. This allows the same teaching structure to work across completely different themes.

## File Structure

Each theme mapping JSON contains:

```json
{
  "theme_id": "unique_identifier",
  "theme_name": "Display Name",
  "description": "What this theme is about",
  "narrative_variables": {
    // 20+ placeholder variables
  }
}
```

## Available Theme Mappings

| Theme ID | Theme Name | Description |
|----------|------------|-------------|
| `professional_coding` | Professional Software Development | Plain coding with no metaphors |
| `fantasy_magic` | Fantasy Magic Academy | Harry Potter-style wizardry |
| `soccer_academy` | Soccer Training Academy | Sports coaching and team building |

## Creating a New Theme

### 1. Start with the minimal theme

Copy `professional_coding.json` as your starting point - it has the least "flavor" to replace.

### 2. Fill in your theme's variables

Replace the values (keep the placeholder names the same):

```json
{
  "theme_id": "your_theme_id",
  "theme_name": "Your Theme Name",
  "description": "Brief description",
  "narrative_variables": {
    "ROLE_TITLE": "What is the learner called?",
    "WORKSPACE": "Where does work happen?",
    "PROJECT_TYPE": "What are they building?",
    // ... etc
  }
}
```

### 3. Test coherence

Read through the values and check:
- Do they work together as a cohesive theme?
- Can you imagine someone saying "build a PROJECT_TYPE with COMPONENT_PLURAL"?
- Does CELEBRATION match the tone of ROLE_TITLE?

### 4. Example transformation

**Professional Coding:**
> "Developer, implement these features in your codebase. Success!"

**Your Sci-Fi Theme:**
> "Engineer, construct these modules in your starship. Systems online!"

Same structure, different theme!

## Variable Categories

### Role & Context (Who & Where)
- `ROLE_TITLE` - The learner's role
- `MENTOR_TITLE` - The guide/authority
- `WORKSPACE` - Where the work happens

### Project & Scope (What & Why)
- `PROJECT_TYPE` - What's being built
- `PROJECT_SCALE` - Size/importance descriptor
- `GOAL` - End objective

### Components & Tasks (How)
- `COMPONENT_SINGULAR` / `COMPONENT_PLURAL` - Units of work
- `TASK_VERB` - Main action word
- `TASK_NOUN` - Name for tasks

### Progress & Feedback (Results)
- `SECTION_ICON` - Visual separator
- `SUCCESS_WORD` - Achievement acknowledgment
- `CELEBRATION` - Victory message
- `PROGRESS_UNIT` - Measurement of advancement

### Narrative Flavor (Tone)
- `OPENING_FLAVOR` - Hook at exercise start
- `TRANSITION_WORD` - Between sections
- `CLOSING_FLAVOR` - Final message

## Tips for Theme Creators

### ✅ DO:
- Keep variables internally consistent (all military OR all sports, not mixed)
- Use singular/plural correctly (COMPONENT_SINGULAR vs COMPONENT_PLURAL)
- Match formality levels (formal mentor → formal celebration)
- Test phrases out loud: "cast your spell" vs "execute your drill"

### ❌ DON'T:
- Mix metaphors (fantasy wizard in a soccer stadium)
- Use overly long values (keep ROLE_TITLE to 1-2 words)
- Change placeholder names (must match template expectations)
- Add new variables (templates won't recognize them)

## Example Themes to Inspire You

**Detective Agency:**
- ROLE_TITLE: "Detective"
- PROJECT_TYPE: "case investigation"
- COMPONENT_PLURAL: "clues"
- CELEBRATION: "Case closed!"

**Sci-Fi Engineering:**
- ROLE_TITLE: "Engineer"
- PROJECT_TYPE: "starship system"
- COMPONENT_PLURAL: "modules"
- CELEBRATION: "Systems online!"

**Military Operations:**
- ROLE_TITLE: "Commander"
- PROJECT_TYPE: "tactical operation"
- COMPONENT_PLURAL: "objectives"
- CELEBRATION: "Mission complete!"

**Restaurant Management:**
- ROLE_TITLE: "Chef"
- PROJECT_TYPE: "signature menu"
- COMPONENT_PLURAL: "recipes"
- CELEBRATION: "Service excellent!"

## Integration

Theme mapping files are used by:

1. **Maya Chat app**: Reads theme at runtime and applies to exercise narratives
2. **Conversion script**: Can validate that exercises work across multiple themes
3. **Content creators**: Reference when writing new exercises

See `docs/NARRATIVE_THEME_INFRASTRUCTURE.md` for technical details.

## Questions?

This system is designed to be simple:
- **One JSON file** = One theme
- **20 variables** = Complete narrative customization
- **Zero template changes** = Works immediately

If something doesn't make sense, check `professional_coding.json` - it's the clearest example with minimal metaphor.
