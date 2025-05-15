'''
Enter n: 5
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''
# Solution 1
'''
def pattern19(n):
    # Upper part
    initSpace = 0
    for i in range(n):
        # Left stars
        for j in range(n - i):
            print("*", end='')

        # Spaces
        for j in range(initSpace):
            print(" ", end='')

        # Right stars
        for j in range(n - i):
            print("*", end='')

        initSpace += 2
        print()

    # Lower part
    space = 2 * (n - 1)
    for i in range(n):
        # Left stars
        for j in range(i + 1):
            print("*", end='')

        # Spaces
        for j in range(space):
            print(" ", end='')

        # Right stars
        for j in range(i + 1):
            print("*", end='')

        space -= 2
        print()


if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter n: "))
        pattern19(n)
'''


# Soliution 2 :  Basic Loop-Based Version 

'''
def pattern19(n):
    # uper part

    iniSpc = 0
    for i in range(n+1):
        stars = n-i+1
        print("*" * stars + " "* iniSpc + "*" * stars)
        iniSpc += 2
    
    # lower part
    space = 2*(n-1)
    for i in range(1,n+1):
        stars = i+1
        print("*" * stars + " " * space + "*" * stars)
        space -= 2


if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter n: "))
        pattern19(n)

'''

# Solution 3 Using String Multiplication and f-strings
'''
def pattern19(n):
    for i in range(n+1):
        stars = "*" * (n-i+1)
        spaces = " " *(2*i)
        print(f"{stars}{spaces}{stars}")

    for i in range(1,n+1):
        stars = "*" * (i+1)
        spaces = " " * (2*(n-i))
        print(f"{stars}{spaces}{stars}")

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter n: "))
        pattern19(n)

'''
# Solution 4  Building Each Line into a List, Then Joining (More Functional Style)

'''
def pattern19(n):
    ptrn19 = []
    for i in range(n):
        stars = "*" * (n-i+1)
        spaces = " " * (2*i)
        ptrn19.append(stars+spaces+stars)

    for i in range(1,n+1):
        stars = "*" * (i+1)
        spaces = " " * (2*(n-i))
        ptrn19.append(stars + spaces + stars)

    print("\n".join(ptrn19))
if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter n: "))
        pattern19(n)

'''
# Solution 5 Compact Version Using a Helper Function

def pattern_lines(stars, spaces):
    return "*" * stars + " " * spaces + "*" * stars

def pattern19(n):
    for i in range(n+1):
        print(pattern_lines(n-i+1,2*i))
    for i in range(1,n+1):
        print(pattern_lines(i+1,2*(n-i)))

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter n: "))
        pattern19(n)
