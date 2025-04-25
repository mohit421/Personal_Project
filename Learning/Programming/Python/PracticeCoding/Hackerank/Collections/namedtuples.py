# Collections.namedtuples()

# Solution 1
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

N  = int(input())
names = input().split()
Student = namedtuple('Student',names)
total = 0
for i in range(N):
    data = input().split()
    student = Student(*data) 
    total += int(student.MARKS)

print(f"{total / N:.2f}")

# Solution 2
# Without using namedtuples

N  = int(input())
columns = input().split()
marks_index = columns.index('MARKS')
total = 0
for _ in range(N):
    data = input().split()
    total += int(data[marks_index])
print(f"{total /N:.2f}")    



# Solution 3
# Approach : Using csv.DictReader for dictionary-based column access
import sys
import csv

n = int(input())
columns = input().split()

# Read remaining n rows
data = [input().split() for _ in range(n)]

# Simulate CSV DictReader with tabular data
total = 0
for row in data:
    row_dict = dict(zip(columns, row))
    total += int(row_dict['MARKS'])

print(f"{total / n:.2f}")



# SOlution 4
# ✅ Approach : With a simple list of dicts
n = int(input())
columns = input().split()

students = []
for _ in range(n):
    row = input().split()
    students.append(dict(zip(columns, row)))

average = sum(int(s['MARKS']) for s in students) / n
print(f"{average:.2f}")
