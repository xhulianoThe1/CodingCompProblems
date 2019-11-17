class Solution(object):
    def containsDuplicate(self, nums):
        nums = sorted(nums)
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]: 
                return True 
            i+=1
        return False
