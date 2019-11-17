class Solution:
    def sortArrayByParity(self, A):
        arr = [] 
        arr2 = []
        for i in range(len(A)): 
            if (A[i] % 2 == 0): 
                arr.append(A[i])
        for i in range (len(A)): 
            if (A[i] % 2 != 0): 
                arr.append(A[i])
        return arr 
