
# Using with python version below 3.5 as well
#  1
# import os

# # Get the directory of the current script
# base_path = os.path.dirname(__file__)

# # Build the full path to "my_directory"
# target_path = os.path.join(base_path, 'my_directory')

# # List the contents
# entries = os.listdir(target_path)
# for entry in entries:
#     print(entry)


# 2
'''
Directory Listing in Modern Python Versions
In modern versions of Python, an alternative to os.listdir() is to use os.scandir() and pathlib.Path().

os.scandir() was introduced in Python 3.5 and is documented in PEP 471. os.scandir() returns an iterator as opposed to a list when called:
'''

import os

# Get the directory of the current script
base_path = os.path.dirname(__file__)

# Build the full path to "my_directory"
target_path = os.path.join(base_path, 'my_directory')

# List the contents
# entries = os.scandir(target_path)
# print(entries)


# 3
'''
Here, os.scandir() is used in conjunction with the with statement because it supports the context manager protocol. Using a context manager closes the iterator and frees up acquired resources automatically after the iterator has been exhausted. The result is a print out of the filenames in my_directory/ just like you saw in the os.listdir() example:
'''
# with os.scandir(target_path) as entires:
#     for entry in entries:
#         print(entry.name)

    
# Another way to get a directory listing is to use the pathlib module:
'''
The objects returned by Path are either PosixPath or WindowsPath objects depending on the OS.
'''
# from pathlib import Path
# entries = Path(target_path)
# for entry in entries.iterdir():
#     print(entry.name)

'''
Function	Description
os.listdir()	Returns a list of all files and folders in a directory
os.scandir()	Returns an iterator of all the objects in a directory including file attribute information
pathlib.Path.iterdir()	Returns an iterator of all the objects in a directory including file attribute information
'''

# listing all files in a directory

# using os.listdir
# for entry in os.listdir(target_path):
#     if os.path.isfile(os.path.join(target_path,entry)):
#         print(entry)


# Using os.scandir

'''
An easier way to list files in a directory is to use os.scandir() or pathlib.Path():
'''

# with os.scandir(target_path) as entries:
#     for entry in entries:
#         if entry.is_file():
#             print(entry.name)


# Here’s how to list files in a directory using pathlib.Path():

from pathlib import Path

basepath = Path(target_path)

# files_in_basepath = basepath.iterdir()
# for item in files_in_basepath:
#     if item.is_file():
#         print(item.name)


# The modified version looks like this:

# files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
# for item in files_in_basepath:
#     print(item.name)


# Listing subdirectories

# 1. list all subdirectories using os.listdir

'''
Manipulating filesystem paths this way can quickly become cumbersome when you have multiple calls to os.path.join()
'''
# for entry in os.listdir(basepath):
#     if os.path.isdir(os.path.join(basepath,entry)):
#         print(entry)


# 2. lsiting os.scandir()

# with os.scandir(basepath) as entries:
#     for entry in entries:
#         if entry.is_dir():
#             print(entry.name)

# 3. using pathlib

for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)