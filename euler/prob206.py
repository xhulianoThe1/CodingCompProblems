arr = [1, "", 2, "", 3, "", 4, "", 5, "", 6, "", 7, "", 8, "", 9, "", 0]
for i in range(10**9, 10**10, 10): 
    li = list(map(int, str(i**2)))
    if li[0] == 1 and li[-1] == 0: 
        if li[::2] == arr[::2] and len(li) == len(arr): 
            return i
