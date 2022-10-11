class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        nums = sorted(nums, reverse = True)
        if len(nums) < 3: 
            return max(nums)
        else: 
            return nums[2]
