class Solution(object):
    def sortedSquares(self, A):
        res = [] 
        for i in A: 
            res.append(i**2)
        return sorted(res)
