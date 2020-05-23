class Solution(object):
    def threeSum(self, nums):
        s = set()
        dic = {}
        nums.sort()
        for i in range(len(nums)): 
            dic[nums[i]] = i 
        for i in range(len(nums)):  
            for k in range(i+1, len(nums)): 
                target = -(nums[i] + nums[k])
                if target in dic and dic[target] > k: 
                    s.add((nums[i], nums[k], target))
        return s
