# 1.  Using str() Function
'''
n = 42

s = str(n)
print(s)

'''

# 2. Using f-strings:- For Python 3.6 or later, f-strings provide a quick way to format and convert values.
'''
n = 42

s = f"{n}"
print(s)

'''

# 3. Using format() Function : format() function inserts values into {} placeholders in a string. This is similar to f-strings but works with older versions of Python (before 3.6).

'''
n = 42

s = "{}".format(n)
print(s)

'''

# Using %s Keyword :- The %s keyword allows us to insert an integer (or any other data type) into a string. This method is part of the older style of string formatting but still works in Python.

'''
n = 42

s = "%s" % n
print(s)

'''

# Using repr() for Debugging:- repr() function is usually used for debugging, as it gives a detailed string version of an object. While it also converts integers to strings, it’s not the most common method for simple integer-to-string conversion.

'''
n = 42

s = repr(n)
print(s)

'''