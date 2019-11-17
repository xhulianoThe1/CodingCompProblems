import collections 
class Solution(object):
    def findTheDifference(self, s, t):
        a = collections.Counter(s)
        b = collections.Counter(t)
        for x in b: 
            if b[x] != a[x]: 
                return x
