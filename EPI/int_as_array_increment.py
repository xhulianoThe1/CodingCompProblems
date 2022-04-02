def plus_one(A: List[int]) -> List[int]:
    # naive one line solution 
    return [int(i) for i in str(int(''.join(list(map(str, A)))) + 1 )]
  
  def plus_one(A: List[int]) -> List[int]:
    #Kind of better solution but still not as clean
    #as the one in the book :) 
    if A[0] == 9 and len(A) ==1:
        return [1, 0]
   
    for i in reversed(range(len(A))): 
        if A[i] == 9 and A[i-1] != 9: 
            A[i] = 0 
            A[i-1] +=1 
            break 
        elif A[i] !=10 and A[i] != 9: 
            A[i] +=1 
            break 
        elif A[i] ==10 and i!= 0 and A[i-1] != 9: 
            A[i] = 0 
            A[i-1] += 1
            break 
        elif A[i] == 10 and i == 0:
            A[i] = 0 
            A.insert(0, 1)
            break 
        elif A[i] == 9: 
            A[i] = 0 
            A[i-1] +=1 
        elif A[i] ==10 and i!= 0 and A[i-1] == 9: 
            A[i] = 0 
            A[i-1] += 1
    return A
