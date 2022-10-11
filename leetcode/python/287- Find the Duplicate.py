from collections import Counter 
class Solution(object):
    def findDuplicate(self, nums):
# SOL: 1
#         nums.sort()
#         for i in range(len(nums)): 
#             if nums[i] == nums[i-1]: 
#                 return nums[i]
# SOL: 2
#         c = Counter(nums)
#         for i in c:
#             if c[i] > 1: 
#                 return i 
# SOL: 3
        dic = {}
        for i in range(len(nums)): 
            if nums[i] in dic:
                return nums[i]
            dic[nums[i]] = i 
