def has_three_sum(A: List[int], t: int) -> bool:
    dic = {}
    for i, i_val in enumerate(A):
        dic[i_val] = i
        for k, k_val in enumerate(A):
            eq = t-i_val-k_val
            if eq in dic: 
                return True
    return False
