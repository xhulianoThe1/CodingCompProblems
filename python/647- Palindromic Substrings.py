class Solution(object):
    def countSubstrings(self, s):
        c = 0 
        for i in range(len(s)): 
            k = 1
            while i + k  < len(s): 
                if (s[i:i + k + 1] == s[i:i + k + 1:][::-1]): 
                    c += 1 
                k += 1  
        return c + len(s)
