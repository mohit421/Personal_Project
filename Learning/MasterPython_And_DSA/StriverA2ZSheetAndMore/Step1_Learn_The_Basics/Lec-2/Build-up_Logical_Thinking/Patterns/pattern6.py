'''
12345
1234
123
12
1
'''





def print1(n):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(j,end=' ')
        print()

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)
