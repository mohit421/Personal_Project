# 01. Using int() Function:- The simplest way to convert a string to an integer in Python is by using the int() function. This function attempts to parse the entire string as a base-10 integer.
# Note: 
# 01. If the string contains non-numeric characters or is empty, int() will raise a ValueError.
# 02. int() function automatically handles leading and trailing whitespaces, so int() function trims whitespaces and converts the core numeric part to an integer.
'''
s = "42"
num = int(s)
print(num)

'''
# 02. Converting Strings with Different Bases:- The int() function also supports other number bases, such as binary (base-2) or hexadecimal (base-16). To specify the base during conversion, we have to provide the base in the second argument of int().
'''
# Binary string
s = "1010"
num = int(s, 2)
print(num)

# Hexadecimal string
s = "A"
num = int(s, 16)
print(num)

'''

# 03. Handling Invalid Input String
# Using try and except
# If the input string contains non-numeric characters, int() will raise a ValueError. To handle this gracefully, we use a try-except block.

'''
s = "abc"
try:
    num = int(s)
    print(num)
except ValueError:
    print("Invalid input: cannot convert to integer")

'''

# 04. Using str.isdigit():- Use str.isdigit() to check if a string is entirely numeric before converting. This method make sure that the input only contains digits.
# Explanation: s.isdigit() returns True if s contains only digits, this allow us safe conversion to an integer.

'''
s = "12345"
if s.isdigit():
    num = int(s)
    print(num)
else:
    print("The string is not numeric.")

'''


