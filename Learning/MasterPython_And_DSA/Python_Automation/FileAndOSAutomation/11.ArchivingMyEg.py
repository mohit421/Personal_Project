# Archiving

# Reading ZIP files

'''
1. What Is a ZIP File?

A ZIP file is an archive that compresses multiple files or folders into one file (like data.zip).
It saves space and keeps related files together.


2. The zipfile Module in Python

Python’s built-in zipfile
 module lets you read, write, and extract ZIP files easily.

You don’t need to install anything — it’s part of the standard library.

#import zipfile


3. Reading a ZIP File (Basic Example)

Let’s say you have a ZIP file called my_data.zip in the same directory as your script.
'''

import zipfile
import os
# open a ZIP file for reading

basePath = os.path.dirname(__file__)
dirPath = os.path.join(basePath,'javascript-amazon-project-main.zip')
# print(dirPath)
# with zipfile.ZipFile(dirPath,'r') as zip_ref:
#     # list all files in the ZIP
#     # print(zip_ref.namelist())

#     # Extract all files
#     pathZ = os.path.join(basePath, "extracted_files")
#     zip_ref.extractall(pathZ)

'''
Explanation:

zipfile.ZipFile("my_data.zip", "r") opens the file in read mode.
namelist() gives you a list of all files inside.
extractall("extracted_files") extracts everything to the folder named extracted_files.
'''


'''
in Python’s zipfile module, the .getinfo() method is used to retrieve detailed information about a specific file inside a ZIP archive.
1. What .getinfo() Does
The method:

$ZipFile.getinfo(filename)

returns a ZipInfo object — which holds metadata about one file inside the ZIP.

That includes things like:
file name
original size
compressed size
modification date
permissions, etc.
'''

# Example - Basic Use of .getinfo()

import zipfile

# with zipfile.ZipFile(dirPath,'r') as zf:
#     info = zf.getinfo("javascript-amazon-project-main/styles/pages/checkout/")
    # print(info)
    # print(info.file_size)
    #  next line shows how to retrieve a file’s last modified date
    # print(info.date_time)
    # The next line shows how to get the size of the file after compression.
    # print(info.compress_size)
    # The last line shows the full path in the archive.
    # print(info.filename)

# ZipFile supports the context manager protocol, which is why you’re able to use it with the with statement


# -===============================================

# Extracting ZIP Archives

# Extracting a Single File — .extract()
'''
Use .extract(member, path=None) to extract one specific file.
'''
import zipfile

# with zipfile.ZipFile(dirPath,'r') as zf:
#     zf.extract("javascript-amazon-project-main/styles/",path='extracted_files')


'''
Explanation:

"docs/readme.txt" → the file name inside the ZIP

path="destination_Files" → the destination folder where it will be saved

If the folder doesn’t exist, Python will create it automatically

If you don’t give a path, it extracts to the current working directory
'''


# =================================-------------
# Extracting All Files — .extractall()

# To extract everything from the archive:

import zipfile

# with zipfile.ZipFile(dirPath,'r') as zf:
#     zf.extractall(basePath)


'''
Explanation:

Extracts all files and folders

Keeps the internal directory structure intact

"basepath" is the base directory for extraction
'''

'''
| Method                 | Purpose                       | Example                           |
| ---------------------- | ----------------------------- | --------------------------------- |
| `.extract(name, path)` | Extract **one file**          | `zf.extract('readme.txt', 'out')` |
| `.extractall(path)`    | Extract **all files/folders** | `zf.extractall('out')`            |

'''


# Examples:- 
# Combine .namelist() and .extract()

import zipfile

with zipfile.ZipFile(dirPath, 'r') as zf:
    for name in zf.namelist():
        if name.endswith(".csv"):
            print(f"extracting {name}...")
            zf.extract(name,"csv_Files")
'''
This extracts only the .csv files to the csv_files/ folder
'''

"""
===========================================================
📘 ZIP Extraction Examples (Base Path, .extract, .getinfo)
===========================================================

This Python file shows:

7️⃣ Using Base Path (relative to script)
8️⃣ Combining .extract() + .getinfo()
9️⃣ Extracting Password-Protected ZIPs
🔟 Full Example Workflow

Author: Your Name
-----------------------------------------------------------
"""

import os
import zipfile

# =========================================================
# 7️⃣ Using Base Path (like from Script Location)
# =========================================================
"""
Sometimes, you want to extract files relative to where your script is located.

You can use os.path.dirname(__file__) to get the directory where this script lives.
Then join that with your ZIP file name and extraction folder.
"""

# Get base directory of this script file
base_path = os.path.dirname(__file__)

# ZIP file path (replace with your actual file)
zip_path = os.path.join(base_path, "data.zip")

# Destination folder for extraction
output_path = os.path.join(base_path, "unzipped")

# Extracting all files from the ZIP
with zipfile.ZipFile(zip_path, "r") as zf:
    zf.extractall(output_path)

print(f"✅ Extracted all files to: {output_path}")

# =========================================================
# 8️⃣ Example — .extract() + .getinfo() Combo
# =========================================================
"""
You can use .getinfo() to read file metadata before extracting.
This gives details such as:
- file size
- compressed size
- modified time
- full filename in the ZIP

Then, you can use .extract() to extract that specific file.
"""

with zipfile.ZipFile("data.zip", "r") as zf:
    # Get info for one specific file inside the ZIP
    info = zf.getinfo("docs/readme.txt")

    print("\n📄 File Information Before Extracting:")
    print("Extracting:", info.filename)
    print("Compressed size:", info.compress_size, "bytes")
    print("Original size:", info.file_size, "bytes")

    # Extract only that file
    zf.extract(info, path="selected_files")

print("✅ Extracted one file into 'selected_files' folder.")

# =========================================================
# 9️⃣ Extracting Password-Protected ZIP Files
# =========================================================
"""
If your ZIP is password-protected (traditional PKZIP encryption),
you can still extract it using the pwd parameter.

⚠️ The password must be in bytes → prefix it with b"password".
"""

# Example of extracting a ZIP with password
secure_zip_path = os.path.join(base_path, "secure.zip")
secure_output_path = os.path.join(base_path, "secure_output")

# Example: only run if file exists
if os.path.exists(secure_zip_path):
    with zipfile.ZipFile(secure_zip_path, "r") as zf:
        zf.extractall(secure_output_path, pwd=b"mypassword")
        print(f"🔐 Secure ZIP extracted to: {secure_output_path}")
else:
    print("\n⚠️ No secure.zip found — skipping password-protected example.")

"""
Note:
If your ZIP uses modern AES encryption (e.g., created by 7-Zip with AES-256),
use the external library 'pyzipper' instead of 'zipfile'.
"""

# =========================================================
# 🔟 Example — Full Workflow
# =========================================================
"""
Here’s a complete working example that combines everything:
- Uses base path for flexibility
- Lists all files in ZIP
- Extracts all files
- Extracts one specific file
"""

# Define paths
project_zip = os.path.join(base_path, "project.zip")
extract_path = os.path.join(base_path, "unzipped_project")

# Open and list files
if os.path.exists(project_zip):
    with zipfile.ZipFile(project_zip, "r") as zf:
        print("\n📦 Files in ZIP:")
        for name in zf.namelist():
            print(" -", name)

        # Extract all files
        zf.extractall(extract_path)
        print(f"\n✅ All files extracted to: {extract_path}")

        # Extract one specific file
        file_name = "project/docs/readme.txt"
        if file_name in zf.namelist():
            zf.extract(file_name, extract_path)
            print(f"✅ Extracted one file: {file_name}")
        else:
            print(f"⚠️ File not found in ZIP: {file_name}")
else:
    print("\n⚠️ project.zip not found — skipping full workflow example.")

# =========================================================
# 🧠 Quick Summary
# =========================================================
"""
Method                             Description                                Notes
-----------------------------------------------------------------------------------------
.extract(name, path)               Extract one specific file                  Must pass exact filename (case-sensitive)
.extractall(path)                  Extracts all files/folders                 Keeps structure
.extractall(path, pwd=b"pass")     Extract all with password (PKZIP only)     Password must be bytes
.getinfo(name)                     Get file info (ZipInfo object)             Useful before extracting

ZipInfo attributes:
  • filename        → File path inside the ZIP
  • file_size       → Uncompressed file size (bytes)
  • compress_size   → Compressed file size (bytes)
  • date_time       → Tuple (year, month, day, hour, min, sec)
"""
