# Solution 1

import numpy



P = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(P,x))


# Solution 2   (Simple & Recommended):

# Read input
coeffs = list(map(float, input().split()))
x = float(input())

# Calculate polynomial value
result = sum(coef * (x ** i) for i, coef in enumerate(reversed(coeffs)))

# Print the result
print(result)
