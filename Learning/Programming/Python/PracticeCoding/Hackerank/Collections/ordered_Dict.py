# Solutions 1
# Using OrderedDict (as before)?
from collections import OrderedDict
N = int(input())
orderedDct = OrderedDict()
for _ in range(N):
    *name_full, price = input().split()
    name = ' '.join(name_full)
    price = int(price)
    orderedDct[name] = orderedDct.get(name,0) + price


for name,total in orderedDct.items():
    print(f"{name} {total}")


# Solution 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
N = int(input())
item_index = defaultdict(int)
seen = []
for _ in range(N):
    *name_full, price = input().split()
    name = ' '.join(name_full)
    price = int(price)
    if name not in item_index:
        seen.append(name)
    item_index[name] += price


for name in seen:
    print(f"{name} {item_index[name]}")