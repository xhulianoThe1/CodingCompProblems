class Solution(object):
    def duplicateZeros(self, arr): 
        ans = []
        i = 0
        while i < len(arr):
            ans.append(arr[i])
            if arr[i] == 0: 
                ans.append(0)
            i+=1
        for i in range(len(arr)): 
            arr[i] = ans[i]
        print arr
