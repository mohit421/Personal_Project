# Mutations
# Problem Link:- https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

'''
strings are immutable, we create a new string with the required changes.
'''

# Code 1
'''
✅ Time Complexity: O(n)
✅ Space Complexity: O(n)
'''
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Code 2
'''
✅ Time Complexity: O(n)
✅ Space Complexity: O(n)
'''
def mutate_string(string, position, character):
    l = [char for char in string]
    l[position] = character
    return ''.join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Code 3
#  Solution 3: Using bytearray() (Efficient for ASCII)
'''
✅ Time Complexity: O(n)
✅ Space Complexity: O(n)

🔹 Why bytearray()? → Faster for ASCII but may not work well with Unicode characters.
'''
def mutate_string(string, position, character):
    ba = bytearray(string, 'utf-8')  # Convert string to bytearray
    ba[position] = ord(character)  # Change character at index
    return ba.decode('utf-8')  # Convert back to string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    result = mutate_string(s, int(i), c)
    print(result)
