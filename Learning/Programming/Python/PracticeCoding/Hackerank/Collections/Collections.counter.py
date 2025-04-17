# Enter your code here. Read input from STDIN. Print output to STDOUT

# from collections import Counter

X = int(input())
shoes = list(map(int,input().split()))
noCustomer = int(input())


sm = 0
for i in range(noCustomer):
    size,price = map(int,input().split())
    if size in shoes:
        sm += price
        shoes.remove(size)
        
print(sm)


# Solution 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())
shoes = list(map(int,input().split()))
noCustomer = int(input())

shoeInventory = Counter(shoes)

sm = 0
for _ in range(noCustomer):
    size,price = map(int,input().split())
    if shoeInventory[size]>0:
        sm+=price
        shoeInventory[size]-=1;
        
print(sm) 