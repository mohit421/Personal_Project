'''
A
AB
ABC
ABCD
ABCDE
'''


def print1(n):
    char = 'A'
    for i in range(1,n+1):
        for j in range(i):
            print(char,end='')
            char= char + 1
        print()

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)
