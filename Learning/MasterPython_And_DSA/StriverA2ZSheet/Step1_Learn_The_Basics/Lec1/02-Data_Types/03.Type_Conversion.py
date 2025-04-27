# Problem lin:- https://www.geeksforgeeks.org/problems/type-conversion--151956/1&selectedLang=python3

# Soluiont 1

d = float(input())
# typecast d to an integer and print it
integer = int(d)
print(integer)


# Soluiton 2

result = [d.get(key, "None") for key in query]
for val in result:
    print(val)

# 