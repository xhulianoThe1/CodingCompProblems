class Solution(object):
    def tribonacci(self, n):
        if n == 0: 
            return 0
        elif n == 1 or n == 2: 
            return 1
        b = [None]*(n + 1)
        b[0] = 0
        b[1] = 1
        b[2] = 1
        for i in range(3, n+1):    
            b[i] = b[i-1] + b[i-2] + b[i-3]
        return b[i]
