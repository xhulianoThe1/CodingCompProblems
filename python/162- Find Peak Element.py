class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1 or nums[0] > nums[1]: 
            return 0 
        i = 0
        k = - 1
        while i < len(nums): 
            if nums[i] > nums[k]: 
                k -= 1  
            elif nums[i] < nums[k]: 
                i += 1 
            elif nums[i] == nums[k] and i != len(nums)+k: 
                i += 1 
            elif  i == len(nums)+k : 
                return i
