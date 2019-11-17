class Solution(object):
    def baseNeg2(self, N):
        arr = []
        base = -2
        if N == 0:
            return "0"
        while N != 0:
            N, remainder = divmod(N, base)
            if remainder < 0:
                N += 1
                remainder -= base
            arr.append(remainder)
        return "".join(map(str, arr[::-1]))
        
