class Solution(object):
    def maxProfit(self, prices):
        if prices == []:
            return 0
        min = prices[0]
        ans = 0 
        arr = [] 
        for i in range(len(prices)): 
            if prices[i] < min: 
                #the new min is i 
                min = prices[i]
            arr.append(prices[i]-min)
            min = prices[i]
        return sum(arr)
