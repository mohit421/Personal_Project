class Solution:
    
    def heapify(self,arr, n, i):
        largest = i 
        l = 2*i + 1
        r = 2*i + 2
        
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
            
        if largest != i:
            arr[i],arr[largest] = arr[largest], arr[i]
            self.heapify(arr,n,largest)
            
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        # build heap (rearrange array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)
        
        # one by one extract an element from heap
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)
            
        return nums
        
