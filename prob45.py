d = {} 
d2 = {} 
for i in range(144, 10**5): 
    tri =  int(i*(i+1)/2) 
    pent = int(i*(3*i-1)/2) 
    hexa = int(i*(2*i-1))
    d[hexa] = i 
    d2[pent] = i 
    if tri in d and tri in d2:
        print(tri)
        break
