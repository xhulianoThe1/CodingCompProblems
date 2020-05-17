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
