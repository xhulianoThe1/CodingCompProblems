import collections 
class Solution(object):
    def singleNumber(self, nums):
        a, b = collections.Counter(nums).values(), collections.Counter(nums).keys() 
        arr = []
        for i in range(len(a)): 
            if a[i] == 1: 
                arr.append(b[i])
        return arr
