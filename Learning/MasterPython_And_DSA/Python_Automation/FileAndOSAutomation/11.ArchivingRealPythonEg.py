# Archiving

'''
Archives are a convenient way to package several files into one. The two most common archive types are ZIP and TAR. The Python programs you write can create, read, and extract data from archives. You will learn how to read and write to both archive formats in this section.



Reading ZIP Files:-

The zipfile module is a low level module that is part of the Python Standard Library. zipfile has functions that make it easy to open and extract ZIP files. To read the contents of a ZIP file, the first thing to do is to create a ZipFile object. ZipFile objects are similar to file objects created using open(). ZipFile is also a context manager and therefore supports the with statement:
'''

import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
    pass
    '''
    Here, you create a ZipFile object, passing in the name of the ZIP file to open in read mode. After opening a ZIP file, information about the archive can be accessed through functions provided by the zipfile module. The data.zip archive in the example above was created from a directory named data that contains a total of 5 files and 1 subdirectory:
    .
|
├── sub_dir/
|   ├── bar.py
|   └── foo.py
|
├── file1.py
├── file2.py
└── file3.py
    '''


# To get a list of files in the archive, call namelist() on the ZipFile object:


import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
    zipobj.namelist()


# .namelist() returns a list of names of the files and directories in the archive. To retrieve information about the files in the archive, use .getinfo():

import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
    bar_info = zipobj.getinfo('sub_dir/bar.py')
    bar_info.file_size



'''
.getinfo() returns a ZipInfo object that stores information about a single member of the archive. To get information about a file in the archive, you pass its path as an argument to .getinfo(). Using getinfo(), you’re able to retrieve information about archive members such as the date the files were last modified, their compressed sizes, and their full filenames. Accessing .file_size retrieves the file’s original size in bytes.


The following example shows how to retrieve more details about archived files in a Python REPL. Assume that the zipfile module has been imported and bar_info is the same object you created in previous examples:


>>> bar_info.date_time
(2018, 10, 7, 23, 30, 10)
>>> bar_info.compress_size
2856
>>> bar_info.filename
'sub_dir/bar.py'



bar_info contains details about bar.py such as its size when compressed and its full path.

The first line shows how to retrieve a file’s last modified date. The next line shows how to get the size of the file after compression. The last line shows the full path of bar.py in the archive.

ZipFile supports the context manager protocol, which is why you’re able to use it with the with statement. Doing this automatically closes the ZipFile object after you’re done with it. Trying to open or extract files from a closed ZipFile object will result in an error.


'''

# ========================================

'''
The zipfile module allows you to extract one or more files from ZIP archives through .extract() and .extractall().

These methods extract files to the current directory by default. They both take an optional path parameter that allows you to specify a different directory to extract files to. If the directory does not exist, it is automatically created. To extract files from the archive, do the following:


'''

'''
>>> import zipfile
>>> import os

>>> os.listdir('.')
['data.zip']

>>> data_zip = zipfile.ZipFile('data.zip', 'r')

>>> # Extract a single file to current directory
>>> data_zip.extract('file1.py')
'/home/terra/test/dir1/zip_extract/file1.py'

>>> os.listdir('.')
['file1.py', 'data.zip']

>>> # Extract all files into a different directory
>>> data_zip.extractall(path='extract_dir/')

>>> os.listdir('.')
['file1.py', 'extract_dir', 'data.zip']

>>> os.listdir('extract_dir')
['file1.py', 'file3.py', 'file2.py', 'sub_dir']

>>> data_zip.close()




'''

'''
The third line of code is a call to os.listdir(), which shows that the current directory has only one file, data.zip.

Next, you open data.zip in read mode and call .extract() to extract file1.py from it. .extract() returns the full file path of the extracted file. Since there’s no path specified, .extract() extracts file1.py to the current directory.

The next line prints a directory listing showing that the current directory now includes the extracted file in addition to the original archive. The line after that shows how to extract the entire archive into the zip_extract directory. .extractall() creates the extract_dir and extracts the contents of data.zip into it. The last line closes the ZIP archive.
'''


# Extracting Data From Password Protected Archives

# zipfile supports extracting password protected ZIPs. To extract password protected ZIP files, pass in the password to the .extract() or .extractall() method as an argument:


'''
>>> import zipfile

>>> with zipfile.ZipFile('secret.zip', 'r') as pwd_zip:
...     # Extract from a password protected archive
...     pwd_zip.extractall(path='extract_dir', pwd='Quish3@o')

This opens the secret.zip archive in read mode. A password is supplied to .extractall(), and the archive contents are extracted to extract_dir. The archive is closed automatically after the extraction is complete thanks to the with statement.
'''


# Creating New ZIP Archives

# To create a new ZIP archive, you open a ZipFile object in write mode (w) and add the files you want to archive:

'''
>>> import zipfile

>>> file_list = ['file1.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']
>>> with zipfile.ZipFile('new.zip', 'w') as new_zip:
...     for name in file_list:
...         new_zip.write(name)
'''

'''
In the example, new_zip is opened in write mode and each file in file_list is added to the archive. When the with statement suite is finished, new_zip is closed. Opening a ZIP file in write mode erases the contents of the archive and creates a new archive.
'''

# -===========================================

# Creating New ZIP Archives

'''
To create a new ZIP archive, you open a ZipFile object in write mode (w) and add the files you want to archive:
'''

'''
>>> import zipfile

>>> file_list = ['file1.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']
>>> with zipfile.ZipFile('new.zip', 'w') as new_zip:
...     for name in file_list:
...         new_zip.write(name)
'''

'''
In the example, new_zip is opened in write mode and each file in file_list is added to the archive. When the with statement suite is finished, new_zip is closed. Opening a ZIP file in write mode erases the contents of the archive and creates a new archive.
'''

'''
To add files to an existing archive, open a ZipFile object in append mode and then add the files:
'''
'''
>>> # Open a ZipFile object in append mode
>>> with zipfile.ZipFile('new.zip', 'a') as new_zip:
...     new_zip.write('data.txt')
...     new_zip.write('latin.txt')
'''

'''
Here, you open the new.zip archive you created in the previous example in append mode. Opening the ZipFile object in append mode allows you to add new files to the ZIP file without deleting its current contents. After adding files to the ZIP file, the with statement goes out of context and closes the ZIP file.
'''

# =======================================
# Opening TAR Archives

''''
TAR files are uncompressed file archives like ZIP. They can be compressed using gzip, bzip2, and lzma compression methods. The TarFile class allows reading and writing of TAR archives.

Do this to read from an archive:
'''
import tarfile

with tarfile.open('example.tar', 'r') as tar_file:
    print(tar_file.getnames())

'''
tarfile objects open like most file-like objects. They have an open() function that takes a mode that determines how the file is to be opened.

Use the 'r', 'w' or 'a' modes to open an uncompressed TAR file for reading, writing, and appending, respectively. To open compressed TAR files, pass in a mode argument to tarfile.open() that is in the form filemode[:compression]. The table below lists the possible modes TAR files can be opened in:

Mode	Action
r	Opens archive for reading with transparent compression
r:gz	Opens archive for reading with gzip compression
r:bz2	Opens archive for reading with bzip2 compression
r:xz	Opens archive for reading with lzma compression
w	Opens archive for uncompressed writing
w:gz	Opens archive for gzip compressed writing
w:xz	Opens archive for lzma compressed writing
a	Opens archive for appending with no compression
'''
# .open() defaults to 'r' mode. To read an uncompressed TAR file and retrieve the names of the files in it, use .getnames():

'''
>>> import tarfile

>>> tar = tarfile.open('example.tar', mode='r')
>>> tar.getnames()
['CONTRIBUTING.rst', 'README.md', 'app.py']

This returns a list with the names of the archive contents.


Note: For the purposes of showing you how to use different tarfile object methods, the TAR file in the examples is opened and closed manually in an interactive REPL session.

Interacting with the TAR file this way allows you to see the output of running each command. Normally, you would want to use a context manager to open file-like objects.
'''

# The metadata of each entry in the archive can be accessed using special attributes:



'''
>>> for entry in tar.getmembers():
...     print(entry.name)
...     print(' Modified:', time.ctime(entry.mtime))
...     print(' Size    :', entry.size, 'bytes')
...     print()
CONTRIBUTING.rst
 Modified: Sat Nov  1 09:09:51 2018
 Size    : 402 bytes

README.md
 Modified: Sat Nov  3 07:29:40 2018
 Size    : 5426 bytes

app.py
 Modified: Sat Nov  3 07:29:13 2018
 Size    : 6218 bytes


 In this example, you loop through the list of files returned by .getmembers() and print out each file’s attributes. The objects returned by .getmembers() have attributes that can be accessed programmatically such as the name, size, and last modified time of each of the files in the archive. After reading or writing to the archive, it must be closed to free up system resources.
'''

# Extracting Files From a TAR Archive

'''
In this section, you’ll learn how to extract files from TAR archives using the following methods:

.extract()
.extractfile()
.extractall()

To extract a single file from a TAR archive, use extract(), passing in the filename:

>>> tar.extract('README.md')
>>> os.listdir('.')
['README.md', 'example.tar']
'''

'''
The README.md file is extracted from the archive to the file system. Calling os.listdir() confirms that README.md file was successfully extracted into the current directory. To unpack or extract everything from the archive, use .extractall():


>>> tar.extractall(path="extracted/")


.extractall() has an optional path argument to specify where extracted files should go. Here, the archive is unpacked into the extracted directory. The following commands show that the archive was successfully extracted:


$ ls
example.tar  extracted  README.md

$ tree
.
├── example.tar
├── extracted
|   ├── app.py
|   ├── CONTRIBUTING.rst
|   └── README.md
└── README.md

1 directory, 5 files

$ ls extracted/
app.py  CONTRIBUTING.rst  README.md
'''

# To extract a file object for reading or writing, use .extractfile(), which takes a filename or TarInfo object to extract as an argument. .extractfile() returns a file-like object that can be read and used:

'''
>>> f = tar.extractfile('app.py')
>>> f.read()
>>> tar.close()
'''

# ===============================

# Creating New TAR Archives
