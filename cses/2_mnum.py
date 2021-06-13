n = int(input()) 
line2 = sorted([int(x) for x in input().split()]) 
arr = [i for i in range(1, n+1)]
print(list(set(arr) - set(line2))[0]) 