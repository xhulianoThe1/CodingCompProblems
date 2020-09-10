from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dic = Counter(magazine)
        for i in range(len(ransomNote)):
            if dic[ransomNote[i]] <= 0: 
                return False 
            dic[ransomNote[i]] -= 1 
        return True 
