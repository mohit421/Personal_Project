# Problem Link:- https://www.geeksforgeeks.org/problems/greatest-of-three--154612/1?&selectedLang=python3

# /Solution 1
a = int(input())
b = int(input())
c = int(input())

if(a>=b and a>=c):
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)

# Solution 2 using ternary expression
def greatest_of_three(a, b, c):
    return a if a >= b and a >= c else b if b >= a and b >= c else c


# Solution 3  Object oriented style

class Greatest:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find(self):
        return max(self.a, self.b, self.c)
