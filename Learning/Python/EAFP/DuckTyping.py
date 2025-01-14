# Duck Typing : It is easier to ask forgiveness than permission (EAFP)

# Pythonic: It means that it following convention of coding style of python language
#  in order to write clean and readable code

# Two aspect of being pythonic in this file
# 1. Duck Typing
# 2. EAFP

# Duck Typing
# If an object walks like a duck and quack like a duck than its a duck

# class Duck:
#     def quack(self):
#         print('Quack','quack')
#     def fly(self):
#         print('Flap, Flap!')

# class Person:
#     def quack(self):
#         print("I'm Quacking like Duck!")
#     def fly(self):
#         print("i'm flapping like a Duck!")

# def quack_and_fly(thing):
#     # Not Duck-Type(Non-Pythonic)
#     if isinstance(thing,Duck):
#         thing.quack()
#         thing.fly()

#     else:
#         print("This has to be a Duck!")
#     print()

# d = Duck()
# quack_and_fly(d)

# p = Person()
# quack_and_fly(p)

# ----------------
# IN dUCK TYPING we actually don't care about whether the object is actually duck or not 
# we only care if it behaves like a duck when ask to do so 
# Defn:- When it ask like a duck and quack like a duck then it's treated like a duck




# -------------

# class Duck:
#     def quack(self):
#         print('Quack','quack')
#     def fly(self):
#         print('Flap, Flap!')

# class Person:
#     def quack(self):
#         print("I'm Quacking like Duck!")
#     def fly(self):
#         print("i'm flapping like a Duck!")

# def quack_and_fly(thing):
#     thing.quack()
#     thing.fly()
#     print()

# d = Duck()
# quack_and_fly(d)

# p = Person()
# quack_and_fly(p)


# ----------------
#  Can't be pass in just any objects that potentially an error 
# and that's true it might attempted to say all we care about in this examples is
#  not what type of object it is whether it can quack and fly
#  How we can put checks in place to make sure those method exists

# =========================================

#  This is where 2nd concept comes in

# It is easier to ask forgiveness than permission 


# --------
# Non-Pythonic way :- Look before you leave

# class Duck:
#     def quack(self):
#         print('Quack','quack')
#     def fly(self):
#         print('Flap, Flap!')

# class Person:
#     def quack(self):
#         print("I'm Quacking like Duck!")
#     def fly(self):
#         print("i'm flapping like a Duck!")

# def quack_and_fly(thing):
#     # LBYL (Non-Pythonic)
#     if hasattr(thing, 'quack'):
#         if callable(thing.quack):
#             thing.quack()

#     if hasattr(thing, 'fly'):
#         if callable(thing.fly):
#             thing.fly()
#     print()

# d = Duck()
# quack_and_fly(d)

# p = Person()
# quack_and_fly(p)

# -----------------------------

# class Duck:
#     def quack(self):
#         print('Quack','quack')
#     def fly(self):
#         print('Flap, Flap!')

# class Person:
#     def quack(self):
#         print("I'm Quacking like Duck!")
#     def fly(self):
#         print("i'm flapping like a Duck!")

# def quack_and_fly(thing):
#     # EAFP (Pythonic)
#     try:
#         thing.quack()
#         thing.fly()
#         thing.bark()
#     except AttributeError as e:
#         print(e)
#     print()

# d = Duck()
# quack_and_fly(d)

# p = Person()
# quack_and_fly(p)


# --------
# Dict

# person = {"name": 'jess', 'age':23, 'job':"Programmer"}

# # LYBL (Non Pythonic)
# if 'name' in person and 'age' in person and 'job' in person:
#     print("I'm {name}. I'm {age} years old and O am a {job}".format(**person))

# else:
#     print("missing some keys")


# -------


# #  EAFP (Pythonic)

# person = {"name": 'jess', 'age':23, 'job':"Programmer"}

# # LYBL (Non Pythonic)
# try:
#     if 'name' in person and 'age' in person and 'job' in person:
#         print("I'm {name}. I'm {age} years old and O am a {job}".format(**person))
# except KeyError as e:
#     print("Missing {} some keys".format(e))





# ---------------------------

# Non-Pythonic

# my_list = [1,2,3,4,5,6]
# if len(my_list)>=6:
#     print(my_list[5])
# else:
#     print('That index does not exist')


# ========

# Pythonic

# my_list = [1,2,3,4,5,6]
# try:   
#     print(my_list[9])
# except IndexError:
#     print('That index does not exist')


# --------------

# import os

# my_file = "/tmp/test.txt"

# # Race condition
# if os.access(my_file,os.R_OK):
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print('File can not be accessed')



# ---------------
# No Race Condition

import os

my_file = "/tmp/test.txt"

try:
    f = open(my_file)
except IOError as e:
    print(e)

else:
    with f:
        print(f.read())

