# Creating a dictionary comprehensions

pairs = [("a",1),("b",2),("c",3)]
my_dict = {k: v for k,v in pairs}
print(my_dict)


# Dictionary Comprehension

names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman','Superman','Wolverine','Deadpool']

# print(dict(zip(names,heros)))

# I want a dict {'name':'hero'} for ach name,hero in zip(names,heros)

# using for loop
my_dict = {}
for name, hero in zip(names,heros):
    my_dict[name] = hero
# print(my_dict)

# Using list comprehension
my_dict = {name:hero for name, hero in zip(names, heros)}
# print(my_dict)

# If name not equal to Peter

my_dict = {name:hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)

