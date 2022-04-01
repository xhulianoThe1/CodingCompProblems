#Problem 5.05 in EPI 

# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    l = 0 
    r = 1 
    tot = len(A) -1 
    while r <= tot: 
        if A[l] == A[r]: 
            del A[r]
            tot -= 1 
        elif A[l] != A[r]: 
            l +=1 
            r +=1 
