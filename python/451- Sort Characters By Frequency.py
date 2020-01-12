import collections 
class Solution(object):
    def frequencySort(self, s):
        arr =  collections.Counter(s).most_common() 
        st = ""
        for i in range(len(arr)): 
            k = 0 
            while k < arr[i][1]: 
                st += str(arr[i][0]) 
                k += 1
        return st
