
# Code class Decorators 

# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
#     def __call__(self,*args, **kwargs):
#         print('call method executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)

# @decorator_class
# def display():
#     print('display function run')

# @decorator_class
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name,age))

# display_info('John',25) 
# display()



# Practical example

# Common usecases for Decorators in python is logging and timing of how much func run
#  Let say we want to keep track of specific func is that how many times it run 
#  what arguments has passed to those func




# Decorators  ===================  CODE

from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))



# display_info = my_logger(my_timer(display_info))
display_info('Tom', 22)
# print(display_info.__name__)