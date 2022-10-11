import collections
class Solution(object):
    def firstUniqChar(self, s):
        s2 = collections.Counter(s).most_common()
        a = ""
        for i in range(len(s2)):
            if s2[i][1] == 1:
                a += s2[i][0]
        for i in range(len(s)):
            if s[i] in a: 
                return i
        else:
            return -1 
