


# Python "with open(...) ad ..." Patter
'''
open() takes a filename and a mode as its arguments. r opens the file in read only mode. To write data to a file, pass in w as an argument instead:
'''

# 1
with open('.\learning\MasterPython_And_DSA\Python_Automation\FileAndOSAutomation\\test.txt','w') as write_file:
    write_file.write("Hello, I'm a file!")

2
with open('.\learning\MasterPython_And_DSA\Python_Automation\FileAndOSAutomation\\test.txt','r') as read_file:
    print(read_file.read())

# 3
with open('.\learning\MasterPython_And_DSA\Python_Automation\FileAndOSAutomation\\test.txt','a') as write_file:
    write_file.write("\nHere's some more text")


# 4
with open('.\learning\MasterPython_And_DSA\Python_Automation\FileAndOSAutomation\\test.txt','r') as read_file:
    print(read_file.read())

# 5
#  If we do write again then all file content willbe overwritten by the content
with open('.\learning\MasterPython_And_DSA\Python_Automation\FileAndOSAutomation\\test.txt','w') as write_file:
    write_file.write("All the text has been deleted!")


# 6
with open('.\learning\MasterPython_And_DSA\Python_Automation\FileAndOSAutomation\\test.txt','r') as read_file:
    print(read_file.read())


# 7
'''
Below is good but file is opened untill unless we close it explicitly
'''
write_file = open('text.txt','w')
# write_file.write(('Original text'))

# we have to clsoe it expliccitly
write_file.close()

'''
when we are working with in large infra we have to manahge resources carefully so best way to do is using with open(..)...:

'''

'''
1. Check out Reading and Writing Files in Python and Working With File I/O in Python for more information on how to read and write to files.

https://realpython.com/read-write-files-python/#what-is-a-file

https://dbader.org/blog/python-file-io
'''

'''
Character	Meaning
'r'	Open for reading (default)
'w'	Open for writing, truncating (overwriting) the file first
'rb' or 'wb'	Open in binary mode (read/write using byte data)
'''

# Below examples of Read , readlines and readline

# Here’s an example of how to open and read the entire file using .read():
with open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt', 'r') as reader:
    print(reader.read())
    # print("File opened successfully!")


# Here’s an example of how to read 5 bytes of a line each time using the Python .readline() method:


with open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt', 'r') as reader:
    # read & print the first 5 characters of the line 5 times

    print(reader.readline(5))
    
    '''
    # Notice that line is greater than the 5 chars and continues
>>>     # down the line, reading 5 chars each time until the end of the
>>>     # line and then "wraps" around
    '''
    # print(reader.readline(5))
    # print(reader.readline(5))
    # print(reader.readline(5))
    # print(reader.readline(5))



# Here’s an example of how to read the entire file as a list using the Python .readlines() method:

f = open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt')
print(f.readlines())  #returns a list object

print("\n===============================")

# The above example can also be done by using list() to create a list out of the file object:

f = open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt')

print(list(f))



# Iterating Over Each Line in the File
'''
A common thing to do while reading a file is to iterate over each line. Here’s an example of how to use the Python .readline() method to perform that iteration:
'''
print("\n===============================")
with open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt', 'r') as reader:
    # read and print the entire file line by line
    line = reader.readline()
    while line != '':  #the EOF char is an empty string
        print(line, end='')
        line = reader.readline()
        # print(line)

print("\n===============================")
# 
'''
Another way you could iterate over each line in the file is to use the Python .readlines() method of the file object. Remember, .readlines() returns a list where each element in the list represents a line in the file:
'''

with open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')

# However, the above examples can be further simplified by iterating over the file object itself:
print("\n===============================")
with open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt', 'r') as reader:
    for line in reader:
        print(line,end='')


# below is example of .write() and  .writelines():


print("\n===============================")
with open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt', 'r') as reader:

    dog_breeds = reader.readlines()



with open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt', 'w') as writer:
    # alternatively we cloud use writer.writelines(reversed(dog_breeds))
    # write the dog breeds to the fil in reversed order

    for breed in reversed(dog_breeds):
        writer.write(breed)


with open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt', 'r') as reader:
    for read in reader:
        print(read,end='')




# Working with bytes

'''
Sometimes, you may need to work with files using byte strings. This is done by adding the 'b' character to the mode argument. All of the same methods for the file object apply. However, each of the methods expect and return a bytes object instead:
'''

print("\n===============================")


with open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt', 'rb') as reader:
    print(reader.readline())



'''
Opening a text file using the b flag isn’t that interesting. Let’s say we have this cute picture of a Jack Russell Terrier (jack_russell.png):
'''

'''
You can actually open that file in Python and examine the contents! Since the .png file format is well defined, the header of the file is 8 bytes broken up like this:

Value	Interpretation
0x89	A “magic” number to indicate that this is the start of a PNG
0x50 0x4E 0x47	PNG in ASCII
0x0D 0x0A	A DOS style line ending \r\n
0x1A	A DOS style EOF character
0x0A	A Unix style line ending \n
Sure enough, when you open the file and read these bytes individually, you can see that this is indeed a .png header file:


'''

with open('./Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/Jack_Russell_Terrier_1.jpg', 'rb') as byte_reader:
    print(byte_reader.read(1))
    print(byte_reader.read(3))
    print(byte_reader.read(2))
    print(byte_reader.read(1))
    print(byte_reader.read(1))



# Appending to a File
with open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt', 'a') as a_writer:
    a_writer.write('\nBeagle')

with open('C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt', 'r') as a_writer:
    a_writer.read()\
    


# Working With Two Files at the Same Time

d_path = 'C:/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dogbreeds.txt'
d_r_path = '/MyProject/Learning/MasterPython_And_DSA/Python_Automation/FileAndOSAutomation/dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))


# More about file :- https://dbader.org/blog/python-file-io

