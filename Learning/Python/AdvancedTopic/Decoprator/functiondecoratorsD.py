# Decorators

# Who it work and when and how to use it

# First class function :-
# First class function is allow us to treat function like any other object
# We can pass function as argument to another function, we can return function 
#  and we can assign function to variables

# Closures:-
#  It allow us to take advantage of first class function and returns an inner functions that 
#   remembers and has access to variables local to the scope which they were created


# Quick recap of first class functions nd closures

# message variable isn't created inside inner_function but instead have access inside inner function 
#  that's message variable known as free variable

# def outer_function():
#     message = 'HI'

#     def inner_function():
#         print(message)
#     return inner_function()

# outer_function()

# =======================================
# It will print out message variable multiple times that whats the closure is
# It remember the message variable even after outer function has finished its execution

# ------------Code--------/////////////////

# def outer_function():
#     message = 'HI'

#     def inner_function():
#         print(message)
#     return inner_function

# my_func = outer_function()
# my_func()
# my_func()
# my_func()


# -----------------Code


# def outer_function(msg):
#     message = msg

#     def inner_function():
#         print(message)
#     return inner_function

# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()


# --------------------Code

# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function

# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()


# ////////////////////\\\\\\\\ Decorators --------------

# Decorator is very much similar to what we have done above 
# It is just a func that takes another function as an arguments add some kind of functionality
#  and return another function. All of these without altering the source code 
#  of the original function that have passed in 
# Instead of message we just take a function as an argument original_function
# and within in our wrapper function we just return original_function
# this is a decorator


# ---------_ Code

# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function


# -------------Code
# decorated_display is just equal to our wrapper_function 
# and its waiting to be executed and when it executed it just execute the original function we passed in and returns it
# now we can run decorated_display variable just like any other function 


# basic decorator function

# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function

# def display():
#     print('Display function ran')

# decorated_display = decorator_function(display)

# decorated_display()


# _________________________________================_____________

# Decorating our function is allow us to easily add functionality to our 
# existing functions by adding that functionality inside of our wrapper 

# This will executed our wrapper message before executed our original display function and printed it out
# that message

# code


# def decorator_function(original_function):
#     def wrapper_function():
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function()
#     return wrapper_function

# def display():
#     print('Display function ran')

# # so far we have used this syntax to create our decorator function 

# decorated_display = decorator_function(display)
# decorated_display()

# ------------------------------------------________+++++++++++++++++++++++


# def decorator_function(original_function):
#     def wrapper_function():
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function()
#     return wrapper_function

# @decorator_function
# def display():
#     print('Display function ran')

# # # so far we have used this syntax to create our decorator function 
# # # but using @decorator_function above display function is same as below line
# # decorated_display = decorator_function(display)
## decorated_display()


# ----------------------Code 


# def decorator_function(original_function):
#     def wrapper_function():
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function()
#     return wrapper_function

# @decorator_function
# def display():
#     print('Display function ran')
# display()

# @decorator_function is same as '''display = decorator_function(display)'''



# ///////////////-------------------- Code 

# Another example

#  what if i want to display both display function and display_info function
# getting error "" TypeError: decorator_function.<locals>.wrapper_function() 
# takes 0 positional arguments but 2 were given"""

# def decorator_function(original_function):
#     def wrapper_function():
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function()
#     return wrapper_function

# @decorator_function
# def display():
#     print('Display function ran')
# # display()

# @decorator_function
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name,age))

# display_info('John',25) 



# -0-----------------------------
# we need to pass any number of positional or keyword argument to our wrapper function 
# the way we are adding like *args and **kwargs to our wrapper function 
#  Now it works with both of our function now

def decorator_function(original_function):
    def wrapper_function(*args, ** kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('Display function ran')
# display()

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John',25) 
