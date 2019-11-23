class Solution(object):
    def maxProfit(self, prices):
        if prices == []:
            return 0
        min = prices[0]
        ans = 0 
        for i in prices: 
            if i < min: 
                min = i
            ans = max(ans, i-min)
        return ans
                
