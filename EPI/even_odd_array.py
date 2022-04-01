#Problem 5.00 

def even_odd(A: List[int]) -> None:
    l_pointer = 0
    r_pointer = len(A)-1 
    
    while l_pointer <= r_pointer:
        if A[l_pointer] %2 != 0 and A[r_pointer] %2 ==0: 
            A[l_pointer], A[r_pointer] = A[r_pointer], A[l_pointer]
        elif A[l_pointer] % 2 == 0: 
            l_pointer += 1 
        elif A[l_pointer] %2 != 0 and A[r_pointer] %2 !=0: 
            r_pointer -= 1
