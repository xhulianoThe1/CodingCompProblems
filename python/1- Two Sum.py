#Solution 1 
class Solution(object):
    def twoSum(self, nums, target):
        dic = {} 
        for i in range(len(nums)): 
            dic[nums[i]] = i 
        for i in range(len(nums)): 
            if target - nums[i] in dic and i != dic[target - nums[i]]: 
                return [i, dic[target - nums[i]]] 


#Solution 2 
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for index, val in enumerate(nums): 
            if (target - val) in dict:  
                return (index, dict[target-val])
            dict[val] = index
        return 0
        
        
