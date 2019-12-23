class Solution(object):
    def subtractProductAndSum(self, n):
        a =  [x for x in str(n)]   
        prod = 1 
        s = 0
        for i in a: 
            prod *= int(i) 
            s += int(i) 
        return prod - s
