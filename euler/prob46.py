from sympy import sieve


def out(tot=10**6 + 1):
    ans = 0
    prime = list(sieve.primerange(1, 9))
    dic = {}
    for i in range(1, tot):
        dic[2 * (i**2)] = i
    for i in range(9, tot, 2):
        prime.extend(list(sieve.primerange(prime[-1] + 1, i + 1)))
        if i not in prime:
            t = False
            for k in reversed(prime):
                if (i - k) in dic:
                    t = True
                    break
            if t != True:
                print(f'answer: {i}')
                return i
