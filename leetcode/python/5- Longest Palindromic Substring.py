class Solution(object):
    def longestPalindrome(self, s):
        if s== s[::-1]: 
            return s 
        arr = [] 
        for i in range(len(s)): 
            k = 1
            while i + k  < len(s): 
                if s[i] == s[i + k]: 
                    arr.append(s[i:i + k + 1])
                k += 1 
        maxx = 0 
        res = ''
        for i in range(len(arr)): 
            if arr[i] == arr[i][::-1] and len(arr[i]) > maxx: 
                maxx = len(arr[i])
                res = arr[i]
        if res == "":
            return s[0]
        return res
