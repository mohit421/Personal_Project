# Problem link: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

import calendar

def is_leap(year):
    leap = False
    
    # Write your logic here
    # if year%4==0:
    #     if year%100 !=0 or year%400==0:
    #         leap = True
    # return leap
    return calendar.isleap(year)
year = int(input())
print(is_leap(year))