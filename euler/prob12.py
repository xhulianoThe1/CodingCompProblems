i = 1
a = 1 
# arr = [] 
while i < float('inf') : 
  i += a 
  a+=1 
  i+=1 
  c = 0 
  for k in range(1, i): 
    if i%k == 0: 
      c+=1
  
  if c == 501: 
    print(i)
    break 
