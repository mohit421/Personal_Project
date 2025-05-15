# Problem link:- https://www.geeksforgeeks.org/problems/the-fizzbuzz-program--125723/1?&selectedLang=python3

# Solution 1

def fizzbuzz_number(a):
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)

# Solution 2

def fizzbuzz_number(a):
    if a % 15 == 0:
        print("FizzBuzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)


# Solution 3 Using string concatenation

def fizzbuzz_number(a):
    output = ""
    if a % 3 == 0:
        output += "Fizz"
    if a % 5 == 0:
        output += "Buzz"
    print(output or a)


# Solution 4 Using Ternary Expression

def fizzbuzz_number(a):
    print("FizzBuzz" if a % 15 == 0 else "Fizz" if a % 3 == 0 else "Buzz" if a % 5 == 0 else a)

# Solution 6

a = int(input())
match(a%3==0, a%5==0):
    case (True, True):
        print("FizzBuzz")
    case (True, False):
        print("Fizz")
    case (False,True):
        print("Buzz")
    case _:
        print(a)