# import ImportModule


# courses = ['History', 'Math','Physics', 'CompSci']
# index = ImportModule.find_index(courses,'Math')
# print(index)


# import ImportModule as mm

# courses = ['History', 'Math','Physics', 'CompSci']
# index = mm.find_index(courses,'Math')
# print(index)

# It gives only access to find_index function
# from ImportModule import find_index

# courses = ['History', 'Math','Physics', 'CompSci']
# index = find_index(courses,'Math')
# print(index)


# Below will give access to test variable and find_index
# from ImportModule import find_index as fi, test

# courses = ['History', 'Math','Physics', 'CompSci']

# index = fi(courses,'Math')
# print(index,test)


#  for importing everything we can do like below

# from ImportModule import *

# courses = ['History', 'Math','Physics', 'CompSci']
# index = find_index(courses,'Math')
# print(index)
# print(test)

# When we importing a module how does it know that where to find this module
#  the way it work when we import a module it checks multiple location
#  and location it checks is within a list called sys.path


# from ImportModule import find_index, test 
# import sys 

# courses = ['History', 'Math','Physics', 'CompSci']
# index = find_index(courses,'Math')
# # This will gives us the list of directory on our machine where python looks for module when we run import and it looks in this order\
# #  First value in sys.path result is the directory we are currently running the script from
# # 2nd value is path of environment variable and after that it added python library
# # and at last it take a look of site packages
# print(sys.path)


# The module we want to import isn't in the same directory the script we are trying to import from 
# then we need to append when we import the path then we will be able to use that import function whatever the location it is in


# import sys
# sys.path.append("mentioned path here")


# Random module
# random value from courses list
import random
courses = ['History', 'Math','Physics', 'CompSci']

random_course = random.choice(courses)
print(random_course)


# Math module
import math
rads = math.radians(90)

print(math.sin(rads))


# Datetime module
import datetime
import calendar
courses = ['History', 'Math','Physics', 'CompSci']
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

# OS Module

import os 

# it will print current working directory
print(os.getcwd())


# It gives us the ability to scan the filesystem, create file , delete file and all of that 
# This modules are just the python file themselves
# We can view the location of the file just by printing  out its 
# dunder file attribute (dunder means double underscore)



print(os.__file__)