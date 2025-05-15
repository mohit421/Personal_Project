'''
     A     
    ABA
   ABCBA
  ABCDCBA
 ABCDEDCBA
ABCDEFEDCBA
'''

# The ord() function in Python returns the Unicode code point (integer value) of a given character.

def print1(n):
    for i in range(n):
        # Spaces before characters
        for j in range(n - i - 1):
            print(" ", end='')

        # Characters in a pyramid pattern
        ch = 'A'
        breakpoint = (2 * i + 1) // 2

        for j in range(2 * i + 1):
            print(ch, end='')

            if j < breakpoint:
                ch = chr(ord(ch) + 1)
            else:
                ch = chr(ord(ch) - 1)

        # Spaces after characters (optional, can be removed)
        for j in range(n - i - 1):
            print(" ", end='')

        print()  # New line after each row

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter n: "))
        print1(n)
