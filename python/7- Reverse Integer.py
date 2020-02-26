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
