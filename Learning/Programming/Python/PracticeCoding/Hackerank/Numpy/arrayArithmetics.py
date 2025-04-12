import numpy

N,M = map(int,input().split())

arrA = [list(map(int,input().split())) for _ in range(N)]
arrB = [list(map(int,input().split())) for _ in range(N)]

arrA = numpy.array(arrA)
arrB = numpy.array(arrB)
print(numpy.add(arrA,arrB))
print(numpy.subtract(arrA,arrB))
print(numpy.multiply(arrA,arrB))
print(arrA//arrB)
print(numpy.mod(arrA,arrB))
print(numpy.power(arrA,arrB))


# Solution 2

# Read the first line
n, m = map(int, input().split())

# Read next n lines for array A
A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Read next n lines for array B
B = []
for _ in range(n):
    row = list(map(int, input().split()))
    B.append(row)

# Optional: print to verify
print("Array A:")
for row in A:
    print(row)

print("Array B:")
for row in B:
    print(row)
