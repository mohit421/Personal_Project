'''
Print N to 1
'''


# Solution 


def print_1ToN(i,N):
    if i<1:
        return 
    print(i)
    print_1ToN(i-1,N)
def main():
    N = int(input())
    print_1ToN(N,N)

if __name__ == "__main__":
    main()