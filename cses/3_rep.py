dna = input()
k = 'A'
ans, c  = 0, 0 
for i in range(len(dna)): 
    if k == dna[i]:  
        c += 1 
    else: 
        k = dna[i]
        c = 1  
    ans = max(ans, c) 
print(ans)