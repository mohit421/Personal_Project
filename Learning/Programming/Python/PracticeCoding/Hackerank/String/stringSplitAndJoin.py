# String Split and Join

# Problem Link:- https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
'''
✅ Time Complexity: O(n)
✅ Space Complexity: O(n)


'''
def split_and_join(line):
    # write your code here
    # line = line.split(" ")
    # line = "-".join(line)
    line = '-'.join(line.split(" "))
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# Code 2

def split_and_join(line):
    return line.replace(" ", "-")

if __name__ == '__main__':
    line = input()
    print(split_and_join(line))


# Using lint comprehension

def split_and_join(line):
    return "-".join([word for word in line.split()])

if __name__ == '__main__':
    line = input()
    print(split_and_join(line))
