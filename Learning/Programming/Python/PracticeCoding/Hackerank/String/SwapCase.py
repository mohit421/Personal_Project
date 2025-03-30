# Swap Case

# Problem link:- https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    newStr = ''
    for i in s:
        if i.isupper():
            newStr += i.lower()
        elif i.islower:
            newStr += i.upper()
        else:
            newStr += i
    return newStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



# Code 2
'''
✅ Time Complexity: O(n) (iterates through all characters)
✅ Space Complexity: O(n) (stores the transformed string)
'''
# The best approach is using swapcase() since it's built-in and optimized:
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Code 3
# using List comprehension

def swap_case(s):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in s])

if __name__ == '__main__':
    s = input()
    print(swap_case(s))


# Code 4
# Using map function

def swap_case(s):
    return ''.join(map(lambda char: char.lower() if char.isupper() else char.upper(), s))

if __name__ == '__main__':
    s = input()
    print(swap_case(s))
