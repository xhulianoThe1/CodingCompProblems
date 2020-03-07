#Expensive time and space solution
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr = []
        arr3 = []
        for i in range(len(arr2)):
            for k in range(len(arr1)):
                if arr2[i] == arr1[k]: 
                    arr.append(arr2[i])
        for j in arr1:
            if j not in arr2: 
                arr3.append(j)
        return arr+sorted(arr3)
