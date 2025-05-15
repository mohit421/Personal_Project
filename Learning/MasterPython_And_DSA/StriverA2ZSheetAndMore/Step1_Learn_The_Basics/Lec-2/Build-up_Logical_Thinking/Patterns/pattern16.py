'''
6
A
BB
CCC
DDDD
EEEEE
FFFFFF

'''



def print1(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(chr(65+i),end='')
        
        print()
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)


