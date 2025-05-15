
# Syntax:-

'''
String {field_name:conversion} Example.format(value)
ValueError: Error occurs during type conversion in this method.
'''

# Python program to convert float to exponential
 
# Declaring the float number
float_number = 1101.02
 
# Converting the float number to exponential number
exp_number = "{:e}".format(float_number)
 
# Printing the converted number
print("Float Number:",float_number)
print("Exponent Number:",exp_number)