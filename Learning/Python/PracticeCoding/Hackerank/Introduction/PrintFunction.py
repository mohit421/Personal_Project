# problem Link :- https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

n = int(input())  # Read input
for i in range(1, n + 1):
    print(i, end="")  # Pr


# another ways
if __name__ == '__main__':
    n = int(input())
    [print(i,end="") for i in range(1,n+1)]