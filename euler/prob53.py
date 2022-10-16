import math
from math import factorial

ans = 0
for n in range(23, 101):
    for r in range(2, n):
        comb = (factorial(n)) / (factorial(r) * factorial((n - r)))
        if comb > 10**6:
            ans += 1
print(ans)