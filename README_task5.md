# File Organizer

**Synent Technologies — Python Development Internship**
**Task 5 | Intermediate Level**

## Description
Automatically organizes a messy directory by moving files into categorized subfolders based on file extension. Generates a timestamped log file after every run.

## Features
- Sorts files into: Images, Videos, Audio, Documents, Code, Archives, Executables, Data, Others
- Creates category folders automatically (no manual setup)
- Handles duplicate filenames by renaming intelligently
- Generates a `.log` file with a full record of what was moved
- Confirmation prompt before any files are moved
- Works on any directory you point it to

## How to Run
```bash
python file_organizer.py
```
Then enter the path to the folder you want to organize (or press Enter for current directory).

## Sample Output
```
  📂  Organizing: /home/user/Downloads
  ✅  photo.jpg                           → Images/
  ✅  report.pdf                          → Documents/
  ✅  setup.exe                           → Executables/
  ✅  archive.zip                         → Archives/
  ✅  script.py                           → Code/

  📊  SUMMARY
  ───────────────────────────────────────
  Archives      : 1 file(s)
  Code          : 1 file(s)
  Documents     : 1 file(s)
  Executables   : 1 file(s)
  Images        : 1 file(s)
  ───────────────────────────────────────
  Total moved   : 5
  Skipped       : 0
```

## Tech Used
- Python 3 standard library (`os`, `shutil`, `pathlib`, `datetime`)


