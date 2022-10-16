i, k = 1, 1
counter, ans = 0, 0
while i < 1001 * 1001 + 1:
    if counter == 4:
        k += 1
        counter = 0
    counter += 1
    ans += i
    i += 2 * k
print(ans)
