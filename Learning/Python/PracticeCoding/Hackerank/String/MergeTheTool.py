# Merge the tool
# Problem Link:- https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

s = 'AABCAAADA'
k = 3

# print(set(s))
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        st = string[i:i+k]
        ans= ''
        for char in st:
            if char not in ans:
                ans += char
        print(ans)
            
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# Code 2

# If order not matters then we cna use  set like below code
def merge_the_tools(s, k):
    # your code goes here
    start = 0
    end = k
    while end<=len(s):
        temp = s[start:end]
        chunks = list(set(list(temp)))
        print(''.join(chunks))
        start += k
        end += k
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# Code 3

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        seen = set()
        unique_sbstr = ''
        for c in string[i:i+k]:
            if c not in seen:
                seen.add(c)
                unique_sbstr += c
        print(unique_sbstr)
            
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# Above code in list comprehension

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        seen = set()
        print(''.join(c for c in string[i:i+k] if not (c in seen or seen.add(c))))
    
            
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# 

def merge_the_tools(s, k):
    print('\n'.join(''.join(dict.fromkeys(s[i:i+k])) for i in range(0, len(s), k)))

# Example Usage
merge_the_tools("AABCAAADA", 3)

