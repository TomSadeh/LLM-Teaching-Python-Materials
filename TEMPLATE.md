# Exercise Template Variables

This document explains how to use theme variables in exercises so they dynamically adapt to the user's selected theme.

## Syntax

Use `{{variable_name}}` in exercise content. These placeholders are replaced at runtime with theme-specific values.

## Available Variables

| Variable | Description | Example (dumblecode) |
|----------|-------------|---------------------|
| `{{hero}}` | Male protagonist | Harry Potter |
| `{{heroine}}` | Female protagonist | Hermione Granger |
| `{{friend}}` | Best friend/sidekick | Ron Weasley |
| `{{mentor}}` | Teacher/guide figure | Dumbledore |
| `{{villain}}` | Antagonist | Voldemort |
| `{{school}}` | Main school/location | Hogwarts |
| `{{house}}` | Sub-group/house | Gryffindor |
| `{{spell1}}` | Simple ability | Lumos |
| `{{spell2}}` | Combat ability | Expelliarmus |
| `{{spell3}}` | Advanced ability | Expecto Patronum |
| `{{spell4}}` | Utility ability | Wingardium Leviosa |
| `{{creature}}` | Magical creature | hippogriff |
| `{{pet}}` | Character's pet | Hedwig the owl |
| `{{location}}` | Adventure location | the Forbidden Forest |
| `{{place}}` | Famous place | Diagon Alley |
| `{{item}}` | Special item | wand |
| `{{transport}}` | Transportation | Nimbus 2000 |
| `{{group}}` | Team/organization | Dumbledore's Army |
| `{{exclamation}}` | Themed exclamation | By Merlin's beard! |
| `{{greeting}}` | Welcome message | Welcome to Hogwarts! |
| `{{password}}` | Password/code word | Caput Draconis |

## Example

**Template:**
```python
# Create a variable called 'hero' with "{{hero}}"
# Print: "{{greeting}}, {{hero}}!"
```

**Rendered (dumblecode theme):**
```python
# Create a variable called 'hero' with "Harry Potter"
# Print: "Welcome to Hogwarts!, Harry Potter!"
```

**Rendered (pyfire theme):**
```python
# Create a variable called 'hero' with "Keefe Sencen"
# Print: "Welcome to Foxfire!, Keefe Sencen!"
```

## Guidelines

1. **Keep it simple** - Use one or two variables per exercise, not all of them
2. **Context matters** - Use `{{heroine}}` for female-led examples, `{{hero}}` for male
3. **Be consistent** - If an exercise mentions `{{hero}}`, keep using `{{hero}}` throughout
4. **Fallback** - The `pymentor` theme has generic values for non-fantasy mode

## Theme Reference

See `theme_variables.json` for the complete mapping of all variables to all themes.

The themes are:

### Fantasy Themes
- `dumblecode` - Harry Potter (Hogwarts magic school)
- `chirthon` - Percy Jackson (Greek mythology demigods)
- `compile-games` - Hunger Games (dystopian survival)
- `pyfire` - Keeper of the Lost Cities (elven telepaths)
- `dnd-srd` - D&D SRD (classic fantasy adventuring) ✨ **Open license**

### Sci-Fi Themes
- `cepheus` - Cepheus Engine (space exploration, Traveller-like) ✨ **Open license**

### Plain Theme
- `pymentor` - Plain/generic (no fantasy, no sci-fi)
