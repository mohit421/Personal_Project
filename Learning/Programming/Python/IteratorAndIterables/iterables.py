nums = [1,2,3]

# for num in nums:
#     print(num) 

'''
- Loops aren't the only things that we can loop over 
- we can loop over tuples, dictionaries , strings, files , generators and all kinds of different objects 
- SO what actually is going on the backgound there 
- how can be thing of something can be looped over or not or another way to ask this is how can we tell if something is iterable 
- if something is iterable then it need to have a special method called double underscore iter ('__iter__()') 
- Double underscore method is also called dunder methods or special methods or also magic methods
- so let's see of our list has this dunder iter method
- So tool at the method and attributes available to a specific object we can simply pass that into the built-in dir function and print that out 
- It will returns alots of methods and attributes but if we look through here then we can see that one of these methods __iter__
so our list gave that dunder iter method
- SO basically something can be looped over if it has that method ,
so what the for loop is doing in the background is calling iter object and returning an iterator that we can loop over 
- So that is why we call out list iterable


'''

# print(dir(nums))


'''
Iterator :- An iterator is an object with a state so that it remembers where it is during iteration a
and Iterator also know how to get their next value they get their next value with a dunder next method so If we look at our list methods then you will see that there's no dunder next method in for our list.
- So our list doesn't have a state and it doesn't know how to get its next value , so therefore it isn't an iterator 
- So let's take an example if we try to print next vaule of my list that will gives us an type error
- Error :- TypeError: 'list' object is not an iterator
- It gives us error because in background it's try to run __next__ method to our list 
'''

# print(next(nums))

# i_nums = nums.__iter__()
i_nums = iter(nums)

print(i_nums)
print(dir(i_nums))