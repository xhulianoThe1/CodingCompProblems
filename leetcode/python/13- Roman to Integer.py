class Solution(object):
    def romanToInt(self, s):
        d = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500,
            "M": 1000
        }
        c = 0
        for i in range(len(s)-1):
            curr = d[s[i]]
            nxt = d[s[i+1]]
            if nxt > curr: 
                c -= curr
            else: 
                c+= curr
        return c +  d[s[-1]]
