class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count, maxc = 0, 0 
        for i in nums:
            if i == 1: 
                count += 1
                maxc = max(count, maxc)
            else:
                count = 0 
        return max(count, maxc)
