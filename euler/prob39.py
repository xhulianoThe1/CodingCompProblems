def func(x):
    dic = {}
    for idx in range(int(x ** 0.5), x // 2):
        dic[idx ** 2] = idx
    c = 0
    for i in range(int(x ** 0.5), x // 2):
        for j in range(i + 1, x // 2):
            if (i ** 2 + j ** 2) in dic and (i + j + dic[(i ** 2 + j ** 2)]) == x:
                c += 1
    return c


maxx = 3
ans = 120
for i in range(121, 1001):
    trip = func(i)
    if trip > maxx:
        maxx = trip
        ans = i
print(ans)
