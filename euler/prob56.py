########Problem 56- Solution 1########
high_c = 0
for a in range(1, 100): 
    for b in range(1, 100): 
        dig, c = str(a**b), 0
        for z in dig: 
            c += int(z)
        if c > high_c: 
            high_c = c

print(f"answer: {high_c}")

########Problem 56- Solution 2########
def func(x): 
    return sum(map(int, str(x)))
high_c = 0 
for a in range(100): 
    for b in range(100): 
        if func(a**b) > high_c: 
            high_c = func(a**b)
print(f"answer: {high_c}")
