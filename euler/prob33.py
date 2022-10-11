import math 
num, dem = 1,1 
for i in range(10, 100): 
    for k in range(i+1, 100):
        try: 
            if i/k == int(str(i)[0])/int(str(k)[1]) and int(str(i)[1]) == int(str(k)[0]): 
                num *= i 
                dem *= k 
        except: 
            pass 
dem /= math.gcd(num, dem)
print(int(dem)) 
