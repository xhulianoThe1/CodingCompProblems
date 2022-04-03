def reverse_bits(x: int) -> int:
    rev = bin(x)[2:][::-1]
    ans = rev + ('0'*(64-len(rev))) 
    return int(ans, 2)
