# alphabet-rangoli
# problem Link:- https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

# Code 1

def print_rangoli(size):
    # your code goes here
    alphabet = [chr(i)  for i in range(97,123)]
    alphabet = alphabet[:size]
    # print(alphabet)

    indices = list(range(size))
    indices = indices[:-1] + indices[::-1]
    # print(indices)

    for i in indices:
        startIdx = i+1
        org = alphabet[-startIdx:]
        rev = org[::-1]
        row = rev + org[1:]
        # print(row)
        row = '-'.join(row)
        w = size*4 -3
        row = row.center(w,'-')
        print(row)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# Code 2

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = 4 * size - 3  # Total width of the pattern

    for i in range(size - 1, -size, -1):  # Loops from size-1 to -size+1
        row = '-'.join(alphabet[size-1:abs(i):-1] + alphabet[abs(i):size])  # Create pattern
        print(row.center(width, '-'))  # Center align the row

# Example Usage
print_rangoli(5)


# Code 3

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = 4 * size - 3
    
    lines = ['-'.join(alphabet[size-1:i:-1] + alphabet[i:size]).center(width, '-') for i in range(size)]
    print('\n'.join(lines + lines[:-1][::-1]))  # Mirror the top part

# Example Usage
print_rangoli(5)


# Code 4
import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = 4 * size - 3
    
    pattern = list(map(lambda i: '-'.join(alphabet[size-1:i:-1] + alphabet[i:size]).center(width, '-'), range(size)))
    
    print('\n'.join(pattern + pattern[:-1][::-1]))

# Example Usage
print_rangoli(5)



