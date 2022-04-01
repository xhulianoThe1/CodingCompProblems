#Problem 4.08

def reverse(x: int) -> int:
    str_x = str(x)[::-1]
    ans = ""
    for i in str_x:
        if i == '-': 
            return int(ans)*-1
        else: 
            ans += i 
    return int(ans)
