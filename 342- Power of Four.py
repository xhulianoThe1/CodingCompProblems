class Solution(object):
    def isPowerOfFour(self, num):
        if num <= 0: 
            return False
        if num == 1:
            return True
        k = 1
        while k < num:
            k *= 4
            if k == num: 
                return True 
        return False

