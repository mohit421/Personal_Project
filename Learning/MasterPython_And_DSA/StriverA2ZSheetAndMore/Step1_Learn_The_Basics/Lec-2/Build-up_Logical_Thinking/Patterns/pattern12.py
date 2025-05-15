'''
1       1
12     21
123   321
1234 4321
123454321

'''



def print1(n):
    space = 2*(n-1)
    for i in range(1,n+1):
        # numbers

        for j in range(1,i+1):
            print(j,end = '')
        # space
        for j in range(1,space+1):
            print(" ",end='')
        # numbers
        for j in range(i,0,-1):
            print(j,end = '')
        print()
        space -=2


        
    

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)
