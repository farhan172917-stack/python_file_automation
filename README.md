# File Automation Tool

A Python CLI tool for **sorting**, **renaming**, and **cleaning** files in a folder — built with the `os` module, full exception handling, operation logging, and an interactive menu.

## Files
- `file_automation.py` — the script (run with `python3 file_automation.py`)
- `sample_output.log` — example log generated from a real run (see below)

## Features
| Feature | How it's met |
|---|---|
| `os` module | `os.listdir`, `os.path.*`, `os.makedirs`, `os.rename`, `os.remove`, `os.rmdir`, `os.walk` |
| Exception handling | Every filesystem call wrapped in `try/except OSError` (+ a top-level safety net and `KeyboardInterrupt` handling) |
| Logging | Python `logging` module writes timestamped logs to both console and `file_automation.log` |
| User input | Interactive menu (`input()`) — choose operation, target folder, rename prefix |

## Menu Options
1. **Sort** — moves files into sub-folders named `<EXT>_files/` based on extension
2. **Rename** — batch renames files to `<prefix>_001.ext`, `<prefix>_002.ext`, ...
3. **Clean** — deletes junk files (`.tmp`, `.bak`, `.cache`, `.DS_Store`) and removes empty sub-folders
4. **Exit**

## How to Run
```bash
python3 file_automation.py
```

---

## Sample Input / Output

### Starting folder: `sample_files/`
```
report.PDF   photo1.JPG   photo2.jpg   notes.txt   archive.zip
data.csv     temp.tmp     backup.bak   script.py   image.png
```

### Sample interactive session (Sort)
```
=======================================================
 FILE AUTOMATION TOOL
 Sort | Rename | Clean  -- with logging
=======================================================

What would you like to do?
  1) Sort files into folders by extension
  2) Batch rename files
  3) Clean junk files & empty folders
  4) Exit
Enter choice (1-4): 1
Enter the target folder path: sample_files

Done. See 'file_automation.log' for the full operation log.
```

### Resulting folder structure
```
sample_files/
├── PDF_files/report.PDF
├── JPG_files/photo1.JPG, photo2.jpg
├── BAK_files/backup.bak
├── ZIP_files/archive.zip
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
