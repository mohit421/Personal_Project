'''
Enter n: 6
******
*    *
*    *
*    *
*    *
******
'''


def print21(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                print("*",end='')
            else:
                print(" ",end='')
        print()

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter n: "))
        print21(n)