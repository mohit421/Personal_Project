# String Formatting

# Problem Link:- https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

# /Code 1
#  using bin, oct, hex built-in and rjust and format string
def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:])+1
    for i in range(1,number+1):
        d = str(i).rjust(w-1)
        b = bin(i)[2:].rjust(w)
        o = oct(i)[2:].rjust(w)
        h = hex(i)[2:].rjust(w).upper()
        print("{}{}{}{}".format(d,o,h,b))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# Code 2

'''
Using .rjust() for Manual Alignment
'''

def print_formatted(number):
    # your code goes here
    width = len(bin(n)[2:])

    for i in range(1, n + 1):
        print(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# Code 3
'''
 Method 3 (Using %-formatting)
 . Using %-formatting (Old Style, Python 2 & 3)
Since %b is unsupported, we can manually convert the binary using bin(i)[2:] and format it using %s:
'''

'''
# Printing Each Number in Different Formats


## print("%*d %*o %*X %*s" % (width, i, width, i, width, i, width, bin(i)[2:]))
#### This line uses old-style formatting (% formatting) to format and print the values.

### reaking Down Each %*d, %*o, %*X, and %*s:
    - %*d → Formats i as decimal (d) and right-aligns (* means use width).
    - %*o → Formats i as octal (o) and right-aligns.
    - %*X → Formats i as hexadecimal (uppercase) (X) and right-aligns.
    - %*s → Formats bin(i)[2:] as binary string (s) and right-aligns.
    - How the % Formatting Works:
    - * in %*d means use dynamic width (provided later in %(width, ...)).
    - The corresponding values are passed in order: (width, i, width, i, width, i, width, bin(i)[2:]).
    - This ensures each number is properly aligned according to width.
'''
def print_formatted(number):
    # your code goes here
    width = len(bin(n)[2:])

    for i in range(1, n + 1):
        print("%*d %*o %*X %*s" % (width, i, width, i, width, i, width, bin(i)[2:]))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



# Code 4
'''
 Using f-strings (Python 3.6+)
'''

'''
Explanation:-

Calculating the Width for Proper Formatting

width = len(f"{n:b}")
- f"{n:b}" converts n to a binary string representation.
- bin(n) returns '0b10001', but f"{n:b}" returns just '10001'.
- len("10001") calculates the length of the binary representation.
- This width ensures all numbers are properly aligned.
- Example Calculation:
For n = 17:

f"{17:b}" → '10001'
len("10001") → 5
So, width = 5.

'''

'''
# print explanation

### Printing Each Number in Different Formats Using f-strings


### print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

### This is an f-string where:

    - {i:>{width}d} → Formats i as decimal (d), right-aligned (>) with width width.
    - {i:>{width}o} → Formats i as octal (o), right-aligned (>) with width width.
    - {i:>{width}X} → Formats i as hexadecimal (uppercase) (X), right-aligned (>) with width width.
    - {i:>{width}b} → Formats i as binary (b), right-aligned (>) with width width.
    - Breaking Down the Formatting:
    - > → Right-align numbers (important for consistent spacing).
    - {width} → Dynamic width based on the longest binary number.
    - d → Decimal format.
    - o → Octal format.
    - X → Hexadecimal (Uppercase) format.
    - b → Binary format.


'''
def print_formatted(number):
    # your code goes here
    width = len(f"{n:b}")  # Calculate width from binary format

    for i in range(1, n + 1):
        print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# Code 5
'''
 Using str.format() (Python 2 & 3)
'''
'''
Explanation :-

Printing Each Number in Different Formats
python
Copy
Edit
print("{:>{w}d} {:>{w}o} {:>{w}X} {:>{w}b}".format(i, i, i, i, w=width))
Let's break down the formatting inside format():

🔹 {:>{w}d} → Decimal
{} is a placeholder.
> means right-align (ensures numbers are aligned).
{w} specifies the width (w=width is passed at the end).
d means decimal format.
🔹 {:>{w}o} → Octal
o converts i to octal (base 8).
🔹 {:>{w}X} → Hexadecimal (Uppercase)
X converts i to hexadecimal (base 16) using uppercase letters.
🔹 {:>{w}b} → Binary
b converts i to binary (base 2).
'''


n = int(input())
width = len(bin(n)[2:])  # To align properly

for i in range(1, n + 1):
    print("{:>{w}d} {:>{w}o} {:>{w}X} {:>{w}b}".format(i, i, i, i, w=width))



# Cxode 6 
# without suing any built-ins

def to_binary(n):
    result = ""
    while n > 0:
        result = str(n % 2) + result  # Get remainder, append at the front
        n //= 2
    return result if result else "0"

def to_octal(n):
    result = ""
    while n > 0:
        result = str(n % 8) + result
        n //= 8
    return result if result else "0"

def to_hexadecimal(n):
    hex_digits = "0123456789ABCDEF"
    result = ""
    while n > 0:
        result = hex_digits[n % 16] + result  # Convert remainder using hex digits
        n //= 16
    return result if result else "0"

# Input
n = int(input())

# Determine the width using manual binary conversion
max_width = len(to_binary(n))

# Print values in formatted way
for i in range(1, n + 1):
    decimal_str = str(i).rjust(max_width)
    octal_str = to_octal(i).rjust(max_width)
    hex_str = to_hexadecimal(i).rjust(max_width)
    binary_str = to_binary(i).rjust(max_width)

    print(decimal_str, octal_str, hex_str, binary_str)
