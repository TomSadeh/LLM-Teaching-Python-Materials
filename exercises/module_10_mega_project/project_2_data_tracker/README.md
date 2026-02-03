# Project 2: {{school}} Data Tracker

Build a data tracking application with CSV storage and analysis.

## Goal

Create a multi-file application that:
- Records observations/events with multiple fields
- Stores data in CSV format (viewable in spreadsheets)
- Provides search and filter capabilities
- Generates statistics and summaries

## File Structure

```
project_2_data_tracker/
├── main.py        # Entry point and menu
├── tracker.py     # Record creation, validation, filtering
├── data_io.py     # CSV read/write operations
├── analyzer.py    # Statistics and analysis
└── config.py      # Field definitions and settings
```

## What Each File Should Do

**config.py** - Define your data structure
- What fields each record has
- Valid categories
- Default settings

**tracker.py** - Manage records
- Create new records
- Validate required fields
- Filter and search capabilities

**data_io.py** - Handle CSV files
- Save records to CSV
- Load records from CSV
- Handle missing files gracefully

**analyzer.py** - Generate insights
- Count records by category, location, etc.
- Find date ranges
- Create summary reports

**main.py** - Tie it all together
- Interactive menu for the user
- Load data on startup

## Success Criteria

- [ ] Records stored in CSV format
- [ ] Can search and filter records
- [ ] Statistics show meaningful insights
- [ ] Handles errors gracefully
- [ ] Code organized across files

{{exclamation}} Build something you're proud of!
