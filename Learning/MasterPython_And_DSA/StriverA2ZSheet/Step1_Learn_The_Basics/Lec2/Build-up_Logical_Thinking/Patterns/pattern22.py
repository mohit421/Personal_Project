'''

'''


def print22(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i 
            left = j 
            right = (2*n-2) - j 
            down = (2*n-2) - i 
            print(n-min((min(top,down),min(left,right))),end='')
        print()

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter n: "))
        print22(n)