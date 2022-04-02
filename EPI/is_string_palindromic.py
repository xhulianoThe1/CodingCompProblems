def is_palindromic(s: str) -> bool:
    #Pythonic solution but w/ extra space 
    # return s == s[::-1]

    #2 pointer solution. No extra space 
    l = 0 
    r = len(s)-1
    while l <= r: 
        if s[l] != s[r]:
            return False
        l +=1 
        r -=1 
    return True
