class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = 0
        total = 0
        b = 0
        tot = 0
        for i in reversed(arr1): 
            if(i == 1): 
                c += (-2)**total
            total+=1
        for k in reversed(arr2): 
            if(k == 1):
                b += (-2)**tot
            tot += 1
        sum = b + c
        print(sum)
        out = []
        n = sum
        b  = -2
        if n == 0:
            return "0"
        while n != 0:
            n, rem = divmod(n, b)
            if rem < 0:
                n += 1
                rem -= b
            out.append(rem)
        return "".join(map(str, out[::-1]))       
