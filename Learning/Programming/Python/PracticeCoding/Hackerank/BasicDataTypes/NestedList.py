# Nested Lists

# Problem link:- https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true


if __name__ == '__main__':
    my_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append([name,score])
    
    scores = sorted(set([lst[1] for lst in my_list]))
    second_lowest_scores = scores[1]
    names = [nam[0] for nam in my_list if nam[1] == second_lowest_scores]
    for nm in sorted(names):
        print(nm)


# using setdefault 

if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.setdefault(score,[]).append(name)
        
    second_lowest_score = sorted(students.keys())[1]
    
    for name in sorted(students[second_lowest_score]):
        print(name)
    