class Solution(object):
    def removeDuplicates(self, nums): 
        if len(nums) == 0: 
            return 0 
        if len(nums) == 1:
            return 1 
        i = 1
        while i < len(nums): 
            if nums[i] == nums[i-1]: 
                del nums[i] 
            else: 
                i+= 1
        print i 
