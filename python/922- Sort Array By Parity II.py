class Solution(object):
    def sortArrayByParityII(self, A):
        arr = [i for i in A if i % 2 == 0]
        arr2 = [i for i in A if i % 2 != 0]        
        arr3 = [] 
        k = 0
        while k < len(arr):
            arr3.append(arr[k])
            arr3.append(arr2[k])
            k+=1
        return arr3
