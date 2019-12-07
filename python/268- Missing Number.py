class Solution(object):
    def missingNumber(self, nums):
        a = sum(nums)
        total = 0 
        for i in range(0, len(nums)+1): 
            total += i
        return total - a
