class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return (x == x[::-1])
  
#Solution without converting to int 
class Solution(object):
    def isPalindrome(self, x):
        res = 0 
        s = abs(x)
        while s!= 0: 
            res*=10
            res += s % 10 
            s /= 10 
        return res == x
