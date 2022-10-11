from collections import Counter
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [Counter(bin(i).split('b')[-1])['1'] for i in range(n+1)]
