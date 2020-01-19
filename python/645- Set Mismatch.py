class Solution(object):
    def findErrorNums(self, nums):
        arr = [] 
        for i in range(1, len(nums)+1):
            arr.append(i)
        dup = sum(nums) - sum(set(nums)) 
        for i in range(len(nums)): 
            if nums[i] == dup: 
                del nums[i]
                break 
        return [dup, sum(arr)-sum(nums)]
