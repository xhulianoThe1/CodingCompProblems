#Problem 4.08

def reverse(x: int) -> int:
    t_f = False
    if x < 0: 
        t_f = True
        x *= -1 
        
    l_x = len(str(x))
    ans = ""
    i=0 
    while i < l_x: 
        ans += str(x % 10) 
        x = x//10 
        i +=1 
    if t_f == True:
        return int(ans)*-1
    return int(ans)
        



#Solution 2 
def reverse(x: int) -> int:
    #Extra space solution 
    str_x = str(x)[::-1]
    ans = ""
    for i in str_x:
        if i == '-': 
            return int(ans)*-1
        else: 
            ans += i 
    return int(ans)
