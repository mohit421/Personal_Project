# Capitalize 
# Problem Link:- https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

#!/bin/python3

'''
Using split() and capitalize() (More Reliable)
'''
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    capitalize_word = ' '.join([word.capitalize() for word in s.split(' ')])
    return capitalize_word

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()



# Code 2

'''
Note: Like title(), capwords() may not handle certain punctuation correctly.
#  Using title() (Simple but Not Always Accurate)
'''


def solve(s):
    return s.title()

'''
✅ Pros:

Short and easy to use.
Works well for simple cases.
❌ Cons:

Incorrectly capitalizes words with apostrophes (e.g., "o'reilly" → "O'Reilly" becomes "O'Reilly" which is correct, but "3rd place" → "3Rd Place" which is incorrect).

'''


# Code 3

'''
Using Regular Expressions (re.sub())

Explanation:
1. Understanding re.sub(pattern, replacement, string)
    re.sub() is a function in Python's re (regular expressions) module that searches for a pattern and replaces it with a specified replacement.
2. Regular Expression Pattern: r'\b\w'
    \b → Matches a word boundary (the position where a word starts or ends).
    \w → Matches any word character (letters, digits, or underscores). Here, it will match the first letter of each word.
    👉 Together, \b\w finds the first letter of each word in the string.

3. Using a Lambda Function to Capitalize
    lambda m: m.group().upper()
    m is the match object found by re.sub().
    m.group() extracts the matched text (the first letter of each word).
    .upper() converts it to uppercase.
    This means every first letter found by \b\w will be converted to uppercase.
4. Putting It All Together

### For example, if:


s = "hello world from python"
The pattern \b\w matches:

"h" in "hello"
"w" in "world"
"f" in "from"
"p" in "python"
Each matched letter is converted to uppercase, resulting in:

output:- 
Hello World From Python
'''
import re

def solve(s):
    return re.sub(r'\b\w', lambda x: x.group().upper(), s)

# Code 4

# Using a for Loop (Step-by-Step Approach)

def solve(s):
    words = s.split(' ')
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return ' '.join(words)



# Code 5

# Using map() Function

def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))




# Code 6
#  Using ASCII Checks (Handling Edge Cases Manually)


#!/bin/python3

import math
import os
import random
import re
import sys
import string
# Complete the solve function below.

def solve(s):
    result = ''
    capitalize = True
    
    for char in s:
        if char != ' ' and capitalize:
            result += char.upper()
            capitalize = False
        else:
            result += char
        if char == ' ':
            capitalize = True

    return result




# Code 7
'''
 Using a For Loop with String Slicing:

You can iterate over each word, capitalize the first letter using slicing, 
and reconstruct the string.
'''
#!/bin/python3

import math
import os
import random
import re
import sys
import string
# Complete the solve function below.

def solve(s):
    words = s.split(' ')
    capitalized_words = []
    for word in words:
        if word:
            capitalized_word = word[0].upper() + word[1:]
        else:
            capitalized_word = ''
        capitalized_words.append(capitalized_word)
    capitalized_s = ' '.join(capitalized_words)
    # print(capitalized_s)
    return capitalized_s





# Code 8
'''
Using a While Loop:

A while loop can also be used to iterate over each word and capitalize the first letter.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import string
# Complete the solve function below.

def solve(s):
    words = s.split(' ')  # Split while keeping spaces intact
    index = 0

    while index < len(words):
        if words[index]:  # Only capitalize if the word is not empty (handles multiple spaces)
            words[index] = words[index].capitalize()
        index += 1

    capitalized_s = ' '.join(words)  #
    return capitalized_s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

