#Problme Link m:- https://www.geeksforgeeks.org/problems/cat-and-hat-python/1?&selectedLang=python3
# 
#  Solution 1 Using SLiding windowe 

def cat_hat_same_count(s):
    cat_count = hat_count = 0
    for i in range(len(s) - 2):
        if s[i:i+3] == "cat":
            cat_count += 1
        elif s[i:i+3] == "hat":
            hat_count += 1
    return cat_count == hat_count


# Solution 2

def cat_hat(str):
  ##your code here##
  ##You need to write complete code this time 
    return str.count('cat') == str.count('hat')


#   Solution 3 Using regular experssion


import re

def cat_hat_same_count(s):
    cat = re.findall('cat', s)
    hat = re.findall('hat', s)
    return len(cat) == len(hat)


# Solution 4  Using list comprehension

def cat_hat_same_count(s):
    cat_count = sum(1 for i in range(len(s)-2) if s[i:i+3] == 'cat')
    hat_count = sum(1 for i in range(len(s)-2) if s[i:i+3] == 'hat')
    return cat_count == hat_count


# Solution 5 Elegant one-liner


def cat_hat_same_count(s):
    return sum(s[i:i+3] == 'cat' for i in range(len(s)-2)) == sum(s[i:i+3] == 'hat' for i in range(len(s)-2))


# Solution 5  Using a dictionary to count manually

def cat_hat_same_count(s):
    counts = {"cat": 0, "hat": 0}
    for i in range(len(s) - 2):
        sub = s[i:i+3]
        if sub in counts:
            counts[sub] += 1
    return counts["cat"] == counts["hat"]
