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


'''

'''

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

'''

# Splution 2

def print1(n):
    for i in range(1, 2*n):
        stars = i
        if i >n:
            stars = 2*n-i
        for j in range(1, stars+1):
            print('*',end=' ')
        print()
    

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)
