# Text Wrap
# Problem Link :- https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

# Code 1

import textwrap

def wrap(string, max_width):
    res = []
    for i in range(0, len(string), max_width):  # Iterate with step of `max_width`
        res.append(string[i:i+max_width])  # Extract substrings
    return "\n".join(res)  

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# Code 2

# using text wrap
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Code 3

# Using list comprehension
import textwrap

def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0,len(string),max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)