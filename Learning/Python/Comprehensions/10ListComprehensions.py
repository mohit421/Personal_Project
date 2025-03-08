# 10 Python Comprehensions you should be using in most places


# Code 1

values = []
for x in range(10):
    values.append(x)

# Using List comprehension
# below code is exactly same as above
values = [x for x in range(10)]
print(values)
# --------------------
values = [x+1 for x in range(10)]
print(values)


# =--------------------------------------
# Code 2
evens = []
for number in range(50):
    is_even = number%2 == 0
    if is_even:
        evens.append(number)
    


# List Comprehensions

evens1 = [number for number in range(50) if number%2==0]
print(evens1)

# -------------------------------------------

# Code 3
# Strings that start with "a" and end in "y"

options = ["any","albany","apples","world","hello",""]
valid_string = []

for string in options:
    if len(string) <=1:
        continue
    if string[0] != 'a':
        continue 
    if string[-1] != "y":
        continue

    valid_string.append(string)

print(valid_string)

# Into List comprehension

valid_str = [
    string 
    for string in options 
    if len(string)>=2 
    if string[0] == "a"
    if string[-1] == "y" 
    ]
print(valid_str)


# =---------------------------------------
# Code 4

# Flattening a matrix (list of lists)

matrix = [[1,2,3],[4,5,6], [7,8,9]]
flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)


# Into List Comprehensions
# First for loop is exterior one and 2nd one for internal one
flattened1 = [
    num 
    for row in matrix 
    for num in row 
    ]
print(flattened1)

# -----------------------------

# Code 5

# Categorize number as even or odd

categories = []
for number in range(10):
    if number %2==0:
        categories.append("Even")
    else:
        categories.append("Odd")
    print(categories)

# Into List Comprehension

categories1 = [
    "Even" if x%2==0 else "Odd" 
    for number in range(10)
]
print(categories1)

# -----------------------------------------------


# Code 7
#Building a 3D list

import pprint

printer = pprint.PrettyPrinter()

lst = []
for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l2)
    lst.append(l1)
# printer.pprint(lst)

# Into List Comprehensions

lst1 = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
printer.pprint(lst1)
# 5 list of 5 list that all have the numbers 0 through 4
# -------------------------------------

# Code 8
# List comprehensions with functions

def square(x):
    return x**2

squared_numbers = [square(x) for x in range(10)]


