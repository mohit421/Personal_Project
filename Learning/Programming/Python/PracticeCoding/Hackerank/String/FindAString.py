# Find a String 

# Problem Link:- https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

'''
✅ Handles overlapping occurrences
✅ Time Complexity: O(n * m), where n = length of string, m = length of sub_string
'''
def count_substring(string, sub_string):
    l = len(sub_string)
    count = 0
    for i in range(len(string)-l+1):
        if string[i:l+i]==sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)



# Code 2

'''
✅ Handles overlapping occurrences
✅ Efficient since it directly finds the next occurrence
'''

def count_substring(string, sub_string):
    count = 0
    start = 0
    while True:
        start = string.find(sub_string,start) 
        if start == -1:
            break 
            
        count +=1 
        start +=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# Code 3

# ✅ Method 4: Using count() (Not for Overlapping Matches)
'''
 Does not count overlapping occurrences!
⚡ Fastest but may not be accepted in HackerRank if overlaps are required.
'''
def count_substring(string, sub_string):
    return string.count(sub_string)  # Simple method

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    print(count_substring(string, sub_string))