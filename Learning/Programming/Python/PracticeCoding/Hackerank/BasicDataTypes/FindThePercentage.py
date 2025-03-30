# Finding the percentage hackerrank

# Problem link :- https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true


'''
✅ Time Complexity: O(n)
✅ Space Complexity: O(n)
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        avg = sum(student_marks[query_name])/len(student_marks[query_name])
    print(f"{avg:.2f}")



# using dict comprehension

'''
✅ More concise and readable
✅ Avoids extra for loops
'''

if __name__ == '__main__':
    n = int(input())

    student_marks = {name: list(map(float, scores)) for name, *scores in (input().split() for _ in range(n))}
    
    query_name = input()
    avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    print(f"{avg_score:.2f}")


# using numpy

import numpy as np

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *scores = input().split()
        student_marks[name] = np.array(scores, dtype=float)  # Store as NumPy array

    query_name = input()
    print(f"{np.mean(student_marks[query_name]):.2f}")  # NumPy's mean function
