def fib(n):
  if n == 1 or n==2: 
    return 1 
  a = [None]*(n+1)
  a[1] = 1
  a[2] = 1 
  for i in range(3, n+1): 
    a[i] = a[i-1] + a[i-2]
  return len(str(a[n]))
def test(): 
  n =1000
  while n < 400000: 
    if fib(n) == 1000: 
      print(n)
      break
    else: 
      n+= 1
