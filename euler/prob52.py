for i in range(125873, 10**9): 
  if sorted(str(i*2)) == sorted(str(i*3)) == sorted(str(i*4)) == sorted(str(i*5)) == sorted(str(i*6)): 
    print(i) 
    break
