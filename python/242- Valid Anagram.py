#Solution 1
class Solution(object):
    def isAnagram(self, s, t):
        dic = {}
        dic2 = {} 
        for i in s: 
            dic[i]= dic.get(i, 0) + 1        
        for k in t: 
            dic2[k] = dic2.get(k, 0) + 1
        return dic == dic2
      
# Solution 2 
class Solution(object):
	def isAnagram(self, s, t):
		sorted(s) == sorted(t) 

#Solution 3 
from collections import defaultdict 
class Solution(object):
    def isAnagram(self, s, t):
        dic = defaultdict(int)
        for i in s:
            dic[i] +=1 
        for i in t: 
            dic[i] -= 1 
        if max(dic.values()) > 0 or min(dic.values()) < 0: 
            return False
        return True
	##Can also do the following: 
        # for i in dic.values():
        #     if i != 0: 
        #         return False 
        # return True
