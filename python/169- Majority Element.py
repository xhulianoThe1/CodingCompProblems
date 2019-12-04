"Basically finding the median aka the most occuring element in the list"

class Solution(object):
    def majorityElement(self, nums):
        nums.sort() 
        return nums[len(nums)//2]
        
        
        
        """Solution Two"""
# import collections
# class Solution(object):
#     def majorityElement(self, nums):
#         a = collections.Counter(nums)
#         print a.get
