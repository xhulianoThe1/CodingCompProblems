class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones = sorted(stones)
            if stones[-1] == stones[-2]: 
                stones = stones[:-2]
            else: 
                stones[-2] = stones[-1] - stones[-2]
                del stones[-1]
        if len(stones) == 1: 
            return stones[0]
        else: 
            return 0 
