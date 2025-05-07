'''
*
* *
* * *
* * * *
* * * * *
* * * * 
* * * 
* * 
* 
'''


def print1(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()
    for i in range(n):
        for j in range(n-i-1):
            print('*',end=' ')
        print()

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)
