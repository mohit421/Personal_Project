'''
Print 1 to N
'''



# Solution 

def print_1ToN(i,n):
    if i>n:
        return 
    print(i)
    print_1ToN(i+1,n)
def main():
    print_1ToN(1,int(input()))

if __name__ == "__main__":
    main()



