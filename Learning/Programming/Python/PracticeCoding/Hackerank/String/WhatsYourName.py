# What's Your Name?

# Problem Link :- https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true

# Code 1:- Using F-string
#  Solution 1: Using f-strings (Best & Modern Approach)
def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first_name} {last_name}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# Code 2:- Using format string
# 🔹 Solution 2: Using String Formatting (.format())

'''
✅ Time Complexity: O(1)
✅ Space Complexity: O(1)
'''
def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# Code 3

#  Solution 3: Using String Concatenation

def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


