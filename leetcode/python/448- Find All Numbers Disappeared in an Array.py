#Solution 1 
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = {} 
        for i, val in enumerate(nums): 
            dic[val] = i 
        return [i for i in range(1,len(nums)+1) if i not in dic]
      
#Solution 2 
from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        return [i for i in range(1,len(nums)+1) if i not in dic]
