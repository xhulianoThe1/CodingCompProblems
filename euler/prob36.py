c = 0
for i in range(10 ** 6):
    a = str(i)
    b = bin(i).split("b")[-1]
    if a == a[::-1] and b == b[::-1]:
        c += i
print(c)
