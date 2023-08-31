def div(n): 
    divisors = []
    for i in range(1, n): 
        if n % i == 0: 
            divisors.append(i)
    return divisors


abudant = []
for k in range(1, 28124):
    tmp = sum(div(k))
    if tmp > k: 
        abudant.append(k)
        
        
out = []
for x in range(24, 28124): #
    flag = 0 
    for z in abudant:
        if (x - z) in abudant: 
            flag = 1
        if flag == 1: 
            break
    if flag == 0: 
        out.append(x)

sum(out)+sum([x for x in range(24)])
