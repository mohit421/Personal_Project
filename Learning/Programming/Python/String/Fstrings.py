# # we can use capital or small case f
# tim = 89
# x = f'hello {6+9} {tim} {5 +9}'
# print(x)
# print(f'hello {tim}')


# =========================\\
# F-string suppoer tin pythion 3.6 or above version

# first_name = 'Mohit'
# last_name = 'Jaiswal'

# # sentence = 'My name is {} {}'.format(first_name, last_name)
# # print(sentence)

# sentence = f'My name is {first_name} {last_name}'
# print(sentence)


# # Cool thing is we can directly run function and method within the f-string]
# sentence = f'My name is {first_name.upper()} {last_name.capitalize()}'
# print(sentence)

# ----------------------------------//////////////////---------
# How we can put dictionary value using f-string

# Using format method
# person = {'name': 'jenn','age':22}

# sentence = 'My name is {} and I am {}  years old'.format(person['name'],person['age'])

# print(sentence)

# ------------
# Using f-string

# person = {'name': 'jenn','age':22}

# sentence = f'My name is {person['name']} and I am {person['age']}  years old'

# print(sentence)


# ---------------------////////////////
# We can also do calculation in f string

# calc = f'4 times 11 is equal to {4*11}'
# print(calc)


# ---------------

# for n in range(1,11):
#     sentence = f'The value is {n}'
#     print(sentence)


#  padded with 2 digit 
# for n in range(1,11):
#     sentence = f'The value is {n:02}'
#     print(sentence)


# For floating value 
#  below ex give 5 digit precision value
# pi= 3.1159265
# sentence = f'Pi is equal to {pi:.5f}'
# print(sentence)


# from datetime import datetime
# birthday  = datetime(1990,1,1)

# sentence = f'Jenn has a birthday on {birthday}'
# print(sentence)



# Additional Formatting

from datetime import datetime
birthday  = datetime(1990,1,1)

sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sentence)