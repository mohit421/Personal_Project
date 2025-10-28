# FilenamePattern Matching

'''
After getting a list of files in a directory using one of the methods above, you will most probably want to search for files that match a particular pattern.

These are the methods and functions available to you:

endswith() and startswith() string methods
fnmatch.fnmatch()
glob.glob()
pathlib.Path.glob()

Each of these is discussed below. The examples in this section will be performed on a directory called some_directory that has the following structure:

.
|
├── sub_dir/
|   ├── file1.py
|   └── file2.py
|
├── admin.py
├── data_01_backup.txt
├── data_01.txt
├── data_02_backup.txt
├── data_02.txt
├── data_03_backup.txt
├── data_03.txt
└── tests.py

If you’re following along using a Bash shell, you can create the above directory structure using the following commands:

$ mkdir some_directory
$ cd some_directory/
$ mkdir sub_dir
$ touch sub_dir/file1.py sub_dir/file2.py
$ touch data_{01..03}.txt data_{01..03}_backup.txt admin.py tests.py
'''

# 1 Using string Methods

'''
Python has several built-in methods for modifying and manipulating strings. Two of these methods, .startswith() and .endswith(), are useful when you’re searching for patterns in filenames. To do this, first get a directory listing and then iterate over it
'''

import os
# Get .txt files

basepath = os.path.dirname(__file__)

# for f_name in os.listdir(basepath):
#     if f_name.endswith('.txt'):
#         print(f_name)



# Simple Filename Pattern Matching Using fnmatch
'''
String methods are limited in their matching abilities. fnmatch has more advanced functions and methods for pattern matching. We will consider fnmatch.fnmatch(), a function that supports the use of wildcards such as * and ? to match filenames. For example, in order to find all .txt files in a directory using fnmatch, you would do the following:
'''

import fnmatch

# for file_name in os.listdir(basepath):
#     if fnmatch.fnmatch(file_name,'*.txt'):
#         print(file_name)


# More advanced pattern matching

'''
Let’s suppose you want to find .txt files that meet certain criteria. For example, you could be only interested in finding .txt files that contain the word data, a number between a set of underscores, and the word backup in their filename. Something similar to data_01_backup, data_02_backup, or data_03_backup.
'''


# for file_name in os.listdir(basepath):
#     if fnmatch.fnmatch(file_name, 'data_*_backup.txt'):
#         print(file_name)



# Filename pattern matching using glob

'''
Another useful module for pattern matching is glob.

.glob() in the glob module works just like fnmatch.fnmatch(), but unlike fnmatch.fnmatch(), it treats files beginning with a period (.) as special.

UNIX and related systems translate name patterns with wildcards like ? and * into a list of files. This is called globbing.


For example, typing mv *.py python_files/ in a UNIX shell moves (mv) all files with the .py extension from the current directory to the directory python_files. The * character is a wildcard that means “any number of characters,” and *.py is the glob pattern. This shell capability is not available in the Windows Operating System. The glob module adds this capability in Python, which enables Windows programs to use this feature.
'''

# example of how to use glob to search for all Python (.py) source files in the current directory:

import glob

src_file = glob.glob('*.py')
# print(f"Glob .py files: {src_file}")


for name in glob.glob('*[0-9]*.txt'):
    print(name)

# glob makes it easy to search for files recursively in subdirectories too:

for file in glob.iglob('**/*.py',recursive=True):
    print(file)

'''
This example makes use of glob.iglob() to search for .py files in the current directory and subdirectories. Passing recursive=True as an argument to .iglob() makes it search for .py files in the current directory and any subdirectories. The difference between glob.iglob() and glob.glob() is that .iglob() returns an iterator instead of a list.
'''


# using pathlib contains similar methods for making flexible file listings. the example below shows how we can use .Path.glob() to list file types that start with the letter p:


from pathlib import Path

p = Path('.')
for name in p.glob('*.p*'):
    print(name)

'''
Calling p.glob('*.p*') returns a generator object that points to all files in the current directory that start with the letter p in their file extension.

Path.glob() is similar to os.glob() discussed above. As you can see, pathlib combines many of the best features of the os, os.path, and glob modules into one single module, which makes it a joy to use.
'''

'''
Function	Description
startswith()	Tests if a string starts with a specified pattern and returns True or False
endswith()	Tests if a string ends with a specified pattern and returns True or False
fnmatch.fnmatch(filename, pattern)	Tests whether the filename matches the pattern and returns True or False
glob.glob()	Returns a list of filenames that match a pattern
pathlib.Path.glob()	Finds patterns in path names and returns a generator object
'''
