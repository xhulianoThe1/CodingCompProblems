n = int(input())  
arr = list(map(int, input().split()) ) 
c = 0 
k = arr[0]
for i in range(len(arr)): 
    if arr[i] - k < 0: 
        c = c + (k - arr[i] )
        arr[i] = k
    k = arr[i]
print(c)