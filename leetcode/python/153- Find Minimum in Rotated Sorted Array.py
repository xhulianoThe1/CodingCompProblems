class Solution(object):
    def findMin(self, nums):
        k = -1
        i = 0 
        while i < len(nums): 
            if nums[i] > nums[k]: 
                i+=1 
            elif nums[i] < nums[k]: 
                k -=1 
            elif nums[i] == nums[k]: 
                return nums[i]
