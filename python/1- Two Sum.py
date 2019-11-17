class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        #Use enumerate as a way to index 
        for index, val in enumerate(nums): 
            if (target - val) in dict: 
                #if this holds true we return the indexes 
                return (index, dict[target-val])
            dict[val] = index
        #error handling
        return 0
        
        
