'''

'''



def print1(n):
    for i in range(0,n):
        # space
        for j in range(0,n-i-1):
            print(" ", end='')
        
        # star
        for j in range(0,2*i+1):
            print(chr(65+j),end='')
        # space
        for j in range(0,n-i-1):
            print(" ", end='')
        print()
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)


