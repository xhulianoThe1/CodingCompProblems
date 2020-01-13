class Solution(object):
    def maxArea(self, height):
        i = 0 
        k = len(height)-1 
        arr = [] 
        while i < k: 
            if height[i] <= height[k]: 
                arr.append(height[i]* ((-1*k) + i)) 
                i+=1
            else: 
                arr.append(height[k]* ((-1*k) + i)) 
                k-=1 
        return min(arr)*-1     
