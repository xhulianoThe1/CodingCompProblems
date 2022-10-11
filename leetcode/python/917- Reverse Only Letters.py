class Solution(object):
    def reverseOnlyLetters(self, S):
        arr, res = [], [] 
        for i in S: 
            if i.isalpha(): 
                arr.append(i)
        for k in S: 
            if k.isalpha(): 
                res.append(arr.pop())
            else: 
                res.append(k)
        return "".join(res)
