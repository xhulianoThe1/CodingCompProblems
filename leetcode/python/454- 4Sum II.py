class Solution(object):
    def fourSumCount(self, A, B, C, D):
        dic1 = {} 
        c = 0
        for i in range(len(A)): 
            for k in range(len(A)): 
                sumAB = A[i] + B[k]
                if sumAB in dic1: 
                    dic1[sumAB] += 1 
                else: 
                    dic1[sumAB] = 1 
        for x in range(len(A)): 
            for y in range(len(A)): 
                sumCD = C[x] + D[y]
                if -(sumCD) in dic1: 
                    c+= dic1[-sumCD]
        return c
