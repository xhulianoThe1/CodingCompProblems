########Problem 92- Solution 1########
def func(x):
    return sum(list(map(lambda num: num**2, list(map(int, str(x))))))


c = 0
for i in range(10**7):
    k = 0
    num = i
    while k < 20:
        if func(num) == 89:
            c += 1
            break
        elif num == 1:
            break
        num = func(num)
        k += 1
print(c)


########Problem 92- Solution 2########
from multiprocess import Pool

ans = []
C1 = [0, 10**6]
C2 = [10**6, 10**6 * 5]
C3 = [10**6 * 5, 10**7]


def output(lower, upper):
    c = 0
    for i in range(lower, upper):
        k = 0
        num = i
        while k < 20:
            if func(num) == 89:
                c += 1
                break
            elif num == 1:
                break
            num = func(num)
            k += 1
    print(c)
    ans.append(c)

def f(li):
    return output(li[0], li[1])

if __name__ == '__main__':
    with Pool(4) as pool:
        print(pool.map(f, [C1, C2, C3]))
    print(f"the final answer is {sum(ans)}")
