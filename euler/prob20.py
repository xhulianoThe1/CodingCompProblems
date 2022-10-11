def factorial(n): 
  if n == 0 or n== 1: 
    return 1 
  else: 
    return n* factorial(n-1)
a, sum = factorial(100), 0  
for i in str(a): 
  sum += int(i)    
print(sum)  
