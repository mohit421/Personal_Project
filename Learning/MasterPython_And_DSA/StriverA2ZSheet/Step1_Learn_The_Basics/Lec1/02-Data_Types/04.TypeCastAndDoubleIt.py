# Problem link:- https://www.geeksforgeeks.org/problems/typecast-and-double-it--153103/1&selectedLang=python3

# Solution 1

num = input()
# TypeCast num to int, double it and print
integer = int(num)
print(integer*2)

# Soluiton 2

num = "5"
result = list(map(int, [num]))[0] * 2
print(result)  # Output: 10

# SOlution 3:- Using eval() (⚠️ careful with this one, only for trusted input)

num = "5"
result = eval(num) * 2
print(result)  # Output: 10

# Solution 4

double = lambda num: int(num) * 2
print(double("5"))  # Output: 10