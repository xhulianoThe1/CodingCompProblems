#Solution 1 
class Solution(object):
    def numJewelsInStones(self, J, S):
        dic = {} 
        c = 0 
        for i in range(len(J)): 
            dic[J[i]] = i
        for i in range(len(S)): 
            if S[i] in dic: 
                c += 1 
        return c 
