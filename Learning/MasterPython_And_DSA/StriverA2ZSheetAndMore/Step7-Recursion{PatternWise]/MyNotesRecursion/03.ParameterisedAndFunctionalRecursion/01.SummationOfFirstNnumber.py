'''
Summataion of number rom 1 to N
'''

# Parameterised way

def print_sum(i,sum):
    if i<1:
        print(sum)
        return 
    print_sum(i-1, sum+i)

def main():
    print_sum(int(input()),0)

if __name__ == "__main__":
    main()







# Functional way


def print_sum(n):
    if n==0:
        return 0 
    return n + print_sum(n-1)

def main():
    print(print_sum(int(input())))

if __name__ == "__main__":
    main()
