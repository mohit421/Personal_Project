'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''



def print1(n):
    stars = 1
    for i in range(n):
        if i%2==0:
            stars = 1
        else:
            stars = 0
        for j in range(i+1):
            print(stars, end='')
            stars = 1- stars
        print()            
        
    

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print1(n)
