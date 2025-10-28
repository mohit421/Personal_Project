# Getting file attributes

'''
Python makes retrieving file attributes such as file size and modified times easy. This is done through os.stat(), os.scandir(), or pathlib.Path().

os.scandir() and pathlib.Path() retrieve a directory listing with file attributes combined. This can be potentially more efficient than using os.listdir() to list files and then getting file attribute information for each file.
'''

# 1

'''
The examples below show how to get the time the files in my_directory/ were last modified. The output is in seconds:

'''

import os
from datetime import datetime  # Optional, for readable timestamps

# Get the directory of the current script (04.GettingFileAttributes)
base_path = os.path.dirname(__file__)

# Go UP one folder and then into 03.GettingdirectoryListing/my_directory
target_path = os.path.join(base_path, '..', 'FileAndOSAutomation/03.GettingdirectoryListing', 'my_directory')

# Normalize the path (resolves ".." to the actual absolute path)
target_path = os.path.abspath(target_path)

# Check that the directory exists before scanning
if os.path.exists(target_path):
    with os.scandir(target_path) as dir_contents:
        for entry in dir_contents:
            info = entry.stat()  # ✅ Correct method
            # Convert modification time to readable format
            print(info.st_mtime)
            # modified_time = datetime.fromtimestamp(info.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            # print(f"{entry.name:20}  Modified: {modified_time}")
else:
    print(f"❌ Directory not found: {target_path}")



# The pathlib module has corresponding methods for retrieving file information that give the same results:

# The st_mtime attribute returns a float value that represents seconds since the epoch.
from pathlib import Path

current_dir = Path(target_path)
for path in current_dir.iterdir():
    info = path.stat()
    print(info.st_mtime)



#  you could write a helper function to convert the seconds into a datetime object:

from datetime import datetime
from os  import scandir

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date

def get_files():
    dir_entries = scandir(target_path)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t Last modified: {convert_date(info.st_mtime)}')

get_files()