'''
ABCDE
ABCD
ABC
AB
A
'''


def print1(n):
    for i in range(n):
        for j in range(n - i):
            print(chr(65 + j), end='')
        print()
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)
