def buy_and_sell_stock_once(prices: List[float]) -> float:
    least_val = prices[0]
    ans = 0 
    for i in prices:
      #least_val = min(least_val, i) also works :) 
        if i < least_val: 
            least_val = i
        ans = max(ans, i - least_val)
    return ans

            
    #O(N^2) solution 
    # ans = 0 
    # for i in range(len(prices)): 
    #     for k in range(i+1, len(prices)): 
    #         ans = max(ans, prices[k] - prices[i])
    # return ans    
        
