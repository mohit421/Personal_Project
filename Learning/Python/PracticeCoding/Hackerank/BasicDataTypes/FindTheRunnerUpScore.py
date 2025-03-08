# Find the Runner-Up Score!
# Hackerrank problem link  :- https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

# Using simple sorting and for loop

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = sorted(arr,reverse=True)
    for i in range(n-1):
        if sorted_arr[i] !=sorted_arr[i+1]:
            print(sorted_arr[i+1])
            break
        else:
            continue
    


# By removing all max_score occurence and list comprehension
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    # get max score
    max_score = max(arr) 
    # remove all max_)score occurence
    lst = [i for i in arr if i!=max_score]
    runner_up = max(lst)
    print(runner_up)



# Using set

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    unique_scores = list(set(arr))  # Convert to set to remove duplicates
    unique_scores.sort(reverse=True)  # Sort in descending order
    print(unique_scores[1])  # Print the second element (runner-up)


# using heap , efficient for large inputs

import heapq

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    runner_up = heapq.nlargest(2, set(arr))[1]  # Get the two largest unique elements
    print(runner_up)


# Runs in O(n) time complexity, making it efficient for large inputs.
