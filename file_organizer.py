"""
Synent Technologies - Task 5: File Organizer
Level  : Intermediate
Author : Intern

Automatically sorts files in a directory into categorized subfolders.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

# ── File type categories ───────────────────────────────────────
CATEGORIES = {
    "Images"     : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff"],
    "Videos"     : [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm", ".m4v"],
    "Audio"      : [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"],
    "Documents"  : [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".odt"],
    "Code"       : [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".json", ".xml", ".sh"],
    "Archives"   : [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Executables": [".exe", ".msi", ".dmg", ".apk", ".deb", ".rpm"],
    "Data"       : [".csv", ".sql", ".db", ".sqlite", ".yaml", ".yml"],
}

def get_category(extension):
    ext = extension.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def log_message(log_lines, msg):
    print(msg)
    log_lines.append(msg)

def organize_directory(target_dir):
    target_path = Path(target_dir).resolve()

    if not target_path.exists():
        print(f"   Directory not found: {target_path}")
        return

    print("\n" + "=" * 55)
    print(f"   Organizing: {target_path}")
    print("=" * 55)

    files = [f for f in target_path.iterdir() if f.is_file()]

    if not files:
        print("  ℹ  No files found to organize.")
        return

    log_lines = []
    moved = 0
    skipped = 0
    category_counts = {}

    for file in files:
        # Skip the log file itself or hidden files
        if file.name.startswith('.') or file.suffix == '.log':
            skipped += 1
            continue

        category = get_category(file.suffix)
        dest_folder = target_path / category

        # Create category folder if it doesn't exist
        dest_folder.mkdir(exist_ok=True)

        dest_file = dest_folder / file.name

        # Avoid overwriting: rename if duplicate
        if dest_file.exists():
            stem = file.stem
            suffix = file.suffix
            counter = 1
            while dest_file.exists():
                dest_file = dest_folder / f"{stem}_{counter}{suffix}"
                counter += 1

        shutil.move(str(file), str(dest_file))
        msg = f"   {file.name:35s} → {category}/"
        log_message(log_lines, msg)

        category_counts[category] = category_counts.get(category, 0) + 1
        moved += 1

    # Write log file
    log_path = target_path / f"organizer_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    with open(log_path, 'w') as lf:
        lf.write(f"File Organizer Log — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        lf.write(f"Directory: {target_path}\n\n")
        lf.write('\n'.join(log_lines))
        lf.write(f"\n\nSummary:\n")
        for cat, count in sorted(category_counts.items()):
            lf.write(f"  {cat}: {count} file(s)\n")

    print("\n" + "─" * 55)
    print(f"  SUMMARY")
    print("─" * 55)
    for cat, count in sorted(category_counts.items()):
        print(f"  {cat:<15}: {count} file(s)")
    print("─" * 55)
    print(f"  Total moved  : {moved}")
    print(f"  Skipped      : {skipped}")
    print(f"  Log saved    : {log_path.name}")
    print("=" * 55)

def main():
    print("=" * 55)
    print("  Synent Technologies — File Organizer")
    print("=" * 55)
    print("\n  Supported categories:")
    for cat, exts in CATEGORIES.items():
        print(f"  • {cat:<14}: {', '.join(exts[:4])}{'...' if len(exts) > 4 else ''}")

    print("\n  Enter the path to the folder you want to organize.")
    print("  (Press Enter to organize the current directory)\n")

    target = input("  Folder path: ").strip()
    if not target:
        target = "."

    confirm = input(f"\n    This will MOVE files in '{os.path.abspath(target)}'.\n  Proceed? (y/n): ").strip().lower()
    if confirm == 'y':
        organize_directory(target)
    else:
        print("\n  Cancelled. No files were moved.")

if __name__ == "__main__":
    main()
