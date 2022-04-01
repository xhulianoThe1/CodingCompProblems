def fibonacci(n: int) -> int:    
    if n == 0: 
        return 0 
    if n == 1 or n == 2: 
        return 1 
    prev = 1 
    curr = 2 
    for i in range(3, n): 
        temp = curr 
        curr += prev 
        prev = temp 
    return curr 
