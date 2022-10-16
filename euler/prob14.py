def func(n): 
    c = 1
    for i in range(n): 
        if n == 1: 
            break 
        if n % 2 == 0: 
            n /= 2 
            c+=1 
        else: 
            n = 3*n+1
            c+=1 
    return c

maxx = 10 
ans = 13 
for i in range(13, 10**6): 
    if func(i) > maxx: 
        maxx = func(i)
        ans = i 
print(ans)