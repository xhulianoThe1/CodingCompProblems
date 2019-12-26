## First solution ###
class Solution(object):
    def containsDuplicate(self, nums):
        nums = sorted(nums)
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]: 
                return True 
            i+=1
        return False

 ## Second Solution ##
class Solution(object):
    def containsDuplicate(self, nums):
        arr = set()
        for i in nums: 
            if i in arr:
                return True 
            else: 
                arr.add(i)
        return False

### Third Solution ###
import collections 
class Solution(object):
    def containsDuplicate(self, nums):
        for i in collections.Counter(nums).values(): 
            if i > 1: 
                return True
        return False  
