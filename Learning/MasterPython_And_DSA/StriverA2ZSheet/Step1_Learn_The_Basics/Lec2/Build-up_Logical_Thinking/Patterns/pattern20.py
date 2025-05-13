'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''


# Solution 1
'''
def print1(n):
    spaces = 2*n-2
    for i in range(1,2*n-1):
        # stars
        stars = i 
        if i>n:
            stars = 2*n-i 
        for j in range(1,stars):
            print("*",end='')
        
        # spaces
        for j in range(1,spaces+1):
            print(" ",end='')
        # stars
        if i>n:
            stars = 2*n-i 
        for j in range(1,stars):
            print("*",end='')
        if i<n:
            spaces -= 2
        else:
            spaces +=2
        print()

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)

'''


# Solution 2  Simple For-Loop with String Multiplication

'''
def pattern20(n):
    for i in range(1,2*n):
        if i<=n:
            stars = i
            spaces = 2*(n-i)
        else:
            spaces = 2*(i-n)
            stars =  2*n-i
        # left stars
        print("*" * stars,end='')
        # Middle spaces
        print(" " * spaces,end='')
        # right stars
        print("*" * stars)
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        pattern20(n)
'''

# Solution 2 Nested Loop Version (No String Multiplication)


def pattern20(n):
    for i in range(1,2*n):
        if i<=n:
            stars = i
            spaces = 2*(n-i)
        else:
            stars = 2*n-i 
            spaces = 2*(i-n)
        for _ in range(stars):
            print("*",end='')
        for _ in range(spaces):
            print(" ",end='')
        for _ in range(stars):
            print("*",end='')
        print()

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        pattern20(n)


# /Solution 3 Using Centered Formatting for Symmetry (Optional Styling)


def pattern20(n):
    width = 2*n 
    for i in range(1,2*n):
        if i<=n:
            stars = i 
            spaces = 2*(n-i)
        else:
            stars = 2*n-i 
            spaces = 2*(i-n)
        left = "*"*stars 
        right = "*" * stars
        middle = " "*spaces
        print(left + middle + right)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        pattern20(n)