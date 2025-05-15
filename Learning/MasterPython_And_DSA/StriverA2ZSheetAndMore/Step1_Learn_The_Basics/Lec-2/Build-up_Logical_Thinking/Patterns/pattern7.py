'''
    *        1
   ***       2
  *****      3
 *******     4
*********    5

123456789
'''

'''
We are printing space,start,space
0th column:- 4 space, 1 star, 4 space -> 5-0-1 space, 2*1+1 star, 5-0-1
1th column:- 3 space, 3 star, 3 space
2th column:- 2 space, 5 star, 2 space
3th column:- 1 space, 7 star, 1 space
4th column:- 0 space, 9 star, 0 space
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
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)


