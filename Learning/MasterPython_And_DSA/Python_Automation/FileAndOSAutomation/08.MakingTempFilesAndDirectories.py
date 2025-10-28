# Making Temporary Files and Directories

'''
Python provides a handy module for creating temporary files and directories called tempfile.

tempfile can be used to open and store data temporarily in a file or directory while your program is running. tempfile handles the deletion of the temporary files when your program is done with them.
'''

# Here’s how to create a temporary file:


from tempfile import TemporaryFile

# create a temporary file and write some data to it

# fp = TemporaryFile('w+t')
# fp.write("Hello universe!")

# Go back to the beginning and read data from file

# fp.seek(0)
# data = fp.read()

# close the file, after which it will be removed
# fp.close()
# 

'''
On Windows, the directories are C:\TEMP, C:\TMP, \TEMP, and \TMP, in that order. On all other platforms, the directories are /tmp, /var/tmp, and /usr/tmp, in that order. As a last resort, tempfile will save temporary files and directories in the current directory.

.TemporaryFile() is also a context manager so it can be used in conjunction with the with statement. Using a context manager takes care of closing and deleting the file automatically after it has been read:
'''

with TemporaryFile('w+t') as fp:
    fp.write('Hello Universe!')
    fp.seek(0)
    fp.read()


# example whole code

"""
08.MakingTempFilesAndDirectories.py

Demonstrates how to create and manage temporary files and directories
using Python's built-in `tempfile` module and `pathlib`.

✅ Works on Windows, macOS, and Linux
✅ Auto-cleans after use
✅ No invalid escape sequence or type errors
"""
>>> import tempfile
>>> with tempfile.TemporaryDirectory() as tmpdir:
...     print('Created temporary directory ', tmpdir)
...     os.path.exists(tmpdir)
...
Created temporary directory  /tmp/tmpoxbkrm6c
True

>>> # Directory contents have been removed
...
>>> tmpdir
'/tmp/tmpoxbkrm6c'
>>> os.path.exists(tmpdir)
False
