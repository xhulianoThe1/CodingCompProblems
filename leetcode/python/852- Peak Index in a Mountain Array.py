class Solution(object):
    def peakIndexInMountainArray(self, nums):
        for i in range(len(nums)): 
            if nums[i] > nums[i+1]: 
                return i
