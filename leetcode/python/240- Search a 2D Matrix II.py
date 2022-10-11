class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):   
            k = 0 
            while k < len(matrix[i]): 
                if matrix[i][k] == target:
                    return True
                elif matrix[i][k] > target: 
                    break
                k+=1
        return False
