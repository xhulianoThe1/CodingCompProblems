class Solution(object):
    def intersect(self, nums1, nums2):
        a = set(nums1) & set(nums2)
        res = []
        for i in a: 
            while i in nums1 and i in nums2: 
                res.append(i)
                nums1.remove(i)
                nums2.remove(i)
        return res
