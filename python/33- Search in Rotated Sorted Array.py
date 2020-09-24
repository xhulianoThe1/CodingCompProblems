class Solution(object):
    def search(self, nums, target):
        dic = {}
        for i in range(len(nums)): 
            dic[nums[i]] = i 
            if target in dic: 
                return i 
        return -1 
