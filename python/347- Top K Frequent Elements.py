import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        a = collections.Counter(nums).most_common()
        i, arr = 0, []  
        while i < k: 
            arr.append(a[i][0]) 
            i+= 1
        return arr
