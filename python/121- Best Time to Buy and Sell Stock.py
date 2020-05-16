#SOLUTION #1 
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
                

#SOLUTION 2 
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        profit = 0 
        m = prices[0]
        for i in range(len(prices)): 
            m = min(m, prices[i]) 
            if prices[i] - m > profit: 
                profit = prices[i] - m 
        return profit 
