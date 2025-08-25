'''

'''

# 
'''
TC: O(N)
SC:- O(N)
'''
def print_name(i,n):
    if i>n:
        return 
    print("Mohit")
    print_name(i+1,n)

def main():
    n = int(input("Give eyour number: "))
    print_name(1,n)

if __name__ == "__main__":
    main()

