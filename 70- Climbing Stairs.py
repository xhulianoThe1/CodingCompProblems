class Solution(object):
    def climbStairs(self, n):
        if n == 0 or n == 1: 
            ans = 1
            return ans 
        b = [None] * (n+1)
        b[0] = 1
        b[1] = 1
        for i in range(2, n + 1):
            b[i] = b[i-1] + b[i-2]
            ans = b[i]
        return ans
