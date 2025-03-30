# Generators
#  Advantages over list 


# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

# my_nums = square_numbers([1,2,3,4,5])
# print (my_nums) # [1,4,9,16,25]


# yield keyword make it generator
#  Generator don't hold the entire result in the memory 
# It yield one result at a time. It waiting for us to ask for next result


# def square_numbers(nums):
#     for i in nums:
#         yield(i*i)

# my_nums = square_numbers([1,2,3,4,5])
# print (my_nums) # return generators objects here
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums)) # got error entire iteration got exhausted and stopIteration means out of value


# =====================

# Instead of getting one value at a time we still use a for loop in this generators


# def square_numbers(nums):
#     for i in nums:
#         yield(i*i)

# my_nums = square_numbers([1,2,3,4,5])
# # We don't get stopIteration error bcuz it for loop know when to stop this iteration
# for num in my_nums:
#     print(num)

# ---------
# This can be also write u using list comprehension by using parenthessi instead of list square braces
# this will return generator objects

# my_nums = (x*x for x in [1,2,3,4,5])
# print(list(my_nums))
# for num in my_nums:
#     print(num)


# -----------------------////////////////////

# import mem_profile
# import random 
# import time

# names = ['John','Corey','Adam','Steve','Rick','Thomas']
# majors = ['Math',"engineering",'CompSci','Arts','Business']

# print('memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))

# def people_list(num_people):
#     result = []
#     for i in range(num_people):
#         person = {
#             'id': i,
#             'name': random.choice(names),
#             'major': random.choice(majors)

#         }
#         result.append(person)
#     return result

# def people_generator(num_people):
#     for i in xrange(num_people):
#         person = {
#             'id': i,
#             'name': random.choice(names),
#             'major': random.choice(majors)
#         }
#     yield person 

# t1 = time.clock()
# # 1 million value value we will check how much memory usage and time tit took
# person = people_list(100000)
# t2 = time.clock()


# print('memory (After): {}Mb'.format(mem_profile.memory_usage_resource()))
# print('Took {} Seconds'.formayt(t2-t1))




import psutil
import os
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def memory_usage():
    """Return the memory usage in MB using psutil."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)  # Convert bytes to MB

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        yield {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

print(f"Memory (Before): {memory_usage()} MB")

# Timing and memory usage for people_list
start_time = time.perf_counter()
person_list = people_list(100000)
end_time = time.perf_counter()
print(f"Memory (After using list): {memory_usage()} MB")
print(f"List took {end_time - start_time:.4f} seconds")

# Timing and memory usage for people_generator
start_time = time.perf_counter()
person_gen = people_generator(100000)
end_time = time.perf_counter()
print(f"Memory (After using generator): {memory_usage()} MB")
print(f"Generator took {end_time - start_time:.4f} seconds")
