# Deleting Files and Directories

'''
You can delete single files, directories, and entire directory trees using the methods found in the os, shutil, and pathlib modules. The following sections describe how to delete files and directories that you no longer need.
'''
# Deleting FIles in Python

# To delete a single file, use pathlib.Path.unlink(), os.remove(). or os.unlink(). os.remove() and os.unlink() are semantically identical. To delete a file using os.remove(), do the following:

import os 

basepath = os.path.dirname(__file__)

target_path = os.path.join(basepath, '..', 'FileAndOSAutomation/03.GettingdirectoryListing', 'my_directory','file_del.txt')
# os.unlink(target_path)
# os.remove(target_path)

# print(target_path)


'''
Calling .unlink() or .remove() on a file deletes the file from the filesystem. These two functions will throw an OSError if the path passed to them points to a directory instead of a file. To avoid this, you can either check that what you’re trying to delete is actually a file and only delete it if it is
'''

# use exception handling to handle the OSError:

# import os

# if os.path.isfile(target_path):
#     os.remove(target_path)
# else:
#     print(f'Error: {target_path} not a valid filename')


'''
os.path.isfile() checks whether data_file is actually a file. If it is, it is deleted by the call to os.remove(). If data_file points to a folder, an error message is printed to the console.
'''

# The following example shows how to use exception handling to handle errors when deleting files:

# import os 

# use exception handling 
# try:
#     os.remove(target_path)
# except OSError  as e:
#     print(f"Error: {target_path} : {e.strerror}")


# --------------------------------------------
# Using Pathlib

# Finally, you can also use pathlib.Path.unlink() to delete files:

from pathlib import Path

# data_file = Path(target_path)
# try:
#     data_file.unlink()
# except IsADirectoryError as e:
#     print(f'Error: {data_file} : {e.strerror}')

'''
This creates a Path object called data_file that points to a file. Calling .remove() on data_file will delete home/data.txt. If data_file points to a directory, an IsADirectoryError is raised. It is worth noting that the Python program above has the same permissions as the user running it. If the user does not have permission to delete the file, a PermissionError is raised.
'''

# ========================================================

# Deleting Directories
'''
The standard library offers the following functions for deleting directories:

1. os.rmdir()
2. pathlib.Path.rmdir()
3. shutil.rmtree()

To delete a single directory or folder, use os.rmdir() or pathlib.rmdir(). These two functions only work if the directory you’re trying to delete is empty. If the directory isn’t empty, an OSError is raised. Here is how to delete a folder:
'''

dir_path = os.path.join(basepath, '..', 'FileAndOSAutomation/03.GettingdirectoryListing', 'my_directory','delte_fold')
trash_dir = dir_path

# try:
#     os.rmdir(trash_dir)
# except OSError as e:
#     print(f'Error: {trash_dir} : {e.strerror}')


'''
Here, the trash_dir directory is deleted by passing its path to os.rmdir(). If the directory isn’t empty, an error message is printed to the screen:

Traceback (most recent call last):
  File '<stdin>', line 1, in <module>
OSError: [Errno 39] Directory not empty: 'my_documents/bad_dir'


'''

# ----------------------------------------------

# Using pathlib 
# Alternatively, you can use pathlib to delete directories:

from pathlib import Path

pathlib_dir = Path(dir_path)

# try:
#     pathlib_dir.rmdir()
# except OSError as e:
#     print(f'Error: {pathlib_dir} : {e.strerror}')


'''
Here, you create a Path object that points to the directory to be deleted. Calling .rmdir() on the Path object will delete it if it is empty.
'''

# =================================
# Deleting Entire Directory Trees

# To delete non-empty directories and entire directory trees, Python offers shutil.rmtree():

import shutil

# sh_path = trash_dir

try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')


'''
Everything  is deleted when shutil.rmtree() is called on on any directory. There may be cases where you want to delete empty folders recursively.
We do this using one of the methods discussed above in conjunction with os.walk():
'''

import os

# for dirpath, dirnames, files in os.walk('.', topdown=False):
#     try:
#         os.rmdir(dirpath)
#     except OSError as ex:
#         pass


'''
This walks down the directory tree and tries to delete each directory it finds. If the directory isn’t empty, an OSError is raised and that directory is skipped. The table below lists the functions covered in this section:



Function	Description
os.remove()	Deletes a file and does not delete directories
os.unlink()	Is identical to os.remove() and deletes a single file
pathlib.Path.unlink()	Deletes a file and cannot delete directories
os.rmdir()	Deletes an empty directory
pathlib.Path.rmdir()	Deletes an empty directory
shutil.rmtree()	Deletes entire directory tree and can be used to delete non-empty directories
'''



