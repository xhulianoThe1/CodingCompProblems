class Solution(object):
    def isPowerOfThree(self, n):
        #base cases 
        if n < 1: 
            return False
        elif n == 1: 
            return True  
        i = 1
        while i < n: 
            i *= 3
            if i == n: 
                return True 
        return False
