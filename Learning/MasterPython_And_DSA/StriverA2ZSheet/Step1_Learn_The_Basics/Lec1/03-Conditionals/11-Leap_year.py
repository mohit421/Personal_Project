# Problem link:- https://www.geeksforgeeks.org/problems/leap-year-1598599919--155509/1?&selectedLang=python3

# Solution 1
year = int(input())

if((year%4==0 and year%100 != 0) or (year%400 == 0)):
    print(True)

else:
    print(False)


# Soluiton 2 
is_leap = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

