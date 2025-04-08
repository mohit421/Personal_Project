import math
z = complex(input())
x = z.real
y = z.imag
r = math.sqrt(x**2+y**2)
th = math.atan2(y,x)
print(r)
print(th)
