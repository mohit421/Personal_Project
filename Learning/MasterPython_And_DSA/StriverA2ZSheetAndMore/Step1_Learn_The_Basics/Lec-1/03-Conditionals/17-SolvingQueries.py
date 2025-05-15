# OProblme link:- 


# Solurtion 1

a = list(map(int, input().split()))
b = list(map(str, input().split()))
query = list(map(int, input().split()))
dict = {}
for i in range(len(a)):
    dict[a[i]] = b[i]
        
ans = []
for key in range(len(query)):
    ########### Write your code below ###############
    # get value for given key
    if query[key] in dict:
        val = dict[query[key]] 
    ########### Write your code above ###############
    else:
         val = "None"
    # append to ans
    ans.append(val)

# Print ans
print(*ans, sep='\n')

# Soluioon 2  List Comprehension with get()
'''
Part 1: [d.get(key, "None") for key in queries] — List Comprehension
🔹 What's happening:
This is a compact way to loop over queries and get values from d.

Step-by-step:

result = []
for key in queries:
    result.append(d.get(key, "None"))
But instead of writing it like that, you write it concisely as:


[d.get(key, "None") for key in queries]
📌 d.get(key, "None") means:

If key is in d, return d[key]

Otherwise, return "None"

 Part 2: print(*..., sep="\n") — Unpacking and printing each on new line
* — Unpacking:
This turns the list into separate arguments:

print("cde", "fgh", "None", sep="\n")
sep="\n":
Each item will be printed on a new line.
'''
def query_dict(d, queries):
    print(*[d.get(key, "None") for key in queries], sep="\n")

# Solution 3 Using .get() Method (Simplest & Most Pythonic)

def query_dict(d, queries):
    for key in queries:
        print(d.get(key, "None"))


# SOlution 4 Using a class with Method Lookup

class DictQuery:
    def __init__(self, d):
        self.d = d

    def run_queries(self, queries):
        for key in queries:
            print(self.d.get(key, "None"))


# Siluton 5   Using Exception Handling (try-except)
def query_dict(d, queries):
    for key in queries:
        try:
            print(d[key])
        except KeyError:
            print("None")

# Solution 6 Using map() and lambda (Functional Style)

def query_dict(d, queries):
    for key in queries:
        try:
            print(d[key])
        except KeyError:
            print("None")
