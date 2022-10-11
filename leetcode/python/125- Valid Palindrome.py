class Solution(object):
    def isPalindrome(self, s):
        ans = ""
        for i in s.lower(): 
            if i.isalpha() == True or i.isnumeric()==True: 
                ans += i 
        return ans[::-1] == ans
