# String Validators
# Problem Link:- https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

'''
✅ Time Complexity: O(n)
✅ Space Complexity: O(1)
✅ Efficient & Pythonic using any()
'''
if __name__ == '__main__':
    s = input()
    checks = [
        any(c.isalnum() for c in s),
        any(c.isalpha() for c in s),
        any(c.isdigit() for c in s),
        any(c.islower() for c in s),
        any(c.isupper() for c in s),
    ]
    for check in checks:
        print(check)
    
# Code 2
'''
Solution 3: Using Loop and Flags (Less Pythonic)
'''
if __name__ == '__main__':
    s = input()

    has_alnum = has_alpha = has_digit = has_lower = has_upper = False

    for c in s:
        if c.isalnum():
            has_alnum = True
        if c.isalpha():
            has_alpha = True
        if c.isdigit():
            has_digit = True
        if c.islower():
            has_lower = True
        if c.isupper():
            has_upper = True

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)
