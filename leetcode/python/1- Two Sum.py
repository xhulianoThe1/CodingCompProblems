class Solution(object):
    def twoSum(self, nums, target):
        dic = {}        
        for idx, val in enumerate(nums): 
            if target - val in dic and idx != dic[target-val]: 
                return idx, dic[target-val]
            dic[val] = idx
