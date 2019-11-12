from collections import Counter 
class Solution(object):
    def uniqueOccurrences(self, arr):
        q = Counter(arr).values()
        b = set(Counter(arr).values())
        return len(q) == len(b) 
