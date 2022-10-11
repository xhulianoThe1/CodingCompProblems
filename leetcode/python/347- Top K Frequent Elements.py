#Solution 1 
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums).most_common()
        ans = []
        for i in dic: 
            if k!= 0:
                ans.append(i[0])
            else: 
                break 
            k-=1
        return ans

 #Solution 2 without calling most_common() 
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        ans = []
        s_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        for i in s_list: 
            if k!= 0: 
                ans.append(i[0])
            else: 
                break 
            k-=1
        return ans
