'''
    *        1
   ***       2
  *****      3
 *******     4
*********    5
 *******
  *****
   ***
    *
'''


def print1(n):
    for i in range(0,n):
        # space
        for j in range(0,n-i-1):
            print(" ", end='')
        
        # star
        for j in range(0,2*i+1):
            print("*",end='')
        # space
        for j in range(0,n-i-1):
            print(" ", end='')
        print()

def print2(n):
    for i in range(0,n):
        # space
        for j in range(0,i):
            print(" ", end='')
        
        # star
        for j in range(0,2*n-2*i-1):
            print("*",end='')
        # space
        for j in range(0,i):
            print(" ", end='')
        print()
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)
        print2(n)


