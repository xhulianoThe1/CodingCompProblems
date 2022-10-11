class Solution(object):
    def findKthLargest(self, nums, k):
        i = 1
        while i < k: 
            a = max(nums)
            nums.remove(a)
            i+=1 
        return max(nums)
