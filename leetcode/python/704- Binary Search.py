class Solution(object):
    def search(self, nums, target):
        #left pointer starting at the leftmost end of the array
        left = 0 
        #right pointer starting at the rightmost end of the array
        right = len(nums) -1 
        while left <= right: 
            mid = left + (right - left) //2 #;) 
            #if the middle of the search is the target we're done
            if nums[mid] == target: 
                return mid
            #if the target is smaller search the left side of the array
            elif target < nums[mid]: 
                right = mid -1
            else: 
                left = mid + 1
        return -1 
       
       
        
