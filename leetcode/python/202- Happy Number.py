class Solution(object):
    def isHappy(self, n):
        c = 0 
        s = set()
        n = str(n)
        while c != 1:  
                for i in n: 
                    c += int(i)**2
                if c == 1:
                    return True 
                elif c in s: 
                    return False 
                else: 
                    s.add(c)
                    n = str(c)
                    c = 0 
