import collections 
class Solution(object):
    def uncommonFromSentences(self, A, B):
        C = collections.Counter(A.split(" "))  + collections.Counter(B.split(" "))
        arr = []
        for i in C: 
            if C[i] == 1:
                arr.append(i)
        return arr
