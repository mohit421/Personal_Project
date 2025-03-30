# Minion Game

# Problem Link :- https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true




def minion_game(string):
    # your code goes here
    vow = 'aeiou'
    Kevin_vow = 0
    stuart_const = 0
    n= len(string)
    for i in range(len(string)):
        letter = string[i].lower()
        remain = n-i
        if letter in vow:
            Kevin_vow += remain
        else:
            stuart_const += remain
    if stuart_const == Kevin_vow:
        print("Draw")
    elif stuart_const > Kevin_vow:
        print("Stuart", stuart_const)
    else:
        print("Kevin", Kevin_vow)
if __name__ == '__main__':
    s = input()
    minion_game(s)


# Code 2
'''
 Approach 2: Using Dictionary for Score Tracking
🔸 Time Complexity: O(N²)
🔸 Idea: Store scores in a dictionary and update values.
'''
def minion_game(s):
    vowels = "AEIOU"
    scores = {"Kevin": 0, "Stuart": 0}
    length = len(s)

    for i in range(length):
        if s[i] in vowels:
            scores["Kevin"] += (length - i)
        else:
            scores["Stuart"] += (length - i)

    if scores["Kevin"] > scores["Stuart"]:
        print(f"Kevin {scores['Kevin']}")
    elif scores["Stuart"] > scores["Kevin"]:
        print(f"Stuart {scores['Stuart']}")
    else:
        print("Draw")

# Example Usage
minion_game("BANANA")



'''
 Approach 1: Brute Force (Nested Loops)
🔸 Time Complexity: O(N²)
🔸 Idea: Generate all possible substrings and count occurrences.


'''


def minion_game(s):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    length = len(s)

    for i in range(length):  # Outer loop (O(N))
        for j in range(i, length):  # Inner loop (O(N))
            if s[i] in vowels:
                kevin_score += 1
            else:
                stuart_score += 1

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")





# Code 3
'''
Approach 3: Using List Comprehension
✅ Time Complexity: O(N) (Linear Time)
✅ Space Complexity: O(1) (Constant Space, as we only use a few integer variables)
'''
def minion_game(s):
    vowels = "AEIOU"
    length = len(s)
    
    kevin_score = sum(length - i for i in range(length) if s[i] in vowels)
    stuart_score = sum(length - i for i in range(length) if s[i] not in vowels)

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

# Example Usage
minion_game("BANANA")


# Code 4

'''
 Approach 4: Optimized Approach Using Counter
🔸 Time Complexity: O(N)
🔸 Idea: Instead of iterating twice, use the Counter method.
'''
from collections import Counter

def minion_game(s):
    vowels = set("AEIOU")
    counts = Counter({"Kevin": 0, "Stuart": 0})
    length = len(s)

    for i, char in enumerate(s):
        counts["Kevin" if char in vowels else "Stuart"] += (length - i)

    if counts["Kevin"] > counts["Stuart"]:
        print(f"Kevin {counts['Kevin']}")
    elif counts["Stuart"] > counts["Kevin"]:
        print(f"Stuart {counts['Stuart']}")
    else:
        print("Draw")

# Example Usage
minion_game("BANANA")



# Code 5

'''
Approach 5: Using Generators for Memory Efficiency
🔸 Time Complexity: O(N)
🔸 Idea: Instead of storing scores, use a generator to calculate dynamically.
'''

def minion_game(s):
    vowels = "AEIOU"
    length = len(s)

    kevin_score = sum((length - i) for i in range(length) if s[i] in vowels)
    stuart_score = sum((length - i) for i in range(length) if s[i] not in vowels)

    print(f"Kevin {kevin_score}" if kevin_score > stuart_score else 
          f"Stuart {stuart_score}" if stuart_score > kevin_score else "Draw")

# Example Usage
minion_game("BANANA")



# Code 6


'''
 Approach 6: Using Functional Programming (map & sum)
🔸 Time Complexity: O(N)
🔸 Idea: Use map() to apply (length - i) calculation dynamically.
'''
def minion_game(s):
    vowels = "AEIOU"
    length = len(s)

    kevin_score = sum(map(lambda i: length - i, filter(lambda i: s[i] in vowels, range(length))))
    stuart_score = sum(map(lambda i: length - i, filter(lambda i: s[i] not in vowels, range(length))))

    print(f"Kevin {kevin_score}" if kevin_score > stuart_score else 
          f"Stuart {stuart_score}" if stuart_score > kevin_score else "Draw")

# Example Usage
minion_game("BANANA")
