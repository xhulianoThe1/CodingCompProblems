""Using counter ""

import collections 
class Solution(object):
    def repeatedNTimes(self, A):
        n = len(A) /2
        a = collections.Counter(A)
        for i in range(len(a)): 
            if a.values()[i] == n: 
                return a.keys()[i]
                
 
