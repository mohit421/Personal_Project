# COmbining multiple conditional together to create one larger condition

x,y,z = 7,8,0

res1 = x==y 
res2 = y>x
res3 = z-2<x+2


print(res1,res2,res3)

# and/or/not -> we use this to combine multiple condition together

res4 = res1 or res2 or res3
print(res4)

res5 = res1 or not res2 or res3
print(not (False or True))
print(not (False and True))

print(not(False and True or False))

# not > and > or :- Ordered operation priority wise not is first then and then or at last




