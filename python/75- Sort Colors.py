#Solution O(n^2) time
class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)): 
            for k in range(i+1, len(nums)): 
                if nums[i] > nums[k]: 
                    nums[i], nums[k] = nums[k], nums[i]
        return nums
