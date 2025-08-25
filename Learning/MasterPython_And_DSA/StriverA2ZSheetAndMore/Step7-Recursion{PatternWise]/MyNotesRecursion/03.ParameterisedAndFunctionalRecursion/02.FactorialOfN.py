'''
Factorial of N
'''

# Solution functional ways



def print_fact(n):
    if n==1:
        return 1 
    return n * print_fact(n-1)

def main():
    print(print_fact(int(input())))

if __name__ == "__main__":
    main()