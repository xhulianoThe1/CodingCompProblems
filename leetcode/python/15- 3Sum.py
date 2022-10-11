class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        s = set()        
        for i, i_val in enumerate(nums): 
            for k, k_val in enumerate(nums): 
                eq = (-1*i_val) + (-1*k_val)
                if eq in dic and (i!=k) and (i!=dic[eq]) and k != dic[eq]: 
                    s.add(tuple(sorted([i_val, k_val, eq]))) 
            dic[(i_val)] = i
        return s
