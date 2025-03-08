x = {'key':[1,23,4,5,6]}
y = {'m':4}

print(x['key'])

x['key2'] = 5

x[2] = 8
print(x)

print('key' in x)

print(list(x.values()))
print(list(x.keys()))


del x['key']

print(x)
print()

for key,value in x.items():
    print(key, value)
print()

for key in x:
    print(key, x[key])