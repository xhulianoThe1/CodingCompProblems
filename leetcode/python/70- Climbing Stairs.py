#Solution 1 
class Solution(object):
    def climbStairs(self, n):
        if n <= 1: 
            return 1  
        prev = 1
        curr = 2 
        for i in range(2, n): 
            temp = curr
            curr += prev
            prev = temp
        return curr
    
#Solution 2 
class Solution(object):
    def climbStairs(self, n):
        if n == 0 or n == 1: 
            return 1 
        b = [None] * (n+1)
        b[0] = 1
        b[1] = 1
        for i in range(2, n + 1):
            b[i] = b[i-1] + b[i-2]
            ans = b[i]
        return ans
