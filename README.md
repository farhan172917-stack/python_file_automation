# File Automation Tool

A simple Python automation tool for **sorting, renaming, and cleaning files** in a folder.

The project uses the `os` module, exception handling, logging, and user input to perform common file-management tasks automatically.

## Features

* **Sort Files** — Organizes files into folders according to their file extensions.
* **Rename Files** — Renames multiple files using a prefix and sequence number.
* **Clean Files** — Removes junk files such as `.tmp`, `.bak`, `.cache`, and `.DS_Store`, and removes empty folders.
* **Exception Handling** — Handles file and folder errors safely.
* **Logging** — Records file operations in a log file.
* **User Input** — Allows the user to select an operation and enter a folder path.

## Requirements

* Python 3
* No external Python libraries are required.

## Project Structure

```text
python_file_automation/
│
├── file_automation.py
├── README.md
├── sample_output.log
│
├── sample_files/
│   ├── photo.jpg
│   ├── document.pdf
│   ├── notes.txt
│   ├── data.csv
│   ├── program.py
│   ├── song.mp3
│   ├── temp.tmp
│   └── backup.bak
│
├── rename_test/
│   ├── apple.txt
│   ├── mango.txt
│   └── orange.txt
│
└── clean_test/
    ├── keep.txt
    ├── temp.tmp
    ├── backup.bak
    └── empty_folder/
```

## How to Run

Open Terminal and go to the project folder:

```bash
cd python_file_automation
```

Run the program:

```bash
python3 file_automation.py
```

## Menu

```text
=============================================
       FILE AUTOMATION TOOL
=============================================

Choose an operation:
1. Sort Files
2. Rename Files
3. Clean Files
4. Exit
```

## 1. Sort Files

Select:

```text
1
```

Then enter:

```text
sample_files
```

The program organizes files according to their extensions.

Example:

```text
sample_files/
├── JPG_files/
│   └── photo.jpg
├── PDF_files/
│   └── document.pdf
├── TXT_files/
│   └── notes.txt
├── CSV_files/
│   └── data.csv
├── PY_files/
│   └── program.py
├── MP3_files/
│   └── song.mp3
├── TMP_files/
│   └── temp.tmp
└── BAK_files/
    └── backup.bak
```

## 2. Rename Files

Select:

```text
2
```

Then enter the folder:

```text
rename_test
```

Enter a prefix:

```text
fruit
```

Example output:

```text
Renamed: apple.txt -> fruit_001.txt
Renamed: mango.txt -> fruit_002.txt
Renamed: orange.txt -> fruit_003.txt
```

## 3. Clean Files

Select:

```text
3
```

Then enter:

```text
clean_test
```

The program removes junk files and empty folders.

Example:

```text
Deleted: temp.tmp
Deleted: backup.bak
Removed empty folder: empty_folder
Cleaning completed. Files deleted: 2
```

## Logging

The program automatically creates:

```text
file_automation.log
```

The log records operations such as:

```text
2026-09-16 20:15:04 | INFO | === New session started ===
2026-09-16 20:15:04 | INFO | Starting SORT operation
2026-09-16 20:15:04 | INFO | Moved photo.jpg -> JPG_files/
2026-09-16 20:15:04 | INFO | Moved document.pdf -> PDF_files/
2026-09-16 20:15:04 | INFO | SORT operation completed
```

A sample log is included in the repository as:

```text
sample_output.log
```

## Assignment Requirements

| Requirement        | Implementation                                                       |
| ------------------ | -------------------------------------------------------------------- |
| OS Module          | `os.listdir()`, `os.path`, `os.rename()`, `os.remove()`, `os.walk()` |
| Exception Handling | `try` / `except` blocks for file operations                          |
| Logging            | Python `logging` module                                              |
| User Input         | `input()` for menu, folder path, and rename prefix                   |
| File Operations    | Sorting, renaming, and cleaning                                      |

## Sample Input

```text
Enter choice (1-4): 1
Enter folder path: sample_files
```

## Sample Output

```text
--- Sorting Files ---
Moved: photo.jpg -> JPG_files/
Moved: document.pdf -> PDF_files/
Moved: notes.txt -> TXT_files/
Sorting completed.
```

## Author

**Md Farhan Khan**

Python File Automation Project
├── CSV_files/data.csv
├── TXT_files/notes.txt
├── PY_files/script.py
├── TMP_files/temp.tmp
└── PNG_files/image.png
```

### Log output (file_automation.log)
```
2026-09-16 15:13:00 | INFO | === New session started ===
2026-09-16 15:13:00 | INFO | Starting SORT operation in: /home/claude/demo/sample_files
2026-09-16 15:13:00 | INFO | Moved 'report.PDF' -> 'PDF_files/'
2026-09-16 15:13:00 | INFO | Moved 'photo2.jpg' -> 'JPG_files/'
2026-09-16 15:13:00 | INFO | Moved 'photo1.JPG' -> 'JPG_files/'
2026-09-16 15:13:00 | INFO | Moved 'backup.bak' -> 'BAK_files/'
2026-09-16 15:13:00 | INFO | Moved 'archive.zip' -> 'ZIP_files/'
2026-09-16 15:13:00 | INFO | Moved 'data.csv' -> 'CSV_files/'
2026-09-16 15:13:00 | INFO | Moved 'notes.txt' -> 'TXT_files/'
2026-09-16 15:13:00 | INFO | Moved 'script.py' -> 'PY_files/'
2026-09-16 15:13:00 | INFO | Moved 'temp.tmp' -> 'TMP_files/'
2026-09-16 15:13:00 | INFO | Moved 'image.png' -> 'PNG_files/'
2026-09-16 15:13:00 | INFO | SORT complete. Moved: 10, Skipped: 0, Failed: 0
```

### Rename example
Input: `apple.txt`, `mango.txt`, `zebra.txt` (prefix = `vacation`)
Output: `vacation_001.txt`, `vacation_002.txt`, `vacation_003.txt`

### Clean example
Input: `keep.txt`, `junk1.tmp`, `junk2.bak`, empty folder `empty_sub/`
Output: only `keep.txt` remains; junk files and the empty folder are deleted.

---

## GitHub
Push `file_automation.py` (and optionally this README) to a public/private repo, e.g.:
```bash
git init
git add file_automation.py README.md
git commit -m "Add file automation tool: sort, rename, clean with logging"
git remote add origin <your-repo-url>
git push -u origin main
```
