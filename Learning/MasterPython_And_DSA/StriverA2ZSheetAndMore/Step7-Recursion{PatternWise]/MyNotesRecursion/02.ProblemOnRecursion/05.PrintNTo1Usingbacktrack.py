'''

'''



def print_1ToN(i,n):
    if i>n:
        return 
    
    print_1ToN(i+1,n)
    print(i)
def main():
    print_1ToN(1,int(input()))

if __name__ == "__main__":
    main()



