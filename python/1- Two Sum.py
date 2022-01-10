class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for index, val in enumerate(nums): 
            if (target - val) in dict:  
                return (index, dict[target-val])
            dict[val] = index
        return 0
        
        
