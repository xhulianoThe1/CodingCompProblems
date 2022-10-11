import math 
arr =[]
for i in range(1, 10**6): 
  s = 0 
  for k in str(i): 
    s+= math.factorial(int(k)) 
    # print(int(k)**4) 
  if s == i: 
    arr.append(i)
print(arr)
print(sum(arr)) 
