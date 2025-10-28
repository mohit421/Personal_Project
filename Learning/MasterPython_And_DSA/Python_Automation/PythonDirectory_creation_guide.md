# 📂 Python Directory Creation Guide

### Using `os` and `pathlib` Modules (Beginner → Advanced)

---

## 🧠 Overview

Python provides two main ways to create and manage directories (folders):

| Module    | Style                    | Ideal For                                |
| --------- | ------------------------ | ---------------------------------------- |
| `os`      | Procedural / Legacy      | Older codebases, system-level operations |
| `pathlib` | Object-Oriented / Modern | Clean, readable, cross-platform code     |

This guide covers both modules with detailed explanations, examples, and **interview questions**.

---

## ⚙️ Requirements

- Python 3.6+ (Recommended 3.10+)
- Cross-platform (Windows / macOS / Linux)
- No third-party dependencies

---

# 🧱 PART 1 — Using the `os` Module

---

## 🔹 1. Introduction

`os` is a built-in Python module that provides functions to interact with the operating system — including file and directory operations.

```python
import os
```

---

## 🔹 2. Creating a Single Directory

```python
import os

os.mkdir("data")
print("✅ Folder created: data")
```

📁 Creates a folder named `data` in the current working directory.

---

## 🔹 3. Creating Nested Directories

Use `os.makedirs()` for creating multiple (nested) folders.

```python
import os

os.makedirs("data/logs/archive")
print("✅ Nested directories created")
```

✅ Automatically creates missing parent folders.

---

## 🔹 4. Avoiding Errors if Folder Already Exists

```python
import os

os.makedirs("data/logs/archive", exist_ok=True)
```

✔️ Prevents `FileExistsError` if folders already exist.

---

## 🔹 5. Creating Folders Relative to Your Script

```python
import os

base_path = os.path.dirname(__file__)
target_path = os.path.join(base_path, "data", "logs")

os.makedirs(target_path, exist_ok=True)
print(f"✅ Created: {target_path}")
```

🧠 Ensures the folder is created where your script is located, not where it’s executed from.

---

## 🔹 6. Creating Multiple Independent Folders

```python
import os

base = os.path.dirname(__file__)
folders = ["images", "videos", "music", "backup"]

for folder in folders:
    path = os.path.join(base, folder)
    os.makedirs(path, exist_ok=True)
    print(f"📁 Created: {path}")
```

---

## 🔹 7. Creating Dynamic (Timestamped) Directories

```python
import os
from datetime import datetime

base = os.path.dirname(__file__)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
folder = os.path.join(base, "backups", timestamp)

os.makedirs(folder, exist_ok=True)
print(f"📦 Backup created: {folder}")
```

---

## 🔹 8. Listing Folders in a Directory

```python
import os

base = os.path.dirname(__file__)
print("📂 Folders:")

for name in os.listdir(base):
    path = os.path.join(base, name)
    if os.path.isdir(path):
        print(" -", name)
```

---

## 🔹 9. Common Mistakes

| Mistake                             | Error                    | Fix                             |
| ----------------------------------- | ------------------------ | ------------------------------- |
| Using `os.mkdir()` for nested paths | `FileNotFoundError`      | Use `os.makedirs()`             |
| Folder exists                       | `FileExistsError`        | Add `exist_ok=True`             |
| Hardcoding slashes `/` or `\`       | OS errors                | Use `os.path.join()`            |
| Wrong folder location               | Folder created elsewhere | Use `os.path.dirname(__file__)` |

---

## 🔹 10. Quick Reference — `os` Module

| Task                      | Code                                      |
| ------------------------- | ----------------------------------------- |
| Create one folder         | `os.mkdir("data")`                        |
| Create nested folders     | `os.makedirs("data/logs", exist_ok=True)` |
| Create relative to script | `os.path.dirname(__file__)`               |
| Check existence           | `os.path.exists(path)`                    |
| List folders              | `os.listdir(path)`                        |

---

# 🧩 PART 2 — Using the `pathlib` Module

---

## 🔹 1. Introduction

`pathlib` is the **modern, object-oriented** way to handle filesystem paths in Python.

```python
from pathlib import Path
```

---

## 🔹 2. Create a Single Directory

```python
from pathlib import Path

base = Path(__file__).parent
new_folder = base / "data"

new_folder.mkdir(exist_ok=True)
print(f"✅ Created: {new_folder}")
```

---

## 🔹 3. Create Nested Directories

```python
from pathlib import Path

base = Path(__file__).parent
nested = base / "data" / "logs" / "archive"

nested.mkdir(parents=True, exist_ok=True)
print(f"✅ Nested folders created: {nested}")
```

---

## 🔹 4. Create Multiple Sibling Folders

```python
from pathlib import Path

base = Path(__file__).parent
folders = ["images", "videos", "music"]

for name in folders:
    folder = base / name
    folder.mkdir(exist_ok=True)
    print(f"📁 Created: {folder}")
```

---

## 🔹 5. Create Timestamped Folder

```python
from pathlib import Path
from datetime import datetime

base = Path(__file__).parent / "backups"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

backup = base / timestamp
backup.mkdir(parents=True, exist_ok=True)

print(f"📦 Backup created: {backup}")
```

---

## 🔹 6. List Existing Folders

```python
from pathlib import Path

base = Path(__file__).parent

print("📂 Directories:")
for item in base.iterdir():
    if item.is_dir():
        print(" -", item.name)
```

---

# 🧾 PART 4 — Interview Questions & Answers

### 🟢 Beginner

**Q1:** Difference between `os.mkdir()` and `os.makedirs()`?  
**A:** `os.mkdir()` creates a single folder. `os.makedirs()` creates all required parent directories.

**Q2:** Purpose of `exist_ok=True`?  
**A:** Prevents `FileExistsError` if folder already exists.

**Q3:** What does `__file__` do?  
**A:** Returns current script file path.

---

### 🟡 Intermediate

**Q4:** Check if folder exists before creating?

```python
if not os.path.exists("data"):
    os.mkdir("data")
```

**Q5:** List only folders, not files?

```python
[name for name in os.listdir() if os.path.isdir(name)]
```

---

### 🔵 Advanced

**Q6:** When to use `pathlib` instead of `os`?  
**A:** Prefer `pathlib` for modern, cleaner, cross-platform code.

**Q7:** How to handle permission errors?

```python
try:
    os.makedirs("restricted/folder")
except PermissionError:
    print("Permission denied")
```

**Q8:** Can `os` and `pathlib` work together?  
**A:** Yes, by converting between strings and Path objects.

---

# 🏁 Conclusion

| Feature     | os         | pathlib         |
| ----------- | ---------- | --------------- |
| Style       | Procedural | Object-Oriented |
| Readability | Medium     | High            |
| Preferred   | ⚠️ Legacy  | ✅ Modern       |

✅ Use `pathlib` for clean, modern code.  
✅ Use `os` for backward compatibility.  
✅ Always include `exist_ok=True`.

---

**Author:** Python Directory Guide  
**Created:** 2025  
**License:** MIT  
**Version:** 1.0
