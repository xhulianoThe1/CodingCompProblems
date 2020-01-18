import collections 
class Solution(object):
    def rotate(self, nums, k):
        a = collections.deque(nums)
        i = 1
        while i <= k: 
            b = a.pop() 
            a.appendleft(b)
            i+=1 
        nums[:] = list(a)
