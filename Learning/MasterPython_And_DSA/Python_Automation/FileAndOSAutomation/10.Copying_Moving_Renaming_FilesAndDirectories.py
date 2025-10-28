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


# Here’s an example of how to copy the contents of one folder to a different location:

src1 = os.path.join(basepath, '..', 'FileAndOSAutomation/03.GettingdirectoryListing', 'my_directory','CopyingMovingRenaming')


dst1 = os.path.join(basepath, '..', 'FileAndOSAutomation/03.GettingdirectoryListing', 'CopyingMovingRenamingDir')

shutil.copytree(src1,dst1)



'''
In this example, .copytree() copies the contents of data_1 to a new location data1_backup and returns the destination directory. The destination directory must not already exist. It will be created as well as missing parent directories. shutil.copytree() is a good way to back up your files.
'''