# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    if n == 1: 
        return []
    
    ans = [] 
    for i in range(2, n+1): 
        t_f = True 
        for k in range(2, int(i**(1/2))+1): 
            if i % k == 0: 
                t_f = False 
                break
        if t_f == True: 
            ans.append(i)
    return ans
