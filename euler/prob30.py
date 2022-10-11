arr =[]
for i in range(10, 10**6): 
  s = 0 
  for k in str(i): 
    s+= int(k)**5
    # print(int(k)**4) 
  if s == i: 
    arr.append(i)
print(sum(arr)) 
