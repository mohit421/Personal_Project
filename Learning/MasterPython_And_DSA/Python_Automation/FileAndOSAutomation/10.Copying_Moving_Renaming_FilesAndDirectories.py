# Copying ,Moving and Renaming Files and Directories

'''
Python ships with the shutil module. shutil is short for shell utilities. It provides a number of high-level operations on files to support copying, archiving, and removal of files and directories. In this section, you’ll learn how to move and copy files and directories.
'''
# ===========================================
# Copying Files in Python
'''
Shutil offers a couple of functions for copying files. The most commonly used functions are shutil.copy() and shutil.copy2(). To copy a file from one location to another using shutil.copy(), do the following:
'''


import os 
import shutil

basepath = os.path.dirname(__file__)

# src = os.path.join(basepath, '..', 'FileAndOSAutomation/03.GettingdirectoryListing', 'my_directory','CopyingMovingRenaming','copymove.txt')


# dst = os.path.join(basepath, '..', 'FileAndOSAutomation/03.GettingdirectoryListing', 'CopyingMovingRenamingDir')


# shutil.copy(src,dst)


'''
- shutil.copy() is comparable to the cp command in UNIX based systems. shutil.copy(src, dst) will copy the file src to the location specified in dst. 
- If dst is a file, the contents of that file are replaced with the contents of src. 

- If dst is a directory, then src will be copied into that directory. shutil.copy() only copies the file’s contents and the file’s permissions. 

- Other metadata like the file’s creation and modification times are not preserved.
'''

# -----------------------------------------
# To preserve all file metadata when copying, use shutil.copy2():

import shutil

# shutil.copy2(src,dst)

'''
Using .copy2() preserves details about the file such as last access time, permission bits, last modification time, and flags.
'''

# ==========================================
# Copying Directories

'''
While shutil.copy() only copies a single file, shutil.copytree() will copy an entire directory and everything contained in it. shutil.copytree(src, dest) takes two arguments: a source directory and the destination directory where files and folders will be copied to.
'''

# Example: Copy the contents of one folder to a different location

import os
import shutil

# Define source and destination paths
src1 = os.path.join(
    basepath, '..', 'FileAndOSAutomation', '03.GettingdirectoryListing', 
    'my_directory', 'CopyingMovingRenaming'
)

dst1 = os.path.join(
    basepath, '..', 'FileAndOSAutomation', '03.GettingdirectoryListing', 
    'CopyingMovingRenamingDir'
)

# Copy the entire folder (recursively)
shutil.copytree(src1, dst1)

'''
Explanation

shutil.copytree(src, dst) copies the entire directory tree from src to dst.

The destination directory must not already exist — copytree() will create it (and any missing parent folders).

It returns the path to the newly created destination directory.

This is a convenient way to back up or duplicate an entire folder.

✅ Example analogy:
If src1 = data_1 and dst1 = data1_backup, then after running this code you’ll have a complete copy of data_1 in data1_backup.

'''

# here’s how you can safely copy a directory even if the destination already exists, using the dirs_exist_ok=True argument (available since Python 3.8).

import os
import shutil

# Define source and destination paths
src1 = os.path.join(
    basepath, '..', 'FileAndOSAutomation', '03.GettingdirectoryListing',
    'my_directory', 'CopyingMovingRenaming'
)

dst1 = os.path.join(
    basepath, '..', 'FileAndOSAutomation', '03.GettingdirectoryListing',
    'CopyingMovingRenamingDir'
)

# Copy the entire folder — overwriting existing files if needed
shutil.copytree(src1, dst1, dirs_exist_ok=True)


# =============
# dirs_exist_ok=True tells Python that it’s okay if the destination folder (dst1) already exists.
# Without this flag, shutil.copytree() would raise:

# FileExistsError: [Errno 17] File exists: 'destination_path'

'''
Existing files in the destination will be overwritten if they have the same name as files in the source.

New files or folders in the source will be copied over.
'''

# Optional — safer overwrite behavior

# If you want to avoid overwriting existing files, you can add a manual check:
import os
import shutil

if not os.path.exists(dst1):
    shutil.copytree(src1, dst1)
else:
    print(f"Destination already exists: {dst1}")


# -------------==============================================--------------

# Moving Files and Directories

'''
Moving files and directories is a common task when automating file organization, backups, or restructuring folders.
The shutil and os modules are typically used for this.
'''

# 1 Using shutil.move()

# shutil.move(src, dst)

'''
Parameters

src → The path of the file or directory you want to move
dst → The destination path (can include a new filename or directory).

Returns
It returns the destination path (a string).

'''

# Example 1 — Moving a file

import shutil
import os

basepath = os.getcwd()
print(f"basepath is: {basepath}")
# Define source and destination
src_file = os.path.join(basepath, 'data', 'report.txt')
dst_dir = os.path.join(basepath, 'archive')

# Move the file
shutil.move(src_file, dst_dir)
print("File moved successfully!")



# Moving a directory

import shutil
import os

src_dir = os.path.join('projects', 'drafts')
dst_dir = os.path.join('projects', 'completed')

shutil.move(src_dir, dst_dir)
print("Directory moved successfully!")


'''
Explanation

If dst_dir already exists, the source folder is moved into it.
Example: moving drafts into completed will result in completed/drafts.

If dst_dir doesn’t exist, it will be renamed to that new location.
'''

'''
Example 3 — Handling existing destination

If the destination file already exists, Python will overwrite it.
'''

import os
import shutil

src = 'data/report.txt'
dst = 'archive/report.txt'

if os.path.exists(dst):
    print(f"File already exists at {dst}. Renaming before move...")
    base, ext = os.path.splitext(dst)
    dst = f"{base}_old{ext}"

shutil.move(src, dst)



# Example 4 — Moving with exception handling
# It’s a good habit to wrap file operations in try/except blocks:

import shutil

try:
    shutil.move('data/report.txt', 'archive/report.txt')
    print("File moved successfully!")
except FileNotFoundError:
    print("Source file not found.")
except PermissionError:
    print("Permission denied — check file access rights.")
except Exception as e:
    print(f"Error: {e}")


'''
Notes and Best Practices

✅ Use absolute paths (os.path.join(os.getcwd(), ...)) to avoid confusion when running scripts from different directories.

⚠️ Be cautious with overwriting — shutil.move() will overwrite files without warning.

🧹 Clean up after moving — once you’ve verified the move, you can safely remove old directories if needed.

🕵️ Use os.rename() for simple renames within the same filesystem:

os.rename('old_name.txt', 'new_name.txt')


But prefer shutil.move() for cross-disk or directory moves — it handles more cases.

💾 Cross-platform support — works on Windows, macOS, and Linux.


Comparison Table

| Task                                | Recommended Function               | Notes                                |
| ----------------------------------- | ---------------------------------- | ------------------------------------ |
| Move a single file                  | `shutil.move()`                    | Automatically handles rename or move |
| Move entire directory               | `shutil.move()`                    | Works recursively                    |
| Rename file/folder (same directory) | `os.rename()`                      | Faster if no directory change        |
| Check if path exists                | `os.path.exists()`                 | Prevent overwriting                  |
| Create destination directory        | `os.makedirs(path, exist_ok=True)` | Creates intermediate folders         |


'''

# Example 5 — Full workflow demo

# Here’s a more complete script showing everything together:

import os
import shutil

basepath = os.getcwd()

src_dir = os.path.join(basepath, 'data', 'draft_reports')
dst_dir = os.path.join(basepath, 'data', 'final_reports')

# Ensure destination exists
os.makedirs(dst_dir, exist_ok=True)

# Loop through all files in source directory
for filename in os.listdir(src_dir):
    src_path = os.path.join(src_dir, filename)
    dst_path = os.path.join(dst_dir, filename)

    # Move file
    shutil.move(src_path, dst_path)
    print(f"Moved: {filename}")

print("All files moved successfully!")


'''
Summary

| Concept                     | Function                           | Description                                      |
| --------------------------- | ---------------------------------- | ------------------------------------------------ |
| Move file or directory      | `shutil.move(src, dst)`            | Moves or renames files/directories               |
| Rename file                 | `os.rename(old, new)`              | Only renames or moves within the same filesystem |
| Handle existing destination | Check with `os.path.exists()`      | Avoid overwriting                                |
| Create destination folder   | `os.makedirs(path, exist_ok=True)` | Ensures destination exists before moving         |

'''


# --------------------------------------------

# Renaming Files and Directories

# Python includes os.rename(src, dst) for renaming files and directories:

os.rename('first.zip', 'first_01.zip')

# The line above will rename first.zip to first_01.zip. If the destination path points to a directory, it will raise an OSError.


# ============-------------
# Another way to rename files or directories is to use rename() from the pathlib module:



from pathlib import Path
data_file = Path('data_01.txt')
data_file.rename('data.txt')


'''
To rename files using pathlib, you first create a pathlib.Path() object that contains a path to the file you want to replace. The next step is to call rename() on the path object and pass a new filename for the file or directory you’re renaming.
'''