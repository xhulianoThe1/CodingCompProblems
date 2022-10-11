#SOLUTION #1 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_val = prices[0]
        ans = 0 
        for i in prices:
            if i < least_val: 
                least_val = i
            ans = max(ans, i - least_val)
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
