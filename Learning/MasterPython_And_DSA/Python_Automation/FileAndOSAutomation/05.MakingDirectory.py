# Making Directory

'''
Function	Description
os.mkdir()	Creates a single subdirectory
pathlib.Path.mkdir()	Creates single or multiple directories
os.makedirs()	Creates multiple directories, including intermediate directories
'''

# 1 Creating a Single Directory

'''
If a directory already exists, os.mkdir() raises FileExistsError. Alternatively, you can create a directory using pathlib:
'''
import os

# Get the directory where this script is located
basepath = os.path.dirname(__file__)

# Define the new folder name
new_dir_name = "test_folder"

# Build the full path for the new directory
new_dir_path = os.path.join(basepath,new_dir_name)


# Create the directory (if it doesn't already exist)
# os.mkdir(new_dir_path)

# print the directory created at
# print(f"Directory created at: {new_dir_path}")



'''
Understanding key functions

| Function               | Description                                  |
| ---------------------- | -------------------------------------------- |
| `os.getcwd()`          | Returns current working directory            |
| `os.chdir(path)`       | Change current working directory             |
| `os.path.join(a, b)`   | Safely combine path components               |
| `os.mkdir(path)`       | Create a single directory                    |
| `os.makedirs(path)`    | Create all necessary directories recursively |
| `os.path.exists(path)` | Check if a path exists                       |
| `os.listdir(path)`     | List files and folders in a directory        |


'''

# Creating multiple indentpendt folders (using a loop)

import os 

basePath = os.path.dirname(__file__)
folders = ["images", "videos", "music", "backup"]

for folder in folders:
    folder_path = os.path.join(basePath, folder)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created multiple independent folders: {folder_path}")



# checking and listing folders

import os
base_path_1 = os.path.dirname(__file__)

if os.path.exists(base_path_1):
    print(f"Existing Folders: ")
    for name in os.listdir(base_path_1):
        path = os.path.join(base_path_1, name)
        if os.path.isdir(path):
            print(" -",name)



'''
| Mistake                                   | Error                   | Fix                             |
| ----------------------------------------- | ----------------------- | ------------------------------- |
| Forgetting `exist_ok=True`                | `FileExistsError`       | Add `exist_ok=True`             |
| Creating nested folders with `os.mkdir()` | `FileNotFoundError`     | Use `os.makedirs()`             |
| Hardcoding paths with `/` or `\`          | OS-dependent bugs       | Use `os.path.join()`            |
| Running script from wrong folder          | Wrong directory created | Use `os.path.dirname(__file__)` |

'''


# 2 Using pathlib
'''
Path(__file__).parent → gives the folder where your script is located.

base_path / "test_folder" → creates a clean, platform-independent path (no need for os.path.join).

mkdir(exist_ok=True) → creates the directory safely (won’t raise an error if it already exists).
'''
from pathlib import Path

# get the current script's folder (05.makinddirectory)
base_path = Path(__file__).parent

# define the new folder name 
new_dir = base_path / "test_folder1"

# create the directory (if it doesn't already exist)
# new_dir.mkdir(exist_ok=True)

# print(f"Direcotry created at: {new_dir} ")



# Created timestamped or dynamic Folders

import os 
from datetime import datetime

base_p = os.path.dirname(__file__)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
foler_path = os.path.join(base_p, "backups", timestamp)

os.makedirs(folder_path, exist_ok=True)

# 3 pathlib

p = Path('example_dir/')
# p.mkdir()

# if the path already exists, mkdir() raise a FileExistsError:

# To avoid errors like this, cath the rror when it happens and let your user know using try and except block

# from pathlib import Path

p = Path('example_dir')

# try:
#     p.mkdir()
# except FileExistsError as exc:
#     print(exc)


# Alternatively, we can ignore the FileExistsError by passing the exist_ok=True argument to .mkdir()

# from pathlib import Path
'''
This will not raise an error if the directory already exists.
'''
p = Path("example_dir")
# p.mkdir(exist_ok=True)


# 4 Creating Multiple Directory

'''
os.makedirs() is similar to os.mkdir(). The difference between the two is that not only can os.makedirs() create individual directories, it can also be used to create directory trees. In other words, it can create any necessary intermediate folders in order to ensure a full path exists.

os.makedirs() is similar to running mkdir -p in Bash. For example, to create a group of directories like 2018/10/05, all you have to do is the following:
'''

import os

# os.mkdir('2018/10/05')

'''
This will create a nested directory structure that contains the folders 2018, 10, and 05:

.
|
└── 2018/
    └── 10/
        └── 05/

        
.makedirs() creates directories with default permissions. If you need to create directories with different permissions call .makedirs() and pass in the mode you would like the directories to be created in:
'''

import os

# os.makedirs('2018/10/05', mode=0o770)

'''
This creates the 2018/10/05 directory structure and gives the owner and group users read, write, and execute permissions. The default mode is 0o777, and the file permission bits of existing parent directories are not changed. For more details on file permissions, and how the mode is applied, see the docs.(https://docs.python.org/3/library/os.html#os.makedirs)
'''

# Real Examples of creating multiple directory

# Example 1

# import os

# this will create all missing parent folders too

'''
Equivalent to running: 
mkdir parent
mkdir parent/child
mkdir parent/child/grandchild

'''
new_dir_name_mult = "parent/child/grandchild"
new_dir_path1 = os.path.join(basepath,new_dir_name_mult)
# os.makedirs(new_dir_path1)

# print(f"Multiple directory created at: {new_dir_path1}")


'''
Avoid Errors if Directory Already Exists

os.makedirs("parent/child/grandchild", exist_ok=True)

'''

# 5 Combine Paths Safely 
'''
Avoid hardcoding slashes (/ or \). Use os.path.join:
'''

import os 
# this will include current folder and file as well

# base = os.getcwd()

# Get the directory where this script (05.makingdirectory.py) lives
base = os.path.dirname(__file__)

new_folder = os.path.join(base,"data", "logs")
# os.makedirs(new_folder, exist_ok=True)
# print(f"Created: {new_folder}")


# 6 Using pathlib module
'''
| Line                                            | What It Does                                                                                                                                        |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from pathlib import Path`                      | Imports the `Path` class for modern path handling.                                                                                                  |
| `base = Path(__file__).parent`                  | Gets the folder containing your script (`05.makingdirectory.py`).                                                                                   |
| `new_folder = base / "data" / "logs"`           | Builds the new folder path — `pathlib` lets you use `/` for joining parts (cleaner than `os.path.join`).                                            |
| `new_folder.mkdir(parents=True, exist_ok=True)` | Creates the directories recursively. <br>✔ `parents=True` → create all missing parent folders.<br>✔ `exist_ok=True` → skip error if already exists. |
| `print(...)`                                    | Prints the full path of the created directory.                                                                                                      |

'''
from pathlib import Path


base = Path(__file__).parent

# define the new folder path (data/logs)

new_folder = base / "youtbe" / "insta"

# create the folders (includign parents if missing)

# new_folder.mkdir(parents=True, exist_ok=True)
# print(f"Created multiple directory using pathlib: {new_folder}")


'''
Why path lib is better

| Feature             | `os` module          | `pathlib`                                                   |
| ------------------- | -------------------- | ----------------------------------------------------------- |
| Style               | Procedural           | Object-Oriented                                             |
| Path joining        | `os.path.join(a, b)` | `Path(a) / b`                                               |
| Readability         | Medium               | Excellent                                                   |
| Works across OS     | ✅                    | ✅                                                           |
| File/Folder actions | Separate `os` calls  | Built-in methods like `.mkdir()`, `.exists()`, `.iterdir()` |

'''


# Parameters of mkdir()

'''
| Parameter  | Default | Description                                                     |
| ---------- | ------- | --------------------------------------------------------------- |
| `mode`     | `0o777` | Permissions for the new folder (ignored on Windows).            |
| `parents`  | `False` | If `True`, creates all parent directories if missing.           |
| `exist_ok` | `False` | If `True`, doesn’t raise an error if the folder already exists. |

'''

# Creating multiple Unrelated directories (loop)

# from pathlib import Path

# base = Path(__file__).parent
# folders = ["images", "videos", "music", "backup"]

# for name in folders:
#     folder = base / name
#     folder.mkdir(exist_ok=True)
#     print(f"Created Folder: {folder}")


# Creating TImestamped or dynamic folders

# You can use variables like dates, user input, or counters in folder names

# Example: Timestamped Folder

from pathlib import Path
from datetime import datetime

base = Path(__file__).parent / "backups"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = base / timestamp

# backup_folder.mkdir(parents=True, exist_ok=True)
# print(f"Backup folder created: {backup_folder}")

# 7. Verifying and Listing Created Directories

from pathlib import Path

base = Path(__file__).parent

# print("Crrent directories: ")
# for item in base.iterdir():
#     if item.is_dir():
#         print(" -", item.name)
    


# Common mistakes and fixes

'''
| Mistake                                                | Error               | Fix                           |
| ------------------------------------------------------ | ------------------- | ----------------------------- |
| Forgetting `parents=True` when creating nested folders | `FileNotFoundError` | Add `parents=True`            |
| Folder already exists                                  | `FileExistsError`   | Add `exist_ok=True`           |
| Using `\` or `/` manually in paths                     | OS-dependent errors | Use `/` operator in `pathlib` |

'''

# Combining Folder creation + File Writing

from pathlib import Path

base = Path(__file__).parent
reports = base / "reports" / " 2025"
# reports.mkdir(parents=True, exist_ok=True)

# file_path = reports / "summary.txt"
# file_path.write_text("report generated successfully!")

# print(f" file created at: {file_path}")
