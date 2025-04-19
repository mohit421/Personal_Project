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

'''
- Now we have an iterator our our nums list 
- This is what that for loop gets for us in the background
- Let's also pass this into the dir method and see what attributes and methods are available to us.

- Now we have our iterators of our nums list 
'''
# i_nums = nums.__iter__()

'''
- it's bit ugly to run our dunder method like above 
- So for most of these there are functions that call these in the background for us so just like I said that the next funct calls the dunder next method (__next__) and the iter function calls the dunder iter mthod(__iter__)
'''
# List iterator
i_nums = iter(nums)

# print(i_nums)
# print(dir(i_nums))

'''
- You might think that is little weird thatiterator has a dunder iter method that's what we ran on our original list in order to get the iterator that we have now but it has to have a dunder iter method bcuz iterator are also iterable
- Iterators are also iterables but the difference is that this __iter__ method retuns the same object so it just return self 

- Previously when we ran next on our original list it threw an error and said that our list wasn't an iterator and that's bcuz it didn't have the dunder next method but our iterator that we just return above does have dunder next method so we should be able to get the next value from this
'''

'''
- this palce it's the fisrt items in the oprigina list now 
- An iteratior is an object with a state so that it remembers where it is during iteration so if we run next on this again 
then it shoudl remember wher it left off and print the next value 
- next method pointed to te next value in the iterator 
'''

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))


'''
- when we run one more time it thre a StopIteration exception now that's excepted so if we run out of values then it raises a stop iteration exception but that's what iterators are meatn to do 
- If we run out of values then it raises a stop iteration exveption but that's what iterators are meant to do so 
- If we hit stop iteratiion exception it means that the iterator has been exhausted and has no more values so we can see it when we run though hem manually like this but when we run a normal for loop it knows how to handle the stop iteration exception and doesn't show it to us so in the background a  for loop is  basically doing something like this
- It's first getting an iterator of our origianl object like we have done above and then it getting the next value until it hits a stop iteration  exception
'''
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

'''
- If we run aboove then we basically got the same result from before when we ran our simple for loop now another characteristics of iterators that i should have mentioned is that they can only go forward so ther's no going backwards resetting it or making a copy of it 
- We can only go forward by calling next if we neex to start from scratch then you can simply create a new iterator object from scratch
'''

'''
- Why does any of this really matter ? so what is the practical examples of knowing this 
-  One example is that we can add these methods to our own classes and make them iterable as well 
# Let's see an examples :-
- Let's create a class that basically behaves like the built-in range function 
'''


class MyRange:

    def __init__(self, start, end):
        self.value = start 
        self.end = end 

    def __iter__(self):
        return self  

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value 
        self.value += 1 
        return current 
    

nums = MyRange(1,10)
for num in nums:
    print(num)