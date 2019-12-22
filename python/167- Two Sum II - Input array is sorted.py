class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        k = len(numbers)-1
        while i < k: 
            if numbers[i] + numbers[k] == target: 
                return [i+1, k+1]
            elif numbers[i] + numbers[k] > target: 
                k-=1 
            else: 
                i +=1 
        return []
