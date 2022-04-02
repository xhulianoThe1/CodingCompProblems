class Solution:
    def reverseBits(self, n: int) -> int:
        rev = bin(n)[2:][::-1]
        ans = rev + ('0'*(32-len(rev))) 
        return int(ans, 2)
