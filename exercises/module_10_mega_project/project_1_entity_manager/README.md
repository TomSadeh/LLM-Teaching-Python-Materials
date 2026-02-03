# Project 1: {{school}} Entity Manager

Build a complete entity management system using OOP and file persistence.

## Goal

Create a multi-file application where users can:
- Create and manage different types of entities (characters, creatures, items)
- Save data to JSON so it persists between sessions
- Export reports to CSV format
- View statistics about their collection

## File Structure

```
project_1_entity_manager/
├── main.py      # Entry point and menu
├── models.py    # Entity classes (use inheritance!)
├── storage.py   # JSON save/load
├── reports.py   # Statistics and CSV export
└── utils.py     # Helper functions (optional)
```

## What Each File Should Do

**models.py** - Define your entity classes
- A base class with shared attributes (name, type, creation date)
- Specialized subclasses with unique attributes
- Methods to display and serialize entities

**storage.py** - Handle data persistence
- Save entities to JSON
- Load entities back (reconstructing the right types)
- Handle missing files gracefully

**reports.py** - Generate output
- Calculate statistics about the collection
- Export data to CSV format

**main.py** - Tie it all together
- Interactive menu for the user
- Load data on startup, save on exit

## Success Criteria

- [ ] Multiple entity types using inheritance
- [ ] Data persists between runs
- [ ] Can export to CSV
- [ ] Handles errors gracefully
- [ ] Code organized across files

{{exclamation}} Build something you're proud of!
