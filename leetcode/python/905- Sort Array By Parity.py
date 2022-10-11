#Solution One 
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

    
#solution Two 
import collections 
class Solution(object):
    def sortArrayByParity(self, A):
        de = collections.deque([])
        for i in A: 
            if i % 2 == 0:
                de.appendleft(i)
            else:
                de.append(i)
        return de 
