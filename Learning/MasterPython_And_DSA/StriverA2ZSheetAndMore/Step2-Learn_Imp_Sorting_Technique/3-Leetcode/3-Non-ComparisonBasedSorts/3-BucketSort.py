
'''
Bucket Sort:- https://leetcode.com/explore/learn/card/sorting/695/non-comparison-based-sorts/4439/
'''

class Solution:
    def bucket_sort(self, lst: List[int], K) -> None:
        """
        Sorts a list of integers using K buckets
        """
        buckets = [[] for _ in range(K)]

        # place elements into buckets
        shift = min(lst)
        max_val = max(lst) - shift
        bucket_size = max(1, max_val / K)
        for i, elem in enumerate(lst):
            # same as K * lst[i] / max(lst)
            index = (elem - shift) // bucket_size
            # edge case for max value
            if index == K:
                # put the max value in the last bucket
                buckets[K - 1].append(elem)
            else:
                buckets[index].append(elem)

        # sort individual buckets
        for bucket in buckets:
            bucket.sort()

        # convert sorted buckets into final output
        sorted_array = []
        for bucket in buckets:
            sorted_array.extend(bucket)

        # common practice to mutate original array with sorted elements
        # perfectly fine to just return sorted_array instead
        for i in range(len(lst)):
            lst[i] = sorted_array[i]