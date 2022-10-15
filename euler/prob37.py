##SOLUTION 1

from sympy import sieve
import multiprocess as mp


def prime(x):
    if len(list(sieve.primerange(x, x + 1))) == 0:
        return False
    return True


ans = []
for i in range(11, 10 ** 6, 2):
    yes = True
    inp = str(i)
    inp_l = len(inp)
    for x in inp:
        a = inp[:inp_l]
        b = inp[inp_l - len(inp) :]
        if prime(int(a)) == False or prime(int(b)) == False:
            yes = False
        inp_l -= 1
    if yes == True:
        ans.append(i)
    yes = True
    if len(ans) == 11:
        break
n_threads = 4
pool = mp.Pool
with pool(n_threads) as p:
    results = p.map(prime, ans)
print(ans)
print(sum(ans))
