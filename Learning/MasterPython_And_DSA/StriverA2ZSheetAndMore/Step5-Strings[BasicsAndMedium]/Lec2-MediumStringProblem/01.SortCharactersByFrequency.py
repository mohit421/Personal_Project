'''
# Sort Dictionary by Values in Python

This example demonstrates how to sort a Python dictionary based on its values, both in ascending and descending order.

## 🐍 Code Example

```python
# Original dictionary
my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# Sort by values in ascending order
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", sorted_dict)

# Sort by values in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_dict_desc)


Output:-
Ascending: {'pear': 1, 'orange': 2, 'banana': 3, 'apple': 4}
Descending: {'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1}


Explanation
dict.items() returns a view of the dictionary’s key-value pairs.

sorted() can sort those pairs.

key=lambda item: item[1] tells sorted() to sort by the values.

reverse=True sorts the dictionary in descending order.
'''



# Solution 1

'''
Time & Space Complexity:
Time Complexity:

Counter(s) = O(n)

Grouping into buckets = O(k), where k is number of unique chars (≤ n)

Final loop = O(n)
✅ Total = O(n)

Space Complexity:

Counter = O(k)

bucket = O(n) (in worst case, all chars are unique)

res list = O(n)
✅ Total = O(n)

 Why it's efficient:
It avoids sorting the characters explicitly (which would be O(n log n)).

Uses a bucket sort idea by frequency, which is linear time.
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        bucket = defaultdict(list)
        for key, val in count.items():
            bucket[val].append(key)
        
        res = []
        for i in range(len(s),0,-1):
            for c in bucket[i]:
                res.append(c*i)
        return ''.join(res)




# Solution 2

class Solution:
    def frequencySort(self, s: str) -> str:
        st = {}
        for i in s:
            st[i] = 1 + st.get(i,0)
        srtd = dict(sorted(st.items(), key=lambda item: item[1], reverse=True))
        ans = ""
        for k,v in srtd.items():
            ans += k*v 
        return ans
