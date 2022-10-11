import itertools 
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation = itertools.permutations(l) 
arr = [] 
for i in list(permutation): 
    arr.append(i)
print(arr[1000000])
