class Solution(object):
    def reverse(self, x):
        s = ""
        for i in reversed(str(x)):
            s+=i
        else: 
            if s[-1] == '-':
                s = s[:-1]
                if int(s) > (2**31)-1 or int(s) < (-2**31)-1:
                    return 0 
                else:
                    return int(s)*-1
            else:
                if int(s) > (2**31)-1 or int(s) < (-2**31)-1:
                    return 0 
                else:
                    return int(s)
#SOlution 2 
class Solution(object):
    def reverse(self, x):
        res = 0
        s = abs(x) 
        while s != 0:
            res *= 10 
            res += s % 10 
            s /= 10 
        if res > (2**31)-1 or res < (-2**31)-1: 
            return 0 
        elif x < 0: 
            return res *-1
        elif x >= 0:
            return res 
