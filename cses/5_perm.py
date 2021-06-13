def main():
    n = int(input()) 
    ans = [] 
    if n <= 3 and n > 1:  
        print('NO SOLUTION') 
    else: 
        for i in range(1, n+1) : 
            if i % 2 == 0: 
                ans.append(i)
        for i in range(1, n+1) : 
            if i % 2 != 0: 
                ans.append(i)
        for i in ans:
            print(i, end = ' ')
if __name__=="__main__":
    main()