# try:
#     pass 
# except Exception:
#     pass 
# else:
#     pass 
# finally:
#     pass

# if our section of the code might throw an error then we use try and except block to handle them in the way we want
# we will getting error if we run below line
# f = open('testFile.txt')

# try:
#     f = open('testFile.txt')
#     var = bad_var
# except Exception:
#     print("Sorry, this file doesn't exist!")


# try:
#     f = open('testFile.txt')
#     var = bad_var
# except FileNotFoundError:
#     print("Sorry, this file doesn't exist!")

# except Exception:
#     print("Sorry. Something went wrong!")


# try:
#     f = open('testFile.txt')
#     var = bad_var
# except FileNotFoundError:
#     print("Sorry, this file doesn't exist!")

# except Exception as e:
#     print(e)

# What else does it run the code that need to be executed if the try 
#  clause doesn't raise an exception

# try:
#     f = open('Files/test_copy.txt')
# except FileNotFoundError as e:
#     print(e)

# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()


# Finally
# It run no matter what happen whether code successful or not

# try:
#     f = open('Files/test_copy.txt')
# except FileNotFoundError as e:
#     print(e)

# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("Executing finally...")


# Raise our own exception
try:
    f = open('Files/test_copy.txt')
    if f.name == 'current_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)

except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...")
