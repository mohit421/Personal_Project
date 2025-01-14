
# ----------------------------------= CODE =-----------------------------------

# def hello_func():
#     pass

# print(hello_func)
# print(hello_func())


# -------------- CODE ------------------------------------------------

# if we have to print same thing mutiple times like below

# print('Hello Function!')
# print('Hello Function!')
# print('Hello Function!')
# print('Hello Function!')

# But what if we want to change something what we have printed so we need to go to every line and change it, so here function comes into picture
# we only need to change inside function and that's work
# it follow DRY -- DOn't repeat yourself
# -------------------------------------- CODE ------------------------------

# def hello_func():
#     print('Hello Function!dfs')

# hello_func()
# hello_func()
# hello_func()
# hello_func()

# -------------------------------------- CODE ------------------------------

# func is equal to return value
# def hello_func():
#     return 'Hello Function!dfs'


# print(hello_func())

# print(len('Test'))

# -------------------------------------- CODE ------------------------------

# we can chained func 
# def hello_func():
#     return 'Hello Function!dfs'


# print(hello_func().upper())


# -------------------------------------- CODE ------------------------------

# # Parameter func

# def hello_func(greeting):
#     return '{} function.'.format(greeting)

# # hello_func() missing 1 required positional argument: 'greeting'
# print(hello_func())


# -------------------------------------- CODE ------------------------------

# Parameter func

# def hello_func(greeting):
#     return '{} function.'.format(greeting)

# print(hello_func('Good morning'))


# -------------------------------------- CODE ------------------------------

# Default value opf greeting

# def hello_func(greeting='Hi', name='Mohit'):
#     return '{}, {} function.'.format(greeting,name)

# print(hello_func())


# -------------------------------------- CODE ------------------------------

# # Positional keyword argument - Default value - it will be printed if we don't pass any parameter


# def hello_func(greeting='Hi', name='Mohit'):
#     return '{}, {} function.'.format(greeting,name)

# print(hello_func('Hi',name='Corey'))


# -------------------------------------- CODE ------------------------------

# def student_info(*args,**kwargs):
#     print(args) # this will print positional argument
#     print(kwargs) # this will print keyword argument


# student_info('Math', 'Art', name='Mohit', age = 22)




# # -------------------------------------- CODE ------------------------------

# def student_info(*args,**kwargs):
#     print(args) # this will print positional argument
#     print(kwargs) # this will print keyword argument


# courses = ['Math', 'Art']
# info = {'name':'Mohit','age':24}

# student_info(courses, info)


# # -------------------------------------- CODE ------------------------------

# def student_info(*args,**kwargs):
#     print(args) # this will print positional argument
#     print(kwargs) # this will print keyword argument


# courses = ['Math', 'Art']
# info = {'name':'Mohit','age':24}

# #  to unpack all this otherwise like above exapmle both will be taken as positional argument - *args , and for **kwargs will be empty dict
# student_info(*courses, **info)



# -------------------------------------- CODE ------------------------------

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2017))
print(is_leap(2020))

print(days_in_month(2017,2))
print(days_in_month(2020,3))
print(days_in_month(2020,2))