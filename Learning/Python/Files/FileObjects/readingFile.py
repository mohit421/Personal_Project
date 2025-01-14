# File Objects - Reading and writing to files
# need to include directly inside open if it is in same directory then we ca use like below

# For appending to the file we use lowercase 'a' and 
# if we want to read the file then we use lowercase 'r'
# and lowercase 'w' if we want to write to the file
# I we want to read and write to the file we use r+


# f = open("Files/test.txt",'r')
# print(f.name, f.mode)

# # we need to explicitly close the file when we done using it.
# f.close()


# If we open the file like we did above then we have to remember to explicitly 
# close the file . If we don't close the File then we end up with leaks 
# that  cause us to run over the maximum amount of file descriptor on our system
#  and our applications throws an error




# Context manager
#  In order to use the context manager that kind of similar we can do this using with keyword
# variable name is f on right. Benefits of this is we open in the block of code and then closed this block of code then automatically close the file
# this will also close the file if any exception that are thrown thats why using context manager is know as best practice
#  It automatically take care of all that cleanup for us

# with open("Files/test.txt",'r') as f:
#     pass

# # we actually have access to f variable after we exit the context manager outside of context manger

# # I/O operation on closed file.
# print(f.read()) # getting error

# we have methods avaialble to read the file contents like:
#  1. read():- The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
#  2. readlines() :- 	Returns a list of lines from the file
#  3. readline()  :- Returns one line from the file


# with open("Files/test.txt",'r') as f:
#     f_contents = f.read()
#     #  this will print all the content of the file
#     print(f_contents)


# with open("Files/test.txt",'r') as f:
#     f_contents = f.readlines()
#     #  this will print all the content of the file
#     print(f_contents)



# with open("Files/test.txt",'r') as f:
#     f_contents = f.readline()
#     #  this will print all the content of the file
#     print(f_contents, end='')
#     f_contents = f.readline()
#     #  if we use readline again and again then first it will print first line then it will read 2nd then 3rd adn so on...
#     print(f_contents, end='')

#  How can we read all of the file from extremely large file
# with open("Files/test.txt",'r') as f:
#     for line in f:
#         print(line, end='')



# but sometime we want more control what we are reading from the file
#  Below will print only first 100 character from the file 
# with open("Files/test.txt",'r') as f:
#     f_contents = f.read(100)
#     print(f_contents, end='')

#     f_contents = f.read(100)
#     print(f_contents, end='')
#     #  if all the character has already read then below will print empty string
#     f_contents = f.read(100)
#     print(f_contents, end='')


# with open("Files/test.txt",'r') as f:
#     size_to_read = 10
#     f_content = f.read(size_to_read)

#     while len(f_content)>0:
#         print(f_content, end='*')
#          it advances its position every time
#         f_content = f.read(size_to_read)

# with open("Files/test.txt",'r') as f:
#     size_to_read = 10
#     f_content = f.read(size_to_read)
#     #  below line will pick from the 10th position this will continue if uses more like this
#     f_content = f.read(size_to_read)
#     # tail() :- 	Returns the current file position
#     print(f.tell())

    

with open("Files/test.txt",'r') as f:
    size_to_read = 10
    f_content = f.read(size_to_read)
    # seek() :- 		Change the file position
    # below line will change position to the beginning of the line again
    #  but we can change to any position we like
    f.seek(0)
    f_content = f.read(size_to_read)
    
    print(f_content)
