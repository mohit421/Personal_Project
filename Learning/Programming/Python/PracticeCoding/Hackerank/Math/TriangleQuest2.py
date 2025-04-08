



for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i//9)**2)


# Solution  2. Using String Concatenation (Manual Build)

n = int(input())

for i in range(1, n + 1):
    left = ''.join(str(x) for x in range(1, i + 1))
    right = ''.join(str(x) for x in range(i - 1, 0, -1))
    print(left + right)


# Solution 3 Using Loops Only (No join, Pure Loop)

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()


# Solution 4 Using List Slicing 

n = int(input())

for i in range(1, n + 1):
    nums = list(range(1, i + 1))
    print(''.join(str(x) for x in nums + nums[-2::-1]))
