# Python program to convert int to exponential

'''
Syntax:- String {field_name:conversion} Example.format(value)
Errors and Exceptions:
ValueError: Error occurs during type conversion in this method.
'''

# Declaring the integer number
int_number = 110102
 
# Converting the integer number to exponential number
exp_number = "{:e}".format(int_number)
 
# Printing the converted number
print("Integer Number:",int_number)
print("Exponent Number:",exp_number)